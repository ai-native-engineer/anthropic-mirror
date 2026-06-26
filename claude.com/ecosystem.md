<!-- source: https://claude.com/ecosystem -->

# Claude meets you**where you work**

# Claude meets you**where you work**

Build on, grow with, or buy from the Claude ecosystem. Connect your favorite services or find partner solutions built on Claude.

Connect to Claude

[Connect to Claude](#directory)Connect to Claude

View partners

[View partners](#marketplace)View partners

## Customize Claude for the best results

Connectors bring your apps and data into Claude to complete tasks. Plugins combine connectors and skills to complete workflows.

Browse connectors

[Browse connectors](/connectors)Browse connectors

Explore plugins

[Explore plugins](/plugins)Explore plugins

### Bring your tools to Claude

Connect Slack, Google Workspace, Microsoft Office, and more.

### Connect across products

Your tools can be connected to Claude Code, Cowork, and Claude on web, desktop, and mobile.

### Built for enterprise

Admins control which tools each team can use, and what those tools can do.

![logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3ac4f7d476b9cf74683f19_Clay.jpg)

![logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690abe745ff5e30a03edd1cc_Canva%20MCP%20Server.jpg)

![logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913f44f36966b0154800214_logo_activecampaign.svg)

![logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a39b31598b765419e5cee20_Asana.jpg)

![logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690abe6914fb83099a240fa4_Box.jpg)

![logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690abf35eff31cb9416d9ec4_Figma.jpg)

![logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a31e1a2bf1bfab338a43231_datadog.png)

![logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6998e8defaa12a843a37084c_docusign.jpeg)

![logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69a36e52639b2e82385fa088_gusto-favicon-192x192-160x160-5cf1c88.png)

![logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690abf96bd16a291db21b1ab_Hugging%20Face.jpg)

![logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690abfac1647ce192e81c3ba_Intercom.jpg)

![logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69c4094afe9398607424b105_quickbooks.svg)

![logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a31e318eaad6802d0604536_Google%20Drive.jpg)

![logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b842de13c16936e674bff7_Mixpanel%20Logomark%20Purple%20(1).svg)

![logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a31e2b71830965692e6a7f4_BigQuery.jpg)

![logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3ac4a4b5df309b6fb48e4f_Gmail.jpg)

![logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69ab72067a1c635172fa9fd1_P-WhiteRGB-bg%20(1).svg)

Claude works with your stack

No retrofitting required. Connect the tools you use everyday.

Explore connectors

[Explore connectors](/connectors)Explore connectors

Browse plugins

[Browse plugins](/plugins)Browse plugins

## How teams use connectors

Design

Development

Project management

Sales

Legal

Finance

Active

Prompt

Build this Figma frame as a responsive site.

Connectors

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690abf35eff31cb9416d9ec4_Figma.jpg)

Figma

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

### Turn designs into coded websites

Handing off designs to engineering takes time and leaves room for things to get lost in translation. Connect Figma to Claude and go from frame to responsive, production-ready code in one step.

Prompt

Fix the latest Sentry error and open a PR.

Connectors

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690ac10642323897e8eebfdd_Sentry%20MCP.jpg)

Sentry

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a31e8b534085f2b4436d1dc_github.png)

GitHub MCP

$ claude "Fix the latest Sentry error and open a PR"

‍

Claude claude-sonnet-4-6 · ~/projects/acme-web

‍

● Fetching latest Sentry issues…

✔ sentry issues list --project acme-web --limit 1 --status unresolved

‍

ISSUE-4821 TypeError: Cannot read properties of undefined (reading 'data')  
 Project: acme-web · Environment: production  
 First seen: 2026-06-15 22:14 UTC · Last seen: 2026-06-16 07:03 UTC  
 Events: 1,847 · Users affected: 312  
 Culprit: src/components/Dashboard/MetricsPanel.tsx line 94

‍

● Fetching full stacktrace for ISSUE-4821…

‍

TypeError: Cannot read properties of undefined (reading 'data')  
 at MetricsPanel.tsx:94:28 — processChartData(response)  
 at MetricsPanel.tsx:61:12 — useEffect(callback)  
 at react-dom/cjs/react-dom.development.js:22794

Most recent breadcrumb:  
 → GET /api/v2/metrics?range=7d → 200 OK (response.metrics was null)

‍

● Reading src/components/Dashboard/MetricsPanel.tsx…

‍

Line 90–98:  
 90 │ const processChartData = (response: ApiResponse) => {  
 91 │ const { metrics } = response  
 92 │ // metrics can be null when no data for the selected range  
 93 │ return metrics.data.map((m: Metric) => ({  
 94 │ label: m.label,  
 95 │ value: m.value ?? 0,  
 96 │ }))  
 97 │ }

‍

● Root cause identified.  
 API returns { metrics: null } when the selected range has no data. Line 93  
 dereferences metrics.data without a null guard, throwing at runtime.

‍

● Checking git status…

On branch main · nothing to commit, working tree clean

‍

● Creating fix branch…

$ git checkout -b fix/metrics-panel-null-data-sentry-4821  
 Switched to a new branch 'fix/metrics-panel-null-data-sentry-4821'

‍

● Applying fix to src/components/Dashboard/MetricsPanel.tsx…

