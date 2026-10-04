<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-3FWTCMVC -->

# ANT-2026-3FWTCMVC · wireshark/wireshark

## heap-buffer-overflow medium

[CVE-2026-15170](https://nvd.nist.gov/vuln/detail/CVE-2026-15170)
[GHSA-hfrj-29vh-pcf2](https://github.com/advisories/GHSA-hfrj-29vh-pcf2)

Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-3FWTCMVC: Z39.50 MARC directory count floor/ceil mismatch overflow

In the Z39.50 dissector's dissect\_marc\_record(), directory\_entry\_count is computed with integer floor division and used to size a wmem\_alloc0 array, but the subsequent while loop iterates ceil() times over the same region. When the attacker-controlled leader field data\_offset makes (data\_offset-1-24) not a multiple of the fixed directory\_entry\_len (12), the loop runs one extra iteration and writes a 12-byte marc\_directory\_entry past the end of the heap allocation. The sanity check on data\_offset only emits an expert-info item and does not abort parsing. A count==0 case (e.g. data\_offset=30) additionally yields a NULL-pointer write because wmem\_alloc0(...,0) returns NULL. Both are reachable unauthenticated via a single Z39.50 response on default TCP/210 or by opening a malicious pcap.

**Project:** wireshark/wireshark
**Location:** `epan/dissectors/packet-z3950.c:12862`

Lines 12819-12822 allocate floor((data\_offset-1-24)/12) entries, but the while loop at line 12830 (`while (offset < (data_offset - 1))`) runs ceil((data\_offset-1-24)/12) times, writing marc\_directory[dir\_index].tag/length/starting\_character at lines 12904-12906 with no bounds check. data\_offset is parsed from 5 attacker-controlled ASCII digits in the MARC leader (line 12748, range 0-99999) and the range check at lines 12756-12762 is non-aborting, so e.g. data\_offset=38 allocates 1 entry but performs 2 iterations, writing 12 attacker-derived bytes into the adjacent wmem block\_fast chunk header.

1. Construct a Z39.50 response carrying an EXTERNAL with OID 1.2.840.10003.5.10 so the MARC dissector is invoked
2. In the MARC leader, set data\_offset (5 ASCII digits) such that (data\_offset - 1 - 24) % 12 != 0, e.g. data\_offset=38
3. Deliver the packet over TCP/210 to a host being captured, or embed it in a pcap the victim opens
4. dissect\_marc\_record() allocates floor(N/12) entries but loops ceil(N/12) times, writing one extra 12-byte entry past the heap buffer
5. Optionally set data\_offset so the count is 0 (e.g. 30) to trigger a NULL-pointer write via wmem\_alloc0(...,0)==NULL

## Suggested Fix

Ensure the number of iterated directory entries equals the number allocated: reject (abort dissection of) MARC records whose directory region length (data\_offset-1-MARC\_LEADER\_LENGTH) is not an exact multiple of directory\_entry\_len, and/or bound the loop by directory\_entry\_count rather than by offset.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-3FWTCMVC.

---

**Reference:** ANT-2026-3FWTCMVC

Triage and disclosure were performed by Ada Logics.

```
diff --git a/epan/dissectors/asn1/z3950/packet-z3950-template.c b/epan/dissectors/asn1/z3950/packet-z3950-template.c
index c6a11d3fd13..13160c5ebe4 100644
--- a/epan/dissectors/asn1/z3950/packet-z3950-template.c
+++ b/epan/dissectors/asn1/z3950/packet-z3950-template.c
@@ -1266,6 +1266,7 @@ dissect_marc_record(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *
     proto_tree *marc_tree, *leader_tree,
                *directory_tree,
                *fields_tree;
+    wmem_array_t *marc_directory_array;
     marc_directory_entry *marc_directory;
     unsigned len = tvb_reported_length(tvb);
     const char *marc_value_str;
@@ -1438,10 +1439,8 @@ dissect_marc_record(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *

     directory_entry_len = 3 + length_of_field_size
                             + starting_character_position_size;
-    directory_entry_count = ((data_offset - 1) - MARC_LEADER_LENGTH) / directory_entry_len;

-    marc_directory = (marc_directory_entry *)wmem_alloc0(pinfo->pool,
-                                 directory_entry_count * sizeof(marc_directory_entry));
+    marc_directory_array = wmem_array_new(pinfo->pool, sizeof(marc_directory_entry));

     directory_item = proto_tree_add_item(marc_tree, hf_marc_directory,
                          tvb, offset, data_offset - offset, ENC_NA);
@@ -1450,9 +1449,7 @@ dissect_marc_record(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *
     dir_index = 0;
     /* Minus one for the terminator character */
     while (offset < (data_offset - 1)) {
-        uint32_t tag_value = 0,
-                length_value = 0,
-                starting_char_value = 0;
+        marc_directory_entry new_entry = {0};
         proto_item *length_item;
         proto_item *directory_entry_item;
         proto_tree *directory_entry_tree;
@@ -1468,7 +1465,7 @@ dissect_marc_record(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *
         offset += 3;
         if (marc_value_str) {
             if (isdigit_string(marc_value_str)) {
-                tag_value = (unsigned)strtoul(marc_value_str, NULL, 10);
+                new_entry.tag = (unsigned)strtoul(marc_value_str, NULL, 10);
             else {
                 expert_add_info_format(pinfo, item,
@@ -1485,7 +1482,7 @@ dissect_marc_record(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *
         offset += length_of_field_size;
         if (marc_value_str) {
             if (isdigit_string(marc_value_str)) {
-                length_value = (unsigned)strtoul(marc_value_str, NULL, 10);
+                new_entry.length = (unsigned)strtoul(marc_value_str, NULL, 10);
             else {
                 expert_add_info_format(pinfo, length_item,
@@ -1501,7 +1498,7 @@ dissect_marc_record(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *
         offset += starting_character_position_size;
         if (marc_value_str) {
             if (isdigit_string(marc_value_str)) {
-                starting_char_value = (unsigned)strtoul(marc_value_str, NULL, 10);
+                new_entry.starting_character = (unsigned)strtoul(marc_value_str, NULL, 10);
             else {
                 expert_add_info_format(pinfo, item,
@@ -1511,23 +1508,24 @@ dissect_marc_record(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *

-        if (starting_char_value >= (record_length - data_offset)) {
+        if (new_entry.starting_character >= (record_length - data_offset)) {
             expert_add_info_format(pinfo, item,
                 &ei_marc_invalid_value,
                 "MARC directory entry %d starting char value %d is outside record size %d",
-                dir_index, starting_char_value, (record_length - data_offset));
+                dir_index, new_entry.starting_character, (record_length - data_offset));
-        if ((starting_char_value + length_value) >= (record_length - data_offset)) {
+        if ((new_entry.starting_character + new_entry.length) >= (record_length - data_offset)) {
             expert_add_info_format(pinfo, length_item,
                 &ei_marc_invalid_value,
                 "MARC directory entry %d length value %d goes outside record size %d",
-                dir_index, length_value, (record_length - data_offset));
+                dir_index, new_entry.length, (record_length - data_offset));
-        marc_directory[dir_index].tag = tag_value;
-        marc_directory[dir_index].length = length_value;
-        marc_directory[dir_index].starting_character = starting_char_value;
+        wmem_array_append_one(marc_directory_array, new_entry);
         dir_index++;
+    directory_entry_count = wmem_array_get_count(marc_directory_array);
+    marc_directory = (marc_directory_entry *)wmem_array_finalize(marc_directory_array);
+
     proto_tree_add_item(directory_tree, hf_marc_directory_terminator,
         tvb, offset, 1, ENC_ASCII);
     offset += 1;
diff --git a/epan/dissectors/packet-z3950.c b/epan/dissectors/packet-z3950.c
index 5c56b20dca4..0c3158ecca1 100644
--- a/epan/dissectors/packet-z3950.c
+++ b/epan/dissectors/packet-z3950.c
@@ -12638,6 +12638,7 @@ dissect_marc_record(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *
     proto_tree *marc_tree, *leader_tree,
                *directory_tree,
                *fields_tree;
+    wmem_array_t *marc_directory_array;
     marc_directory_entry *marc_directory;
     unsigned len = tvb_reported_length(tvb);
     const char *marc_value_str;
@@ -12810,10 +12811,8 @@ dissect_marc_record(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *

     directory_entry_len = 3 + length_of_field_size
                             + starting_character_position_size;
-    directory_entry_count = ((data_offset - 1) - MARC_LEADER_LENGTH) / directory_entry_len;

-    marc_directory = (marc_directory_entry *)wmem_alloc0(pinfo->pool,
-                                 directory_entry_count * sizeof(marc_directory_entry));
+    marc_directory_array = wmem_array_new(pinfo->pool, sizeof(marc_directory_entry));

     directory_item = proto_tree_add_item(marc_tree, hf_marc_directory,
                          tvb, offset, data_offset - offset, ENC_NA);
@@ -12822,9 +12821,7 @@ dissect_marc_record(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *
     dir_index = 0;
     /* Minus one for the terminator character */
     while (offset < (data_offset - 1)) {
-        uint32_t tag_value = 0,
-                length_value = 0,
-                starting_char_value = 0;
+        marc_directory_entry new_entry = {0};
         proto_item *length_item;
         proto_item *directory_entry_item;
         proto_tree *directory_entry_tree;
@@ -12840,7 +12837,7 @@ dissect_marc_record(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *
         offset += 3;
         if (marc_value_str) {
             if (isdigit_string(marc_value_str)) {
-                tag_value = (unsigned)strtoul(marc_value_str, NULL, 10);
+                new_entry.tag = (unsigned)strtoul(marc_value_str, NULL, 10);
             else {
                 expert_add_info_format(pinfo, item,
@@ -12857,7 +12854,7 @@ dissect_marc_record(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *
         offset += length_of_field_size;
         if (marc_value_str) {
             if (isdigit_string(marc_value_str)) {
-                length_value = (unsigned)strtoul(marc_value_str, NULL, 10);
+                new_entry.length = (unsigned)strtoul(marc_value_str, NULL, 10);
             else {
                 expert_add_info_format(pinfo, length_item,
@@ -12873,7 +12870,7 @@ dissect_marc_record(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *
         offset += starting_character_position_size;
         if (marc_value_str) {
             if (isdigit_string(marc_value_str)) {
-                starting_char_value = (unsigned)strtoul(marc_value_str, NULL, 10);
+                new_entry.starting_character = (unsigned)strtoul(marc_value_str, NULL, 10);
             else {
                 expert_add_info_form
… (truncated)
```

<https://github.com/wireshark/wireshark/commit/c9bd49828f4e9cd8c04f90aacb11e2238016bc31>

1. 2026-04-02
2. 2026-07-06
3. 2026-07-08
4. 2026-08-12
5. 2026-09-28

d412d9b4df5da6160175e4ae967ca471c65afc20dddacda0b5e94dc1890ad9df074ee9882366b2675d462711323835d53ecd2ba92232ec6c59c3e2e2c62e4187

Committed 2026-07-22 07:34 UTC

Revealed 2026-09-28 20:01 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-3FWTCMVC%22%2C%22bug_class%22%3A%22Heap%20Buffer%20Overflow%20/%20Integer%20Rounding%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-16T14%3A11%3A14%2B00%3A00%22%2C%22description%22%3A%22In%20the%20Z39.50%20dissector%27s%20dissect_marc_record%28%29%2C%20directory_entry_count%20is%20computed%20with%20integer%20floor%20division%20and%20used%20to%20size%20a%20wmem_alloc0%20array%2C%20but%20the%20subsequent%20while%20loop%20iterates%20ceil%28%29%20times%20over%20the%20same%20region.%20When%20the%20attacker-controlled%20leader%20field%20data_offset%20makes%20%28data_offset-1-24%29%20not%20a%20multiple%20of%20the%20fixed%20directory_entry_len%20%2812%29%2C%20the%20loop%20runs%20one%20extra%20iteration%20and%20writes%20a%2012-byte%20marc_directory_entry%20past%20the%20end%20of%20the%20heap%20allocation.%20The%20sanity%20check%20on%20data_offset%20only%20emits%20an%20expert-info%20item%20and%20does%20not%20abort%20parsing.%20A%20count%3D%3D0%20case%20%28e.g.%20data_offset%3D30%29%20additionally%20yields%20a%20NULL-pointer%20write%20because%20wmem_alloc0%28...%2C0%29%20returns%20NULL.%20Both%20are%20reachable%20unauthenticated%20via%20a%20single%20Z39.50%20response%20on%20default%20TCP/210%20or%20by%20opening%20a%20malicious%20pcap.%22%2C%22discovered_at%22%3A%222026-04-02T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22epan/dissectors/packet-z3950.c%3A12862%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22wireshark/wireshark%22%2C%22reproduction%22%3A%5B%221.%20Construct%20a%20Z39.50%20response%20carrying%20an%20EXTERNAL%20with%20OID%201.2.840.10003.5.10%20so%20the%20MARC%20dissector%20is%20invoked%22%2C%222.%20In%20the%20MARC%20leader%2C%20set%20data_offset%20%285%20ASCII%20digits%29%20such%20that%20%28data_offset%20-%201%20-%2024%29%20%25%2012%20%21%3D%200%2C%20e.g.%20data_offset%3D38%22%2C%223.%20Deliver%20the%20packet%20over%20TCP/210%20to%20a%20host%20being%20captured%2C%20or%20embed%20it%20in%20a%20pcap%20the%20victim%20opens%22%2C%224.%20dissect_marc_record%28%29%20allocates%20floor%28N/12%29%20entries%20but%20loops%20ceil%28N/12%29%20times%2C%20writing%20one%20extra%2012-byte%20entry%20past%20the%20heap%20buffer%22%2C%225.%20Optionally%20set%20data_offset%20so%20the%20count%20is%200%20%28e.g.%2030%29%20to%20trigger%20a%20NULL-pointer%20write%20via%20wmem_alloc0%28...%2C0%29%3D%3DNULL%22%5D%2C%22technical_details%22%3A%22Lines%2012819-12822%20allocate%20floor%28%28data_offset-1-24%29/12%29%20entries%2C%20but%20the%20while%20loop%20at%20line%2012830%20%28%60while%20%28offset%20%3C%20%28data_offset%20-%201%29%29%60%29%20runs%20ceil%28%28data_offset-1-24%29/12%29%20times%2C%20writing%20marc_directory%5Bdir_index%5D.tag/length/starting_character%20at%20lines%2012904-12906%20with%20no%20bounds%20check.%20data_offset%20is%20parsed%20from%205%20attacker-controlled%20ASCII%20digits%20in%20the%20MARC%20leader%20%28line%2012748%2C%20range%200-99999%29%20and%20the%20range%20check%20at%20lines%2012756-12762%20is%20non-aborting%2C%20so%20e.g.%20data_offset%3D38%20allocates%201%20entry%20but%20performs%202%20iterations%2C%20writing%2012%20attacker-derived%20bytes%20into%20the%20adjacent%20wmem%20block_fast%20chunk%20header.%22%2C%22title%22%3A%22Z39.50%20MARC%20directory%20count%20floor/ceil%20mismatch%20overflow%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-3FWTCMVC",
  "bug_class": "Heap Buffer Overflow / Integer Rounding",
  "created_at": "2026-04-16T14:11:14+00:00",
  "description": "In the Z39.50 dissector's dissect_marc_record(), directory_entry_count is computed with integer floor division and used to size a wmem_alloc0 array, but the subsequent while loop iterates ceil() times over the same region. When the attacker-controlled leader field data_offset makes (data_offset-1-24) not a multiple of the fixed directory_entry_len (12), the loop runs one extra iteration and writes a 12-byte marc_directory_entry past the end of the heap allocation. The sanity check on data_offset only emits an expert-info item and does not abort parsing. A count==0 case (e.g. data_offset=30) additionally yields a NULL-pointer write because wmem_alloc0(...,0) returns NULL. Both are reachable unauthenticated via a single Z39.50 response on default TCP/210 or by opening a malicious pcap.",
  "discovered_at": "2026-04-02T00:00:00+00:00",
  "location": "epan/dissectors/packet-z3950.c:12862",
  "project": "wireshark/wireshark",
    "1. Construct a Z39.50 response carrying an EXTERNAL with OID 1.2.840.10003.5.10 so the MARC dissector is invoked",
    "2. In the MARC leader, set data_offset (5 ASCII digits) such that (data_offset - 1 - 24) % 12 != 0, e.g. data_offset=38",
    "3. Deliver the packet over TCP/210 to a host being captured, or embed it in a pcap the victim opens",
    "4. dissect_marc_record() allocates floor(N/12) entries but loops ceil(N/12) times, writing one extra 12-byte entry past the heap buffer",
    "5. Optionally set data_offset so the count is 0 (e.g. 30) to trigger a NULL-pointer write via wmem_alloc0(...,0)==NULL"
  "technical_details": "Lines 12819-12822 allocate floor((data_offset-1-24)/12) entries, but the while loop at line 12830 (`while (offset < (data_offset - 1))`) runs ceil((data_offset-1-24)/12) times, writing marc_directory[dir_index].tag/length/starting_character at lines 12904-12906 with no bounds check. data_offset is parsed from 5 attacker-controlled ASCII digits in the MARC leader (line 12748, range 0-99999) and the range check at lines 12756-12762 is non-aborting, so e.g. data_offset=38 allocates 1 entry but performs 2 iterations, writing 12 attacker-derived bytes into the adjacent wmem block_fast chunk header.",
  "title": "Z39.50 MARC directory count floor/ceil mismatch overflow",
```
