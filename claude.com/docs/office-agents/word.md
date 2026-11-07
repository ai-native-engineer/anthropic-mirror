<!-- source: https://claude.com/docs/office-agents/word -->

Claude for Word is an add-in that brings Claude into Word. Ask questions
about your document with clickable section citations, edit selected
passages while preserving formatting, review counterparty redlines,
work through comment threads, and fill templates in your document’s
styles.

Claude for Word is generally available to Pro, Max, Team,
and Enterprise plans.

With Claude for Word, you can:

* Ask questions about your document and get answers with clickable
  section citations.
* Edit selected text while preserving surrounding styles, numbering,
  and formatting.
* Use tracked changes mode so every edit lands as a revision you can
  accept or reject in Word’s native review pane.
* Have Claude work through comment threads, editing the anchored text
  and replying with what it changed.
* Summarize counterparty redlines and flag the revisions worth pushing
  back on.
* Fill templates with drafted content that inherits your document’s
  heading and paragraph styles.
* Find every provision touching a theme with semantic navigation, not
  just keyword search.

##  Get started with Claude for Word

Claude for Word runs on the following Word builds.

* Word on the web
* Word on Windows with a Microsoft 365 subscription, Version 2205,
  build 15202.10000 or later
* Word on Mac, version 16.61, build 22040100 or later

