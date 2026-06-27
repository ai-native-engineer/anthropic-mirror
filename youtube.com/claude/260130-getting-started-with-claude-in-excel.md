---
title: "Getting started with Claude in Excel"
channel: claude
url: https://www.youtube.com/watch?v=54BdUqMQUMI
youtube_id: 54BdUqMQUMI
published: 2026-01-30
duration: "7:10"
captions: en-orig
---

# Getting started with Claude in Excel

[![Getting started with Claude in Excel](https://img.youtube.com/vi/54BdUqMQUMI/hqdefault.jpg)](https://www.youtube.com/watch?v=54BdUqMQUMI)

<details>
<summary>자막: Getting started with Claude in Excel (7:10)</summary>

[00:00]
Claude in Excel is a powerful AI agent
right inside your spreadsheet.
Everything you do manually, Claude can
help with.
Whether you're in finance building
valuation models, in accounting
reconciling data, or in operations
tracking performance, Claude can work
the way that you do.
You open it with control option C on Mac
or control alt C on Windows.
So, let's try starting by asking
questions about your workbook. Claude
can look through the data and use it to
answer questions that would otherwise
require manual calculation.
Here's an expense report with seven line
items. I want to keep my travel and meal
budget under 40% of my total spend. So,
let's ask Claude, "I'm trying to keep my
travel and meal budget to under 40% of
my total costs. Did I hit that target?"
Then, Claude calculates the total, adds

[00:01]
up travel and meals, computes the
percentage, and tells me I'm just under
budget. It shows the math so I can
verify.
Claude can also help you with errors. It
knows what error messages mean, and
couples that with knowledge of your data
set to provide more valuable debugging
information. So, right here, we have a
monthly sales sheet with an error in the
average price column for May.
To find out the problem, we can simply
ask, "Why is there an error in May?"
Claude traces the error to its source.
The formula in D6 divides revenue by
units, but cells C6 is empty. So, no
units mean division by zero. Claude
suggests a fix, fill in the missing
data.
So, Claude traced the error without me
having to click into the cell, read the
formula, and check each reference
manually. It just did it on its own.
Formulas can be opaque, especially in
spreadsheets that you didn't build.
Claude can break them down for you.

[00:02]
So, here's a grade book right here that
uses VLOOKUP to convert numeric scores
into letter grades. If you inherit this
spreadsheet, the grading logic might not
be obvious just from looking at it. I
know it isn't to me.
So, when we ask Claude, "How does the
letter grade formula work?" Claude
breaks down the formula piece by piece.
It gives us citation boxes so we can
jump directly to the cells being
referenced. It shows that the formula is
in column C and that is VLOOKUP.
Then it explains the parameter, the
lookup value, the table array, the
column index, and that true means
approximate matching.
So far, we've asked Claude single
questions, but Claude can also work
through multi-step tasks like cleaning
messy data and building a model from
scratch.
This workbook right here has a raw sales
sheet with monthly revenue data from the
past 3 years.
But before we can build anything useful,
we need to clean this up. So, we can

[00:03]
give Claude a clear prompt. Clean the
raw sales data, standardize all dates to
YYYYMMDD
format, remove duplicate entries, sort
by date, and create a summary of an
annual view in a new sheet called
historical.
Claude asked for permission before
modifying the spreadsheet. Once I
approve, it works through the data and
reports what it did.
It standardized all the date formats. It
removed three duplicate entries and
sorted 34 remaining records
chronologically. It also created a
historical sheet with annual revenue
totals and transaction counts for each
year. Claude even adds context. 2024
revenue shows a 16% increase over 2023
and 2025 is on track to finish strong
with only 10 months of data recorded.
Awesome. Now we have clean historical
data.
Let's build a forecast.
Based on the historical revenue, build a
three-year forecast on the forecast
sheet and calculate the average annual
growth rate and use it to project 2026,

[00:04]
2027, and 2028. Put the growth rate
assumption on the assumption sheet so I
can adjust it later.
It fills in the assumption sheet with
this rate and builds out the forecast
sheet with projections through 2028. The
model is fully dynamic. All forecast
values are linked via formulas to the
growth rate and the assumption sheet.
Claude also adds context noting that
2025 only includes 10 months of data,
which affects the calculated growth
rate.
The same approach works for finance
professionals needing more complex
financial analysis.
Here's a workbook with five years of
historical financials.
We can ask Claude to build a DCF model
to value this company, use a 10%
discount rate, 3% terminal growth, and
project five years of cash flows based
on historical trends. Show me the
implied enterprise value.
Claude analyzes the historical growth
rate and margins, fills in the
assumption sheet, and builds out a
complete DCF model. It projects free
cash flows, calculates the terminal

[00:05]
value, discounts everything back to
present value, and shows the implied
enterprise value. The model is fully
dynamic. If I want to test different
assumptions, I can ask Claude to adjust
the discount rate or growth rate and the
valuation updates automatically.
Pivot tables are one of Excel's most
powerful features and one of its hardest
to master. Claude can build them for
you. This workbook right here has a year
of sales transactions, dates, regions,
products, sales reps, and revenue.
Create a pivot table showing total
revenue by region and product.
Claude builds the pivot table organizing
revenue by region in the rows and
product in the same columns.
It's the same pivot table you'd build
manually, but Claude handles the setup.
Now, create a chart from this pivot
table showing revenue by region.
Claude creates a chart from the pivot
table. It chooses an appropriate chart
type and adds labels. Claude can then
edit any part of the chart, the type,
the axes, the title, or the colors.

[00:06]
Change the chart to be a stacked bar
chart and add a title.
Claude shows you every change it makes
and explains its reasoning.
Use this transparency.
You can click the citation boxes in
Claude's responses to jump directly to
the cells being referenced.
Your organization may have specific
methodologies.
Verify the output smash your standards,
especially for work that will be shared
externally.
And for sensitive or regulated data,
always follow your organization's data
handling policies.
Whether you're in finance building
valuation models, in accounting cleaning
up GL data, in operations analyzing
sales performance, or just someone who
uses Excel extensively, Claude can help
you move much faster.
Claude compresses the mechanical work so
you can focus on the decisions. What
assumptions to use? What scenarios to
test? And what story does the data tell?

[00:07]
Open the sidebar with control option C
on Mac or control alt C on Windows.

</details>
