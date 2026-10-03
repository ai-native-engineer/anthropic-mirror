<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-XV1EVAMH -->

# ANT-2026-XV1EVAMH · libreoffice/core

## heap-buffer-overflow medium

[CVE-2026-8357](https://nvd.nist.gov/vuln/detail/CVE-2026-8357)

Claude critical
Maintainer medium

Claude Sonnet 4.6

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-XV1EVAMH: Heap-buffer-overflow in libreoffice

LibreOffice Calc's formula compiler (ScCompiler::CompileString in sc/source/core/tool/compiler.cxx) allocates a FunctionStack array sized to the formula string length when that length exceeds a 512-element stack buffer. For each '(' token it increments nFunction and writes to pFunctionStack[nFunction] without bounds checking. A crafted FODS file containing a formula of 513 '(' characters causes nFunction to reach 513 while the heap buffer has only indices 0-512, producing a 2-byte out-of-bounds heap write. An attacker who can get a victim to open a malicious FODS/ODS document can corrupt heap memory, potentially leading to code execution.

**Project:** libreoffice/core

ASAN: heap-buffer-overflow WRITE of size 2 at 0x51d000009484 in ScCompiler::CompileString (compiler.cxx:4907:53). The root cause is an off-by-one: the FunctionStack heap buffer is sized to rFormula.getLength() (513), but nFunction starts at 0 and is pre-incremented once per '(' token, so 513 open-parens drive the index to 513 and pFunctionStack[513].eOp is written one element past the end of the allocation.

**Crash trace:**

```
INFO: Running with entropic power schedule (0xFF, 100).
INFO: Seed: 1873441852
INFO: Loaded 1 modules   (2649230 inline 8-bit counters): 2649230 [0x5f3f59fc7538, 0x5f3f5a24e1c6),
INFO: Loaded 1 PC tables (2649230 PCs): 2649230 [0x5f3f5a24e1c8,0x5f3f5cabaaa8),
/out/fodsfuzzer: Running 1 inputs 1 time(s) each.
Running: /tmp/poc
EXIT_CODE:1
```

Reproduce against the target as described under Technical Details.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-XV1EVAMH.

---

**Reference:** ANT-2026-XV1EVAMH

Triage and disclosure were performed by Ada Logics.

1. 2026-03-24
2. 2026-05-07
3. 2026-05-12
4. 2026-06-15
5. 2026-07-08

46a2e2e4443a4f989f784b937a63d3aa8021f566ad7d8f9974478c1791e72f7c64c4d7e525f2dab06d95313c4dd097f29f18a4934760cf9edc5ff0881631d565

Committed 2026-05-07 21:16 UTC

Revealed 2026-07-08 23:30 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-XV1EVAMH%22%2C%22bug_class%22%3A%22Heap-buffer-overflow%22%2C%22claude_severity%22%3A%22critical%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-24T18%3A45%3A47%2B00%3A00%22%2C%22description%22%3A%22LibreOffice%20Calc%27s%20formula%20compiler%20%28ScCompiler%3A%3ACompileString%20in%20sc/source/core/tool/compiler.cxx%29%20allocates%20a%20FunctionStack%20array%20sized%20to%20the%20formula%20string%20length%20when%20that%20length%20exceeds%20a%20512-element%20stack%20buffer.%20For%20each%20%27%28%27%20token%20it%20increments%20nFunction%20and%20writes%20to%20pFunctionStack%5BnFunction%5D%20without%20bounds%20checking.%20A%20crafted%20FODS%20file%20containing%20a%20formula%20of%20513%20%27%28%27%20characters%20causes%20nFunction%20to%20reach%20513%20while%20the%20heap%20buffer%20has%20only%20indices%200-512%2C%20producing%20a%202-byte%20out-of-bounds%20heap%20write.%20An%20attacker%20who%20can%20get%20a%20victim%20to%20open%20a%20malicious%20FODS/ODS%20document%20can%20corrupt%20heap%20memory%2C%20potentially%20leading%20to%20code%20execution.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22libreoffice%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3A%22ASAN%3A%20heap-buffer-overflow%20WRITE%20of%20size%202%20at%200x51d000009484%20in%20ScCompiler%3A%3ACompileString%20%28compiler.cxx%3A4907%3A53%29.%20The%20root%20cause%20is%20an%20off-by-one%3A%20the%20FunctionStack%20heap%20buffer%20is%20sized%20to%20rFormula.getLength%28%29%20%28513%29%2C%20but%20nFunction%20starts%20at%200%20and%20is%20pre-incremented%20once%20per%20%27%28%27%20token%2C%20so%20513%20open-parens%20drive%20the%20index%20to%20513%20and%20pFunctionStack%5B513%5D.eOp%20is%20written%20one%20element%20past%20the%20end%20of%20the%20allocation.%22%2C%22title%22%3A%22Heap-buffer-overflow%20in%20libreoffice%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-XV1EVAMH",
  "bug_class": "Heap-buffer-overflow",
  "claude_severity": "critical",
  "created_at": "2026-03-24T18:45:47+00:00",
  "description": "LibreOffice Calc's formula compiler (ScCompiler::CompileString in sc/source/core/tool/compiler.cxx) allocates a FunctionStack array sized to the formula string length when that length exceeds a 512-element stack buffer. For each '(' token it increments nFunction and writes to pFunctionStack[nFunction] without bounds checking. A crafted FODS file containing a formula of 513 '(' characters causes nFunction to reach 513 while the heap buffer has only indices 0-512, producing a 2-byte out-of-bounds heap write. An attacker who can get a victim to open a malicious FODS/ODS document can corrupt heap memory, potentially leading to code execution.",
  "project": "libreoffice",
  "technical_details": "ASAN: heap-buffer-overflow WRITE of size 2 at 0x51d000009484 in ScCompiler::CompileString (compiler.cxx:4907:53). The root cause is an off-by-one: the FunctionStack heap buffer is sized to rFormula.getLength() (513), but nFunction starts at 0 and is pre-incremented once per '(' token, so 513 open-parens drive the index to 513 and pFunctionStack[513].eOp is written one element past the end of the allocation.",
  "title": "Heap-buffer-overflow in libreoffice",
```
