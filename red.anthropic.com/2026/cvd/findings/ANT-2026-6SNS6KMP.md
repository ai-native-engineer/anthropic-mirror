<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-6SNS6KMP -->

# ANT-2026-6SNS6KMP · gitoxidelabs/gitoxide

## rce high

[GHSA-f26g-jm89-4g65](https://github.com/advisories/GHSA-f26g-jm89-4g65)

Security research firm -
Maintainer high

Anthropic's analysis of this finding, sealed at approval.

# ANT-2026-6SNS6KMP: RCE when updating a Git submodule of a malicious repository

Updating a Git submodule from a malicious repository leads to remote code execution.

**Project:** gitoxidelabs/gitoxide

Step [A] reads `submodule.<name>.update` newest-to-oldest across sections, so if the trusted override section has no `update` key the attacker's .gitmodules value is returned. Step [B] then disarms the guard because `.any(|s| s.header().subsection_name() == Some(name) && !std::ptr::eq(s.meta(), ours))` only checks that a foreign-metadata section exists for that name, not that it supplied the value read in [A]. The two checks ask different questions, and the mismatch lets a .gitmodules-sourced `!command` pass as trusted.

This finding was identified by static analysis and has not yet been dynamically reproduced. The Technical Details section above describes the code path; a trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-6SNS6KMP.

---

**Reference:** ANT-2026-6SNS6KMP

```
diff --git a/gix-submodule/src/access.rs b/gix-submodule/src/access.rs
index 0b2f5b21c2d..0ae7d654867 100644
--- a/gix-submodule/src/access.rs
+++ b/gix-submodule/src/access.rs
@@ -166,7 +166,12 @@ impl File {

     /// Retrieve the `update` field of the submodule named `name`, if present.
     pub fn update(&self, name: &BStr) -> Result<Option<Update>, config::update::Error> {
-        let value: Update = match self.config.string(&format!("submodule.{name}.update")) {
+        let mut value_is_from_modules_file = None;
+        let our_meta = self.config.meta();
+        let value: Update = match self.config.string_filter(&format!("submodule.{name}.update"), |meta| {
+            value_is_from_modules_file = Some(std::ptr::eq(meta, our_meta));
+            true
+        }) {
             Some(v) => v.as_ref().try_into().map_err(|()| config::update::Error::Invalid {
                 submodule: name.to_owned(),
                 actual: v.into_owned(),
@@ -175,14 +180,7 @@ impl File {
         };

         if let Update::Command(cmd) = &value {
-            let ours = self.config.meta();
-            let has_value_from_foreign_section = self
-                .config
-                .sections_by_name("submodule")
-                .into_iter()
-                .flatten()
-                .any(|s| s.header().subsection_name() == Some(name) && !std::ptr::eq(s.meta(), ours));
-            if !has_value_from_foreign_section {
+            if value_is_from_modules_file.unwrap_or_default() {
                 return Err(config::update::Error::CommandForbiddenInModulesConfiguration {
                     submodule: name.to_owned(),
                     actual: cmd.to_owned(),
```

<https://github.com/GitoxideLabs/gitoxide/commit/e3ca1e64b0bcd627c7c5d3620f891cc22d1d03c7>

ADVISORY

<https://github.com/GitoxideLabs/gitoxide/security/advisories/GHSA-f26g-jm89-4g65>

1. 2026-03-10
2. 2026-03-29
3. 2026-04-24
4. 2026-05-08
5. 2026-05-20

bc1d508742c8b9b677d57b6feae069ec5a97a697eba86a13021c648a8457d27998aac7f9245b25e244e4ae804163175bd310e4302c522abf267f76e64a845221

Committed 2026-05-08 16:37 UTC

Revealed 2026-05-20 07:40 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-6SNS6KMP%22%2C%22bug_class%22%3A%22Remote%20Code%20Execution%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A43%3A51%2B00%3A00%22%2C%22description%22%3A%22Updating%20a%20Git%20submodule%20from%20a%20malicious%20repository%20leads%20to%20remote%20code%20execution.%22%2C%22discovered_at%22%3A%222026-03-10T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22GitoxideLabs/gitoxide%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3A%22Step%20%5BA%5D%20reads%20%60submodule.%3Cname%3E.update%60%20newest-to-oldest%20across%20sections%2C%20so%20if%20the%20trusted%20override%20section%20has%20no%20%60update%60%20key%20the%20attacker%27s%20.gitmodules%20value%20is%20returned.%20Step%20%5BB%5D%20then%20disarms%20the%20guard%20because%20%60.any%28%7Cs%7C%20s.header%28%29.subsection_name%28%29%20%3D%3D%20Some%28name%29%20%26%26%20%21std%3A%3Aptr%3A%3Aeq%28s.meta%28%29%2C%20ours%29%29%60%20only%20checks%20that%20a%20foreign-metadata%20section%20exists%20for%20that%20name%2C%20not%20that%20it%20supplied%20the%20value%20read%20in%20%5BA%5D.%20The%20two%20checks%20ask%20different%20questions%2C%20and%20the%20mismatch%20lets%20a%20.gitmodules-sourced%20%60%21command%60%20pass%20as%20trusted.%22%2C%22title%22%3A%22RCE%20when%20updating%20a%20Git%20submodule%20of%20a%20malicious%20repository%22%2C%22vendor_severity%22%3Anull%7D)

```
  "ant_id": "ANT-2026-6SNS6KMP",
  "bug_class": "Remote Code Execution",
  "created_at": "2026-03-29T20:43:51+00:00",
  "description": "Updating a Git submodule from a malicious repository leads to remote code execution.",
  "discovered_at": "2026-03-10T00:00:00+00:00",
  "location": null,
  "project": "GitoxideLabs/gitoxide",
  "technical_details": "Step [A] reads `submodule.<name>.update` newest-to-oldest across sections, so if the trusted override section has no `update` key the attacker's .gitmodules value is returned. Step [B] then disarms the guard because `.any(|s| s.header().subsection_name() == Some(name) && !std::ptr::eq(s.meta(), ours))` only checks that a foreign-metadata section exists for that name, not that it supplied the value read in [A]. The two checks ask different questions, and the mismatch lets a .gitmodules-sourced `!command` pass as trusted.",
  "title": "RCE when updating a Git submodule of a malicious repository",
  "vendor_severity": null
```
