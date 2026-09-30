<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-QRYCJNAP -->

# ANT-2026-QRYCJNAP · dnsmasq

## denial-of-service medium

[CVE-2026-13002](https://nvd.nist.gov/vuln/detail/CVE-2026-13002)
[CVE-2026-4890](https://nvd.nist.gov/vuln/detail/CVE-2026-4890)

Maintainer medium

an unreleased Anthropic model

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Trail of Bits.

# ANT-2026-QRYCJNAP: DNSSEC NSEC typemap infinite loop hangs daemon

In dnsmasq's DNSSEC validator, prove\_non\_existence\_nsec() (dnssec.c:1340-1356) and the matching NSEC3 loop (1507-1523) iterate NSEC type-bitmap windows but decrement rdlen and advance p by only p[1] (bitmap length) rather than p[1]+2 (header + bitmap). When an attacker supplies a two-byte window block [window#][0x00] with window# != (qtype>>8), the bounds check passes and the loop state never changes, yielding an infinite loop. The attacker controls the NSEC RDATA bytes; a valid RRSIG over malformed bytes is accepted (line 2313 path), and the wildcard path at line 2275 reaches the loop before NSEC signatures are even verified. Because dnsmasq is single-threaded with no per-handler timeout, one hostile reply permanently hangs DNS, DHCP, TFTP, and RA services until the process is killed.

**Project:** dnsmasq
**Version:** commit b95d5a25777cc8910d2c2a921c68c778a3b30498 (still present at HEAD)
**Location:** `src/dnssec.c:1354`

Built a unit harness that #includes dnssec.c and calls the static prove\_non\_existence\_nsec() with a crafted NSEC RR whose type-bitmap window has window#=1 and bitmap-length=0 (p[1]==0), with the NSEC owner name equal to the queried name so the rc==0 branch is taken. The function never returned; a 3-second SIGALRM watchdog fired, proving the infinite loop. Root cause confirmed at src/dnssec.c:1354-1355: the loop advances by p[1] bytes instead of p[1]+2, so a zero-length bitmap leaves rdlen and p unchanged forever. Identical pattern present in the NSEC3 path. Reaching this in production requires an attacker who controls a DNSSEC-signed zone (or can forge a validly-signed NSEC), which is plausible for any domain owner — a single hostile signed reply hangs the daemon's single-threaded resolver loop.

**Crash signature:** `Hang / 100% CPU in prove_non_existence_nsec typemap loop; 3s SIGALRM watchdog fired (no return)`

1. Register a domain and provision a valid DNSSEC chain (DS in parent, signed DNSKEY).
2. Configure the authoritative server to answer `nx.evil.example AAAA` with a NODATA response whose authority section contains an NSEC record owner==qname and type-bitmap RDATA `0xFF 0x00`, plus a valid RRSIG over it.
3. Induce any client behind the target dnsmasq to resolve `nx.evil.example` (e.g., a webpage embedding the hostname).
4. dnsmasq forwards, receives the reply, validates the RRSIG, and calls prove\_non\_existence() at dnssec.c:2313 for the unanswered question.
5. prove\_non\_existence\_nsec() matches owner==qname (rc==0 at line 1312) and enters the typemap loop with p[0]=0xFF, p[1]=0x00, rdlen=2; the loop never advances.
6. The single-threaded event loop is blocked; the process spins at 100% CPU until killed.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-QRYCJNAP.

---

**Reference:** ANT-2026-QRYCJNAP

Triage and disclosure were performed by Trail of Bits.

1. 2026-04-08
2. 2026-04-21
3. 2026-05-07
4. 2026-05-09

aa75ba64f155bef4fe2bf47909666cea6dbecd39cfa0804362552cd6bb47eab70613db0438ce271d146d51e68e26b89bfb8ec8c1c8caf89093405a2f5e6f8585

Committed 2026-05-07 00:02 PT

Revealed 2026-08-17 10:47 PT

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-QRYCJNAP%22%2C%22bug_class%22%3A%22Denial-of-service%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-09T05%3A32%3A53%2B00%3A00%22%2C%22description%22%3A%22In%20dnsmasq%27s%20DNSSEC%20validator%2C%20prove_non_existence_nsec%28%29%20%28dnssec.c%3A1340-1356%29%20and%20the%20matching%20NSEC3%20loop%20%281507-1523%29%20iterate%20NSEC%20type-bitmap%20windows%20but%20decrement%20rdlen%20and%20advance%20p%20by%20only%20p%5B1%5D%20%28bitmap%20length%29%20rather%20than%20p%5B1%5D%2B2%20%28header%20%2B%20bitmap%29.%20When%20an%20attacker%20supplies%20a%20two-byte%20window%20block%20%5Bwindow%23%5D%5B0x00%5D%20with%20window%23%20%21%3D%20%28qtype%3E%3E8%29%2C%20the%20bounds%20check%20passes%20and%20the%20loop%20state%20never%20changes%2C%20yielding%20an%20infinite%20loop.%20The%20attacker%20controls%20the%20NSEC%20RDATA%20bytes%3B%20a%20valid%20RRSIG%20over%20malformed%20bytes%20is%20accepted%20%28line%202313%20path%29%2C%20and%20the%20wildcard%20path%20at%20line%202275%20reaches%20the%20loop%20before%20NSEC%20signatures%20are%20even%20verified.%20Because%20dnsmasq%20is%20single-threaded%20with%20no%20per-handler%20timeout%2C%20one%20hostile%20reply%20permanently%20hangs%20DNS%2C%20DHCP%2C%20TFTP%2C%20and%20RA%20services%20until%20the%20process%20is%20killed.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3A%22src/dnssec.c%3A1354%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22dnsmasq%22%2C%22reproduction%22%3A%5B%221.%20Register%20a%20domain%20and%20provision%20a%20valid%20DNSSEC%20chain%20%28DS%20in%20parent%2C%20signed%20DNSKEY%29.%22%2C%222.%20Configure%20the%20authoritative%20server%20to%20answer%20%60nx.evil.example%20AAAA%60%20with%20a%20NODATA%20response%20whose%20authority%20section%20contains%20an%20NSEC%20record%20owner%3D%3Dqname%20and%20type-bitmap%20RDATA%20%600xFF%200x00%60%2C%20plus%20a%20valid%20RRSIG%20over%20it.%22%2C%223.%20Induce%20any%20client%20behind%20the%20target%20dnsmasq%20to%20resolve%20%60nx.evil.example%60%20%28e.g.%2C%20a%20webpage%20embedding%20the%20hostname%29.%22%2C%224.%20dnsmasq%20forwards%2C%20receives%20the%20reply%2C%20validates%20the%20RRSIG%2C%20and%20calls%20prove_non_existence%28%29%20at%20dnssec.c%3A2313%20for%20the%20unanswered%20question.%22%2C%225.%20prove_non_existence_nsec%28%29%20matches%20owner%3D%3Dqname%20%28rc%3D%3D0%20at%20line%201312%29%20and%20enters%20the%20typemap%20loop%20with%20p%5B0%5D%3D0xFF%2C%20p%5B1%5D%3D0x00%2C%20rdlen%3D2%3B%20the%20loop%20never%20advances.%22%2C%226.%20The%20single-threaded%20event%20loop%20is%20blocked%3B%20the%20process%20spins%20at%20100%25%20CPU%20until%20killed.%22%5D%2C%22technical_details%22%3A%22Built%20a%20unit%20harness%20that%20%23includes%20dnssec.c%20and%20calls%20the%20static%20prove_non_existence_nsec%28%29%20with%20a%20crafted%20NSEC%20RR%20whose%20type-bitmap%20window%20has%20window%23%3D1%20and%20bitmap-length%3D0%20%28p%5B1%5D%3D%3D0%29%2C%20with%20the%20NSEC%20owner%20name%20equal%20to%20the%20queried%20name%20so%20the%20rc%3D%3D0%20branch%20is%20taken.%20The%20function%20never%20returned%3B%20a%203-second%20SIGALRM%20watchdog%20fired%2C%20proving%20the%20infinite%20loop.%20Root%20cause%20confirmed%20at%20src/dnssec.c%3A1354-1355%3A%20the%20loop%20advances%20by%20p%5B1%5D%20bytes%20instead%20of%20p%5B1%5D%2B2%2C%20so%20a%20zero-length%20bitmap%20leaves%20rdlen%20and%20p%20unchanged%20forever.%20Identical%20pattern%20present%20in%20the%20NSEC3%20path.%20Reaching%20this%20in%20production%20requires%20an%20attacker%20who%20controls%20a%20DNSSEC-signed%20zone%20%28or%20can%20forge%20a%20validly-signed%20NSEC%29%2C%20which%20is%20plausible%20for%20any%20domain%20owner%20%E2%80%94%20a%20single%20hostile%20signed%20reply%20hangs%20the%20daemon%27s%20single-threaded%20resolver%20loop.%22%2C%22title%22%3A%22DNSSEC%20NSEC%20typemap%20infinite%20loop%20hangs%20daemon%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-QRYCJNAP",
  "bug_class": "Denial-of-service",
  "created_at": "2026-04-09T05:32:53+00:00",
  "description": "In dnsmasq's DNSSEC validator, prove_non_existence_nsec() (dnssec.c:1340-1356) and the matching NSEC3 loop (1507-1523) iterate NSEC type-bitmap windows but decrement rdlen and advance p by only p[1] (bitmap length) rather than p[1]+2 (header + bitmap). When an attacker supplies a two-byte window block [window#][0x00] with window# != (qtype>>8), the bounds check passes and the loop state never changes, yielding an infinite loop. The attacker controls the NSEC RDATA bytes; a valid RRSIG over malformed bytes is accepted (line 2313 path), and the wildcard path at line 2275 reaches the loop before NSEC signatures are even verified. Because dnsmasq is single-threaded with no per-handler timeout, one hostile reply permanently hangs DNS, DHCP, TFTP, and RA services until the process is killed.",
  "location": "src/dnssec.c:1354",
  "project": "dnsmasq",
    "1. Register a domain and provision a valid DNSSEC chain (DS in parent, signed DNSKEY).",
    "2. Configure the authoritative server to answer `nx.evil.example AAAA` with a NODATA response whose authority section contains an NSEC record owner==qname and type-bitmap RDATA `0xFF 0x00`, plus a valid RRSIG over it.",
    "3. Induce any client behind the target dnsmasq to resolve `nx.evil.example` (e.g., a webpage embedding the hostname).",
    "4. dnsmasq forwards, receives the reply, validates the RRSIG, and calls prove_non_existence() at dnssec.c:2313 for the unanswered question.",
    "5. prove_non_existence_nsec() matches owner==qname (rc==0 at line 1312) and enters the typemap loop with p[0]=0xFF, p[1]=0x00, rdlen=2; the loop never advances.",
    "6. The single-threaded event loop is blocked; the process spins at 100% CPU until killed."
  "technical_details": "Built a unit harness that #includes dnssec.c and calls the static prove_non_existence_nsec() with a crafted NSEC RR whose type-bitmap window has window#=1 and bitmap-length=0 (p[1]==0), with the NSEC owner name equal to the queried name so the rc==0 branch is taken. The function never returned; a 3-second SIGALRM watchdog fired, proving the infinite loop. Root cause confirmed at src/dnssec.c:1354-1355: the loop advances by p[1] bytes instead of p[1]+2, so a zero-length bitmap leaves rdlen and p unchanged forever. Identical pattern present in the NSEC3 path. Reaching this in production requires an attacker who controls a DNSSEC-signed zone (or can forge a validly-signed NSEC), which is plausible for any domain owner — a single hostile signed reply hangs the daemon's single-threaded resolver loop.",
  "title": "DNSSEC NSEC typemap infinite loop hangs daemon",
```
