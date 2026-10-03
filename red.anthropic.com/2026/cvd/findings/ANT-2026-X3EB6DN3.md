<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-X3EB6DN3 -->

# ANT-2026-X3EB6DN3 · libexpat/libexpat

## heap-buffer-overflow medium

[CVE-2026-56132](https://nvd.nist.gov/vuln/detail/CVE-2026-56132)
[GHSA-425r-vwq2-26qv](https://github.com/advisories/GHSA-425r-vwq2-26qv)

Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Trail of Bits.

# ANT-2026-X3EB6DN3: Heap-buffer-overflow in doProlog at xmlparse.c:5957 via deeply nested DTD with external entity interaction

The bug sits in libexpat's doProlog function in xmlparse.c, triggered when a crafted XML document combines an external entity containing a deeply nested ELEMENT content model (~32 levels) with a main DTD having even deeper nesting (~64+ levels). The external entity sub-parser reallocates m\_groupConnector based on its own nesting level, but when control returns to the main parser with deeper nesting, the bounds check at line 5906 (m\_prologState.level >= m\_groupSize) fails to account for the cross-context buffer state. An attacker controls the XML document structure and nesting depths. The result is a 4-byte write of zero past the 264-byte heap buffer, potentially corrupting adjacent heap metadata or objects for code execution or denial of service.

**Project:** libexpat/libexpat
**Location:** `xmlparse.c:5957, doProlog()`

ASAN reports a WRITE of size 4 exactly at the boundary of the 264-byte heap region allocated via expat\_realloc. The root cause is that parser->m\_groupConnector[parser->m\_prologState.level] = 0 at line 5957 writes past the buffer end because the size check at line 5906 doesn't correctly synchronize m\_groupSize between the parent parser and the external entity sub-parser — the sub-parser's reallocation doesn't propagate properly when the main parser resumes with deeper nesting.

**Crash trace (truncated — full trace in attached crash.log):**

```
INFO: found LLVMFuzzerCustomMutator (0x5f8e8389b200). Disabling -len_control by default.
INFO: Running with entropic power schedule (0xFF, 100).
INFO: Seed: 441415985
INFO: Loaded 1 modules   (9447 inline 8-bit counters): 9447 [0x5f8e83c31538, 0x5f8e83c33a1f),
INFO: Loaded 1 PC tables (9447 PCs): 9447 [0x5f8e83c33a20,0x5f8e83c58890),
/out/xml_lpm_fuzzer: Running 1 inputs 1 time(s) each.
Running: /tmp/poc
EXIT_CODE:1

=== ASAN Report ===
=================================================================
==27==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x6e7de3de1048 at pc 0x5f8e838c7592 bp 0x7ffe6d51ea30 sp 0x7ffe6d51ea28
WRITE of size 4 at 0x6e7de3de1048 thread T0
    #0 0x5f8e838c7591 in doProlog /src/expat/expat/lib/xmlparse.c:5957:42
    #1 0x5f8e838bc444 in prologProcessor /src/expat/expat/lib/xmlparse.c:5189:10
    #2 0x5f8e838bc444 in prologInitProcessor /src/expat/expat/lib/xmlparse.c:4991:10
    #3 0x5f8e838b9765 in callProcessor /src/expat/expat/lib/xmlparse.c:1293:11
    #4 0x5f8e838b9046 in XML_ParseBuffer /src/expat/expat/lib/xmlparse.c:2494:25
    #5 0x5f8e8389bed5 in Parse /src/expat/expat/fuzz/xml_lpm_fuzzer.cpp:117:28
    #6 0x5f8e8389bed5 in TestOneProtoInput /src/expat/expat/fuzz/xml_lpm_fuzzer.cpp:437:14
    #7 0x5f8e8389bed5 in LLVMFuzzerTestOneInput /src/expat/expat/fuzz/xml_lpm_fuzzer.cpp:414:1
    [... 27 more frames — full trace in crash.log]
```

1. Construct an external entity definition containing an ELEMENT content model with ~32 levels of nested parentheses
2. Construct a main document DTD with ~64+ levels of nested parentheses that references the external entity via %e;
3. Deliver the crafted XML to the target parser
4. External entity sub-parser reallocates m\_groupConnector to fit its nesting depth
5. Control returns to main parser; deeper nesting bypasses the stale size check at line 5906
6. Write at line 5957 overflows the 264-byte buffer by 4 bytes

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-X3EB6DN3.

---

**Reference:** ANT-2026-X3EB6DN3

Triage and disclosure were performed by Trail of Bits.

The change that resolved this finding.

```
diff --git a/expat/lib/xmlparse.c b/expat/lib/xmlparse.c
index 28d991b581..056c724305 100644
--- a/expat/lib/xmlparse.c
+++ b/expat/lib/xmlparse.c
@@ -424,6 +424,7 @@ typedef struct {
   unsigned scaffCount;
   int scaffLevel;
   int *scaffIndex;
+  size_t scaffIndexSize;
 } DTD;

 enum EntityType {
@@ -5920,36 +5921,18 @@ doProlog(XML_Parser parser, const ENCODING *enc, const char *s, const char *end,
     case XML_ROLE_GROUP_OPEN:
       if (parser->m_prologState.level >= parser->m_groupSize) {
         if (parser->m_groupSize) {
-          {
-            /* Detect and prevent integer overflow */
-            if (parser->m_groupSize > SIZE_MAX / 2) {
-              return XML_ERROR_NO_MEMORY;
-            }
-
-            char *const new_connector = REALLOC(
-                parser, parser->m_groupConnector, parser->m_groupSize *= 2);
-            if (new_connector == NULL) {
-              parser->m_groupSize /= 2;
-              return XML_ERROR_NO_MEMORY;
-            }
-            parser->m_groupConnector = new_connector;
+          /* Detect and prevent integer overflow */
+          if (parser->m_groupSize > SIZE_MAX / 2) {
+            return XML_ERROR_NO_MEMORY;

-          if (dtd->scaffIndex) {
-            /* Detect and prevent integer overflow. */
-            if (parser->m_groupSize > SIZE_MAX / sizeof(int)) {
-              parser->m_groupSize /= 2;
-              return XML_ERROR_NO_MEMORY;
-            }
-
-            int *const new_scaff_index = REALLOC(
-                parser, dtd->scaffIndex, parser->m_groupSize * sizeof(int));
-            if (new_scaff_index == NULL) {
-              parser->m_groupSize /= 2;
-              return XML_ERROR_NO_MEMORY;
-            }
-            dtd->scaffIndex = new_scaff_index;
+          char *const new_connector = REALLOC(parser, parser->m_groupConnector,
+                                              parser->m_groupSize *= 2);
+          if (new_connector == NULL) {
+            parser->m_groupSize /= 2;
+            return XML_ERROR_NO_MEMORY;
+          parser->m_groupConnector = new_connector;
         } else {
           parser->m_groupConnector = MALLOC(parser, parser->m_groupSize = 32);
           if (! parser->m_groupConnector) {
@@ -5964,6 +5947,21 @@ doProlog(XML_Parser parser, const ENCODING *enc, const char *s, const char *end,
         if (myindex < 0)
           return XML_ERROR_NO_MEMORY;
         assert(dtd->scaffIndex != NULL);
+        if ((size_t)dtd->scaffLevel >= dtd->scaffIndexSize) {
+          /* Detect and prevent integer overflow */
+          if (dtd->scaffIndexSize > SIZE_MAX / 2 / sizeof(int)) {
+            return XML_ERROR_NO_MEMORY;
+          }
+          assert(dtd->scaffIndexSize > 0);
+          const size_t new_size = dtd->scaffIndexSize * 2;
+          int *const new_scaff_index
+              = REALLOC(parser, dtd->scaffIndex, new_size * sizeof(int));
+          if (new_scaff_index == NULL) {
+            return XML_ERROR_NO_MEMORY;
+          }
+          dtd->scaffIndex = new_scaff_index;
+          dtd->scaffIndexSize = new_size;
+        }
         dtd->scaffIndex[dtd->scaffLevel] = myindex;
         dtd->scaffLevel++;
         dtd->scaffold[myindex].type = XML_CTYPE_SEQ;
@@ -7548,6 +7546,7 @@ dtdCreate(XML_Parser parser) {

   p->in_eldecl = XML_FALSE;
   p->scaffIndex = NULL;
+  p->scaffIndexSize = 0;
   p->scaffold = NULL;
   p->scaffLevel = 0;
   p->scaffSize = 0;
@@ -7588,6 +7587,7 @@ dtdReset(DTD *p, XML_Parser parser) {

   FREE(parser, p->scaffIndex);
   p->scaffIndex = NULL;
+  p->scaffIndexSize = 0;
   FREE(parser, p->scaffold);
   p->scaffold = NULL;

@@ -7767,6 +7767,7 @@ dtdCopy(XML_Parser oldParser, DTD *newDtd, const DTD *oldDtd,
   newDtd->scaffSize = oldDtd->scaffSize;
   newDtd->scaffLevel = oldDtd->scaffLevel;
   newDtd->scaffIndex = oldDtd->scaffIndex;
+  newDtd->scaffIndexSize = oldDtd->scaffIndexSize;

   return 1;
 } /* End dtdCopy */
@@ -8294,6 +8295,7 @@ nextScaffoldPart(XML_Parser parser) {
     dtd->scaffIndex = MALLOC(parser, parser->m_groupSize * sizeof(int));
     if (! dtd->scaffIndex)
       return -1;
+    dtd->scaffIndexSize = parser->m_groupSize;
     dtd->scaffIndex[0] = 0;

diff --git a/expat/tests/basic_tests.c b/expat/tests/basic_tests.c
index 03e6064f39..d4dd9adce1 100644
--- a/expat/tests/basic_tests.c
+++ b/expat/tests/basic_tests.c
@@ -4382,6 +4382,37 @@ START_TEST(test_skipped_external_entity) {
 END_TEST

+START_TEST(test_scaff_index_shared_across_external_entity_parser) {
+  const char text[]
+      = "<!DOCTYPE doc [\n"
+        "<!ELEMENT a "
+        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((b))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))>\n"
+        "<!ENTITY % e SYSTEM 'ext'>\n"
+        "%e;\n"
+        "<!ELEMENT c "
+        "(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((d)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))>\n"
+        "]>\n"
+        "<doc/>";
+  ExtOption options[]
+      = {{XCS("ext"),
+          "<!ELEMENT x "
+          "((((((((((((((((((((((((((((((((y))))))))))))))))))))))))))))))))>"},
+         {NULL, NULL}};
+
+  XML_Parser parser = XML_ParserCreate(NULL);
+  XML_SetParamEntityParsing(parser, XML_PARAM_ENTITY_PARSING_ALWAYS);
+  XML_SetUserData(parser, options);
+  XML_SetExternalEntityRefHandler(parser, external_entity_optioner);
+  XML_SetElementDeclHandler(parser, dummy_element_decl_handler);
+
+  if (_XML_Parse_SINGLE_BYTES(parser, text, (int)strlen(text), XML_TRUE)
+      == XML_STATUS_ERROR)
+    xml_failure(parser);
+
+  XML_ParserFree(parser);
+}
+END_TEST
+
 /* Test a different form of unknown external entity */
 START_TEST(test_skipped_null_loaded_ext_entity) {
   const char *text = "<!DOCTYPE doc SYSTEM 'http://example.org/one.ent'>\n"
@@ -6749,6 +6780,8 @@ make_basic_test_case(Suite *s) {
   tcase_add_test(tc_basic, test_trailing_cr_in_att_value);
   tcase_add_test(tc_basic, test_standalone_internal_entity);
   tcase_add_test(tc_basic, test_skipped_external_entity);
+  tcase_add_test__ifdef_xml_dtd(
+      tc_basic, test_scaff_index_shared_across_external_entity_parser);
   tcase_add_test(tc_basic, test_skipped_null_loaded_ext_entity);
   tcase_add_test(tc_basic, test_skipped_unloaded_ext_entity);
   tcase_add_test__ifdef_xml_dtd(tc_basic, test_param_entity_with_trailing_cr);
```

<https://github.com/libexpat/libexpat/commit/db1a48091b40f6892e622a282eba20752e6860ad>

ADVISORY

<https://github.com/libexpat/libexpat/pull/1272>

1. 2026-03-20
2. 2026-05-21
3. 2026-05-28
4. 2026-06-20
5. 2026-08-17

bdf77e15fd29d60ffc0dcf00fd4d2b1f0bc1d862c694e8e5914a35f23e54ce99c7998642f61aa543090450bc1a91ce59ed8130f7b012838ec15bfec160129a02

Committed 2026-05-28 15:14 UTC

Revealed 2026-08-17 17:47 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-X3EB6DN3%22%2C%22bug_class%22%3A%22heap-buffer-overflow%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-20T19%3A13%3A12%2B00%3A00%22%2C%22description%22%3A%22The%20bug%20sits%20in%20libexpat%27s%20doProlog%20function%20in%20xmlparse.c%2C%20triggered%20when%20a%20crafted%20XML%20document%20combines%20an%20external%20entity%20containing%20a%20deeply%20nested%20ELEMENT%20content%20model%20%28~32%20levels%29%20with%20a%20main%20DTD%20having%20even%20deeper%20nesting%20%28~64%2B%20levels%29.%20The%20external%20entity%20sub-parser%20reallocates%20m_groupConnector%20based%20on%20its%20own%20nesting%20level%2C%20but%20when%20control%20returns%20to%20the%20main%20parser%20with%20deeper%20nesting%2C%20the%20bounds%20check%20at%20line%205906%20%28m_prologState.level%20%3E%3D%20m_groupSize%29%20fails%20to%20account%20for%20the%20cross-context%20buffer%20state.%20An%20attacker%20controls%20the%20XML%20document%20structure%20and%20nesting%20depths.%20The%20result%20is%20a%204-byte%20write%20of%20zero%20past%20the%20264-byte%20heap%20buffer%2C%20potentially%20corrupting%20adjacent%20heap%20metadata%20or%20objects%20for%20code%20execution%20or%20denial%20of%20service.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3A%22xmlparse.c%3A5957%2C%20doProlog%28%29%22%2C%22poc_sha256%22%3A%22351f79465c6d5b8827d4581c30d24cd52b65dcbcff71cbdb8559372a9ccd7c46%22%2C%22preimage_version%22%3A1%2C%22project%22%3A%22expat%22%2C%22reproduction%22%3A%5B%22Construct%20an%20external%20entity%20definition%20containing%20an%20ELEMENT%20content%20model%20with%20~32%20levels%20of%20nested%20parentheses%22%2C%22Construct%20a%20main%20document%20DTD%20with%20~64%2B%20levels%20of%20nested%20parentheses%20that%20references%20the%20external%20entity%20via%20%25e%3B%22%2C%22Deliver%20the%20crafted%20XML%20to%20the%20target%20parser%22%2C%22External%20entity%20sub-parser%20reallocates%20m_groupConnector%20to%20fit%20its%20nesting%20depth%22%2C%22Control%20returns%20to%20main%20parser%3B%20deeper%20nesting%20bypasses%20the%20stale%20size%20check%20at%20line%205906%22%2C%22Write%20at%20line%205957%20overflows%20the%20264-byte%20buffer%20by%204%20bytes%22%5D%2C%22technical_details%22%3A%22ASAN%20reports%20a%20WRITE%20of%20size%204%20exactly%20at%20the%20boundary%20of%20the%20264-byte%20heap%20region%20allocated%20via%20expat_realloc.%20The%20root%20cause%20is%20that%20parser-%3Em_groupConnector%5Bparser-%3Em_prologState.level%5D%20%3D%200%20at%20line%205957%20writes%20past%20the%20buffer%20end%20because%20the%20size%20check%20at%20line%205906%20doesn%27t%20correctly%20synchronize%20m_groupSize%20between%20the%20parent%20parser%20and%20the%20external%20entity%20sub-parser%20%E2%80%94%20the%20sub-parser%27s%20reallocation%20doesn%27t%20propagate%20properly%20when%20the%20main%20parser%20resumes%20with%20deeper%20nesting.%22%2C%22title%22%3A%22Heap-buffer-overflow%20in%20doProlog%20at%20xmlparse.c%3A5957%20via%20deeply%20nested%20DTD%20with%20external%20entity%20interaction%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-X3EB6DN3",
  "bug_class": "heap-buffer-overflow",
  "created_at": "2026-03-20T19:13:12+00:00",
  "description": "The bug sits in libexpat's doProlog function in xmlparse.c, triggered when a crafted XML document combines an external entity containing a deeply nested ELEMENT content model (~32 levels) with a main DTD having even deeper nesting (~64+ levels). The external entity sub-parser reallocates m_groupConnector based on its own nesting level, but when control returns to the main parser with deeper nesting, the bounds check at line 5906 (m_prologState.level >= m_groupSize) fails to account for the cross-context buffer state. An attacker controls the XML document structure and nesting depths. The result is a 4-byte write of zero past the 264-byte heap buffer, potentially corrupting adjacent heap metadata or objects for code execution or denial of service.",
  "location": "xmlparse.c:5957, doProlog()",
  "poc_sha256": "351f79465c6d5b8827d4581c30d24cd52b65dcbcff71cbdb8559372a9ccd7c46",
  "project": "expat",
    "Construct an external entity definition containing an ELEMENT content model with ~32 levels of nested parentheses",
    "Construct a main document DTD with ~64+ levels of nested parentheses that references the external entity via %e;",
    "Deliver the crafted XML to the target parser",
    "External entity sub-parser reallocates m_groupConnector to fit its nesting depth",
    "Control returns to main parser; deeper nesting bypasses the stale size check at line 5906",
    "Write at line 5957 overflows the 264-byte buffer by 4 bytes"
  "technical_details": "ASAN reports a WRITE of size 4 exactly at the boundary of the 264-byte heap region allocated via expat_realloc. The root cause is that parser->m_groupConnector[parser->m_prologState.level] = 0 at line 5957 writes past the buffer end because the size check at line 5906 doesn't correctly synchronize m_groupSize between the parent parser and the external entity sub-parser — the sub-parser's reallocation doesn't propagate properly when the main parser resumes with deeper nesting.",
  "title": "Heap-buffer-overflow in doProlog at xmlparse.c:5957 via deeply nested DTD with external entity interaction",
```
