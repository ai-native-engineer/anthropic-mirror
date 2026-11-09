<!-- source: https://support.claude.com/en/articles/17603594-free-code-review-promotional-credits-for-claude-enterprise -->

# Free Code Review promotional credits for Claude Enterprise

Updated over a week ago

Table of contents

We're giving eligible Claude Enterprise organizations promotional credits: a dollar amount of free Code Review. An Owner or Primary Owner claims them on the Code Review settings page.

Claim by the last day given under "How to get it." You can claim only once, and your amount is set when you claim, so read "How to get it" first. From the moment of the claim, your organization's reviews of pull requests are paid for from these credits first. That lasts for 30 days or until the credits are used up, whichever comes first. After that, Code Review is billed as usual, within your organization's spend limits.

This article explains who's eligible, how to claim the credits, how they're counted, and what happens when they run out or their 30 days end.

Available to eligible paid Claude Enterprise organizations. See **[Eligibility](#h_29caa9c16f)** for exclusions.

Additional offer terms apply and are available here: **[Claude Promotional Credit Offer Terms](https://www.anthropic.com/legal/promotion-credit-terms).**

## Eligibility

The offer is available to paid Claude Enterprise organizations, both new and existing.

The offer isn't available to:

* Organizations billed through a reseller (paying through a cloud marketplace subscription does not count as a reseller)
* Organizations on a trial, or whose subscription is canceled, unpaid, paused, or not yet fully set up
* Claude Team, Pro, Max, Ultra, and Free plans
* Organizations that claimed the **[earlier free Code Review offer](https://support.claude.com/en/articles/15926672-free-code-review-for-self-serve-claude-enterprise)**
* Organizations that can't use Code Review (for example, those with zero data retention)

Your organization's subscription must be active and in good standing throughout the offer. If your organization stops being eligible, reviews are billed as usual from then on. If your organization claimed the earlier free Code Review offer, it can't claim this one, even after the earlier offer has ended. While the earlier offer still applies, the Code Review settings page shows that offer and not this one. The earlier offer keeps applying as before until it ends.

## How to get it

To claim the credits, an Owner or Primary Owner of your organization can take the following steps:

1. Go to **[Organization settings > Claude Code](https://claude.ai/admin-settings/claude-code)**.
2. Find the **Code Review** section.
3. Click "Claim."

One claim covers the whole organization, and it can be made only once.

You can claim from October 15, 2026 through January 15, 2027. The last moment to claim is 23:59 UTC (3:59 PM PT) on January 15, 2027. Your credits last 30 days from the moment you claim.

Claiming does two things at that moment: it sets your organization's amount, and it starts your 30 days. A claim can't be undone or made a second time, and the amount isn't set again.

**Important:** Set up Code Review on your repositories before you claim. Your 30 days run from the claim whether or not reviews are running.

If nobody claims by the last day to claim, your organization gets no credits, and reviews are billed as usual.

## How the credits work

The amount of your organization's credits, in US dollars, is set at the moment of the claim. It's between $10,000 and $50,000, based on your organization's active Claude Code seats. The Code Review settings page shows it after the claim.

Each review counts against the amount, including reviews of new commits and re-reviews requested on the same pull request.

The credits pay for reviews triggered between the moment of the claim and the same time 30 days later.

## How each review is counted

* Every review that starts runs as a normal Code Review. When it finishes, its actual cost is taken from your credits first, to the last cent. The cost is worked out at the same list prices as any other Code Review.
* If enough of the amount is left to cover the review, your organization pays nothing for it.
* If the review costs more than what's left, the amount covers what it can, and only the part past the amount is billed, as usual and within your spend limits.
* After the amount is used up, reviews are billed as usual.
* A review that fails or is stopped because of a problem on our side isn't billed and doesn't count against the amount.
* A review stopped by a new push, or stopped by you, is counted for what it cost until it stopped.

Using up the credits, or reaching the end of their 30 days, doesn't by itself stop or pause reviews. They keep running and are billed as usual, within your spend limits. From then on, reviews that your spend limits or billing would stop don't run, just as before the offer.

If the part of a review that the credits don't cover can't be billed because your organization reached its spend limit while the review was running, that part isn't billed.

## When billing would otherwise stop a review

While you have credits left, reviews can run even if your organization has reached its spend limit, set it to $0, or run out of prepaid extra usage credit. We won't bill those reviews beyond your remaining credits. Some reviews may still be stopped or delayed, and none of this applies while Code Review or your organization's access is paused.

The part of a review covered by the credits doesn't count toward your organization's spend limits and isn't charged to you. These credits are separate from your organization's prepaid extra usage credit.

What's not covered: self-hosted Code Review (the GitHub Action), the `/code-review` command in the Claude Code CLI, the `/ultrareview` command, Claude Code usage, Claude Cowork, Claude chat, the Claude API, or any usage outside Code Review. That usage continues to be metered and billed as usual.

## When your 30 days end

Your organization's credits can be used for 30 days from the moment of the claim, or until they're used up, whichever comes first. Any unused credits don't carry over after the 30 days.

The last moment to claim is 23:59 UTC (3:59 PM PT) on January 15, 2027. An organization that claims on the last day still gets its full 30 days.

Anthropic may shorten or extend the time to claim. Once your organization claims, we won't lower its amount or shorten its 30 days, except as described under "Eligibility" and "Holds on eligibility." If this article conflicts with the Claude Promotional Credit Offer Terms, this article controls for this offer.

After your 30 days end or the amount is used up, Code Review continues as a paid feature. Reviews are billed as usual, within your organization's usual Code Review billing and spend limits.

An Owner or Primary Owner can turn off Code Review at any time from the Code Review settings page. Turning it off stops new reviews. Reviews already running finish and are counted as described above.

## Track usage in your organization

Before the claim, if your organization can claim, the Code Review settings page shows an Owner or Primary Owner the "Claim" button and the last day to claim. After the claim, it shows the amount of your credits, how much is used, and the date and time your 30 days end. Once the amount is used up, the page says so. The Code Review analytics page counts reviews paid for from the credits along with your other reviews.

## Holds on eligibility

If we detect abuse, we may pause an organization's credits while we review the activity, and remove them if we confirm abuse.

## Frequently asked questions

### Do you need to do anything to get it?

Yes. An Owner or Primary Owner claims the credits once on the Code Review settings page, no later than the last day to claim. Until then your organization has no credits, and reviews are billed as usual.

### What happens when you click "Claim"?

Two things happen at that moment. Your organization's amount is set, and your 30 days start. Reviews triggered from then on are paid for from the credits first. A claim can't be undone or made a second time, and the amount isn't set again.

### Can you claim later?

Yes, any time through the last day to claim. Your 30 days start when you claim, not when the time to claim opens, so claiming later doesn't shorten them.

### Does the amount change after you claim?

No. Once you claim, we won't lower your amount, except as described under "Eligibility" and "Holds on eligibility."

### What counts as a review?

A review is one Code Review of a pull request. Each of these can start a review, and each review counts against the amount:

* Opening a new pull request
* Pushing new commits to an open pull request
* Requesting a re-review of the same commits

A review can start when someone asks for one with `@claude review`, or automatically, depending on your organization's Code Review settings.

### What if a review costs more than what's left?

The credits cover what they can. Only the part of that review past the amount is billed, as usual and within your spend limits.

### What happens when the amount is used up?

The review that uses up the last of the amount is billed only for the part past it, unless that part can't be billed, as described under "How the credits work." Every review after that is billed as usual, within your organization's spend limits. The same goes for reviews triggered after your 30 days end.

### Can you use the credits if you've reached your spend limit or run out of prepaid extra usage credit?

If you have credits left, yes. Reviews can run even if your organization has reached its spend limit, set it to $0, or run out of prepaid extra usage credit. We won't bill those reviews beyond your remaining credits. Some reviews may still be stopped or delayed, and none of this applies while Code Review or your organization's access is paused.

Once the credits are used up or their 30 days end, reviews are subject to your spend limits as usual.

### How is your amount set?

It's set for your organization when you claim, between $10,000 and $50,000, based on your organization's active Claude Code seats. After the claim, the Code Review settings page shows it.

### Are failed reviews counted?

Not when the problem is on our side. A review that fails or is stopped because of a problem on our side isn't billed and doesn't count against the amount.

### Does this cover GitHub Enterprise?

Yes. Organizations that have connected a GitHub Enterprise Server instance or a GitHub Enterprise Cloud with data residency instance (a .ghe.com address) can claim the credits, and their reviews are paid for from the credits like any other organization's. Connecting one after you claim doesn't change your credits.

### Where can you get help?

Contact **[our support team](https://support.claude.com/en/articles/9015913-how-to-get-support).**

---

Related Articles

* [Manage usage credits for Team and seat-based Enterprise plans](https://support.claude.com/en/articles/12005970-manage-usage-credits-for-team-and-seat-based-enterprise-plans)
* [Claude Code on Console to Enterprise migration](https://support.claude.com/en/articles/14128775-claude-code-on-console-to-enterprise-migration)
* [Set up Code Review for Claude Code](https://support.claude.com/en/articles/14233555-set-up-code-review-for-claude-code)
* [Claude Enterprise consumption guide](https://support.claude.com/en/articles/14782391-claude-enterprise-consumption-guide)
* [Monthly API credits for Max, Ultra, and Team plans](https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-ultra-and-team-plans)

Disappointed Reaction😞Neutral Reaction😐Smiley Reaction😃

Table of contents
