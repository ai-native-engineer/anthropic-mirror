<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-HFGGE6HR -->

# ANT-2026-HFGGE6HR · asterisk/asterisk

## stack-buffer-overflow critical

[GHSA-589g-qgf8-m6mx](https://github.com/advisories/GHSA-589g-qgf8-m6mx)

Claude critical
Security research firm critical (revised; sealed as high)
Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Trail of Bits.

# ANT-2026-HFGGE6HR: Stack buffer overflow in parse\_simple\_message\_summary via unbounded sscanf %s (SIP MWI NOTIFY)

In res\_pjsip\_pubsub.c at line 3889, parse\_simple\_message\_summary() uses sscanf with an unbounded %s conversion to read a field from the body of an incoming SIP NOTIFY (Event: message-summary) into a fixed-size stack buffer. The parser is reached from the network via pubsub\_on\_rx\_notify\_request → pubsub\_on\_rx\_mwi\_notify\_request → parse\_simple\_message\_summary. An attacker who can deliver a single UDP NOTIFY with an oversized body field writes fully attacker-controlled bytes past the end of the stack local (a 901-byte out-of-bounds WRITE was observed). This yields stack memory corruption and potential control-flow hijack.

**Project:** asterisk/asterisk
**Location:** `res/res_pjsip_pubsub.c:3889`

res\_pjsip\_pubsub.c:3889 parse\_simple\_message\_summary() calls sscanf with an unbounded %s into a fixed stack buffer while parsing the body of an incoming SIP NOTIFY (Event: message-summary). A single UDP NOTIFY whose body field exceeds the buffer length writes attacker-controlled bytes (observed 901-byte WRITE) past the stack local. Reached via pubsub\_on\_rx\_notify\_request → pubsub\_on\_rx\_mwi\_notify\_request → parse\_simple\_message\_summary.

1. Craft a SIP NOTIFY request with Event: message-summary and a body field longer than the fixed stack buffer.
2. Send the NOTIFY over UDP to the target's SIP endpoint.
3. pubsub\_on\_rx\_notify\_request dispatches to pubsub\_on\_rx\_mwi\_notify\_request, which calls parse\_simple\_message\_summary().
4. sscanf with unbounded %s copies the oversized field into the stack buffer, writing attacker-controlled bytes past its end.

## Suggested Fix

Replace the unbounded %s in sscanf at res\_pjsip\_pubsub.c:3889 with a width-limited specifier (e.g., %255s) sized to the destination buffer, or rewrite using ast\_strsep/ast\_copy\_string.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-HFGGE6HR.

---

**Reference:** ANT-2026-HFGGE6HR

Triage and disclosure were performed by Trail of Bits. The severity shown is the firm's current assessment; the report was sealed with the firm's earlier assessment of high.

:   critical (revised; sealed as high)

ADVISORY

<https://github.com/asterisk/asterisk/commit/7a1ffcdf38cc76d1c4eae51651667f3fd4548ab0>

1. 2026-04-10
2. 2026-05-07
3. 2026-05-09
4. 2026-05-29
5. 2026-07-20

4af0e700ec9c669355834e3145eef3b8a700d116006ebbf92fbb1219711ed32b6b53e7c3625b7c28fe84fb31aa2e9c5adcfae86b6091f267dcff34fe0dee0386

Committed 2026-05-07 00:03 PT

Revealed 2026-07-20 22:23 PT

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-HFGGE6HR%22%2C%22bug_class%22%3A%22stack_buffer_overflow%22%2C%22claude_severity%22%3A%22critical%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-10T23%3A56%3A30%2B00%3A00%22%2C%22description%22%3A%22In%20res_pjsip_pubsub.c%20at%20line%203889%2C%20parse_simple_message_summary%28%29%20uses%20sscanf%20with%20an%20unbounded%20%25s%20conversion%20to%20read%20a%20field%20from%20the%20body%20of%20an%20incoming%20SIP%20NOTIFY%20%28Event%3A%20message-summary%29%20into%20a%20fixed-size%20stack%20buffer.%20The%20parser%20is%20reached%20from%20the%20network%20via%20pubsub_on_rx_notify_request%20%E2%86%92%20pubsub_on_rx_mwi_notify_request%20%E2%86%92%20parse_simple_message_summary.%20An%20attacker%20who%20can%20deliver%20a%20single%20UDP%20NOTIFY%20with%20an%20oversized%20body%20field%20writes%20fully%20attacker-controlled%20bytes%20past%20the%20end%20of%20the%20stack%20local%20%28a%20901-byte%20out-of-bounds%20WRITE%20was%20observed%29.%20This%20yields%20stack%20memory%20corruption%20and%20potential%20control-flow%20hijack.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3A%22res/res_pjsip_pubsub.c%3A3889%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22asterisk/asterisk%22%2C%22reproduction%22%3A%5B%221.%20Craft%20a%20SIP%20NOTIFY%20request%20with%20Event%3A%20message-summary%20and%20a%20body%20field%20longer%20than%20the%20fixed%20stack%20buffer.%22%2C%222.%20Send%20the%20NOTIFY%20over%20UDP%20to%20the%20target%27s%20SIP%20endpoint.%22%2C%223.%20pubsub_on_rx_notify_request%20dispatches%20to%20pubsub_on_rx_mwi_notify_request%2C%20which%20calls%20parse_simple_message_summary%28%29.%22%2C%224.%20sscanf%20with%20unbounded%20%25s%20copies%20the%20oversized%20field%20into%20the%20stack%20buffer%2C%20writing%20attacker-controlled%20bytes%20past%20its%20end.%22%5D%2C%22technical_details%22%3A%22res_pjsip_pubsub.c%3A3889%20parse_simple_message_summary%28%29%20calls%20sscanf%20with%20an%20unbounded%20%25s%20into%20a%20fixed%20stack%20buffer%20while%20parsing%20the%20body%20of%20an%20incoming%20SIP%20NOTIFY%20%28Event%3A%20message-summary%29.%20A%20single%20UDP%20NOTIFY%20whose%20body%20field%20exceeds%20the%20buffer%20length%20writes%20attacker-controlled%20bytes%20%28observed%20901-byte%20WRITE%29%20past%20the%20stack%20local.%20Reached%20via%20pubsub_on_rx_notify_request%20%E2%86%92%20pubsub_on_rx_mwi_notify_request%20%E2%86%92%20parse_simple_message_summary.%22%2C%22title%22%3A%22Stack%20buffer%20overflow%20in%20parse_simple_message_summary%20via%20unbounded%20sscanf%20%25s%20%28SIP%20MWI%20NOTIFY%29%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-HFGGE6HR",
  "bug_class": "stack_buffer_overflow",
  "claude_severity": "critical",
  "created_at": "2026-04-10T23:56:30+00:00",
  "description": "In res_pjsip_pubsub.c at line 3889, parse_simple_message_summary() uses sscanf with an unbounded %s conversion to read a field from the body of an incoming SIP NOTIFY (Event: message-summary) into a fixed-size stack buffer. The parser is reached from the network via pubsub_on_rx_notify_request → pubsub_on_rx_mwi_notify_request → parse_simple_message_summary. An attacker who can deliver a single UDP NOTIFY with an oversized body field writes fully attacker-controlled bytes past the end of the stack local (a 901-byte out-of-bounds WRITE was observed). This yields stack memory corruption and potential control-flow hijack.",
  "location": "res/res_pjsip_pubsub.c:3889",
  "project": "asterisk/asterisk",
    "1. Craft a SIP NOTIFY request with Event: message-summary and a body field longer than the fixed stack buffer.",
    "2. Send the NOTIFY over UDP to the target's SIP endpoint.",
    "3. pubsub_on_rx_notify_request dispatches to pubsub_on_rx_mwi_notify_request, which calls parse_simple_message_summary().",
    "4. sscanf with unbounded %s copies the oversized field into the stack buffer, writing attacker-controlled bytes past its end."
  "technical_details": "res_pjsip_pubsub.c:3889 parse_simple_message_summary() calls sscanf with an unbounded %s into a fixed stack buffer while parsing the body of an incoming SIP NOTIFY (Event: message-summary). A single UDP NOTIFY whose body field exceeds the buffer length writes attacker-controlled bytes (observed 901-byte WRITE) past the stack local. Reached via pubsub_on_rx_notify_request → pubsub_on_rx_mwi_notify_request → parse_simple_message_summary.",
  "title": "Stack buffer overflow in parse_simple_message_summary via unbounded sscanf %s (SIP MWI NOTIFY)",
```
