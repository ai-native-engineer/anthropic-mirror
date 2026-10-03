<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-HY56VRSB -->

# ANT-2026-HY56VRSB · nginx/nginx

## heap-buffer-overflow high

[CVE-2026-27654](https://nvd.nist.gov/vuln/detail/CVE-2026-27654)

Security research firm critical
Maintainer high

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Calif.

# ANT-2026-HY56VRSB: Heap buffer overflow in ngx\_http\_dav\_copy\_move\_handler at ngx\_http\_dav\_module.c:703 via short Destination header with alias directive

In ngx\_http\_dav\_copy\_move\_handler(), processing a COPY or MOVE request in a location using the alias directive temporarily replaces r->uri with the attacker-controlled Destination header URI and calls ngx\_http\_map\_uri\_to\_path() without re-matching location blocks. If the Destination URI is shorter than clcf->alias, the buffer size computation (root.len + reserved + uri.len - alias + 1) produces an undersized allocation. ngx\_copy then writes root.len bytes into this undersized buffer, overflowing it, and a subsequent ngx\_copy computes uri.len - alias as size\_t, underflowing to a massive length and crashing the worker. An attacker needs only a single COPY request with a short Destination header (e.g., Destination: /x against a 5-character alias) to trigger worker crash and potential heap corruption.

**Project:** nginx/nginx
**Location:** `src/http/modules/ngx_http_dav_module.c:703`

The root cause is that the handler swaps r->uri with the Destination URI (line 701) and immediately calls ngx\_http\_map\_uri\_to\_path() (line 703) without validating that the new URI length is >= clcf->alias. In ngx\_http\_map\_uri\_to\_path() at ngx\_http\_core\_module.c:1943, path->len = clcf->root.len + reserved + r->uri.len - alias + 1 underflows when uri.len < alias (e.g., 9+0+2-5+1 = 7 for a 9-byte root), and ngx\_copy at line 1950 writes the full 9-byte root into the 7-byte buffer. Neither ngx\_http\_parse\_unsafe\_uri nor the valid\_location check enforces a minimum Destination length relative to the alias.

1. Identify a target location combining alias and dav\_methods COPY/MOVE (e.g., location /dav/ { alias /var/www/; dav\_methods COPY; })
2. Send: COPY /dav/file.txt HTTP/1.1 with header Destination: /x (any path shorter than the 5-character alias '/dav/')
3. Handler swaps r->uri to '/x' (len=2), calls ngx\_http\_map\_uri\_to\_path(); path->len computes to 7 bytes but ngx\_copy writes 9 bytes of root, overflowing by 2; second ngx\_copy underflows 2-5 as size\_t and wild-copies until crash

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-HY56VRSB.

---

**Reference:** ANT-2026-HY56VRSB

Triage and disclosure were performed by Calif.

:   critical

CONSOLIDATED FROM

The following finding was consolidated into this one after publication; this card carries the shared disclosure record. Each original commitment remains in the ledger.

[ANT-2026-VS18SA90](https://red.anthropic.com/2026/cvd/findings/ANT-2026-VS18SA90.html)

70c7065a7506628831667e565053165f8142abd80e67756200c4b6cb0d6c34fe0590d7f2fa655fbfd2cc36da73eeb98d23667209d18f2ca4ba3f2554e8194d1c

1. 2026-03-20
2. 2026-03-20
3. 2026-05-20
4. 2026-05-20
5. 2026-08-20

64bfee709f646fc04ffed676034930182615fbe340bb4bbeecf2bdd53bc3fafc738cc51c1b25e2601cd2de21f1d303a90581e3201aaf0062593b5a4179344db5

Committed 2026-03-20 23:27 UTC

Revealed 2026-05-20 07:40 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-HY56VRSB%22%2C%22bug_class%22%3A%22Heap%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-20T19%3A13%3A25%2B00%3A00%22%2C%22description%22%3A%22In%20ngx_http_dav_copy_move_handler%28%29%2C%20processing%20a%20COPY%20or%20MOVE%20request%20in%20a%20location%20using%20the%20alias%20directive%20temporarily%20replaces%20r-%3Euri%20with%20the%20attacker-controlled%20Destination%20header%20URI%20and%20calls%20ngx_http_map_uri_to_path%28%29%20without%20re-matching%20location%20blocks.%20If%20the%20Destination%20URI%20is%20shorter%20than%20clcf-%3Ealias%2C%20the%20buffer%20size%20computation%20%28root.len%20%2B%20reserved%20%2B%20uri.len%20-%20alias%20%2B%201%29%20produces%20an%20undersized%20allocation.%20ngx_copy%20then%20writes%20root.len%20bytes%20into%20this%20undersized%20buffer%2C%20overflowing%20it%2C%20and%20a%20subsequent%20ngx_copy%20computes%20uri.len%20-%20alias%20as%20size_t%2C%20underflowing%20to%20a%20massive%20length%20and%20crashing%20the%20worker.%20An%20attacker%20needs%20only%20a%20single%20COPY%20request%20with%20a%20short%20Destination%20header%20%28e.g.%2C%20Destination%3A%20/x%20against%20a%205-character%20alias%29%20to%20trigger%20worker%20crash%20and%20potential%20heap%20corruption.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3A%22src/http/modules/ngx_http_dav_module.c%3A703%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22nginx%22%2C%22reproduction%22%3A%5B%221.%20Identify%20a%20target%20location%20combining%20alias%20and%20dav_methods%20COPY/MOVE%20%28e.g.%2C%20location%20/dav/%20%7B%20alias%20/var/www/%3B%20dav_methods%20COPY%3B%20%7D%29%22%2C%222.%20Send%3A%20COPY%20/dav/file.txt%20HTTP/1.1%20with%20header%20Destination%3A%20/x%20%28any%20path%20shorter%20than%20the%205-character%20alias%20%27/dav/%27%29%22%2C%223.%20Handler%20swaps%20r-%3Euri%20to%20%27/x%27%20%28len%3D2%29%2C%20calls%20ngx_http_map_uri_to_path%28%29%3B%20path-%3Elen%20computes%20to%207%20bytes%20but%20ngx_copy%20writes%209%20bytes%20of%20root%2C%20overflowing%20by%202%3B%20second%20ngx_copy%20underflows%202-5%20as%20size_t%20and%20wild-copies%20until%20crash%22%5D%2C%22technical_details%22%3A%22The%20root%20cause%20is%20that%20the%20handler%20swaps%20r-%3Euri%20with%20the%20Destination%20URI%20%28line%20701%29%20and%20immediately%20calls%20ngx_http_map_uri_to_path%28%29%20%28line%20703%29%20without%20validating%20that%20the%20new%20URI%20length%20is%20%3E%3D%20clcf-%3Ealias.%20In%20ngx_http_map_uri_to_path%28%29%20at%20ngx_http_core_module.c%3A1943%2C%20path-%3Elen%20%3D%20clcf-%3Eroot.len%20%2B%20reserved%20%2B%20r-%3Euri.len%20-%20alias%20%2B%201%20underflows%20when%20uri.len%20%3C%20alias%20%28e.g.%2C%209%2B0%2B2-5%2B1%20%3D%207%20for%20a%209-byte%20root%29%2C%20and%20ngx_copy%20at%20line%201950%20writes%20the%20full%209-byte%20root%20into%20the%207-byte%20buffer.%20Neither%20ngx_http_parse_unsafe_uri%20nor%20the%20valid_location%20check%20enforces%20a%20minimum%20Destination%20length%20relative%20to%20the%20alias.%22%2C%22title%22%3A%22Heap%20buffer%20overflow%20in%20ngx_http_dav_copy_move_handler%20at%20ngx_http_dav_module.c%3A703%20via%20short%20Destination%20header%20with%20alias%20directive%22%2C%22vendor_severity%22%3Anull%7D)

```
  "ant_id": "ANT-2026-HY56VRSB",
  "bug_class": "Heap",
  "created_at": "2026-03-20T19:13:25+00:00",
  "description": "In ngx_http_dav_copy_move_handler(), processing a COPY or MOVE request in a location using the alias directive temporarily replaces r->uri with the attacker-controlled Destination header URI and calls ngx_http_map_uri_to_path() without re-matching location blocks. If the Destination URI is shorter than clcf->alias, the buffer size computation (root.len + reserved + uri.len - alias + 1) produces an undersized allocation. ngx_copy then writes root.len bytes into this undersized buffer, overflowing it, and a subsequent ngx_copy computes uri.len - alias as size_t, underflowing to a massive length and crashing the worker. An attacker needs only a single COPY request with a short Destination header (e.g., Destination: /x against a 5-character alias) to trigger worker crash and potential heap corruption.",
  "location": "src/http/modules/ngx_http_dav_module.c:703",
  "project": "nginx",
    "1. Identify a target location combining alias and dav_methods COPY/MOVE (e.g., location /dav/ { alias /var/www/; dav_methods COPY; })",
    "2. Send: COPY /dav/file.txt HTTP/1.1 with header Destination: /x (any path shorter than the 5-character alias '/dav/')",
    "3. Handler swaps r->uri to '/x' (len=2), calls ngx_http_map_uri_to_path(); path->len computes to 7 bytes but ngx_copy writes 9 bytes of root, overflowing by 2; second ngx_copy underflows 2-5 as size_t and wild-copies until crash"
  "technical_details": "The root cause is that the handler swaps r->uri with the Destination URI (line 701) and immediately calls ngx_http_map_uri_to_path() (line 703) without validating that the new URI length is >= clcf->alias. In ngx_http_map_uri_to_path() at ngx_http_core_module.c:1943, path->len = clcf->root.len + reserved + r->uri.len - alias + 1 underflows when uri.len < alias (e.g., 9+0+2-5+1 = 7 for a 9-byte root), and ngx_copy at line 1950 writes the full 9-byte root into the 7-byte buffer. Neither ngx_http_parse_unsafe_uri nor the valid_location check enforces a minimum Destination length relative to the alias.",
  "title": "Heap buffer overflow in ngx_http_dav_copy_move_handler at ngx_http_dav_module.c:703 via short Destination header with alias directive",
  "vendor_severity": null
```
