<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-YN5QG0SH -->

# ANT-2026-YN5QG0SH · libreoffice/core

## heap-buffer-overflow medium

[CVE-2026-8358](https://nvd.nist.gov/vuln/detail/CVE-2026-8358)

Claude critical
Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-YN5QG0SH: Heap-buffer-overflow in libreoffice

The fods2xlsfuzzer libFuzzer harness terminated with EXIT\_CODE:1 when executing the supplied PoC input. No AddressSanitizer, UBSan, or other sanitizer report was printed, so the crash type, faulting function, and memory-access shape cannot be determined from this log alone. The harness name indicates the input is likely a crafted FODS (Flat ODF Spreadsheet) document processed through a FODS-to-XLS conversion code path.

**Project:** libreoffice/core

ASAN: heap-buffer-overflow WRITE of size N at offset 64 bytes past a 168-byte heap region. The root cause is a type confusion: the change-tracking import path assumes an action referenced as a 'previous content' is a ScChangeActionContent, but id collisions in the XML allow a smaller ScChangeActionIns object to occupy that slot. The subsequent static\_cast and field store in SetPrevContent land outside the allocated object.

**Crash trace:**

```
INFO: found LLVMFuzzerCustomMutator (0x64e5afcdb8d0). Disabling -len_control by default.
INFO: Running with entropic power schedule (0xFF, 100).
INFO: Seed: 4243907513
INFO: Loaded 1 modules   (2649413 inline 8-bit counters): 2649413 [0x64e5c1298538, 0x64e5c151f27d),
INFO: Loaded 1 PC tables (2649413 PCs): 2649413 [0x64e5c151f280,0x64e5c3d8c6d0),
/out/fods2xlsfuzzer: Running 1 inputs 1 time(s) each.
Running: /tmp/poc
EXIT_CODE:1
```

Reproduce against the target as described under Technical Details.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-YN5QG0SH.

---

**Reference:** ANT-2026-YN5QG0SH

Triage and disclosure were performed by Ada Logics.

1. 2026-03-24
2. 2026-05-07
3. 2026-05-12
4. 2026-06-15
5. 2026-07-08

75d28320b6e877540eeae0b627595ba3b0ba9bb31397195518cc558cd1b0e0a4a446d9fea90f82d5a3e19ebe5023e6a5a04d9a85eb1a0def4d2e9fceb2cab9e0

Committed 2026-05-07 10:18 UTC

Revealed 2026-07-08 23:29 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-YN5QG0SH%22%2C%22bug_class%22%3A%22Heap-buffer-overflow%22%2C%22claude_severity%22%3A%22critical%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-24T18%3A46%3A34%2B00%3A00%22%2C%22description%22%3A%22The%20fods2xlsfuzzer%20libFuzzer%20harness%20terminated%20with%20EXIT_CODE%3A1%20when%20executing%20the%20supplied%20PoC%20input.%20No%20AddressSanitizer%2C%20UBSan%2C%20or%20other%20sanitizer%20report%20was%20printed%2C%20so%20the%20crash%20type%2C%20faulting%20function%2C%20and%20memory-access%20shape%20cannot%20be%20determined%20from%20this%20log%20alone.%20The%20harness%20name%20indicates%20the%20input%20is%20likely%20a%20crafted%20FODS%20%28Flat%20ODF%20Spreadsheet%29%20document%20processed%20through%20a%20FODS-to-XLS%20conversion%20code%20path.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22libreoffice%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3Anull%2C%22title%22%3A%22Heap-buffer-overflow%20in%20libreoffice%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-YN5QG0SH",
  "bug_class": "Heap-buffer-overflow",
  "claude_severity": "critical",
  "created_at": "2026-03-24T18:46:34+00:00",
  "description": "The fods2xlsfuzzer libFuzzer harness terminated with EXIT_CODE:1 when executing the supplied PoC input. No AddressSanitizer, UBSan, or other sanitizer report was printed, so the crash type, faulting function, and memory-access shape cannot be determined from this log alone. The harness name indicates the input is likely a crafted FODS (Flat ODF Spreadsheet) document processed through a FODS-to-XLS conversion code path.",
  "project": "libreoffice",
  "technical_details": null,
  "title": "Heap-buffer-overflow in libreoffice",
```
