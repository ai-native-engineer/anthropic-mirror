<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-RSSMAMA7 -->

# ANT-2026-RSSMAMA7 · wolfssl/wolfssl

## crypto-failure high

[CVE-2026-5479](https://nvd.nist.gov/vuln/detail/CVE-2026-5479)

Maintainer high

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Calif.

# ANT-2026-RSSMAMA7: wolfSSL EVP\_CipherFinal does not verify the Poly1305 tag on ChaCha20-Poly1305 decrypt

In wolfSSL's OpenSSL-compatibility EVP layer, wolfSSL\_EVP\_CipherFinal() (wolfcrypt/src/evp.c) finalised ChaCha20-Poly1305 decryption by computing the Poly1305 tag into ctx->authTag, overwriting the expected tag the caller had supplied through EVP\_CTRL\_AEAD\_SET\_TAG, and then returned success without comparing the two. Any application that decrypts with EVP\_chacha20\_poly1305() and relies on EVP\_DecryptFinal\_ex()/EVP\_CipherFinal() to reject forgeries, including wolfSSL's own QUIC helper wolfSSL\_quic\_aead\_decrypt() when TLS\_CHACHA20\_POLY1305\_SHA256 is negotiated, therefore accepted tampered or forged ciphertext as authentic. The issue is tracked as CVE-2026-5479 (GHSA-3xr8-r75g-g9c6) and was fixed by commit 1faddd640, which is included in wolfSSL 5.9.1.

**Project:** wolfssl/wolfssl
**Location:** `wolfcrypt/src/evp.c:wolfSSL_EVP_CipherFinal`

**Root cause.** In `wolfSSL_EVP_CipherFinal()` (`wolfcrypt/src/evp.c`), the `WC_CHACHA20_POLY1305_TYPE` case had no `ctx->enc` branch: for both encryption and decryption it called `wc_ChaCha20Poly1305_Final(&ctx->cipher.chachaPoly, ctx->authTag)` and returned `WOLFSSL_SUCCESS` whenever that call succeeded. `wc_ChaCha20Poly1305_Final()` only generates a tag, so on the decrypt path it overwrote the expected tag that `EVP_CIPHER_CTX_ctrl(..., EVP_CTRL_AEAD_SET_TAG, ...)` had copied into `ctx->authTag`. `wc_ChaCha20Poly1305_CheckTag()` was not called anywhere in `evp.c`, and `wolfSSL_EVP_DecryptFinal_ex()` is a plain passthrough to `wolfSSL_EVP_CipherFinal()`, so no tag comparison took place at any point. The adjacent AES-GCM branch of the same function does verify the tag.

**Reach and preconditions.** The code is compiled when the EVP compatibility layer is enabled (`OPENSSL_EXTRA`) together with `HAVE_CHACHA`/`HAVE_POLY1305`. It is reached by any caller that follows the standard OpenSSL AEAD pattern: decrypt with `EVP_chacha20_poly1305()`, set the received tag with `EVP_CTRL_AEAD_SET_TAG`, and treat a successful `EVP_DecryptFinal_ex()`/`EVP_CipherFinal()` as proof of authenticity. wolfSSL's QUIC integration uses exactly this pattern: `wolfSSL_quic_get_aead()` maps `TLS_CHACHA20_POLY1305_SHA256` to `EVP_chacha20_poly1305()`, and `wolfSSL_quic_aead_decrypt()` (`src/quic.c`) sets the tag via `EVP_CTRL_AEAD_SET_TAG` and relies solely on the return value of `wolfSSL_EVP_CipherFinal()`. wolfSSL's native TLS record layer calls the wolfCrypt ChaCha20-Poly1305 primitives directly and does not go through this EVP path.

**Impact.** Loss of AEAD integrity and authenticity for ChaCha20-Poly1305 via the EVP interface: an attacker who can modify or inject ciphertext has forged or tampered messages accepted, and the resulting plaintext is returned to the application as if it had been authenticated. The published advisory (CVE-2026-5479 / GHSA-3xr8-r75g-g9c6, CWE-354) rates the issue High, CVSS 3.1 8.1 (`AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`).

**Fix.** Commit `1faddd640edc8195c1fb7cb3904876e434ecab87` ("evp: verify Poly1305 tag on ChaCha20-Poly1305 decrypt"), merged via wolfSSL/wolfssl#10102 on 2026-04-06 and included in the wolfSSL 5.9.1 release (the 5.9.0 release does not contain it), saves the expected tag before calling `wc_ChaCha20Poly1305_Final()` and, on the decrypt path, compares it against the computed tag with `wc_ChaCha20Poly1305_CheckTag()`, returning `WOLFSSL_FAILURE` on mismatch. A regression test was added asserting that `EVP_DecryptFinal_ex()` rejects a forged tag.

```
case WC_CHACHA20_POLY1305_TYPE:
    byte computedTag[CHACHA20_POLY1305_AEAD_AUTHTAG_SIZE];
    if (!ctx->enc) {
        /* Save the expected tag before _Final() overwrites ctx->authTag */
        XMEMCPY(computedTag, ctx->authTag, sizeof(computedTag));
    if (wc_ChaCha20Poly1305_Final(&ctx->cipher.chachaPoly, ctx->authTag) != 0) {
        WOLFSSL_MSG("wc_ChaCha20Poly1305_Final failed");
        return WOLFSSL_FAILURE;
    if (!ctx->enc) {
        int tagErr = wc_ChaCha20Poly1305_CheckTag(computedTag, ctx->authTag);
        ForceZero(computedTag, sizeof(computedTag));
        if (tagErr != 0) {
            WOLFSSL_MSG("ChaCha20-Poly1305 tag mismatch");
            return WOLFSSL_FAILURE;
    *outl = 0;
    return WOLFSSL_SUCCESS;
```

This finding was identified by static analysis and has not yet been dynamically reproduced. The Technical Details section above describes the code path; a trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-RSSMAMA7.

---

**Reference:** ANT-2026-RSSMAMA7

Triage and disclosure were performed by Calif.

The change that resolved this finding.

```
diff --git a/tests/api/test_evp_cipher.c b/tests/api/test_evp_cipher.c
index b4e37df7a28..1e88da9979c 100644
--- a/tests/api/test_evp_cipher.c
+++ b/tests/api/test_evp_cipher.c
@@ -1915,6 +1915,7 @@ int test_wolfssl_EVP_chacha20_poly1305(void)
     byte cipherText[sizeof(plainText)];
     byte decryptedText[sizeof(plainText)];
     byte tag[CHACHA20_POLY1305_AEAD_AUTHTAG_SIZE];
+    byte badTag[CHACHA20_POLY1305_AEAD_AUTHTAG_SIZE];
     EVP_CIPHER_CTX* ctx = NULL;
     int outSz;

@@ -1979,6 +1980,28 @@ int test_wolfssl_EVP_chacha20_poly1305(void)
     EVP_CIPHER_CTX_free(ctx);
     ctx = NULL;

+    /* Negative test: forged (all-zero) tag must be rejected. */
+    XMEMSET(badTag, 0, sizeof(badTag));
+    ExpectNotNull((ctx = EVP_CIPHER_CTX_new()));
+    ExpectIntEQ(EVP_DecryptInit_ex(ctx, EVP_chacha20_poly1305(), NULL,
+                NULL, NULL), WOLFSSL_SUCCESS);
+    ExpectIntEQ(EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_AEAD_SET_IVLEN,
+                CHACHA20_POLY1305_AEAD_IV_SIZE, NULL), WOLFSSL_SUCCESS);
+    ExpectIntEQ(EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_AEAD_SET_TAG,
+                CHACHA20_POLY1305_AEAD_AUTHTAG_SIZE, badTag),
+                WOLFSSL_SUCCESS);
+    ExpectIntEQ(EVP_DecryptInit_ex(ctx, NULL, NULL, key, iv),
+                WOLFSSL_SUCCESS);
+    ExpectIntEQ(EVP_DecryptUpdate(ctx, NULL, &outSz, aad, sizeof(aad)),
+                WOLFSSL_SUCCESS);
+    ExpectIntEQ(EVP_DecryptUpdate(ctx, decryptedText, &outSz, cipherText,
+                sizeof(cipherText)), WOLFSSL_SUCCESS);
+    /* EVP_DecryptFinal_ex MUST return failure on tag mismatch */
+    ExpectIntNE(EVP_DecryptFinal_ex(ctx, decryptedText, &outSz),
+                WOLFSSL_SUCCESS);
+    EVP_CIPHER_CTX_free(ctx);
+    ctx = NULL;
+
     /* Test partial Inits. CipherInit() allow setting of key and iv
      * in separate calls. */
     ExpectNotNull((ctx = EVP_CIPHER_CTX_new()));
diff --git a/wolfcrypt/src/evp.c b/wolfcrypt/src/evp.c
index fc4f68eb9fc..121d926555f 100644
--- a/wolfcrypt/src/evp.c
+++ b/wolfcrypt/src/evp.c
@@ -1499,16 +1499,33 @@ int wolfSSL_EVP_CipherFinal(WOLFSSL_EVP_CIPHER_CTX *ctx, unsigned char *out,
         * HAVE_FIPS_VERSION >= 2 */
 #if defined(HAVE_CHACHA) && defined(HAVE_POLY1305)
         case WC_CHACHA20_POLY1305_TYPE:
+        {
+            byte computedTag[CHACHA20_POLY1305_AEAD_AUTHTAG_SIZE];
+            if (!ctx->enc) {
+                /* Save the expected tag before _Final() overwrites
+                 * ctx->authTag */
+                XMEMCPY(computedTag, ctx->authTag, sizeof(computedTag));
+            }
             if (wc_ChaCha20Poly1305_Final(&ctx->cipher.chachaPoly,
                                           ctx->authTag) != 0) {
                 WOLFSSL_MSG("wc_ChaCha20Poly1305_Final failed");
                 return WOLFSSL_FAILURE;
-            else {
-                *outl = 0;
-                return WOLFSSL_SUCCESS;
+            if (!ctx->enc) {
+                /* ctx->authTag now holds computed tag; computedTag holds
+                 * expected */
+                int tagErr = wc_ChaCha20Poly1305_CheckTag(computedTag,
+                                                          ctx->authTag);
+                ForceZero(computedTag, sizeof(computedTag));
+                if (tagErr != 0) {
+                    WOLFSSL_MSG("ChaCha20-Poly1305 tag mismatch");
+                    return WOLFSSL_FAILURE;
+                }
-            break;
+            *outl = 0;
+            return WOLFSSL_SUCCESS;
+        }
+        break;
 #endif
 #ifdef WOLFSSL_SM4_GCM
         case WC_SM4_GCM_TYPE:
```

<https://github.com/wolfSSL/wolfssl/commit/1faddd640>

1. 2026-03-29
2. 2026-04-05
3. 2026-05-07
4. 2026-05-07
5. 2026-05-20

3d2166ecae422707fc5deddb8399d45cfe7100af81f11c4db5e69c322ab9e357919f53f646abd59e37131b10cd08784ab37185431b9cfd803d3bc0f26297cddf

Committed 2026-04-05 23:37 UTC

Revealed 2026-05-20 07:40 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-RSSMAMA7%22%2C%22bug_class%22%3A%22crypto-failure%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A42%3A34%2B00%3A00%22%2C%22description%22%3Anull%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22wolfSSL%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3Anull%2C%22title%22%3A%22wolfssl%20evp%20chacha20%20poly1305%20poly1305%20tag%20never%20verifi%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-RSSMAMA7",
  "bug_class": "crypto-failure",
  "created_at": "2026-03-29T20:42:34+00:00",
  "description": null,
  "project": "wolfSSL",
  "technical_details": null,
  "title": "wolfssl evp chacha20 poly1305 poly1305 tag never verifi",
```
