<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-VV0PRKKV -->

# ANT-2026-VV0PRKKV · wolfssl/wolfssl

## heap-buffer-overflow medium

[CVE-2026-5447](https://nvd.nist.gov/vuln/detail/CVE-2026-5447)
[GHSA-mx4j-fjqx-f8qj](https://github.com/advisories/GHSA-mx4j-fjqx-f8qj)

Security research firm medium
Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Calif.

# ANT-2026-VV0PRKKV: wolfSSL: heap buffer overflow in CertFromX509() from AuthorityKeyIdentifier size mismatch

In wolfSSL's OpenSSL-compatibility layer, CertFromX509() in src/x509.c converts a parsed certificate back into a Cert structure for re-encoding. When WOLFSSL\_AKID\_NAME is enabled, it bounds-checked only the AuthorityKeyIdentifier keyIdentifier length (authKeyIdSz) against the fixed-size cert->akid buffer but then copied the entire raw extension (authKeyIdSrcSz bytes, including authorityCertIssuer and authorityCertSerialNumber), whose length comes from the certificate without an upper bound. A crafted certificate with a short keyIdentifier and a multi-kilobyte authorityCertIssuer therefore passes the check and overflows the heap-allocated Cert when an application parses it and then re-encodes or re-signs it (for example via wolfSSL\_i2d\_X509\_bio() or wolfSSL\_X509\_sign()). The issue is CVE-2026-5447 / GHSA-mx4j-fjqx-f8qj and was fixed upstream in wolfSSL PR #10112 (merge commit d278da09), which validates the length that is actually copied.

**Project:** wolfSSL
**Location:** `src/x509.c:CertFromX509()`

**Root cause.** `CertFromX509()` (`src/x509.c`) copies the AuthorityKeyIdentifier (AKID) from a `WOLFSSL_X509` into the fixed-size `akid[]` array of a `Cert` structure that is heap-allocated during DER generation. Before the fix, the guard and the copy used different lengths:

```
if (x509->authKeyIdSz < sizeof(cert->akid)) {
#ifdef WOLFSSL_AKID_NAME
    cert->rawAkid = 0;
    if (x509->authKeyIdSrc) {
        XMEMCPY(cert->akid, x509->authKeyIdSrc, x509->authKeyIdSrcSz);
        cert->akidSz = (int)x509->authKeyIdSrcSz;
        cert->rawAkid = 1;
    else
#endif
    ...
```

`authKeyIdSz` is the length of the `[0] keyIdentifier` sub-field only, whereas `authKeyIdSrcSz` is the length of the complete raw extension value (`keyIdentifier` + `[1] authorityCertIssuer` + `[2] authorityCertSerialNumber`) as encoded in the certificate, and is propagated from the DER parser with no upper bound. A certificate whose AKID carries a small keyIdentifier (e.g. 20 bytes) and a large authorityCertIssuer GeneralName (e.g. a ~4 KB URI) satisfies the check and then writes several kilobytes past the end of `cert->akid`, whose size (`CTC_MAX_AKID_SIZE + sizeof(CertName) + CTC_SERIAL_SIZE` under `WOLFSSL_AKID_NAME`) is on the order of 1-1.6 KB depending on build options; the upstream regression test notes that re-encoding such a certificate "would write ~4000 bytes past the end of cert->akid[]".

**Reachability and preconditions.** The vulnerable branch is compiled when `WOLFSSL_CERT_GEN`, `WOLFSSL_CERT_EXT` and `WOLFSSL_AKID_NAME` are defined together with `OPENSSL_EXTRA`/`OPENSSL_ALL`. It is reached when an application parses an untrusted certificate (e.g. `wolfSSL_X509_d2i()`) and then re-encodes or re-signs the resulting object through the compatibility API, such as `wolfSSL_i2d_X509_bio()`/`i2d_X509` or `wolfSSL_X509_sign()` -- the pattern used by TLS interception proxies and certificate-rewriting tools. This conversion is not part of the default TLS client/server handshake path, so ordinary peer-certificate verification does not reach it.

**Impact.** The attacker controls both the length and the content of the out-of-bounds heap write, corrupting adjacent `Cert` fields and heap metadata in the process performing the conversion; consequences range from a crash to potentially exploitable memory corruption. The GitHub Advisory Database entry classifies the issue as CWE-122 (heap-based buffer overflow) with overall severity Medium, listing a CVSS 4.0 base score of 6.3 and a CVSS 3.1 vector of `AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N` (7.5).

**Fix.** wolfSSL PR #10112 ("Fix CertFromX509 copy length check"), merged 2026-04-03 as commit `d278da09dfa60237f246236f2c8acc5d11c5915a`, checks each copy against `sizeof(cert->akid)` using the length that is actually copied (`authKeyIdSrcSz` for the raw-AKID branch, `authKeyIdSz` otherwise), records `BUFFER_E` and returns `WOLFSSL_FAILURE` when the value does not fit, and adds the regression test `test_x509_CertFromX509_akid_overflow`. The advisory (GHSA-mx4j-fjqx-f8qj / CVE-2026-5447, published 2026-04-09) does not enumerate an affected version range; builds that predate this commit and enable the options above should be treated as affected.

**Crash signature:** `heap-buffer-overflow (READ)`

Reproduce against the target as described under Technical Details.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-VV0PRKKV.

---

**Reference:** ANT-2026-VV0PRKKV

Triage and disclosure were performed by Calif.

:   medium

UPSTREAM FIX

The change that resolved this finding.

```
diff --git a/src/x509.c b/src/x509.c
index 3593cd82f47..f4006ffe3ac 100644
--- a/src/x509.c
+++ b/src/x509.c
@@ -11870,25 +11870,28 @@ static int CertFromX509(Cert* cert, WOLFSSL_X509* x509)
         return WOLFSSL_FAILURE;

-    if (x509->authKeyIdSz < sizeof(cert->akid)) {
     #ifdef WOLFSSL_AKID_NAME
-        cert->rawAkid = 0;
-        if (x509->authKeyIdSrc) {
-            XMEMCPY(cert->akid, x509->authKeyIdSrc, x509->authKeyIdSrcSz);
-            cert->akidSz = (int)x509->authKeyIdSrcSz;
-            cert->rawAkid = 1;
+    cert->rawAkid = 0;
+    if (x509->authKeyIdSrc) {
+        if (x509->authKeyIdSrcSz > sizeof(cert->akid)) {
+            WOLFSSL_MSG("Auth Key ID too large");
+            WOLFSSL_ERROR_VERBOSE(BUFFER_E);
+            return WOLFSSL_FAILURE;
-        else
+        XMEMCPY(cert->akid, x509->authKeyIdSrc, x509->authKeyIdSrcSz);
+        cert->akidSz = (int)x509->authKeyIdSrcSz;
+        cert->rawAkid = 1;
+    }
+    else
     #endif
-        if (x509->authKeyId) {
-            XMEMCPY(cert->akid, x509->authKeyId, x509->authKeyIdSz);
-            cert->akidSz = (int)x509->authKeyIdSz;
+    if (x509->authKeyId) {
+        if (x509->authKeyIdSz > sizeof(cert->akid)) {
+            WOLFSSL_MSG("Auth Key ID too large");
+            WOLFSSL_ERROR_VERBOSE(BUFFER_E);
+            return WOLFSSL_FAILURE;
-    }
-    else {
-        WOLFSSL_MSG("Auth Key ID too large");
-        WOLFSSL_ERROR_VERBOSE(BUFFER_E);
-        return WOLFSSL_FAILURE;
+        XMEMCPY(cert->akid, x509->authKeyId, x509->authKeyIdSz);
+        cert->akidSz = (int)x509->authKeyIdSz;

     for (i = 0; i < x509->certPoliciesNb; i++) {
diff --git a/tests/api/test_x509.c b/tests/api/test_x509.c
index cd0a06241de..47780e6dc4e 100644
--- a/tests/api/test_x509.c
+++ b/tests/api/test_x509.c
@@ -38,6 +38,7 @@

 #include <wolfssl/internal.h>
 #include <wolfssl/wolfcrypt/asn.h>
+#include <wolfssl/wolfcrypt/asn_public.h>

 #if defined(OPENSSL_ALL) && \
     defined(HAVE_MANUAL_MEMIO_TESTS_DEPENDENCIES)
@@ -632,3 +633,245 @@ int test_x509_time_field_overread_via_tls(void)
 #endif /* compile guards */
     return EXPECT_RESULT();
+
+
+/* Test that CertFromX509 rejects an oversized raw AuthorityKeyIdentifier
+ * extension. Before the fix, the guard checked authKeyIdSz (the [0]
+ * keyIdentifier sub-field) but the WOLFSSL_AKID_NAME branch copied
+ * authKeyIdSrcSz (the full extension) bytes, causing a heap overflow. */
+int test_x509_CertFromX509_akid_overflow(void)
+{
+    EXPECT_DECLS;
+#if defined(WOLFSSL_AKID_NAME) && defined(WOLFSSL_CERT_GEN) && \
+    defined(WOLFSSL_CERT_EXT) && !defined(NO_BIO) && \
+    (defined(OPENSSL_EXTRA) || defined(OPENSSL_ALL))
+    /* DER builder helpers -- write into a flat buffer */
+#ifdef WOLFSSL_SMALL_STACK
+    unsigned char* buf = NULL;
+#else
+    unsigned char buf[16384];
+#endif
+    size_t pos = 0;
+    size_t akid_val_len;
+    unsigned char* akid_val = NULL;
+    WOLFSSL_X509* x = NULL;
+    WOLFSSL_BIO* bio = NULL;
+
+#ifdef WOLFSSL_SMALL_STACK
+    buf = (unsigned char*)XMALLOC(16384, NULL, DYNAMIC_TYPE_TMP_BUFFER);
+    ExpectNotNull(buf);
+    if (buf == NULL)
+        return EXPECT_RESULT();
+#endif
+
+    #define PUT1(b) do { buf[pos++] = (b); } while(0)
+    #define PUTN(p, n) do { XMEMCPY(buf + pos, (p), (n)); pos += (n); } while(0)
+
+    /* Emit tag + definite-length header, return header size */
+    #define TLV_HDR(tag, n, out, hlen) do {                          \
+        size_t _i = 0;                                               \
+        (out)[_i++] = (tag);                                         \
+        if ((n) < 0x80u)       { (out)[_i++] = (unsigned char)(n); } \
+        else if ((n) < 0x100u) { (out)[_i++] = 0x81;                \
+            (out)[_i++] = (unsigned char)(n); }                      \
+        else if ((n) < 0x10000u) { (out)[_i++] = 0x82;              \
+            (out)[_i++] = (unsigned char)((n)>>8);                   \
+            (out)[_i++] = (unsigned char)(n); }                      \
+        (hlen) = _i;                                                 \
+    } while(0)
+
+    /* Wrap [start, pos) in-place with a TLV header */
+    #define WRAP(start, tag) do {                                    \
+        size_t _len = pos - (start);                                 \
+        unsigned char _hdr[6]; size_t _hlen;                         \
+        TLV_HDR((tag), _len, _hdr, _hlen);                          \
+        XMEMMOVE(buf + (start) + _hlen, buf + (start), _len);       \
+        XMEMCPY(buf + (start), _hdr, _hlen);                        \
+        pos += _hlen;                                                \
+    } while(0)
+
+    /* ---- Build AKID extension value ---- */
+    {
+        size_t akid_start = pos;
+        size_t s;
+        int i;
+
+        /* [0] keyIdentifier: 20 bytes (small, passes old check) */
+        s = pos;
+        for (i = 0; i < 20; i++) PUT1(0x41);
+        WRAP(s, 0x80);
+
+        /* [1] authorityCertIssuer: one URI of ~4000 bytes
+         * This makes authKeyIdSrcSz >> sizeof(cert->akid) (~1628) */
+        s = pos;
+        {
+            const char* pfx = "http://e/";
+            PUTN(pfx, (size_t)XSTRLEN(pfx));
+            for (i = 0; i < 4000; i++) PUT1('Z');
+        }
+        WRAP(s, 0x86); /* GeneralName [6] URI */
+        WRAP(s, 0xA1); /* [1] IMPLICIT */
+
+        /* [2] authorityCertSerialNumber */
+        s = pos;
+        PUT1(0x01);
+        WRAP(s, 0x82);
+
+        WRAP(akid_start, 0x30); /* SEQUENCE */
+        akid_val_len = pos - akid_start;
+        akid_val = (unsigned char*)XMALLOC(akid_val_len, NULL,
+                                           DYNAMIC_TYPE_TMP_BUFFER);
+        ExpectNotNull(akid_val);
+        if (akid_val != NULL)
+            XMEMCPY(akid_val, buf + akid_start, akid_val_len);
+    }
+
+    /* ---- Build minimal self-signed v3 certificate ---- */
+    pos = 0;
+    {
+        size_t tbs_start = pos;
+        size_t s;
+
+        /* version [0] EXPLICIT INTEGER 2 (v3) */
+        PUT1(0xA0); PUT1(0x03); PUT1(0x02); PUT1(0x01); PUT1(0x02);
+
+        /* serialNumber INTEGER 1 */
+        PUT1(0x02); PUT1(0x01); PUT1(0x01);
+
+        /* signature: ecdsa-with-SHA256 */
+        s = pos;
+        {
+            unsigned char oid[] = {0x06,0x08,0x2A,0x86,0x48,0xCE,
+                                   0x3D,0x04,0x03,0x02};
+            PUTN(oid, sizeof(oid));
+        }
+        WRAP(s, 0x30);
+
+        /* issuer: CN=A */
+        s = pos;
+        {
+            size_t rdn = pos, atv = pos;
+            unsigned char cn[] = {0x06,0x03,0x55,0x04,0x03};
+            PUTN(cn, sizeof(cn));
+            PUT1(0x0C); PUT1(0x01); PUT1('A');
+            WRAP(atv, 0x30); WRAP(rdn, 0x31); WRAP(s, 0x30);
+        }
+
+        /* validity */
+        s = pos;
+        {
+            unsigned char t1[] = {0x17,0x0D,'2','5','0','1','0','1',
+                                  '0','0','0','0','0','0','Z'};
+            unsigned char t2[] = {0x17,0x0D,'3','5','0','1','0','1',
+                                  '0','0','0','0','0','0','Z'};
+            PUTN(t1, sizeof(t1)); PUTN(t2, sizeof(t2));
+        }
+        WRAP(s, 0x30);
+
+        /* subject: CN=A */
+        s = pos;
+        {
+            size_t rdn = pos, atv = pos;
+            unsigned char cn[] = {0x06,0x03,0x55,0x04,0x03};
+            PUTN(cn, sizeof(cn));
+            PUT1(0x0C); PUT1(0x01); PUT1('A');
+            WRAP(atv, 0x30); WRAP(rdn, 0x31); WRAP(s, 0x30);
+        }
+
+        /* subjectPublicKeyInfo: EC P-256 with dummy point */
+        s = pos;
+        {
+            size_t alg = pos, bs;
+            unsigned char ecpk[] = {0x06,0x07,0x2A,0x86,0x48,0xCE,
+                                    0x3D,0x02,0x01};
+            unsigned char p256[] = {0x06,0x08,0x2A,0x86,0x48,0xCE,
+                                    0x3D,0x03,0x01,0x07};
+            PUTN(ecpk, sizeof(ecpk));
+            PUTN(p256, sizeof(p256));
+            WRAP(alg, 0x30);
+            bs = pos;
+            PUT1(0x00); PUT1(0x04);
+            /* Use P-256 generator point (valid on-curve point) so th
… (truncated)
```

<https://github.com/wolfSSL/wolfssl/commit/d278da09dfa60237f246236f2c8acc5d11c5915a>

1. 2026-03-26
2. 2026-03-26
3. 2026-03-27
4. 2026-04-08
5. 2026-05-21

1bab7d8c0711e693bd53c3eec2b556b1ba8709ea1e4f3b0719a15ee8eaa70c89eeec4797e90b5ab922b7b8935bd6636effceefe31a976be0d557537919daab7d

Committed 2026-03-26 17:00 PT

Revealed 2026-05-21 16:00 PT

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-VV0PRKKV%22%2C%22bug_class%22%3A%22heap-buffer-overflow%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-27T02%3A08%3A32%2B00%3A00%22%2C%22description%22%3Anull%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22wolfSSL%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3Anull%2C%22title%22%3Anull%2C%22vendor_severity%22%3A%22medium%22%7D)

```
  "ant_id": "ANT-2026-VV0PRKKV",
  "bug_class": "heap-buffer-overflow",
  "created_at": "2026-03-27T02:08:32+00:00",
  "description": null,
  "project": "wolfSSL",
  "technical_details": null,
  "title": null,
  "vendor_severity": "medium"
```
