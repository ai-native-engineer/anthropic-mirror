<!-- source: https://claude.com/docs/office-agents/excel -->

Claude for Excel is an add-in that brings Claude into Excel. Ask questions
about open workbooks, adjust assumptions while preserving formula
relationships, debug errors, and build or populate models, all without
leaving Excel.

Claude for Excel is generally available to Pro, Max, Team,

With Claude for Excel, you can:

* Ask questions about your workbook and get answers with cell-level
  citations.
* Adjust assumptions while keeping formula relationships intact.
* Identify and resolve errors and their root causes.
* Generate new spreadsheet models or populate existing templates.
* Work across multi-tab workbooks.
* Pull external context through connectors such as S&P Global, LSEG,
  and Daloopa.
* Apply enabled Skills automatically while you work.

##  Get started with Claude for Excel

Claude for Excel runs on the following Excel builds.

* Excel on the web
* Excel on Windows with a Microsoft 365 subscription, build 16.0.13127.20296 or later
* Excel on Mac, version 16.46 or later, build 21011600 or later

Open Excel, activate the add-in, and sign in with your Claude account.

Organization admins can deploy Claude for Excel through the Microsoft 365
Admin Center.

For environments where “Let users access the Office Store” is disabled,
deploy using the custom manifest XML file instead. Download the
[Excel manifest XML file](https://pivot.claude.ai/manifest-excel.xml),
then follow
[Deploy with a custom manifest](https://claude.com/docs/office-agents/word#deploy-with-a-custom-manifest)
for the upload steps. The flow is identical apart from which manifest
file you upload in Step 1.

###  Understand complex models

Ask Claude to trace assumptions, explain formulas, or walk through how a
number was derived. Answers include cell-level citations you can click
to navigate to the referenced cell.

* “Walk me through how the revenue number in cell C42 is calculated.”
* “What assumptions drive the gross margin forecast?”

###  Update values safely

Claude updates cell values while keeping formula relationships intact,
so downstream cells recompute correctly.

* “Change the discount rate to 8% and update dependent calculations.”
* “Flex the growth rate from 5% to 10% and show me the impact on terminal
  value.”

###  Build templates and models

Populate an existing template or generate a new model from a natural
language description.

* “Populate this LBO template with a $500M purchase price and 6x
  leverage.”
* “Build a three-statement model from this trial balance.”

###  Debug errors

Locate the root cause of calculation errors and suggest fixes.

* “Find the source of the #REF! error in the summary tab.”
* “Trace why cell H15 is returning #DIV/0.”

###  Native Excel operations

Claude can sort, filter, edit pivot tables, apply conditional
formatting, and create data validation dropdowns. Ask for these
directly.

Claude for Excel supports connectors for pulling external context into
your workbook, and Skills for applying reusable task recipes. See

apply to every conversation in Excel. Instructions are useful for
formatting conventions such as “format numbers with thousand separators”
or “always bold column headers”, currency or locale preferences, or
recurring context about your workflow.
Instructions you set in Excel only apply to Excel. They are separate
from Instructions you set in PowerPoint or Word.

Claude for Excel shares context with Claude for PowerPoint, Word, and
Outlook, so a single conversation can span your open workbook,
presentation, document, and inbox. See

The add-in handles long sessions and protects against accidental
overwrites for you.

* **Overwrite protection**: Claude warns you before overwriting existing
  data to avoid accidental data loss.

Your use of Claude for Excel is associated with your existing Claude
account and is subject to the same usage limits.

context in recently closed workbooks.
Claude for Excel does not inherit custom data retention settings your
organization might have set. Activity is not included in Enterprise
enabled, Claude for Excel sessions are included in the Compliance API.

Claude for Excel is not recommended for:

* Final client deliverables without human review.
* Audit-critical calculations without verification.
* Models containing highly sensitive or regulated data without proper
  controls.

Unsupported capabilities:

* Data tables.
* Macros and VBA operations.

The add-in does not run on these Excel versions.

* Excel 2016 and 2019 perpetual or volume license.
* Excel on iPad. The add-in requires SharedRuntime support, which iPad
  does not provide.
* Excel on Android.
* Older builds of Microsoft 365 Excel below the SharedRuntime threshold.

Only use Claude for Excel with trusted spreadsheets. Files from external
sources can contain hidden instructions that manipulate the add-in into
extracting data, modifying records, or performing destructive actions.

External files such as downloaded templates, vendor files, and data
imports can contain prompt injections that try to trick Claude into
taking unintended actions. Testing has identified scenarios where Claude for
Excel can be manipulated to extract sensitive information, modify
critical data, or perform destructive actions if allowed to act without
verification.
it runs. Review confirmations carefully, especially for files from

Follow these guidelines to use Claude for Excel safely and effectively.

* Always review changes before finalizing your work.
* Start with a trusted copy of the workbook before asking Claude to edit
  widely.
* Be specific about what you want changed.
* Verify that outputs match your organization’s standards and your own
  judgment.
