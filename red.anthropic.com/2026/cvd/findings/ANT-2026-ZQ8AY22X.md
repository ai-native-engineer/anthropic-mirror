<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-ZQ8AY22X -->

# ANT-2026-ZQ8AY22X · craftcms/cms

## privilege-escalation high

[GHSA-cc7p-2j3x-x7xf](https://github.com/advisories/GHSA-cc7p-2j3x-x7xf)

Security research firm -
Maintainer high

Anthropic's analysis of this finding, sealed at approval.

# ANT-2026-ZQ8AY22X: Privilege Escalation/Bypass through UsersController->actionImpersonateWithToken()

Craft CMS's actionPreview() re-dispatches requests with $skipSpecialHandling=true and $checkToken=false, allowing an attacker-supplied action query parameter to redirect execution to UsersController::actionImpersonateWithToken(). That endpoint's only guard, requireToken(), merely checks the boolean \_hadToken set when the preview token was resolved, without verifying the token was minted for impersonation. Because the action is also listed in $allowAnonymous, no prior authentication is enforced. An editor (or anyone holding a shared preview URL) can therefore append &action=users/impersonate-with-token&userId=1&prevUserId=1 to a preview URL and be logged in as user 1 (admin).

**Project:** craftcms/cms

Root cause is a confused-deputy between the preview dispatcher and the impersonation endpoint: actionPreview() passes $skipSpecialHandling=true to handleRequest() and $checkToken=false to checkIfActionRequest(), so security guards are skipped and the action parameter is attacker-controlled. requireToken() on actionImpersonateWithToken() only inspects \_hadToken (set for any valid token) rather than validating that the token was issued for this route, and the action is in $allowAnonymous, so no further authorization occurs.

This finding was identified by static analysis and has not yet been dynamically reproduced. The Technical Details section above describes the code path; a trigger input is not included.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-ZQ8AY22X.

---

**Reference:** ANT-2026-ZQ8AY22X

```
diff --git a/CHANGELOG.md b/CHANGELOG.md
index 9a940756613..ddca7497e41 100644
--- a/CHANGELOG.md
+++ b/CHANGELOG.md
@@ -1,5 +1,11 @@
 # Release Notes for Craft CMS 4

+## Unreleased
+
+- Added `craft\services\Tokens::getRemainingTokenUsages()`.
+- Added `craft\web\Request::getTokenRoute()`.
+- Fixed a [high-severity](https://github.com/craftcms/cms/security/policy#severity--remediation) permission escalation vulnerability. (GHSA-cc7p-2j3x-x7xf)
+
 ## 4.17.5 - 2026-02-17

 - Added `craft\web\Request::getWantsImage()`.
diff --git a/src/helpers/UrlHelper.php b/src/helpers/UrlHelper.php
index c29f01f2a6a..737b3b90443 100644
--- a/src/helpers/UrlHelper.php
+++ b/src/helpers/UrlHelper.php
@@ -658,9 +658,15 @@ private static function _createUrl(
                 $params[$generalConfig->siteToken] = $siteToken;
             if ($request->getIsSiteRequest()) {
-                if ($addToken && !isset($params[$generalConfig->tokenParam]) && ($token = $request->getToken()) !== null) {
+                if (
+                    $addToken &&
+                    !isset($params[$generalConfig->tokenParam]) &&
+                    ($token = $request->getToken()) !== null &&
+                    Craft::$app->getTokens()->getRemainingTokenUsages($token) !== 0
+                ) {
                     $params[$generalConfig->tokenParam] = $token;
+
                 if (
                     !isset($params['x-craft-preview']) &&
                     !isset($params['x-craft-live-preview']) &&
diff --git a/src/services/Tokens.php b/src/services/Tokens.php
index 37dff3c34b0..a3cb272a6d7 100644
--- a/src/services/Tokens.php
+++ b/src/services/Tokens.php
@@ -34,6 +34,12 @@ class Tokens extends Component
      */
     private bool $_deletedExpiredTokens = false;

+    /**
+     * @var array<string,int|null>
+     * @see getRemainingTokenUsages()
+     */
+    private array $_remainingTokenUsages = [];
+
     /**
      * Creates a new token and returns it.
      * ---
@@ -137,24 +143,25 @@ public function getTokenRoute(string $token): array|false
                 ->one();

             if (!$result) {
-                // Remove it from the request  so it doesn’t get added to generated URLs
-                Craft::$app->getRequest()->setToken(null);
+                $this->_remainingTokenUsages[$token] = 0;
                 return false;

             // Usage limit enforcement (for future requests)
             if ($result['usageLimit']) {
                 // Does it have any more life after this?
-                if ($result['usageCount'] < $result['usageLimit'] - 1) {
+                $newUsageCount = $result['usageCount'] + 1;
+                if ($newUsageCount < $result['usageLimit']) {
                     // Increment its count
                     $this->incrementTokenUsageCountById($result['id']);
+                    $this->_remainingTokenUsages[$token] = $result['usageLimit'] - $newUsageCount;
                 } else {
                     // Just delete it
                     $this->deleteTokenById($result['id']);
-
-                    // Remove it from the request as well so it doesn’t get added to generated URLs
-                    Craft::$app->getRequest()->setToken(null);
+                    $this->_remainingTokenUsages[$token] = 0;
+            } else {
+                $this->_remainingTokenUsages[$token] = null;

             return (array)Json::decodeIfJson($result['route']);
@@ -163,6 +170,36 @@ public function getTokenRoute(string $token): array|false

+    /**
+     * Returns the remaining usage count for a given token, if it has a limit.
+     *
+     * @param string $token
+     * @return int|null
+     * @since 4.17.6
+     */
+    public function getRemainingTokenUsages(string $token): ?int
+    {
+        if (!array_key_exists($token, $this->_remainingTokenUsages)) {
+            $result = (new Query())
+                ->select(['usageLimit', 'usageCount'])
+                ->from([Table::TOKENS])
+                ->where(['token' => $token])
+                ->one();
+
+            if ($result) {
+                if ($result['usageLimit']) {
+                    $this->_remainingTokenUsages[$token] = $result['usageLimit'] - $result['usageCount'];
+                } else {
+                    $this->_remainingTokenUsages[$token] = null;
+                }
+            } else {
+                $this->_remainingTokenUsages[$token] = 0;
+            }
+        }
+
+        return $this->_remainingTokenUsages[$token];
+    }
+
     /**
      * Increments a token's usage count.
      *
diff --git a/src/web/Controller.php b/src/web/Controller.php
index a5c16a9281f..9c7b5f9da63 100644
--- a/src/web/Controller.php
+++ b/src/web/Controller.php
@@ -526,7 +526,8 @@ public function requireAcceptsJson(): void
      */
     public function requireToken(): void
-        if (!$this->request->getHadToken()) {
+        $tokenRoute = $this->request->getTokenRoute()[0] ?? null;
+        if ($tokenRoute !== $this->getRoute()) {
             throw new BadRequestHttpException('Valid token required');
diff --git a/src/web/Request.php b/src/web/Request.php
index f854e2081a2..a5b36d5730a 100644
--- a/src/web/Request.php
+++ b/src/web/Request.php
@@ -17,6 +17,7 @@
 use craft\helpers\StringHelper;
 use craft\models\Site;
 use craft\services\Sites;
+use craft\services\Tokens;
 use yii\base\InvalidArgumentException;
 use yii\base\InvalidConfigException;
 use yii\db\Exception as DbException;
@@ -197,6 +198,12 @@ class Request extends \yii\web\Request
      */
     public ?string $_token = null;

+    /**
+     * @var array|null
+     * @see getTokenRoute()
+     */
+    public ?array $_tokenRoute = null;
+
     /**
      * @inheritdoc
      */
@@ -510,7 +517,7 @@ public function getHadToken(): bool
      *
      * @return string|null The token, or `null` if there isn’t one.
      * @throws BadRequestHttpException if an invalid token is supplied
-     * @see \craft\services\Tokens::createToken()
+     * @see Tokens::createToken()
      * @see Controller::requireToken()
      */
     public function getToken(): ?string
@@ -519,6 +526,21 @@ public function getToken(): ?string
         return $this->_token;

+    /**
+     * Returns the route the request’s token resolves to.
+     *
+     * @return array|null The route, or `null` if there isn’t one.
+     * @throws BadRequestHttpException if an invalid token is supplied
+     * @see getToken())
+     * @see Tokens::createToken()
+     * @since 4.17.6
+     */
+    public function getTokenRoute(): ?array
+    {
+        $this->_findToken();
+        return $this->_tokenRoute;
+    }
+
     /**
      * Sets the token value.
      *
@@ -549,10 +571,17 @@ private function _findToken(): void

         $this->_token = ($this->getQueryParam($this->generalConfig->tokenParam) ?? $this->getHeaders()->get('X-Craft-Token')) ?: null;

-        if ($this->_token && !preg_match('/^[A-Za-z0-9_-]+$/', $this->_token)) {
-            $this->_token = null;
-            $this->_hadToken = false;
-            throw new BadRequestHttpException('Invalid token');
+        if ($this->_token) {
+            if (!preg_match('/^[A-Za-z0-9_-]+$/', $this->_token)) {
+                $this->_token = null;
+                $this->_hadToken = false;
+                throw new BadRequestHttpException('Invalid token');
+            }
+
+            $this->_tokenRoute = Craft::$app->getTokens()->getTokenRoute($this->_token) ?: null;
+            if (!$this->_tokenRoute) {
+                $this->_token = null;
+            }

         $this->_hadToken = isset($this->_token);
diff --git a/src/web/UrlManager.php b/src/web/UrlManager.php
index 9af83c76b5d..4c3e2f9b0a2 100644
--- a/src/web/UrlManager.php
+++ b/src/web/UrlManager.php
@@ -548,6 +548,7 @@ private function _getTokenRoute(Request $request): array|false

         $token = $request->getToken();
+        $route = $request->getTokenRoute();

         if (App::devMode()) {
             Craft::debug([
@@ -557,10 +558,6 @@ private
… (truncated)
```

<https://github.com/craftcms/cms/commit/6301e217c5f15617d939c432cb770db50af14b33>

ADVISORY

<https://github.com/craftcms/cms/security/advisories/GHSA-cc7p-2j3x-x7xf>

1. 2026-02-18
2. 2026-02-18
3. 2026-03-29
4. 2026-05-08
5. 2026-05-20

dc75439eef02f2f72ba1440db7ca5fbae9599c252caba20b38f6b5c634fae74db645c91470b08c00012cc38b7353a9a7f79f52cf703bb1a668c6df7682c8907f

Committed 2026-05-08 16:37 UTC

Revealed 2026-05-20 07:40 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-ZQ8AY22X%22%2C%22bug_class%22%3A%22privilege-escalation%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-03-29T20%3A43%3A35%2B00%3A00%22%2C%22description%22%3A%22Craft%20CMS%27s%20actionPreview%28%29%20re-dispatches%20requests%20with%20%24skipSpecialHandling%3Dtrue%20and%20%24checkToken%3Dfalse%2C%20allowing%20an%20attacker-supplied%20action%20query%20parameter%20to%20redirect%20execution%20to%20UsersController%3A%3AactionImpersonateWithToken%28%29.%20That%20endpoint%27s%20only%20guard%2C%20requireToken%28%29%2C%20merely%20checks%20the%20boolean%20_hadToken%20set%20when%20the%20preview%20token%20was%20resolved%2C%20without%20verifying%20the%20token%20was%20minted%20for%20impersonation.%20Because%20the%20action%20is%20also%20listed%20in%20%24allowAnonymous%2C%20no%20prior%20authentication%20is%20enforced.%20An%20editor%20%28or%20anyone%20holding%20a%20shared%20preview%20URL%29%20can%20therefore%20append%20%26action%3Dusers/impersonate-with-token%26userId%3D1%26prevUserId%3D1%20to%20a%20preview%20URL%20and%20be%20logged%20in%20as%20user%201%20%28admin%29.%22%2C%22discovered_at%22%3Anull%2C%22location%22%3Anull%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22CraftCMS%22%2C%22reproduction%22%3Anull%2C%22technical_details%22%3A%22Root%20cause%20is%20a%20confused-deputy%20between%20the%20preview%20dispatcher%20and%20the%20impersonation%20endpoint%3A%20actionPreview%28%29%20passes%20%24skipSpecialHandling%3Dtrue%20to%20handleRequest%28%29%20and%20%24checkToken%3Dfalse%20to%20checkIfActionRequest%28%29%2C%20so%20security%20guards%20are%20skipped%20and%20the%20action%20parameter%20is%20attacker-controlled.%20requireToken%28%29%20on%20actionImpersonateWithToken%28%29%20only%20inspects%20_hadToken%20%28set%20for%20any%20valid%20token%29%20rather%20than%20validating%20that%20the%20token%20was%20issued%20for%20this%20route%2C%20and%20the%20action%20is%20in%20%24allowAnonymous%2C%20so%20no%20further%20authorization%20occurs.%22%2C%22title%22%3A%22Privilege%20Escalation/Bypass%20through%20UsersController-%3EactionImpersonateWithToken%28%29%22%2C%22vendor_severity%22%3Anull%7D)

