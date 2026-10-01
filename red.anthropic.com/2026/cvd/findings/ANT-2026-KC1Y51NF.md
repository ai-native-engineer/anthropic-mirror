<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-KC1Y51NF -->

# ANT-2026-KC1Y51NF · openmeterio/openmeter

## sql-injection medium

[GHSA-wc3v-3457-c8cm](https://github.com/advisories/GHSA-wc3v-3457-c8cm)

Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Anvil Security.

# ANT-2026-KC1Y51NF: SQL injection in ClickHouse JSONPath validation

The meter create/update HTTP handlers validate user-supplied `valueProperty` and `groupBy` JSONPaths by building `SELECT JSON_VALUE('{}', '<path>')` with `fmt.Sprintf` and executing it against ClickHouse. The value is passed through `sqlbuilder.Escape`, which only doubles `$` and does not escape single quotes, so an attacker can break out of the string literal. This validation runs on the raw request body before Go-side input validation, and the OpenAPI schema imposes no pattern restriction on `valueProperty`. Because the query runs against the shared `om_events` table without tenant scoping, an authenticated tenant can inject arbitrary ClickHouse SQL and read every other tenant's usage events.

**Project:** openmeterio/openmeter
**Location:** `openmeter/streaming/clickhouse/utils_query.go:15`

`sqlbuilder.Escape` (huandu/go-sqlbuilder) only replaces `$` with `$$` for placeholder protection and performs no SQL string-literal escaping, so single quotes in the JSONPath terminate the literal and inject SQL. A correct escaper, `escapeJSONPathLiteral` (meter\_query.go:484-509), exists and is used everywhere else but was omitted at this call site.

1. Send POST /api/v1/meters with body {"slug":"m","aggregation":"SUM","eventType":"e","valueProperty":"$.a'), throwIf((SELECT count() FROM openmeter.om\_events WHERE namespace='victim-ns' AND subject='target')>0) --"}
2. Server builds SELECT JSON\_VALUE('{}', '$.a'), throwIf(...) --') and executes it via ClickHouse.Exec
3. Observe HTTP 200 vs 500 as a boolean oracle, or use sleep() for time-based blind extraction, or url() for out-of-band exfiltration

## Suggested Fix

Pass user-supplied JSONPath strings to ClickHouse as bound parameters, or escape them with a ClickHouse-aware string-literal escaper (e.g. the existing `escapeJSONPathLiteral`) before interpolation; never let them influence query structure.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-KC1Y51NF.

---

**Reference:** ANT-2026-KC1Y51NF

Triage and disclosure were performed by Anvil Security.

1. 2026-04-21
2. 2026-05-19
3. 2026-05-19
4. 2026-05-19

551ef9de796cb83e2d8a460f860441abb3fd6c1559e97ca04e279fbc62694ab4688a3dc7a995d86d6eebd4b93a1b94d22afac15a2d797c4094befcd2cd1c8f5b

Committed 2026-05-19 14:41 PT

Revealed 2026-08-17 10:47 PT

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-KC1Y51NF%22%2C%22bug_class%22%3A%22sql_injection%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-21T16%3A56%3A09%2B00%3A00%22%2C%22description%22%3A%22The%20meter%20create/update%20HTTP%20handlers%20validate%20user-supplied%20%60valueProperty%60%20and%20%60groupBy%60%20JSONPaths%20by%20building%20%60SELECT%20JSON_VALUE%28%27%7B%7D%27%2C%20%27%3Cpath%3E%27%29%60%20with%20%60fmt.Sprintf%60%20and%20executing%20it%20against%20ClickHouse.%20The%20value%20is%20passed%20through%20%60sqlbuilder.Escape%60%2C%20which%20only%20doubles%20%60%24%60%20and%20does%20not%20escape%20single%20quotes%2C%20so%20an%20attacker%20can%20break%20out%20of%20the%20string%20literal.%20This%20validation%20runs%20on%20the%20raw%20request%20body%20before%20Go-side%20input%20validation%2C%20and%20the%20OpenAPI%20schema%20imposes%20no%20pattern%20restriction%20on%20%60valueProperty%60.%20Because%20the%20query%20runs%20against%20the%20shared%20%60om_events%60%20table%20without%20tenant%20scoping%2C%20an%20authenticated%20tenant%20can%20inject%20arbitrary%20ClickHouse%20SQL%20and%20read%20every%20other%20tenant%27s%20usage%20events.%22%2C%22discovered_at%22%3A%222026-04-19T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22openmeter/streaming/clickhouse/utils_query.go%3A15%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22openmeterio/openmeter%22%2C%22reproduction%22%3A%5B%22Send%20POST%20/api/v1/meters%20with%20body%20%7B%5C%22slug%5C%22%3A%5C%22m%5C%22%2C%5C%22aggregation%5C%22%3A%5C%22SUM%5C%22%2C%5C%22eventType%5C%22%3A%5C%22e%5C%22%2C%5C%22valueProperty%5C%22%3A%5C%22%24.a%27%29%2C%20throwIf%28%28SELECT%20count%28%29%20FROM%20openmeter.om_events%20WHERE%20namespace%3D%27victim-ns%27%20AND%20subject%3D%27target%27%29%3E0%29%20--%5C%22%7D%22%2C%22Server%20builds%20SELECT%20JSON_VALUE%28%27%7B%7D%27%2C%20%27%24.a%27%29%2C%20throwIf%28...%29%20--%27%29%20and%20executes%20it%20via%20ClickHouse.Exec%22%2C%22Observe%20HTTP%20200%20vs%20500%20as%20a%20boolean%20oracle%2C%20or%20use%20sleep%28%29%20for%20time-based%20blind%20extraction%2C%20or%20url%28%29%20for%20out-of-band%20exfiltration%22%5D%2C%22technical_details%22%3A%22%60sqlbuilder.Escape%60%20%28huandu/go-sqlbuilder%29%20only%20replaces%20%60%24%60%20with%20%60%24%24%60%20for%20placeholder%20protection%20and%20performs%20no%20SQL%20string-literal%20escaping%2C%20so%20single%20quotes%20in%20the%20JSONPath%20terminate%20the%20literal%20and%20inject%20SQL.%20A%20correct%20escaper%2C%20%60escapeJSONPathLiteral%60%20%28meter_query.go%3A484-509%29%2C%20exists%20and%20is%20used%20everywhere%20else%20but%20was%20omitted%20at%20this%20call%20site.%22%2C%22title%22%3A%22SQL%20injection%20in%20ClickHouse%20JSONPath%20validation%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-KC1Y51NF",
  "bug_class": "sql_injection",
  "created_at": "2026-04-21T16:56:09+00:00",
  "description": "The meter create/update HTTP handlers validate user-supplied `valueProperty` and `groupBy` JSONPaths by building `SELECT JSON_VALUE('{}', '<path>')` with `fmt.Sprintf` and executing it against ClickHouse. The value is passed through `sqlbuilder.Escape`, which only doubles `$` and does not escape single quotes, so an attacker can break out of the string literal. This validation runs on the raw request body before Go-side input validation, and the OpenAPI schema imposes no pattern restriction on `valueProperty`. Because the query runs against the shared `om_events` table without tenant scoping, an authenticated tenant can inject arbitrary ClickHouse SQL and read every other tenant's usage events.",
  "discovered_at": "2026-04-19T00:00:00+00:00",
  "location": "openmeter/streaming/clickhouse/utils_query.go:15",
  "project": "openmeterio/openmeter",
    "Send POST /api/v1/meters with body {\"slug\":\"m\",\"aggregation\":\"SUM\",\"eventType\":\"e\",\"valueProperty\":\"$.a'), throwIf((SELECT count() FROM openmeter.om_events WHERE namespace='victim-ns' AND subject='target')>0) --\"}",
    "Server builds SELECT JSON_VALUE('{}', '$.a'), throwIf(...) --') and executes it via ClickHouse.Exec",
    "Observe HTTP 200 vs 500 as a boolean oracle, or use sleep() for time-based blind extraction, or url() for out-of-band exfiltration"
  "technical_details": "`sqlbuilder.Escape` (huandu/go-sqlbuilder) only replaces `$` with `$$` for placeholder protection and performs no SQL string-literal escaping, so single quotes in the JSONPath terminate the literal and inject SQL. A correct escaper, `escapeJSONPathLiteral` (meter_query.go:484-509), exists and is used everywhere else but was omitted at this call site.",
  "title": "SQL injection in ClickHouse JSONPath validation",
```
