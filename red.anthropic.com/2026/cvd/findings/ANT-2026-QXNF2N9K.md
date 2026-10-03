<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-QXNF2N9K -->

# ANT-2026-QXNF2N9K · rocketchat/rocket.chat

## auth-bypass high

[CVE-2026-48929](https://nvd.nist.gov/vuln/detail/CVE-2026-48929)

Maintainer high

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ophion Security.

# ANT-2026-QXNF2N9K: Unauthenticated Arbitrary File Deletion via `deleteFileMessage` Meteor Method

A completely unauthenticated attacker can permanently delete any file attachment uploaded to any Rocket.Chat room — including files in private channels, direct messages, and admin-only rooms — by invoking the `deleteFileMessage` Meteor method through the `/api/v1/method.callAnon/:method` REST endpoint.

The root cause is a broken authorization guard in `deleteFileMessage` that **only performs a permission check when a user ID is present**. When the method is invoked anonymously, `Meteor.userId()` returns `null`, the guarded branch is skipped, and execution falls through to an unprotected `FileUpload.deleteById()` call.

The irony: being **unauthenticated** grants *more* destructive power than being a logged-in low-privilege user.

**Project:** rocketchat/rocket.chat
**Commit:** `7b641d319bab2cd9`
**Location:** `apps/meteor/app/lib/server/functions/deleteMessage.ts:13`

Line 23's compound condition `if (msg && userId)` is a fail-open guard: when userId is null (anonymous invocation), the permission-validating branch is skipped and line 27 calls FileUpload.deleteById(fileID) directly, which performs no owner or room ACL check. The method.callAnon route (misc.ts:534-576) has authRequired: false and no method allowlist, so deleteFileMessage is reachable with zero credentials. Net effect: being unauthenticated grants more destructive power than being a logged-in low-privilege user.

This finding was identified by static analysis and has not yet been dynamically reproduced. The Technical Details section above describes the code path; a trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-QXNF2N9K.

---

**Reference:** ANT-2026-QXNF2N9K

Triage and disclosure were performed by Ophion Security.

1. 2026-03-30
2. 2026-04-25
3. 2026-05-09
4. 2026-06-11
5. 2026-08-17

7f41196694c65ea6357c1f9c2b8ccd820fe8ebe3738c83fcf418fafc8335eebe0059f820e31e58377599b8af68aa3097f53780f7714fe1a60401ad59fc28175b

Committed 2026-04-25 07:05 UTC

Revealed 2026-08-17 17:47 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-QXNF2N9K%22%2C%22bug_class%22%3A%22Authentication-bypass%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3A%227b641d319bab2cd9%22%2C%22created_at%22%3A%222026-03-30T23%3A20%3A41%2B00%3A00%22%2C%22description%22%3A%22A%20completely%20unauthenticated%20attacker%20can%20permanently%20delete%20any%20file%20attachment%20uploaded%20to%20any%20Rocket.Chat%20room%20%E2%80%94%20including%20files%20in%20private%20channels%2C%20direct%20messages%2C%20and%20admin-only%20rooms%20%E2%80%94%20by%20invoking%20the%20%60deleteFileMessage%60%20Meteor%20method%20through%20the%20%60/api/v1/method.callAnon/%3Amethod%60%20REST%20endpoint.%5Cn%5CnThe%20root%20cause%20is%20a%20broken%20authorization%20guard%20in%20%60deleteFileMessage%60%20that%20%2A%2Aonly%20performs%20a%20permission%20check%20when%20a%20user%20ID%20is%20present%2A%2A.%20When%20the%20method%20is%20invoked%20anonymously%2C%20%60Meteor.userId%28%29%60%20returns%20%60null%60%2C%20the%20guarded%20branch%20is%20skipped%2C%20and%20execution%20falls%20through%20to%20an%20unprotected%20%60FileUpload.deleteById%28%29%60%20call.%5Cn%5CnThe%20irony%3A%20being%20%2A%2Aunauthenticated%2A%2A%20grants%20%2Amore%2A%20destructive%20power%20than%20being%20a%20logged-in%20low-privilege%20user.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3A%22apps/meteor/app/lib/server/functions/deleteMessage.ts%3A13%22%2C%22poc_sha256%22%3A%229313af1c30072fba3ed504fea55c98d5484d97d9fe858d992c925bf42057f298%22%2C%22preimage_version%22%3A1%2C%22project%22%3A%22rocketchat%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3A%22Line%2023%27s%20compound%20condition%20%60if%20%28msg%20%26%26%20userId%29%60%20is%20a%20fail-open%20guard%3A%20when%20userId%20is%20null%20%28anonymous%20invocation%29%2C%20the%20permission-validating%20branch%20is%20skipped%20and%20line%2027%20calls%20FileUpload.deleteById%28fileID%29%20directly%2C%20which%20performs%20no%20owner%20or%20room%20ACL%20check.%20The%20method.callAnon%20route%20%28misc.ts%3A534-576%29%20has%20authRequired%3A%20false%20and%20no%20method%20allowlist%2C%20so%20deleteFileMessage%20is%20reachable%20with%20zero%20credentials.%20Net%20effect%3A%20being%20unauthenticated%20grants%20more%20destructive%20power%20than%20being%20a%20logged-in%20low-privilege%20user.%22%2C%22title%22%3A%22Unauthenticated%20Arbitrary%20File%20Deletion%20via%20%60deleteFileMessage%60%20Meteor%20Method%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-QXNF2N9K",
  "bug_class": "Authentication-bypass",
  "commit_sha": "7b641d319bab2cd9",
  "created_at": "2026-03-30T23:20:41+00:00",
  "description": "A completely unauthenticated attacker can permanently delete any file attachment uploaded to any Rocket.Chat room — including files in private channels, direct messages, and admin-only rooms — by invoking the `deleteFileMessage` Meteor method through the `/api/v1/method.callAnon/:method` REST endpoint.\n\nThe root cause is a broken authorization guard in `deleteFileMessage` that **only performs a permission check when a user ID is present**. When the method is invoked anonymously, `Meteor.userId()` returns `null`, the guarded branch is skipped, and execution falls through to an unprotected `FileUpload.deleteById()` call.\n\nThe irony: being **unauthenticated** grants *more* destructive power than being a logged-in low-privilege user.",
  "location": "apps/meteor/app/lib/server/functions/deleteMessage.ts:13",
  "poc_sha256": "9313af1c30072fba3ed504fea55c98d5484d97d9fe858d992c925bf42057f298",
  "project": "rocketchat",
  "technical_details": "Line 23's compound condition `if (msg && userId)` is a fail-open guard: when userId is null (anonymous invocation), the permission-validating branch is skipped and line 27 calls FileUpload.deleteById(fileID) directly, which performs no owner or room ACL check. The method.callAnon route (misc.ts:534-576) has authRequired: false and no method allowlist, so deleteFileMessage is reachable with zero credentials. Net effect: being unauthenticated grants more destructive power than being a logged-in low-privilege user.",
  "title": "Unauthenticated Arbitrary File Deletion via `deleteFileMessage` Meteor Method",
```
