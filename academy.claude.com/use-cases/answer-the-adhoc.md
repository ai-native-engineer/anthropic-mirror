<!-- source: https://academy.claude.com/use-cases/answer-the-adhoc -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Answer the ad-hoc data question

The query, the chart, and the plain-English answer.

10 minDataClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-f72xos2e.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-j0qghno4.png)

## Set up[](#set-up)

### Try a plugin[](#try-a-plugin)

The Data plugin ships with `/write-query` and other warehouse-and-BI skills as a starting point, already structured to read a data model and write queries against it. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Data10 skills for SQL generation, table profiling, dashboard specs, and metric narratives

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=data)

`/write-query`Read the warehouse model, write the SQL, and answer the business question

[Run](claude://cowork/new?q=%2Fwrite-query)

`/explore-data`Profile a table and summarize what's in it

[Run](claude://cowork/new?q=%2Fexplore-data)

Show all 9 skills

### Connect your tools[](#connect-your-tools)

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

Databricks

Read the semantic layer and run SQL against the lakehouse so the answer comes with the query.

[Connect](https://claude.ai/desktop/directory/databricks)

![](images/3cb5db332ced9f49.svg)

Microsoft 365

Pull the stakeholder's question from Teams or email and write the answer back as a reply.

[Connect](https://claude.ai/desktop/directory/microsoft-365)

![](https://academy.claude.com/assets/v1/snowflake-f7euzg40.svg)

SnowflakeOptional

Query the warehouse directly when the answer isn't in the semantic model yet.

[Connect](https://claude.ai/desktop/directory/snowflake)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder[](#set-your-working-folder)

Drag the files you'll use (your schema export or dbt models, your metrics library, your data dictionary) into one folder and point Cowork at it. Cowork reads the model from there and writes the SQL, the result table, and the answer memo back to it. If you field ad-hoc questions regularly, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so your naming conventions and certified-metric list stay attached.

Analytics / EMEA-margin-question

finance-schema.sqlApr 22, 2026312 KB

metrics-library.mdMar 30, 202618 KB

data-dictionary.xlsxFeb 14, 202662 KB

In Cowork’s chat bar:Analytics / EMEA-margin-question

## The prompt[](#the-prompt)

### Copy this into Claude Cowork[](#copy-this-into-claude-cowork)

Here's the question from the business: "Why is gross margin down in EMEA this quarter?" Write the SQL to answer it, run it against the warehouse, and tell me what's driving the move. Then give me the chart spec to add to the dashboard so nobody has to ask again.

Analytics / EMEA-margin-questionOpen in Cowork

### Why this works[](#why-this-works)

Prompt

**Paste the question verbatim.** Using their exact words keeps the answer aimed at what they asked, in the terms they used.

Prompt

**Ask for what's driving the number.** "What's driving the move" is asking for the breakdown behind the number: which segment, which change, which date.

Prompt

**Ask for a reusable output.** "Chart spec to add to the dashboard" is asking for something the asker can refresh themselves next time.

Source

**Let the working folder supply context.** SQL is written against your tables and your metric names, not invented ones.

### Get a better draft[](#get-a-better-draft)

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you[](#make-cowork-work-for-you)

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /write-query skill with my feedback.

AnalyticsOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable[](#make-it-repeatable)

### Run it on every inbound question[](#run-it-on-every-inbound-question)

The ad-hoc queue never stops. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill watches your analytics-requests channel and drafts the query and answer before you've even read the message.

**/schedule** Every hour, check #analytics-requests for new questions, run /write-query on each one, and write the draft answer to Analytics/Inbox/<thread-id>.md for me to review before it goes back.

AnalyticsOpen in Cowork

Scheduled taskActive

Ad-hoc analytics inbox

Hourly, reads new questions in #analytics-requests, runs `/write-query` against the warehouse, and writes a draft answer for review.

Every **hour on weekdays**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates[](#share-with-your-teammates)

Your customized `/write-query` now carries your warehouse model, your certified metrics, and your answer format. Share it so every analyst writes SQL against the same definitions, and the business gets the same number no matter who they ask.

Share the skill

In Cowork, open **Skills** → `/write-query` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your model and naming rules baked in, so they don't repeat Steps 1-3.

## What changes for the analytics queue[](#what-changes-for-the-analytics-queue)

Ad-hoc data questions are answered with a working query and explanation drafted together — you review and correct instead of writing SQL from scratch.

You did this for one margin question. The same approach covers cohort retention, funnel conversion, and anomaly checks — each one becomes a skill your team runs the same way.

### Finish it where the file lives

[![](https://academy.claude.com/surfaces/excel-icon.svg)

Claude in Excel

Validate the numbers in a workbook

Install](https://claude.com/claude-for-excel)

[Next: Metrics deep-dive → narrative](https://academy.claude.com/use-cases/metrics-narrative)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for the analytics queue](#what-changes-for-the-analytics-queue)
