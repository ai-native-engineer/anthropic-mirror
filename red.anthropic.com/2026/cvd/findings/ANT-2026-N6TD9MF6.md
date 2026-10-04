<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-N6TD9MF6 -->

# ANT-2026-N6TD9MF6 · opencontainers/runc

## symlink-following medium

[CVE-2026-41579](https://nvd.nist.gov/vuln/detail/CVE-2026-41579)
[GHSA-xjvp-4fhw-gc47](https://github.com/advisories/GHSA-xjvp-4fhw-gc47)

Maintainer medium

an unreleased Anthropic model

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Ada Logics.

# ANT-2026-N6TD9MF6: Host filesystem write via /dev symlink in container image

In libcontainer/rootfs\_linux.go, prepareRootfs() mounts the /dev tmpfs and creates device nodes using safe RESOLVE\_IN\_ROOT fd-relative operations, which follow a /dev symlink scoped inside the rootfs and leave the symlink itself intact. Immediately after, setupPtmx() and setupDevSymlinks() call filepath.Join(rootfs, "dev/...") with os.Remove/os.Symlink, which the kernel resolves without scoping — following an absolute /dev symlink out to the host filesystem. This runs as host root and before pivot\_root, while the mount namespace still mirrors the host. An attacker who authors a container image with /dev as a symlink to an arbitrary absolute host directory causes runc to create fixed-name symlinks (ptmx, fd, stdin, stdout, stderr, core) in that host directory. Pointing /dev at host /dev deletes and replaces the real /dev/ptmx, breaking PTY allocation host-wide.

**Project:** opencontainers/runc
**Version:** 7a1cae6dd02884889960889fe11c1dad832a3cce (present at HEAD)
**Location:** `libcontainer/rootfs_linux.go:1125`

Built runc at HEAD (7a1cae6dd). Created an OCI bundle whose rootfs/dev is a symlink to an absolute path /tmp/host-sentinel-408 (a directory OUTSIDE the rootfs, on the 'host' — here the outer privileged Docker container). The bundle uses the standard tmpfs /dev mount. Ran `runc run`. The container started successfully (exit 0). After the run, /tmp/host-sentinel-408 contained five new symlinks: ptmx→pts/ptmx, fd→/proc/self/fd, stdin→/proc/self/fd/0, stdout→/proc/self/fd/1, stderr→/proc/self/fd/2. These were created by setupPtmx() and setupDevSymlinks() in libcontainer/rootfs\_linux.go, which use filepath.Join(rootfs,"dev/...")+os.Symlink — the kernel followed the absolute symlink at rootfs/dev unscoped, landing outside the rootfs, before pivot\_root. The safe pathrs-based /dev tmpfs mount followed the symlink SCOPED (to rootfs/tmp/host-sentinel-408), leaving the rootfs/dev symlink itself intact for the unsafe calls to follow. This is a host-filesystem write from a malicious container image with no privileges beyond image authorship.

1. Build an OCI rootfs where /dev is a symlink to an absolute host path (e.g. /etc or /dev) and a real directory exists at that path inside the rootfs so scoped resolution succeeds.
2. Push the image; victim pulls and runs it with standard config.json (tmpfs on /dev).
3. prepareRootfs mounts tmpfs onto the scoped target (/) via openat2 RESOLVE\_IN\_ROOT, leaving the /dev symlink untouched.
4. setupPtmx() does os.Remove + os.Symlink on "/dev/ptmx"; kernel follows the absolute symlink unscoped and creates //ptmx -> pts/ptmx on the host.
5. setupDevSymlinks() likewise creates fd, stdin, stdout, stderr, core symlinks in the host target directory.
6. If target is host /dev, the real /dev/ptmx char device is deleted and replaced, breaking PTY allocation for non-root users on systems with ptmxmode=000.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-N6TD9MF6.

---

**Reference:** ANT-2026-N6TD9MF6

Triage and disclosure were performed by Ada Logics.

```
diff --git a/internal/pathrs/mkdirall.go b/internal/pathrs/mkdirall.go
index 81c9a022c74..31cc08579e2 100644
--- a/internal/pathrs/mkdirall.go
+++ b/internal/pathrs/mkdirall.go
@@ -24,6 +24,14 @@ import (
 	"path/filepath"
 )

+func splitPath(path string) (dirPath, filename string, err error) {
+	dirPath, filename = filepath.Split(path)
+	if filepath.Join("/", filename) == "/" {
+		return "", "", fmt.Errorf("root subpath %q has bad trailing component %q", path, filename)
+	}
+	return dirPath, filename, nil
+}
+
 // MkdirAllParentInRoot is like [MkdirAllInRoot] except that it only creates
 // the parent directory of the target path, returning the trailing component so
 // the caller has more flexibility around constructing the final inode.
@@ -41,9 +49,9 @@ func MkdirAllParentInRoot(root *os.File, unsafePath string, mode os.FileMode) (*
 		return nil, "", fmt.Errorf("failed to construct hallucinated target path: %w", err)

-	dirPath, filename := filepath.Split(unsafePath)
-	if filepath.Join("/", filename) == "/" {
-		return nil, "", fmt.Errorf("create parent dir in root subpath %q has bad trailing component %q", unsafePath, filename)
+	dirPath, filename, err := splitPath(unsafePath)
+	if err != nil {
+		return nil, "", fmt.Errorf("split path %q for mkdir parent: %w", unsafePath, err)

 	dirFd, err := MkdirAllInRoot(root, dirPath, mode)
diff --git a/internal/pathrs/root_pathrslite.go b/internal/pathrs/root_pathrslite.go
index 0ddabf80429..fc5114a856b 100644
--- a/internal/pathrs/root_pathrslite.go
+++ b/internal/pathrs/root_pathrslite.go
@@ -19,7 +19,9 @@
 package pathrs

 import (
+	"fmt"
 	"os"
+	"path/filepath"

 	"github.com/cyphar/filepath-securejoin/pathrs-lite"
 	"golang.org/x/sys/unix"
@@ -65,3 +67,46 @@ func CreateInRoot(root *os.File, subpath string, flags int, fileMode uint32) (*o
 	return os.NewFile(uintptr(fd), root.Name()+"/"+subpath), nil
+
+// UnlinkInRoot deletes the inode specified at the given subpath. If you pass
+// [unix.AT_REMOVEDIR] it will remove directories, otherwise it will remove
+// non-directory inodes.
+func UnlinkInRoot(root *os.File, subpath string, flags int) error {
+	dirPath, filename, err := splitPath(subpath)
+	if err != nil {
+		return fmt.Errorf("split path %q for unlink: %w", subpath, err)
+	}
+
+	dirFd := root
+	if filepath.Join("/", dirPath) != "/" {
+		newDirFd, err := OpenInRoot(root, dirPath, unix.O_DIRECTORY|unix.O_PATH)
+		if err != nil {
+			return fmt.Errorf("failed to open parent directory %q for unlink: %w", dirPath, err)
+		}
+		dirFd = newDirFd
+		defer dirFd.Close()
+	}
+
+	err = unix.Unlinkat(int(dirFd.Fd()), filename, flags)
+	if err != nil {
+		err = &os.PathError{Op: "unlinkat", Path: dirFd.Name() + "/" + filename, Err: err}
+	}
+	return err
+}
+
+// SymlinkInRoot creates a symlink inside a root with the given target (as well
+// as creating any missing parent directories). If the subpath already exists,
+// an error is returned.
+func SymlinkInRoot(linktarget string, root *os.File, subpath string) error {
+	dirFd, filename, err := MkdirAllParentInRoot(root, subpath, 0o755)
+	if err != nil {
+		return err
+	}
+	defer dirFd.Close()
+
+	err = unix.Symlinkat(linktarget, int(dirFd.Fd()), filename)
+	if err != nil {
+		err = &os.PathError{Op: "symlinkat", Path: dirFd.Name() + "/" + filename, Err: err}
+	}
+	return err
+}
diff --git a/libcontainer/rootfs_linux.go b/libcontainer/rootfs_linux.go
index 8bd5d1ef8c8..7accf3648a6 100644
--- a/libcontainer/rootfs_linux.go
+++ b/libcontainer/rootfs_linux.go
@@ -97,6 +97,19 @@ func needsSetupDev(config *configs.Config) bool {
 	return true

+func doSetupDev(rootFd *os.File, config *configs.Config) error {
+	if err := createDevices(rootFd, config); err != nil {
+		return fmt.Errorf("error creating device nodes: %w", err)
+	}
+	if err := setupPtmx(rootFd); err != nil {
+		return fmt.Errorf("error setting up ptmx: %w", err)
+	}
+	if err := setupDevSymlinks(rootFd); err != nil {
+		return fmt.Errorf("error setting up /dev symlinks: %w", err)
+	}
+	return nil
+}
+
 // setupAndMountToRootfs sets up the mount for a single mount point and mounts it to the rootfs.
 func setupAndMountToRootfs(pipe *syncSocket, config *configs.Config, mountConfig *mountConfig, m *configs.Mount) error {
 	entry := mountEntry{Mount: m}
@@ -184,14 +197,8 @@ func prepareRootfs(pipe *syncSocket, iConfig *initConfig) (err error) {

 	setupDev := needsSetupDev(config)
 	if setupDev {
-		if err := createDevices(rootFd, config); err != nil {
-			return fmt.Errorf("error creating device nodes: %w", err)
-		}
-		if err := setupPtmx(config); err != nil {
-			return fmt.Errorf("error setting up ptmx: %w", err)
-		}
-		if err := setupDevSymlinks(config.Rootfs); err != nil {
-			return fmt.Errorf("error setting up /dev symlinks: %w", err)
+		if err := doSetupDev(rootFd, config); err != nil {
+			return fmt.Errorf("configuring container /dev: %w", err)

@@ -893,7 +900,7 @@ func checkProcMount(rootfs, dest string, m mountEntry) error {
 	return fmt.Errorf("%q cannot be mounted because it is inside /proc", dest)

-func setupDevSymlinks(rootfs string) error {
+func setupDevSymlinks(rootFd *os.File) error {
 	// In theory, these should be links to /proc/thread-self, but systems
 	// expect these to be /proc/self and this matches how most distributions
 	// work.
@@ -909,11 +916,8 @@ func setupDevSymlinks(rootfs string) error {
 		links = append(links, [2]string{"/proc/kcore", "/dev/core"})
 	for _, link := range links {
-		var (
-			src = link[0]
-			dst = filepath.Join(rootfs, link[1])
-		)
-		if err := os.Symlink(src, dst); err != nil && !errors.Is(err, os.ErrExist) {
+		target, devName := link[0], link[1]
+		if err := pathrs.SymlinkInRoot(target, rootFd, devName); err != nil && !errors.Is(err, os.ErrExist) {
 			return err
@@ -1129,15 +1133,11 @@ func setReadonly() error {
 	return mount("", "/", "", flags, "")

-func setupPtmx(config *configs.Config) error {
-	ptmx := filepath.Join(config.Rootfs, "dev/ptmx")
-	if err := os.Remove(ptmx); err != nil && !errors.Is(err, os.ErrNotExist) {
+func setupPtmx(rootFd *os.File) error {
+	if err := pathrs.UnlinkInRoot(rootFd, "/dev/ptmx", 0); err != nil && !errors.Is(err, os.ErrNotExist) {
 		return err
-	if err := os.Symlink("pts/ptmx", ptmx); err != nil {
-		return err
-	}
-	return nil
+	return pathrs.SymlinkInRoot("pts/ptmx", rootFd, "/dev/ptmx")

 // pivotRoot will call pivot_root such that rootfs becomes the new root
```

<https://github.com/opencontainers/runc/commit/864db8042dbb191028676f80addf8c35f348aee2>

1. 2026-04-09
2. 2026-04-16
3. 2026-06-13
4. 2026-08-17

9208b5c16f124f4133ecf196cfb0a749223196aaab8e2a859cbb2cd13a594b6681e743b3ef14eecd894e9c2a805ed3e2949ee01d5288459576a46d6416469d42

Committed 2026-04-16 15:59 UTC

Revealed 2026-08-17 17:47 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-N6TD9MF6%22%2C%22bug_class%22%3A%22Symlink-following%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-09T05%3A38%3A25%2B00%3A00%22%2C%22description%22%3A%22In%20libcontainer/rootfs_linux.go%2C%20prepareRootfs%28%29%20mounts%20the%20/dev%20tmpfs%20and%20creates%20device%20nodes%20using%20safe%20RESOLVE_IN_ROOT%20fd-relative%20operations%2C%20which%20follow%20a%20/dev%20symlink%20scoped%20inside%20the%20rootfs%20and%20leave%20the%20symlink%20itself%20intact.%20Immediately%20after%2C%20setupPtmx%28%29%20and%20setupDevSymlinks%28%29%20call%20filepath.Join%28rootfs%2C%20%5C%22dev/...%5C%22%29%20with%20os.Remove/os.Symlink%2C%20which%20the%20kernel%20resolves%20without%20scoping%20%E2%80%94%20following%20an%20absolute%20/dev%20symlink%20out%20to%20the%20host%20filesystem.%20This%20runs%20as%20host%20root%20and%20before%20pivot_root%2C%20while%20the%20mount%20namespace%20still%20mirrors%20the%20host.%20An%20attacker%20who%20authors%20a%20container%20image%20with%20/dev%20as%20a%20symlink%20to%20an%20arbitrary%20absolute%20host%20directory%20causes%20runc%20to%20create%20fixed-name%20symlinks%20%28ptmx%2C%20fd%2C%20stdin%2C%20stdout%2C%20stderr%2C%20core%29%20in%20that%20host%20directory.%20Pointing%20/dev%20at%20host%20/dev%20deletes%20and%20replaces%20the%20real%20/dev/ptmx%2C%20breaking%20PTY%20allocation%20host-wide.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3A%22libcontainer/rootfs_linux.go%3A1125%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22runc%22%2C%22reproduction%22%3A%5B%221.%20Build%20an%20OCI%20rootfs%20where%20/dev%20is%20a%20symlink%20to%20an%20absolute%20host%20path%20%28e.g.%20/etc%20or%20/dev%29%20and%20a%20real%20directory%20exists%20at%20that%20path%20inside%20the%20rootfs%20so%20scoped%20resolution%20succeeds.%22%2C%222.%20Push%20the%20image%3B%20victim%20pulls%20and%20runs%20it%20with%20standard%20config.json%20%28tmpfs%20on%20/dev%29.%22%2C%223.%20prepareRootfs%20mounts%20tmpfs%20onto%20the%20scoped%20target%20%28%3Crootfs%3E/%3Ctarget%3E%29%20via%20openat2%20RESOLVE_IN_ROOT%2C%20leaving%20the%20%3Crootfs%3E/dev%20symlink%20untouched.%22%2C%224.%20setupPtmx%28%29%20does%20os.Remove%20%2B%20os.Symlink%20on%20%5C%22%3Crootfs%3E/dev/ptmx%5C%22%3B%20kernel%20follows%20the%20absolute%20symlink%20unscoped%20and%20creates%20/%3Ctarget%3E/ptmx%20-%3E%20pts/ptmx%20on%20the%20host.%22%2C%225.%20setupDevSymlinks%28%29%20likewise%20creates%20fd%2C%20stdin%2C%20stdout%2C%20stderr%2C%20core%20symlinks%20in%20the%20host%20target%20directory.%22%2C%226.%20If%20target%20is%20host%20/dev%2C%20the%20real%20/dev/ptmx%20char%20device%20is%20deleted%20and%20replaced%2C%20breaking%20PTY%20allocation%20for%20non-root%20users%20on%20systems%20with%20ptmxmode%3D000.%22%5D%2C%22technical_details%22%3A%22Built%20runc%20at%20HEAD%20%287a1cae6dd%29.%20Created%20an%20OCI%20bundle%20whose%20rootfs/dev%20is%20a%20symlink%20to%20an%20absolute%20path%20/tmp/host-sentinel-408%20%28a%20directory%20OUTSIDE%20the%20rootfs%2C%20on%20the%20%27host%27%20%E2%80%94%20here%20the%20outer%20privileged%20Docker%20container%29.%20The%20bundle%20uses%20the%20standard%20tmpfs%20/dev%20mount.%20Ran%20%60runc%20run%60.%20The%20container%20started%20successfully%20%28exit%200%29.%20After%20the%20run%2C%20/tmp/host-sentinel-408%20contained%20five%20new%20symlinks%3A%20ptmx%E2%86%92pts/ptmx%2C%20fd%E2%86%92/proc/self/fd%2C%20stdin%E2%86%92/proc/self/fd/0%2C%20stdout%E2%86%92/proc/self/fd/1%2C%20stderr%E2%86%92/proc/self/fd/2.%20These%20were%20created%20by%20setupPtmx%28%29%20and%20setupDevSymlinks%28%29%20in%20libcontainer/rootfs_linux.go%2C%20which%20use%20filepath.Join%28rootfs%2C%5C%22dev/...%5C%22%29%2Bos.Symlink%20%E2%80%94%20the%20kernel%20followed%20the%20absolute%20symlink%20at%20rootfs/dev%20unscoped%2C%20landing%20outside%20the%20rootfs%2C%20before%20pivot_root.%20The%20safe%20pathrs-based%20/dev%20tmpfs%20mount%20followed%20the%20symlink%20SCOPED%20%28to%20rootfs/tmp/host-sentinel-408%29%2C%20leaving%20the%20rootfs/dev%20symlink%20itself%20intact%20for%20the%20unsafe%20calls%20to%20follow.%20This%20is%20a%20host-filesystem%20write%20from%20a%20malicious%20container%20image%20with%20no%20privileges%20beyond%20image%20authorship.%22%2C%22title%22%3A%22Host%20filesystem%20write%20via%20/dev%20symlink%20in%20container%20image%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-N6TD9MF6",
  "bug_class": "Symlink-following",
  "created_at": "2026-04-09T05:38:25+00:00",
  "description": "In libcontainer/rootfs_linux.go, prepareRootfs() mounts the /dev tmpfs and creates device nodes using safe RESOLVE_IN_ROOT fd-relative operations, which follow a /dev symlink scoped inside the rootfs and leave the symlink itself intact. Immediately after, setupPtmx() and setupDevSymlinks() call filepath.Join(rootfs, \"dev/...\") with os.Remove/os.Symlink, which the kernel resolves without scoping — following an absolute /dev symlink out to the host filesystem. This runs as host root and before pivot_root, while the mount namespace still mirrors the host. An attacker who authors a container image with /dev as a symlink to an arbitrary absolute host directory causes runc to create fixed-name symlinks (ptmx, fd, stdin, stdout, stderr, core) in that host directory. Pointing /dev at host /dev deletes and replaces the real /dev/ptmx, breaking PTY allocation host-wide.",
  "location": "libcontainer/rootfs_linux.go:1125",
  "project": "runc",
    "1. Build an OCI rootfs where /dev is a symlink to an absolute host path (e.g. /etc or /dev) and a real directory exists at that path inside the rootfs so scoped resolution succeeds.",
    "2. Push the image; victim pulls and runs it with standard config.json (tmpfs on /dev).",
    "3. prepareRootfs mounts tmpfs onto the scoped target (<rootfs>/<target>) via openat2 RESOLVE_IN_ROOT, leaving the <rootfs>/dev symlink untouched.",
    "4. setupPtmx() does os.Remove + os.Symlink on \"<rootfs>/dev/ptmx\"; kernel follows the absolute symlink unscoped and creates /<target>/ptmx -> pts/ptmx on the host.",
    "5. setupDevSymlinks() likewise creates fd, stdin, stdout, stderr, core symlinks in the host target directory.",
    "6. If target is host /dev, the real /dev/ptmx char device is deleted and replaced, breaking PTY allocation for non-root users on systems with ptmxmode=000."
  "technical_details": "Built runc at HEAD (7a1cae6dd). Created an OCI bundle whose rootfs/dev is a symlink to an absolute path /tmp/host-sentinel-408 (a directory OUTSIDE the rootfs, on the 'host' — here the outer privileged Docker container). The bundle uses the standard tmpfs /dev mount. Ran `runc run`. The container started successfully (exit 0). After the run, /tmp/host-sentinel-408 contained five new symlinks: ptmx→pts/ptmx, fd→/proc/self/fd, stdin→/proc/self/fd/0, stdout→/proc/self/fd/1, stderr→/proc/self/fd/2. These were created by setupPtmx() and setupDevSymlinks() in libcontainer/rootfs_linux.go, which use filepath.Join(rootfs,\"dev/...\")+os.Symlink — the kernel followed the absolute symlink at rootfs/dev unscoped, landing outside the rootfs, before pivot_root. The safe pathrs-based /dev tmpfs mount followed the symlink SCOPED (to rootfs/tmp/host-sentinel-408), leaving the rootfs/dev symlink itself intact for the unsafe calls to follow. This is a host-filesystem write from a malicious container image with no privileges beyond image authorship.",
  "title": "Host filesystem write via /dev symlink in container image",
```
