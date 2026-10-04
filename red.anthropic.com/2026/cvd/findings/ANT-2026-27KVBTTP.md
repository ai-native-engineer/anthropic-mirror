<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-27KVBTTP -->

# ANT-2026-27KVBTTP · wireshark/wireshark

## other low

[CVE-2026-76891](https://nvd.nist.gov/vuln/detail/CVE-2026-76891)

Maintainer low

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-27KVBTTP: sharkd tap request leaves dangling stack-object listeners

In sharkd\_session\_process\_tap(), a stack-local rtpstream\_tapinfo\_t is declared (~line 3608) and registered into the global tap listener queue at line 3865. The remove\_tap\_listener cleanup loop at lines ~4076-4083 only runs on normal function exit, but 14 error branches between lines 3632-4053 return early after registration when a later tapN parameter is invalid. A client sending {"tap0":"rtp-streams","tap1":"stat:bogus"} registers the stack object then bails out, leaving the global listener list pointing into a dead stack frame. Any follow-up request that triggers sharkd\_retap() (follow, iograph, download, tap) invokes rtpstream\_reset\_cb on the stale pointer, reading a function pointer at offset 0 and calling it, then treating stale stack bytes as GHashTable*/GList* and destroying them — yielding a crash or control-flow hijack in the long-lived, unauthenticated daemon.

**Project:** wireshark/wireshark
**Location:** `sharkd_session.c:3865`

The root cause is that stack-allocated tap state is registered into a global list but the unregister-cleanup loop is not on every exit path; early `return` statements in the tap0..tap15 processing loop skip it. Because rtpstream\_tapinfo\_t's first field (ui/rtp\_stream.h:88) is the tap\_reset function pointer, rtpstream\_reset\_cb (ui/tap-rtp-common.c:174-176) loads and calls a function pointer straight from reclaimed stack memory, then rtpstream\_reset() (ui/tap-rtp-common.c:149-165) dereferences further stale bytes as glib container pointers.

1. Connect to the sharkd socket.
2. Send {"req":"tap","tap0":"rtp-streams","tap1":"stat:bogus"} (or follow:bogus) so tap0 registers the stack-local rtp\_tapinfo and tap1 hits an early-return error branch before the cleanup loop.
3. Send a follow-up request that calls sharkd\_retap() — e.g. load a pcap containing RTP, or issue an iograph/follow/download/tap request.
4. reset\_tap\_listeners() invokes rtpstream\_reset\_cb on the dangling stack pointer, reading and calling ti->tap\_reset from stale stack memory.

## Suggested Fix

Ensure tap listeners are removed on every exit path: route all error branches through a common cleanup label (goto cleanup) that calls remove\_tap\_listener for each registered tap, or stop registering stack-allocated objects as global listeners (heap-allocate and track them for unconditional teardown).

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-27KVBTTP.

---

**Reference:** ANT-2026-27KVBTTP

Triage and disclosure were performed by Ada Logics.

```
diff --git a/sharkd_session.c b/sharkd_session.c
index 0577ff418fb..610967eef7d 100644
--- a/sharkd_session.c
+++ b/sharkd_session.c
@@ -3572,488 +3572,516 @@ sharkd_session_eo_register_tap_listener(register_eo_t *eo, const char *tap_type,
     return register_tap_listener(get_eo_tap_listener_name(eo), eo_object, tap_filter, 0, NULL, get_eo_packet_func(eo), tap_draw, NULL);

-/**
- * sharkd_session_process_tap()
- *
- * Process tap request
- *
- * Input:
- *   (m) tap0         - First tap request
- *   (o) tap1...tap15 - Other tap requests
- *
- * Output object with attributes:
- *   (m) taps  - array of object with attributes:
- *                  (m) tap  - tap name
- *                  (m) type - tap output type
- *                  ...
- *                  for type:stats see sharkd_session_process_tap_stats_cb()
- *                  for type:nstat see sharkd_session_process_tap_nstat_cb()
- *                  for type:conv see sharkd_session_process_tap_conv_cb()
- *                  for type:host see sharkd_session_process_tap_conv_cb()
- *                  for type:rtp-streams see sharkd_session_process_tap_rtp_cb()
- *                  for type:rtp-analyse see sharkd_session_process_tap_rtp_analyse_cb()
- *                  for type:eo see sharkd_session_process_tap_eo_cb()
- *                  for type:expert see sharkd_session_process_tap_expert_cb()
- *                  for type:rtd see sharkd_session_process_tap_rtd_cb()
- *                  for type:srt see sharkd_session_process_tap_srt_cb()
- *                  for type:flow see sharkd_session_process_tap_flow_cb()
- *
- *   (m) err   - error code
- */
 static void
-sharkd_session_process_tap(char *buf, const jsmntok_t *tokens, int count)
+rtpstream_free_cb(void *data)
-    void *taps_data[16];
-    GFreeFunc taps_free[16];
-    int taps_count = 0;
-    int i;
-    const char *tap_filter = json_find_attr(buf, tokens, count, "filter");
-
-    rtpstream_tapinfo_t rtp_tapinfo =
-    { NULL, NULL, NULL, NULL, 0, NULL, NULL, 0, TAP_ANALYSE, NULL, NULL, NULL, false, false};
+    rtpstream_tapinfo_t *rtp_tapinfo = (rtpstream_tapinfo_t*)data;

-    for (i = 0; i < 16; i++)
-    {
-        char tapbuf[32];
-        const char *tok_tap;
+    rtpstream_reset(rtp_tapinfo);
+    g_free(rtp_tapinfo);
+}

-        void *tap_data = NULL;
-        GFreeFunc tap_free = NULL;
-        GString *tap_error = NULL;
+static bool
+sharkd_session_register_tap(const char *tok_tap, const char *tap_filter, void **tap_datap, GFreeFunc *tap_freep)
+{
+    void *tap_data = NULL;
+    GFreeFunc tap_free = NULL;
+    GString *tap_error = NULL;

-        snprintf(tapbuf, sizeof(tapbuf), "tap%d", i);
-        tok_tap = json_find_attr(buf, tokens, count, tapbuf);
-        if (!tok_tap)
-            break;
+    if (!strncmp(tok_tap, "stat:", 5))
+    {
+        stats_tree_cfg *cfg = stats_tree_get_cfg_by_abbr(tok_tap + 5);
+        stats_tree *st;

-        if (!strncmp(tok_tap, "stat:", 5))
+        if (!cfg)
-            stats_tree_cfg *cfg = stats_tree_get_cfg_by_abbr(tok_tap + 5);
-            stats_tree *st;
+            sharkd_json_error(
+                    rpcid, -11001, NULL,
+                    "sharkd_session_process_tap() stat %s not found", tok_tap + 5
+                    );
+            return false;
+        }

-            if (!cfg)
-            {
-                sharkd_json_error(
-                        rpcid, -11001, NULL,
-                        "sharkd_session_process_tap() stat %s not found", tok_tap + 5
-                        );
-                return;
-            }
+        st = stats_tree_new(cfg, NULL, tap_filter);

-            st = stats_tree_new(cfg, NULL, tap_filter);
+        tap_error = register_tap_listener(st->cfg->tapname, st, st->filter, st->cfg->flags, stats_tree_reset, stats_tree_packet, sharkd_session_process_tap_stats_cb, NULL);

-            tap_error = register_tap_listener(st->cfg->tapname, st, st->filter, st->cfg->flags, stats_tree_reset, stats_tree_packet, sharkd_session_process_tap_stats_cb, NULL);
+        if (!tap_error && cfg->init)
+            cfg->init(st);

-            if (!tap_error && cfg->init)
-                cfg->init(st);
+        tap_data = st;
+        tap_free = sharkd_session_free_tap_stats_cb;
+    }
+    else if (!strcmp(tok_tap, "expert"))
+    {
+        struct sharkd_expert_tap *expert_tap;

-            tap_data = st;
-            tap_free = sharkd_session_free_tap_stats_cb;
-        }
-        else if (!strcmp(tok_tap, "expert"))
-        {
-            struct sharkd_expert_tap *expert_tap;
+        expert_tap = g_new0(struct sharkd_expert_tap, 1);
+        expert_tap->text = g_string_chunk_new(100);

-            expert_tap = g_new0(struct sharkd_expert_tap, 1);
-            expert_tap->text = g_string_chunk_new(100);
+        tap_error = register_tap_listener("expert", expert_tap, tap_filter, 0, NULL, sharkd_session_packet_tap_expert_cb, sharkd_session_process_tap_expert_cb, NULL);

-            tap_error = register_tap_listener("expert", expert_tap, tap_filter, 0, NULL, sharkd_session_packet_tap_expert_cb, sharkd_session_process_tap_expert_cb, NULL);
+        tap_data = expert_tap;
+        tap_free = sharkd_session_free_tap_expert_cb;
+    }
+    else if (!strncmp(tok_tap, "seqa:", 5))
+    {
+        seq_analysis_info_t *graph_analysis;
+        register_analysis_t *analysis;
+        const char *tap_name;
+        tap_packet_cb tap_func;
+        unsigned tap_flags;

-            tap_data = expert_tap;
-            tap_free = sharkd_session_free_tap_expert_cb;
-        }
-        else if (!strncmp(tok_tap, "seqa:", 5))
+        analysis = sequence_analysis_find_by_name(tok_tap + 5);
+        if (!analysis)
-            seq_analysis_info_t *graph_analysis;
-            register_analysis_t *analysis;
-            const char *tap_name;
-            tap_packet_cb tap_func;
-            unsigned tap_flags;
-
-            analysis = sequence_analysis_find_by_name(tok_tap + 5);
-            if (!analysis)
-            {
-                sharkd_json_error(
-                        rpcid, -11002, NULL,
-                        "sharkd_session_process_tap() seq analysis %s not found", tok_tap + 5
-                        );
-                return;
-            }
+            sharkd_json_error(
+                    rpcid, -11002, NULL,
+                    "sharkd_session_process_tap() seq analysis %s not found", tok_tap + 5
+                    );
+            return false;
+        }

-            graph_analysis = sequence_analysis_info_new();
-            graph_analysis->name = tok_tap + 5;
-            /* TODO, make configurable */
-            graph_analysis->any_addr = false;
+        graph_analysis = sequence_analysis_info_new();
+        graph_analysis->name = tok_tap + 5;
+        /* TODO, make configurable */
+        graph_analysis->any_addr = false;

-            tap_name  = sequence_analysis_get_tap_listener_name(analysis);
-            tap_flags = sequence_analysis_get_tap_flags(analysis);
-            tap_func  = sequence_analysis_get_packet_func(analysis);
+        tap_name  = sequence_analysis_get_tap_listener_name(analysis);
+        tap_flags = sequence_analysis_get_tap_flags(analysis);
+        tap_func  = sequence_analysis_get_packet_func(analysis);

-            tap_error = register_tap_listener(tap_name, graph_analysis, tap_filter, tap_flags, NULL, tap_func, sharkd_session_process_tap_flow_cb, NULL);
+        tap_error = register_tap_listener(tap_name, graph_analysis, tap_filter, tap_flags, NULL, tap_func, sharkd_session_process_tap_flow_cb, NULL);

-            tap_data = graph_analysis;
-            tap_free = sharkd_session_free_tap_flow_cb;
-        }
-        else if (!strncmp(tok_tap, "conv:", 5) || !strncmp(tok_tap, "endpt:", 6))
+        tap_data = graph_analysis;
+        tap_free = sharkd_session_free_tap_flow_cb;
+    }
+    else if (!strncmp(tok_tap, "conv:", 5) || !strncmp(tok_tap, "endpt:", 6))
+    {
+        struct register_ct *ct = NULL;
+        const char *ct_tapname;
+        struct sharkd_conv_tap_data *ct_data;
+        tap_packet_cb tap_func =
… (truncated)
```

<https://github.com/wireshark/wireshark/commit/178939f126d5eeb442d96e10b0ea4c1cfc6920e9>

1. 2026-04-02
2. 2026-07-06
3. 2026-08-12
4. 2026-08-12
5. 2026-09-28

6ed8764aad5fa25e5525477fd786fbf8d794d34771bc0f74ac4138bd7696d6df8346a2f218b9a8cecbfbf97e2505eb75392ac5b08d3c66090de68db8b96a70c7

Committed 2026-07-22 07:34 UTC

Revealed 2026-09-28 20:36 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-27KVBTTP%22%2C%22bug_class%22%3A%22Use-After-Return%20/%20Memory%20Corruption%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-16T14%3A11%3A16%2B00%3A00%22%2C%22description%22%3A%22In%20sharkd_session_process_tap%28%29%2C%20a%20stack-local%20rtpstream_tapinfo_t%20is%20declared%20%28~line%203608%29%20and%20registered%20into%20the%20global%20tap%20listener%20queue%20at%20line%203865.%20The%20remove_tap_listener%20cleanup%20loop%20at%20lines%20~4076-4083%20only%20runs%20on%20normal%20function%20exit%2C%20but%2014%20error%20branches%20between%20lines%203632-4053%20return%20early%20after%20registration%20when%20a%20later%20tapN%20parameter%20is%20invalid.%20A%20client%20sending%20%7B%5C%22tap0%5C%22%3A%5C%22rtp-streams%5C%22%2C%5C%22tap1%5C%22%3A%5C%22stat%3Abogus%5C%22%7D%20registers%20the%20stack%20object%20then%20bails%20out%2C%20leaving%20the%20global%20listener%20list%20pointing%20into%20a%20dead%20stack%20frame.%20Any%20follow-up%20request%20that%20triggers%20sharkd_retap%28%29%20%28follow%2C%20iograph%2C%20download%2C%20tap%29%20invokes%20rtpstream_reset_cb%20on%20the%20stale%20pointer%2C%20reading%20a%20function%20pointer%20at%20offset%200%20and%20calling%20it%2C%20then%20treating%20stale%20stack%20bytes%20as%20GHashTable%2A/GList%2A%20and%20destroying%20them%20%E2%80%94%20yielding%20a%20crash%20or%20control-flow%20hijack%20in%20the%20long-lived%2C%20unauthenticated%20daemon.%22%2C%22discovered_at%22%3A%222026-04-02T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22sharkd_session.c%3A3865%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22wireshark/wireshark%22%2C%22reproduction%22%3A%5B%221.%20Connect%20to%20the%20sharkd%20socket.%22%2C%222.%20Send%20%7B%5C%22req%5C%22%3A%5C%22tap%5C%22%2C%5C%22tap0%5C%22%3A%5C%22rtp-streams%5C%22%2C%5C%22tap1%5C%22%3A%5C%22stat%3Abogus%5C%22%7D%20%28or%20follow%3Abogus%29%20so%20tap0%20registers%20the%20stack-local%20rtp_tapinfo%20and%20tap1%20hits%20an%20early-return%20error%20branch%20before%20the%20cleanup%20loop.%22%2C%223.%20Send%20a%20follow-up%20request%20that%20calls%20sharkd_retap%28%29%20%E2%80%94%20e.g.%20load%20a%20pcap%20containing%20RTP%2C%20or%20issue%20an%20iograph/follow/download/tap%20request.%22%2C%224.%20reset_tap_listeners%28%29%20invokes%20rtpstream_reset_cb%20on%20the%20dangling%20stack%20pointer%2C%20reading%20and%20calling%20ti-%3Etap_reset%20from%20stale%20stack%20memory.%22%5D%2C%22technical_details%22%3A%22The%20root%20cause%20is%20that%20stack-allocated%20tap%20state%20is%20registered%20into%20a%20global%20list%20but%20the%20unregister-cleanup%20loop%20is%20not%20on%20every%20exit%20path%3B%20early%20%60return%60%20statements%20in%20the%20tap0..tap15%20processing%20loop%20skip%20it.%20Because%20rtpstream_tapinfo_t%27s%20first%20field%20%28ui/rtp_stream.h%3A88%29%20is%20the%20tap_reset%20function%20pointer%2C%20rtpstream_reset_cb%20%28ui/tap-rtp-common.c%3A174-176%29%20loads%20and%20calls%20a%20function%20pointer%20straight%20from%20reclaimed%20stack%20memory%2C%20then%20rtpstream_reset%28%29%20%28ui/tap-rtp-common.c%3A149-165%29%20dereferences%20further%20stale%20bytes%20as%20glib%20container%20pointers.%22%2C%22title%22%3A%22sharkd%20tap%20request%20leaves%20dangling%20stack-object%20listeners%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-27KVBTTP",
  "bug_class": "Use-After-Return / Memory Corruption",
  "created_at": "2026-04-16T14:11:16+00:00",
  "description": "In sharkd_session_process_tap(), a stack-local rtpstream_tapinfo_t is declared (~line 3608) and registered into the global tap listener queue at line 3865. The remove_tap_listener cleanup loop at lines ~4076-4083 only runs on normal function exit, but 14 error branches between lines 3632-4053 return early after registration when a later tapN parameter is invalid. A client sending {\"tap0\":\"rtp-streams\",\"tap1\":\"stat:bogus\"} registers the stack object then bails out, leaving the global listener list pointing into a dead stack frame. Any follow-up request that triggers sharkd_retap() (follow, iograph, download, tap) invokes rtpstream_reset_cb on the stale pointer, reading a function pointer at offset 0 and calling it, then treating stale stack bytes as GHashTable*/GList* and destroying them — yielding a crash or control-flow hijack in the long-lived, unauthenticated daemon.",
  "discovered_at": "2026-04-02T00:00:00+00:00",
  "location": "sharkd_session.c:3865",
  "project": "wireshark/wireshark",
    "1. Connect to the sharkd socket.",
    "2. Send {\"req\":\"tap\",\"tap0\":\"rtp-streams\",\"tap1\":\"stat:bogus\"} (or follow:bogus) so tap0 registers the stack-local rtp_tapinfo and tap1 hits an early-return error branch before the cleanup loop.",
    "3. Send a follow-up request that calls sharkd_retap() — e.g. load a pcap containing RTP, or issue an iograph/follow/download/tap request.",
    "4. reset_tap_listeners() invokes rtpstream_reset_cb on the dangling stack pointer, reading and calling ti->tap_reset from stale stack memory."
  "technical_details": "The root cause is that stack-allocated tap state is registered into a global list but the unregister-cleanup loop is not on every exit path; early `return` statements in the tap0..tap15 processing loop skip it. Because rtpstream_tapinfo_t's first field (ui/rtp_stream.h:88) is the tap_reset function pointer, rtpstream_reset_cb (ui/tap-rtp-common.c:174-176) loads and calls a function pointer straight from reclaimed stack memory, then rtpstream_reset() (ui/tap-rtp-common.c:149-165) dereferences further stale bytes as glib container pointers.",
  "title": "sharkd tap request leaves dangling stack-object listeners",
```
