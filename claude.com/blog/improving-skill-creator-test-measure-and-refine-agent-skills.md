<!-- source: https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2287f90c57df4c9dd97_c1ef4c0b6882dfe985555b52999d370ea88a3c50-1000x1000.svg)

# Improving skill-creator: Test, measure, and refine Agent Skills

Skill authors can now verify that their skills work, catch regressions, and improve descriptions.

  [Claude Code](https://claude.com/blog/category/claude-code)

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  [Claude Code](https://claude.com/product/claude-code)
* Date

  March 3, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills

Skill-creator now helps you write evals, run benchmarks, and keep your skills working as models evolve. These updates are available now in Claude.ai and Cowork, as a [plugin for Claude Code](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator), and [within our repo](https://github.com/anthropics/skills/tree/main/skills/skill-creator).

Since [launching Agent Skills](https://claude.com/blog/skills) last October, we've noticed that most authors are subject matter experts, not engineers. They know their workflows but don't have the tools to tell whether a skill still works with a new model, triggers when it should, or if it actually improved after an edit.

Today we're announcing skill-creator enhancements that help authors build with more confidence. We are bringing some of the rigor of software development (testing, benchmarking, iterative improvement) to skill authoring without requiring anyone to write code.

## **Two kinds of skills**

Skills generally fall into two categories:

**Capability uplift** skills help Claude do something the base model either can't do or can't do consistently. Our [document creation skills](https://github.com/anthropics/skills/tree/main/skills) are good examples. They encode techniques and patterns that produce better output than prompting alone.

**Encoded preference** skills document workflows where Claude can already do each piece, but the skill sequences them according to your team's process. Examples: a skill that walks through NDA review against set criteria, or one that drafts weekly updates with data from various MCPs.

This distinction matters because these two types of skills may need testing for different reasons:

* Capability uplift skills may become less necessary as models improve. Evals tell you when that's happened.
* Encoded preference skills are more durable, but only as valuable as their fidelity to your actual workflow. Evals verify that fidelity.

Either way, testing turns a skill that *seems* to work into one you *know* works.

## **Using evals to test and improve skills**

Skill-creator now helps you write evals, which are tests that check Claude does what you expect for a given prompt. If you've written software tests, this will feel familiar: define some test prompts (plus files if needed), describe what good looks like, and skill-creator tells you whether the skill holds up.

Our PDF skill, for instance, previously struggled with non-fillable forms. Claude had to place text at exact coordinates with no defined fields to guide it. Evals isolated the failure, and we shipped a fix that anchors positioning to extracted text coordinates.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69a237b02128b691d9e8b2af_skillscreator-PDFevals-1920x840-v1.png)

Evals help in many ways, but two important uses are to catch quality regressions and understand model progress.

First, **catching regressions in quality.** As models and the infrastructure around them evolve, a skill that worked well last month might behave differently today. Running evals against a new model gives you an early signal when something shifts before it impacts your team’s work.

Second, **knowing when general model capabilities have outgrown your skill.** This applies mainly to capability uplift skills. If the base model starts passing your evals *without* the skill loaded, that's a signal the skill's techniques may have been incorporated into the model's default behavior. The skill isn't broken; it's just no longer necessary.

We've also added a **benchmark mode** that runs a standardized assessment using your evals. This is something you can run after model updates or as you iterate on the skill itself. It tracks eval pass rate, elapsed time, and token usage.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69a237f15fbc61e1ccd00a0a_skillscreator-benchmarkmode-1920x1080-v1.png)

Your evals and results stay with you. Store them locally, integrate them with a dashboard, or plug them into a CI system.

## **Faster, more consistent evaluation with multi-agent support**

Running evals sequentially can be slow, and accumulating context can bleed between test runs. Skill-creator now spins up independent agents to run evals in parallel with **multi-agent support** — each in a clean context with its own token and timing metrics. Faster results, no cross-contamination.

We've also added **comparator agents** for A/B comparisons: two skill versions, or skill vs. no skill. They judge outputs without knowing which is which, so you can tell whether a change actually helped.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69a74e0afa8435f070120ed9_skillscreator-AB-testing-1920x1080-v1.png)

## **Getting skills to trigger at the right time**

Evals measure output quality, but that only matters if your skill triggers when it should. As your skill count grows, description precision becomes critical: too broad and you get false triggers, too narrow and it never fires. Skill-creator now helps you tune descriptions for more reliable triggering — it analyzes your current description against sample prompts and suggests edits that cut both false positives and false negatives.

We ran it across our document-creation skills and saw improved triggering on 5 out of 6 public skills.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69a74e1f72940942cb534904_skillscreator-skill-description-optimization-results.png)

## **Looking ahead**

As models improve, the line between "skill" and "specification" may blur. Today, a SKILL.md file is essentially an implementation plan, providing detailed instructions telling Claude *how* to do something. Over time, a natural-language description of *what* the skill should do may be enough, with the model figuring out the rest.

The eval framework we're releasing today is a step in that direction. Evals already describe the "what." Eventually, that description may be the skill itself.

## Getting Started

All skill-creator updates are available now on Claude.ai and Cowork. Ask Claude to use the skill-creator to get started.

Claude Code users can install the [plugin](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator) or download from our [repo](https://github.com/anthropics/skills/tree/main/skills/skill-creator).

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690937bee860a953417a8eee_Object-CodeBrowserGlobe.svg)

Aug 7, 2026

### Auto mode is now the default in Claude Code for Pro, Max, and Team plans

Claude Code

[Auto mode is now the default in Claude Code for Pro, Max, and Team plans](#)Auto mode is now the default in Claude Code for Pro, Max, and Team plans

[Auto mode is now the default in Claude Code for Pro, Max, and Team plans](https://claude.com/blog/auto-mode-default-in-claude-code)Auto mode is now the default in Claude Code for Pro, Max, and Team plans

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22b1ef956a6d81cfd9c_653e7474811cf768b6b0f628e253f98c60e2747e-1000x1000.svg)

Aug 7, 2026

### Running auto mode in production

Claude Code

[Running auto mode in production](#)Running auto mode in production

[Running auto mode in production](https://claude.com/blog/auto-mode-in-production)Running auto mode in production

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22753311132c8c37b39_d3dd09ad16c68461dc3fb01df5e84cf7ccafda6c-1000x1000.svg)

Aug 5, 2026

### Inference hooks: inline data loss prevention for Claude Enterprise

Enterprise AI

[Inference hooks: inline data loss prevention for Claude Enterprise](#)Inference hooks: inline data loss prevention for Claude Enterprise

[Inference hooks: inline data loss prevention for Claude Enterprise](https://claude.com/blog/claude-enterprise-inference-hooks)Inference hooks: inline data loss prevention for Claude Enterprise

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22651dd05046d0fdb0b_39c40393e610cc0a5e65f50ad12ff5ada273f792-1000x1000.svg)

Aug 6, 2026

### Run Claude Code sessions on your own compute

Product announcements

[Run Claude Code sessions on your own compute](#)Run Claude Code sessions on your own compute

[Run Claude Code sessions on your own compute](https://claude.com/blog/run-claude-code-sessions-on-your-own-compute)Run Claude Code sessions on your own compute

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
