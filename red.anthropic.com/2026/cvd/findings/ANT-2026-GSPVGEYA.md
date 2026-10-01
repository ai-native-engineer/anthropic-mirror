<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-GSPVGEYA -->

# ANT-2026-GSPVGEYA · gpg/libgcrypt

## stack-buffer-overflow medium

[CVE-2026-41990](https://nvd.nist.gov/vuln/detail/CVE-2026-41990)
[GHSA-78pv-qq8x-94px](https://github.com/advisories/GHSA-78pv-qq8x-94px)

Security research firm -
Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Calif.

# ANT-2026-GSPVGEYA: ML-DSA context string stack buffer overflow

In cipher/dilithium.c, dilithium\_sign() and dilithium\_verify() declare `uint8_t pre[257]` and loop-copy `ctxlen` bytes of the caller's context into it with no bound check. The reference implementation's `if(ctxlen>255) return -1;` guard in dilithium-dep.c is wrapped in `#ifndef DILITHIUM_INTERNAL_API_ONLY`, but libgcrypt defines that macro at dilithium.c:85, so the check is compiled out. The context arrives from the public gcry\_pk\_sign/gcry\_pk\_verify API via the `(label ...)` S-expression token, which pubkey-util.c stores into ctx.label/ctx.labellen with no length cap and pubkey-dilithium.c passes straight through. An attacker who can influence the label to exceed 255 bytes overwrites the stack past `pre[]`, smashing saved registers/return address and likely achieving code execution during signature verification.

**Project:** gpg/libgcrypt
**Location:** `cipher/dilithium.c:189`

dilithium.c:189 declares `uint8_t pre[257]` and lines 199-200 execute `for(i=0;i<ctxlen;i++) pre[2+i]=ctx[i];` with `ctxlen` as an unchecked size\_t. The upstream 255-byte guard at dilithium-dep.c:1061/1235 is excluded by `#define DILITHIUM_INTERNAL_API_ONLY` (dilithium.c:85), and no replacement cap exists anywhere in the active gcry\_pk\_verify → mldsa\_verify → dilithium\_verify path, so any label >255 bytes writes past the end of the stack array.

1. Attacker supplies an ML-DSA signed object or handshake message whose domain-separation context/label is longer than 255 bytes.
2. Application builds the data S-expression including `(label #...>255 bytes...#)` and calls gcry\_pk\_verify().
3. \_gcry\_pk\_util\_data\_to\_mpi reads the label via sexp\_nth\_buffer with no length cap (pubkey-util.c:760-777).
4. mldsa\_verify passes ctx->label / ctx->labellen directly to dilithium\_verify (pubkey-dilithium.c:356-357).
5. dilithium\_verify loop-copies ctxlen bytes into the 257-byte stack array `pre[]`, overflowing it and overwriting saved registers / return address.

## Suggested Fix

Enforce the FIPS-204 / reference-implementation limit that the ML-DSA context string is at most 255 bytes before copying into the fixed `pre[]` prefix buffer, regardless of which internal API variant is compiled (e.g., re-add `if(ctxlen>255) return -1;` in dilithium\_sign/dilithium\_verify or cap labellen in pubkey-util.c / mldsa\_sign/mldsa\_verify).

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-GSPVGEYA.

---

**Reference:** ANT-2026-GSPVGEYA

Triage and disclosure were performed by Calif.

UPSTREAM FIX

The change that resolved this finding.

```
diff --git a/cipher/dilithium.c b/cipher/dilithium.c
index 955feb2ae..212c4afe5 100644
--- a/cipher/dilithium.c
+++ b/cipher/dilithium.c
@@ -82,6 +82,7 @@
 #include "gcrypt-int.h"
 #include "const-time.h"

+/* With glue code, we only use the "_internal" API of Dilithium.  */
 #define DILITHIUM_INTERNAL_API_ONLY 1

 #include "dilithium.h"
@@ -120,23 +121,33 @@ static int crypto_sign_verify_internal_5 (const uint8_t *sig, size_t siglen,
                                           const uint8_t *pre, size_t prelen,
                                           const uint8_t *pk);

-int
+gpg_err_code_t
 dilithium_keypair (int algo, uint8_t *pk, uint8_t *sk,
                    const uint8_t seed[SEEDBYTES])
+  int r;
+
   switch (algo)
     case GCRY_MLDSA44:
-      return crypto_sign_keypair_internal_2 (pk, sk, seed);
+      r = crypto_sign_keypair_internal_2 (pk, sk, seed);
+      break;
     case GCRY_MLDSA65:
     default:
-      return crypto_sign_keypair_internal_3 (pk, sk, seed);
+      r = crypto_sign_keypair_internal_3 (pk, sk, seed);
+      break;
     case GCRY_MLDSA87:
-      return crypto_sign_keypair_internal_5 (pk, sk, seed);
+      r = crypto_sign_keypair_internal_5 (pk, sk, seed);
+      break;
+
+  if (r < 0)
+    return GPG_ERR_INTERNAL;
+
+  return 0;

-int
+gpg_err_code_t
 dilithium_sign (int algo, uint8_t *sig, size_t siglen,
                 const uint8_t *m, size_t mlen,
                 const uint8_t *ctx, size_t ctxlen,
@@ -145,9 +156,17 @@ dilithium_sign (int algo, uint8_t *sig, size_t siglen,
   size_t i;
   uint8_t pre[257];
   size_t prelen;
+  int r;

-  if (ctx == NULL && ctxlen == -1)
-    prelen = 0;
+  if (ctx == NULL)
+    {
+      if (ctxlen == -1)
+        prelen = 0;
+      else
+        return GPG_ERR_INV_DATA;
+    }
+  else if (ctxlen > 255)
+    return GPG_ERR_INV_DATA;
   else
       /* Prepare pre = (0, ctxlen, ctx) */
@@ -158,28 +177,44 @@ dilithium_sign (int algo, uint8_t *sig, size_t siglen,
       prelen = 2 + ctxlen;

+  /*
+   * Note that the second argument of the upstream routine is the
+   * pointer to output length of signature.  It assumes the first
+   * argument (pointer to output signature) should have correct (or
+   * more) length, beforehand.
+   *
+   * Before calling the routine, we should check the length.
+   */
   switch (algo)
     case GCRY_MLDSA44:
       if (siglen != CRYPTO_BYTES_2)
-        return -1;
-      return crypto_sign_signature_internal_2 (sig, &siglen, m, mlen,
-                                               pre, prelen, rnd, sk);
+        return GPG_ERR_INV_DATA;
+      r = crypto_sign_signature_internal_2 (sig, &siglen, m, mlen,
+                                            pre, prelen, rnd, sk);
+      break;
     case GCRY_MLDSA65:
     default:
       if (siglen != CRYPTO_BYTES_3)
-        return -1;
-      return crypto_sign_signature_internal_3 (sig, &siglen, m, mlen,
-                                               pre, prelen, rnd, sk);
+        return GPG_ERR_INV_DATA;
+      r = crypto_sign_signature_internal_3 (sig, &siglen, m, mlen,
+                                            pre, prelen, rnd, sk);
+      break;
     case GCRY_MLDSA87:
       if (siglen != CRYPTO_BYTES_5)
-        return -1;
-      return crypto_sign_signature_internal_5 (sig, &siglen, m, mlen,
-                                               pre, prelen, rnd, sk);
+        return GPG_ERR_INV_DATA;
+      r = crypto_sign_signature_internal_5 (sig, &siglen, m, mlen,
+                                            pre, prelen, rnd, sk);
+      break;
+
+  if (r < 0)
+    return GPG_ERR_INTERNAL;
+
+  return 0;

-int
+gpg_err_code_t
 dilithium_verify (int algo, const uint8_t *sig, size_t siglen,
                   const uint8_t *m, size_t mlen,
                   const uint8_t *ctx, size_t ctxlen,
@@ -188,9 +223,17 @@ dilithium_verify (int algo, const uint8_t *sig, size_t siglen,
   size_t i;
   uint8_t pre[257];
   size_t prelen;
+  int r;

-  if (ctx == NULL && ctxlen == -1)
-    prelen = 0;
+  if (ctx == NULL)
+    {
+      if (ctxlen == -1)
+        prelen = 0;
+      else
+        return GPG_ERR_INV_DATA;
+    }
+  else if (ctxlen > 255)
+    return GPG_ERR_INV_DATA;
   else
       /* Prepare pre = (0, ctxlen, ctx) */
@@ -204,16 +247,24 @@ dilithium_verify (int algo, const uint8_t *sig, size_t siglen,
   switch (algo)
     case GCRY_MLDSA44:
-      return crypto_sign_verify_internal_2 (sig, siglen, m, mlen,
-                                            pre, prelen, pk);
+      r = crypto_sign_verify_internal_2 (sig, siglen, m, mlen,
+                                         pre, prelen, pk);
+      break;
     case GCRY_MLDSA65:
     default:
-      return crypto_sign_verify_internal_3 (sig, siglen, m, mlen,
-                                            pre, prelen, pk);
+      r = crypto_sign_verify_internal_3 (sig, siglen, m, mlen,
+                                         pre, prelen, pk);
+      break;
     case GCRY_MLDSA87:
-      return crypto_sign_verify_internal_5 (sig, siglen, m, mlen,
-                                            pre, prelen, pk);
+      r = crypto_sign_verify_internal_5 (sig, siglen, m, mlen,
+                                         pre, prelen, pk);
+      break;
+
+  if (r < 0)
+    return GPG_ERR_BAD_SIGNATURE;
+
+  return 0;

 typedef struct {
diff --git a/cipher/dilithium.h b/cipher/dilithium.h
index dd3597a53..1e868e1e6 100644
--- a/cipher/dilithium.h
+++ b/cipher/dilithium.h
@@ -64,16 +64,16 @@
 #define DILITHIUM_SIGN_STACK_BURN (161 * 1024)
 #define DILITHIUM_VERIFY_STACK_BURN (122 * 1024)

-int dilithium_keypair (int algo, uint8_t *pk, uint8_t *sk,
-                       const uint8_t seed[SEEDBYTES]);
-int dilithium_sign (int algo, uint8_t *sig, size_t siglen,
-                    const uint8_t *m, size_t mlen,
-                    const uint8_t *ctx, size_t ctxlen,
-                    const uint8_t *sk, const uint8_t rnd[RNDBYTES]);
-int dilithium_verify (int algo, const uint8_t *sig, size_t siglen,
-                      const uint8_t *m, size_t mlen,
-                      const uint8_t *ctx, size_t ctxlen,
-                      const uint8_t *pk);
+gpg_err_code_t dilithium_keypair (int algo, uint8_t *pk, uint8_t *sk,
+                                  const uint8_t seed[SEEDBYTES]);
+gpg_err_code_t dilithium_sign (int algo, uint8_t *sig, size_t siglen,
+                               const uint8_t *m, size_t mlen,
+                               const uint8_t *ctx, size_t ctxlen,
+                               const uint8_t *sk, const uint8_t rnd[RNDBYTES]);
+gpg_err_code_t dilithium_verify (int algo, const uint8_t *sig, size_t siglen,
+                                 const uint8_t *m, size_t mlen,
+                                 const uint8_t *ctx, size_t ctxlen,
+                                 const uint8_t *pk);
 #endif

 #if defined(DILITHIUM_MODE)
diff --git a/cipher/pubkey-dilithium.c b/cipher/pubkey-dilithium.c
index 03958bb08..8c3f650e5 100644
--- a/cipher/pubkey-dilithium.c
+++ b/cipher/pubkey-dilithium.c
@@ -170,7 +170,7 @@ mldsa_generate (const gcry_sexp_t genparms, gcry_sexp_t *r_skey)
       memcpy (seed, seed_supplied, SEEDBYTES);

-  dilithium_keypair (info->algo, pk, sk, seed);
+  rc = dilithium_keypair (info->algo, pk, sk, seed);
   _gcry_burn_stack (DILITHIUM_KEYPAIR_STACK_BURN);

   if (!rc)
@@ -206,7 +206,6 @@ mldsa_sign (gcry_sexp_t *r_sig, gcry_sexp_t s_data, gcry_sexp_t keyparms)
   size_t data_len;
   const unsigned char *sk;
   const struct mldsa_info *info = mldsa_get_info (keyparms);
-  int r;

   if (!info)
     return GPG_ERR_PUBKEY_ALGO;
@@ -258,17 +257,14 @@ mldsa_sign (gcry_sexp_t *r_sig, gcry_sexp_t s_data, gcry_sexp_t keyparms)
   else
     randombytes (rnd, RNDBYTES);
   if (ctx.flags & PUBKEY_FLAG_NO_PREFIX)
-    r = dilithium_sign (info->algo, sig, info->sig_len, data, data_len,
-                        NULL, -1, sk, rnd);
+    rc = dilithium_sign (info->algo, sig, info->sig_len, data, data_len,
+                         NULL, -1, sk, rnd);
   else
-    r = dilithium_sign (info->algo, sig, info->sig_len, da
… (truncated)
```

<https://github.com/gpg/libgcrypt/commit/905e00f046a71e5670517779afaf85a354952832>

1. 2026-04-13
2. 2026-04-15
3. 2026-04-15
4. 2026-05-28

86f014c5715067bbe17ca099b1f5c66cb367ce1167c9d0c77c15ca73594cb5c2a6ae966ae8809431af4cb2bc6eb0b7201c5ebdd8f1e2ae2f29987915712a8300

Committed 2026-05-28 08:09 PT

Revealed 2026-08-17 10:47 PT

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-GSPVGEYA%22%2C%22bug_class%22%3A%22Stack%20Buffer%20Overflow%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-16T02%3A33%3A49%2B00%3A00%22%2C%22description%22%3A%22In%20cipher/dilithium.c%2C%20dilithium_sign%28%29%20and%20dilithium_verify%28%29%20declare%20%60uint8_t%20pre%5B257%5D%60%20and%20loop-copy%20%60ctxlen%60%20bytes%20of%20the%20caller%27s%20context%20into%20it%20with%20no%20bound%20check.%20The%20reference%20implementation%27s%20%60if%28ctxlen%3E255%29%20return%20-1%3B%60%20guard%20in%20dilithium-dep.c%20is%20wrapped%20in%20%60%23ifndef%20DILITHIUM_INTERNAL_API_ONLY%60%2C%20but%20libgcrypt%20defines%20that%20macro%20at%20dilithium.c%3A85%2C%20so%20the%20check%20is%20compiled%20out.%20The%20context%20arrives%20from%20the%20public%20gcry_pk_sign/gcry_pk_verify%20API%20via%20the%20%60%28label%20...%29%60%20S-expression%20token%2C%20which%20pubkey-util.c%20stores%20into%20ctx.label/ctx.labellen%20with%20no%20length%20cap%20and%20pubkey-dilithium.c%20passes%20straight%20through.%20An%20attacker%20who%20can%20influence%20the%20label%20to%20exceed%20255%20bytes%20overwrites%20the%20stack%20past%20%60pre%5B%5D%60%2C%20smashing%20saved%20registers/return%20address%20and%20likely%20achieving%20code%20execution%20during%20signature%20verification.%22%2C%22discovered_at%22%3A%222026-04-02T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22cipher/dilithium.c%3A189%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22gpg/libgcrypt%22%2C%22reproduction%22%3A%5B%221.%20Attacker%20supplies%20an%20ML-DSA%20signed%20object%20or%20handshake%20message%20whose%20domain-separation%20context/label%20is%20longer%20than%20255%20bytes.%22%2C%222.%20Application%20builds%20the%20data%20S-expression%20including%20%60%28label%20%23...%3E255%20bytes...%23%29%60%20and%20calls%20gcry_pk_verify%28%29.%22%2C%223.%20_gcry_pk_util_data_to_mpi%20reads%20the%20label%20via%20sexp_nth_buffer%20with%20no%20length%20cap%20%28pubkey-util.c%3A760-777%29.%22%2C%224.%20mldsa_verify%20passes%20ctx-%3Elabel%20/%20ctx-%3Elabellen%20directly%20to%20dilithium_verify%20%28pubkey-dilithium.c%3A356-357%29.%22%2C%225.%20dilithium_verify%20loop-copies%20ctxlen%20bytes%20into%20the%20257-byte%20stack%20array%20%60pre%5B%5D%60%2C%20overflowing%20it%20and%20overwriting%20saved%20registers%20/%20return%20address.%22%5D%2C%22technical_details%22%3A%22dilithium.c%3A189%20declares%20%60uint8_t%20pre%5B257%5D%60%20and%20lines%20199-200%20execute%20%60for%28i%3D0%3Bi%3Cctxlen%3Bi%2B%2B%29%20pre%5B2%2Bi%5D%3Dctx%5Bi%5D%3B%60%20with%20%60ctxlen%60%20as%20an%20unchecked%20size_t.%20The%20upstream%20255-byte%20guard%20at%20dilithium-dep.c%3A1061/1235%20is%20excluded%20by%20%60%23define%20DILITHIUM_INTERNAL_API_ONLY%60%20%28dilithium.c%3A85%29%2C%20and%20no%20replacement%20cap%20exists%20anywhere%20in%20the%20active%20gcry_pk_verify%20%E2%86%92%20mldsa_verify%20%E2%86%92%20dilithium_verify%20path%2C%20so%20any%20label%20%3E255%20bytes%20writes%20past%20the%20end%20of%20the%20stack%20array.%22%2C%22title%22%3A%22ML-DSA%20context%20string%20stack%20buffer%20overflow%22%2C%22vendor_severity%22%3Anull%7D)

```
  "ant_id": "ANT-2026-GSPVGEYA",
  "bug_class": "Stack Buffer Overflow",
  "created_at": "2026-04-16T02:33:49+00:00",
  "description": "In cipher/dilithium.c, dilithium_sign() and dilithium_verify() declare `uint8_t pre[257]` and loop-copy `ctxlen` bytes of the caller's context into it with no bound check. The reference implementation's `if(ctxlen>255) return -1;` guard in dilithium-dep.c is wrapped in `#ifndef DILITHIUM_INTERNAL_API_ONLY`, but libgcrypt defines that macro at dilithium.c:85, so the check is compiled out. The context arrives from the public gcry_pk_sign/gcry_pk_verify API via the `(label ...)` S-expression token, which pubkey-util.c stores into ctx.label/ctx.labellen with no length cap and pubkey-dilithium.c passes straight through. An attacker who can influence the label to exceed 255 bytes overwrites the stack past `pre[]`, smashing saved registers/return address and likely achieving code execution during signature verification.",
  "discovered_at": "2026-04-02T00:00:00+00:00",
  "location": "cipher/dilithium.c:189",
  "project": "gpg/libgcrypt",
    "1. Attacker supplies an ML-DSA signed object or handshake message whose domain-separation context/label is longer than 255 bytes.",
    "2. Application builds the data S-expression including `(label #...>255 bytes...#)` and calls gcry_pk_verify().",
    "3. _gcry_pk_util_data_to_mpi reads the label via sexp_nth_buffer with no length cap (pubkey-util.c:760-777).",
    "4. mldsa_verify passes ctx->label / ctx->labellen directly to dilithium_verify (pubkey-dilithium.c:356-357).",
    "5. dilithium_verify loop-copies ctxlen bytes into the 257-byte stack array `pre[]`, overflowing it and overwriting saved registers / return address."
  "technical_details": "dilithium.c:189 declares `uint8_t pre[257]` and lines 199-200 execute `for(i=0;i<ctxlen;i++) pre[2+i]=ctx[i];` with `ctxlen` as an unchecked size_t. The upstream 255-byte guard at dilithium-dep.c:1061/1235 is excluded by `#define DILITHIUM_INTERNAL_API_ONLY` (dilithium.c:85), and no replacement cap exists anywhere in the active gcry_pk_verify → mldsa_verify → dilithium_verify path, so any label >255 bytes writes past the end of the stack array.",
  "title": "ML-DSA context string stack buffer overflow",
  "vendor_severity": null
```
