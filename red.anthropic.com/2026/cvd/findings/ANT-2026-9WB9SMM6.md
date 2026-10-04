<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-9WB9SMM6 -->

# ANT-2026-9WB9SMM6 · libass/libass

## heap-buffer-overflow high

[GHSA-pjjp-65r7-ppgm](https://github.com/libass/libass/security/advisories/GHSA-pjjp-65r7-ppgm)

Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-9WB9SMM6: Heap-buffer-overflow in wrap\_lines\_measure at ass\_render.c:1902 via malformed ASS/SSA subtitle

OSS-Fuzz discovered a heap-buffer-overflow (ASAN READ) in libass, the ASS/SSA subtitle renderer embedded in mpv, VLC, and FFmpeg-based players. The bug is an out-of-bounds read on heap memory triggered when parsing malformed subtitle data. An attacker who delivers a crafted subtitle file alongside media content can cause a crash or potentially leak heap memory contents. The specific crashing function and root cause are not identified in this report — no stack trace or affected code location was provided.

**Project:** libass/libass
**Location:** `wrap_lines_measure() at libass/ass_render.c:1902`

ASAN reports a READ crash (heap-buffer-overflow) with no size or address details provided. The root cause is not pinpointed — the report lacks the crash trace and function name. It may be related to the CVE-2020-36430 decode\_chars() integer-subtraction bug (fixed in 0.15.1) or may be a distinct novel issue depending on the target version.

**Crash trace (truncated — full trace in attached crash.log):**

```
INFO: Running with entropic power schedule (0xFF, 100).
INFO: Seed: 4264302108
INFO: Loaded 1 modules   (55507 inline 8-bit counters): 55507 [0x5eeae80e8038, 0x5eeae80f590b),
INFO: Loaded 1 PC tables (55507 PCs): 55507 [0x5eeae80f5910,0x5eeae81ce640),
/out/libass_fuzzer: Running 1 inputs 1 time(s) each.
Running: /tmp/poc
EXIT_CODE:1

=== ASAN Report ===
=================================================================
==27==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x7486d9f71878 at pc 0x5eeae7ab4023 bp 0x7ffca0db89d0 sp 0x7ffca0db89c8
READ of size 4 at 0x7486d9f71878 thread T0
    #0 0x5eeae7ab4022 in wrap_lines_measure /src/libass/libass/ass_render.c:1902:50
    #1 0x5eeae7ab4022 in wrap_lines_smart /src/libass/libass/ass_render.c:1958:5
    #2 0x5eeae7ab4022 in ass_render_event /src/libass/libass/ass_render.c:2883:5
    #3 0x5eeae7aab505 in ass_render_frame /src/libass/libass/ass_render.c:3399:17
    #4 0x5eeae7a946d8 in consume_track /src/libass/fuzz/fuzz.c:163:23
    #5 0x5eeae7a946d8 in LLVMFuzzerTestOneInput /src/libass/fuzz/fuzz.c:425:9
    #6 0x5eeae7931b9d in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) /src/llvm-project/compiler-rt/lib/fuzzer/FuzzerLoop.cpp:619:13
    #7 0x5eeae791c912 in fuzzer::RunOneTest(fuzzer::Fuzzer*, char const*, unsigned long) /src/llvm-project/compiler-rt/lib/fuzzer/FuzzerDriver.cpp:329:6
    [... 16 more frames — full trace in crash.log]
```

1. Craft a malicious ASS/SSA subtitle file
2. Deliver it alongside or embedded within media content (e.g., MKV container)
3. Victim opens the media in a player using libass (mpv, VLC, etc.)
4. Heap-buffer-overflow triggers during subtitle parsing

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-9WB9SMM6.

---

**Reference:** ANT-2026-9WB9SMM6

Triage and disclosure were performed by Ada Logics.

```
diff --git a/libass/ass_render.c b/libass/ass_render.c
index b10d5e241..e7ea7314a 100644
--- a/libass/ass_render.c
+++ b/libass/ass_render.c
@@ -1886,13 +1886,21 @@ wrap_lines_measure(RenderContext *state, char *unibrks)

     while (i < text_info->length && text_info->glyphs[i].skip)
         ++i;
+
+    if (i == text_info->length) {
+        text_info->lines[0].len = 0;
+        text_info->lines[0].offset = 0;
+        return;
+    }
+
     double pen_shift_x = d6_to_double(-text_info->glyphs[i].pos.x);
     double pen_shift_y = 0.;

     for (i = 0; i < text_info->length; ++i) {
         GlyphInfo *cur = text_info->glyphs + i;
+
         if (cur->linebreak) {
-            while (i < text_info->length && cur->skip && !FORCEBREAK(cur->symbol, i))
+            while (i < text_info->length - 1 && cur->skip && !FORCEBREAK(cur->symbol, i))
                 cur = text_info->glyphs + ++i;
             double height =
                 text_info->lines[cur_line - 1].desc +
```

<https://github.com/libass/libass/commit/f2ef59755292bc4bb950ef22710e18a5487c399d>

1. 2026-03-20
2. 2026-05-13
3. 2026-05-13
4. 2026-06-24
5. 2026-08-17

b30eb2f05b830a169503a3765c0555ccd9d372c80abf92ee9ee6dbed3123cf115f25403726ac9bf34bc7449bf9c55d8e7d994e6a99a2b3d73d54e087c8850536

Committed 2026-05-13 17:55 UTC

Revealed 2026-08-17 17:47 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-9WB9SMM6%22%2C%22bug_class%22%3A%22heap-buffer-overflow%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-20T19%3A13%3A31%2B00%3A00%22%2C%22description%22%3A%22OSS-Fuzz%20discovered%20a%20heap-buffer-overflow%20%28ASAN%20READ%29%20in%20libass%2C%20the%20ASS/SSA%20subtitle%20renderer%20embedded%20in%20mpv%2C%20VLC%2C%20and%20FFmpeg-based%20players.%20The%20bug%20is%20an%20out-of-bounds%20read%20on%20heap%20memory%20triggered%20when%20parsing%20malformed%20subtitle%20data.%20An%20attacker%20who%20delivers%20a%20crafted%20subtitle%20file%20alongside%20media%20content%20can%20cause%20a%20crash%20or%20potentially%20leak%20heap%20memory%20contents.%20The%20specific%20crashing%20function%20and%20root%20cause%20are%20not%20identified%20in%20this%20report%20%E2%80%94%20no%20stack%20trace%20or%20affected%20code%20location%20was%20provided.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3A%22wrap_lines_measure%28%29%20at%20libass/ass_render.c%3A1902%22%2C%22poc_sha256%22%3A%22f2a97f5480f0f390f4e5df3100ffa01c057e55cdf514767c586dc4c265882e8b%22%2C%22preimage_version%22%3A1%2C%22project%22%3A%22libass%22%2C%22reproduction%22%3A%5B%22Craft%20a%20malicious%20ASS/SSA%20subtitle%20file%22%2C%22Deliver%20it%20alongside%20or%20embedded%20within%20media%20content%20%28e.g.%2C%20MKV%20container%29%22%2C%22Victim%20opens%20the%20media%20in%20a%20player%20using%20libass%20%28mpv%2C%20VLC%2C%20etc.%29%22%2C%22Heap-buffer-overflow%20triggers%20during%20subtitle%20parsing%22%5D%2C%22technical_details%22%3A%22ASAN%20reports%20a%20READ%20crash%20%28heap-buffer-overflow%29%20with%20no%20size%20or%20address%20details%20provided.%20The%20root%20cause%20is%20not%20pinpointed%20%E2%80%94%20the%20report%20lacks%20the%20crash%20trace%20and%20function%20name.%20It%20may%20be%20related%20to%20the%20CVE-2020-36430%20decode_chars%28%29%20integer-subtraction%20bug%20%28fixed%20in%200.15.1%29%20or%20may%20be%20a%20distinct%20novel%20issue%20depending%20on%20the%20target%20version.%22%2C%22title%22%3A%22Heap-buffer-overflow%20in%20wrap_lines_measure%20at%20ass_render.c%3A1902%20via%20malformed%20ASS/SSA%20subtitle%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-9WB9SMM6",
  "bug_class": "heap-buffer-overflow",
  "created_at": "2026-03-20T19:13:31+00:00",
  "description": "OSS-Fuzz discovered a heap-buffer-overflow (ASAN READ) in libass, the ASS/SSA subtitle renderer embedded in mpv, VLC, and FFmpeg-based players. The bug is an out-of-bounds read on heap memory triggered when parsing malformed subtitle data. An attacker who delivers a crafted subtitle file alongside media content can cause a crash or potentially leak heap memory contents. The specific crashing function and root cause are not identified in this report — no stack trace or affected code location was provided.",
  "location": "wrap_lines_measure() at libass/ass_render.c:1902",
  "poc_sha256": "f2a97f5480f0f390f4e5df3100ffa01c057e55cdf514767c586dc4c265882e8b",
  "project": "libass",
    "Craft a malicious ASS/SSA subtitle file",
    "Deliver it alongside or embedded within media content (e.g., MKV container)",
    "Victim opens the media in a player using libass (mpv, VLC, etc.)",
    "Heap-buffer-overflow triggers during subtitle parsing"
  "technical_details": "ASAN reports a READ crash (heap-buffer-overflow) with no size or address details provided. The root cause is not pinpointed — the report lacks the crash trace and function name. It may be related to the CVE-2020-36430 decode_chars() integer-subtraction bug (fixed in 0.15.1) or may be a distinct novel issue depending on the target version.",
  "title": "Heap-buffer-overflow in wrap_lines_measure at ass_render.c:1902 via malformed ASS/SSA subtitle",
```
