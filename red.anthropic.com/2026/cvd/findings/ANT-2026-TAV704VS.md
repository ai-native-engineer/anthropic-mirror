<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-TAV704VS -->

# ANT-2026-TAV704VS · freerdp/freerdp

## rce high

[CVE-2026-64624](https://nvd.nist.gov/vuln/detail/CVE-2026-64624)
[GHSA-rq8f-9xjh-pr3m](https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-rq8f-9xjh-pr3m)

Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-TAV704VS: .rdp file lines injected as CLI options enabling command execution

freerdp\_client\_parse\_rdp\_file\_buffer\_int() at client/common/file.c:938 appends any .rdp line beginning with '/' to file->args, which is later passed wholesale to freerdp\_client\_settings\_parse\_command\_line() (file.c:~2605). This exposes every CLI switch to the .rdp author, including /rdp2tcp:, which causes channels/rdp2tcp/client/rdp2tcp\_main.c:97-108 to call CreateProcessA() on the attacker-controlled string during VirtualChannelEntryEx — before any TCP/TLS handshake. The rdp2tcp channel is built by default and argv[1] ending in .rdp is auto-parsed, so a victim merely opening an emailed .rdp file gets one-click arbitrary command execution. Additional injectable primitives include /cert:ignore, /drive:root,/ and /action-script.

**Project:** freerdp/freerdp
**Location:** `client/common/file.c:938`

The .rdp parser falls back to treating any unmatched '/'-prefixed line as a raw argv option with no allowlist, collapsing the trust boundary between an externally-delivered interchange file and local command-line configuration. Because /rdp2tcp: is a valid CLI option whose value is handed straight to CreateProcessA()/fork+execve during pre-connect channel load, the .rdp author gains arbitrary local command execution with no server-side or TLS gating.

1. file.c:938-943 appends any '/'-prefixed .rdp line verbatim to file->args via freerdp\_client\_add\_option()
2. file.c:2600-2610 passes file->args to freerdp\_client\_settings\_parse\_command\_line() — the full CLI parser
3. cmdline.c:5574-5577 accepts /rdp2tcp: and stores it in FreeRDP\_RDP2TCPArgs
4. cmdline.c:6386-6402 adds and loads the rdp2tcp static channel when FreeRDP\_RDP2TCPArgs is set
5. freerdp.c:135 → utils\_reload\_channels() → LoadChannels runs BEFORE rdp\_client\_connect() (pre-TLS)
6. client.c:1548 invokes the channel's VirtualChannelEntryEx during load
7. rdp2tcp\_main.c:310 → init\_external\_addin() → rdp2tcp\_main.c:97-108 passes the attacker string directly to CreateProcessA()
8. On POSIX, winpr process.c:216,313 performs fork()+execve() on it

## Suggested Fix

Do not interpret unrecognised .rdp content as command-line switches; restrict .rdp parsing strictly to the documented Microsoft key:type:value grammar and ignore all other lines (or apply an explicit allowlist of safe options).

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-TAV704VS.

---

**Reference:** ANT-2026-TAV704VS

Triage and disclosure were performed by Ada Logics. The writeup below is the document the firm sent to the maintainer.

## Summary

FreeRDP's `.rdp` connection-file parser treats **any line beginning with `/` as a
raw command-line option** and appends it verbatim to the argument vector later
handed to the full `CLI` parser (`freerdp_client_settings_parse_command_line`).
The documented `.rdp` grammar is strictly `name:type:value` (the Microsoft
interchange format); this `/`-prefixed fallback is **not documented in the
FreeRDP man page or user manual** — which show `CLI` options only *after* the file
on the command line (`xfreerdp connection.rdp /p:… /f`) — and it silently exposes
the **entire `xfreerdp` option surface** to whoever authored the file.

The concrete consequences, in rough order of how hard they are to dismiss as
"intended," are:

* **`/cert:ignore` — silent TLS-validation bypass.** A `.rdp` file can disable
  certificate checking with no prompt, so a victim connecting to a
  man-in-the-middled or spoofed server gets no warning. There is no legitimate
  reason an interchange file should be able to silently weaken the client's
  transport security.
* **`/drive:...` — local filesystem exposure.** A `.rdp` file can mount the
  user's local directories into the (attacker-controlled) remote session.
* **`/rdp2tcp:<command>` — local command execution.** The `rdp2tcp` channel is
  *designed* to launch a helper process, so its argument goes straight to
  `CreateProcessA()` (POSIX: `fork()`+`execve()`). Because channel loading
  happens inside `freerdp_connect()` **before the TCP/TLS handshake**, merely
  opening the file runs an attacker-named local command — no server, no
  certificate, no authentication, even if no RDP server exists. This is the most
  severe outcome but also the one most easily read as "that option is meant to
  spawn a process"; the report is really about the *file → full-CLI* exposure
  that makes it (and the two above) reachable from an untrusted file. The
  `/rdp2tcp` variant additionally requires the channel to be compiled in (OFF in
  the bare upstream cmake default, but ON in Debian/Ubuntu packaging); the
  `/cert:ignore` and `/drive` variants are present in every client build.

## Note on FreeRDP reacting to this

* Deprecation of arbitrary `CLI` parsing: The behavior where /-prefixed lines in a `.rdp` file are forwarded to the `CLI` parser will be disabled by default in the next (=3.28.0) release and is officially marked for complete removal in a future major version. `FreeRDP` already supports the /args-from parameter for users who explicitly intend to load command-line arguments from a local file (or `stdin`).
* Untrusted paradigm for `.rdp` files: Because `.rdp` files are widespread, standard and expected default options must continue to work. However, we recognize that even standard properties (such as drive redirection drivestoredirect) can be used maliciously to expose local data. Unless a `.rdp` file is signed and verified via a trusted chain, it must be treated as untrusted. For future versions, we will be discussing a model where only a "safe default set" of options is allowed automatically, while risky or potentially problematic options will require an explicit confirmation (such as a specific command-line flag provided by the user). Signature verification isn't implemented yet.
* /rdp2tcp: The ability for a `.rdp` file to spawn a helper process via /rdp2tcp is a possible risk. With the argument parsing disabled this should be mitigated. We will be adding a build-time notice regarding this behavior and are planning a future architecture rewrite. On a long term our goal is to deprecate the external binary requirement entirely and move toward an internal tunneling mechanism (similar to SSH -L and -R port forwarding). We've already add a deprecation warning for the next release.

## Compatibility

With 3.28.0 the option has been disabled by default, use `-DWITH_EMBEDDED_CLI_IN_RDP_FILES=ON` to enable this behavior again.

```
diff --git a/client/common/CMakeLists.txt b/client/common/CMakeLists.txt
index 79b2700cf3d5..8b0952ec2c1f 100644
--- a/client/common/CMakeLists.txt
+++ b/client/common/CMakeLists.txt
@@ -50,6 +50,11 @@ else()
   set(OPT_FUSE_DEFAULT OFF)
 endif()

+option(WITH_EMBEDDED_CLI_IN_RDP_FILES "[dangrous] allow embedded cli arguments in rdp files" OFF)
+if(WITH_EMBEDDED_CLI_IN_RDP_FILES)
+  add_compile_definitions(WITH_EMBEDDED_CLI_IN_RDP_FILES)
+endif()
+
 option(WITH_FUSE "Build clipboard with FUSE file copy support" ${OPT_FUSE_DEFAULT})
 if(WITH_FUSE)
   find_package(PkgConfig REQUIRED)
diff --git a/client/common/file.c b/client/common/file.c
index 91c170796788..8936dee45f36 100644
--- a/client/common/file.c
+++ b/client/common/file.c
@@ -27,6 +27,8 @@
 #include <winpr/file.h>
 #include <winpr/cast.h>

+#include <freerdp/utils/warnings.h>
+
 #include <freerdp/client.h>
 #include <freerdp/client/file.h>
 #include <freerdp/client/cmdline.h>
@@ -879,13 +881,17 @@ static BOOL parse_line(rdpFile* file, char* line, size_t length, rdp_file_fkt_pa

 	const char* beg = line;
 #if !defined(WITHOUT_FREERDP_3x_DEPRECATED)
+#if defined(WITH_EMBEDDED_CLI_IN_RDP_FILES)
 	if (beg[0] == '/')
+		freerdp_warn_deprecated(WLog_Get(TAG), "Parsing CLI options within an RDP file",
+		                        "Will be removed in FreeRDP 4.0");
 		if (!freerdp_client_add_option(file, line))
 			return FALSE;

 		return TRUE; /* FreeRDP option */
+#endif
 #endif

 	char* d1 = strchr(line, ':');
```

<https://github.com/FreeRDP/FreeRDP/commit/22c5deea52404f51a13276b3abda44e1e60704cf>

1. 2026-04-02
2. 2026-07-06
3. 2026-07-22
4. 2026-07-22
5. 2026-09-28

9414feb034ec0b96d72acb97d9a689482815eddf76e8bb5ca1ffec484ed7f1332f728b0de81285e8cf7fe93b84d128b420fb8b71e4832301886d0ca16c5e14f6

Committed 2026-07-22 07:29 UTC

Revealed 2026-09-28 21:46 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-TAV704VS%22%2C%22bug_class%22%3A%22Argument%20Injection%20/%20Remote%20Code%20Execution%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-16T01%3A52%3A40%2B00%3A00%22%2C%22description%22%3A%22freerdp_client_parse_rdp_file_buffer_int%28%29%20at%20client/common/file.c%3A938%20appends%20any%20.rdp%20line%20beginning%20with%20%27/%27%20to%20file-%3Eargs%2C%20which%20is%20later%20passed%20wholesale%20to%20freerdp_client_settings_parse_command_line%28%29%20%28file.c%3A~2605%29.%20This%20exposes%20every%20CLI%20switch%20to%20the%20.rdp%20author%2C%20including%20/rdp2tcp%3A%3Ccmd%3E%2C%20which%20causes%20channels/rdp2tcp/client/rdp2tcp_main.c%3A97-108%20to%20call%20CreateProcessA%28%29%20on%20the%20attacker-controlled%20string%20during%20VirtualChannelEntryEx%20%E2%80%94%20before%20any%20TCP/TLS%20handshake.%20The%20rdp2tcp%20channel%20is%20built%20by%20default%20and%20argv%5B1%5D%20ending%20in%20.rdp%20is%20auto-parsed%2C%20so%20a%20victim%20merely%20opening%20an%20emailed%20.rdp%20file%20gets%20one-click%20arbitrary%20command%20execution.%20Additional%20injectable%20primitives%20include%20/cert%3Aignore%2C%20/drive%3Aroot%2C/%20and%20/action-script.%22%2C%22discovered_at%22%3A%222026-04-02T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22client/common/file.c%3A938%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22freerdp/freerdp%22%2C%22reproduction%22%3A%5B%221.%20file.c%3A938-943%20appends%20any%20%27/%27-prefixed%20.rdp%20line%20verbatim%20to%20file-%3Eargs%20via%20freerdp_client_add_option%28%29%22%2C%222.%20file.c%3A2600-2610%20passes%20file-%3Eargs%20to%20freerdp_client_settings_parse_command_line%28%29%20%E2%80%94%20the%20full%20CLI%20parser%22%2C%223.%20cmdline.c%3A5574-5577%20accepts%20/rdp2tcp%3A%3Cvalue%3E%20and%20stores%20it%20in%20FreeRDP_RDP2TCPArgs%22%2C%224.%20cmdline.c%3A6386-6402%20adds%20and%20loads%20the%20rdp2tcp%20static%20channel%20when%20FreeRDP_RDP2TCPArgs%20is%20set%22%2C%225.%20freerdp.c%3A135%20%E2%86%92%20utils_reload_channels%28%29%20%E2%86%92%20LoadChannels%20runs%20BEFORE%20rdp_client_connect%28%29%20%28pre-TLS%29%22%2C%226.%20client.c%3A1548%20invokes%20the%20channel%27s%20VirtualChannelEntryEx%20during%20load%22%2C%227.%20rdp2tcp_main.c%3A310%20%E2%86%92%20init_external_addin%28%29%20%E2%86%92%20rdp2tcp_main.c%3A97-108%20passes%20the%20attacker%20string%20directly%20to%20CreateProcessA%28%29%22%2C%228.%20On%20POSIX%2C%20winpr%20process.c%3A216%2C313%20performs%20fork%28%29%2Bexecve%28%29%20on%20it%22%5D%2C%22technical_details%22%3A%22The%20.rdp%20parser%20falls%20back%20to%20treating%20any%20unmatched%20%27/%27-prefixed%20line%20as%20a%20raw%20argv%20option%20with%20no%20allowlist%2C%20collapsing%20the%20trust%20boundary%20between%20an%20externally-delivered%20interchange%20file%20and%20local%20command-line%20configuration.%20Because%20/rdp2tcp%3A%20is%20a%20valid%20CLI%20option%20whose%20value%20is%20handed%20straight%20to%20CreateProcessA%28%29/fork%2Bexecve%20during%20pre-connect%20channel%20load%2C%20the%20.rdp%20author%20gains%20arbitrary%20local%20command%20execution%20with%20no%20server-side%20or%20TLS%20gating.%22%2C%22title%22%3A%22.rdp%20file%20lines%20injected%20as%20CLI%20options%20enabling%20command%20execution%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-TAV704VS",
  "bug_class": "Argument Injection / Remote Code Execution",
  "created_at": "2026-04-16T01:52:40+00:00",
  "description": "freerdp_client_parse_rdp_file_buffer_int() at client/common/file.c:938 appends any .rdp line beginning with '/' to file->args, which is later passed wholesale to freerdp_client_settings_parse_command_line() (file.c:~2605). This exposes every CLI switch to the .rdp author, including /rdp2tcp:<cmd>, which causes channels/rdp2tcp/client/rdp2tcp_main.c:97-108 to call CreateProcessA() on the attacker-controlled string during VirtualChannelEntryEx — before any TCP/TLS handshake. The rdp2tcp channel is built by default and argv[1] ending in .rdp is auto-parsed, so a victim merely opening an emailed .rdp file gets one-click arbitrary command execution. Additional injectable primitives include /cert:ignore, /drive:root,/ and /action-script.",
  "discovered_at": "2026-04-02T00:00:00+00:00",
  "location": "client/common/file.c:938",
  "project": "freerdp/freerdp",
    "1. file.c:938-943 appends any '/'-prefixed .rdp line verbatim to file->args via freerdp_client_add_option()",
    "2. file.c:2600-2610 passes file->args to freerdp_client_settings_parse_command_line() — the full CLI parser",
    "3. cmdline.c:5574-5577 accepts /rdp2tcp:<value> and stores it in FreeRDP_RDP2TCPArgs",
    "4. cmdline.c:6386-6402 adds and loads the rdp2tcp static channel when FreeRDP_RDP2TCPArgs is set",
    "5. freerdp.c:135 → utils_reload_channels() → LoadChannels runs BEFORE rdp_client_connect() (pre-TLS)",
    "6. client.c:1548 invokes the channel's VirtualChannelEntryEx during load",
    "7. rdp2tcp_main.c:310 → init_external_addin() → rdp2tcp_main.c:97-108 passes the attacker string directly to CreateProcessA()",
    "8. On POSIX, winpr process.c:216,313 performs fork()+execve() on it"
  "technical_details": "The .rdp parser falls back to treating any unmatched '/'-prefixed line as a raw argv option with no allowlist, collapsing the trust boundary between an externally-delivered interchange file and local command-line configuration. Because /rdp2tcp: is a valid CLI option whose value is handed straight to CreateProcessA()/fork+execve during pre-connect channel load, the .rdp author gains arbitrary local command execution with no server-side or TLS gating.",
  "title": ".rdp file lines injected as CLI options enabling command execution",
```
