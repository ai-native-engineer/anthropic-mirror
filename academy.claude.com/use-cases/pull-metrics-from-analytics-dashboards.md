<!-- source: https://academy.claude.com/use-cases/pull-metrics-from-analytics-dashboards -->

![Pull metrics from analytics dashboards result](https://academy.claude.com/assets/v1/pull-metrics-from-analytics-dashboards-ot36n6cn.png)

## 1. Describe the task

Claude navigates your analytics dashboards—Amplitude, Mixpanel, or other tools—and extracts the metrics you specify. It reads the same reports you would, pulls the numbers, and compiles them into a summary you can paste into a team update or Slack.

Specify which metrics matter and from which tools. Claude handles the navigation and extraction.

Pull my weekly metrics from both my Amplitude and Mixpanel open tabs.

**From Amplitude:**

* Weekly active users (WAU) — past 4 weeks
* New user signups — this week vs. last week
* Retention (Day 1, Day 7, Day 30) — for the cohort from 30 days ago

**From Mixpanel:**

* Feature adoption rate for new dashboard (% of WAU who used it)
* Conversion rate through onboarding flow
* Top 5 events by volume this week

**Output:** Format as a summary I can paste into our weekly product update.

Copy prompt

## 2. Give Claude context

Claude uses browser use to navigate your analytics tools through your existing browser sessions. If you're logged into Amplitude and Mixpanel, Claude can access the same dashboards and reports you see—no API keys or integrations to configure.

### Required context

Log into your analytics tools in Chrome before starting. Claude navigates to the dashboards and reports using your sessions.

## 3. What Claude creates

Claude compiles metrics from both tools into a single summary.

**Weekly Product Metrics Summary**

**User Growth**

*Source: Amplitude*

| Week | WAU | Change |
| --- | --- | --- |
| 4 weeks ago | 24,312 | — |
| 3 weeks ago | 25,891 | +6.5% |
| 2 weeks ago | 26,455 | +2.2% |
| This week | 27,102 | +2.4% |

**Key Stats:**

* **New signups:** 1,847 this week vs 1,623 last week (+13.8%)
* **Retention (30-day-old cohort):** Day 1: 68% → Day 7: 41% → Day 30: 23%

**Feature Engagement**

*Source: Mixpanel*

* **New dashboard adoption:** 34% of WAU (up from 28% last week)
* **Onboarding conversion:** 71% complete the full flow

**Top Events This Week:**

| Event | Count |
| --- | --- |
| Dashboard viewed | 45,221 |
| Report exported | 12,847 |
| Filter applied | 11,293 |
| Team member invited | 4,891 |
| Integration connected | 3,442 |

**Summary for Your Update**

WAU grew **11.5% over the past month** to 27.1K. New signups are up 14% week-over-week. The new dashboard is seeing solid adoption at 34% of active users. Retention remains steady with 23% of users still active at Day 30.

## 4. Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Dig into a specific metric

Have Claude investigate before you share the report and get more detail when something looks off.

The onboarding conversion dropped from 78% last week. Can you go into Mixpanel and show me where in the flow people are dropping off? I need to understand this before the meeting.

Copy prompt

### Share the output in a different channel

Once your summary is ready, have Claude format it and post it directly to your team channel.

This looks good. Can you turn it into a few bullet points and post it to #product-weekly in Slack? Just the highlights and anything that changed significantly.

Copy prompt

### Add another data source

Pull in another data source without starting over. Claude can look in a new tab and add to your summary.

Can you also pull our revenue metrics from Stripe? I need MRR, new subscriptions this week, and churn rate. Add them to the summary.

Copy prompt

## 5. Tricks, tips, and troubleshooting

### Schedule weekly metrics pulls

Click the clock icon in the extension panel to schedule this workflow. Set it to run Monday morning and Claude will have your metrics summary ready before your weekly product sync. No more scrambling to pull numbers before the meeting.

### Drag all your analytics tabs into one group

For multi-tool metrics, drag Amplitude, Mixpanel, and any other dashboards into Claude's tab group. You'll see a green banner confirming Claude can access all of them. Now Claude reads across every tool simultaneously—no manual switching.

### Save your workflow as a shortcut

Once you have a metrics pull that covers what you need, save it as a shortcut by clicking on the shortcut icon below a successful prompt. You can also set a schedule for when you want the workflow to run next. Alternatively, manually trigger the workflow, by typing "/" and selecting the shortcut.

### Grant permission to your analytics platforms

If Claude asks for permission on every dashboard page, go to Settings → Permissions and enable "Always allow actions on this site" for Amplitude, Mixpanel, and other trusted work tools. Persistent access speeds up multi-page navigation significantly.

## 6. Ready to try for yourself?

Claude in Chrome is available to all paid plan users. Install the extension, log into your analytics tools, and describe the metrics you need. Claude navigates the dashboards and compiles a summary ready to paste into your team update.

[Try in Claude(opens in new tab)](https://claude.com/download)