```
  "ant_id": "ANT-2026-ZQ8AY22X",
  "bug_class": "privilege-escalation",
  "created_at": "2026-03-29T20:43:35+00:00",
  "description": "Craft CMS's actionPreview() re-dispatches requests with $skipSpecialHandling=true and $checkToken=false, allowing an attacker-supplied action query parameter to redirect execution to UsersController::actionImpersonateWithToken(). That endpoint's only guard, requireToken(), merely checks the boolean _hadToken set when the preview token was resolved, without verifying the token was minted for impersonation. Because the action is also listed in $allowAnonymous, no prior authentication is enforced. An editor (or anyone holding a shared preview URL) can therefore append &action=users/impersonate-with-token&userId=1&prevUserId=1 to a preview URL and be logged in as user 1 (admin).",
  "location": null,
  "project": "CraftCMS",
  "technical_details": "Root cause is a confused-deputy between the preview dispatcher and the impersonation endpoint: actionPreview() passes $skipSpecialHandling=true to handleRequest() and $checkToken=false to checkIfActionRequest(), so security guards are skipped and the action parameter is attacker-controlled. requireToken() on actionImpersonateWithToken() only inspects _hadToken (set for any valid token) rather than validating that the token was issued for this route, and the action is in $allowAnonymous, so no further authorization occurs.",
  "title": "Privilege Escalation/Bypass through UsersController->actionImpersonateWithToken()",
  "vendor_severity": null
```
