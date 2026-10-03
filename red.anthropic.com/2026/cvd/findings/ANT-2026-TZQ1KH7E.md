<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-TZQ1KH7E -->

# ANT-2026-TZQ1KH7E · cesnet/libyang

## use-after-free medium

[CVE-2026-41401](https://nvd.nist.gov/vuln/detail/CVE-2026-41401)
[GHSA-9f49-8x56-jmjc](https://github.com/CESNET/libyang/security/advisories/GHSA-9f49-8x56-jmjc)
[GHSA-v7jp-vmx6-5429](https://github.com/advisories/GHSA-v7jp-vmx6-5429)

Claude medium
Security research firm medium
Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Trail of Bits.

# ANT-2026-TZQ1KH7E: Heap use-after-free write in metadata list management during XML data parsing due to incorrect list head pointer update

A heap use-after-free write occurs in metadata list management during XML data parsing due to an incorrect update of the list head pointer.

**Project:** cesnet/libyang

During XML data parsing, the code managing the metadata linked list updates the list head pointer incorrectly, leaving a reference to freed heap memory that is subsequently written to.

This finding was identified by static analysis and has not yet been dynamically reproduced. The Technical Details section above describes the code path; a trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-TZQ1KH7E.

---

**Reference:** ANT-2026-TZQ1KH7E

Triage and disclosure were performed by Trail of Bits. The writeup below is the document the firm sent to the maintainer.

:   medium

### Summary

A heap use-after-free write in libyang’s XML data parser can be triggered by a crafted YANG XML document with specific metadata attributes, leading to memory corruption (process crash, and potentially code execution in some deployments).

In `lyd_parser_set_data_flags` at `src/parser_common.c:316-319`, the metadata list head pointer is incorrectly updated when freeing a non-head "default" metadata entry.

Validated against: https://github.com/CESNET/libyang @ 6b5ed47ee674fbe86b31bbebc4ff26889aeff38c (devel)

### Details and PoC

Build fuzzers:

```
  git clone https://github.com/google/oss-fuzz.git
  cd oss-fuzz
  python3 infra/helper.py build_fuzzers --sanitizer address libyang
```

Run the PoC: `python3 infra/helper.py reproduce libyang lyd_parse_mem_xml poc.bin`

Expected output: ASAN reports heap-use-after-free WRITE in lyd\_insert\_meta at tree\_data.c:1313.

**We have attached a zip containing:**

* Full technical details of each finding
* Reproduction steps and proof-of-concept where applicable
* Candidate patch(es) with regression tests

### Impact

Any application using libyang to parse attacker-controlled (or semi-trusted) XML-encoded YANG instance data (NETCONF/RESTCONF, config import, etc.) is impacted. That can lead to denial of service issues. Depending on allocator behavior and application heap layout, memory corruption could potentially be leveraged further.

### Bug discovery context

Anthropic is conducting research into the use of large language models for automated vulnerability discovery in open source software. As part of that work, Anthropic used Claude to scan a set of widely used open source projects for security issues. Anthropic then engaged Trail of Bits to independently triage, manually validate, and develop patches for the findings. Each issue in this report has been reviewed and confirmed by human security researchers at Trail of Bits.

Thank you for your work on libyang!

The change that resolved this finding.

```
diff --git a/src/parser_common.c b/src/parser_common.c
index 39fb4ab0a..f11fce560 100644
--- a/src/parser_common.c
+++ b/src/parser_common.c
@@ -313,8 +313,8 @@ lyd_parser_set_data_flags(struct lyd_node *node, struct lyd_meta **meta, struct
             next_meta = meta2->next;

             /* delete the metadata */
-            if (meta != &node->meta) {
-                *meta = (*meta)->next;
+            if ((meta != &node->meta) && (meta2 == *meta)) {
+                *meta = next_meta;
             lyd_free_meta_single(meta2);
             if (prev_meta) {
diff --git a/tests/fuzz/corpus/lyd_parse_mem_xml/advisory2026_03_26 b/tests/fuzz/corpus/lyd_parse_mem_xml/advisory2026_03_26
new file mode 100644
index 000000000..7e3b6c39e
--- /dev/null
+++ b/tests/fuzz/corpus/lyd_parse_mem_xml/advisory2026_03_26
@@ -0,0 +1,5 @@
+<int32 xmlns="urn:tests:types"
+       xmlns:yang="urn:ietf:params:xml:ns:yang:1"
+       xmlns:dflt="urn:ietf:params:xml:ns:netconf:default:1.0"
+       yang:operation="create"
+       dflt:default="true">5</int32>
```

<https://github.com/CESNET/libyang/commit/54c3276d871023da266d4ed3ceaee7e8d71d0b04>

1. 2026-03-26
2. 2026-03-26
3. 2026-03-29
4. 2026-05-09
5. 2026-05-20

e0d7ff03175cfb6f262ec1ce13576b26ab2125bf68ff4ba73e0038c768ad2a44514bb277f85c8737968bf040c411a277752967b60dfd39ae451244fd83ed6ad4

Committed 2026-05-07 07:01 UTC

Revealed 2026-05-20 07:40 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-TZQ1KH7E%22%2C%22bug_class%22%3A%22Use-After-Free%22%2C%22claude_severity%22%3A%22medium%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A43%3A15%2B00%3A00%22%2C%22description%22%3A%22A%20heap%20use-after-free%20write%20occurs%20in%20metadata%20list%20management%20during%20XML%20data%20parsing%20due%20to%20an%20incorrect%20update%20of%20the%20list%20head%20pointer.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22libyang%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3A%22During%20XML%20data%20parsing%2C%20the%20code%20managing%20the%20metadata%20linked%20list%20updates%20the%20list%20head%20pointer%20incorrectly%2C%20leaving%20a%20reference%20to%20freed%20heap%20memory%20that%20is%20subsequently%20written%20to.%22%2C%22title%22%3A%22Heap%20use-after-free%20write%20in%20metadata%20list%20management%20during%20XML%20data%20parsing%20due%20to%20incorrect%20list%20head%20pointer%20update%22%2C%22vendor_severity%22%3A%22medium%22%7D)

```
  "ant_id": "ANT-2026-TZQ1KH7E",
  "bug_class": "Use-After-Free",
  "claude_severity": "medium",
  "created_at": "2026-03-29T20:43:15+00:00",
  "description": "A heap use-after-free write occurs in metadata list management during XML data parsing due to an incorrect update of the list head pointer.",
  "project": "libyang",
  "technical_details": "During XML data parsing, the code managing the metadata linked list updates the list head pointer incorrectly, leaving a reference to freed heap memory that is subsequently written to.",
  "title": "Heap use-after-free write in metadata list management during XML data parsing due to incorrect list head pointer update",
  "vendor_severity": "medium"
```
