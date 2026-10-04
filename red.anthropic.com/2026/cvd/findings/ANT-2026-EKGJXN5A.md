<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-EKGJXN5A -->

# ANT-2026-EKGJXN5A · wireshark/wireshark

## buffer-overflow medium

[CVE-2026-19694](https://nvd.nist.gov/vuln/detail/CVE-2026-19694)

Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-EKGJXN5A: TTL reader fixed-offset write into undersized buffer

In ttl\_read\_segmented\_message\_entry(), item->size is read from the .ttl file and passed directly to g\_try\_malloc() with only an upper bound check and no minimum enforced. After reassembly (which the attacker can complete in a single segment by setting item->size as small as 2 and choosing the nested-frame type), the buffer is handed to ttl\_check\_segmented\_message\_recursion() and ttl\_fix\_segmented\_message\_entry\_timestamp(), which perform raw memcpy() at fixed offsets with no size check. This yields an 8-byte OOB read at ttl.c:2016/2040 and an 8-byte OOB write of an attacker-controlled timestamp at buf+8 (ttl.c:2045). The attacker controls both the allocation size and the 8 bytes written, and can repeat the primitive per log entry, giving a multi-shot controlled heap corruption primitive triggered simply by opening a crafted capture in Wireshark.

**Project:** wireshark/wireshark
**Location:** `wiretap/ttl.c:2097`

Root cause: item->size from the file header is trusted as the allocation size (g\_try\_malloc(item->size)) without enforcing that it is at least as large as the fixed header area the code later writes into. The subsequent memcpy(in->buf + sizeof(ttl\_entryheader\_t), &timestamp, 8) assumes ≥16 bytes and bypasses the bounds-checked helper ttl\_read\_bytes(), so a size of 2 results in 8 attacker-chosen bytes written past the heap chunk.

1. Craft a .ttl file with a segmented message entry header advertising item->size = 2 and item->type = TTL\_SEGMENTED\_MESSAGE\_ENTRY\_TYPE\_NESTED\_FRAME.
2. Set the first 2 bytes so the nested entry type resolves to TTL\_BUS\_DATA\_ENTRY (0), and supply an arbitrary 64-bit timestamp value.
3. Victim opens the file; ttl\_read\_entry() dispatches to ttl\_read\_segmented\_message\_entry(), which allocates 2 bytes via g\_try\_malloc().
4. Reassembly completes in one segment; ttl\_fix\_segmented\_message\_entry\_timestamp() memcpy()s the 8-byte attacker-controlled timestamp to buf+8, writing OOB.
5. Repeat with multiple entries for a multi-shot heap corruption primitive.

## Suggested Fix

Reject or clamp log-entry sizes that are smaller than the fixed header area before allocating and before performing any fixed-offset stores into the buffer.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-EKGJXN5A.

---

**Reference:** ANT-2026-EKGJXN5A

Triage and disclosure were performed by Ada Logics.

```
diff --git a/wiretap/ttl.c b/wiretap/ttl.c
index e33c021c635..696eab17226 100644
--- a/wiretap/ttl.c
+++ b/wiretap/ttl.c
@@ -2009,10 +2009,15 @@ ttl_check_segmented_message_recursion(const ttl_read_t* in, int* err, char** err

     if (in->validity != VALIDITY_BUF) {
         *err = WTAP_ERR_INTERNAL;
-        *err_info = ws_strdup("tt_fix_segmented_message_entry_payload: input buffer is not valid");
+        *err_info = ws_strdup("ttl_check_segmented_message_recursion: input buffer is not valid");
         return false;

+    if (sizeof(ttl_entryheader_t) > in->size - in->cur_pos) {
+        *err = WTAP_ERR_INTERNAL;
+        *err_info = ws_strdup("ttl_check_segmented_message_recursion: input buffer too short");
+        return false;
+    }
     memcpy(&header, in->buf + in->cur_pos, sizeof(ttl_entryheader_t));
     fix_endianness_ttl_entryheader(&header);

@@ -2033,14 +2038,23 @@ ttl_fix_segmented_message_entry_timestamp(const ttl_read_t* in, uint64_t timesta

     if (in->validity != VALIDITY_BUF) {
         *err = WTAP_ERR_INTERNAL;
-        *err_info = ws_strdup("tt_fix_segmented_message_entry_payload: input buffer is not valid");
+        *err_info = ws_strdup("ttl_fix_segmented_message_entry_timestamp: input buffer is not valid");
         return false;

+    if (sizeof(ttl_entryheader_t) > in->size - in->cur_pos) {
+        goto buf_too_small;
+    }
     memcpy(&header, in->buf + in->cur_pos, sizeof(ttl_entryheader_t));
     fix_endianness_ttl_entryheader(&header);

     if ((header.size_type >> 12) == TTL_BUS_DATA_ENTRY) {
+        if (sizeof(uint64_t) > in->size - (in->cur_pos + sizeof(ttl_entryheader_t))) {
+        buf_too_small:
+            *err = WTAP_ERR_INTERNAL;
+            *err_info = ws_strdup("ttl_fix_segmented_message_entry_timestamp: input buffer too short");
+            return false;
+        }
         timestamp = GUINT64_TO_LE(timestamp);
         memcpy(in->buf + in->cur_pos + sizeof(ttl_entryheader_t), &timestamp, sizeof(uint64_t));
```

<https://github.com/wireshark/wireshark/commit/f9fdd24295456219f39be01beeaf734c2e3a8a2c>

1. 2026-04-02
2. 2026-07-04
3. 2026-08-12
4. 2026-08-12
5. 2026-09-28

c760c779f7e6bc3898cd2b37f9232f2c382e5872f55457418cf3f6d6ca636a3c6601c1b8138d1c6551ef896021d5c6ac6f59e30e3d9519168fcdfd8ded48febd

Committed 2026-07-22 07:34 UTC

Revealed 2026-09-28 20:39 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-EKGJXN5A%22%2C%22bug_class%22%3A%22buffer_overflow%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-16T14%3A11%3A18%2B00%3A00%22%2C%22description%22%3A%22In%20ttl_read_segmented_message_entry%28%29%2C%20item-%3Esize%20is%20read%20from%20the%20.ttl%20file%20and%20passed%20directly%20to%20g_try_malloc%28%29%20with%20only%20an%20upper%20bound%20check%20and%20no%20minimum%20enforced.%20After%20reassembly%20%28which%20the%20attacker%20can%20complete%20in%20a%20single%20segment%20by%20setting%20item-%3Esize%20as%20small%20as%202%20and%20choosing%20the%20nested-frame%20type%29%2C%20the%20buffer%20is%20handed%20to%20ttl_check_segmented_message_recursion%28%29%20and%20ttl_fix_segmented_message_entry_timestamp%28%29%2C%20which%20perform%20raw%20memcpy%28%29%20at%20fixed%20offsets%20with%20no%20size%20check.%20This%20yields%20an%208-byte%20OOB%20read%20at%20ttl.c%3A2016/2040%20and%20an%208-byte%20OOB%20write%20of%20an%20attacker-controlled%20timestamp%20at%20buf%2B8%20%28ttl.c%3A2045%29.%20The%20attacker%20controls%20both%20the%20allocation%20size%20and%20the%208%20bytes%20written%2C%20and%20can%20repeat%20the%20primitive%20per%20log%20entry%2C%20giving%20a%20multi-shot%20controlled%20heap%20corruption%20primitive%20triggered%20simply%20by%20opening%20a%20crafted%20capture%20in%20Wireshark.%22%2C%22discovered_at%22%3A%222026-04-02T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22wiretap/ttl.c%3A2097%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22wireshark/wireshark%22%2C%22reproduction%22%3A%5B%221.%20Craft%20a%20.ttl%20file%20with%20a%20segmented%20message%20entry%20header%20advertising%20item-%3Esize%20%3D%202%20and%20item-%3Etype%20%3D%20TTL_SEGMENTED_MESSAGE_ENTRY_TYPE_NESTED_FRAME.%22%2C%222.%20Set%20the%20first%202%20bytes%20so%20the%20nested%20entry%20type%20resolves%20to%20TTL_BUS_DATA_ENTRY%20%280%29%2C%20and%20supply%20an%20arbitrary%2064-bit%20timestamp%20value.%22%2C%223.%20Victim%20opens%20the%20file%3B%20ttl_read_entry%28%29%20dispatches%20to%20ttl_read_segmented_message_entry%28%29%2C%20which%20allocates%202%20bytes%20via%20g_try_malloc%28%29.%22%2C%224.%20Reassembly%20completes%20in%20one%20segment%3B%20ttl_fix_segmented_message_entry_timestamp%28%29%20memcpy%28%29s%20the%208-byte%20attacker-controlled%20timestamp%20to%20buf%2B8%2C%20writing%20OOB.%22%2C%225.%20Repeat%20with%20multiple%20entries%20for%20a%20multi-shot%20heap%20corruption%20primitive.%22%5D%2C%22technical_details%22%3A%22Root%20cause%3A%20item-%3Esize%20from%20the%20file%20header%20is%20trusted%20as%20the%20allocation%20size%20%28g_try_malloc%28item-%3Esize%29%29%20without%20enforcing%20that%20it%20is%20at%20least%20as%20large%20as%20the%20fixed%20header%20area%20the%20code%20later%20writes%20into.%20The%20subsequent%20memcpy%28in-%3Ebuf%20%2B%20sizeof%28ttl_entryheader_t%29%2C%20%26timestamp%2C%208%29%20assumes%20%E2%89%A516%20bytes%20and%20bypasses%20the%20bounds-checked%20helper%20ttl_read_bytes%28%29%2C%20so%20a%20size%20of%202%20results%20in%208%20attacker-chosen%20bytes%20written%20past%20the%20heap%20chunk.%22%2C%22title%22%3A%22TTL%20reader%20fixed-offset%20write%20into%20undersized%20buffer%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-EKGJXN5A",
  "bug_class": "buffer_overflow",
  "created_at": "2026-04-16T14:11:18+00:00",
  "description": "In ttl_read_segmented_message_entry(), item->size is read from the .ttl file and passed directly to g_try_malloc() with only an upper bound check and no minimum enforced. After reassembly (which the attacker can complete in a single segment by setting item->size as small as 2 and choosing the nested-frame type), the buffer is handed to ttl_check_segmented_message_recursion() and ttl_fix_segmented_message_entry_timestamp(), which perform raw memcpy() at fixed offsets with no size check. This yields an 8-byte OOB read at ttl.c:2016/2040 and an 8-byte OOB write of an attacker-controlled timestamp at buf+8 (ttl.c:2045). The attacker controls both the allocation size and the 8 bytes written, and can repeat the primitive per log entry, giving a multi-shot controlled heap corruption primitive triggered simply by opening a crafted capture in Wireshark.",
  "discovered_at": "2026-04-02T00:00:00+00:00",
  "location": "wiretap/ttl.c:2097",
  "project": "wireshark/wireshark",
    "1. Craft a .ttl file with a segmented message entry header advertising item->size = 2 and item->type = TTL_SEGMENTED_MESSAGE_ENTRY_TYPE_NESTED_FRAME.",
    "2. Set the first 2 bytes so the nested entry type resolves to TTL_BUS_DATA_ENTRY (0), and supply an arbitrary 64-bit timestamp value.",
    "3. Victim opens the file; ttl_read_entry() dispatches to ttl_read_segmented_message_entry(), which allocates 2 bytes via g_try_malloc().",
    "4. Reassembly completes in one segment; ttl_fix_segmented_message_entry_timestamp() memcpy()s the 8-byte attacker-controlled timestamp to buf+8, writing OOB.",
    "5. Repeat with multiple entries for a multi-shot heap corruption primitive."
  "technical_details": "Root cause: item->size from the file header is trusted as the allocation size (g_try_malloc(item->size)) without enforcing that it is at least as large as the fixed header area the code later writes into. The subsequent memcpy(in->buf + sizeof(ttl_entryheader_t), &timestamp, 8) assumes ≥16 bytes and bypasses the bounds-checked helper ttl_read_bytes(), so a size of 2 results in 8 attacker-chosen bytes written past the heap chunk.",
  "title": "TTL reader fixed-offset write into undersized buffer",
```