Go to the [Claude for Microsoft 365 listing on Microsoft AppSource](https://marketplace.microsoft.com/en-us/product/office/WA200010725?tab=Overview).

Sign in

Open Word, activate the add-in, and sign in with your Claude
account.

Organization admins can deploy Claude for Word through the Microsoft
365 Admin Center.

Go to Settings, Integrated apps, Add-ins.

Search for “Claude for Microsoft 365” in Microsoft AppSource.

Assign the add-in to your organization or to specific users or
groups. Share [Microsoft’s deployment guide](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-deployment-of-add-ins)
with your team for activation steps.

After deployment, users can activate the Claude add-in from Tools,
Add-ins on Mac or Home, Add-ins on Windows, sign in, and start working.

Organizations that have disabled “Let users access the Office Store” may
find that admin-deployed add-ins don’t appear for users. To work around
this, deploy using the manifest XML file described below.

###  Deploy with a custom manifest

For IT administrators deploying to multiple users when the Office Store
is disabled:

Download the manifest

Download the [custom manifest XML file](https://pivot.claude.ai/manifest-word.xml)
and save it to a secure location.

Open the Admin Center

Go to <https://admin.microsoft.com>,
sign in, and open Settings, Integrated apps.

Upload the custom add-in

Select “Upload custom apps”, choose “Office Add-in”, then
“I have a manifest file on this device”. Upload the manifest.

Assign users

Choose entire organization, specific users, specific groups, or just
yourself for admin testing.

5

Review settings and select “Deploy”. The add-in is available within
minutes. Full organization rollout can take up to 24 hours.

After deployment, users see Claude in Word’s Home ribbon and sign in
with their Claude credentials on first use.

If your organization routes AI traffic through Amazon Bedrock, Google Cloud
Vertex AI, Azure AI Foundry, or an LLM gateway, your admin can deploy
the add-in without individual Claude accounts. See

##  Key features

###  Read and understand documents

Ask Claude questions about specific sections, clauses, or defined terms
in your document. Claude provides answers with clickable citations that
navigate directly to the referenced section.

Claude recognizes common document patterns including multi-level legal
numbering, defined terms, cross-references, and standard contract
structures. Verify that outputs match your specific requirements and
your firm’s standard positions.

Example prompts:

* “What’s the liability cap and is it mutual?”
* “Summarize the key commercial terms in this agreement.”
* “What assumptions drive the revenue forecast in section 3?”

###  Edit selected text

Select a passage and tell Claude what to change. Claude edits only the
selection while preserving surrounding styles, numbering, and
formatting. New text inherits the paragraph style, font, and numbering
of the surrounding content.
Example prompts:

* “Tighten this paragraph and drop the passive voice.”
* “Rewrite this clause to make the indemnification mutual.”
* “Simplify this section for a non-technical audience.”

###  Tracked changes mode

When you enter tracked changes mode, Claude’s edits land as tracked
revisions. The original text is visible as a deletion and the new text
as an insertion, all reviewable in Word’s native review pane. Review
every edit before accepting it, and undo with Word’s standard Ctrl+Z
on Windows or Cmd+Z on Mac if you want to revert.
Example prompts:

* “Rewrite section 4.2 to cap damages at 12 months of fees, and make it
  mutual.”
* “Draft a mutual indemnification clause after section 8.”

###  Comment-driven editing

Claude reads comment threads in your document, understands what text
each thread is anchored to, and can work through them one by one. For
each comment, Claude edits the anchored passage and replies to the
thread with a note explaining what it did.
Example prompts:

* “Work through my open comments.”
* “Address the comment on the liability section.”

###  Summarize counterparty redlines

When a counterparty returns a document with tracked changes, Claude can
read and summarize what they changed. Ask Claude to group changes by
severity or flag the ones worth pushing back on.
Example prompts:

* “Summarize what the other side changed and flag anything that’s worth
  discussing.”
* “Which of these redlines are dealbreakers?”

###  Fill templates

Draft sections in your document’s heading and paragraph styles. Claude
uses your template’s formatting when generating content, so new
headings, bullets, and table entries match what’s already there. Tables
populate in place without reflowing layout or changing column widths.
Example prompts:

* “Draft the Key Risks section with four risks in the template’s style.”
* “Populate the summary table with revenue, gross margin, and net
  retention for the last three years.”

###  Semantic navigation

Find every provision or passage in your document that touches a
specific theme. Claude returns thematic matches, not just keyword hits,
and each result navigates to the relevant location on click.
Example prompts:

* “Find every provision touching data retention.”
* “Where does this agreement address termination?”

##  Connectors and Skills

Claude for Word supports connectors for pulling external context into
your document, and Skills for applying reusable task recipes. See
[Connectors and Skills](https://claude.com/docs/office-agents/connectors-and-skills) for
details.

##  Set persistent instructions

Open Settings in the add-in sidebar and use the Instructions field to
set preferences that
apply to every conversation in Word. Instructions are useful for tone
and style conventions such as “use formal tone” or “follow APA citation
style”, document structure preferences, or recurring context about your
workflow.
Instructions you set in Word only apply to Word. They are separate from
Instructions you set in Excel or PowerPoint.

Claude for Word shares context with Claude for Excel, PowerPoint, and
Outlook, so a single conversation can span your open document,
workbook, deck, and inbox. See

##  Context and session management

The add-in handles long sessions for you so a single conversation can
span an entire workflow.

* **Auto-compaction**: longer conversations are automatically compacted
  into new conversations to avoid running out of context. See
  [Understanding usage and length limits](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits).

Your use of Claude for Word is associated with your existing Claude
account and is subject to the same usage limits.

##  Models available

Claude for M365 offers a curated subset of the Claude models: the ones
that work best for Office tasks, so the list you see in the add-in can
be shorter than what you see in Claude.ai. Your organization’s model
access settings also apply, and a model appears here only if your role
permits it. See
[Manage model access for your organization](https://support.claude.com/en/articles/15694740-manage-model-access-for-your-organization)
for how those settings interact with each product. If you connect
through Amazon Bedrock, Google Cloud Vertex AI, Azure AI Foundry, or an
LLM gateway, the available models come from that platform and your
admin’s configuration instead of your Claude.ai model access settings.
See [Use Claude for M365 with third-party platforms](https://claude.com/docs/office-agents/third-party-platforms)

Inputs and outputs are deleted on the backend within 30 days of receipt
or generation, except in cases outlined in
Data is cached for a number of hours after deletion so users can access
context in recently closed documents.
not synced across devices and can be cleared from Settings at any time.
Reinstalling the add-in or switching between Claude add-ins does not
remove it. See [Data storage and retention](https://claude.com/docs/office-agents/data-storage)
for where it sits on disk and how long it is kept.
document and any files you attach. Clearing chat history removes only
the copy in your browser. It does not delete the messages or attached
files that Anthropic keeps.
Claude for Word does not inherit custom data retention settings your
organization might have set. Activity is not included in Enterprise
audit logs. For Enterprise organizations with the
enabled, Claude for Word sessions are included in the Compliance API.
This coverage requires no additional setup: the same Compliance Access
Keys apply.
Claude reads the content of your currently open document, including
text, comments, tracked changes, footnotes, tables, and bookmarks. It
only accesses the document you have open in Word. For highly sensitive
or regulated data, follow your organization’s data handling policies.

Claude for Word is not recommended for:

* Final client deliverables or counterparty sends without human review.
* Litigation filings or audit-critical documents without verification.
* Replacing legal or financial judgment.
* Documents containing highly sensitive or privileged data without
  proper controls.

###  Unsupported versions

The add-in does not run on these Word versions.

* Word 2016 and 2019 perpetual or volume license.
* Word on iPad.
* Word on Android.
* Microsoft 365 Word builds older than Version 2205 on Windows or
  version 16.61 on Mac.
* Legacy `.doc` files. Save as `.docx` first.

##  Prompt injection risk

Only use Claude for Word with trusted documents. Documents from external
sources such as downloaded templates, counterparty files, or files
shared via email can contain hidden instructions that manipulate the
add-in into extracting data, modifying records, or performing
destructive actions.

Prompt injection attacks hide malicious instructions in document
content such as text, comments, tracked changes, headers, and footers
to trick Claude into taking unintended actions. Testing has identified
scenarios where Claude for Word can be manipulated to:

* Extract and share sensitive information through web searches
  containing your sensitive data or file system access that exposes
  proprietary information.
* Modify critical content such as contract terms or financial figures.
* Perform destructive actions without verification when allowed to act
  unsupervised.

When Claude proposes a risky operation, you are asked to confirm before
it runs. Review confirmations carefully, especially for content from
external sources.

##  Best practices

Follow these guidelines to use Claude for Word safely and effectively.

* Always review tracked changes before accepting them.
* Verify that outputs match your firm’s playbook and standard
  positions.
* Use appropriate permissions and access controls.
* Maintain human oversight for client-facing work.

##  Example use cases

###  Legal contract review

Prompts that review and revise contracts and counterparty redlines.

* “Summarize the key commercial terms: parties, term, governing law,
  and anything off-market.”
* “Flag provisions that deviate from standard market position, ranked
  by severity.”
* “Make the indemnification mutual and insert our standard fallback
  language.”
* “Work through all five reviewer comments as tracked changes.”
* “What did the counterparty change, and which revisions are
  dealbreakers?”

###  Finance memo drafting

Prompts that build out investment memos and finance writeups.

* “Draft the Investment Thesis section with three points, pulling the
  numbers from the uploaded 10-K.”
* “Populate the summary table with revenue, gross margin, and FCF for
  the last three years.”
* “Too generic on point two. Use the customer count from the deck.”
* “Address the partner’s comment on the Risks section.”

###  Document QA and consistency

Prompts that check a document for internal consistency and quality.

* “Flag inconsistent defined terms and broken cross-references.”
* “Check the numbering scheme for gaps.”
* “Proofread for spelling, grammar, and punctuation.”
* “Is the same party referred to by different names anywhere in this
  document?”

###  General document editing

Prompts that tighten or restructure prose.

* “Tighten section 4 and drop the passive voice.”
* “Rewrite this for a non-technical audience.”
* “Add a fourth risk addressing customer concentration.”
* “Define this term and use it consistently throughout.”

{"docsConfig":{"theme":"mint","$schema":"https://mintlify.com/docs.json","name":"Claude.ai Documentation","colors":{"primary":"#0E0E0E","light":"#D4A27F","dark":"#0E0E0E"},"logo":{"light":"https://mintcdn.com/claude-ai/1fyDNLAICe3KG6rB/logo/light.svg?fit=max\u0026auto=format\u0026n=1fyDNLAICe3KG6rB\u0026q=85\u0026s=e870c19cb781d8a7c7b7d19de53b0a10","dark":"https://mintcdn.com/claude-ai/1fyDNLAICe3KG6rB/logo/dark.svg?fit=max\u0026auto=format\u0026n=1fyDNLAICe3KG6rB\u0026q=85\u0026s=80cc0b06d8fd9aeefec8acb226de6866"},"favicon":"https://mintcdn.com/claude-ai/N9YeVEPVxANlc2We/favicon.ico?fit=max\u0026auto=format\u0026n=N9YeVEPVxANlc2We\u0026q=85\u0026s=a22e48fa0189917f9be516d4a555898c","background":{"color":{"light":"#FDFDF7","dark":"#09090B"}},"navbar":{"links":[{"href":"https://support.anthropic.com","label":"Support"}],"primary":{"type":"button","label":"Go to Claude","href":"https://claude.ai"}},"footer":{"socials":{"x":"https://x.com/AnthropicAI","linkedin":"https://www.linkedin.com/company/anthropicresearch"},"links":[{"header":"Company","items":[{"label":"Anthropic","href":"https://www.anthropic.com/company"},{"label":"Careers","href":"https://www.anthropic.com/careers"},{"label":"Economic Futures","href":"https://www.anthropic.com/economic-futures"},{"label":"Research","href":"https://www.anthropic.com/research"},{"label":"News","href":"https://www.anthropic.com/news"},{"label":"Trust center","href":"https://trust.anthropic.com/"},{"label":"Transparency","href":"https://www.anthropic.com/transparency"}]},{"header":"Help and security","items":[{"label":"Availability","href":"https://www.anthropic.com/supported-countries"},{"label":"Status","href":"https://status.anthropic.com/"},{"label":"Support center","href":"https://support.claude.com/"}]},{"header":"Learn","items":[{"label":"Courses","href":"https://academy.claude.com/"},{"label":"MCP connectors","href":"https://claude.com/partners/mcp"},{"label":"Customer stories","href":"https://www.claude.com/customers"},{"label":"Engineering blog","href":"https://www.anthropic.com/engineering"},{"label":"Events","href":"https://www.anthropic.com/events"},{"label":"Powered by Claude","href":"https://claude.com/partners/powered-by-claude"},{"label":"Service partners","href":"https://claude.com/partners/services"},{"label":"Startups program","href":"https://claude.com/programs/startups"}]},{"header":"Terms and policies","items":[{"label":"Privacy policy","href":"https://www.anthropic.com/legal/privacy"},{"label":"Disclosure policy","href":"https://www.anthropic.com/responsible-disclosure-policy"},{"label":"Usage policy","href":"https://www.anthropic.com/legal/aup"},{"label":"Commercial terms","href":"https://www.anthropic.com/legal/commercial-terms"},{"label":"Consumer terms","href":"https://www.anthropic.com/legal/consumer-terms"}]}]},"seo":{"metatags":{"canonical":"https://claude.com/docs"}},"fonts":{"family":"Anthropic Sans"},"contextual":{"options":["copy","view","claude"],"display":"header"},"styling":{"latex":false},"navigation":{"pages":[]}},"deployment":{"deploymentMetadataValue":{"subdomain":"claude-ai","hasAudioNarration":false,"actualSubdomain":"claude-ai","customDomains":["claude.com"],"gitSource":{"type":"github","owner":"anthropics","repo":"claude-ai-docs","deployBranch":"main","contentDirectory":"","isPrivate":true,"mountPath":"","label":""},"feedback":{"thumbs":true},"entitlements":{"AI\_CHAT":{"status":"ENABLED"},"REMOVE\_BRANDING":{"status":"ENABLED"},"CONTEXTUAL\_FEEDBACK":{"status":"ENABLED"},"CODE\_SNIPPET\_FEEDBACK":{"status":"ENABLED"},"WEB\_MCP":{"status":"ENABLED"},"NARRATION":{"status":"ENABLED"}},"buildId":"6aeeb42e59edac7bace5a40b","clientVersion":"0.0.4076","searchFilterCounts":[{"language":"default","tag":"Claude Tag","count":76},{"language":"default","tag":"For administrators","count":61},{"language":"default","tag":"Claude for Government","count":44},{"language":"default","tag":"Claude on third-party platforms","count":42},{"language":"default","tag":"Claude Desktop","count":42},{"language":"default","tag":"Claude Science","count":41},{"language":"default","tag":"Build for Claude","count":30},{"language":"default","tag":"Set up Claude Tag","count":30},{"language":"default","tag":"Use Claude Science","count":23},{"language":"default","tag":"Customize Claude","count":22}]},"assistantConfig":{"enableAskAiButton":false,"enableStarterQuestions":false,"enableAskAiSearchBar":true},"basePath":"/docs","hasChatPermissions":true,"hasWebMcpPermissions":true,"toggles":[{"name":"kill-isr","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"agent-mintlify-slack","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"agent-integrations-settings","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"rbac-expansion","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"automations-pr-grouping","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"custom-prefix","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"analytics-v7","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"user-flows-analytics","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"no-publish-flow","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"workos-onboarding","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"llms-txt-v2","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"snapshot-serving-live","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"stripTemperatureMiddleware","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"support-platform-pylon-zendesk","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"snapshot-serving","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"instant-rollback","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"granular-notifications-server","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"granular-notifications","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"automations-fable","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"fixed-ai-action-pricing","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"automation-resolve-merge-conflict","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"scoped-publishing","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"mintql","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"page-level-analytics","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"editor-version-history-v2","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"billing-page-v2","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"full-page-search","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"workspace-projects","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"assistant-v5","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"fork-pr-previews","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"revalidation-jwt","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"workos-sso-scim","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"hobby-abuse-scan","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"dashboard-inbox","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"workos-signup","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"turbopuffer-dual-write","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"workos-enabled","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"approve-review-flow","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"editor-metadata","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"sso-setup-deadline-banner","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"turbopuffer-serve","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"live-agents","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"comment-mode","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false}],"googleFontsInlined":false},"customCss":[{"filePath":"style.css","href":"/docs/\_mintlify/custom/claude-ai/f864c4801ebb83ca/style.css"}],"page":{"pagePath":"office-agents/word","slug":"/office-agents/word","pageMetadata":{"title":"Use Claude for Word","description":"A Word add-in that integrates Claude into your document workflow, for Pro, Max, Team, and Enterprise plans.","href":"/office-agents/word"},"description":{"compiledSource":"\"use strict\";\nconst {jsx: \_jsx} = arguments[0];\nconst {useMDXComponents: \_provideComponents} = arguments[0];\nfunction \_createMdxContent(props) {\n const \_components = {\n p: \"p\",\n ...\_provideComponents(),\n ...props.components\n };\n return \_jsx(\_components.p, {\n children: \"A Word add-in that integrates Claude into your document workflow, for Pro, Max, Team, and Enterprise plans.\"\n });\n}\nfunction MDXContent(props = {}) {\n const {wrapper: MDXLayout} = {\n ...\_provideComponents(),\n ...props.components\n };\n return MDXLayout ? \_jsx(MDXLayout, {\n ...props,\n children: \_jsx(\_createMdxContent, {\n ...props\n })\n }) : \_createMdxContent(props);\n}\nreturn {\n default: MDXContent\n};\n","frontmatter":{},"scope":{}},"pageType":"default","mdx":{"mdxSource":{"compiledSource":"\"use strict\";const{Fragment:\_Fragment,jsx:\_jsx,jsxs:\_jsxs}=arguments[0];const{useMDXComponents:\_provideComponents}=arguments[0];function \_createMdxContent(props){const \_components={a:`a`,code:`code`,li:`li`,p:`p`,strong:`strong`,ul:`ul`,...\_provideComponents(),...props.components},{Heading,Note,Step,Steps,Warning}=\_components;if(!Heading)\_missingMdxReference(`Heading`,true);if(!Note)\_missingMdxReference(`Note`,true);if(!Step)\_missingMdxReference(`Step`,true);if(!Steps)\_missingMdxReference(`Steps`,true);if(!Warning)\_missingMdxReference(`Warning`,true);return \_jsxs(\_Fragment,{children:[\_jsx(Warning,{children:\_jsxs(\_components.p,{children:[`After the September and October 2026 Microsoft 365 updates on Windows, some\nusers are missing their chat history and uploaded skills in the Claude add-in.\nAnthropic is working with Microsoft to solve this issue. In the meantime, see\n`,\_jsx(\_components.a,{href:`/office-agents/data-storage#chat-history-and-skills-missing-after-a-microsoft-365-update-on-windows`,children:`what you and your IT team can do`}),`.`]})}),`\n`,\_jsx(\_components.p,{children:`Claude for Word is an add-in that brings Claude into Word. Ask questions\nabout your document with clickable section citations, edit selected\npassages while preserving formatting, review counterparty redlines,\nwork through comment threads, and fill templates in your document’s\nstyles.`}),`\n`,\_jsx(Note,{children:\_jsx(\_components.p,{children:`Claude for Word is generally available to Pro, Max, Team,\nand Enterprise plans.`})}),`\n`,\_jsx(Heading,{level:`2`,id:`what-you-can-do`,children:`What you can do`}),`\n`,\_jsx(\_components.p,{children:`With Claude for Word, you can:`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`Ask questions about your document and get answers with clickable\nsection citations.`}),`\n`,\_jsx(\_components.li,{children:`Edit selected text while preserving surrounding styles, numbering,\nand formatting.`}),`\n`,\_jsx(\_components.li,{children:`Use tracked changes mode so every edit lands as a revision you can\naccept or reject in Word’s native review pane.`}),`\n`,\_jsx(\_components.li,{children:`Have Claude work through comment threads, editing the anchored text\nand replying with what it changed.`}),`\n`,\_jsx(\_components.li,{children:`Summarize counterparty redlines and flag the revisions worth pushing\nback on.`}),`\n`,\_jsx(\_components.li,{children:`Fill templates with drafted content that inherits your document’s\nheading and paragraph styles.`}),`\n`,\_jsx(\_components.li,{children:`Find every provision touching a theme with semantic navigation, not\njust keyword search.`}),`\n`]}),`\n`,\_jsx(Heading,{level:`2`,id:`get-started-with-claude-for-word`,children:`Get started with Claude for Word`}),`\n`,\_jsx(Heading,{level:`3`,id:`supported-versions`,children:`Supported versions`}),`\n`,\_jsx(\_components.p,{children:`Claude for Word runs on the following Word builds.`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`Word on the web`}),`\n`,\_jsx(\_components.li,{children:`Word on Windows with a Microsoft 365 subscription, Version 2205,\nbuild 15202.10000 or later`}),`\n`,\_jsx(\_components.li,{children:`Word on Mac, version 16.61, build 22040100 or later`}),`\n`]}),`\n`,\_jsx(Heading,{level:`3`,id:`install-for-yourself`,children:`Install for yourself`}),`\n`,\_jsxs(Steps,{children:[\_jsx(Step,{title:`Open the marketplace listing`,children:\_jsxs(\_components.p,{children:[`Go to the `,\_jsx(\_components.a,{href:`https://marketplace.microsoft.com/en-us/product/office/WA200010725?tab=Overview`,children:`Claude for Microsoft 365 listing on Microsoft AppSource`}),`.`]})}),\_jsx(Step,{title:`Install the add-in`,children:\_jsx(\_components.p,{children:`Select “Get it now” to install.`})}),\_jsx(Step,{title:`Sign in`,children:\_jsx(\_components.p,{children:`Open Word, activate the add-in, and sign in with your Claude\naccount.`})})]}),`\n`,\_jsx(Heading,{level:`3`,id:`deploy-to-your-organization`,children:`Deploy to your organization`}),`\n`,\_jsx(\_components.p,{children:`Organization admins can deploy Claude for Word through the Microsoft\n365 Admin Center.`}),`\n`,\_jsxs(Steps,{children:[\_jsx(Step,{title:`Allow Office Store access`,children:\_jsxs(\_components.p,{children:[`In the `,\_jsx(\_components.a,{href:`https://admin.microsoft.com`,children:`Microsoft 365 Admin Center`}),`, go\nto Settings, Org Settings, User owned apps and services, and turn on\n`,\_jsx(\_components.a,{href:`https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-addins-in-the-admin-center`,children:`“Let users access the Office Store”`}),`.`]})}),\_jsx(Step,{title:`Open Integrated apps`,children:\_jsx(\_components.p,{children:`Go to Settings, Integrated apps, Add-ins.`})}),\_jsx(Step,{title:`Find the add-in`,children:\_jsx(\_components.p,{children:`Search for “Claude for Microsoft 365” in Microsoft AppSource.`})}),\_jsx(Step,{title:`Deploy`,children:\_jsxs(\_components.p,{children:[`Assign the add-in to your organization or to specific users or\ngroups. Share `,\_jsx(\_components.a,{href:`https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-deployment-of-add-ins`,children:`Microsoft’s deployment guide`}),`\nwith your team for activation steps.`]})})]}),`\n`,\_jsx(Note,{children:\_jsxs(\_components.p,{children:[`If your organization uses Microsoft Entra Privileged Identity\nManagement (PIM) for admin roles, the Integrated apps page does not\nrecognize roles activated through PIM, so deployment fails. This is a\n`,\_jsx(\_components.a,{href:`https://learn.microsoft.com/en-us/office/dev/add-ins/resources/resources-office-add-in-known-issues`,children:`known Microsoft issue`}),`,\ntracking ID 11126536. To work around it, deploy from an admin account\nwith the required role assigned as permanently active rather than\nPIM-eligible. See\n`,\_jsx(\_components.a,{href:`https://learn.microsoft.com/en-us/troubleshoot/microsoft-365/admin/miscellaneous/cannot-deploy-add-in-integrated-apps-menu`,children:`Microsoft’s troubleshooting guidance`}),`.\nIndividual users can still\n`,\_jsx(\_components.a,{href:`#install-for-yourself`,children:`install the add-in themselves`}),`.`]})}),`\n`,\_jsx(\_components.p,{children:`After deployment, users can activate the Claude add-in from Tools,\nAdd-ins on Mac or Home, Add-ins on Windows, sign in, and start working.`}),`\n`,\_jsx(Warning,{children:\_jsx(\_components.p,{children:`Organizations that have disabled “Let users access the Office Store” may\nfind that admin-deployed add-ins don’t appear for users. To work around\nthis, deploy using the manifest XML file described below.`})}),`\n`,\_jsx(Heading,{level:`3`,id:`deploy-with-a-custom-manifest`,children:`Deploy with a custom manifest`}),`\n`,\_jsx(\_components.p,{children:`For IT administrators deploying to multiple users when the Office Store\nis disabled:`}),`\n`,\_jsxs(Steps,{children:[\_jsx(Step,{title:`Download the manifest`,children:\_jsxs(\_components.p,{children:[`Download the `,\_jsx(\_components.a,{href:`https://pivot.claude.ai/manifest-word.xml`,children:`custom manifest XML file`}),`\nand save it to a secure location.`]})}),\_jsx(Step,{title:`Open the Admin Center`,children:\_jsxs(\_components.p,{children:[`Go to `,\_jsx(\_components.a,{href:`https://admin.microsoft.com`,children:`https://admin.microsoft.com`}),`,\nsign in, and open Settings, Integrated apps.`]})}),\_jsx(Step,{title:`Upload the custom add-in`,children:\_jsx(\_components.p,{children:`Select “Upload custom apps”, choose “Office Add-in”, then\n“I have a manifest file on this device”. Upload the manifest.`})}),\_jsx(Step,{title:`Assign users`,children:\_jsx(\_components.p,{children:`Choose entire organization, specific users, specific groups, or just\nyourself for admin testing.`})}),\_jsx(Step,{title:`Deploy`,children:\_jsx(\_components.p,{children:`Review settings and select “Deploy”. The add-in is available within\nminutes. Full organization rollout can take up to 24 hours.`})})]}),`\n`,\_jsx(\_components.p,{children:`After deployment, users see Claude in Word’s Home ribbon and sign in\nwith their Claude credentials on first use.`}),`\n`,\_jsx(Heading,{level:`3`,id:`connect-through-a-third-party-platform`,children:`Connect through a third-party platform`}),`\n`,\_jsxs(\_components.p,{children:[`If your organization routes AI traffic through Amazon Bedrock, Google Cloud\nVertex AI, Azure AI Foundry, or an LLM gateway, your admin can deploy\nthe add-in without individual Claude accounts. See\n`,\_jsx(\_components.a,{href:`/office-agents/third-party-platforms`,children:`Use Claude for M365 with third-party platforms`}),`.`]}),`\n`,\_jsx(Heading,{level:`2`,id:`key-features`,children:`Key features`}),`\n`,\_jsx(Heading,{level:`3`,id:`read-and-understand-documents`,children:`Read and understand documents`}),`\n`,\_jsx(\_components.p,{children:`Ask Claude questions about specific sections, clauses, or defined terms\nin your document. Claude provides answers with clickable citations that\nnavigate directly to the referenced section.`}),`\n`,\_jsx(Note,{children:\_jsx(\_components.p,{children:`Claude recognizes common document patterns including multi-level legal\nnumbering, defined terms, cross-references, and standard contract\nstructures. Verify that outputs match your specific requirements and\nyour firm’s standard positions.`})}),`\n`,\_jsx(\_components.p,{children:`Example prompts:`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`“What’s the liability cap and is it mutual?”`}),`\n`,\_jsx(\_components.li,{children:`“Summarize the key commercial terms in this agreement.”`}),`\n`,\_jsx(\_components.li,{children:`“What assumptions drive the revenue forecast in section 3?”`}),`\n`]}),`\n`,\_jsx(Heading,{level:`3`,id:`edit-selected-text`,children:`Edit selected text`}),`\n`,\_jsx(\_components.p,{children:`Select a passage and tell Claude what to change. Claude edits only the\nselection while preserving surrounding styles, numbering, and\nformatting. New text inherits the paragraph style, font, and numbering\nof the surrounding content.`}),`\n`,\_jsx(\_components.p,{children:`Example prompts:`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`“Tighten this paragraph and drop the passive voice.”`}),`\n`,\_jsx(\_components.li,{children:`“Rewrite this clause to make the indemnification mutual.”`}),`\n`,\_jsx(\_components.li,{children:`“Simplify this section for a non-technical audience.”`}),`\n`]}),`\n`,\_jsx(Heading,{level:`3`,id:`tracked-changes-mode`,children:`Tracked changes mode`}),`\n`,\_jsx(\_components.p,{children:`When you enter tracked changes mode, Claude’s edits land as tracked\nrevisions. The original text is visible as a deletion and the new text\nas an insertion, all reviewable in Word’s native review pane. Review\nevery edit before accepting it, and undo with Word’s standard Ctrl+Z\non Windows or Cmd+Z on Mac if you want to revert.`}),`\n`,\_jsx(\_components.p,{children:`Example prompts:`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`“Rewrite section 4.2 to cap damages at 12 months of fees, and make it\nmutual.”`}),`\n`,\_jsx(\_components.li,{children:`“Draft a mutual indemnification clause after section 8.”`}),`\n`]}),`\n`,\_jsx(Heading,{level:`3`,id:`comment-driven-editing`,children:`Comment-driven editing`}),`\n`,\_jsx(\_components.p,{children:`Claude reads comment threads in your document, understands what text\neach thread is anchored to, and can work through them one by one. For\neach comment, Claude edits the anchored passage and replies to the\nthread with a note explaining what it did.`}),`\n`,\_jsx(\_components.p,{children:`Example prompts:`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`“Work through my open comments.”`}),`\n`,\_jsx(\_components.li,{children:`“Address the comment on the liability section.”`}),`\n`]}),`\n`,\_jsx(Heading,{level:`3`,id:`summarize-counterparty-redlines`,children:`Summarize counterparty redlines`}),`\n`,\_jsx(\_components.p,{children:`When a counterparty returns a document with tracked changes, Claude can\nread and summarize what they changed. Ask Claude to group changes by\nseverity or flag the ones worth pushing back on.`}),`\n`,\_jsx(\_components.p,{children:`Example prompts:`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`“Summarize what the other side changed and flag anything that’s worth\ndiscussing.”`}),`\n`,\_jsx(\_components.li,{children:`“Which of these redlines are dealbreakers?”`}),`\n`]}),`\n`,\_jsx(Heading,{level:`3`,id:`fill-templates`,children:`Fill templates`}),`\n`,\_jsx(\_components.p,{children:`Draft sections in your document’s heading and paragraph styles. Claude\nuses your template’s formatting when generating content, so new\nheadings, bullets, and table entries match what’s already there. Tables\npopulate in place without reflowing layout or changing column widths.`}),`\n`,\_jsx(\_components.p,{children:`Example prompts:`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`“Draft the Key Risks section with four risks in the template’s style.”`}),`\n`,\_jsx(\_components.li,{children:`“Populate the summary table with revenue, gross margin, and net\nretention for the last three years.”`}),`\n`]}),`\n`,\_jsx(Heading,{level:`3`,id:`semantic-navigation`,children:`Semantic navigation`}),`\n`,\_jsx(\_components.p,{children:`Find every provision or passage in your document that touches a\nspecific theme. Claude returns thematic matches, not just keyword hits,\nand each result navigates to the relevant location on click.`}),`\n`,\_jsx(\_components.p,{children:`Example prompts:`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`“Find every provision touching data retention.”`}),`\n`,\_jsx(\_components.li,{children:`“Where does this agreement address termination?”`}),`\n`]}),`\n`,\_jsx(Heading,{level:`2`,id:`connectors-and-skills`,children:`Connectors and Skills`}),`\n`,\_jsxs(\_components.p,{children:[`Claude for Word supports connectors for pulling external context into\nyour document, and Skills for applying reusable task recipes. See\n`,\_jsx(\_components.a,{href:`/office-agents/connectors-and-skills`,children:`Connectors and Skills`}),` for\ndetails.`]}),`\n`,\_jsx(Heading,{level:`2`,id:`set-persistent-instructions`,children:`Set persistent instructions`}),`\n`,\_jsx(\_components.p,{children:`Open Settings in the add-in sidebar and use the Instructions field to\nset preferences that\napply to every conversation in Word. Instructions are useful for tone\nand style conventions such as “use formal tone” or “follow APA citation\nstyle”, document structure preferences, or recurring context about your\nworkflow.`}),`\n`,\_jsx(\_components.p,{children:`Instructions you set in Word only apply to Word. They are separate from\nInstructions you set in Excel or PowerPoint.`}),`\n`,\_jsx(Heading,{level:`2`,id:`work-across-m365-apps`,children:`Work across M365 apps`}),`\n`,\_jsxs(\_components.p,{children:[`Claude for Word shares context with Claude for Excel, PowerPoint, and\nOutlook, so a single conversation can span your open document,\nworkbook, deck, and inbox. See\n`,\_jsx(\_components.a,{href:`/office-agents/work-across-apps`,children:`Work across M365 apps`}),`.`]}),`\n`,\_jsx(Heading,{level:`2`,id:`context-and-session-management`,children:`Context and session management`}),`\n`,\_jsx(\_components.p,{children:`The add-in handles long sessions for you so a single conversation can\nspan an entire workflow.`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsxs(\_components.li,{children:[\_jsx(\_components.strong,{children:`Auto-compaction`}),`: longer conversations are automatically compacted\ninto new conversations to avoid running out of context. See\n`,\_jsx(\_components.a,{href:`https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits`,children:`Understanding usage and length limits`}),`.`]}),`\n`]}),`\n`,\_jsx(\_components.p,{children:`Your use of Claude for Word is associated with your existing Claude\naccount and is subject to the same usage limits.`}),`\n`,\_jsx(Heading,{level:`2`,id:`models-available`,children:`Models available`}),`\n`,\_jsxs(\_components.p,{children:[`Claude for M365 offers a curated subset of the Claude models: the ones\nthat work best for Office tasks, so the list you see in the add-in can\nbe shorter than what you see in Claude.ai. Your organization’s model\naccess settings also apply, and a model appears here only if your role\npermits it. See\n`,\_jsx(\_components.a,{href:`https://support.claude.com/en/articles/15694740-manage-model-access-for-your-organization`,children:`Manage model access for your organization`}),`\nfor how those settings interact with each product. If you connect\nthrough Amazon Bedrock, Google Cloud Vertex AI, Azure AI Foundry, or an\nLLM gateway, the available models come from that platform and your\nadmin’s configuration instead of your Claude.ai model access settings.\nSee `,\_jsx(\_components.a,{href:`/office-agents/third-party-platforms`,children:`Use Claude for M365 with third-party platforms`}),`\nfor details.`]}),`\n`,\_jsx(Heading,{level:`2`,id:`data-handling`,children:`Data handling`}),`\n`,\_jsxs(\_components.p,{children:[`Inputs and outputs are deleted on the backend within 30 days of receipt\nor generation, except in cases outlined in\n`,\_jsx(\_components.a,{href:`https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data`,children:`How long do you store my organization’s data?`}),`.\nData is cached for a number of hours after deletion so users can access\ncontext in recently closed documents.`]}),`\n`,\_jsxs(\_components.p,{children:[`Chat history is stored locally in your browser using IndexedDB. It is\nnot synced across devices and can be cleared from Settings at any time.\nReinstalling the add-in or switching between Claude add-ins does not\nremove it. See `,\_jsx(\_components.a,{href:`/office-agents/data-storage`,children:`Data storage and retention`}),`\nfor where it sits on disk and how long it is kept.`]}),`\n`,\_jsx(\_components.p,{children:`When you sign in with a Claude account, the add-in sends your\nconversations to Anthropic, including the content Claude reads from your\ndocument and any files you attach. Clearing chat history removes only\nthe copy in your browser. It does not delete the messages or attached\nfiles that Anthropic keeps.`}),`\n`,\_jsxs(\_components.p,{children:[`Claude for Word does not inherit custom data retention settings your\norganization might have set. Activity is not included in Enterprise\naudit logs. For Enterprise organizations with the\n`,\_jsx(\_components.a,{href:`https://platform.claude.com/docs/en/manage-claude/compliance-api`,children:`Compliance API`}),`\nenabled, Claude for Word sessions are included in the Compliance API.\nThis coverage requires no additional setup: the same Compliance Access\nKeys apply.`]}),`\n`,\_jsx(\_components.p,{children:`Claude reads the content of your currently open document, including\ntext, comments, tracked changes, footnotes, tables, and bookmarks. It\nonly accesses the document you have open in Word. For highly sensitive\nor regulated data, follow your organization’s data handling policies.`}),`\n`,\_jsx(Heading,{level:`2`,id:`current-limitations`,children:`Current limitations`}),`\n`,\_jsx(\_components.p,{children:`Claude for Word is not recommended for:`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`Final client deliverables or counterparty sends without human review.`}),`\n`,\_jsx(\_components.li,{children:`Litigation filings or audit-critical documents without verification.`}),`\n`,\_jsx(\_components.li,{children:`Replacing legal or financial judgment.`}),`\n`,\_jsx(\_components.li,{children:`Documents containing highly sensitive or privileged data without\nproper controls.`}),`\n`]}),`\n`,\_jsx(Heading,{level:`3`,id:`unsupported-versions`,children:`Unsupported versions`}),`\n`,\_jsx(\_components.p,{children:`The add-in does not run on these Word versions.`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`Word 2016 and 2019 perpetual or volume license.`}),`\n`,\_jsx(\_components.li,{children:`Word on iPad.`}),`\n`,\_jsx(\_components.li,{children:`Word on Android.`}),`\n`,\_jsx(\_components.li,{children:`Microsoft 365 Word builds older than Version 2205 on Windows or\nversion 16.61 on Mac.`}),`\n`,\_jsxs(\_components.li,{children:[`Legacy `,\_jsx(\_components.code,{children:`.doc`}),` files. Save as `,\_jsx(\_components.code,{children:`.docx`}),` first.`]}),`\n`]}),`\n`,\_jsx(Heading,{level:`2`,id:`prompt-injection-risk`,children:`Prompt injection risk`}),`\n`,\_jsx(Warning,{children:\_jsx(\_components.p,{children:`Only use Claude for Word with trusted documents. Documents from external\nsources such as downloaded templates, counterparty files, or files\nshared via email can contain hidden instructions that manipulate the\nadd-in into extracting data, modifying records, or performing\ndestructive actions.`})}),`\n`,\_jsx(\_components.p,{children:`Prompt injection attacks hide malicious instructions in document\ncontent such as text, comments, tracked changes, headers, and footers\nto trick Claude into taking unintended actions. Testing has identified\nscenarios where Claude for Word can be manipulated to:`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`Extract and share sensitive information through web searches\ncontaining your sensitive data or file system access that exposes\nproprietary information.`}),`\n`,\_jsx(\_components.li,{children:`Modify critical content such as contract terms or financial figures.`}),`\n`,\_jsx(\_components.li,{children:`Perform destructive actions without verification when allowed to act\nunsupervised.`}),`\n`]}),`\n`,\_jsx(\_components.p,{children:`When Claude proposes a risky operation, you are asked to confirm before\nit runs. Review confirmations carefully, especially for content from\nexternal sources.`}),`\n`,\_jsx(Heading,{level:`2`,id:`best-practices`,children:`Best practices`}),`\n`,\_jsx(\_components.p,{children:`Follow these guidelines to use Claude for Word safely and effectively.`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`Always review tracked changes before accepting them.`}),`\n`,\_jsx(\_components.li,{children:`Verify that outputs match your firm’s playbook and standard\npositions.`}),`\n`,\_jsx(\_components.li,{children:`Use appropriate permissions and access controls.`}),`\n`,\_jsx(\_components.li,{children:`Maintain human oversight for client-facing work.`}),`\n`]}),`\n`,\_jsx(Heading,{level:`2`,id:`example-use-cases`,children:`Example use cases`}),`\n`,\_jsx(Heading,{level:`3`,id:`legal-contract-review`,children:`Legal contract review`}),`\n`,\_jsx(\_components.p,{children:`Prompts that review and revise contracts and counterparty redlines.`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`“Summarize the key commercial terms: parties, term, governing law,\nand anything off-market.”`}),`\n`,\_jsx(\_components.li,{children:`“Flag provisions that deviate from standard market position, ranked\nby severity.”`}),`\n`,\_jsx(\_components.li,{children:`“Make the indemnification mutual and insert our standard fallback\nlanguage.”`}),`\n`,\_jsx(\_components.li,{children:`“Work through all five reviewer comments as tracked changes.”`}),`\n`,\_jsx(\_components.li,{children:`“What did the counterparty change, and which revisions are\ndealbreakers?”`}),`\n`]}),`\n`,\_jsx(Heading,{level:`3`,id:`finance-memo-drafting`,children:`Finance memo drafting`}),`\n`,\_jsx(\_components.p,{children:`Prompts that build out investment memos and finance writeups.`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`“Draft the Investment Thesis section with three points, pulling the\nnumbers from the uploaded 10-K.”`}),`\n`,\_jsx(\_components.li,{children:`“Populate the summary table with revenue, gross margin, and FCF for\nthe last three years.”`}),`\n`,\_jsx(\_components.li,{children:`“Too generic on point two. Use the customer count from the deck.”`}),`\n`,\_jsx(\_components.li,{children:`“Address the partner’s comment on the Risks section.”`}),`\n`]}),`\n`,\_jsx(Heading,{level:`3`,id:`document-qa-and-consistency`,children:`Document QA and consistency`}),`\n`,\_jsx(\_components.p,{children:`Prompts that check a document for internal consistency and quality.`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`“Flag inconsistent defined terms and broken cross-references.”`}),`\n`,\_jsx(\_components.li,{children:`“Check the numbering scheme for gaps.”`}),`\n`,\_jsx(\_components.li,{children:`“Proofread for spelling, grammar, and punctuation.”`}),`\n`,\_jsx(\_components.li,{children:`“Is the same party referred to by different names anywhere in this\ndocument?”`}),`\n`]}),`\n`,\_jsx(Heading,{level:`3`,id:`general-document-editing`,children:`General document editing`}),`\n`,\_jsx(\_components.p,{children:`Prompts that tighten or restructure prose.`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`“Tighten section 4 and drop the passive voice.”`}),`\n`,\_jsx(\_components.li,{children:`“Rewrite this for a non-technical audience.”`}),`\n`,\_jsx(\_components.li,{children:`“Add a fourth risk addressing customer concentration.”`}),`\n`,\_jsx(\_components.li,{children:`“Define this term and use it consistently throughout.”`}),`\n`]})]})}function MDXContent(props={}){const{wrapper:MDXLayout}={...\_provideComponents(),...props.components};return MDXLayout?\_jsx(MDXLayout,{...props,children:\_jsx(\_createMdxContent,{...props})}):\_createMdxContent(props)}return{default:MDXContent};function \_missingMdxReference(id,component){throw new Error(`Expected `+(component?`component`:`object`)+\" `\"+id+\"` to be defined: you likely forgot to import, pass, or provide it.\")}","frontmatter":{},"scope":{"config":{},"pageMetadata":{"title":"Use Claude for Word","description":"A Word add-in that integrates Claude into your document workflow, for Pro, Max, Team, and Enterprise plans.","href":"/office-agents/word"}}},"mdxSourceWithNoJs":null},"mdxExtracts":{"tableOfContents":[{"title":"What you can do","slug":"what-you-can-do","depth":2,"children":[]},{"title":"Get started with Claude for Word","slug":"get-started-with-claude-for-word","depth":2,"children":[{"title":"Supported versions","slug":"supported-versions","depth":3,"children":[]},{"title":"Install for yourself","slug":"install-for-yourself","depth":3,"children":[]},{"title":"Deploy to your organization","slug":"deploy-to-your-organization","depth":3,"children":[]},{"title":"Deploy with a custom manifest","slug":"deploy-with-a-custom-manifest","depth":3,"children":[]},{"title":"Connect through a third-party platform","slug":"connect-through-a-third-party-platform","depth":3,"children":[]}]},{"title":"Key features","slug":"key-features","depth":2,"children":[{"title":"Read and understand documents","slug":"read-and-understand-documents","depth":3,"children":[]},{"title":"Edit selected text","slug":"edit-selected-text","depth":3,"children":[]},{"title":"Tracked changes mode","slug":"tracked-changes-mode","depth":3,"children":[]},{"title":"Comment-driven editing","slug":"comment-driven-editing","depth":3,"children":[]},{"title":"Summarize counterparty redlines","slug":"summarize-counterparty-redlines","depth":3,"children":[]},{"title":"Fill templates","slug":"fill-templates","depth":3,"children":[]},{"title":"Semantic navigation","slug":"semantic-navigation","depth":3,"children":[]}]},{"title":"Connectors and Skills","slug":"connectors-and-skills","depth":2,"children":[]},{"title":"Set persistent instructions","slug":"set-persistent-instructions","depth":2,"children":[]},{"title":"Work across M365 apps","slug":"work-across-m365-apps","depth":2,"children":[]},{"title":"Context and session management","slug":"context-and-session-management","depth":2,"children":[]},{"title":"Models available","slug":"models-available","depth":2,"children":[]},{"title":"Data handling","slug":"data-handling","depth":2,"children":[]},{"title":"Current limitations","slug":"current-limitations","depth":2,"children":[{"title":"Unsupported versions","slug":"unsupported-versions","depth":3,"children":[]}]},{"title":"Prompt injection risk","slug":"prompt-injection-risk","depth":2,"children":[]},{"title":"Best practices","slug":"best-practices","depth":2,"children":[]},{"title":"Example use cases","slug":"example-use-cases","depth":2,"children":[{"title":"Legal contract review","slug":"legal-contract-review","depth":3,"children":[]},{"title":"Finance memo drafting","slug":"finance-memo-drafting","depth":3,"children":[]},{"title":"Document QA and consistency","slug":"document-qa-and-consistency","depth":3,"children":[]},{"title":"General document editing","slug":"general-document-editing","depth":3,"children":[]}]}],"codeExamples":{}},"jsLinks":["/docs/\_mintlify/custom/claude-ai/b857db804a3a9481/desktop-app-nav.js"],"subdomain":"claude-ai","siteName":"Claude.ai Documentation","title":"Use Claude for Word - Claude.ai Documentation","navMaps":{"firstHrefInVersion":{},"firstHrefInLanguage":{}},"lastModified":"2026-10-31T01:01:21.373Z","originalFileLocation":"office-agents/word.mdx"},"headHtml":"\u003cscript data-mint-head>(function(){var d=document.documentElement,p=null;if(!p){try{p=localStorage.getItem(\"isDarkMode\")}catch(e){}if(p==='true')p='dark';else if(p==='false')p='light';if(p!=='light'\u0026\u0026p!=='dark'\u0026\u0026p!=='system')p=\"system\"}var r=p==='system'?(matchMedia(\"(prefers-color-scheme: dark)\").matches?'dark':'light'):p;d.classList.remove(r==='dark'?'light':'dark');d.classList.add(r);d.setAttribute(\"data-theme-preference\",p)})();\u003c/script>\u003cmeta data-mint-head name=\"description\" content=\"A Word add-in that integrates Claude into your document workflow, for Pro, Max, Team, and Enterprise plans.\">\u003cmeta data-mint-head name=\"application-name\" content=\"Claude.ai Documentation\">\u003cmeta data-mint-head name=\"generator\" content=\"Mintlify\">\u003clink data-mint-head rel=\"icon\" type=\"image/png\" sizes=\"192x192\" href=\"/docs/mintlify-assets/\_mintlify/favicons/claude-ai/zHw4o4W7dZma2XXV/\_generated/favicon/android-chrome-192x192.png\" media=\"(prefers-color-scheme: light)\">\u003clink data-mint-head rel=\"apple-touch-icon\" type=\"image/png\" sizes=\"180x180\" href=\"/docs/mintlify-assets/\_mintlify/favicons/claude-ai/zHw4o4W7dZma2XXV/\_generated/favicon/apple-touch-icon.png\">\u003clink data-mint-head rel=\"icon\" type=\"image/png\" sizes=\"16x16\" href=\"/docs/mintlify-assets/\_mintlify/favicons/claude-ai/zHw4o4W7dZma2XXV/\_generated/favicon/favicon-16x16.png\" media=\"(prefers-color-scheme: light)\">\u003clink data-mint-head rel=\"icon\" type=\"image/png\" sizes=\"32x32\" href=\"/docs/mintlify-assets/\_mintlify/favicons/claude-ai/zHw4o4W7dZma2XXV/\_generated/favicon/favicon-32x32.png\" media=\"(prefers-color-scheme: light)\">\u003clink data-mint-head rel=\"shortcut icon\" type=\"image/x-icon\" href=\"/docs/mintlify-assets/\_mintlify/favicons/claude-ai/zHw4o4W7dZma2XXV/\_generated/favicon/favicon.ico\" media=\"(prefers-color-scheme: light)\">\u003clink data-mint-head rel=\"icon\" type=\"image/png\" sizes=\"192x192\" href=\"/docs/mintlify-assets/\_mintlify/favicons/claude-ai/zHw4o4W7dZma2XXV/\_generated/favicon-dark/android-chrome-192x192.png\" media=\"(prefers-color-scheme: dark)\">\u003clink data-mint-head rel=\"icon\" type=\"image/png\" sizes=\"16x16\" href=\"/docs/mintlify-assets/\_mintlify/favicons/claude-ai/zHw4o4W7dZma2XXV/\_generated/favicon-dark/favicon-16x16.png\" media=\"(prefers-color-scheme: dark)\">\u003clink data-mint-head rel=\"icon\" type=\"image/png\" sizes=\"32x32\" href=\"/docs/mintlify-assets/\_mintlify/favicons/claude-ai/zHw4o4W7dZma2XXV/\_generated/favicon-dark/favicon-32x32.png\" media=\"(prefers-color-scheme: dark)\">\u003clink data-mint-head rel=\"shortcut icon\" type=\"image/x-icon\" href=\"/docs/mintlify-assets/\_mintlify/favicons/claude-ai/zHw4o4W7dZma2XXV/\_generated/favicon-dark/favicon.ico\" media=\"(prefers-color-scheme: dark)\">\u003cmeta data-mint-head property=\"og:title\" content=\"Use Claude for Word - Claude.ai Documentation\">\u003cmeta data-mint-head property=\"og:description\" content=\"A Word add-in that integrates Claude into your document workflow, for Pro, Max, Team, and Enterprise plans.\">\u003cmeta data-mint-head property=\"og:site\_name\" content=\"Claude.ai Documentation\">\u003cmeta data-mint-head property=\"og:url\" content=\"https://claude.com/docs/office-agents/word\">\u003cmeta data-mint-head property=\"og:type\" content=\"website\">\u003cmeta data-mint-head property=\"og:image\" content=\"https://claude-ai.mintlify.site/docs/\_mintlify/api/og/v2?division=+\u0026amp;title=Use+Claude+for+Word\u0026amp;description=A+Word+add-in+that+integrates+Claude+into+your+document+workflow%2C+for+Pro%2C+Max%2C+Team%2C+and+Enterprise+plans.\u0026amp;theme=c937feb09b37748e448783d0\u0026amp;signature=7d30fa96ae780c48b9843ed0680644959c3cc715e015c4e80553b13f7154c05e\">\u003cmeta data-mint-head property=\"og:image:width\" content=\"1200\">\u003cmeta data-mint-head property=\"og:image:height\" content=\"630\">\u003cmeta data-mint-head name=\"twitter:card\" content=\"summary\_large\_image\">\u003cmeta data-mint-head name=\"twitter:title\" content=\"Use Claude for Word - Claude.ai Documentation\">\u003cmeta data-mint-head name=\"twitter:description\" content=\"A Word add-in that integrates Claude into your document workflow, for Pro, Max, Team, and Enterprise plans.\">\u003cmeta data-mint-head name=\"twitter:image\" content=\"https://claude-ai.mintlify.site/docs/\_mintlify/api/og/v2?division=+\u0026amp;title=Use+Claude+for+Word\u0026amp;description=A+Word+add-in+that+integrates+Claude+into+your+document+workflow%2C+for+Pro%2C+Max%2C+Team%2C+and+Enterprise+plans.\u0026amp;theme=c937feb09b37748e448783d0\u0026amp;signature=7d30fa96ae780c48b9843ed0680644959c3cc715e015c4e80553b13f7154c05e\">\u003cmeta data-mint-head name=\"twitter:image:width\" content=\"1200\">\u003cmeta data-mint-head name=\"twitter:image:height\" content=\"630\">\u003cmeta data-mint-head name=\"msapplication-config\" content=\"/docs/mintlify-assets/\_mintlify/favicons/claude-ai/zHw4o4W7dZma2XXV/\_generated/favicon/browserconfig.xml\">\u003cmeta data-mint-head name=\"apple-mobile-web-app-title\" content=\"Claude.ai Documentation\">\u003cmeta data-mint-head name=\"msapplication-TileColor\" content=\"#0E0E0E\">\u003clink data-mint-head rel=\"canonical\" href=\"https://claude.com/docs/office-agents/word\">\u003clink data-mint-head rel=\"alternate\" type=\"application/xml\" href=\"/docs/sitemap.xml\">\u003clink data-mint-head rel=\"alternate\" type=\"text/markdown\" href=\"/docs/office-agents/word.md\">\u003cscript data-mint-head type=\"application/ld+json\">{\"@context\":\"https://schema.org\",\"@graph\":[{\"@type\":\"Organization\",\"@id\":\"https://claude.com/#organization\",\"name\":\"Claude.ai Documentation\",\"url\":\"https://claude.com\",\"logo\":{\"@type\":\"ImageObject\",\"url\":\"https://mintcdn.com/claude-ai/1fyDNLAICe3KG6rB/logo/light.svg?fit=max\u0026auto=format\u0026n=1fyDNLAICe3KG6rB\u0026q=85\u0026s=e870c19cb781d8a7c7b7d19de53b0a10\"}},{\"@type\":\"WebSite\",\"@id\":\"https://claude.com/docs#website\",\"name\":\"Claude.ai Documentation\",\"url\":\"https://claude.com/docs\",\"publisher\":{\"@id\":\"https://claude.com/#organization\"}},{\"@type\":\"WebPage\",\"@id\":\"https://claude.com/docs/office-agents/word#webpage\",\"url\":\"https://claude.com/docs/office-agents/word\",\"name\":\"Use Claude for Word\",\"description\":\"A Word add-in that integrates Claude into your document workflow, for Pro, Max, Team, and Enterprise plans.\",\"dateModified\":\"2026-10-31T01:01:21.373Z\",\"isPartOf\":{\"@id\":\"https://claude.com/docs#website\"},\"breadcrumb\":{\"@id\":\"https://claude.com/docs/office-agents/word#breadcrumb\"}},{\"@type\":\"BreadcrumbList\",\"@id\":\"https://claude.com/docs/office-agents/word#breadcrumb\",\"itemListElement\":[{\"@type\":\"ListItem\",\"position\":1,\"name\":\" \",\"item\":\"https://claude.com/docs/office-agents/overview\"},{\"@type\":\"ListItem\",\"position\":2,\"name\":\"Use Claude for Word\",\"item\":\"https://claude.com/docs/office-agents/word\"}]},{\"@type\":[\"Article\",\"TechArticle\"],\"@id\":\"https://claude.com/docs/office-agents/word#article\",\"headline\":\"Use Claude for Word\",\"name\":\"Use Claude for Word\",\"description\":\"A Word add-in that integrates Claude into your document workflow, for Pro, Max, Team, and Enterprise plans.\",\"url\":\"https://claude.com/docs/office-agents/word\",\"mainEntityOfPage\":{\"@id\":\"https://claude.com/docs/office-agents/word#webpage\"},\"dateModified\":\"2026-10-31T01:01:21.373Z\",\"publisher\":{\"@id\":\"https://claude.com/#organization\"},\"isPartOf\":{\"@id\":\"https://claude.com/docs#website\"}}]}\u003c/script>","siteName":"Claude.ai Documentation","nav":{"global":null,"tabs":[{"tab":"Welcome","pages":[{"title":"Welcome","href":""}]},{"tab":"Customize Claude","pages":[{"title":"Customize Claude","href":"/extend/overview"}]},{"tab":"Build for Claude","pages":[{"title":"Build for Claude","href":"/build/overview"}]},{"tab":"Cowork","pages":[{"title":"Cowork","href":"/cowork/overview"}]},{"tab":"Claude Tag","pages":[{"title":"Claude Tag","href":"/claude-tag/overview"}]},{"tab":"Claude for M365","groups":[{"group":" ","pages":[{"sidebarTitle":"Overview","title":"Claude for M365 overview","href":"/office-agents/overview"},{"title":"Use Claude for Excel","href":"/office-agents/excel"},{"title":"Use Claude for PowerPoint","description":"A PowerPoint add-in that integrates Claude into your presentation workflow, for Pro, Max, Team, and Enterprise plans.","href":"/office-agents/powerpoint"},{"title":"Use Claude for Word","href":"/office-agents/word"},{"title":"Use Claude for Outlook","description":"An Outlook add-in that integrates Claude into your inbox and calendar, for Pro, Max, Team, and Enterprise plans.","href":"/office-agents/outlook"}]},{"group":"Features","pages":[{"title":"Work across M365 apps","href":"/office-agents/work-across-apps"},{"title":"Use dictation in Claude for M365","href":"/office-agents/dictation"},{"title":"Connectors and Skills","href":"/office-agents/connectors-and-skills"}]},{"group":"Administration","pages":[{"title":"Security, admin auditability, and analytics","href":"/office-agents/enterprise-readiness"},{"title":"Configure a custom OpenTelemetry collector","href":"/office-agents/opentelemetry"},{"title":"Performance and limits","href":"/office-agents/performance"},{"title":"Data storage and retention","href":"/office-agents/data-storage"},{"title":"Use Claude for M365 with third-party platforms","href":"/office-agents/third-party-platforms"},{"title":"Install financial services plugins for Cowork","href":"/office-agents/fsi-plugins"}]}]},{"tab":"Claude Science","pages":[{"title":"Claude Science","href":"/claude-science/overview"}]},{"tab":"Claude on third-party platforms","pages":[{"title":"Claude on third-party platforms","href":"/third-party/claude-desktop/overview"}]},{"tab":"Claude self-hosted","hidden":true,"pages":[{"title":"Claude self-hosted","href":"/third-party/claude-desktop/self-hosted/overview"}]},{"tab":"Claude for Government","pages":[{"title":"Claude for Government","href":"/government/overview"}]}]},"basePath":"","title":"Use Claude for Word - Claude.ai Documentation","buildId":"dpl\_ATnXPMW25DMPUr9VBw6kL6MfBt6T","deploymentId":"dpl\_ATnXPMW25DMPUr9VBw6kL6MfBt6T","dynamics":[],"chunks":[]}
