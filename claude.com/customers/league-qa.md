<!-- source: https://claude.com/customers/league-qa -->

Q&A | Claude Enterprise

# How League went all in on Claude in a regulated industry

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7e50faffe550cd0871c1c9_logo_league-light-mode.png)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7e50fdc2966b1ac852794a_logo_league-dark-mode.png)

Industry:

Healthcare

Company size:

Medium

Product:

[Claude Enterprise](https://claude.com/solutions/enterprise)

[Claude Code](https://claude.com/product/claude-code)

Location:

North America

98% Claude adoption,

up from 80% when League's company-wide rollout began

Under a quarter

for a 12-year-old regulated healthcare company to go company-wide on Claude Enterprise

Case Study: League

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7e557b127ab6a1deab03ed_og_case-study-league%20(1).jpg)

League cuts product development cycle times in half with Claude

Read more

[Read more](https://claude.com/customers/league)Read more

Case Study: League

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

League cuts product development cycle times in half with Claude

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Case Study: League

League cuts product development cycle times in half with Claude

[Prev](#)Prev

[Next](#)Next

[League](https://league.com/) has spent almost 12 years building software for health plans and providers. They work in an industry where new tools typically wait weeks to get off the ground, yet roughly 98% of League's code is AI-authored. We asked CEO and Co-founder Dan Galperin, SVP of Data and AI Engineering Jordan Christensen, and AVP of AI Transformation Signy Roland how they move this fast in a highly regulated industry.

## Anthropic: Why did you choose Claude, and what stands out to you about its frontier capabilities?

**Dan Galperin, League:** What Anthropic has built covers the whole arc of the work in healthcare tech: research, brainstorming, execution, validation, design, security, and more, all in one place, end to end. And it’s connected to the dozens of other tools we already use every day using MCP. Claude also keeps shipping features before we even know we want them. Our engineers, and everyone else, spend their time on harder problems now because we trust Claude with the execution. That has taken us further and faster than we expected.

"Our engineers spend their time on harder problems now because we trust Claude with the execution. That has taken us further and faster than we expected."

Dan Galperin

CEO and Co-founder, League

## Anthropic: What's the hardest problem your engineering team has handed Claude, and what was the outcome?

**Galperin:** We build AI agents into the member experiences we ship, and an internal system scores how well each one performs. When one agent scores badly, though, improving it means an engineer rewriting the prompt by hand and guessing. The score tells you if something is off, but it doesn't tell you how to fix it. Our team set out to close that loop and build something with Claude that reads the scores and rewrites the prompt itself. That is not a feature. It is a small machine-learning system: it has to turn a critique of a bad answer into an actual edit, it has to be stopped from writing a prompt that aces the test cases but fails on real work, and it spans four codebases in two languages.

First came an exploratory session with Fable running parallel agents to work out what to build. That session produced the biggest transcript anyone at League has on disk. Then came the implementation, deliberately broken into eight stacked pull requests so each layer could be reviewed on its own instead of landing as one unreviewable blob. All eight merged, roughly 48,000 lines across 271 files. The manual guesswork was gone: a failing agent now gets its prompt rewritten automatically. And in that early exploration, Claude arrived at an approach matching GEPA, a published prompt-evolution technique nobody had pointed it to, then ran the check that confirmed the two were the same.

## Anthropic: One of your engineers recently shared a picture of a workflow running 50 parallel agents. What keeps that work on Claude?

**Jordan Christensen, League:** I use other agentic coding systems and platforms as well, and I always just keep coming back to the trust. With Claude, I know it's going to do the thing that I need done. As I give it harder problems, it keeps handling them. That's the whole reason you can run fifty agents at once on one problem. Our engineers do that through Swarm, our own orchestration layer built on Claude Code. Each agent takes a real piece of the build, writes the code, runs the tests, and opens a pull request. Nobody is watching them work, and nobody needs to, because none of it ships until an engineer reviews it and signs off.

The ceiling also keeps moving. Every release I've picked up has let me hand off something I was still doing by hand a month before that. The question we're asking now is how ambitious we can be, while keeping the level of safety and security our industry requires.

## Anthropic: Did you run an evaluation against what you were already using?

**Signy Roland, League:** There was no eval. After Opus 4.5 came out in December, we just realized we needed to have it, and we were willing to commit to a minimum spend, which we blew through very quickly. It was just a matter of getting it into people's hands and making sure they were actually using it. This was the one we knew was going to make a huge difference this year.

**Galperin:** What was released in December was a massive step function in the ability to agentically create and solve problems. I showed up at our company conference in January and said that by mid-year I expected everyone on our team to be a manager of agents. It happened much sooner than that, around March.

## Anthropic: What changed for the people who don't write code?

**Roland:** For the teams that aren't coders or engineers, they went from AI telling them how to do something to AI just doing it. Our finance team is the clearest example. They now have more than 60 automated processes for month-end, quarter-end, and payroll, work that all used to be handled manually. The earlier tools we had tried could set up the plan or tell you which formula to use in a spreadsheet. Doing the work itself was the part only Claude unlocked, and it has been a big eye-opener for everyone. I am someone with zero computer engineering background, and even I have opened a pull request.

Claude for Healthcare

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/696415a56ed108d94045852e_heart-marginalia.avif)

Claude helps healthcare organizations move faster without sacrificing accuracy, safety, or compliance. Less administrative work, more time with the people you serve.

Read more

[Read more](https://claude.com/healthcare)Read more

Claude for Healthcare

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Claude helps healthcare organizations move faster without sacrificing accuracy, safety, or compliance. Less administrative work, more time with the people you serve.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude for Healthcare

Claude helps healthcare organizations move faster without sacrificing accuracy, safety, or compliance. Less administrative work, more time with the people you serve.

"Security is the first question on everything we do, and Anthropic clearly treats it the same way. We can set the boundaries we need."

Dan Galperin

CEO and Co-founder, League

## Anthropic: How far does that go across the rest of the company?

**Roland:** Everyone's roles are blurring. Infrastructure teams like compliance, legal and finance are now coding, along with our COO. We are also all designing with Claude Design. Getting ready for our all-hands used to mean setting aside hours or days just to make slides. Now the content for our weekly town hall and company conference come out of Claude Design, with our own design system and branding built in, so we are not spending hours polishing decks anymore. That’s just one example. Nothing feels intimidating now. There is a lot of work I used to procrastinate on that today I just get Claude to do a first draft.

## Anthropic: How do you square all of that speed with healthcare's regulators, and where does it go from here?

**Galperin:** Security is the first question on everything we do, and Anthropic clearly treats it the same way. The controls reflect that: we can tier model access, manage which connectors are available and to whom, and set the boundaries we need. Claude Security itself has been excellent. The spend and usage transparency is the best we have seen in this market. Most importantly, Anthropic already understands what it takes to operate in a regulated industry, and that shows up in how they build. What it adds up to is that our whole R&D process now runs on what we call bets: a small team takes two or three weeks to build out an ambitious idea we would previously have ruled out as taking too long, and comes back with a working prototype we can put in front of the market. The cycle is insanely fast, and our ability to experiment and execute on those bets is phenomenal.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Prev](#)Prev

[Next](#)Next

## Related stories

[League cuts product development cycle times in half with Claude](https://claude.com/customers/league) League cuts product development cycle times in half with Claude

League cuts product development cycle times in half with Claude

Customer story

[Customer story](https://claude.com/customers/league)Customer story

[How can a medical lab keep patients at the center of its work while the caseload keeps growing?](https://claude.com/customers/arkana-labs)How can a medical lab keep patients at the center of its work while the caseload keeps growing?

How can a medical lab keep patients at the center of its work while the caseload keeps growing?

Customer story

[Customer story](https://claude.com/customers/arkana-labs)Customer story

[How Zingage automates care coordination for 400+ home care agencies with Claude](https://claude.com/customers/zingage)How Zingage automates care coordination for 400+ home care agencies with Claude

How Zingage automates care coordination for 400+ home care agencies with Claude

Customer story

[Customer story](https://claude.com/customers/zingage)Customer story

[A conversation with Seth Hain about Epic’s internal AI adoption](https://claude.com/customers/epic-systems)A conversation with Seth Hain about Epic’s internal AI adoption

A conversation with Seth Hain about Epic’s internal AI adoption

Customer story

[Customer story](https://claude.com/customers/epic-systems)Customer story
