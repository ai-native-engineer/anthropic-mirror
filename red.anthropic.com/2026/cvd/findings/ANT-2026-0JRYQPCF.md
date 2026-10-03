<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-0JRYQPCF -->

# ANT-2026-0JRYQPCF · wolfssl/wolfssl

## heap-buffer-overflow medium

[CVE-2026-5503](https://nvd.nist.gov/vuln/detail/CVE-2026-5503)
[GHSA-65xm-pfx9-g5p3](https://github.com/advisories/GHSA-65xm-pfx9-g5p3)

Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Calif.

# ANT-2026-0JRYQPCF: wolfSSL ECH: heap buffer overflow in TLSX\_EchChangeSNI via publicName SNI pollution

wolfSSL's TLS 1.3 Encrypted Client Hello (ECH) client code contained a heap buffer overflow, tracked as CVE-2026-5503 (GHSA-65xm-pfx9-g5p3). When a client used ECH with no Server Name Indication (SNI) configured, TLSX\_EchChangeSNI() in src/tls.c attached the ECH configuration's public name as an SNI entry on the shared WOLFSSL\_CTX and TLSX\_EchRestoreSNI() never removed it; the inner ClientHello, which had been sized before this injection but was serialized after it, was then overrun when TLSX\_SNI\_Write() copied the public name up to 255 bytes past the end of the allocation. wolfSSL fixed the issue in commit 1823f2e9f (PR #10102), released in wolfSSL 5.9.1, by performing the SNI swap only when an SNI is actually present, always removing the injected public-name SNI, and rejecting ECH use without an inner SNI.

**Project:** wolfssl/wolfssl
**Location:** `src/tls.c:TLSX_EchChangeSNI (and TLSX_EchRestoreSNI)`

**Component.** The defect is in the ECH helper pair `TLSX_EchChangeSNI()` / `TLSX_EchRestoreSNI()` in `src/tls.c`, compiled when both `WOLFSSL_TLS13` and `HAVE_ECH` are defined. These helpers run from `TLSX_GetSizeWithEch()` and `TLSX_WriteWithEch()` while the client sizes and writes its ClientHello extensions: for the outer ClientHello, `TLSX_EchChangeSNI()` temporarily replaces the client's real (inner) SNI with `echConfig->publicName`, and `TLSX_EchRestoreSNI()` undoes the swap afterwards.

**Root cause.** `TLSX_EchChangeSNI()` looks for an existing SNI first on `ssl->extensions` and then on `ssl->ctx->extensions`. The `ssl->extensions` branch only selected that list as the swap target when `TLSX_Find()` actually returned an SNI entry; the `ssl->ctx->extensions` branch selected the context list unconditionally, and the remove/add that followed ran regardless:

```
if (serverNameX == NULL && ssl->ctx && ssl->ctx->extensions) {
    serverNameX = TLSX_Find(ssl->ctx->extensions, TLSX_SERVER_NAME);
    extensions = &ssl->ctx->extensions;      /* set even when serverNameX == NULL */
...
TLSX_Remove(extensions, TLSX_SERVER_NAME, ssl->heap);
TLSX_UseSNI(extensions, WOLFSSL_SNI_HOST_NAME, echConfig->publicName, ...);
```

If the application enabled ECH but had configured no SNI on either the `WOLFSSL` object or its `WOLFSSL_CTX` (with `ssl->ctx->extensions` non-NULL), `TLSX_UseSNI()` therefore added a new SNI entry carrying the attacker-controlled `publicName` to the shared `WOLFSSL_CTX`. `TLSX_EchRestoreSNI()` only called `TLSX_Remove()` inside `if (serverNameX != NULL)`, so with no original SNI the injected entry was never removed and persisted on the context. The inner ClientHello had been sized before this injection but was written after it; `TLSX_SNI_Write()` then copied the public name (up to 255 bytes) past the end of the heap buffer allocated for the message.

**Impact.** Heap out-of-bounds write (CWE-787) in the wolfSSL TLS client while constructing an ECH ClientHello, resulting in memory corruption, plus an unintended public-name SNI left attached to a `WOLFSSL_CTX` that may be shared by other connections. Preconditions: wolfSSL built with TLS 1.3 and ECH support, and a client connection that uses ECH without an SNI configured. The GitHub advisory rates the issue medium severity.

**Fix and affected versions.** Fixed by wolfSSL commit `1823f2e9fcdf0c3a6a41d255033d817d23a5ebb3` ("tls: fix ECH heap buffer overflow via publicName SNI pollution"), merged in wolfSSL/wolfssl PR #10102 and first shipped in wolfSSL 5.9.1; wolfSSL 5.9.0 contains the vulnerable code. The fix (a) sets `extensions` in the `ctx` branch only when `TLSX_Find()` returns non-NULL and performs the `TLSX_Remove()`/`TLSX_UseSNI()` swap only when `extensions` is non-NULL, (b) moves `TLSX_Remove()` in `TLSX_EchRestoreSNI()` outside the `serverNameX` guard so an injected `publicName` SNI is always cleaned up, and (c) returns `BAD_FUNC_ARG` when ECH is used without an inner SNI instead of building the ClientHello. The fix commit credits Anthropic and Calif.io as reporters. Identifiers: CVE-2026-5503, GHSA-65xm-pfx9-g5p3.

This finding was identified by static analysis and has not yet been dynamically reproduced. The Technical Details section above describes the code path; a trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-0JRYQPCF.

---

**Reference:** ANT-2026-0JRYQPCF

Triage and disclosure were performed by Calif.

The change that resolved this finding.

```
diff --git a/src/tls.c b/src/tls.c
index b854b8f8cd5..09e6c921740 100644
--- a/src/tls.c
+++ b/src/tls.c
@@ -16086,11 +16086,18 @@ static int TLSX_EchChangeSNI(WOLFSSL* ssl, TLSX** pEchX,

         if (serverNameX == NULL && ssl->ctx && ssl->ctx->extensions) {
             serverNameX = TLSX_Find(ssl->ctx->extensions, TLSX_SERVER_NAME);
-            extensions = &ssl->ctx->extensions;
+            if (serverNameX != NULL)
+                extensions = &ssl->ctx->extensions;
+        }
+
+        /* ECH requires an inner SNI to be present for ClientHelloInner.
+         * Without it, fail instead of mutating extension lists. */
+        if (serverNameX == NULL) {
+            ret = BAD_FUNC_ARG;

         /* store the inner server name */
-        if (serverNameX != NULL) {
+        if (ret == 0 && serverNameX != NULL) {
             char* hostName = ((SNI*)serverNameX->data)->data.host_name;
             word32 hostNameSz = (word32)XSTRLEN(hostName) + 1;

@@ -16101,15 +16108,19 @@ static int TLSX_EchChangeSNI(WOLFSSL* ssl, TLSX** pEchX,
             XMEMCPY(serverName, hostName, hostNameSz);

-        /* remove the inner server name */
-        TLSX_Remove(extensions, TLSX_SERVER_NAME, ssl->heap);
+        /* only swap the SNI if one was found; extensions is non-NULL if an
+         * SNI entry was found on ssl->extensions or ctx->extensions */
+        if (ret == 0 && extensions != NULL) {
+            /* remove the inner server name */
+            TLSX_Remove(extensions, TLSX_SERVER_NAME, ssl->heap);

-        /* set the public name as the server name */
-        if ((ret = TLSX_UseSNI(extensions, WOLFSSL_SNI_HOST_NAME,
-                ((WOLFSSL_ECH*)echX->data)->echConfig->publicName,
-                XSTRLEN(((WOLFSSL_ECH*)echX->data)->echConfig->publicName),
-                ssl->heap)) == WOLFSSL_SUCCESS)
-            ret = 0;
+            /* set the public name as the server name */
+            if ((ret = TLSX_UseSNI(extensions, WOLFSSL_SNI_HOST_NAME,
+                    ((WOLFSSL_ECH*)echX->data)->echConfig->publicName,
+                    XSTRLEN(((WOLFSSL_ECH*)echX->data)->echConfig->publicName),
+                    ssl->heap)) == WOLFSSL_SUCCESS)
+                ret = 0;
+        }
     *pServerNameX = serverNameX;
     *pExtensions = extensions;
@@ -16122,10 +16133,12 @@ static int TLSX_EchRestoreSNI(WOLFSSL* ssl, char* serverName,
     int ret = 0;

-    if (serverNameX != NULL) {
-        /* remove the public name SNI */
+    /* always remove the publicName SNI we injected, regardless of whether
+     * there was a prior inner SNI to restore */
+    if (extensions != NULL)
         TLSX_Remove(extensions, TLSX_SERVER_NAME, ssl->heap);

+    if (serverNameX != NULL) {
         /* restore the inner server name */
         ret = TLSX_UseSNI(extensions, WOLFSSL_SNI_HOST_NAME,
             serverName, XSTRLEN(serverName), ssl->heap);
```

<https://github.com/wolfSSL/wolfssl/commit/1823f2e9f>

1. 2026-03-29
2. 2026-04-05
3. 2026-05-07
4. 2026-05-07
5. 2026-05-20

5175ece3afdba9cf93587112f7601b7e22caaf48410a2cb260e59f4b801eedbaf9de7f494493b446bd9e829ce6162cd0dcf3b285879b0f82342bc38b1e3b1ac8

Committed 2026-04-05 23:37 UTC

Revealed 2026-05-20 07:40 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-0JRYQPCF%22%2C%22bug_class%22%3A%22heap-buffer-overflow%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A42%3A36%2B00%3A00%22%2C%22description%22%3Anull%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22wolfSSL%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3Anull%2C%22title%22%3A%22wolfssl%20ech%20heap%20buffer%20overflow%20via%20publicname%20sni%20pol%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-0JRYQPCF",
  "bug_class": "heap-buffer-overflow",
  "created_at": "2026-03-29T20:42:36+00:00",
  "description": null,
  "project": "wolfSSL",
  "technical_details": null,
  "title": "wolfssl ech heap buffer overflow via publicname sni pol",
```
