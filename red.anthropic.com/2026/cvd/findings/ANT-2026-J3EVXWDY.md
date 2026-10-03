<!-- source: https://red.anthropic.com/2026/cvd/findings/ANT-2026-J3EVXWDY -->

# ANT-2026-J3EVXWDY · twigphp/twig

## code-injection critical

[CVE-2026-46633](https://nvd.nist.gov/vuln/detail/CVE-2026-46633)
[GHSA-7p85-w9px-jpjp](https://github.com/advisories/GHSA-7p85-w9px-jpjp)

Maintainer critical

Anthropic's analysis, sealed at approval. Disclosure to the maintainer was performed by Anvil Security.

# ANT-2026-J3EVXWDY: PHP code injection via single quote in {% use %} template name

In ModuleNode::compileConstructor() (lines 251-255), the error message for an undefined trait block is built by writing a single-quoted PHP string and interpolating the trait template name via subcompile(). Compiler::string() escapes double quotes and backslashes but not single quotes, and UseTokenParser accepts arbitrary template-name strings. A single quote in the {% use %} template name therefore closes the surrounding PHP string literal and drops the attacker into PHP expression context inside the generated \_\_construct(). Because this code runs before the sandbox security check (and 'use' is always permitted anyway), an attacker who can author templates and control template names achieves arbitrary PHP execution and sandbox escape.

**Project:** twigphp/twig
**Location:** `src/Node/ModuleNode.php:254`

The compiler opens a single-quoted PHP literal with ->write("throw new RuntimeError('Block ") and does not close it before subcompiling the trait template-name node; Compiler::string() uses addcslashes on \0\t\"\$\ only, so single quotes pass through unescaped. A template name containing ' terminates the outer string and the remainder is parsed as live PHP expression code. Lines 235-237 in the same function handle a similar case correctly by closing and reopening the quoted literal around the subcompile.

1. Create a template in the loader named '.system('id').' containing {% block x %}{% endblock %}
2. Create a second template containing: {% use "'.system('id').'" with foo as bar %}
3. Compilation emits: throw new RuntimeError('Block "foo" is not defined in trait "'.system('id').'".', 1, $this->source);
4. Render the second template; instantiating the compiled class runs \_\_construct() and executes the injected system() call before any sandbox check

## Suggested Fix

Ensure values emitted via Compiler::string()/repr() are only placed where a standalone double-quoted PHP literal is valid; in compileConstructor(), close the surrounding single-quoted literal before subcompiling the ConstantExpression and reopen it afterward, mirroring the correct pattern at lines 235-237.

This vulnerability was discovered by Claude, Anthropic's AI assistant, and triaged by the Anthropic security team in collaboration with Anthropic Research. Please direct questions to security-cvd@anthropic.com and reference ANT-2026-J3EVXWDY.

---

**Reference:** ANT-2026-J3EVXWDY

Triage and disclosure were performed by Anvil Security.

The change that resolved this finding.

```
diff --git a/src/Node/ModuleNode.php b/src/Node/ModuleNode.php
index 71c57201982..a3f66827ff6 100644
--- a/src/Node/ModuleNode.php
+++ b/src/Node/ModuleNode.php
@@ -248,11 +248,11 @@ protected function compileConstructor(Compiler $compiler)
                         ->string($key)
                         ->raw("])) {\n")
                         ->indent()
-                        ->write("throw new RuntimeError('Block ")
+                        ->write("throw new RuntimeError(sprintf('Block \"%s\" is not defined in trait \"%s\".', ")
                         ->string($key)
-                        ->raw(' is not defined in trait ')
+                        ->raw(', ')
                         ->subcompile($trait->getNode('template'))
-                        ->raw(".', ")
+                        ->raw('), ')
                         ->repr($node->getTemplateLine())
                         ->raw(", \$this->source);\n")
                         ->outdent()
diff --git a/tests/Node/ModuleTest.php b/tests/Node/ModuleTest.php
index df28815c569..b8df54f77e7 100644
--- a/tests/Node/ModuleTest.php
+++ b/tests/Node/ModuleTest.php
@@ -21,6 +21,7 @@
  */

 use Twig\Environment;
+use Twig\Error\RuntimeError;
 use Twig\Loader\ArrayLoader;
 use Twig\Node\BodyNode;
 use Twig\Node\EmptyNode;
@@ -56,6 +57,29 @@ public function testConstructor()
         $this->assertEquals($source->getName(), $node->getTemplateName());

+    public function testUseTagTemplateNameDoesNotInjectPhpInCompiledOutput()
+    {
+        $evilName = "evil' . print('BAD-EOL') . '.twig";
+        $loader = new ArrayLoader([
+            $evilName => '{% block existing %}ok{% endblock %}',
+            'main.twig' => "{% use \"$evilName\" with absent_block as alias %}",
+        ]);
+        $twig = new Environment($loader);
+
+        ob_start();
+        $message = null;
+        try {
+            $twig->load('main.twig');
+        } catch (RuntimeError $e) {
+            $message = $e->getMessage();
+        }
+        $stdout = ob_get_clean();
+
+        $this->assertSame('', $stdout, 'No code from the template name must execute when the trait is loaded.');
+        $this->assertNotNull($message, 'A RuntimeError must be raised for the missing block.');
+        $this->assertStringContainsString($evilName, $message, 'The error message must contain the literal template name.');
+    }
+
     public static function provideTests(): iterable
         $twig = new Environment(new ArrayLoader(['foo.twig' => '{{ foo }}']));
```

<https://github.com/twigphp/Twig/commit/e9ff55f6910832428e48a35b2e0748189ad49ae3>

1. 2026-04-19
2. 2026-04-28
3. 2026-04-28
4. 2026-05-19
5. 2026-08-17

93b28dc10565abff791346a81f85dd6ab280b8d67795c451349092fc8cacd8d74fa1efe5ea8621424843330fcf14161d7bd1d3108e0fd946afbe9cba8e5d9d2f

Committed 2026-05-19 21:41 UTC

Revealed 2026-08-17 17:47 UTC

[Verify (download preimage.json)](data:application/json;charset=utf-8,%7B%22ant_id%22%3A%22ANT-2026-J3EVXWDY%22%2C%22bug_class%22%3A%22code_injection%22%2C%22claude_severity%22%3A%22high%22%2C%22commit_sha%22%3Anull%2C%22created_at%22%3A%222026-04-21T16%3A56%3A59%2B00%3A00%22%2C%22description%22%3A%22In%20ModuleNode%3A%3AcompileConstructor%28%29%20%28lines%20251-255%29%2C%20the%20error%20message%20for%20an%20undefined%20trait%20block%20is%20built%20by%20writing%20a%20single-quoted%20PHP%20string%20and%20interpolating%20the%20trait%20template%20name%20via%20subcompile%28%29.%20Compiler%3A%3Astring%28%29%20escapes%20double%20quotes%20and%20backslashes%20but%20not%20single%20quotes%2C%20and%20UseTokenParser%20accepts%20arbitrary%20template-name%20strings.%20A%20single%20quote%20in%20the%20%7B%25%20use%20%25%7D%20template%20name%20therefore%20closes%20the%20surrounding%20PHP%20string%20literal%20and%20drops%20the%20attacker%20into%20PHP%20expression%20context%20inside%20the%20generated%20__construct%28%29.%20Because%20this%20code%20runs%20before%20the%20sandbox%20security%20check%20%28and%20%27use%27%20is%20always%20permitted%20anyway%29%2C%20an%20attacker%20who%20can%20author%20templates%20and%20control%20template%20names%20achieves%20arbitrary%20PHP%20execution%20and%20sandbox%20escape.%22%2C%22discovered_at%22%3A%222026-04-19T00%3A00%3A00%2B00%3A00%22%2C%22location%22%3A%22src/Node/ModuleNode.php%3A254%22%2C%22poc_sha256%22%3Anull%2C%22preimage_version%22%3A1%2C%22project%22%3A%22twigphp/Twig%22%2C%22reproduction%22%3A%5B%22Create%20a%20template%20in%20the%20loader%20named%20%27.system%28%27id%27%29.%27%20containing%20%7B%25%20block%20x%20%25%7D%7B%25%20endblock%20%25%7D%22%2C%22Create%20a%20second%20template%20containing%3A%20%7B%25%20use%20%5C%22%27.system%28%27id%27%29.%27%5C%22%20with%20foo%20as%20bar%20%25%7D%22%2C%22Compilation%20emits%3A%20throw%20new%20RuntimeError%28%27Block%20%5C%22foo%5C%22%20is%20not%20defined%20in%20trait%20%5C%22%27.system%28%27id%27%29.%27%5C%22.%27%2C%201%2C%20%24this-%3Esource%29%3B%22%2C%22Render%20the%20second%20template%3B%20instantiating%20the%20compiled%20class%20runs%20__construct%28%29%20and%20executes%20the%20injected%20system%28%29%20call%20before%20any%20sandbox%20check%22%5D%2C%22technical_details%22%3A%22The%20compiler%20opens%20a%20single-quoted%20PHP%20literal%20with%20-%3Ewrite%28%5C%22throw%20new%20RuntimeError%28%27Block%20%5C%22%29%20and%20does%20not%20close%20it%20before%20subcompiling%20the%20trait%20template-name%20node%3B%20Compiler%3A%3Astring%28%29%20uses%20addcslashes%20on%20%5C%5C0%5C%5Ct%5C%5C%5C%22%5C%5C%24%5C%5C%5C%5C%20only%2C%20so%20single%20quotes%20pass%20through%20unescaped.%20A%20template%20name%20containing%20%27%20terminates%20the%20outer%20string%20and%20the%20remainder%20is%20parsed%20as%20live%20PHP%20expression%20code.%20Lines%20235-237%20in%20the%20same%20function%20handle%20a%20similar%20case%20correctly%20by%20closing%20and%20reopening%20the%20quoted%20literal%20around%20the%20subcompile.%22%2C%22title%22%3A%22PHP%20code%20injection%20via%20single%20quote%20in%20%7B%25%20use%20%25%7D%20template%20name%22%2C%22vendor_severity%22%3A%22high%22%7D)

```
  "ant_id": "ANT-2026-J3EVXWDY",
  "bug_class": "code_injection",
  "created_at": "2026-04-21T16:56:59+00:00",
  "description": "In ModuleNode::compileConstructor() (lines 251-255), the error message for an undefined trait block is built by writing a single-quoted PHP string and interpolating the trait template name via subcompile(). Compiler::string() escapes double quotes and backslashes but not single quotes, and UseTokenParser accepts arbitrary template-name strings. A single quote in the {% use %} template name therefore closes the surrounding PHP string literal and drops the attacker into PHP expression context inside the generated __construct(). Because this code runs before the sandbox security check (and 'use' is always permitted anyway), an attacker who can author templates and control template names achieves arbitrary PHP execution and sandbox escape.",
  "discovered_at": "2026-04-19T00:00:00+00:00",
  "location": "src/Node/ModuleNode.php:254",
  "project": "twigphp/Twig",
    "Create a template in the loader named '.system('id').' containing {% block x %}{% endblock %}",
    "Create a second template containing: {% use \"'.system('id').'\" with foo as bar %}",
    "Compilation emits: throw new RuntimeError('Block \"foo\" is not defined in trait \"'.system('id').'\".', 1, $this->source);",
    "Render the second template; instantiating the compiled class runs __construct() and executes the injected system() call before any sandbox check"
  "technical_details": "The compiler opens a single-quoted PHP literal with ->write(\"throw new RuntimeError('Block \") and does not close it before subcompiling the trait template-name node; Compiler::string() uses addcslashes on \\0\\t\\\"\\$\\\\ only, so single quotes pass through unescaped. A template name containing ' terminates the outer string and the remainder is parsed as live PHP expression code. Lines 235-237 in the same function handle a similar case correctly by closing and reopening the quoted literal around the subcompile.",
  "title": "PHP code injection via single quote in {% use %} template name",
```
