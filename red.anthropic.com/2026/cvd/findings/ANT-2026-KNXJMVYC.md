<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-KNXJMVYC -->

# ANT-2026-KNXJMVYC · wolfssl/wolfssl

## signature-bypass high

[CVE-2026-5466](https://nvd.nist.gov/vuln/detail/CVE-2026-5466)
[GHSA-47qf-hp3h-rwmm](https://github.com/advisories/GHSA-47qf-hp3h-rwmm)

Maintainer high

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Calif.

# ANT-2026-KNXJMVYC: Universal ECCSI signature forgery in wolfSSL wc\_VerifyEccsiHash via r = 0, s = 0

wolfSSL's ECCSI (RFC 6507) signature verifier, wc\_VerifyEccsiHash() in wolfcrypt/src/eccsi.c, decoded the signature components r and s from the signature buffer with mp\_read\_unsigned\_bin() and never checked that they lie in the range [1, q-1]. A signature carrying s = 0 makes the verification point J the point at infinity, whose x-coordinate is treated as 0, and with r = 0 the final comparison of J's x-coordinate against r succeeds, so the forged signature is accepted for any message and any signer identity using only publicly known constants. The issue is CVE-2026-5466 / GHSA-47qf-hp3h-rwmm, rated High, and is fixed in wolfSSL 5.9.1.

**Project:** wolfssl/wolfssl
**Location:** `wolfcrypt/src/eccsi.c:wc_VerifyEccsiHash (and eccsi_calc_j)`

ECCSI verification (RFC 6507, section 5.2.2) in wolfSSL decodes a signature of the form `r | s | PVT`, computes `HE = hash(HS | r | M)`, `Y = [HS]PVT + KPAK` and `J = [s]([HE]G + [r]Y)`, and accepts the signature when the x-coordinate of J compares equal to r. In `wolfcrypt/src/eccsi.c`, `eccsi_decode_sig_r_pvt()` and `eccsi_decode_sig_s()` read r and s with `mp_read_unsigned_bin()`; before the fix, the checks applied to the signature were its length and that PVT decodes to a point on the curve. Neither r nor s was validated against `[1, q-1]`.

With s = 0, the scalar multiplication in `eccsi_calc_j()` returns the point at infinity, so J's x-coordinate is 0. With r = 0, the final `mp_cmp(jx, r) == MP_EQ` test in `wc_VerifyEccsiHash()` then holds and `*verified` is set to 1. Because this outcome does not depend on the message or the signer identity, an attacker who supplies r = 0 and s = 0 together with a PVT that is a valid curve point obtains a signature that verifies against any message for any identity, using only publicly known constants. The code is reachable by any application that passes attacker-controlled signatures to `wc_VerifyEccsiHash()` in a build with ECCSI support (`WOLFCRYPT_HAVE_ECCSI`).

* Impact: universal signature forgery / improper verification of cryptographic signature (CWE-347). Severity High (CVSS v3.1 base score 8.1 as recorded in the GitHub Advisory Database).
* Identifiers: CVE-2026-5466, GHSA-47qf-hp3h-rwmm.
* Fix: commit `13a016367ff4b4d3cc4c9bc2bfdfe692a512dd81` ("eccsi: fix universal signature forgery via r=0/s=0"), merged via wolfSSL PR #10102 and released in wolfSSL 5.9.1. The patch adds `[1, q-1]` range checks for r (in `wc_VerifyEccsiHash()`, after the curve parameters are loaded) and for s (in `eccsi_calc_j()`, after `eccsi_decode_sig_s()`), returning `MP_ZERO_E` or `ECC_OUT_OF_RANGE_E` and mirroring the existing `wc_ecc_check_r_s_range()` checks, and adds a defense-in-depth rejection of J = point at infinity (`ECC_INF_E`) before the final comparison.

```
/* added in wc_VerifyEccsiHash(); an equivalent check on s is added in eccsi_calc_j() */
if (err == 0) {
    if (mp_iszero(r)) {
        err = MP_ZERO_E;
    else if (mp_cmp(r, ¶ms->order) != MP_LT) {
        err = ECC_OUT_OF_RANGE_E;
```

This finding was identified by static analysis and has not yet been dynamically reproduced. The Technical Details section above describes the code path; a trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-KNXJMVYC.

---

**Reference:** ANT-2026-KNXJMVYC

Triage and disclosure were performed by Calif.

```
diff --git a/wolfcrypt/src/eccsi.c b/wolfcrypt/src/eccsi.c
index b4cf859e500..d919dd8a341 100644
--- a/wolfcrypt/src/eccsi.c
+++ b/wolfcrypt/src/eccsi.c
@@ -2159,6 +2159,18 @@ static int eccsi_calc_j(EccsiKey* key, const mp_int* hem, const byte* sig,
     if (err == 0) {
         err = eccsi_decode_sig_s(key, sig, sigSz, s);
+    /* Validate s is in [1, q-1]: reject zero or out-of-range second signature
+     * component.  With s=0, [s](...) yields the point at infinity whose
+     * affine x-coordinate is 0, making the final mp_cmp(0,0) accept any
+     * forged signature. */
+    if (err == 0) {
+        if (mp_iszero(s)) {
+            err = MP_ZERO_E;
+        }
+        else if (mp_cmp(s, &key->params.order) != MP_LT) {
+            err = ECC_OUT_OF_RANGE_E;
+        }
+    }
     /* [s]( [HE]G + [r]Y ) */
     if (err == 0) {
         err = eccsi_mulmod_point(key, s, j, j, 1);
@@ -2238,6 +2250,19 @@ int wc_VerifyEccsiHash(EccsiKey* key, enum wc_HashType hashType,
         err = mp_montgomery_setup(&params->prime, &mp);

+    /* Validate r is in [1, q-1]: reject zero or out-of-range first signature
+     * component before any scalar multiplication takes place.
+     * Without this check, r=0 causes J_x=0 and the final mp_cmp(0,0)==MP_EQ
+     * comparison accepts the forged signature unconditionally. */
+    if (err == 0) {
+        if (mp_iszero(r)) {
+            err = MP_ZERO_E;
+        }
+        else if (mp_cmp(r, &params->order) != MP_LT) {
+            err = ECC_OUT_OF_RANGE_E;
+        }
+    }
+
     /* Step 1: Validate PVT is on curve */
     if (err == 0) {
         err = wc_ecc_is_point(pvt, &params->a, &params->b, &params->prime);
@@ -2273,6 +2298,16 @@ int wc_VerifyEccsiHash(EccsiKey* key, enum wc_HashType hashType,
         key->params.haveBase = 0;

+    /* Defense-in-depth: reject J = point at infinity before the final
+     * comparison. Catches any future path that might reach this point
+     * with a neutral-element result (e.g. s = 0 mod q for a non-zero
+     * encoded s). */
+    if (err == 0) {
+        if (wc_ecc_point_is_at_infinity(j)) {
+            err = ECC_INF_E;
+        }
+    }
+
     /* Step 6: Jx fitting, compare with r */
     if (err == 0) {
         jx = &key->tmp;
```

<https://github.com/wolfSSL/wolfssl/commit/13a016367>

1. 2026-03-29
2. 2026-04-05
3. 2026-05-07
4. 2026-05-07
5. 2026-05-20

e4b9aa3b2e76b2e8e469e6d0bcadd5f14c9a876e667184ecf444b15e78488876b22e9c62781469f71687db5744334620cfa82068c52c47642611ed20394f2bcd

Committed 2026-04-05 23:37 UTC

Revealed 2026-05-20 07:40 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-KNXJMVYC%22%2C%22bug_class%22%3A%22signature-bypass%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A42%3A34%2B00%3A00%22%2C%22description%22%3Anull%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22wolfSSL%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3Anull%2C%22title%22%3A%22eccsi%20universal%20signature%20forgery%20via%20r%200%20s%200%20missing%20s%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-KNXJMVYC",
  "bug_class": "signature-bypass",
  "created_at": "2026-03-29T20:42:34+00:00",
  "description": null,
  "location": null,
  "project": "wolfSSL",
  "technical_details": null,
  "title": "eccsi universal signature forgery via r 0 s 0 missing s",
```
