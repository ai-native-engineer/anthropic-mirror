<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-P7DSVPH6 -->

# ANT-2026-P7DSVPH6 · bytecodealliance/wasm-micro-runtime

## heap-buffer-overflow critical

[GHSA-wj3p-xhqm-pffc](https://github.com/wasm-micro-runtime/wasm-micro-runtime/security/advisories/GHSA-wj3p-xhqm-pffc)

Claude critical
Security research firm critical
Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-P7DSVPH6: Heap-buffer-overflow in posix.c:2253

In WAMR's sandboxed WASI layer, wasmtime\_ssp\_poll\_oneoff allocates a 16-byte heap buffer at posix.c:2186 but later writes 8 bytes past its end at posix.c:2253 while emitting poll events. A 116-byte valid WebAssembly module that invokes the WASI poll\_oneoff import deterministically triggers the overflow (3/3 identical ASAN reports in a clean container). The attacker controls the guest Wasm module and thus the poll\_oneoff subscription arguments that drive the event count. The result is an out-of-bounds heap WRITE in the host runtime from guest-controlled sandboxed code.

**Project:** bytecodealliance/wasm-micro-runtime
**Location:** `posix.c:2253`

ASAN: heap-buffer-overflow, WRITE of size 8, 0 bytes to the right of a 16-byte region allocated at posix.c:2186. The output buffer sized at allocation time is too small for the number of events subsequently written at posix.c:2253, so the event-store loop runs off the end of the heap block.

**Crash trace:**

```
The PoC is a 116-byte valid WebAssembly module that deterministically triggers a heap-buffer-overflow in WAMR's WASI `poll_oneoff` implementation.

All 3 runs in a fresh container produced identical ASAN reports:
- Error: heap-buffer-overflow (WRITE of size 8)
- Crash location: `wasmtime_ssp_poll_oneoff` at `posix.c:2253`
- Root cause: A 16-byte heap allocation is made at `posix.c:2186`, but a write at `posix.c:2253` goes exactly 0 bytes past the end of that allocation (writing 8 bytes beyond the 16-byte buffer boundary)
- Call chain: `main` -> `wasm_application_execute_main` -> `wasm_interp_call_func_bytecode` -> `wasi_poll_oneoff` -> `wasmtime_ssp_poll_oneoff` (crash)
- Exit code: 1 in all runs
- No OOM or timeout indicators

The crash is a genuine memory safety bug in the WAMR project's libc-wasi sandboxed system primitives code, specifically in the poll_oneoff event handling where the output buffer is under-allocated relative to the number of events being written.
```

1. Craft a small (≈116-byte) Wasm module that imports and invokes wasi\_snapshot\_preview1 poll\_oneoff with subscription arguments that yield more output events than the host allocates space for
2. Execute the module with iwasm / wasm\_application\_execute\_main
3. wasi\_poll\_oneoff calls wasmtime\_ssp\_poll\_oneoff, which allocates a 16-byte buffer at posix.c:2186
4. The event-write loop at posix.c:2253 stores 8 bytes past the end of that buffer, corrupting adjacent heap memory

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-P7DSVPH6.

---

**Reference:** ANT-2026-P7DSVPH6

Triage and disclosure were performed by Ada Logics.

:   critical

The change that resolved this finding.

```
diff --git a/core/iwasm/libraries/libc-uvwasi/libc_uvwasi_wrapper.c b/core/iwasm/libraries/libc-uvwasi/libc_uvwasi_wrapper.c
index 35d091e78d..fad77406fe 100644
--- a/core/iwasm/libraries/libc-uvwasi/libc_uvwasi_wrapper.c
+++ b/core/iwasm/libraries/libc-uvwasi/libc_uvwasi_wrapper.c
@@ -927,13 +927,16 @@ wasi_poll_oneoff(wasm_exec_env_t exec_env, const wasi_subscription_t *in,
     wasm_module_inst_t module_inst = get_module_inst(exec_env);
     uvwasi_t *uvwasi = get_wasi_ctx(module_inst);
     uvwasi_size_t nevents;
+    uint64 subscriptions_size =
+        (uint64)nsubscriptions * sizeof(wasi_subscription_t);
+    uint64 events_size = (uint64)nsubscriptions * sizeof(wasi_event_t);
     wasi_errno_t err;

     if (!uvwasi)
         return (wasi_errno_t)-1;

-    if (!validate_native_addr((void *)in, (uint64)sizeof(wasi_subscription_t))
-        || !validate_native_addr(out, (uint64)sizeof(wasi_event_t))
+    if (!validate_native_addr((void *)in, subscriptions_size)
+        || !validate_native_addr(out, events_size)
         || !validate_native_addr(nevents_app, (uint64)sizeof(uint32)))
         return (wasi_errno_t)-1;

diff --git a/core/iwasm/libraries/libc-wasi/libc_wasi_wrapper.c b/core/iwasm/libraries/libc-wasi/libc_wasi_wrapper.c
index 5ab189e71d..7eebf12ef9 100644
--- a/core/iwasm/libraries/libc-wasi/libc_wasi_wrapper.c
+++ b/core/iwasm/libraries/libc-wasi/libc_wasi_wrapper.c
@@ -1093,13 +1093,16 @@ wasi_poll_oneoff(wasm_exec_env_t exec_env, const wasi_subscription_t *in,
     wasi_ctx_t wasi_ctx = get_wasi_ctx(module_inst);
     struct fd_table *curfds = wasi_ctx_get_curfds(wasi_ctx);
     size_t nevents = 0;
+    uint64 subscriptions_size =
+        (uint64)nsubscriptions * sizeof(wasi_subscription_t);
+    uint64 events_size = (uint64)nsubscriptions * sizeof(wasi_event_t);
     wasi_errno_t err;

     if (!wasi_ctx)
         return (wasi_errno_t)-1;

-    if (!validate_native_addr((void *)in, (uint64)sizeof(wasi_subscription_t))
-        || !validate_native_addr(out, (uint64)sizeof(wasi_event_t))
+    if (!validate_native_addr((void *)in, subscriptions_size)
+        || !validate_native_addr(out, events_size)
         || !validate_native_addr(nevents_app, (uint64)sizeof(uint32)))
         return (wasi_errno_t)-1;

diff --git a/tests/regression/ba-issues/build_wamr.sh b/tests/regression/ba-issues/build_wamr.sh
index 9f2b3c716f..233f7bad8f 100755
--- a/tests/regression/ba-issues/build_wamr.sh
+++ b/tests/regression/ba-issues/build_wamr.sh
@@ -66,4 +66,8 @@ build_iwasm "-DWAMR_BUILD_BRANCH_HINTS=1" "default-branch-hints-enabled"
 # build default iwasm for testing tail call with fast-interp
 build_iwasm "-DWAMR_BUILD_REF_TYPES=1 -DWAMR_BUILD_FAST_INTERP=1 -DWAMR_BUILD_TAIL_CALL=1 -DWAMR_BUILD_LIBC_WASI=0" "default-tail-call-wasi-disabled"

+# build classic-interp iwasm with ASAN and hardware bounds checks disabled
+# for poll_oneoff host memory safety regressions
+build_iwasm "-DWAMR_BUILD_REF_TYPES=1 -DWAMR_BUILD_FAST_INTERP=0 -DWAMR_BUILD_AOT=0 -DWAMR_BUILD_JIT=0 -DWAMR_BUILD_FAST_JIT=0 -DWAMR_BUILD_SIMD=0 -DWAMR_DISABLE_HW_BOUND_CHECK=1" "poll-oneoff-asan"
+
 # TODO: add more version of iwasm, for example, sgx version
diff --git a/tests/regression/ba-issues/issues/issue-980004/poll_oneoff_out_of_bounds_write.wasm b/tests/regression/ba-issues/issues/issue-980004/poll_oneoff_out_of_bounds_write.wasm
new file mode 100644
index 0000000000..ec56c43f3d
Binary files /dev/null and b/tests/regression/ba-issues/issues/issue-980004/poll_oneoff_out_of_bounds_write.wasm differ
diff --git a/tests/regression/ba-issues/issues/issue-980004/poll_oneoff_out_of_bounds_write.wat b/tests/regression/ba-issues/issues/issue-980004/poll_oneoff_out_of_bounds_write.wat
new file mode 100644
index 0000000000..2121e0b64e
--- /dev/null
+++ b/tests/regression/ba-issues/issues/issue-980004/poll_oneoff_out_of_bounds_write.wat
@@ -0,0 +1,38 @@
+(module
+  (import "wasi_snapshot_preview1" "poll_oneoff"
+    (func $poll_oneoff (param i32 i32 i32 i32) (result i32)))
+  (import "wasi_snapshot_preview1" "proc_exit"
+    (func $proc_exit (param i32)))
+  (memory (export "memory") 1)
+  (func (export "_start")
+    ;; Two absolute clock subscriptions ensure poll_oneoff writes two events.
+    i32.const 0
+    i64.const 1
+    i64.store
+    i32.const 8
+    i32.const 0
+    i32.store8
+    i32.const 40
+    i32.const 1
+    i32.store16
+
+    i32.const 48
+    i64.const 2
+    i64.store
+    i32.const 56
+    i32.const 0
+    i32.store8
+    i32.const 88
+    i32.const 1
+    i32.store16
+
+    ;; out points to exactly one wasi_event_t at the end of memory.
+    i32.const 0
+    i32.const 65504
+    i32.const 2
+    i32.const 65500
+    call $poll_oneoff
+    drop
+
+    i32.const 0
+    call $proc_exit))
diff --git a/tests/regression/ba-issues/issues/issue-980005/poll_oneoff_out_of_bounds_read.wasm b/tests/regression/ba-issues/issues/issue-980005/poll_oneoff_out_of_bounds_read.wasm
new file mode 100644
index 0000000000..30ebce2925
Binary files /dev/null and b/tests/regression/ba-issues/issues/issue-980005/poll_oneoff_out_of_bounds_read.wasm differ
diff --git a/tests/regression/ba-issues/issues/issue-980005/poll_oneoff_out_of_bounds_read.wat b/tests/regression/ba-issues/issues/issue-980005/poll_oneoff_out_of_bounds_read.wat
new file mode 100644
index 0000000000..cce8e8b299
--- /dev/null
+++ b/tests/regression/ba-issues/issues/issue-980005/poll_oneoff_out_of_bounds_read.wat
@@ -0,0 +1,28 @@
+(module
+  (import "wasi_snapshot_preview1" "poll_oneoff"
+    (func $poll_oneoff (param i32 i32 i32 i32) (result i32)))
+  (import "wasi_snapshot_preview1" "proc_exit"
+    (func $proc_exit (param i32)))
+  (memory (export "memory") 1)
+  (func (export "_start")
+    ;; Place exactly one subscription at the end of memory.
+    i32.const 65488
+    i64.const 1
+    i64.store
+    i32.const 65496
+    i32.const 0
+    i32.store8
+    i32.const 65528
+    i32.const 1
+    i32.store16
+
+    ;; nsubscriptions=2 forces validation of the full subscription array.
+    i32.const 65488
+    i32.const 64
+    i32.const 2
+    i32.const 60
+    call $poll_oneoff
+    drop
+
+    i32.const 0
+    call $proc_exit))
diff --git a/tests/regression/ba-issues/running_config.json b/tests/regression/ba-issues/running_config.json
index 9083af9014..ebde50babd 100644
--- a/tests/regression/ba-issues/running_config.json
+++ b/tests/regression/ba-issues/running_config.json
@@ -1853,6 +1853,38 @@

         },
+        {
+            "deprecated": false,
+            "ids": [
+                980004
+            ],
+            "runtime": "iwasm-poll-oneoff-asan",
+            "file": "poll_oneoff_out_of_bounds_write.wasm",
+            "mode": "classic-interp",
+            "options": "-f _start",
+            "argument": "",
+            "expected return": {
+                "ret code": 1,
+                "stdout content": "Exception: out of bounds memory access",
+                "description": "poll_oneoff rejects an undersized event buffer for multi-subscription WASI calls"
+            }
+        },
+        {
+            "deprecated": false,
+            "ids": [
+                980005
+            ],
+            "runtime": "iwasm-poll-oneoff-asan",
+            "file": "poll_oneoff_out_of_bounds_read.wasm",
+            "mode": "classic-interp",
+            "options": "-f _start",
+            "argument": "",
+            "expected return": {
+                "ret code": 1,
+                "stdout content": "Exception: out of bounds memory access",
+                "description": "poll_oneoff rejects an undersized subscription array for multi-subscription WASI calls"
+            }
+        },
             "deprecated": false,
             "ids": [
```

<https://github.com/bytecodealliance/wasm-micro-runtime/commit/1f98fb01d09b2ef5e49dc0be2e6006f962fd87f1>

1. 2026-03-24
2. 2026-05-07
3. 2026-06-25
4. 2026-08-17

9680ba7f19079c28d92bf1d9291a85ad88dbecf9fadd1316805a0ed4783ceb902a261fe1af85a092280115e0fde1b6183c2ac7af27cc7aa23ebbbc23d0bd29ed

Committed 2026-05-07 10:18 UTC

Revealed 2026-08-17 17:47 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-P7DSVPH6%22%2C%22bug_class%22%3A%22Heap-buffer-overflow%22%2C%22claude_severity%22%3A%22critical%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-24T20%3A43%3A47%2B00%3A00%22%2C%22description%22%3A%22In%20WAMR%27s%20sandboxed%20WASI%20layer%2C%20wasmtime_ssp_poll_oneoff%20allocates%20a%2016-byte%20heap%20buffer%20at%20posix.c%3A2186%20but%20later%20writes%208%20bytes%20past%20its%20end%20at%20posix.c%3A2253%20while%20emitting%20poll%20events.%20A%20116-byte%20valid%20WebAssembly%20module%20that%20invokes%20the%20WASI%20poll_oneoff%20import%20deterministically%20triggers%20the%20overflow%20%283/3%20identical%20ASAN%20reports%20in%20a%20clean%20container%29.%20The%20attacker%20controls%20the%20guest%20Wasm%20module%20and%20thus%20the%20poll_oneoff%20subscription%20arguments%20that%20drive%20the%20event%20count.%20The%20result%20is%20an%20out-of-bounds%20heap%20WRITE%20in%20the%20host%20runtime%20from%20guest-controlled%20sandboxed%20code.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3A%22posix.c%3A2253%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22wasm-micro-runtime%22%2C%22reproduction%22%3A%5B%221.%20Craft%20a%20small%20%28%E2%89%88116-byte%29%20Wasm%20module%20that%20imports%20and%20invokes%20wasi_snapshot_preview1%20poll_oneoff%20with%20subscription%20arguments%20that%20yield%20more%20output%20events%20than%20the%20host%20allocates%20space%20for%22%2C%222.%20Execute%20the%20module%20with%20iwasm%20/%20wasm_application_execute_main%22%2C%223.%20wasi_poll_oneoff%20calls%20wasmtime_ssp_poll_oneoff%2C%20which%20allocates%20a%2016-byte%20buffer%20at%20posix.c%3A2186%22%2C%224.%20The%20event-write%20loop%20at%20posix.c%3A2253%20stores%208%20bytes%20past%20the%20end%20of%20that%20buffer%2C%20corrupting%20adjacent%20heap%20memory%22%5D%2C%22technical_details%22%3A%22ASAN%3A%20heap-buffer-overflow%2C%20WRITE%20of%20size%208%2C%200%20bytes%20to%20the%20right%20of%20a%2016-byte%20region%20allocated%20at%20posix.c%3A2186.%20The%20output%20buffer%20sized%20at%20allocation%20time%20is%20too%20small%20for%20the%20number%20of%20events%20subsequently%20written%20at%20posix.c%3A2253%2C%20so%20the%20event-store%20loop%20runs%20off%20the%20end%20of%20the%20heap%20block.%22%2C%22title%22%3A%22Heap-buffer-overflow%20in%20posix.c%3A2253%22%2C%22vendor_severity%22%3A%22critical%22%7D)

