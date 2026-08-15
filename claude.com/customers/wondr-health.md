<!-- source: https://claude.com/customers/wondr-health -->

Case study | Claude Platform

# Wondr Health scales trusted health coaching with Claude

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7554a1ec915407cc422bfa_logo_wondrhealth-light-mode%201.png)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7554a6949ac0de1b799cd2_logo_wondrhealth-dark-mode.png)

Industry:

Software

Company size:

Startup

Product:

[Claude Platform](https://claude.com/platform/api)

Partner:

AWS

Blank Metal

Location:

North America

700+ questions tested by Wondr's team

before any real participant met their AI coach

Onboarding time reduced

From 30 to 60 minutes into a 10-minute guided conversation

[Wondr Health](https://wondrhealth.com/) is a digital health company whose behavior-based weight management program is offered to employees as part of their employer-sponsored benefits plan. The program combines a structured curriculum, human coaches, and accountability tools to make lasting change possible for participants. To bring that experience to more people, Wondr partnered with AI-native engineering firm [Blank Metal](https://blankmetal.ai) across a three-sprint engagement to build Wonda, an AI-powered coaching layer that extends Wondr's human coaches rather than replacing them. The coach is powered by Claude through Amazon Bedrock. Its first phase, now built, tested, and heading into a beta rollout, reshapes the onboarding experience, one of the most critical moments in the program.

## With Claude, Wondr Health built:

* An AI coaching layer that reduces onboarding time from 30 to 60 minutes into a 10-minute guided conversation, without shortening the relationship it leads into
* A testing console that let clinical and coaching teams put 700+ questions through Wonda across six user personas, without engineering support
* A parallel safety subagent that monitors every conversation turn and escalates to human coaches through Zendesk
* Onboarding conversations grounded in Wondr's actual curriculum through a retrieval augmented generation (RAG) pipeline
* A coach that keeps improving through automated evaluators, scored human evaluation rounds, and full conversation tracing

## The challenge

Advancing Claude in healthcare and the life sciences

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6961abe753199c35cdc7f2a2_HCLS%20Launch%20-%20Blog%20-%20Social%20Image%20-%201200%20x%20628%20A.png)

Transform healthcare from insight to action

Read more

[Read more](https://www.anthropic.com/news/healthcare-life-sciences)Read more

Advancing Claude in healthcare and the life sciences

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Transform healthcare from insight to action

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Advancing Claude in healthcare and the life sciences

Transform healthcare from insight to action

## Earning trust in a 10-minute window

Weight loss journeys are complex and different for every participant, and Wondr's results rest on the coaching relationships that guide them. The company wanted to scale its programs to serve more people while making those relationships stronger, and the place to start was the beginning. Participants arrive at program launch with questions about what they signed up for and how the program will help them, and the trust-building that historically took a human coach 30 to 60 minutes now happens in a 10-minute digital window. Getting that window right matters for everyone: participants who don't find their footing early can drop off before the program has a chance to work, a loss for their health, for the employer paying for the benefit, and for Wondr's retention.

Coaches were stretched thin fielding high-volume, repetitive questions while needing to analyze data across systems to understand a single participant's situation. And Wondr's existing Zendesk bot had surfaced something unexpected: participants were asking questions anonymously that they wouldn't ask a human, which highlighted a great opportunity.

To build the answer, Wondr Health brought in [Blank Metal](https://claude.com/customers/blank-metal-qa), an AI-native engineering firm that helps enterprises take AI from pilot to production and runs its own operations on Claude before deploying anything for a client. "Wondr is a great service built on strong coaching relationships,”  said Elli Rader, the firm's Chief Revenue Officer. “They wanted to test how AI could help them scale their programs to serve more people without compromising the coaching quality that makes them who they are.”

## The solution

Claude for Healthcare

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/696415a56ed108d94045852e_heart-marginalia.avif)

Claude helps healthcare organizations move faster without sacrificing accuracy, safety, or compliance. Less administrative work, more time with the people you serve.

Read more

[Read more](https://claude.com/healthcare)Read more

Claude for Healthcare

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Claude helps healthcare organizations move faster without sacrificing accuracy, safety, or compliance. Less administrative work, more time with the people you serve.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude for Healthcare

Claude helps healthcare organizations move faster without sacrificing accuracy, safety, or compliance. Less administrative work, more time with the people you serve.

## A model to trust with sensitive conversations

Blank Metal came in planning to build on Claude. Wondr needed "an AI coach that could stay clinically accurate and know when to hand off to a human," said Blank Metal’s Healthcare practice lead, Jason Dehler. "That's not a task you can afford to get wrong."

Wondr’s team selected Claude for its empathy. “We came in with a plan to use Claude from the start,” the team said. “For a healthcare use case, we needed a model that could handle sensitive, emotionally loaded conversations with accuracy, empathy, and no hallucinations."

The infrastructure choice followed the team's guiding principle of using proven, dependable tools chosen for production reliability, not novelty. Running Claude on Amazon Bedrock fit exactly that. "In healthcare, you're not running experiments on users," Dehler said. "You need a model you can trust to stay in bounds, respond with clinical accuracy, and escalate appropriately if something goes wrong."

The plan also called for a parallel safety agent monitoring every conversation turn, and that design depends on the primary model staying on-task and the safety model having clear signal. Claude's instruction-following provided both. The coaching voice mattered just as much: Wonda needed to be warm, clinically grounded, and specific to Wondr's coaching voice, especially for someone asking sensitive questions about their weight.

## Production architecture with safety at the center

Wonda was designed to extend Wondr's human coaching into the first 10-minute interaction with the program, at scale. First, Wonda collects a participant's "My Why," guides goal setting, answers questions grounded in the curriculum, and starts building the kind of trust that then leads them to the human coach. "It’s not a generic chatbot, but a purpose-built coaching presence," the Blank Metal team says.

The architecture was designed for production from day one, not as a prototype. The team established Wonda's behavior on synthetic data outside Wondr's systems, keeping real participant health information out of the build while surfacing the modernization work Wondr's environment would need for production. Claude sits at the center of an agentic architecture handling participant conversations: personalized onboarding, goal setting, and answers grounded in Wondr's curriculum through a RAG pipeline.

Claude Opus 4.5 powers the coaching agent's reasoning, Claude Sonnet detects escalation scenarios in the safety subagent, and Claude Haiku runs the automated evaluations as an LLM judge, all through Amazon Bedrock. At every conversation turn, the safety subagent checks the input and conversation history for clinical risk, off-topic behavior, and escalation triggers. When it fires, it automatically creates a Zendesk ticket with the risk level and a full conversation summary, gated for human coach follow-up based on severity.

An API gateway screens every request, handling authentication, rate limiting, and participant data filtering before anything reaches the model. LangGraph handles orchestration and LangSmith captures full conversation tracing, so every interaction is logged and inspectable. Custom automated evaluators run verbosity checks and content accuracy scoring. And a Next.js testing console on Vercel gave Wondr's clinical and coaching teams direct access to test Wonda's responses across six user personas, each built with realistic simulated metadata, without needing engineering support.

Wondr accelerated the build by showing up prepared. The company came in with user personas, program content, escalation guidelines, and a personality document, which compressed weeks of discovery into days.

That preparation carried into evaluation. The hardest problem in the engagement was trust, on two fronts at once: end users would have to trust Wonda in sensitive conversations, and Wondr's clinical team had to trust Wonda enough to put it in front of them. The persona and safety design addressed the first; the evaluation earned the second. Internal Wondr employees adopted personas and put 700+ questions through the system, covering onboarding workflows, human escalations, and specific questions about Wondr content, alongside automated evaluators and two rounds of scored human evaluation. The testing console is what earned the clinical team's trust: "Getting them into the tool early, as a partner in evaluation, not a gate at the end, was what built that confidence," the team said.

"You need a model you can trust to stay in bounds, respond with clinical accuracy, and escalate appropriately if something goes wrong."

Jason Dehler,

Healthcare practice lead, Blank Metal

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## The outcome

## Measured quality and trust earned on both fronts

Wonda delivers onboarding in a 10-minute conversation, compressing what historically took a coach 30 to 60 minutes, now allowing participants to get to human coaching more efficiently. Between the two human evaluation rounds, Wonda's scored response quality kept improving, with strong reception on tone, empathy, and personalization from the coaching and clinical teams, the two groups who needed to trust Wonda most.

The deeper result echoes what the Zendesk data first revealed: evaluators told Wonda things they wouldn't tell a human coach. An AI coach that earns enough trust to surface those questions, and answers them accurately and safely, points to support participants weren't getting before, and to a new input into Wondr's care model.

The design also keeps coaches at the center: every repetitive onboarding question Wonda takes on is meant to free a coach for the conversations that require a human. The coaches' expertise, empathy, and clinical judgment remain the core of the program. "The hybrid model was the design principle from day one: AI handles scale, humans handle depth," the team said.

Phase 1 was scoped to prove the experience works before putting it in front of real participants. Phase 2 does exactly that: a beta rollout measuring retention and activation. The published research behind Wonda's design suggests what's possible: in comparable programs, AI onboarding has shown 13.6 percentage points higher completion than traditional onboarding, and roughly 2x retention with empathetic persona design.  Those are the outcomes Wonda is being built toward.

## Related stories

[Office Hours: Building the case for leaders who ship with DoorDash](https://claude.com/customers/doordash-boris-office-hours) Office Hours: Building the case for leaders who ship with DoorDash

Office Hours: Building the case for leaders who ship with DoorDash

Customer story

[Customer story](https://claude.com/customers/doordash-boris-office-hours)Customer story

[Office Hours: Asynchronous coding and the end of the IDE with Spotify](https://claude.com/customers/spotify-boris-office-hours) Office Hours: Asynchronous coding and the end of the IDE with Spotify

Office Hours: Asynchronous coding and the end of the IDE with Spotify

Customer story

[Customer story](https://claude.com/customers/spotify-boris-office-hours)Customer story

[Office Hours: Building for the model that doesn't exist yet](https://claude.com/customers/ramp-boris-office-hours)Office Hours: Building for the model that doesn't exist yet

Office Hours: Building for the model that doesn't exist yet

Customer story

[Customer story](https://claude.com/customers/ramp-boris-office-hours)Customer story

[How Miro's champions run their week with Claude Cowork](https://claude.com/customers/miro-qa)How Miro's champions run their week with Claude Cowork

How Miro's champions run their week with Claude Cowork

Customer story

[Customer story](https://claude.com/customers/miro-qa)Customer story
