<!-- source: https://academy.claude.com/use-cases/prd-from-a-one-pager -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# PRD from a problem statement

A structured PRD with the open questions flagged.

6 minProductClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-fxf6oslq.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-lntba6wn.png)

## Set up

### Try a plugin

The Product Management plugin ships with `/write-spec` and other spec-writing skills as a starting point, already structured to interview you on the problem and produce a sectioned PRD. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Product Management7 skills to write specs, synthesize research, run competitive analysis, and keep the roadmap honest

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=product-management)

`/write-spec`Interview the PM on a problem statement and draft a structured PRD

[Run](claude://cowork/new?q=%2Fwrite-spec)

Show all 8 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/d9bcb0bb9b2b1fff.svg)

Linear

[Connect](https://claude.ai/desktop/directory/linear)

![](images/ea7c24639ab8053c.svg)

Notion

[Connect](https://claude.ai/desktop/directory/notion)

![](images/a3bfc5814bd6a3e2.svg)

Google DriveOptional

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (your org's PRD template, a recent PRD you like the depth of, any research notes on the problem) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the new PRD back to it.

Product / prds

prd-template.docxJan 5, 202614 KB

PRD-bulk-export.docxMar 20, 202638 KB

saved-views-research-notes.mdOptionalApr 14, 202622 KB

In Cowork’s chat bar:Product / prds

## The prompt

### Copy this into Claude Cowork

Write a PRD for the saved-views problem. Interview me first about the problem, who hits it, the constraints, and how we'd measure success. Then draft it in prd-template.docx, call out the goals and non-goals, match the depth of PRD-bulk-export.docx, and flag every open question for design review.

Product / prdsOpen in Cowork

### Why this works

Prompt

**Ask to be interviewed.** "Interview me first" turns a blank-page problem into a guided conversation; Cowork pulls the problem, users, constraints, and metrics out of your head before it writes a word of the spec.

Source

**Point at your template.** Naming prd-template.docx sends the draft into your section order and depth, so the output reads like one of yours and not a generic spec.

Prompt

**List what's in and out of scope.** Calling out goals and non-goals keeps scope honest; the things you decided not to do are as load-bearing in review as the things you did.

Source

**Show it what good looks like.** Pointing at PRD-bulk-export.docx hands Cowork your quality bar; it matches the structure and depth of a PRD you already trust instead of guessing at both.

Prompt

**Give open questions a named owner.** "For design review" means each unresolved item gets a clear next owner instead of sitting in a list nobody picks up.

### Get a better draft

What Cowork gives you back is mostly determined by what you put in. A real template, one PRD you like, and honest interview answers move the draft further than any rewording of the prompt, so invest there first.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

**Try dictation for the interview.** The thought dump is faster spoken than typed. Hit the mic in Cowork, talk through the problem and the users out loud, and let Cowork turn the transcript into the structured PRD.

Practice

**Check the goals and open questions before it goes to review.** Read the draft's goals and non-goals against what you said in the interview, and confirm every flagged open question is one you actually left open. Cowork fills gaps with reasonable guesses, and unchecked guesses are what design review catches. Fix what you didn't decide, then send it.

## Going forward

### Now in your Cowork

Your processes

Product Management plugin

Your tools

![](images/d9bcb0bb9b2b1fff.svg)Linear![](images/ea7c24639ab8053c.svg)Notion![](images/a3bfc5814bd6a3e2.svg)Google Docs

Your workspace

Product / prds

Spec writing starts from a structured draft in your template with the open questions flagged, so you spend your time reviewing instead of writing from scratch.

[Next: User story breakdown](https://academy.claude.com/use-cases/launch-readiness)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Going forward](#going-forward)