```
  "ant_id": "ANT-2026-P7DSVPH6",
  "bug_class": "Heap-buffer-overflow",
  "claude_severity": "critical",
  "created_at": "2026-03-24T20:43:47+00:00",
  "description": "In WAMR's sandboxed WASI layer, wasmtime_ssp_poll_oneoff allocates a 16-byte heap buffer at posix.c:2186 but later writes 8 bytes past its end at posix.c:2253 while emitting poll events. A 116-byte valid WebAssembly module that invokes the WASI poll_oneoff import deterministically triggers the overflow (3/3 identical ASAN reports in a clean container). The attacker controls the guest Wasm module and thus the poll_oneoff subscription arguments that drive the event count. The result is an out-of-bounds heap WRITE in the host runtime from guest-controlled sandboxed code.",
  "location": "posix.c:2253",
  "project": "wasm-micro-runtime",
    "1. Craft a small (≈116-byte) Wasm module that imports and invokes wasi_snapshot_preview1 poll_oneoff with subscription arguments that yield more output events than the host allocates space for",
    "2. Execute the module with iwasm / wasm_application_execute_main",
    "3. wasi_poll_oneoff calls wasmtime_ssp_poll_oneoff, which allocates a 16-byte buffer at posix.c:2186",
    "4. The event-write loop at posix.c:2253 stores 8 bytes past the end of that buffer, corrupting adjacent heap memory"
  "technical_details": "ASAN: heap-buffer-overflow, WRITE of size 8, 0 bytes to the right of a 16-byte region allocated at posix.c:2186. The output buffer sized at allocation time is too small for the number of events subsequently written at posix.c:2253, so the event-store loop runs off the end of the heap block.",
  "title": "Heap-buffer-overflow in posix.c:2253",
  "vendor_severity": "critical"
```
