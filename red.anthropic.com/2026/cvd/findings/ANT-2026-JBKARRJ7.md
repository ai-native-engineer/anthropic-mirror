<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-JBKARRJ7 -->

# ANT-2026-JBKARRJ7 · libvips/libvips

## oob-write low

[CVE-2026-35590](https://nvd.nist.gov/vuln/detail/CVE-2026-35590)
[GHSA-jmwm-wc68-mhwm](https://github.com/libvips/libvips/security/advisories/GHSA-jmwm-wc68-mhwm)

Claude low
Security research firm low
Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Trail of Bits.

# ANT-2026-JBKARRJ7: Out-of-bounds IFD array access in EXIF metadata processing leading to write through corrupted pointer

An out-of-bounds index into the IFD array during EXIF parsing produces a corrupted pointer that is then used as a write target.

**Project:** libvips/libvips

This finding was identified by static analysis and has not yet been dynamically reproduced. A trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-JBKARRJ7.

---

**Reference:** ANT-2026-JBKARRJ7

Triage and disclosure were performed by Trail of Bits.

:   low

```
diff --git a/ChangeLog b/ChangeLog
index bc3e3ace80..5ea68a830d 100644
--- a/ChangeLog
+++ b/ChangeLog
@@ -1,6 +1,7 @@
 date-tbd 8.18.2

 - convolution: avoid using unsigned accumulators [nakrovati]
+- exif: check ifdN range [trailofbits]
 - tiffload: check jpeg and jp2k components [wooseokdotkim]
 - uhdrsave: set Q for gainmap recompress, don't chroma subsample RGB gainmaps
 - uhdrsave: prevent early unref of image with alpha channel [lovell]
diff --git a/libvips/foreign/exif.c b/libvips/foreign/exif.c
index b98e8cfd06..db4395b5e0 100644
--- a/libvips/foreign/exif.c
+++ b/libvips/foreign/exif.c
@@ -1284,6 +1284,11 @@ vips_exif_image_field(VipsImage *image,

 	p = field + strlen("exif-ifd");
 	ifd = atoi(p);
+	if (ifd < 0 ||
+		ifd >= EXIF_IFD_COUNT) {
+		g_warning("bad exif ifd %d in \"%s\"", ifd, field);
+		return NULL;
+	}

 	for (; g_ascii_isdigit(*p); p++)
 		;
```

<https://github.com/libvips/libvips/commit/91ebd4d35341a8353ea490392d556d582e4b846f>

1. 2026-03-26
2. 2026-03-29
3. 2026-03-31
4. 2026-05-09
5. 2026-08-17

3d086296fdc3ee597627329b2198c6f0a171f3bd2c5912fead06195a09493bc3afd1314179768a43ecdd28a66f5fc9a18544fc24276ed804afd3496622bb7325

Committed 2026-04-09 18:50 UTC

Revealed 2026-08-17 17:47 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-JBKARRJ7%22%2C%22bug_class%22%3A%22Out-of-bounds%20Write%22%2C%22claude_severity%22%3A%22low%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A43%3A13%2B00%3A00%22%2C%22description%22%3A%22An%20out-of-bounds%20index%20into%20the%20IFD%20array%20during%20EXIF%20parsing%20produces%20a%20corrupted%20pointer%20that%20is%20then%20used%20as%20a%20write%20target.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22libvips%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3Anull%2C%22title%22%3A%22Out-of-bounds%20IFD%20array%20access%20in%20EXIF%20metadata%20processing%20leading%20to%20write%20through%20corrupted%20pointer%22%2C%22vendor_severity%22%3A%22low%22%7D)

```
  "ant_id": "ANT-2026-JBKARRJ7",
  "bug_class": "Out-of-bounds Write",
  "claude_severity": "low",
  "created_at": "2026-03-29T20:43:13+00:00",
  "description": "An out-of-bounds index into the IFD array during EXIF parsing produces a corrupted pointer that is then used as a write target.",
  "location": null,
  "project": "libvips",
  "technical_details": null,
  "title": "Out-of-bounds IFD array access in EXIF metadata processing leading to write through corrupted pointer",
  "vendor_severity": "low"
```
