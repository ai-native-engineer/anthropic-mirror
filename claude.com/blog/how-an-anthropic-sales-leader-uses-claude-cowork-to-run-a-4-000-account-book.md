<!-- source: https://claude.com/blog/how-an-anthropic-sales-leader-uses-claude-cowork-to-run-a-4-000-account-book -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22349f86cd1968deab7_f06ca06f9d08ca4a85f26357eb896c3730274507-1000x1000.svg)

# How an Anthropic sales leader uses Claude Cowork to run a 4,000-account book

*Travis Bryant, Head of US Mid-Market GTM at Anthropic, shares how he uses Claude Cowork to prepare customer briefs and weekly forecasts, and to run an overnight territory scoring that used to take cross-functional teams hundreds of hours.*

‍

Travis walks through how he uses Claude Cowork to prepare customer briefs, pull weekly forecasts, and score 4,000 accounts overnight.

Join the webinar

[Join the webinar](https://www.anthropic.com/webinars/how-anthropics-sales-leader-runs-his-week-with-claude)Join the webinar

  [Enterprise AI](https://claude.com/blog/category/enterprise-ai)
* Product

  Claude Cowork
* Date

  May 20, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/how-an-anthropic-sales-leader-uses-claude-cowork-to-run-a-4-000-account-book

In sales leadership, the job is to make judgment calls: where to invest the team's hours, and what to tell leadership about how the quarter is shaping up. The work surrounding those decisions, like assembling data from four systems and re-baselining numbers every time numbers refresh, used to eat most of my week. [Claude Cowork](http://claude.com/cowork) has shifted that balance: it handles the data assembly and reformatting, so I can dedicate more time to customer conversations and strategic decisions.

I run US mid-market go-to-market at Anthropic, which means I'm responsible for 4,000 accounts split between mid-market tech and industries. Mid-market includes tech companies that aren't startups anymore, but aren't large enterprises yet either. Industries cover everything else, from financial services and healthcare to retail and manufacturing.

My work spans three cadences: daily customer call prep, the weekly forecast rollup to Anthropic's sales leadership, and quarterly territory and prospect-list work across the full 4,000-account book. Each is a lot of work on its own and doing all three well used to be impossible.

I tried Claude Code, but never got comfortable with working with the terminal. Claude Cowork wraps the same engine in an interface I can work in. That was when it clicked: I finally had a way to hand off the work and trust it would get done.

## **What I run in Claude Cowork every day, week, and quarter**

Most of the time I save with Claude Cowork falls into about 90 minutes of small daily wins, or micro-optimizations, that it runs for me.

Each morning, a scheduled task runs a [skill](https://claude.com/skills) that scans my Google Calendar and books a conference room for any external meeting that's missing one. A second skill runs customer call prep before each meeting, pulling spend from BigQuery and pipeline status from Salesforce into a brief that's waiting for me when I open my laptop. The scheduler was the bigger unlock than the skill itself. Once prep stops being a slash command I have to remember and starts running on its own, I stop forgetting it.

The Friday forecast is the next tier up and it saves me about three hours per week. A scheduled skill pulls opportunity records and submitted commits from Salesforce's Forecast tab, token spend from BigQuery, and notes from a handful of internal documents. It assembles a single-page web report in the exact format Anthropic's sales leadership wants to read: top-line metrics, top deals, movers and decliners, and the forecast snapshot rolled up from each first-line manager. The skill deploys the page to an internally shared link before Monday's forecast call. My Monday job is to add commentary: Claude builds the what; I do the why.

The biggest project I've run through Claude Cowork was account propensity scoring for the whole mid-market segment. Every fiscal year, every account in the book needs a score that helps the assigned AE prioritize the territory. In previous companies and roles, work like this ran for hundreds of hours across RevOps, FP&A, and marketing. I did it in one night.

I started by defining two five-dimension scoring rubrics with Claude: one for tech accounts and one for industries. The dimensions for tech were agent opportunity, internal transformation, AI commitment, white space against existing spend, and industry fit. Industries used a different rubric, with dimensions like knowledge-worker density (which can be very high at law firms, for example, and lower in manufacturing because so many employees are on the shop floor), and public AI commitments measured by mentions on the company's open jobs page.

Once the rubric was set, I pointed Claude Cowork at the 4,000-account list. Claude Cowork ran overnight, scoring each account one by one with deep web research, Salesforce data, and BigQuery data, producing a numerical score and a written rationale for every dimension. Then I asked Claude Cowork to build an interactive dashboard from the results. Each AE clicks into their territory's pie slice and sees their accounts ranked by score, with the rationale generated for each dimension. Hovering over an account surfaces potential use cases and comparable case studies for prospecting. The dashboard turned the scores from a data exercise into a working sales tool.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0cba7471891499b1cc0948_Sales-dashboard-demo.png)

*Territory scoring dashboard, shown here with demo data.*

None of the prompts were technical. The pattern was: tell Claude what dimensions to score on, run a test territory, check the output, adjust the weights ("I think D4 is probably weighted a little heavy; bring it down a bit"), run the next territory.

## **Why Claude Cowork works for me**

What made Claude Cowork stick for me is the interface. Prompts read like English sentences, outputs land in formats I already work in (docs, web pages, and Salesforce updates), and the human-in-the-loop pattern is built in so Claude proposes and I approve before anything ships.

Sales is full of people who got into the job for the customer conversations. Claude Cowork can give them back the hours to do just that.

## **Where sales teams should start**

Two patterns from my own week are worth taking back to a sales team.

The first is to put prep on a schedule. Scheduled tasks run themselves; I don’t have to remember to do any of the small daily tasks that end up taking a fair bit of time collectively. Encoding the team's required format into the skill matters too: my forecast lands in the exact layout my leadership reads, so my Monday time goes to commentary instead of formatting. If you want a starting point for your setup, Anthropic's [Sales plugin](https://claude.com/plugins/sales) ships with baseline skills, including the call prep one. Those are meant to be customized to match how your team actually works.

The second is to run big strategic projects as overnight Claude Cowork routines. The 4,000-account scoring run is the showcase example, but the same shape works for TAM sizing, account research, comp benchmarking, anything historically deferred because no team had the hours for it. You can refine the prompt the next morning, if needed.

Before Claude Cowork, data assembly, report formatting, and the rebaseline when a number changes used to fill my week. Now, I have the hours back to dedicate to the strategic and customer-relationship work that pushes the needle.

[***Learn more about how sales teams use Claude Cowork***](https://claude.com/resources/tutorials/using-claude-cowork-for-sales-account-research) ***and*** [***get started***](http://claude.com/cowork) ***today.***

‍

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0112e18cdd7f0b92d19e40_Hand-BuildingBricks.svg)

Jun 24, 2026

### Building effective human-agent teams

Enterprise AI

[Building effective human-agent teams](#)Building effective human-agent teams

[Building effective human-agent teams](/blog/building-effective-human-agent-teams)Building effective human-agent teams

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22c7f111435762ad994_1b398dbdfa4995ce5ce943aa87d8b78b2c2ba065-1000x1000.svg)

Jun 22, 2026

### The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry

Enterprise AI

[The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry](#)The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry

[The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry](/blog/the-full-claude-desktop-experience-on-aws-google-cloud-and-microsoft-foundry)The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22930b7622d6096c33d_4d663bd87c391c144b9bca513b3849ccfa00a3b9-1000x1000.svg)

Mar 13, 2026

### 1M context is now generally available for Opus 4.6 and Sonnet 4.6

Product announcements

[1M context is now generally available for Opus 4.6 and Sonnet 4.6](#)1M context is now generally available for Opus 4.6 and Sonnet 4.6

[1M context is now generally available for Opus 4.6 and Sonnet 4.6](/blog/1m-context-ga)1M context is now generally available for Opus 4.6 and Sonnet 4.6

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2319ef2161fcf9ba649_ddad92700787ec1bf1d80359c0c5e6ca305682b0-1000x1000.svg)

Feb 5, 2026

### Advancing finance with Claude Opus 4.6

Enterprise AI

[Advancing finance with Claude Opus 4.6](#)Advancing finance with Claude Opus 4.6

[Advancing finance with Claude Opus 4.6](/blog/opus-4-6-finance)Advancing finance with Claude Opus 4.6

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

    

    

    

    

    

    

    

    

    

    

Claude Cowork

Productivity

Sales
