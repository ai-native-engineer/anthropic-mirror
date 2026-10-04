<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-GACTPNVK -->

# ANT-2026-GACTPNVK · wireshark/wireshark

## other low

[CVE-2026-76890](https://nvd.nist.gov/vuln/detail/CVE-2026-76890)

Maintainer low

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-GACTPNVK: sharkd iograph error path leaks stack-array listeners

sharkd\_session\_process\_iograph() declares `struct sharkd_iograph graphs[10]` on the stack and registers each as a tap listener. If a later graph in the same request has an invalid filter or field, the function emits an error and returns without removing the listeners already registered for earlier valid graphs, leaving the global tap\_listener\_queue holding pointers into a dead stack frame. On the next request that triggers retap/redissection, the io-stat packet callback runs with a dangling tapdata pointer, reads garbage fields, and calls g\_realloc on stack garbage before writing back into the reused frame. A connected sharkd client fully controls the graphN/filterN JSON strings needed to trigger this, yielding memory corruption and a plausible path to RCE.

**Project:** wireshark/wireshark
**Location:** `sharkd_session.c:4758`

The error path at lines 4758–4765 returns immediately when graph->error is set, but listener removal (remove\_tap\_listener at line 4818) is only reached on the success path after the loop. Because register\_tap\_listener stores the address of the stack-local graph struct (tap.c:576–608) into the global tap\_listener\_queue, any subsequent retap invokes sharkd\_iograph\_packet on freed stack memory, where it dereferences graph->interval/num\_items/space\_items and calls g\_realloc(graph->items, ...) on whatever now occupies that slot.

1. Send {"req":"iograph","graph0":"packets","graph1":"packets","filter1":"!!invalid!!"} — graph0 registers &graphs[0]; graph1's filter fails compilation and the handler returns early without cleanup.
2. Send any request that calls sharkd\_retap() (e.g. {"req":"iograph","graph0":"bytes"}, or tap/follow/download-rtp).
3. tap\_push\_tapped\_queue invokes sharkd\_iograph\_packet with tapdata pointing at reused stack memory, calling g\_realloc on garbage and writing into the current frame.

## Suggested Fix

Remove all successfully-registered tap listeners before any early return — restructure to a single exit point with unconditional cleanup, or validate all graph inputs before registering any listener.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-GACTPNVK.

---

**Reference:** ANT-2026-GACTPNVK

Triage and disclosure were performed by Ada Logics.

```
diff --git a/sharkd_session.c b/sharkd_session.c
index 610967eef7d..481119fc69f 100644
--- a/sharkd_session.c
+++ b/sharkd_session.c
@@ -4680,10 +4680,9 @@ sharkd_session_process_iograph(char *buf, const jsmntok_t *tokens, int count)
     const char *tok_interval = json_find_attr(buf, tokens, count, "interval");
     const char *tok_interval_units = json_find_attr(buf, tokens, count, "interval_units");
     struct sharkd_iograph graphs[10];
-    bool is_any_ok = false;
-    int graph_count;
+    unsigned graph_count;

-    int i;
+    unsigned i;

     /* default: 1000ms = one per second */
     uint32_t interval = 1000;
@@ -4721,7 +4720,7 @@ sharkd_session_process_iograph(char *buf, const jsmntok_t *tokens, int count)
         interval_us = 1000000 * interval;

-    for (i = graph_count = 0; i < (int) G_N_ELEMENTS(graphs); i++)
+    for (i = graph_count = 0; i < G_N_ELEMENTS(graphs); i++)
         struct sharkd_iograph *graph = &graphs[graph_count];

@@ -4791,8 +4790,6 @@ sharkd_session_process_iograph(char *buf, const jsmntok_t *tokens, int count)
         if (!graph->error)
             graph->error = register_tap_listener("frame", graph, tok_filter, TL_REQUIRES_PROTO_TREE, NULL, sharkd_iograph_packet, NULL, NULL);

-        graph_count++;
-
         if (graph->error)
             sharkd_json_error(
@@ -4800,15 +4797,14 @@ sharkd_session_process_iograph(char *buf, const jsmntok_t *tokens, int count)
                     "%s", graph->error->str
                     );
             g_string_free(graph->error, TRUE);
-            return;
+            goto cleanup;

-        if (graph->error == NULL)
-            is_any_ok = true;
+        graph_count++;

     /* retap only if we have at least one ok */
-    if (is_any_ok)
+    if (graph_count)
         sharkd_retap();

     sharkd_json_result_prologue(rpcid);
@@ -4853,12 +4849,19 @@ sharkd_session_process_iograph(char *buf, const jsmntok_t *tokens, int count)
         json_dumper_end_object(&dumper);

-        remove_tap_listener(graph);
-        g_free(graph->items);
     sharkd_json_array_close();

     sharkd_json_result_epilogue();
+
+cleanup:
+    for (i = 0; i < graph_count; i++)
+    {
+        struct sharkd_iograph *graph = &graphs[i];
+
+        remove_tap_listener(graph);
+        g_free(graph->items);
+    }

 /**
```

<https://github.com/wireshark/wireshark/commit/d43d89d201b18f1c6d77460e52b4e6b5a4ec68f8>

1. 2026-04-02
2. 2026-07-06
3. 2026-08-12
4. 2026-08-12
5. 2026-09-28

ab180bc6dad222dd8d350da26913a397d4ed975e56370475735de8b0eaf7643f9df293cb10754ccd26af8a4fdf0452eaaf04f98a01c8dbabbd3efd0af47a4785

Committed 2026-07-22 07:34 UTC

Revealed 2026-09-28 20:38 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-GACTPNVK%22%2C%22bug_class%22%3A%22Use-After-Return%20/%20Memory%20Corruption%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-16T14%3A11%3A17%2B00%3A00%22%2C%22description%22%3A%22sharkd_session_process_iograph%28%29%20declares%20%60struct%20sharkd_iograph%20graphs%5B10%5D%60%20on%20the%20stack%20and%20registers%20each%20as%20a%20tap%20listener.%20If%20a%20later%20graph%20in%20the%20same%20request%20has%20an%20invalid%20filter%20or%20field%2C%20the%20function%20emits%20an%20error%20and%20returns%20without%20removing%20the%20listeners%20already%20registered%20for%20earlier%20valid%20graphs%2C%20leaving%20the%20global%20tap_listener_queue%20holding%20pointers%20into%20a%20dead%20stack%20frame.%20On%20the%20next%20request%20that%20triggers%20retap/redissection%2C%20the%20io-stat%20packet%20callback%20runs%20with%20a%20dangling%20tapdata%20pointer%2C%20reads%20garbage%20fields%2C%20and%20calls%20g_realloc%20on%20stack%20garbage%20before%20writing%20back%20into%20the%20reused%20frame.%20A%20connected%20sharkd%20client%20fully%20controls%20the%20graphN/filterN%20JSON%20strings%20needed%20to%20trigger%20this%2C%20yielding%20memory%20corruption%20and%20a%20plausible%20path%20to%20RCE.%22%2C%22discovered_at%22%3A%222026-04-02T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22sharkd_session.c%3A4758%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22wireshark/wireshark%22%2C%22reproduction%22%3A%5B%221.%20Send%20%7B%5C%22req%5C%22%3A%5C%22iograph%5C%22%2C%5C%22graph0%5C%22%3A%5C%22packets%5C%22%2C%5C%22graph1%5C%22%3A%5C%22packets%5C%22%2C%5C%22filter1%5C%22%3A%5C%22%21%21invalid%21%21%5C%22%7D%20%E2%80%94%20graph0%20registers%20%26graphs%5B0%5D%3B%20graph1%27s%20filter%20fails%20compilation%20and%20the%20handler%20returns%20early%20without%20cleanup.%22%2C%222.%20Send%20any%20request%20that%20calls%20sharkd_retap%28%29%20%28e.g.%20%7B%5C%22req%5C%22%3A%5C%22iograph%5C%22%2C%5C%22graph0%5C%22%3A%5C%22bytes%5C%22%7D%2C%20or%20tap/follow/download-rtp%29.%22%2C%223.%20tap_push_tapped_queue%20invokes%20sharkd_iograph_packet%20with%20tapdata%20pointing%20at%20reused%20stack%20memory%2C%20calling%20g_realloc%20on%20garbage%20and%20writing%20into%20the%20current%20frame.%22%5D%2C%22technical_details%22%3A%22The%20error%20path%20at%20lines%204758%E2%80%934765%20returns%20immediately%20when%20graph-%3Eerror%20is%20set%2C%20but%20listener%20removal%20%28remove_tap_listener%20at%20line%204818%29%20is%20only%20reached%20on%20the%20success%20path%20after%20the%20loop.%20Because%20register_tap_listener%20stores%20the%20address%20of%20the%20stack-local%20graph%20struct%20%28tap.c%3A576%E2%80%93608%29%20into%20the%20global%20tap_listener_queue%2C%20any%20subsequent%20retap%20invokes%20sharkd_iograph_packet%20on%20freed%20stack%20memory%2C%20where%20it%20dereferences%20graph-%3Einterval/num_items/space_items%20and%20calls%20g_realloc%28graph-%3Eitems%2C%20...%29%20on%20whatever%20now%20occupies%20that%20slot.%22%2C%22title%22%3A%22sharkd%20iograph%20error%20path%20leaks%20stack-array%20listeners%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-GACTPNVK",
  "bug_class": "Use-After-Return / Memory Corruption",
  "created_at": "2026-04-16T14:11:17+00:00",
  "description": "sharkd_session_process_iograph() declares `struct sharkd_iograph graphs[10]` on the stack and registers each as a tap listener. If a later graph in the same request has an invalid filter or field, the function emits an error and returns without removing the listeners already registered for earlier valid graphs, leaving the global tap_listener_queue holding pointers into a dead stack frame. On the next request that triggers retap/redissection, the io-stat packet callback runs with a dangling tapdata pointer, reads garbage fields, and calls g_realloc on stack garbage before writing back into the reused frame. A connected sharkd client fully controls the graphN/filterN JSON strings needed to trigger this, yielding memory corruption and a plausible path to RCE.",
  "discovered_at": "2026-04-02T00:00:00+00:00",
  "location": "sharkd_session.c:4758",
  "project": "wireshark/wireshark",
    "1. Send {\"req\":\"iograph\",\"graph0\":\"packets\",\"graph1\":\"packets\",\"filter1\":\"!!invalid!!\"} — graph0 registers &graphs[0]; graph1's filter fails compilation and the handler returns early without cleanup.",
    "2. Send any request that calls sharkd_retap() (e.g. {\"req\":\"iograph\",\"graph0\":\"bytes\"}, or tap/follow/download-rtp).",
    "3. tap_push_tapped_queue invokes sharkd_iograph_packet with tapdata pointing at reused stack memory, calling g_realloc on garbage and writing into the current frame."
  "technical_details": "The error path at lines 4758–4765 returns immediately when graph->error is set, but listener removal (remove_tap_listener at line 4818) is only reached on the success path after the loop. Because register_tap_listener stores the address of the stack-local graph struct (tap.c:576–608) into the global tap_listener_queue, any subsequent retap invokes sharkd_iograph_packet on freed stack memory, where it dereferences graph->interval/num_items/space_items and calls g_realloc(graph->items, ...) on whatever now occupies that slot.",
  "title": "sharkd iograph error path leaks stack-array listeners",
```