@@ -90,8 +90,8 @@  
 const processChartData = (response: ApiResponse) => {  
 const { metrics } = response  
 - return metrics.data.map((m: Metric) => ({  
 + if (!metrics?.data) return []  
 + return metrics.data.map((m: Metric) => ({  
 label: m.label,  
 value: m.value ?? 0,  
 }))

‍

● Also updating src/components/Dashboard/MetricsPanel.tsx render guard…

@@ -61,6 +61,7 @@  
 useEffect(() => {  
 fetchMetrics(range).then((response) => {  
 + if (!response?.metrics) { setChartData([]); return }  
 setChartData(processChartData(response))  
 })  
 }, [range])

‍

● Running tests…

$ pnpm test --testPathPattern=MetricsPanel  
 PASS src/components/Dashboard/\_\_tests\_\_/MetricsPanel.test.tsx  
 ✓ renders loading state (12ms)  
 ✓ renders chart when data present (34ms)  
 ✓ renders empty state when metrics is null (8ms)  
 ✓ renders empty state when metrics.data is empty array (6ms)

Test Suites: 1 passed, 1 total  
 Tests: 4 passed, 4 total

‍

● Committing…

$ git add src/components/Dashboard/MetricsPanel.tsx  
 $ git commit -m "fix(dashboard): guard against null metrics.data in MetricsPanel

Fixes Sentry ISSUE-4821 (1,847 events, 312 users).

The /api/v2/metrics endpoint returns { metrics: null } when no data  
exists for the requested range. processChartData() dereferenced  
metrics.data without a null check, causing a TypeError at runtime.

- Add early return guard in processChartData(): if !metrics?.data return []  
- Add response guard in useEffect to short-circuit setChartData call  
- Affected users would see a blank panel crash; now renders empty state

Sentry: ISSUE-4821"

[fix/metrics-panel-null-data-sentry-4821 a3f9c12] fix(dashboard): guard against null metrics.data...  
 1 file changed, 2 insertions(+), 1 deletion(-)

‍

● Pushing branch and opening PR…

$ git push -u origin fix/metrics-panel-null-data-sentry-4821  
 Enumerating objects: 9, done.  
 Counting objects: 100% (9/9), done.  
 Writing objects: 100% (5/5), 1.02 KiB | 1.02 MiB/s, done.  
 Branch 'fix/metrics-panel-null-data-sentry-4821' set up to track remote.

$ gh pr create \  
 --title "fix(dashboard): guard against null metrics.data in MetricsPanel" \  
 --body "..." \  
 --base main \  
 --label "bug,sentry"

✓ Pull request created:  
 https://github.com/acme-org/acme-web/pull/1138

‍

──────────────────────────────────────────────────

‍

Done. PR #1138 opened · 2 lines changed · 4 tests passing  
 Sentry ISSUE-4821 will auto-resolve once the deploy goes out.

‍

$

‍

### Turn a production error into a ready-to-review PR

Triaging a production error means jumping between your error monitor, your codebase, and your version control before you can write a single line of fix. Connect Sentry and GitHub to Claude and go straight from error to pull request.

Prompt

Turn this Slack thread's action items into Asana tasks.

Connectors

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690ac11074040a8d303e83a5_Slack.jpg)

Slack

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a39b31598b765419e5cee20_Asana.jpg)

Asana

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

### Turn threads into action items

Important decisions and next steps get buried in Slack threads. Connect Slack and Asana to Claude and turn any conversation into a structured task list without leaving the thread.

Prompt

Update HubSpot from my last Granola call and draft a follow-up.

Connectors

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6983856f3c47bff2ec615f86_logo-square.svg)

Granola

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690abf89f91d777702ff37af_HubSpot.jpg)

Hubspot

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3ac4a4b5df309b6fb48e4f_Gmail.jpg)

Gmail

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

Prompt

Update HubSpot from my last Granola call and draft a follow-up.

Connectors

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

Prompt

Update HubSpot from my last Granola call and draft a follow-up.

Connectors

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

Prompt

Update HubSpot from my last Granola call and draft a follow-up.

Connectors

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

Prompt

Update HubSpot from my last Granola call and draft a follow-up.

Connectors

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

### Turn threads into action items

After every call, reps spend time manually logging notes and drafting follow-ups instead of focusing on the deal. Connect Granola, HubSpot, and Gmail to Claude and close out the call in minutes.

Prompt

Find contracts expiring in 90 days and add renewal reminders.

Connectors

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69fe3a22c5204e580b088032_ironclad.svg)

Ironclad Contracts

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/699d19b00926e2026aaf79eb_google-calendar.png)

Google Calendar

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

### Find expiring contracts and set renewal reminders

Contracts expire quietly. By the time someone catches it, the window to renegotiate has often closed. Connect Ironclad and Google Calendar to Claude and stay ahead of every renewal date.

Prompt

Reconcile last month's Brex spend against NetSuite and flag mismatches.

Connectors

![Brex logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b073e9d3f60065e71d81f8_Brex-symbol-ink-gray-1024x1024px.svg)

Brex

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690ac0797fb7905db81f0c5f_NetSuite%20AI%20Connector%20for%20Claude.jpg)

Oracle NetSuite

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

### Reconcile card spend against the books and flag mismatches

Month-end reconciliation means manually comparing card transactions against your accounting system, line by line. Connect Brex and NetSuite to Claude and surface mismatches in one pass.

## Purchase from Claude-powered partners

Apply your existing Anthropic commitment across the tools your team already uses.

Explore marketplace

[Explore marketplace](/platform/marketplace)Explore marketplace

### Consolidated AI spend

Use your existing Anthropic commitment across multiple Claude-powered partner tools.

### Enterprise-ready partners

Browse Claude-powered tools built for enterprise teams. Spend less time evaluating, more time building.

### Built to scale with you

Add partners as your needs evolve. Your commitment flexes with your organization.

## FAQ

### What's the difference between the directory and the marketplace?

The directory brings your tools into Claude. The marketplace brings Claude to you inside partner solutions, using your committed spend. Many teams use both.

### What's the difference between connectors and plugins?

Connectors give Claude direct access to a single app. Plugins combine connectors with instructions, so Claude can handle complete workflows across multiple tools without you having to set it up each time.

[Prev](#)Prev

[Next](#)Next
