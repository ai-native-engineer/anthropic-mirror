<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-TNXYTAEH -->

# ANT-2026-TNXYTAEH · libreoffice/core

## stack-buffer-overflow medium

[CVE-2026-8356](https://nvd.nist.gov/vuln/detail/CVE-2026-8356)

Claude critical
Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-TNXYTAEH: Stack-buffer-overflow in libreoffice

The pptfuzzer harness was run against a single reproducer (/tmp/poc) and exited with a non-zero status (EXIT\_CODE:1). No AddressSanitizer, UBSan, or other crash diagnostics were printed, so the crash type, faulting function, and access shape cannot be determined from this output alone. The target name suggests a PPT-format parsing entry point, but no source location or call chain is available.

**Project:** libreoffice/core

libFuzzer target pptfuzzer terminated with EXIT\_CODE:1 on the supplied input; no sanitizer diagnostic or stack trace was emitted.

**Crash trace:**

```
INFO: Running with entropic power schedule (0xFF, 100).
INFO: Seed: 1013862475
INFO: Loaded 1 modules   (1616799 inline 8-bit counters): 1616799 [0x619344d44708, 0x619344ecf2a7),
INFO: Loaded 1 PC tables (1616799 PCs): 1616799 [0x619344ecf2a8,0x61934677ac98),
/out/pptfuzzer: Running 1 inputs 1 time(s) each.
Running: /tmp/poc
EXIT_CODE:1
```

Reproduce against the target as described under Technical Details.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-TNXYTAEH.

---

**Reference:** ANT-2026-TNXYTAEH

Triage and disclosure were performed by Ada Logics.

1. 2026-03-24
2. 2026-04-25
3. 2026-05-12
4. 2026-05-13
5. 2026-07-14

d9cc357c5b6f7b6f74a76b06e2fe5f113c23a266bad42dd24dc5a86d1279175092594cbc68c21f6b8503bec67f6484af81dc7b3de16dcb8b2b7dc61abeeac758

Committed 2026-05-07 10:18 UTC

Revealed 2026-07-14 00:08 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-TNXYTAEH%22%2C%22bug_class%22%3A%22Stack-buffer-overflow%22%2C%22claude_severity%22%3A%22critical%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-24T18%3A31%3A41%2B00%3A00%22%2C%22description%22%3A%22The%20pptfuzzer%20harness%20was%20run%20against%20a%20single%20reproducer%20%28/tmp/poc%29%20and%20exited%20with%20a%20non-zero%20status%20%28EXIT_CODE%3A1%29.%20No%20AddressSanitizer%2C%20UBSan%2C%20or%20other%20crash%20diagnostics%20were%20printed%2C%20so%20the%20crash%20type%2C%20faulting%20function%2C%20and%20access%20shape%20cannot%20be%20determined%20from%20this%20output%20alone.%20The%20target%20name%20suggests%20a%20PPT-format%20parsing%20entry%20point%2C%20but%20no%20source%20location%20or%20call%20chain%20is%20available.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22libreoffice%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3Anull%2C%22title%22%3A%22Stack-buffer-overflow%20in%20libreoffice%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-TNXYTAEH",
  "bug_class": "Stack-buffer-overflow",
  "claude_severity": "critical",
  "created_at": "2026-03-24T18:31:41+00:00",
  "description": "The pptfuzzer harness was run against a single reproducer (/tmp/poc) and exited with a non-zero status (EXIT_CODE:1). No AddressSanitizer, UBSan, or other crash diagnostics were printed, so the crash type, faulting function, and access shape cannot be determined from this output alone. The target name suggests a PPT-format parsing entry point, but no source location or call chain is available.",
  "project": "libreoffice",
  "technical_details": null,
  "title": "Stack-buffer-overflow in libreoffice",
```
