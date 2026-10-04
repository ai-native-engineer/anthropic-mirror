<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-AYWQW7P2 -->

# ANT-2026-AYWQW7P2 · openssl/openssl

## use-after-free critical

[CVE-2026-45447](https://nvd.nist.gov/vuln/detail/CVE-2026-45447)
[GHSA-f684-cpcq-j565](https://github.com/advisories/GHSA-f684-cpcq-j565)

Maintainer critical

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Calif.

# ANT-2026-AYWQW7P2: PKCS7\_verify frees caller-owned `indata` BIO when `digestAlgorithms` SET is empty

In PKCS7\_dataInit(), when the attacker-supplied SignedData has an empty md\_algs SET (DER `31 00`), no BIO\_f\_md filter chain is built and the caller's indata BIO pointer is returned verbatim instead of a library-owned chain. PKCS7\_verify()'s unconditional cleanup then calls BIO\_free\_all() on that pointer, freeing caller-owned memory. Any consumer following the documented SMIME\_read\_PKCS7 → PKCS7\_verify → BIO\_free(indata) pattern (including apps/smime.c) then performs a second BIO\_free on the freed 128-byte struct bio\_st. The second free writes to offset +88 (refcount decrement) and, if the chunk has been reclaimed with suitable contents, dereferences a vtable pointer at offset +8 for an attacker-influenced indirect call. The trigger is valid DER and reachable via an ordinary S/MIME email with a CA-issued certificate.

**Project:** openssl/openssl
**Location:** `crypto/pkcs7/pk7_smime.c:349-356 (sink); crypto/pkcs7/pk7_doit.c:304-306,403-406 (root cause)`

ASAN: heap-use-after-free, WRITE of size 4 at freed heap address in CRYPTO\_DOWN\_REF. The empty-SET case leaves `out == NULL` in PKCS7\_dataInit so it returns `out = bio` (the caller's pointer) directly; PKCS7\_verify's cleanup assumes p7bio has a library-owned head and calls BIO\_free\_all(p7bio), freeing the caller's BIO. The caller's subsequent BIO\_free(indata) then atomically decrements `a->references` at +88 in freed memory and, if ret hits 0, calls `a->method->destroy(a)` through a function pointer read from offset +8 of the reclaimed chunk.

**Crash trace:**

```
==NNN==ERROR: AddressSanitizer: heap-use-after-free on address 0x... at pc ...
WRITE of size 4 at 0x... thread T0
    #0 ... in CRYPTO_DOWN_REF include/internal/refcount.h:64
    #1 ... in BIO_free crypto/bio/bio_lib.c:126
    #2 ... in smime_main apps/smime.c:732
freed by thread T0 here:
    #3 ... in PKCS7_verify crypto/pkcs7/pk7_smime.c:356
previously allocated by thread T0 here:
    #4 ... in multi_split crypto/asn1/asn_mime.c:678
```

1. Craft a multipart/signed S/MIME message whose PKCS7 SignedData has md\_algs = empty SET (DER 31 00), with a valid signer cert and SignerInfo.
2. Deliver the message to the victim (email, gateway, or file fed to `openssl smime -verify`).
3. Victim calls PKCS7\_verify; PKCS7\_dataInit returns the caller's indata; cleanup BIO\_free\_all frees it (first free).
4. Victim's own BIO\_free(indata) runs: CRYPTO\_DOWN\_REF writes 4 bytes at +88 of the freed/reclaimed chunk.
5. If the slot was reclaimed with ref==1 and a fake BIO\_METHOD\* at +8, execution falls through to a->method->destroy(a) — attacker-controlled indirect call.

## Suggested Fix

Either (1) in PKCS7\_verify cleanup, add `if (p7bio == indata) p7bio = NULL;` before BIO\_free\_all(p7bio); or (2) in PKCS7\_dataInit, when no digest filters were pushed and a caller bio was supplied, reject the input or push a BIO\_f\_null() so the returned chain always has a library-owned head.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-AYWQW7P2.

---

**Reference:** ANT-2026-AYWQW7P2

Triage and disclosure were performed by Calif.

```
diff --git a/crypto/pkcs7/pk7_smime.c b/crypto/pkcs7/pk7_smime.c
index 4bf26331c1a05..49129690deb96 100644
--- a/crypto/pkcs7/pk7_smime.c
+++ b/crypto/pkcs7/pk7_smime.c
@@ -221,6 +221,7 @@ int PKCS7_verify(PKCS7 *p7, const STACK_OF(X509) *certs, X509_STORE *store,
     int i, j = 0, k, ret = 0;
     BIO *p7bio = NULL;
     BIO *tmpout = NULL;
+    BIO *next = NULL;
     const PKCS7_CTX *p7_ctx;

     if (p7 == NULL) {
@@ -351,9 +352,11 @@ int PKCS7_verify(PKCS7 *p7, const STACK_OF(X509) *certs, X509_STORE *store,
         BIO_free(tmpout);
     X509_STORE_CTX_free(cert_ctx);
     OPENSSL_free(buf);
-    if (indata != NULL)
-        BIO_pop(p7bio);
-    BIO_free_all(p7bio);
+    while (p7bio != NULL && p7bio != indata) {
+        next = BIO_pop(p7bio);
+        BIO_free(p7bio);
+        p7bio = next;
+    }
     sk_X509_free(signers);
     sk_X509_free(untrusted);
     return ret;
```

<https://github.com/openssl/openssl/commit/f4129fbe3cde786d363510069fe297234f99be8f>

1. 2026-03-28
2. 2026-05-28
3. 2026-05-28
4. 2026-06-09
5. 2026-08-17

c437365f3af15fb6db66d201e976b79c3cd9f89a37e15f897449b63d820ae951ecb1b647c56e7bc44774c928fbadf2437715bff69c2a687000563ff2260c9acc

Committed 2026-05-28 15:09 UTC

Revealed 2026-08-17 17:47 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-AYWQW7P2%22%2C%22bug_class%22%3A%22Use-After-Free%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-05-20T01%3A49%3A21%2B00%3A00%22%2C%22description%22%3A%22In%20PKCS7_dataInit%28%29%2C%20when%20the%20attacker-supplied%20SignedData%20has%20an%20empty%20md_algs%20SET%20%28DER%20%6031%2000%60%29%2C%20no%20BIO_f_md%20filter%20chain%20is%20built%20and%20the%20caller%27s%20indata%20BIO%20pointer%20is%20returned%20verbatim%20instead%20of%20a%20library-owned%20chain.%20PKCS7_verify%28%29%27s%20unconditional%20cleanup%20then%20calls%20BIO_free_all%28%29%20on%20that%20pointer%2C%20freeing%20caller-owned%20memory.%20Any%20consumer%20following%20the%20documented%20SMIME_read_PKCS7%20%E2%86%92%20PKCS7_verify%20%E2%86%92%20BIO_free%28indata%29%20pattern%20%28including%20apps/smime.c%29%20then%20performs%20a%20second%20BIO_free%20on%20the%20freed%20128-byte%20struct%20bio_st.%20The%20second%20free%20writes%20to%20offset%20%2B88%20%28refcount%20decrement%29%20and%2C%20if%20the%20chunk%20has%20been%20reclaimed%20with%20suitable%20contents%2C%20dereferences%20a%20vtable%20pointer%20at%20offset%20%2B8%20for%20an%20attacker-influenced%20indirect%20call.%20The%20trigger%20is%20valid%20DER%20and%20reachable%20via%20an%20ordinary%20S/MIME%20email%20with%20a%20CA-issued%20certificate.%22%2C%22discovered_at%22%3A%222026-03-28T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22crypto/pkcs7/pk7_smime.c%3A349-356%20%28sink%29%3B%20crypto/pkcs7/pk7_doit.c%3A304-306%2C403-406%20%28root%20cause%29%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22openssl%22%2C%22reproduction%22%3A%5B%221.%20Craft%20a%20multipart/signed%20S/MIME%20message%20whose%20PKCS7%20SignedData%20has%20md_algs%20%3D%20empty%20SET%20%28DER%2031%2000%29%2C%20with%20a%20valid%20signer%20cert%20and%20SignerInfo.%22%2C%222.%20Deliver%20the%20message%20to%20the%20victim%20%28email%2C%20gateway%2C%20or%20file%20fed%20to%20%60openssl%20smime%20-verify%60%29.%22%2C%223.%20Victim%20calls%20PKCS7_verify%3B%20PKCS7_dataInit%20returns%20the%20caller%27s%20indata%3B%20cleanup%20BIO_free_all%20frees%20it%20%28first%20free%29.%22%2C%224.%20Victim%27s%20own%20BIO_free%28indata%29%20runs%3A%20CRYPTO_DOWN_REF%20writes%204%20bytes%20at%20%2B88%20of%20the%20freed/reclaimed%20chunk.%22%2C%225.%20If%20the%20slot%20was%20reclaimed%20with%20ref%3D%3D1%20and%20a%20fake%20BIO_METHOD%2A%20at%20%2B8%2C%20execution%20falls%20through%20to%20a-%3Emethod-%3Edestroy%28a%29%20%E2%80%94%20attacker-controlled%20indirect%20call.%22%5D%2C%22technical_details%22%3A%22ASAN%3A%20heap-use-after-free%2C%20WRITE%20of%20size%204%20at%20freed%20heap%20address%20in%20CRYPTO_DOWN_REF.%20The%20empty-SET%20case%20leaves%20%60out%20%3D%3D%20NULL%60%20in%20PKCS7_dataInit%20so%20it%20returns%20%60out%20%3D%20bio%60%20%28the%20caller%27s%20pointer%29%20directly%3B%20PKCS7_verify%27s%20cleanup%20assumes%20p7bio%20has%20a%20library-owned%20head%20and%20calls%20BIO_free_all%28p7bio%29%2C%20freeing%20the%20caller%27s%20BIO.%20The%20caller%27s%20subsequent%20BIO_free%28indata%29%20then%20atomically%20decrements%20%60a-%3Ereferences%60%20at%20%2B88%20in%20freed%20memory%20and%2C%20if%20ret%20hits%200%2C%20calls%20%60a-%3Emethod-%3Edestroy%28a%29%60%20through%20a%20function%20pointer%20read%20from%20offset%20%2B8%20of%20the%20reclaimed%20chunk.%22%2C%22title%22%3A%22PKCS7_verify%20frees%20caller-owned%20%60indata%60%20BIO%20when%20%60digestAlgorithms%60%20SET%20is%20empty%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-AYWQW7P2",
  "bug_class": "Use-After-Free",
  "created_at": "2026-05-20T01:49:21+00:00",
  "description": "In PKCS7_dataInit(), when the attacker-supplied SignedData has an empty md_algs SET (DER `31 00`), no BIO_f_md filter chain is built and the caller's indata BIO pointer is returned verbatim instead of a library-owned chain. PKCS7_verify()'s unconditional cleanup then calls BIO_free_all() on that pointer, freeing caller-owned memory. Any consumer following the documented SMIME_read_PKCS7 → PKCS7_verify → BIO_free(indata) pattern (including apps/smime.c) then performs a second BIO_free on the freed 128-byte struct bio_st. The second free writes to offset +88 (refcount decrement) and, if the chunk has been reclaimed with suitable contents, dereferences a vtable pointer at offset +8 for an attacker-influenced indirect call. The trigger is valid DER and reachable via an ordinary S/MIME email with a CA-issued certificate.",
  "discovered_at": "2026-03-28T00:00:00+00:00",
  "location": "crypto/pkcs7/pk7_smime.c:349-356 (sink); crypto/pkcs7/pk7_doit.c:304-306,403-406 (root cause)",
  "project": "openssl",
    "1. Craft a multipart/signed S/MIME message whose PKCS7 SignedData has md_algs = empty SET (DER 31 00), with a valid signer cert and SignerInfo.",
    "2. Deliver the message to the victim (email, gateway, or file fed to `openssl smime -verify`).",
    "3. Victim calls PKCS7_verify; PKCS7_dataInit returns the caller's indata; cleanup BIO_free_all frees it (first free).",
    "4. Victim's own BIO_free(indata) runs: CRYPTO_DOWN_REF writes 4 bytes at +88 of the freed/reclaimed chunk.",
    "5. If the slot was reclaimed with ref==1 and a fake BIO_METHOD* at +8, execution falls through to a->method->destroy(a) — attacker-controlled indirect call."
  "technical_details": "ASAN: heap-use-after-free, WRITE of size 4 at freed heap address in CRYPTO_DOWN_REF. The empty-SET case leaves `out == NULL` in PKCS7_dataInit so it returns `out = bio` (the caller's pointer) directly; PKCS7_verify's cleanup assumes p7bio has a library-owned head and calls BIO_free_all(p7bio), freeing the caller's BIO. The caller's subsequent BIO_free(indata) then atomically decrements `a->references` at +88 in freed memory and, if ret hits 0, calls `a->method->destroy(a)` through a function pointer read from offset +8 of the reclaimed chunk.",
  "title": "PKCS7_verify frees caller-owned `indata` BIO when `digestAlgorithms` SET is empty",
```
