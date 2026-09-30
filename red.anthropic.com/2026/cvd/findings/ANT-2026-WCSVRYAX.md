<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-WCSVRYAX -->

# ANT-2026-WCSVRYAX · oisf/suricata

## use-after-free high

[GHSA-59q6-j4w8-8pjx](https://github.com/advisories/GHSA-59q6-j4w8-8pjx)

Claude critical
Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Trail of Bits.

# ANT-2026-WCSVRYAX: heap-use-after-free in suricata

A heap-use-after-free was detected in Suricata while fuzzing through the fuzz\_sigpcap\_aware7 harness. The faulting access is a READ of freed heap memory. The sigpcap\_aware harness drives combined signature rules and pcap traffic through the detection engine, so the bug is likely reachable via a crafted rule set paired with crafted packet capture input.

**Project:** suricata
**Commit:** `7eb45c02afbaf2ad`

AddressSanitizer heap-use-after-free (READ) in Suricata triggered via the fuzz\_sigpcap\_aware7 fuzzing entrypoint.

**Crash signature:** `ASAN heap-use-after-free READ`

Reproduce against the commit listed above as described under Technical Details.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-WCSVRYAX.

---

**Reference:** ANT-2026-WCSVRYAX

Triage and disclosure were performed by Trail of Bits.

UPSTREAM FIX

The change that resolved this finding.

```
diff --git a/rust/src/detect/transforms/dotprefix.rs b/rust/src/detect/transforms/dotprefix.rs
index 2b52462fba1a..b6f973835671 100644
--- a/rust/src/detect/transforms/dotprefix.rs
+++ b/rust/src/detect/transforms/dotprefix.rs
@@ -18,8 +18,8 @@
 use crate::detect::SIGMATCH_NOOPT;
 use suricata_sys::sys::{
     DetectEngineCtx, DetectEngineThreadCtx, InspectionBuffer, SCDetectHelperTransformRegister,
-    SCDetectSignatureAddTransform, SCTransformTableElmt, Signature, SCInspectionBufferCheckAndExpand,
-    SCInspectionBufferTruncate,
+    SCDetectSignatureAddTransform, SCInspectionBufferCheckAndExpand, SCInspectionBufferInPlace,
+    SCInspectionBufferTruncate, SCTransformTableElmt, Signature,
 };

 use std::os::raw::{c_int, c_void};
@@ -49,17 +49,19 @@ unsafe extern "C" fn dot_prefix_transform(
     if input_len == 0 {
         return;
+    let inplace = SCInspectionBufferInPlace(buffer);
+
     let output = SCInspectionBufferCheckAndExpand(buffer, input_len + 1);
     if output.is_null() {
         // allocation failure
         return;
-    // get input after possible realloc
-    let input = (*buffer).inspect;
-    if input.is_null() {
-        // allocation failure
-        return;
-    }
+    let input = if inplace {
+        // may have been reallocated
+        (*buffer).buf
+    } else {
+        (*buffer).inspect
+    };
     let input = build_slice!(input, input_len as usize);
     let output = std::slice::from_raw_parts_mut(output, (input_len + 1) as usize);
```

<https://github.com/OISF/suricata/commit/6d437956e2ed2da75976d7635cbe09a953d3c489>

1. 2026-03-26
2. 2026-04-29
3. 2026-05-09
4. 2026-05-17

b21d5c53bcd9424f1c836f2ca4da99b974bbc8e0df5a3ef201cb2cc4f734880595b27a54ff544e55a50dc1268af982b35e83fea10a760091735bb9d8ffc4b5c8

Committed 2026-04-29 00:04 PT

Revealed 2026-08-17 10:47 PT

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-WCSVRYAX%22%2C%22bug_class%22%3A%22heap-use-after-free%22%2C%22claude_severity%22%3A%22critical%22%2C%22commit_sha%22%3A%227eb45c02afbaf2ad%22%2C%22created_at%22%3A%222026-03-27T02%3A07%3A51%2B00%3A00%22%2C%22description%22%3A%22A%20heap-use-after-free%20was%20detected%20in%20Suricata%20while%20fuzzing%20through%20the%20fuzz_sigpcap_aware7%20harness.%20The%20faulting%20access%20is%20a%20READ%20of%20freed%20heap%20memory.%20The%20sigpcap_aware%20harness%20drives%20combined%20signature%20rules%20and%20pcap%20traffic%20through%20the%20detection%20engine%2C%20so%20the%20bug%20is%20likely%20reachable%20via%20a%20crafted%20rule%20set%20paired%20with%20crafted%20packet%20capture%20input.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22suricata%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3Anull%2C%22title%22%3A%22heap-use-after-free%20in%20suricata%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-WCSVRYAX",
  "bug_class": "heap-use-after-free",
  "claude_severity": "critical",
  "commit_sha": "7eb45c02afbaf2ad",
  "created_at": "2026-03-27T02:07:51+00:00",
  "description": "A heap-use-after-free was detected in Suricata while fuzzing through the fuzz_sigpcap_aware7 harness. The faulting access is a READ of freed heap memory. The sigpcap_aware harness drives combined signature rules and pcap traffic through the detection engine, so the bug is likely reachable via a crafted rule set paired with crafted packet capture input.",
  "project": "suricata",
  "technical_details": null,
  "title": "heap-use-after-free in suricata",
```
