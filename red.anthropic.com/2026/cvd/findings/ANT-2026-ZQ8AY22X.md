<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-ZQ8AY22X -->

# ANT-2026-ZQ8AY22X · craftcms/cms

## privilege-escalation high

[GHSA-cc7p-2j3x-x7xf](https://github.com/advisories/GHSA-cc7p-2j3x-x7xf)

Security research firm -
Maintainer high

Anthropic's analysis of this finding, sealed at approval.

# ANT-2026-ZQ8AY22X: Privilege Escalation/Bypass through UsersController->actionImpersonateWithToken()

Craft CMS's actionPreview() re-dispatches requests with $skipSpecialHandling=true and $checkToken=false, allowing an attacker-supplied action query parameter to redirect execution to UsersController::actionImpersonateWithToken(). That endpoint's only guard, requireToken(), merely checks the boolean \_hadToken set when the preview token was resolved, without verifying the token was minted for impersonation. Because the action is also listed in $allowAnonymous, no prior authentication is enforced. An editor (or anyone holding a shared preview URL) can therefore append &action=users/impersonate-with-token&userId=1&prevUserId=1 to a preview URL and be logged in as user 1 (admin).

**Project:** CraftCMS

Root cause is a confused-deputy between the preview dispatcher and the impersonation endpoint: actionPreview() passes $skipSpecialHandling=true to handleRequest() and $checkToken=false to checkIfActionRequest(), so security guards are skipped and the action parameter is attacker-controlled. requireToken() on actionImpersonateWithToken() only inspects \_hadToken (set for any valid token) rather than validating that the token was issued for this route, and the action is in $allowAnonymous, so no further authorization occurs.

This finding was identified by static analysis and has not yet been dynamically reproduced. The Technical Details section above describes the code path; a trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-ZQ8AY22X.

---

**Reference:** ANT-2026-ZQ8AY22X

ADVISORY

<https://github.com/craftcms/cms/security/advisories/GHSA-cc7p-2j3x-x7xf>

1. 2026-02-18
2. 2026-02-18
3. 2026-03-29
4. 2026-05-08
5. 2026-05-20

dc75439eef02f2f72ba1440db7ca5fbae9599c252caba20b38f6b5c634fae74db645c91470b08c00012cc38b7353a9a7f79f52cf703bb1a668c6df7682c8907f

Committed 2026-05-08 09:37 PT

Revealed 2026-05-20 00:40 PT

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-ZQ8AY22X%22%2C%22bug_class%22%3A%22privilege-escalation%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A43%3A35%2B00%3A00%22%2C%22description%22%3A%22Craft%20CMS%27s%20actionPreview%28%29%20re-dispatches%20requests%20with%20%24skipSpecialHandling%3Dtrue%20and%20%24checkToken%3Dfalse%2C%20allowing%20an%20attacker-supplied%20action%20query%20parameter%20to%20redirect%20execution%20to%20UsersController%3A%3AactionImpersonateWithToken%28%29.%20That%20endpoint%27s%20only%20guard%2C%20requireToken%28%29%2C%20merely%20checks%20the%20boolean%20_hadToken%20set%20when%20the%20preview%20token%20was%20resolved%2C%20without%20verifying%20the%20token%20was%20minted%20for%20impersonation.%20Because%20the%20action%20is%20also%20listed%20in%20%24allowAnonymous%2C%20no%20prior%20authentication%20is%20enforced.%20An%20editor%20%28or%20anyone%20holding%20a%20shared%20preview%20URL%29%20can%20therefore%20append%20%26action%3Dusers/impersonate-with-token%26userId%3D1%26prevUserId%3D1%20to%20a%20preview%20URL%20and%20be%20logged%20in%20as%20user%201%20%28admin%29.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22CraftCMS%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3A%22Root%20cause%20is%20a%20confused-deputy%20between%20the%20preview%20dispatcher%20and%20the%20impersonation%20endpoint%3A%20actionPreview%28%29%20passes%20%24skipSpecialHandling%3Dtrue%20to%20handleRequest%28%29%20and%20%24checkToken%3Dfalse%20to%20checkIfActionRequest%28%29%2C%20so%20security%20guards%20are%20skipped%20and%20the%20action%20parameter%20is%20attacker-controlled.%20requireToken%28%29%20on%20actionImpersonateWithToken%28%29%20only%20inspects%20_hadToken%20%28set%20for%20any%20valid%20token%29%20rather%20than%20validating%20that%20the%20token%20was%20issued%20for%20this%20route%2C%20and%20the%20action%20is%20in%20%24allowAnonymous%2C%20so%20no%20further%20authorization%20occurs.%22%2C%22title%22%3A%22Privilege%20Escalation/Bypass%20through%20UsersController-%3EactionImpersonateWithToken%28%29%22%2C%22vendor_severity%22%3Anull%7D)

```
  "ant_id": "ANT-2026-ZQ8AY22X",
  "bug_class": "privilege-escalation",
  "created_at": "2026-03-29T20:43:35+00:00",
  "description": "Craft CMS's actionPreview() re-dispatches requests with $skipSpecialHandling=true and $checkToken=false, allowing an attacker-supplied action query parameter to redirect execution to UsersController::actionImpersonateWithToken(). That endpoint's only guard, requireToken(), merely checks the boolean _hadToken set when the preview token was resolved, without verifying the token was minted for impersonation. Because the action is also listed in $allowAnonymous, no prior authentication is enforced. An editor (or anyone holding a shared preview URL) can therefore append &action=users/impersonate-with-token&userId=1&prevUserId=1 to a preview URL and be logged in as user 1 (admin).",
  "project": "CraftCMS",
  "technical_details": "Root cause is a confused-deputy between the preview dispatcher and the impersonation endpoint: actionPreview() passes $skipSpecialHandling=true to handleRequest() and $checkToken=false to checkIfActionRequest(), so security guards are skipped and the action parameter is attacker-controlled. requireToken() on actionImpersonateWithToken() only inspects _hadToken (set for any valid token) rather than validating that the token was issued for this route, and the action is in $allowAnonymous, so no further authorization occurs.",
  "title": "Privilege Escalation/Bypass through UsersController->actionImpersonateWithToken()",
  "vendor_severity": null
```
