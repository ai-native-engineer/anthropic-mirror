<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-SB4PHA43 -->

# ANT-2026-SB4PHA43 · wolfssl/wolfssl

## crypto-failure medium

[CVE-2026-5446](https://nvd.nist.gov/vuln/detail/CVE-2026-5446)
[GHSA-vgv9-mv66-mpc7](https://github.com/advisories/GHSA-vgv9-mv66-mpc7)

Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Calif.

# ANT-2026-SB4PHA43: ARIA-GCM Nonce Reuse in TLS 1.2 Record Encryption in wolfSSL

The ARIA-GCM implementation reuses nonces when encrypting TLS 1.2 records.

**Project:** wolfSSL

This finding was identified by static analysis and has not yet been dynamically reproduced. A trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-SB4PHA43.

---

**Reference:** ANT-2026-SB4PHA43

Triage and disclosure were performed by Calif.

UPSTREAM FIX

The change that resolved this finding.

```
diff --git a/src/internal.c b/src/internal.c
index 516f7ccc683..70a7f42569d 100644
--- a/src/internal.c
+++ b/src/internal.c
@@ -19714,7 +19714,9 @@ static int DoDtlsHandShakeMsg(WOLFSSL* ssl, byte* input, word32* inOutIdx,
 #if (!defined(NO_PUBLIC_GCM_SET_IV) && \
     ((defined(HAVE_FIPS) || defined(HAVE_SELFTEST)) && \
     (!defined(HAVE_FIPS_VERSION) || (HAVE_FIPS_VERSION < 2)))) || \
-    (defined(HAVE_POLY1305) && defined(HAVE_CHACHA))
+    (defined(HAVE_POLY1305) && defined(HAVE_CHACHA)) || \
+    defined(HAVE_ARIA) || \
+    defined(WOLFSSL_SM4_GCM) || defined(WOLFSSL_SM4_CCM)
 static WC_INLINE void AeadIncrementExpIV(WOLFSSL* ssl)
     int i;
@@ -20701,10 +20703,9 @@ static WC_INLINE int Encrypt(WOLFSSL* ssl, byte* out, const byte* input,
                 sizeof(ssl->encrypt.sanityCheck));
         #endif

-        #if defined(BUILD_AESGCM) || defined(HAVE_AESCCM) || defined(HAVE_ARIA)
+        #if defined(BUILD_AESGCM) || defined(HAVE_AESCCM)
             if (ssl->specs.bulk_cipher_algorithm == wolfssl_aes_ccm ||
-                ssl->specs.bulk_cipher_algorithm == wolfssl_aes_gcm ||
-                ssl->specs.bulk_cipher_algorithm == wolfssl_aria_gcm)
+                ssl->specs.bulk_cipher_algorithm == wolfssl_aes_gcm)
                 /* finalize authentication cipher */
 #if !defined(NO_PUBLIC_GCM_SET_IV) && \
@@ -20715,7 +20716,17 @@ static WC_INLINE int Encrypt(WOLFSSL* ssl, byte* out, const byte* input,
                 if (ssl->encrypt.nonce)
                     ForceZero(ssl->encrypt.nonce, AESGCM_NONCE_SZ);
-        #endif /* BUILD_AESGCM || HAVE_AESCCM || HAVE_ARIA */
+        #endif /* BUILD_AESGCM || HAVE_AESCCM */
+        #ifdef HAVE_ARIA
+            if (ssl->specs.bulk_cipher_algorithm == wolfssl_aria_gcm)
+            {
+                /* finalize authentication cipher — wc_AriaEncrypt is
+                 * stateless, so the explicit IV must always advance */
+                AeadIncrementExpIV(ssl);
+                if (ssl->encrypt.nonce)
+                    ForceZero(ssl->encrypt.nonce, AESGCM_NONCE_SZ);
+            }
+        #endif /* HAVE_ARIA */
         #if defined(WOLFSSL_SM4_GCM) || defined(WOLFSSL_SM4_CCM)
             if (ssl->specs.bulk_cipher_algorithm == wolfssl_sm4_ccm ||
                 ssl->specs.bulk_cipher_algorithm == wolfssl_sm4_gcm)
```

<https://github.com/wolfSSL/wolfssl/commit/6495e8e94>

1. 2026-03-29
2. 2026-05-07
3. 2026-05-07
4. 2026-05-07
5. 2026-05-20

42db4adeeadfd87fee4e773a054ec682b406867ffe8d0e9cc84b22a2c51a7726959887e1bc23098eea81effa882b38313a69a5acc6a465e8d3162b57e754ed79

Committed 2026-05-07 00:03 PT

Revealed 2026-05-20 00:40 PT

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-SB4PHA43%22%2C%22bug_class%22%3A%22Cryptographic%20Nonce%20Reuse%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A42%3A29%2B00%3A00%22%2C%22description%22%3A%22The%20ARIA-GCM%20implementation%20reuses%20nonces%20when%20encrypting%20TLS%201.2%20records.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22wolfSSL%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3Anull%2C%22title%22%3A%22ARIA-GCM%20Nonce%20Reuse%20in%20TLS%201.2%20Record%20Encryption%20in%20wolfSSL%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-SB4PHA43",
  "bug_class": "Cryptographic Nonce Reuse",
  "created_at": "2026-03-29T20:42:29+00:00",
  "description": "The ARIA-GCM implementation reuses nonces when encrypting TLS 1.2 records.",
  "project": "wolfSSL",
  "technical_details": null,
  "title": "ARIA-GCM Nonce Reuse in TLS 1.2 Record Encryption in wolfSSL",
```
