<!-- source: https://claude.com/resources/use-cases/compare-products-across-sites -->

Personal

Professional

Claude in Chrome

Browser Use

# Compare products across sites

Claude in Chrome reads the specs from multiple product pages you have open, normalizes the data, and creates a comparison table in Google Sheets. You stop tab-switching and start deciding.

Try in Claude

[Try in Claude](https://claude.com/download)Try in Claude

* Author

  Anthropic

  Claude in Chrome
* Model

  Haiku 4.5
* Features

  Browser Use
* Share

  [Copy link](#)

  https://claude.com/resources/use-case/compare-products-across-sites

1

## Describe the task

You've got four browser tabs open with different laptops—or TVs, or vacuums, or whatever you're comparing. Each site shows specs differently: one says "RAM," another says "Memory," a third buries it in a collapsible section. You're switching back and forth, trying to remember which one had better battery life. Claude in Chrome can read each product page, pull the specs, normalize the labels, and build a comparison table in Google Docs.

Open the product pages you want to compare. Tell Claude which specs matter to you, and it handles the rest.

I'm trying to decide between a few laptops and I have the product pages open in different tabs. Can you look at each one, pull out the specs, and put them in a Google Doc so I can compare them side by side?

I care most about: processor, RAM, storage, screen size, battery life, and weight. Let me know which one wins on each category.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

2

## Give Claude context

Claude reads directly from the product pages you have open—switching between tabs to extract the specs, then creating a spreadsheet with everything normalized into consistent columns.

## Required context

Tell Claude which products you're wanting to compare or open the product pages in separate browser tabs. Log into Google Docs so Claude can draft the comparison there. Claude navigates between tabs on its own—you just need everything accessible in your browser.

If you're comparing several products, consider telling Claude which specs matter most upfront. Otherwise it will pull everything it finds, which can make the spreadsheet wider than you need.

No items found.

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

## Optional context

No items found.

3

## What Claude creates

Claude analyzes and extracts information from across tabs, drafting a comparison doc that highlights which product wins each category, and gives a quick recommendation.

From Claude

**4 Laptops Compared**

**Spreadsheet created**

 I found these products across your open tabs:

* Dell XPS 15 (dell.com) — $1,499
* MacBook Pro 14" (apple.com) — $1,999
* Lenovo ThinkPad X1 Carbon (lenovo.com) — $1,649
* HP Spectre x360 (hp.com) — $1,399

**Spec Comparison**

 Here's the comparison based on the specs you care about:

 Price  
  - Dell XPS 15: $1,499  
  - MacBook Pro 14": $1,999  
  - ThinkPad X1: $1,649  
  - HP Spectre: $1,399  
 *- Winner: HP Spectre*

 Processor  
  - Dell XPS 15: Intel i7-13700H  
  - MacBook Pro 14": Apple M3 Pro  
  - ThinkPad X1: Intel i7-1365U  
  - HP Spectre: Intel i7-1360P  
  *- Winner: MacBook (M3 Pro)*

 RAM  
  - Dell XPS 15: 16 GB  
  - MacBook Pro 14": 18 GB  
  - ThinkPad X1: 16 GB  
  - HP Spectre: 16 GB  
 *- Winner: MacBook (18 GB)*

 Storage  
  - Dell XPS 15: 512 GB SSD  
  - MacBook Pro 14": 512 GB SSD  
  - ThinkPad X1: 512 GB SSD  
  - HP Spectre: 1 TB SSD  
  - *Winner: HP Spectre (1 TB)*

 Screen  
  - Dell XPS 15: 15.6" OLED  
  - MacBook Pro 14": 14.2" Liquid Retina  
  - ThinkPad X1: 14" IPS  
  - HP Spectre: 13.5" OLED  
 *- Winner: Dell (15.6" OLED)*

 Battery  
  - Dell XPS 15: 13 hours  
  - MacBook Pro 14": 17 hours  
  - ThinkPad X1: 15 hours  
  - HP Spectre: 12 hours  
 *- Winner: MacBook (17 hrs)*

 Weight  
  - Dell XPS 15: 4.2 lbs  
  - MacBook Pro 14": 3.4 lbs  
  - ThinkPad X1: 2.48 lbs  
  - HP Spectre: 3.01 lbs  
 *- Winner: ThinkPad (2.48 lbs)*

**Quick Notes**

* Lenovo listed battery as "up to 15 hours" and HP said "12 hrs mixed use"—I normalized both to comparable estimates
* Dell's page said "Memory" instead of RAM; HP buried it in the "Tech Specs" accordion
* The Intel laptops have upgradeable RAM (user-accessible slots); the MacBook's 18GB is soldered and fixed
* The ThinkPad keyboard is consistently rated best-in-class if you type a lot—worth considering beyond just specs

I've created the comparison in Google Sheets with conditional formatting highlighting the winner in each row.

**Bottom Line**

The MacBook wins the most categories (processor, RAM, battery) but costs $350–600 more than the others.

* If portability is your priority: The ThinkPad is the clear choice—it's nearly 2 lbs lighter and $350 less than the MacBook.
* If you want the best performance and battery regardless of price: The MacBook is hard to beat.

I can also pull real-world battery tests from reviews if you want—manufacturer claims are often optimistic.

4

## Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Add another option

Expand your comparison as you find more candidates. Claude adds new products to the existing doc without starting over.

I just found one more laptop option. Can you add it to the doc and update the comparison?

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Check reviews for the top pick

Before deciding, see what actual buyers say. Claude can scan reviews and summarize common praise and complaints.

The MacBook looks like the best specs, but what are people saying about it? Can you check reviews and tell me if there are any common complaints I should know about?

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Find the best price

Once you've picked a winner, Claude can check multiple retailers to find the lowest current price.

I think I want the MacBook Pro. Can you check a few sites and find where it's cheapest right now?

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

5

## Tricks, tips, and troubleshooting

### Drag tabs into Claude's tab group

If you already have relevant product page tabs open, you can drag them into Claude's designated tab group. You'll see a banner highlighting the group of tabs that Claude is active in. Claude can read and work across all tabs in the group simultaneously—no tab-switching required. Before visiting new sites, Claude asks for permission. You can grant site-level permissions for websites you trust, allowing Claude to work without repeated approvals on those specific domains.

### Save your comparison template as a shortcut

If you research products regularly, save your workflow as a shortcut by clicking on the shortcut icon below a previous prompt. Next time you're comparing options, just type "/" and select the shortcut for Claude to follow the same directions.

## Ready to try for yourself?

Claude in Chrome is available to all paid plan subscribers. Install the extension, describe or open a few product pages you're comparing, and ask Claude to build your spreadsheet.

Try in Claude

[Try in Claude](/download)Try in Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69433656958ac4e8cb0beab9_product.png)

Open artifact in new window

[Open artifact in new window](#)Open artifact in new window

## Related use cases

[Pull metrics from analytics dashboards](/resources/use-cases/pull-metrics-from-analytics-dashboards)Pull metrics from analytics dashboards

Pull metrics from analytics dashboards

Use case

[Use case](/resources/use-cases/pull-metrics-from-analytics-dashboards)Use case

[Prepare and plan from your calendar](/resources/use-cases/prepare-and-plan-from-your-calendar)Prepare and plan from your calendar

Prepare and plan from your calendar

Use case

[Use case](/resources/use-cases/prepare-and-plan-from-your-calendar)Use case

[Log sales calls to your CRM](/resources/use-cases/log-sales-calls-to-your-crm)Log sales calls to your CRM

Log sales calls to your CRM

Use case

[Use case](/resources/use-cases/log-sales-calls-to-your-crm)Use case

[Clean up promotional emails](/resources/use-cases/clean-up-promotional-emails)Clean up promotional emails

Clean up promotional emails

Use case

[Use case](/resources/use-cases/clean-up-promotional-emails)Use case
