<!-- source: https://claude.com/blog/code-review -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f76874e94e489958af8ba_Object-CodeMagnifier.svg)

# Bringing Code Review to Claude Code

Practical guidance on how to structure agent tasks using three common workflow patterns, with tradeoffs and benefits for each.

* Category

  [Claude Code](https://claude.com/blog/category/claude-code)

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  [Claude Code](https://claude.com/product/claude-code)
* Date

  March 9, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/code-review

Today we're introducing Code Review, which dispatches a team of agents on every PR to catch the bugs that skims miss, built for depth, not speed. It's the system we run on nearly every PR at Anthropic. Now in research preview for Team and Enterprise.

## **Managing the review bottleneck**

Code output per Anthropic engineer has grown 200% in the last year. Code review has become a bottleneck, and we hear the same from customers every week. They tell us developers are stretched thin, and many PRs get skims rather than deep reads.

We needed a reviewer we could trust on every PR. Code Review is the result: deep, multi-agent reviews that catch bugs human reviewers often miss themselves. It's a more thorough (and more expensive) option than our existing [Claude Code GitHub Action](https://code.claude.com/docs/en/github-actions), which remains open source and available.

We run Code Review on nearly every PR at Anthropic. Before, 16% of PRs got substantive review comments. Now 54% do. It won't approve PRs — that's still a human call — but it closes the gap so reviewers can actually cover what's shipping.

## **How it works**

When a PR is opened, Code Review dispatches a team of agents. The agents look for bugs in parallel, verify bugs to filter out false positives, and rank bugs by severity. The result lands on the PR as a single high-signal overview comment, plus in-line comments for specific bugs.

Reviews scale with the PR. Large or complex changes get more agents and a deeper read; trivial ones get a lightweight pass. Based on our testing, the average review takes around 20 minutes.

## **Code Review in action**

We've been running Code Review internally for months: on large PRs (over 1,000 lines changed), 84% get findings, averaging 7.5 issues. On small PRs under 50 lines, that drops to 31%, averaging 0.5 issues. Engineers largely agree with what it surfaces: less than 1% of findings are marked incorrect.

In one case, a one-line change to a production service looked routine and was the kind of diff that normally gets a quick approval. But Code Review flagged it as critical. The change would have broken authentication for the service, a failure mode that’s easy to read past in the diff but obvious once pointed out. It was fixed before merge, and the engineer shared afterwards that they wouldn't have caught it on their own.

Early access customers have seen similar patterns. On a [ZFS encryption refactor in TrueNAS's open-source middleware](https://github.com/truenas/middleware/pull/18291), Code Review surfaced a pre-existing bug in adjacent code: a type mismatch that was silently wiping the encryption key cache on every sync. It was a latent issue in code the PR happened to touch, the kind of thing a human reviewer scanning the changeset wouldn't immediately go looking for.

## **Cost and control**

Code Review optimizes for depth and is more expensive than lighter-weight solutions like the [Claude Code GitHub Action](https://code.claude.com/docs/en/github-actions). Reviews are billed on token usage and generally average $15–25, scaling with PR size and complexity.

Admins have many ways to control spend and usage:

* **Monthly organization caps**: Define total monthly spend across all reviews
* **Repository-level control**: Enable reviews only on the repositories you choose
* **Analytics dashboard**: Track PRs reviewed, acceptance rate, and total review costs

## **Getting started**

Code Review is available now as a research preview in beta for Team and Enterprise plans.

* **For admins**: Enable Code Review in your [Claude Code settings](http://claude.ai/admin-settings/claude-code), install the GitHub App, and select repositories you’d like to run reviews on.
* **For developers**: Once enabled, reviews run automatically on new PRs. No configuration needed.

[Explore the docs](http://code.claude.com/docs/en/code-review) for more information.

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d228c83775fcc75f4e6d_74409af25137110ac04cc39e4d5ea0a2fbcea421-1000x1000.svg)

Sep 2, 2026

### Building commerce agents with Claude

Product announcements

[Building commerce agents with Claude](#)Building commerce agents with Claude

[Building commerce agents with Claude](https://claude.com/blog/claude-for-commerce-agents)Building commerce agents with Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a90479f5433ec75978f1e8a_Object-Apple.svg)

Aug 28, 2026

### Claude for Teachers, now available for U.S. K-12 schools and districts

Product announcements

[Claude for Teachers, now available for U.S. K-12 schools and districts](#)Claude for Teachers, now available for U.S. K-12 schools and districts

[Claude for Teachers, now available for U.S. K-12 schools and districts](https://claude.com/blog/claude-for-teachers-now-available-for-schools-and-districts)Claude for Teachers, now available for U.S. K-12 schools and districts

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d222061abf091318fb82_423062049d4676b41d52b16068cbb5e21603190e-1000x1000.svg)

Aug 20, 2026

### The Claude Code guide for startups

Claude Code

[The Claude Code guide for startups](#)The Claude Code guide for startups

[The Claude Code guide for startups](https://claude.com/blog/claude-code-guide-for-startups)The Claude Code guide for startups

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22b8840b2f6f9a40fe0_8925ac952fa2cb8eb5e845b2e44f3e71b33fd695-1000x1000.svg)

Aug 26, 2026

### Claude gets its own browser in Cowork

Product announcements

[Claude gets its own browser in Cowork](#)Claude gets its own browser in Cowork

[Claude gets its own browser in Cowork](https://claude.com/blog/cowork-built-in-browser)Claude gets its own browser in Cowork

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Claude Code

Coding
