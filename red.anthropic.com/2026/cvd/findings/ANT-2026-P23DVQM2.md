<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-P23DVQM2 -->

# ANT-2026-P23DVQM2 · wolfssl/wolfssl

## crypto-failure high

[CVE-2026-5500](https://nvd.nist.gov/vuln/detail/CVE-2026-5500)
[GHSA-m77r-vqw2-hffx](https://github.com/advisories/GHSA-m77r-vqw2-hffx)

Maintainer high

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Calif.

# ANT-2026-P23DVQM2: wolfSSL PKCS#7 AuthEnvelopedData decoder accepts truncated AES-GCM authentication tags

wc\_PKCS7\_DecodeAuthEnvelopedData() in wolfcrypt/src/pkcs7.c took the AES-GCM authentication tag length directly from the mac OCTET STRING of the incoming CMS AuthEnvelopedData message, applied only an upper-bound check, and never compared it with the message's aes-ICVlen parameter; the underlying wc\_AesGcmDecrypt() in turn accepted tags as short as one byte even though the encrypt path enforces WOLFSSL\_MIN\_AUTH\_TAG\_SZ. An attacker able to modify a message in transit could alter the encrypted content and truncate the mac field from 16 bytes to 1 byte, reducing the integrity check from a 2^-128 to a 2^-8 per-attempt forgery probability. The issue is tracked as CVE-2026-5500 / GHSA-m77r-vqw2-hffx and was fixed in commit a88dd07c7 (wolfSSL PR #10102), included in wolfSSL 5.9.1.

**Project:** wolfssl/wolfssl
**Location:** `wolfcrypt/src/pkcs7.c:wc_PKCS7_DecodeAuthEnvelopedData (with wolfcrypt/src/aes.c:wc_AesGcmDecrypt)`

**Root cause.** In `wc_PKCS7_DecodeAuthEnvelopedData()` (`wolfcrypt/src/pkcs7.c`), the length of the `mac` OCTET STRING parsed from the attacker-supplied DER is stored in `authTagSz` and checked only against the 16-byte upper bound of the local tag buffer before being passed through `wc_PKCS7_DecryptContent()` to `wc_AesGcmDecrypt()`. The RFC 5084 `aes-ICVlen` value from the content-encryption AlgorithmIdentifier is parsed into `macSz` but never cross-checked against `authTagSz`, and neither length is covered by the GCM additional authenticated data (only the encoded authenticated attributes are). Separately, in `wolfcrypt/src/aes.c`, `wc_AesGcmDecrypt()` rejected only `authTagSz == 0` or `authTagSz > WC_AES_BLOCK_SIZE`, whereas the encrypt side enforces `WOLFSSL_MIN_AUTH_TAG_SZ` (12 by default). The combination made a one-byte tag comparison reachable through the CMS AuthEnvelopedData decoder.

**Reach and impact.** The path requires a build with PKCS#7 and AES-GCM support and an application that calls `wc_PKCS7_DecodeAuthEnvelopedData()` on untrusted input using AES-128/192/256-GCM content encryption. A man-in-the-middle who captures a legitimate AuthEnvelopedData message can modify the ciphertext, rewrite the `mac` field to a single byte, and enumerate that byte in at most 256 submissions; the default software AES-GCM path then compares only the one byte and the recipient accepts the tampered content as authentic. The impact is loss of integrity and authenticity of the decrypted content; the issue does not provide key or plaintext recovery. The GitHub advisory rates it High (CVSS 3.1 5.9, `AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:H/A:N`; CVSS 4.0 8.7; CWE-20).

**Fix.** Commit `a88dd07c70e9415c3daa64d478f9a45bd65f9e5d` ("pkcs7,aes: reject truncated GCM auth tags", merged via wolfSSL PR #10102 and shipped in wolfSSL 5.9.1) validates that the parsed `macSz` is in 1..16, requires `authTagSz` to equal `macSz`, rejects GCM tags shorter than `WOLFSSL_MIN_AUTH_TAG_SZ` in the PKCS#7 decoder, enforces the same minimum in `wc_AesGcmDecrypt()`, and adds a regression test that truncates the final MAC OCTET STRING from 16 bytes to 1 and expects decoding to fail:

```
authTagSz = (word32)length;
if (ret == 0 && authTagSz != (word32)macSz) {
    WOLFSSL_MSG("AuthEnvelopedData authTag size mismatch");
    ret = ASN_PARSE_E;
if (ret == 0 &&
        (encOID == AES128GCMb || encOID == AES192GCMb ||
         encOID == AES256GCMb) &&
        authTagSz < WOLFSSL_MIN_AUTH_TAG_SZ) {
    WOLFSSL_MSG("AuthEnvelopedData GCM authTag too small");
    ret = ASN_PARSE_E;
```

Identifiers: CVE-2026-5500, GHSA-m77r-vqw2-hffx.

This finding was identified by static analysis and has not yet been dynamically reproduced. The Technical Details section above describes the code path; a trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-P23DVQM2.

---

**Reference:** ANT-2026-P23DVQM2

Triage and disclosure were performed by Calif.

The change that resolved this finding.

```
diff --git a/wolfcrypt/src/aes.c b/wolfcrypt/src/aes.c
index a3b75dbb34b..41b01031c41 100644
--- a/wolfcrypt/src/aes.c
+++ b/wolfcrypt/src/aes.c
@@ -10217,8 +10217,9 @@ int  wc_AesGcmDecrypt(Aes* aes, byte* out, const byte* in, word32 sz,
     /* If the sz is non-zero, both in and out must be set. If sz is 0,
      * in and out are don't cares, as this is is the GMAC case. */
     if (aes == NULL || iv == NULL || (sz != 0 && (in == NULL || out == NULL)) ||
-        authTag == NULL || authTagSz > WC_AES_BLOCK_SIZE || authTagSz == 0 ||
-        ivSz == 0 || ((authInSz > 0) && (authIn == NULL)))
+        authTag == NULL || authTagSz > WC_AES_BLOCK_SIZE ||
+        authTagSz < WOLFSSL_MIN_AUTH_TAG_SZ || ivSz == 0 ||
+        ((authInSz > 0) && (authIn == NULL)))
         return BAD_FUNC_ARG;
@@ -10781,8 +10782,8 @@ int wc_AesGcmDecrypt(Aes* aes, byte* out, const byte* in, word32 sz,
     /* If the sz is non-zero, both in and out must be set. If sz is 0,
      * in and out are don't cares, as this is is the GMAC case. */
     if (aes == NULL || iv == NULL || (sz != 0 && (in == NULL || out == NULL)) ||
-        authTag == NULL || authTagSz > WC_AES_BLOCK_SIZE || authTagSz == 0 ||
-        ivSz == 0) {
+        authTag == NULL || authTagSz > WC_AES_BLOCK_SIZE ||
+        authTagSz < WOLFSSL_MIN_AUTH_TAG_SZ || ivSz == 0) {

         return BAD_FUNC_ARG;
@@ -12473,7 +12474,7 @@ int wc_AesGcmEncryptFinal(Aes* aes, byte* authTag, word32 authTagSz)

     /* Check validity of parameters. */
     if ((aes == NULL) || (authTag == NULL) || (authTagSz > WC_AES_BLOCK_SIZE) ||
-            (authTagSz == 0)) {
+            (authTagSz < WOLFSSL_MIN_AUTH_TAG_SZ)) {
         ret = BAD_FUNC_ARG;

diff --git a/wolfcrypt/src/pkcs7.c b/wolfcrypt/src/pkcs7.c
index 9efec15ec7f..174c04d632c 100644
--- a/wolfcrypt/src/pkcs7.c
+++ b/wolfcrypt/src/pkcs7.c
@@ -140,6 +140,7 @@ struct PKCS7State {
     word32 nonceSz;  /* size of nonce stored */
     word32 aadSz;    /* size of additional AEAD data */
     word32 tagSz;    /* size of tag for AEAD */
+    word32 icvSz;    /* expected ICV/MAC size from AlgoID parameter */
     word32 contentSz;
     word32 currContIdx;   /* index of current content */
     word32 currContSz;    /* size of current content */
@@ -14235,6 +14236,10 @@ int wc_PKCS7_DecodeAuthEnvelopedData(wc_PKCS7* pkcs7, byte* in,
             if (ret == 0 && GetMyVersion(pkiMsg, &idx, &macSz, pkiMsgSz) < 0) {
                 ret = ASN_PARSE_E;
+            if (ret == 0 && (macSz <= 0 || macSz > WC_AES_BLOCK_SIZE)) {
+                WOLFSSL_MSG("AuthEnvelopedData invalid MAC length");
+                ret = ASN_PARSE_E;
+            }

             if (ret == 0) {
                 explicitOctet = 0;
@@ -14280,7 +14285,8 @@ int wc_PKCS7_DecodeAuthEnvelopedData(wc_PKCS7* pkcs7, byte* in,
                 break;

-            /* store nonce for later */
+            /* store nonce and macSz for later */
+            pkcs7->stream->icvSz = (word32)macSz;
             if (nonceSz > 0) {
                 pkcs7->stream->nonceSz = (word32)nonceSz;
                 pkcs7->stream->nonce = (byte*)XMALLOC((word32)nonceSz,
@@ -14471,6 +14477,7 @@ int wc_PKCS7_DecodeAuthEnvelopedData(wc_PKCS7* pkcs7, byte* in,
                 encodedAttribSz = pkcs7->stream->aadSz;
                 encodedAttribs  = pkcs7->stream->aad;
+            macSz = (int)pkcs7->stream->icvSz;
         #endif

@@ -14487,6 +14494,17 @@ int wc_PKCS7_DecodeAuthEnvelopedData(wc_PKCS7* pkcs7, byte* in,
                 ret = ASN_PARSE_E;
             authTagSz = (word32)length;
+            if (ret == 0 && authTagSz != (word32)macSz) {
+                WOLFSSL_MSG("AuthEnvelopedData authTag size mismatch");
+                ret = ASN_PARSE_E;
+            }
+            if (ret == 0 &&
+                    (encOID == AES128GCMb || encOID == AES192GCMb ||
+                     encOID == AES256GCMb) &&
+                    authTagSz < WOLFSSL_MIN_AUTH_TAG_SZ) {
+                WOLFSSL_MSG("AuthEnvelopedData GCM authTag too small");
+                ret = ASN_PARSE_E;
+            }

         #ifndef NO_PKCS7_STREAM
             /* there might not be enough data for the auth tag too */
diff --git a/wolfcrypt/test/test.c b/wolfcrypt/test/test.c
index 755aa94358e..8077342566b 100644
--- a/wolfcrypt/test/test.c
+++ b/wolfcrypt/test/test.c
@@ -57721,6 +57721,9 @@ static wc_test_ret_t pkcs7authenveloped_run_vectors(byte* rsaCert, word32 rsaCer
     wc_test_ret_t ret = 0;
     int testSz = 0, i;
     int envelopedSz, decodedSz;
+#ifdef HAVE_AESGCM
+    int tagTruncationChecked = 0;
+#endif

     byte   *enveloped = NULL;
     byte   *decoded = NULL;
@@ -58232,6 +58235,45 @@ static wc_test_ret_t pkcs7authenveloped_run_vectors(byte* rsaCert, word32 rsaCer
             ERROR_OUT(WC_TEST_RET_ENC_NC, out);

+#ifdef HAVE_AESGCM
+        if (tagTruncationChecked == 0 &&
+                (testVectors[i].encryptOID == AES128GCMb ||
+                 testVectors[i].encryptOID == AES192GCMb ||
+                 testVectors[i].encryptOID == AES256GCMb) &&
+                testVectors[i].authAttribsSz == 0 &&
+                testVectors[i].unauthAttribsSz == 0 &&
+                envelopedSz > (WC_AES_BLOCK_SIZE + 2)) {
+            int macIdx = envelopedSz - (WC_AES_BLOCK_SIZE + 2);
+            byte* tampered = NULL;
+
+            /* For plain DER output without unauthenticated attributes, the
+             * MAC OCTET STRING is the final field. */
+            if (enveloped[macIdx] == ASN_OCTET_STRING &&
+                    enveloped[macIdx + 1] == WC_AES_BLOCK_SIZE) {
+                tampered = (byte*)XMALLOC((word32)envelopedSz, HEAP_HINT,
+                                          DYNAMIC_TYPE_TMP_BUFFER);
+                if (tampered == NULL) {
+                    wc_PKCS7_Free(pkcs7);
+                    ERROR_OUT(WC_TEST_RET_ENC_ERRNO, out);
+                }
+                XMEMCPY(tampered, enveloped, (word32)envelopedSz);
+                tampered[macIdx + 1] = 1;
+
+                decodedSz = wc_PKCS7_DecodeAuthEnvelopedData(pkcs7, tampered,
+                        (word32)envelopedSz, decoded, PKCS7_BUF_SIZE);
+
+                XFREE(tampered, HEAP_HINT, DYNAMIC_TYPE_TMP_BUFFER);
+                tampered = NULL;
+
+                if (decodedSz > 0) {
+                    wc_PKCS7_Free(pkcs7);
+                    ERROR_OUT(WC_TEST_RET_ENC_NC, out);
+                }
+                tagTruncationChecked = 1;
+            }
+        }
+#endif
+
 #ifdef PKCS7_OUTPUT_TEST_BUNDLES
         /* output pkcs7 envelopedData for external testing */
         pkcs7File = XFOPEN(testVectors[i].outFileName, "wb");
diff --git a/wolfssl/wolfcrypt/settings.h b/wolfssl/wolfcrypt/settings.h
index a0c79c5e846..4929b61cb43 100644
--- a/wolfssl/wolfcrypt/settings.h
+++ b/wolfssl/wolfcrypt/settings.h
@@ -3429,6 +3429,8 @@ extern void uITRON4_free(void *p) ;
 /* Default AES minimum auth tag sz, allow user to override */
 #ifndef WOLFSSL_MIN_AUTH_TAG_SZ
     #define WOLFSSL_MIN_AUTH_TAG_SZ 12
+#elif WOLFSSL_MIN_AUTH_TAG_SZ < 1
+    #error WOLFSSL_MIN_AUTH_TAG_SZ must be at least 1
 #endif
```

<https://github.com/wolfSSL/wolfssl/commit/a88dd07c7>

1. 2026-03-29
2. 2026-04-05
3. 2026-05-07
4. 2026-05-07
5. 2026-05-20

2c8aa01adff247bee658ef6ef3ae642a97192eb85e456ea259eb203b183b4eed7b40c8a991be73dc4ab9dd6829d840aae1799e93cdad5de9615a26a38614f46a

Committed 2026-04-05 23:37 UTC

Revealed 2026-05-20 07:40 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-P23DVQM2%22%2C%22bug_class%22%3A%22crypto-failure%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A42%3A35%2B00%3A00%22%2C%22description%22%3Anull%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22wolfSSL%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3Anull%2C%22title%22%3A%22cms%20authenvelopeddata%20aead%20forgery%20via%20gcm%20tag%20truncati%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-P23DVQM2",
  "bug_class": "crypto-failure",
  "created_at": "2026-03-29T20:42:35+00:00",
  "description": null,
  "project": "wolfSSL",
  "technical_details": null,
  "title": "cms authenvelopeddata aead forgery via gcm tag truncati",
```
