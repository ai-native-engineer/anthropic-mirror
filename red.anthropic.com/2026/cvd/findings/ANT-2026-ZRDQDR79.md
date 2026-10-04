<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-ZRDQDR79 -->

# ANT-2026-ZRDQDR79 · util-linux/util-linux

## use-after-free medium

[CVE-2026-13595](https://nvd.nist.gov/vuln/detail/CVE-2026-13595)
[GHSA-qpmf-9p9c-455w](https://github.com/advisories/GHSA-qpmf-9p9c-455w)

Claude critical
Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Calif.

# ANT-2026-ZRDQDR79: Heap-use-after-free in blkid\_partition\_get\_start at partitions.c:1447 via nested BSD disklabel in DOS partition table

A heap-use-after-free (READ) was detected in util-linux's libblkid library through the OSS-Fuzz test-blkid-fuzz harness. libblkid handles probing of block device content types (filesystem superblocks, partition tables) and is invoked by blkid, udev, and automount infrastructure. An attacker who can present a crafted block device image to the system — via USB insertion, virtual disk attachment, or placing a disk image where automounting will scan it — can trigger the read of freed memory during probing. The READ-type UAF most likely yields information disclosure or denial of service, with code execution possible but harder given heap layout dependencies.

**Project:** util-linux/util-linux
**Location:** `blkid_partition_get_start() at libblkid/src/partitions/partitions.c:1447`

ASAN reports a READ-type heap-use-after-free during libblkid's probing of a crafted input, indicating internal probing data structures are freed and then accessed again. No specific ASAN size/address line or stack frames were provided in the report; the root-cause function and exact freed object are not identified. ASAN READ heap-UAF detections are highly reliable with near-zero false-positive rates due to precise allocator instrumentation.

**Crash trace (truncated — full trace in attached crash.log):**

```
INFO: Running with entropic power schedule (0xFF, 100).
INFO: Seed: 2157158283
INFO: Loaded 1 modules   (9192 inline 8-bit counters): 9192 [0x568d75257fc8, 0x568d7525a3b0),
INFO: Loaded 1 PC tables (9192 PCs): 9192 [0x568d7525a3b0,0x568d7527e230),
/out/test_blkid_fuzz: Running 1 inputs 1 time(s) each.
Running: /tmp/poc
EXIT_CODE:1

=== ASAN Report ===
=================================================================
==27==ERROR: AddressSanitizer: heap-use-after-free on address 0x75a1663e0200 at pc 0x568d75141f54 bp 0x7fff11ca9940 sp 0x7fff11ca9938
READ of size 8 at 0x75a1663e0200 thread T0
    #0 0x568d75141f53 in blkid_partition_get_start /src/util-linux/libblkid/src/partitions/partitions.c:1447:28
    #1 0x568d7517ea47 in probe_bsd_pt /src/util-linux/libblkid/src/partitions/bsd.c:132:17
    #2 0x568d751428a7 in idinfo_probe /src/util-linux/libblkid/src/partitions/partitions.c:560:8
    #3 0x568d751422f8 in blkid_partitions_do_subprobe /src/util-linux/libblkid/src/partitions/partitions.c:719:7
    #4 0x568d75180320 in probe_dos_pt /src/util-linux/libblkid/src/partitions/dos.c:342:10
    #5 0x568d751428a7 in idinfo_probe /src/util-linux/libblkid/src/partitions/partitions.c:560:8
    #6 0x568d751403a6 in partitions_probe /src/util-linux/libblkid/src/partitions/partitions.c:620:8
    #7 0x568d7512ff22 in blkid_probe_get_binary_data /src/util-linux/libblkid/src/probe.c:391:7
    [... 60 more frames — full trace in crash.log]
```

1. Craft a malicious filesystem/partition image that triggers the UAF code path in libblkid probing
2. Present the image to the target: insert USB storage, attach a virtual disk, or place the image where automount infrastructure scans it
3. libblkid (invoked by blkid/udev/udisks, typically as root) probes the device and reads freed heap memory
4. Result: crash (DoS), potential information disclosure, or — with favorable heap layout and chaining — possible escalation

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-ZRDQDR79.

---

**Reference:** ANT-2026-ZRDQDR79

Triage and disclosure were performed by Calif.

```
diff --git a/libblkid/src/partitions/partitions.c b/libblkid/src/partitions/partitions.c
index f95fe898f33..a428c6d6c16 100644
--- a/libblkid/src/partitions/partitions.c
+++ b/libblkid/src/partitions/partitions.c
@@ -199,7 +199,7 @@ struct blkid_struct_partlist {

 	int		nparts;		/* number of partitions */
 	int		nparts_max;	/* max.number of partitions */
-	blkid_partition	parts;		/* array of partitions */
+	blkid_partition	*parts;		/* array of pointers to partitions */

 	struct list_head l_tabs;	/* list of partition tables */
 };
@@ -358,13 +358,16 @@ static void reset_partlist(blkid_partlist ls)
 	free_parttables(ls);

 	if (ls->next_partno) {
-		/* already initialized - reset */
-		int tmp_nparts = ls->nparts_max;
-		blkid_partition tmp_parts = ls->parts;
+		/* already initialized - free individually allocated partitions */
+		int i, tmp_nparts_max = ls->nparts_max;
+		blkid_partition *tmp_parts = ls->parts;
+
+		for (i = 0; i < ls->nparts; i++)
+			free(ls->parts[i]);

 		memset(ls, 0, sizeof(struct blkid_struct_partlist));

-		ls->nparts_max = tmp_nparts;
+		ls->nparts_max = tmp_nparts_max;
 		ls->parts = tmp_parts;

@@ -399,6 +402,7 @@ static void partitions_free_data(blkid_probe pr __attribute__((__unused__)),
 				 void *data)
 	blkid_partlist ls = (blkid_partlist) data;
+	int i;

 	if (!ls)
 		return;
@@ -406,6 +410,8 @@ static void partitions_free_data(blkid_probe pr __attribute__((__unused__)),
 	free_parttables(ls);

 	/* deallocate partitions and partlist */
+	for (i = 0; i < ls->nparts; i++)
+		free(ls->parts[i]);
 	free(ls->parts);
 	free(ls);
@@ -439,15 +445,17 @@ static blkid_partition new_partition(blkid_partlist ls, blkid_parttable tab)
 		 * generic Linux machine -- let's start with 32 partitions.
 		 */
 		void *tmp = reallocarray(ls->parts, ls->nparts_max + 32,
-					 sizeof(struct blkid_struct_partition));
+					 sizeof(blkid_partition));
 		if (!tmp)
 			return NULL;
 		ls->parts = tmp;
 		ls->nparts_max += 32;

-	par = &ls->parts[ls->nparts++];
-	memset(par, 0, sizeof(struct blkid_struct_partition));
+	par = calloc(1, sizeof(struct blkid_struct_partition));
+	if (!par)
+		return NULL;
+	ls->parts[ls->nparts++] = par;

 	ref_parttable(tab);
 	par->tab = tab;
@@ -852,7 +860,7 @@ int blkid_probe_is_covered_by_pt(blkid_probe pr,

 	/* check if the partition table fits into the device */
 	for (i = 0; i < nparts; i++) {
-		blkid_partition par = &ls->parts[i];
+		blkid_partition par = ls->parts[i];

 		if (par->start + par->size > (pr->size >> 9)) {
 			DBG(LOWPROBE, ul_debug("partition #%d overflows "
@@ -864,7 +872,7 @@ int blkid_probe_is_covered_by_pt(blkid_probe pr,

 	/* check if the requested area is covered by PT */
 	for (i = 0; i < nparts; i++) {
-		blkid_partition par = &ls->parts[i];
+		blkid_partition par = ls->parts[i];

 		if (start >= par->start && end <= par->start + par->size) {
 			rc = 1;
@@ -963,7 +971,7 @@ blkid_partition blkid_partlist_get_partition(blkid_partlist ls, int n)
 	if (n < 0 || n >= ls->nparts)
 		return NULL;

-	return &ls->parts[n];
+	return ls->parts[n];

 blkid_partition blkid_partlist_get_partition_by_start(blkid_partlist ls, uint64_t start)
@@ -1075,7 +1083,7 @@ blkid_partition blkid_partlist_devno_to_partition(blkid_partlist ls, dev_t devno
 		 * and an entry in partition table.
 		 */
 		 for (i = 0; i < ls->nparts; i++) {
-			 blkid_partition par = &ls->parts[i];
+			 blkid_partition par = ls->parts[i];

 			 if (partno != blkid_partition_get_partno(par))
 				 continue;
@@ -1091,7 +1099,7 @@ blkid_partition blkid_partlist_devno_to_partition(blkid_partlist ls, dev_t devno
 	DBG(LOWPROBE, ul_debug("searching by offset/size"));

 	for (i = 0; i < ls->nparts; i++) {
-		blkid_partition par = &ls->parts[i];
+		blkid_partition par = ls->parts[i];

 		if ((uint64_t)blkid_partition_get_start(par) == start &&
 		    (uint64_t)blkid_partition_get_size(par) == size)
```

<https://github.com/util-linux/util-linux/commit/c0186f14fbdb02f64c8e0ba701ce727ea764ff4c>

ADVISORY

<https://github.com/util-linux/util-linux/commit/c0186f14fbdb02f64c8e0ba701ce727ea764ff4c>

1. 2026-03-20
2. 2026-05-08
3. 2026-05-09
4. 2026-06-16
5. 2026-08-17

b322f519496ca8294ecf2a7fb53c3196ba0c9377d8c9ea3292509a123e5a32feecfbb9abdf3d4a533628cf09218b84e43bf768ae3dd331c5fbcb96e4aecf000b

Committed 2026-05-08 07:11 UTC

Revealed 2026-08-17 17:47 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-ZRDQDR79%22%2C%22bug_class%22%3A%22heap-use-after-free%22%2C%22claude_severity%22%3A%22critical%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-20T19%3A13%3A36%2B00%3A00%22%2C%22description%22%3A%22A%20heap-use-after-free%20%28READ%29%20was%20detected%20in%20util-linux%27s%20libblkid%20library%20through%20the%20OSS-Fuzz%20test-blkid-fuzz%20harness.%20libblkid%20handles%20probing%20of%20block%20device%20content%20types%20%28filesystem%20superblocks%2C%20partition%20tables%29%20and%20is%20invoked%20by%20blkid%2C%20udev%2C%20and%20automount%20infrastructure.%20An%20attacker%20who%20can%20present%20a%20crafted%20block%20device%20image%20to%20the%20system%20%E2%80%94%20via%20USB%20insertion%2C%20virtual%20disk%20attachment%2C%20or%20placing%20a%20disk%20image%20where%20automounting%20will%20scan%20it%20%E2%80%94%20can%20trigger%20the%20read%20of%20freed%20memory%20during%20probing.%20The%20READ-type%20UAF%20most%20likely%20yields%20information%20disclosure%20or%20denial%20of%20service%2C%20with%20code%20execution%20possible%20but%20harder%20given%20heap%20layout%20dependencies.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3A%22blkid_partition_get_start%28%29%20at%20libblkid/src/partitions/partitions.c%3A1447%22%2C%22poc_sha256%22%3A%22f013a9bb91af93bb8e505dad1e48b271ddade3e924c1192cc8c6cb49dc7d93d9%22%2C%22preimage_version%22%3A1%2C%22project%22%3A%22util-linux%22%2C%22reproduction%22%3A%5B%22Craft%20a%20malicious%20filesystem/partition%20image%20that%20triggers%20the%20UAF%20code%20path%20in%20libblkid%20probing%22%2C%22Present%20the%20image%20to%20the%20target%3A%20insert%20USB%20storage%2C%20attach%20a%20virtual%20disk%2C%20or%20place%20the%20image%20where%20automount%20infrastructure%20scans%20it%22%2C%22libblkid%20%28invoked%20by%20blkid/udev/udisks%2C%20typically%20as%20root%29%20probes%20the%20device%20and%20reads%20freed%20heap%20memory%22%2C%22Result%3A%20crash%20%28DoS%29%2C%20potential%20information%20disclosure%2C%20or%20%E2%80%94%20with%20favorable%20heap%20layout%20and%20chaining%20%E2%80%94%20possible%20escalation%22%5D%2C%22technical_details%22%3A%22ASAN%20reports%20a%20READ-type%20heap-use-after-free%20during%20libblkid%27s%20probing%20of%20a%20crafted%20input%2C%20indicating%20internal%20probing%20data%20structures%20are%20freed%20and%20then%20accessed%20again.%20No%20specific%20ASAN%20size/address%20line%20or%20stack%20frames%20were%20provided%20in%20the%20report%3B%20the%20root-cause%20function%20and%20exact%20freed%20object%20are%20not%20identified.%20ASAN%20READ%20heap-UAF%20detections%20are%20highly%20reliable%20with%20near-zero%20false-positive%20rates%20due%20to%20precise%20allocator%20instrumentation.%22%2C%22title%22%3A%22Heap-use-after-free%20in%20blkid_partition_get_start%20at%20partitions.c%3A1447%20via%20nested%20BSD%20disklabel%20in%20DOS%20partition%20table%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-ZRDQDR79",
  "bug_class": "heap-use-after-free",
  "claude_severity": "critical",
  "created_at": "2026-03-20T19:13:36+00:00",
  "description": "A heap-use-after-free (READ) was detected in util-linux's libblkid library through the OSS-Fuzz test-blkid-fuzz harness. libblkid handles probing of block device content types (filesystem superblocks, partition tables) and is invoked by blkid, udev, and automount infrastructure. An attacker who can present a crafted block device image to the system — via USB insertion, virtual disk attachment, or placing a disk image where automounting will scan it — can trigger the read of freed memory during probing. The READ-type UAF most likely yields information disclosure or denial of service, with code execution possible but harder given heap layout dependencies.",
  "location": "blkid_partition_get_start() at libblkid/src/partitions/partitions.c:1447",
  "poc_sha256": "f013a9bb91af93bb8e505dad1e48b271ddade3e924c1192cc8c6cb49dc7d93d9",
  "project": "util-linux",
    "Craft a malicious filesystem/partition image that triggers the UAF code path in libblkid probing",
    "Present the image to the target: insert USB storage, attach a virtual disk, or place the image where automount infrastructure scans it",
    "libblkid (invoked by blkid/udev/udisks, typically as root) probes the device and reads freed heap memory",
    "Result: crash (DoS), potential information disclosure, or — with favorable heap layout and chaining — possible escalation"
  "technical_details": "ASAN reports a READ-type heap-use-after-free during libblkid's probing of a crafted input, indicating internal probing data structures are freed and then accessed again. No specific ASAN size/address line or stack frames were provided in the report; the root-cause function and exact freed object are not identified. ASAN READ heap-UAF detections are highly reliable with near-zero false-positive rates due to precise allocator instrumentation.",
  "title": "Heap-use-after-free in blkid_partition_get_start at partitions.c:1447 via nested BSD disklabel in DOS partition table",
```
