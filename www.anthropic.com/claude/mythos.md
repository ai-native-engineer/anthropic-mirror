<!-- source: https://www.anthropic.com/claude/mythos -->

# Claude Claude Mythos 5

![Claude Claude Mythos 5](https://www-cdn.anthropic.com/images/4zrzovbb/website/996bdedc16539920ce70c987f4e612feee3d604a-1040x141.svg)

![Claude Claude Mythos 5](https://www-cdn.anthropic.com/images/4zrzovbb/website/1e46f1ab2c13b19a2a2fc420f0677409f71e0908-184x156.svg)

Our most capable model for cybersecurity and biology research.

## Announcements

* NEW

  Introducing Claude Mythos 5.1

  Sep 1, 2026

  Claude Mythos 5.1 is our newest Mythos-class model, with gains in cybersecurity and biology. Access remains limited to a small set of vetted organizations.

  [Read more](https://www.anthropic.com/introducing-claude-fable-mythos-5-1)
* Claude Mythos 5 export controls have been lifted

  Jul 1, 2026

  We have restored access to Mythos 5 for a set of US organizations, following the US government’s approval.

  [Read more](https://www.anthropic.com/news/redeploying-fable-5)
* Claude Mythos 5 is currently unavailable

  Jun 12, 2026

  We apologize for this disruption to our customers and are working to restore access as soon as possible.

  [Read more](https://www.anthropic.com/news/fable-mythos-access)
* Claude Mythos 5

  Jun 9, 2026

  Claude Mythos 5 is the latest update for Mythos Preview, seeing gains in cybersecurity, biology, and healthcare benchmarks. Given its capabilities, Mythos 5 is currently only available to a small group of vetted partners with a goal of opening up more broadly in the future.

  [Read more](https://www.anthropic.com/news/claude-fable-5-mythos-5)
* Expanding Project Glasswing

  Jun 2, 2026

  We’re extending Project Glasswing to approximately 150 new organizations in more than fifteen countries.

  [Read more](https://www.anthropic.com/news/expanding-project-glasswing)

## Availability and pricing

Claude Mythos 5.1 is available to vetted cyberdefenders and life scientists through our trusted access programs. The Life Sciences Verification Program is launching as an invite-only beta offering access with reduced biology safeguards for advanced life sciences researchers. The Cyber Verification Program, which provides reduced cyber safeguards for defensive security work, will include access to Mythos models in the near future. Currently, we’re only able to make it available to a set of US organizations, though we’re working to expand access.

Claude Security also now runs on Mythos 5.1.

Pricing for Claude Mythos 5.1 starts at $10 per million input tokens and $50 per million output tokens.

## Safeguards

Because Mythos 5.1 is highly capable for cybersecurity and biology research, it could be used both for good and for harm. We currently only provide access to a small, but growing, set of vetted organizations through our trusted access programs.

To release Mythos-level capabilities more broadly, we’ve added additional safeguards. [Claude Fable 5.1](https://www.anthropic.com/claude/fable) is the same underlying model as Claude Mythos 5.1 with safeguards for cybersecurity and biology. With Fable 5.1, these safeguards are more precise: Fable 5.1 can now be used to identify software vulnerabilities in source code, and our biology safeguards intervene on benign requests [85% less often](https://www.anthropic.com/news/improving-fable-5-s-biology-safeguards) than the ones we launched with Fable 5. Our safeguards still route dual-use biology and chemistry research questions to our Opus models, and prevent penetration testing, exploit generation, and binary-based vulnerability scanning. [Learn more](https://support.claude.com/en/articles/15363606-why-claude-switched-models-in-your-conversation-with-fable-5) about how the fallback experience works.

We extensively test and evaluate our models to ensure they meet Anthropic’s standards for safety, security, and reliability. The accompanying [system card](https://www.anthropic.com/claude-fable-5-1-mythos-5-1-system-card) covers safety results in depth.

## Data retention

Using Claude Mythos 5.1 requires accepting a 30-day data retention policy for safety monitoring by default. [Learn more](https://support.claude.com/en/articles/15425996-data-retention-practices-for-covered-models).

## Benchmarks

Claude Fable 5.1 and Claude Mythos 5.1 are the same underlying model. Results below are for Fable 5.1 unless noted; where Mythos 5.1 results are shown, the gap reflects tasks where Fable 5.1’s safeguards intervene.

![Benchmark table for Fable 5.1 comparing the model against Fable 5, Opus 5, and GPT-5.6 Sol.](https://www-cdn.anthropic.com/images/4zrzovbb/website/a0ec790d784db6dab9e05a7cfe2664e31aec1681-2160x1996.png)

Fable 5.1 was evaluated with its production safeguards enabled. On tasks where these safeguards intervened, Fable 5.1 and Fable 5 scored a zero on OSWorld 2.0, and Fable 5 scored a zero on AutomationBench. In all other interventions from our safeguards, cybersecurity tasks were completed by Claude Opus 4.8, and biology tasks were completed by Claude Opus 5. This likely reduces the performance of Fable 5.1 and Fable 5 on these benchmarks.
1Terminal-Bench-Science 0.1: The standard error is ±3.5–4.5 pts per model. The public leaderboard (3 trials/task, Claude Code harness) reports Claude Opus 5 at 30.0% and Claude Fable 5 at 21.4%; our setup reproduces them at 29.0% and 24.7%, respectively, both within noise.
2OSWorld 2.0: Scores are on the benchmark authors’ August 2026 task release; Fable 5 and Opus 5 were re-run under the same conditions. Because the task files differ from earlier releases, these numbers aren't directly comparable to previously published OSWorld 2.0 results, which is why no competitor score is shown.

## Frequently asked questions

### Why did you create a new version of Mythos for general availability?

Making a model as capable as Mythos 5.1 generally available comes with risks. The model’s capabilities in specific areas like cybersecurity and biology are advanced enough that they could be misused to create cyberattacks or dangerous weapons. To release Mythos-level capabilities more broadly, we developed [Claude Fable 5.1](https://www.anthropic.com/claude/fable) with safeguards that block or limit its performance in risky areas.

### How can I apply for access to Mythos 5.1?

Claude Mythos 5.1 is available to vetted organizations through our trusted access programs. Cyberdefenders can apply to the Cyber Verification Program [here](https://claude.com/form/mythos-access-interest), which will include Mythos access in the near future.
