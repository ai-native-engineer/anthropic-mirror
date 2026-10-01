<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-PCBAKVPB -->

# ANT-2026-PCBAKVPB · dnsmasq

## heap-buffer-overflow high

[CVE-2026-4892](https://nvd.nist.gov/vuln/detail/CVE-2026-4892)
[GHSA-m62j-63mf-xr95](https://github.com/advisories/GHSA-m62j-63mf-xr95)

Maintainer high

an unreleased Anthropic model

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Trail of Bits.

# ANT-2026-PCBAKVPB: Heap overflow in privileged helper via oversized DHCPv6 client identifier

In dnsmasq's privileged script helper (helper.c:265-270), each byte of the DHCP client-ID is hex-encoded with sprintf into daemon->packet, a ~2267-byte buffer allocated at startup and inherited via fork(). DHCPv6 option lengths are 16-bit and state->clid\_len is taken from the wire at rfc3315.c:338 with no upper bound, then flows unchanged through lease\_set\_hwaddr() and queue\_script() to the helper. A local-network attacker sends a single DHCPv6 SOLICIT with RAPID\_COMMIT and a ~1200-byte OPTION6\_CLIENT\_ID (fits in one unfragmented IPv6 frame); when the lease script event fires, the helper writes ~3599 bytes into the 2267-byte buffer. The attacker controls the overflow length and the hex-digit content, corrupting the heap of a process that runs as root by default.

**Project:** dnsmasq
**Version:** commit b95d5a25777cc8910d2c2a921c68c778a3b30498 (still present at HEAD)
**Location:** `src/helper.c:265`

Sink confirmed via ASAN: a harness allocating daemon->packet exactly as dnsmasq.c:128-129 does (PACKETSZ+MAXDNAME+RRFIXEDSZ = 1547 bytes at default edns\_pktsz) and running the exact helper.c:265-270 hex-encode loop with clid\_len=800 produced 'AddressSanitizer: heap-buffer-overflow … WRITE of size 3 … 0 bytes after 1547-byte region allocated by safe\_malloc'. Source path verified statically: rfc3315.c:338 assigns state->clid\_len = opt6\_len(opt) with no upper bound; lease\_set\_hwaddr() (lease.c:992) stores it unchecked; queue\_script() (helper.c:794/809) forwards it to the helper pipe unchanged. The helper inherits daemon->packet via fork(). Overflow threshold is clid\_len ≥ ceil((bufsz+1)/3) ≈ 516 at defaults — well within the 16-bit DHCPv6 option length. Did not stand up a full DHCPv6 transaction in the time box, hence medium confidence on end-to-end reachability (requires --dhcp-script configured).

**Crash trace (truncated — full trace in attached crash.log):**

```
daemon->packet size = 1547 (PACKETSZ=512 MAXDNAME=1025 RRFIXEDSZ=10)
=================================================================
==17==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x51b000000d8b at pc 0xffff86e829d4 bp 0xffffc5315490 sp 0xffffc5315530
WRITE of size 3 at 0x51b000000d8b thread T0
    #0 0xffff86e829d0 in vsprintf ../../../../src/libsanitizer/sanitizer_common/sanitizer_common_interceptors.inc:1671
    #1 0xffff86e83cf0 in sprintf ../../../../src/libsanitizer/sanitizer_common/sanitizer_common_interceptors.inc:1714
    #2 0xaaaab6b5ca6c in main /build/harness_400509.c:35
    #3 0xffff863c2258  (/lib/aarch64-linux-gnu/libc.so.6+0x22258) (BuildId: 45918bc10b33fd96afc550c98de062dccdf44328)
    #4 0xffff863c2338 in __libc_start_main (/lib/aarch64-linux-gnu/libc.so.6+0x22338) (BuildId: 45918bc10b33fd96afc550c98de062dccdf44328)
    #5 0xaaaab6b5c5ec in _start (/build/h509+0x24c5ec) (BuildId: 59c1c64e9de91afd8fd09c5c0f7cb8edeff03a60)

allocated by thread T0 here:
    #0 0xffff86ea9e4c in calloc ../../../../src/libsanitizer/asan/asan_malloc_linux.cpp:77
    #1 0xaaaab6cbe2bc in safe_malloc /build/dnsmasq/src/util.c:321
    #2 0xaaaab6b5c7bc in main /build/harness_400509.c:21
    #3 0xffff863c2258  (/lib/aarch64-linux-gnu/libc.so.6+0x22258) (BuildId: 45918bc10b33fd96afc550c98de062dccdf44328)
    #4 0xffff863c2338 in __libc_start_main (/lib/aarch64-linux-gnu/libc.so.6+0x22338) (BuildId: 45918bc10b33fd96afc550c98de062dccdf44328)
    #5 0xaaaab6b5c5ec in _start (/build/h509+0x24c5ec) (BuildId: 59c1c64e9de91afd8fd09c5c0f7cb8edeff03a60)

SUMMARY: AddressSanitizer: heap-buffer-overflow ../../../../src/libsanitizer/sanitizer_common/sanitizer_common_interceptors.inc:1671 in vsprintf
```

1. Craft a DHCPv6 SOLICIT containing OPTION6\_RAPID\_COMMIT, a minimal IA\_TA (4-byte header + 4-byte IAID), and OPTION6\_CLIENT\_ID with a ≥756-byte (e.g. 1200-byte) payload
2. Send it to the dnsmasq DHCPv6 port; packet fits in a single 1280-byte-MTU IPv6 frame
3. RAPID\_COMMIT path (rfc3315.c:654-660) sets lease\_allocate=1; server allocates an address and stores clid/clid\_len verbatim in the lease
4. do\_script\_run() fires and queue\_script() pipes clid\_len to the helper child
5. Helper reads data.clid\_len and runs the sprintf hex-encode loop at helper.c:265-270, writing ~3×clid\_len bytes into the fixed daemon->packet buffer and overflowing it by ~1332 bytes

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-PCBAKVPB.

---

**Reference:** ANT-2026-PCBAKVPB

Triage and disclosure were performed by Trail of Bits.

1. 2026-04-08
2. 2026-05-07
3. 2026-05-09
4. 2026-05-09

11a65d2d8b73e1b60aecd4aa985a653c77e1870999845708ab73eb335b44073062498a75e0adff81fdda190aa5e9610c21c27d36961cc01f8493cf85f7e3fa81

Committed 2026-05-07 00:02 PT

Revealed 2026-08-17 10:47 PT

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-PCBAKVPB%22%2C%22bug_class%22%3A%22Heap-buffer-overflow%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-09T05%3A32%3A58%2B00%3A00%22%2C%22description%22%3A%22In%20dnsmasq%27s%20privileged%20script%20helper%20%28helper.c%3A265-270%29%2C%20each%20byte%20of%20the%20DHCP%20client-ID%20is%20hex-encoded%20with%20sprintf%20into%20daemon-%3Epacket%2C%20a%20~2267-byte%20buffer%20allocated%20at%20startup%20and%20inherited%20via%20fork%28%29.%20DHCPv6%20option%20lengths%20are%2016-bit%20and%20state-%3Eclid_len%20is%20taken%20from%20the%20wire%20at%20rfc3315.c%3A338%20with%20no%20upper%20bound%2C%20then%20flows%20unchanged%20through%20lease_set_hwaddr%28%29%20and%20queue_script%28%29%20to%20the%20helper.%20A%20local-network%20attacker%20sends%20a%20single%20DHCPv6%20SOLICIT%20with%20RAPID_COMMIT%20and%20a%20~1200-byte%20OPTION6_CLIENT_ID%20%28fits%20in%20one%20unfragmented%20IPv6%20frame%29%3B%20when%20the%20lease%20script%20event%20fires%2C%20the%20helper%20writes%20~3599%20bytes%20into%20the%202267-byte%20buffer.%20The%20attacker%20controls%20the%20overflow%20length%20and%20the%20hex-digit%20content%2C%20corrupting%20the%20heap%20of%20a%20process%20that%20runs%20as%20root%20by%20default.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3A%22src/helper.c%3A265%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22dnsmasq%22%2C%22reproduction%22%3A%5B%221.%20Craft%20a%20DHCPv6%20SOLICIT%20containing%20OPTION6_RAPID_COMMIT%2C%20a%20minimal%20IA_TA%20%284-byte%20header%20%2B%204-byte%20IAID%29%2C%20and%20OPTION6_CLIENT_ID%20with%20a%20%E2%89%A5756-byte%20%28e.g.%201200-byte%29%20payload%22%2C%222.%20Send%20it%20to%20the%20dnsmasq%20DHCPv6%20port%3B%20packet%20fits%20in%20a%20single%201280-byte-MTU%20IPv6%20frame%22%2C%223.%20RAPID_COMMIT%20path%20%28rfc3315.c%3A654-660%29%20sets%20lease_allocate%3D1%3B%20server%20allocates%20an%20address%20and%20stores%20clid/clid_len%20verbatim%20in%20the%20lease%22%2C%224.%20do_script_run%28%29%20fires%20and%20queue_script%28%29%20pipes%20clid_len%20to%20the%20helper%20child%22%2C%225.%20Helper%20reads%20data.clid_len%20and%20runs%20the%20sprintf%20hex-encode%20loop%20at%20helper.c%3A265-270%2C%20writing%20~3%C3%97clid_len%20bytes%20into%20the%20fixed%20daemon-%3Epacket%20buffer%20and%20overflowing%20it%20by%20~1332%20bytes%22%5D%2C%22technical_details%22%3A%22Sink%20confirmed%20via%20ASAN%3A%20a%20harness%20allocating%20daemon-%3Epacket%20exactly%20as%20dnsmasq.c%3A128-129%20does%20%28PACKETSZ%2BMAXDNAME%2BRRFIXEDSZ%20%3D%201547%20bytes%20at%20default%20edns_pktsz%29%20and%20running%20the%20exact%20helper.c%3A265-270%20hex-encode%20loop%20with%20clid_len%3D800%20produced%20%27AddressSanitizer%3A%20heap-buffer-overflow%20%E2%80%A6%20WRITE%20of%20size%203%20%E2%80%A6%200%20bytes%20after%201547-byte%20region%20allocated%20by%20safe_malloc%27.%20Source%20path%20verified%20statically%3A%20rfc3315.c%3A338%20assigns%20state-%3Eclid_len%20%3D%20opt6_len%28opt%29%20with%20no%20upper%20bound%3B%20lease_set_hwaddr%28%29%20%28lease.c%3A992%29%20stores%20it%20unchecked%3B%20queue_script%28%29%20%28helper.c%3A794/809%29%20forwards%20it%20to%20the%20helper%20pipe%20unchanged.%20The%20helper%20inherits%20daemon-%3Epacket%20via%20fork%28%29.%20Overflow%20threshold%20is%20clid_len%20%E2%89%A5%20ceil%28%28bufsz%2B1%29/3%29%20%E2%89%88%20516%20at%20defaults%20%E2%80%94%20well%20within%20the%2016-bit%20DHCPv6%20option%20length.%20Did%20not%20stand%20up%20a%20full%20DHCPv6%20transaction%20in%20the%20time%20box%2C%20hence%20medium%20confidence%20on%20end-to-end%20reachability%20%28requires%20--dhcp-script%20configured%29.%22%2C%22title%22%3A%22Heap%20overflow%20in%20privileged%20helper%20via%20oversized%20DHCPv6%20client%20identifier%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-PCBAKVPB",
  "bug_class": "Heap-buffer-overflow",
  "created_at": "2026-04-09T05:32:58+00:00",
  "description": "In dnsmasq's privileged script helper (helper.c:265-270), each byte of the DHCP client-ID is hex-encoded with sprintf into daemon->packet, a ~2267-byte buffer allocated at startup and inherited via fork(). DHCPv6 option lengths are 16-bit and state->clid_len is taken from the wire at rfc3315.c:338 with no upper bound, then flows unchanged through lease_set_hwaddr() and queue_script() to the helper. A local-network attacker sends a single DHCPv6 SOLICIT with RAPID_COMMIT and a ~1200-byte OPTION6_CLIENT_ID (fits in one unfragmented IPv6 frame); when the lease script event fires, the helper writes ~3599 bytes into the 2267-byte buffer. The attacker controls the overflow length and the hex-digit content, corrupting the heap of a process that runs as root by default.",
  "location": "src/helper.c:265",
  "project": "dnsmasq",
    "1. Craft a DHCPv6 SOLICIT containing OPTION6_RAPID_COMMIT, a minimal IA_TA (4-byte header + 4-byte IAID), and OPTION6_CLIENT_ID with a ≥756-byte (e.g. 1200-byte) payload",
    "2. Send it to the dnsmasq DHCPv6 port; packet fits in a single 1280-byte-MTU IPv6 frame",
    "3. RAPID_COMMIT path (rfc3315.c:654-660) sets lease_allocate=1; server allocates an address and stores clid/clid_len verbatim in the lease",
    "4. do_script_run() fires and queue_script() pipes clid_len to the helper child",
    "5. Helper reads data.clid_len and runs the sprintf hex-encode loop at helper.c:265-270, writing ~3×clid_len bytes into the fixed daemon->packet buffer and overflowing it by ~1332 bytes"
  "technical_details": "Sink confirmed via ASAN: a harness allocating daemon->packet exactly as dnsmasq.c:128-129 does (PACKETSZ+MAXDNAME+RRFIXEDSZ = 1547 bytes at default edns_pktsz) and running the exact helper.c:265-270 hex-encode loop with clid_len=800 produced 'AddressSanitizer: heap-buffer-overflow … WRITE of size 3 … 0 bytes after 1547-byte region allocated by safe_malloc'. Source path verified statically: rfc3315.c:338 assigns state->clid_len = opt6_len(opt) with no upper bound; lease_set_hwaddr() (lease.c:992) stores it unchecked; queue_script() (helper.c:794/809) forwards it to the helper pipe unchanged. The helper inherits daemon->packet via fork(). Overflow threshold is clid_len ≥ ceil((bufsz+1)/3) ≈ 516 at defaults — well within the 16-bit DHCPv6 option length. Did not stand up a full DHCPv6 transaction in the time box, hence medium confidence on end-to-end reachability (requires --dhcp-script configured).",
  "title": "Heap overflow in privileged helper via oversized DHCPv6 client identifier",
```
