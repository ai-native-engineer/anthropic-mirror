<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-87DJGDRB -->

# ANT-2026-87DJGDRB · wolfssl/wolfssl

## heap-buffer-overflow low

[CVE-2026-12340](https://nvd.nist.gov/vuln/detail/CVE-2026-12340)
[GHSA-q349-x427-xg3w](https://github.com/advisories/GHSA-q349-x427-xg3w)

Maintainer low

Anthropic's analysis of this finding, sealed at approval.

# ANT-2026-87DJGDRB: Heap-buffer-overflow in sha.c:733

When wc\_PKCS7\_InitWithCert is given an attacker-supplied certificate buffer, ParseCertRelative calls CalcHashId\_ex to hash certificate data, which reaches wc\_ShaUpdate. With a crafted short input, wc\_ShaUpdate performs a 64-byte memcpy that reads past the end of the 8-byte input allocation. The attacker controls the certificate bytes and length supplied to the PKCS#7 API. The result is an out-of-bounds heap read that could disclose adjacent heap memory or crash the process.

**Project:** wolfssl/wolfssl
**Location:** `sha.c:733`

ASAN: "READ of size 64 at 0x704ffcee0058 ... 0 bytes after 8-byte region". During certificate parsing, CalcHashId\_ex passes a buffer/length derived from the malformed DER to wc\_ShaHash → wc\_ShaUpdate, which copies a full 64-byte SHA block without ensuring that many bytes remain in the source buffer, reading beyond the allocation.

**Crash trace (truncated — full trace in attached crash.log):**

```
INFO: Running with entropic power schedule (0xFF, 100).
INFO: Seed: 2781334584
INFO: Loaded 1 modules   (77873 inline 8-bit counters): 77873 [0x622b0ccbf5d8, 0x622b0ccd2609),
INFO: Loaded 1 PC tables (77873 PCs): 77873 [0x622b0ccd2610,0x622b0ce02920),
/out/fuzzer-wolfssl-misc: Running 1 inputs 1 time(s) each.
Running: /tmp/poc
EXIT_CODE:1

=== ASAN Report ===
=================================================================
==28==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x704ffcee0058 at pc 0x622b0c6cf4ab bp 0x7ffece072150 sp 0x7ffece071910
READ of size 64 at 0x704ffcee0058 thread T0
    #0 0x622b0c6cf4aa in __asan_memcpy /src/llvm-project/compiler-rt/lib/asan/asan_interceptors_memintrinsics.cpp:63:3
    #1 0x622b0ca76fcf in wc_ShaUpdate /src/wolf-ssl-ssh-fuzzers/oss-fuzz/projects/wolf-ssl-ssh/fuzzers/wolfssl/wolfssl/wolfcrypt/src/sha.c:733:13
    #2 0x622b0ca0217e in wc_ShaHash_ex /src/wolf-ssl-ssh-fuzzers/oss-fuzz/projects/wolf-ssl-ssh/fuzzers/wolfssl/wolfssl/wolfcrypt/src/hash.c:1381:24
    #3 0x622b0ca0217e in wc_ShaHash /src/wolf-ssl-ssh-fuzzers/oss-fuzz/projects/wolf-ssl-ssh/fuzzers/wolfssl/wolfssl/wolfcrypt/src/hash.c:1403:16
    #4 0x622b0c751247 in CalcHashId_ex /src/wolf-ssl-ssh-fuzzers/oss-fuzz/projects/wolf-ssl-ssh/fuzzers/wolfssl/wolfssl/wolfcrypt/src/asn.c:14544:15
    #5 0x622b0c751247 in ParseCertRelative /src/wolf-ssl-ssh-fuzzers/oss-fuzz/projects/wolf-ssl-ssh/fuzzers/wolfssl/wolfssl/wolfcrypt/src/asn.c
    #6 0x622b0c750122 in ParseCert /src/wolf-ssl-ssh-fuzzers/oss-fuzz/projects/wolf-ssl-ssh/fuzzers/wolfssl/wolfssl/wolfcrypt/src/asn.c:24900:11
    #7 0x622b0c7d6934 in wc_PKCS7_InitWithCert /src/wolf-ssl-ssh-fuzzers/oss-fuzz/projects/wolf-ssl-ssh/fuzzers/wolfssl/wolfssl/wolfcrypt/src/pkcs7.c:1173:15
    [... 12 more frames — full trace in crash.log]
```

1. Craft a short/malformed DER certificate buffer
2. Supply it to wc\_PKCS7\_InitWithCert()
3. ParseCertRelative → CalcHashId\_ex → wc\_ShaHash → wc\_ShaUpdate memcpy reads 64 bytes past the buffer end

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-87DJGDRB.

---

**Reference:** ANT-2026-87DJGDRB

Independent triage by an external party.

The change that resolved this finding.

```
diff --git a/wolfcrypt/src/asn.c b/wolfcrypt/src/asn.c
index 00be607506c..664d7862f5b 100644
--- a/wolfcrypt/src/asn.c
+++ b/wolfcrypt/src/asn.c
@@ -23380,6 +23380,10 @@ int ParseCertRelative(DecodedCert* cert, int type, int verify, void* cm,
         if (cert->extSubjKeyIdSet == 0 && cert->publicKey != NULL &&
                                                          cert->pubKeySize > 0) {
             if (cert->signatureOID == CTC_SM3wSM2) {
+                if (cert->pubKeySize < 65) {
+                    WOLFSSL_ERROR_VERBOSE(BUFFER_E);
+                    return BUFFER_E;
+                }
                 /* TODO: GmSSL creates IDs this way but whole public key info
                  * block should be hashed. */
                 ret = CalcHashId_ex(cert->publicKey + cert->pubKeySize - 65, 65,
```

<https://github.com/wolfSSL/wolfssl/commit/6bfb53f084a25198835a50796eca83f463a0e7be>

ADVISORY

<https://github.com/wolfSSL/wolfssl/pull/10641>

1. 2026-03-24
2. 2026-03-27
3. 2026-03-27
4. 2026-06-25
5. 2026-08-17

f35e4f410ec58dab28431670e173e03fd1e5105f8afefc79c7edd5117d684d3aa377d218762d2f1ab70c6262e31227885bacaf2062958b077e305e5aebc6c37d

Committed 2026-05-18 03:27 UTC

Revealed 2026-08-17 17:47 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-87DJGDRB%22%2C%22bug_class%22%3A%22Heap-buffer-overflow%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-24T18%3A46%3A56%2B00%3A00%22%2C%22description%22%3A%22When%20wc_PKCS7_InitWithCert%20is%20given%20an%20attacker-supplied%20certificate%20buffer%2C%20ParseCertRelative%20calls%20CalcHashId_ex%20to%20hash%20certificate%20data%2C%20which%20reaches%20wc_ShaUpdate.%20With%20a%20crafted%20short%20input%2C%20wc_ShaUpdate%20performs%20a%2064-byte%20memcpy%20that%20reads%20past%20the%20end%20of%20the%208-byte%20input%20allocation.%20The%20attacker%20controls%20the%20certificate%20bytes%20and%20length%20supplied%20to%20the%20PKCS%237%20API.%20The%20result%20is%20an%20out-of-bounds%20heap%20read%20that%20could%20disclose%20adjacent%20heap%20memory%20or%20crash%20the%20process.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3A%22sha.c%3A733%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22wolfssl%22%2C%22reproduction%22%3A%5B%221.%20Craft%20a%20short/malformed%20DER%20certificate%20buffer%22%2C%222.%20Supply%20it%20to%20wc_PKCS7_InitWithCert%28%29%22%2C%223.%20ParseCertRelative%20%E2%86%92%20CalcHashId_ex%20%E2%86%92%20wc_ShaHash%20%E2%86%92%20wc_ShaUpdate%20memcpy%20reads%2064%20bytes%20past%20the%20buffer%20end%22%5D%2C%22technical_details%22%3A%22ASAN%3A%20%5C%22READ%20of%20size%2064%20at%200x704ffcee0058%20...%200%20bytes%20after%208-byte%20region%5C%22.%20During%20certificate%20parsing%2C%20CalcHashId_ex%20passes%20a%20buffer/length%20derived%20from%20the%20malformed%20DER%20to%20wc_ShaHash%20%E2%86%92%20wc_ShaUpdate%2C%20which%20copies%20a%20full%2064-byte%20SHA%20block%20without%20ensuring%20that%20many%20bytes%20remain%20in%20the%20source%20buffer%2C%20reading%20beyond%20the%20allocation.%22%2C%22title%22%3A%22Heap-buffer-overflow%20in%20sha.c%3A733%22%2C%22vendor_severity%22%3Anull%7D)

```
  "ant_id": "ANT-2026-87DJGDRB",
  "bug_class": "Heap-buffer-overflow",
  "created_at": "2026-03-24T18:46:56+00:00",
  "description": "When wc_PKCS7_InitWithCert is given an attacker-supplied certificate buffer, ParseCertRelative calls CalcHashId_ex to hash certificate data, which reaches wc_ShaUpdate. With a crafted short input, wc_ShaUpdate performs a 64-byte memcpy that reads past the end of the 8-byte input allocation. The attacker controls the certificate bytes and length supplied to the PKCS#7 API. The result is an out-of-bounds heap read that could disclose adjacent heap memory or crash the process.",
  "location": "sha.c:733",
  "project": "wolfssl",
    "1. Craft a short/malformed DER certificate buffer",
    "2. Supply it to wc_PKCS7_InitWithCert()",
    "3. ParseCertRelative → CalcHashId_ex → wc_ShaHash → wc_ShaUpdate memcpy reads 64 bytes past the buffer end"
  "technical_details": "ASAN: \"READ of size 64 at 0x704ffcee0058 ... 0 bytes after 8-byte region\". During certificate parsing, CalcHashId_ex passes a buffer/length derived from the malformed DER to wc_ShaHash → wc_ShaUpdate, which copies a full 64-byte SHA block without ensuring that many bytes remain in the source buffer, reading beyond the allocation.",
  "title": "Heap-buffer-overflow in sha.c:733",
  "vendor_severity": null
```
