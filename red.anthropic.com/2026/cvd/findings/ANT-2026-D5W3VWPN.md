<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-D5W3VWPN -->

# ANT-2026-D5W3VWPN · freerdp/freerdp

## heap-buffer-overflow high

[CVE-2026-68579](https://nvd.nist.gov/vuln/detail/CVE-2026-68579)
[GHSA-m37j-jcr2-8gcc](https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-m37j-jcr2-8gcc)

Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-D5W3VWPN: Windows clipboard stream read ignores caller buffer size

The Windows FreeRDP client's IStream::Read implementation for remote clipboard files (CliprdrStream\_Read, wf\_cliprdr.c:249) calls CopyMemory(pv, clipboard->req\_fdata, clipboard->req\_fsize) where req\_fsize is taken directly from the server's CLIPRDR\_FILE\_CONTENTS\_RESPONSE (wf\_cliprdr.c:2449, cliprdr\_common.c:377) and never compared to the caller's buffer size cb before the copy. The resulting IStream is handed to arbitrary paste consumers (e.g., explorer.exe) via OleSetClipboard and IDataObject::GetData. A malicious RDP server can answer a small FILECONTENTS\_RANGE read with an arbitrarily large payload, and the client memcpy()s the entire attacker-controlled payload into the consumer's fixed-size buffer. This yields a scope-changing heap overflow with attacker-controlled content in a process outside the RDP client, enabling code execution.

**Project:** freerdp/freerdp
**Location:** `client/Windows/wf_cliprdr.c:249`

req\_fsize is assigned directly from fileContentsResponse->cbRequested, which is derived from the server-sent PDU dataLen (response->cbRequested = response->common.dataLen - 4) with no validation or correlation to the original requested size. The only size comparison (req\_fsize < cb at wf\_cliprdr.c:256) runs after the CopyMemory and only handles short reads, so an oversized server response is copied in full before any check occurs.

1. Attacker's RDP server advertises CFSTR\_FILEDESCRIPTORW / CFSTR\_FILECONTENTS on the shared clipboard
2. Victim presses Ctrl+V in Explorer; Explorer obtains the IStream from FreeRDP's IDataObject and calls IStream::Read(pv, 0x1000, &read)
3. FreeRDP sends a FILECONTENTS\_RANGE request for 0x1000 bytes
4. Server replies with a CB\_FILECONTENTS\_RESPONSE carrying ~0x100000 bytes of attacker data
5. wf\_cliprdr\_server\_file\_contents\_response() sets req\_fsize=0x100000; CliprdrStream\_Read() CopyMemory()s 1 MiB into Explorer's 4 KiB buffer

## Suggested Fix

Clamp the bytes copied and reported in CliprdrStream\_Read to min(cb, server-returned size), and treat server responses larger than the requested range as a protocol error; retain the requested size from cliprdr\_send\_request\_filecontents() so it can be validated against the response.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-D5W3VWPN.

---

**Reference:** ANT-2026-D5W3VWPN

Triage and disclosure were performed by Ada Logics. The writeup below is the document the firm sent to the maintainer.

This issue was found using AI and agents, and has been reviewed manually.

This is a Windows-only issues, but I don't have access to a Window machine so did not create an end-to-end windows reproducer.
I left out a harness-based Linux reproducer to as I think auditing the code should be sufficient to identify the vulnerability. Let me know if you need more information from me and I will see if I can extract it.

## Summary

FreeRDP's Windows client exposes clipboard file contents to OLE paste consumers
(e.g. `explorer.exe`) through a COM `IStream`. When the consumer calls
`IStream::Read(pv, cb, …)` — `pv` is its own fixed-size buffer of `cb` bytes —
`CliprdrStream_Read()` asks the RDP server for the data via a
`CB_FILECONTENTS_RANGE` request, then copies the server's response into `pv` using
the **server-supplied length** (`req_fsize`), not `cb`:

```
CopyMemory(pv, clipboard->req_fdata, clipboard->req_fsize);   // length is server-controlled
```

A malicious or compromised RDP server answers the bounded request with an
arbitrarily large `CB_FILECONTENTS_RESPONSE`; `req_fsize` becomes the attacker's
chosen size and the copy overflows the consumer's buffer with attacker-controlled
content.

## Affected versions

* **FreeRDP `master`** — HEAD `5e8e987b469b60a3bafadf8f5afc40f91c09f458`,
  `client/Windows/wf_cliprdr.c:249` (`CliprdrStream_Read`): the copy still uses
  `clipboard->req_fsize` with no clamp to `cb`. Unpatched.
* **FreeRDP 3.x** — present in the released Windows client.
* Appears novel — no GHSA/CVE found for `CliprdrStream_Read` copying a
  server-controlled length.

## Details

All line numbers at `master` HEAD `5e8e987b`, `client/Windows/wf_cliprdr.c`.

```
// CliprdrStream_Read() :225
static HRESULT STDMETHODCALLTYPE CliprdrStream_Read(IStream* This, void* pv, ULONG cb,
                                                    ULONG* pcbRead)
    ...
    /* Ask the server for the file contents (bounded request of cb bytes). */
    ret = cliprdr_send_request_filecontents(clipboard, (void*)This, instance->m_lIndex,
                                            FILECONTENTS_RANGE, instance->m_lOffset.QuadPart, cb);
    if (ret < 0)
        return E_FAIL;

    if (clipboard->req_fdata)
        CopyMemory(pv, clipboard->req_fdata, clipboard->req_fsize);   // :249  cb is IGNORED
        free(clipboard->req_fdata);
    ...
```

`req_fsize` / `req_fdata` are set by the channel callback
`wf_cliprdr_server_file_contents_response()` directly from the server's
`CB_FILECONTENTS_RESPONSE` PDU (the `CopyMemory` of the server payload is around
`:2455`). Nothing constrains `req_fsize` to the `cb` the consumer passed, so the
copy at `:249` writes `req_fsize` bytes into a `cb`-byte buffer. `cb` is the size
the paste consumer requested (commonly a small, fixed value); `req_fsize` is
whatever the server put in the response.

**Reach:** OLE paste consumer → `IStream::Read` → `CliprdrStream_Read` →
`cliprdr_send_request_filecontents` (server round-trip) → `CopyMemory` overflow.

## Impact

A malicious/compromised RDP server overflows a fixed-size heap buffer in the OLE
paste consumer (e.g. `explorer.exe`) with attacker-controlled bytes when a user
pastes server-offered clipboard file contents — a classic attacker-content heap
overflow, in a process outside the RDP client.

## Suggested fix

Clamp the copy to the caller's buffer size, and report only what fits:

```
     if (clipboard->req_fdata)
-        CopyMemory(pv, clipboard->req_fdata, clipboard->req_fsize);
+        ULONG n = (clipboard->req_fsize < cb) ? clipboard->req_fsize : cb;
+        CopyMemory(pv, clipboard->req_fdata, n);
         free(clipboard->req_fdata);
-    *pcbRead = clipboard->req_fsize;
-    instance->m_lOffset.QuadPart += clipboard->req_fsize;
+    *pcbRead = n;
+    instance->m_lOffset.QuadPart += n;
```

(An `IStream::Read` must never write more than `cb` bytes into `pv`; a server
returning more than requested should be treated as a short read or an error.)

## References

* `client/Windows/wf_cliprdr.c` (master `5e8e987b`) — `CliprdrStream_Read`
  (`:225`, overflowing `CopyMemory` at `:249`), server file-contents response
  handler (`CopyMemory` of the server payload near `:2455`).
* CWE-787 (Out-of-bounds Write), CWE-120, CWE-130.

## Attribution

This issue was found using AI and agents, and has been reviewed manually. Please
credit **Claude** and **Ada Logics** — found by Anthropic using agents to study the
security of open-source projects, with Ada Logics validating and reporting. Let us
know if you need any more information.

## Disclosure

We follow coordinated disclosure policy here:
https://www.anthropic.com/coordinated-vulnerability-disclosure (90 day deadline).

```
diff --git a/client/Windows/wf_cliprdr.c b/client/Windows/wf_cliprdr.c
index 70895ba3999c..c0a6feea6f3d 100644
--- a/client/Windows/wf_cliprdr.c
+++ b/client/Windows/wf_cliprdr.c
@@ -225,25 +225,27 @@ static ULONG STDMETHODCALLTYPE CliprdrStream_Release(IStream* This)
 static HRESULT STDMETHODCALLTYPE CliprdrStream_Read(IStream* This, void* pv, ULONG cb,
                                                     ULONG* pcbRead)
-	int ret;
 	CliprdrStream* instance = (CliprdrStream*)This;
-	wfClipboard* clipboard;

 	if (!pv || !pcbRead || !instance)
 		return E_INVALIDARG;

-	clipboard = (wfClipboard*)instance->m_pData;
+	wfClipboard* clipboard = (wfClipboard*)instance->m_pData;
 	*pcbRead = 0;

 	if (instance->m_lOffset.QuadPart >= instance->m_lSize.QuadPart)
 		return S_FALSE;

-	ret = cliprdr_send_request_filecontents(clipboard, (void*)This, instance->m_lIndex,
-	                                        FILECONTENTS_RANGE, instance->m_lOffset.QuadPart, cb);
+	const int ret =
+	    cliprdr_send_request_filecontents(clipboard, (void*)This, instance->m_lIndex,
+	                                      FILECONTENTS_RANGE, instance->m_lOffset.QuadPart, cb);

 	if (ret < 0)
 		return E_FAIL;

+	if (clipboard->req_fsize > cb)
+		return E_FAIL;
+
 	if (clipboard->req_fdata)
 		CopyMemory(pv, clipboard->req_fdata, clipboard->req_fsize);
```

<https://github.com/FreeRDP/FreeRDP/commit/680426e58a986b6fd0f1c352624f813708fc3432>

1. 2026-04-02
2. 2026-07-16
3. 2026-07-22
4. 2026-07-22
5. 2026-09-28

94f4c703ec61699c8fd0ad4be74e234d085309ee2bb5837ca53b81cda8e86e1c3929d5ff789e4decaa75dca0af0433f6ba2a82a3f0d4299ddb8fd529d6f8a703

Committed 2026-07-22 07:29 UTC

Revealed 2026-09-28 21:38 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-D5W3VWPN%22%2C%22bug_class%22%3A%22Heap%20Buffer%20Overflow%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-16T01%3A52%3A39%2B00%3A00%22%2C%22description%22%3A%22The%20Windows%20FreeRDP%20client%27s%20IStream%3A%3ARead%20implementation%20for%20remote%20clipboard%20files%20%28CliprdrStream_Read%2C%20wf_cliprdr.c%3A249%29%20calls%20CopyMemory%28pv%2C%20clipboard-%3Ereq_fdata%2C%20clipboard-%3Ereq_fsize%29%20where%20req_fsize%20is%20taken%20directly%20from%20the%20server%27s%20CLIPRDR_FILE_CONTENTS_RESPONSE%20%28wf_cliprdr.c%3A2449%2C%20cliprdr_common.c%3A377%29%20and%20never%20compared%20to%20the%20caller%27s%20buffer%20size%20cb%20before%20the%20copy.%20The%20resulting%20IStream%20is%20handed%20to%20arbitrary%20paste%20consumers%20%28e.g.%2C%20explorer.exe%29%20via%20OleSetClipboard%20and%20IDataObject%3A%3AGetData.%20A%20malicious%20RDP%20server%20can%20answer%20a%20small%20FILECONTENTS_RANGE%20read%20with%20an%20arbitrarily%20large%20payload%2C%20and%20the%20client%20memcpy%28%29s%20the%20entire%20attacker-controlled%20payload%20into%20the%20consumer%27s%20fixed-size%20buffer.%20This%20yields%20a%20scope-changing%20heap%20overflow%20with%20attacker-controlled%20content%20in%20a%20process%20outside%20the%20RDP%20client%2C%20enabling%20code%20execution.%22%2C%22discovered_at%22%3A%222026-04-02T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22client/Windows/wf_cliprdr.c%3A249%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22freerdp/freerdp%22%2C%22reproduction%22%3A%5B%221.%20Attacker%27s%20RDP%20server%20advertises%20CFSTR_FILEDESCRIPTORW%20/%20CFSTR_FILECONTENTS%20on%20the%20shared%20clipboard%22%2C%222.%20Victim%20presses%20Ctrl%2BV%20in%20Explorer%3B%20Explorer%20obtains%20the%20IStream%20from%20FreeRDP%27s%20IDataObject%20and%20calls%20IStream%3A%3ARead%28pv%2C%200x1000%2C%20%26read%29%22%2C%223.%20FreeRDP%20sends%20a%20FILECONTENTS_RANGE%20request%20for%200x1000%20bytes%22%2C%224.%20Server%20replies%20with%20a%20CB_FILECONTENTS_RESPONSE%20carrying%20~0x100000%20bytes%20of%20attacker%20data%22%2C%225.%20wf_cliprdr_server_file_contents_response%28%29%20sets%20req_fsize%3D0x100000%3B%20CliprdrStream_Read%28%29%20CopyMemory%28%29s%201%20MiB%20into%20Explorer%27s%204%20KiB%20buffer%22%5D%2C%22technical_details%22%3A%22req_fsize%20is%20assigned%20directly%20from%20fileContentsResponse-%3EcbRequested%2C%20which%20is%20derived%20from%20the%20server-sent%20PDU%20dataLen%20%28response-%3EcbRequested%20%3D%20response-%3Ecommon.dataLen%20-%204%29%20with%20no%20validation%20or%20correlation%20to%20the%20original%20requested%20size.%20The%20only%20size%20comparison%20%28req_fsize%20%3C%20cb%20at%20wf_cliprdr.c%3A256%29%20runs%20after%20the%20CopyMemory%20and%20only%20handles%20short%20reads%2C%20so%20an%20oversized%20server%20response%20is%20copied%20in%20full%20before%20any%20check%20occurs.%22%2C%22title%22%3A%22Windows%20clipboard%20stream%20read%20ignores%20caller%20buffer%20size%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-D5W3VWPN",
  "bug_class": "Heap Buffer Overflow",
  "created_at": "2026-04-16T01:52:39+00:00",
  "description": "The Windows FreeRDP client's IStream::Read implementation for remote clipboard files (CliprdrStream_Read, wf_cliprdr.c:249) calls CopyMemory(pv, clipboard->req_fdata, clipboard->req_fsize) where req_fsize is taken directly from the server's CLIPRDR_FILE_CONTENTS_RESPONSE (wf_cliprdr.c:2449, cliprdr_common.c:377) and never compared to the caller's buffer size cb before the copy. The resulting IStream is handed to arbitrary paste consumers (e.g., explorer.exe) via OleSetClipboard and IDataObject::GetData. A malicious RDP server can answer a small FILECONTENTS_RANGE read with an arbitrarily large payload, and the client memcpy()s the entire attacker-controlled payload into the consumer's fixed-size buffer. This yields a scope-changing heap overflow with attacker-controlled content in a process outside the RDP client, enabling code execution.",
  "discovered_at": "2026-04-02T00:00:00+00:00",
  "location": "client/Windows/wf_cliprdr.c:249",
  "project": "freerdp/freerdp",
    "1. Attacker's RDP server advertises CFSTR_FILEDESCRIPTORW / CFSTR_FILECONTENTS on the shared clipboard",
    "2. Victim presses Ctrl+V in Explorer; Explorer obtains the IStream from FreeRDP's IDataObject and calls IStream::Read(pv, 0x1000, &read)",
    "3. FreeRDP sends a FILECONTENTS_RANGE request for 0x1000 bytes",
    "4. Server replies with a CB_FILECONTENTS_RESPONSE carrying ~0x100000 bytes of attacker data",
    "5. wf_cliprdr_server_file_contents_response() sets req_fsize=0x100000; CliprdrStream_Read() CopyMemory()s 1 MiB into Explorer's 4 KiB buffer"
  "technical_details": "req_fsize is assigned directly from fileContentsResponse->cbRequested, which is derived from the server-sent PDU dataLen (response->cbRequested = response->common.dataLen - 4) with no validation or correlation to the original requested size. The only size comparison (req_fsize < cb at wf_cliprdr.c:256) runs after the CopyMemory and only handles short reads, so an oversized server response is copied in full before any check occurs.",
  "title": "Windows clipboard stream read ignores caller buffer size",
```
