<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-Q5A1RHS0 -->

# ANT-2026-Q5A1RHS0 · libssh2/libssh2

## double-free high

[CVE-2026-66032](https://nvd.nist.gov/vuln/detail/CVE-2026-66032)

Claude critical
Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Calif.

# ANT-2026-Q5A1RHS0: SFTP double-free via server-controlled FXP\_STATUS packet length

The SFTP client's handler for SSH\_FXP\_STATUS messages allocates a buffer whose size is taken directly from a server-supplied packet length field. With a crafted response, this buffer ends up being released twice along the client code path. Because the server controls both the allocation size and the sequencing that leads to the two frees, a malicious or compromised SSH server can reliably induce a double-free in any connecting client. This corrupts heap allocator state and may be leveraged for remote code execution on the client.

**Project:** libssh2/libssh2
**Location:** `SFTP packet handling (libssh2 client)`

Malicious SSH server sends crafted SSH\_FXP\_STATUS where packet length controls allocation that is freed twice in SFTP client path. Allocation size and free sequencing server-controlled.

1. Attacker operates or compromises an SSH server the victim will connect to
2. Victim starts an SFTP session against that server
3. Server responds with a crafted SSH\_FXP\_STATUS packet containing a chosen length field
4. Client allocates a buffer of attacker-chosen size and subsequently frees it twice

## Suggested Fix

NULL the pointer after first free; restructure SFTP error path to not re-enter cleanup.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-Q5A1RHS0.

---

**Reference:** ANT-2026-Q5A1RHS0

Triage and disclosure were performed by Calif.

```
diff --git a/src/sftp.c b/src/sftp.c
index ec3a8ae18a..842eb6ea51 100644
--- a/src/sftp.c
+++ b/src/sftp.c
@@ -1259,6 +1259,7 @@ static LIBSSH2_SFTP_HANDLE *sftp_open(LIBSSH2_SFTP *sftp,
                 ssh2_deb((session, LIBSSH2_TRACE_SFTP, "got HANDLE FXOK"));

                 SSH2_FREE(session, data);
+                data = NULL;

                 /* silly situation, but check for a HANDLE */
                 rc = sftp_packet_require(sftp, SSH_FXP_HANDLE,
```

<https://github.com/libssh2/libssh2/commit/5e4776146552d898b9c0e1b313cd093fa8dc92d0>

1. 2026-04-11
2. 2026-05-08
3. 2026-05-09
4. 2026-07-02
5. 2026-08-17

c95720be6ce18be43e5a114a6d86a7d4aefcf6c4c1fe181d1ce94f81ed83af02e425f520c6a995a091d6341a318d3af8813d5863c169cdcc22353bc11912122c

Committed 2026-05-08 07:10 UTC

Revealed 2026-08-17 17:47 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-Q5A1RHS0%22%2C%22bug_class%22%3A%22double_free%22%2C%22claude_severity%22%3A%22critical%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-11T01%3A14%3A19%2B00%3A00%22%2C%22description%22%3A%22The%20SFTP%20client%27s%20handler%20for%20SSH_FXP_STATUS%20messages%20allocates%20a%20buffer%20whose%20size%20is%20taken%20directly%20from%20a%20server-supplied%20packet%20length%20field.%20With%20a%20crafted%20response%2C%20this%20buffer%20ends%20up%20being%20released%20twice%20along%20the%20client%20code%20path.%20Because%20the%20server%20controls%20both%20the%20allocation%20size%20and%20the%20sequencing%20that%20leads%20to%20the%20two%20frees%2C%20a%20malicious%20or%20compromised%20SSH%20server%20can%20reliably%20induce%20a%20double-free%20in%20any%20connecting%20client.%20This%20corrupts%20heap%20allocator%20state%20and%20may%20be%20leveraged%20for%20remote%20code%20execution%20on%20the%20client.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3A%22SFTP%20packet%20handling%20%28libssh2%20client%29%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22libssh2/libssh2%22%2C%22reproduction%22%3A%5B%221.%20Attacker%20operates%20or%20compromises%20an%20SSH%20server%20the%20victim%20will%20connect%20to%22%2C%222.%20Victim%20starts%20an%20SFTP%20session%20against%20that%20server%22%2C%223.%20Server%20responds%20with%20a%20crafted%20SSH_FXP_STATUS%20packet%20containing%20a%20chosen%20length%20field%22%2C%224.%20Client%20allocates%20a%20buffer%20of%20attacker-chosen%20size%20and%20subsequently%20frees%20it%20twice%22%5D%2C%22technical_details%22%3A%22Malicious%20SSH%20server%20sends%20crafted%20SSH_FXP_STATUS%20where%20packet%20length%20controls%20allocation%20that%20is%20freed%20twice%20in%20SFTP%20client%20path.%20Allocation%20size%20and%20free%20sequencing%20server-controlled.%22%2C%22title%22%3A%22SFTP%20double-free%20via%20server-controlled%20FXP_STATUS%20packet%20length%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-Q5A1RHS0",
  "bug_class": "double_free",
  "claude_severity": "critical",
  "created_at": "2026-04-11T01:14:19+00:00",
  "description": "The SFTP client's handler for SSH_FXP_STATUS messages allocates a buffer whose size is taken directly from a server-supplied packet length field. With a crafted response, this buffer ends up being released twice along the client code path. Because the server controls both the allocation size and the sequencing that leads to the two frees, a malicious or compromised SSH server can reliably induce a double-free in any connecting client. This corrupts heap allocator state and may be leveraged for remote code execution on the client.",
  "location": "SFTP packet handling (libssh2 client)",
  "project": "libssh2/libssh2",
    "1. Attacker operates or compromises an SSH server the victim will connect to",
    "2. Victim starts an SFTP session against that server",
    "3. Server responds with a crafted SSH_FXP_STATUS packet containing a chosen length field",
    "4. Client allocates a buffer of attacker-chosen size and subsequently frees it twice"
  "technical_details": "Malicious SSH server sends crafted SSH_FXP_STATUS where packet length controls allocation that is freed twice in SFTP client path. Allocation size and free sequencing server-controlled.",
  "title": "SFTP double-free via server-controlled FXP_STATUS packet length",
```
