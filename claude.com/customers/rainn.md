<!-- source: https://claude.com/customers/rainn -->

Q&A | Claude

# RAINN brings crisis support to encrypted messaging platforms with Claude

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a57cc3a12ba4fd5b38e358a_logo_rainn-light-mode.svg)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a57cc4468867728a26e33ae_logo_rainn-dark-mode.svg)

Industry:

Beneficial Deployments

Company size:

Small

Product:

[Claude for Nonprofits](https://claude.com/solutions/nonprofits)

[Claude Code](https://claude.com/product/claude-code)

[Claude Enterprise](https://claude.com/solutions/enterprise)

Location:

North America

Signal Messenger integration in 30 days

extending encrypted, anonymous access to RAINN's services

Full crisis support deployed for higher education institution in one week

via WhatsApp, text, and phone services

Beneficial Deployments

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a57d4749f1d659f155a38d4_Screenshot%202026-07-15%20at%2011.41.43%E2%80%AFAM.png)

Accelerate the work that matters most

Read more

[Read more](https://www.anthropic.com/news/claude-for-nonprofits)Read more

Beneficial Deployments

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Accelerate the work that matters most

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Beneficial Deployments

Accelerate the work that matters most

[Prev](#)Prev

[Next](#)Next

[RAINN](https://rainn.org/help-and-healing/hotline/), the Rape, Abuse & Incest National Network, has connected survivors of sexual violence with confidential support for over 30 years through its National Sexual Assault Hotline and online services. As CTO, William Bondurant leads the engineering work that extends RAINN's reach to new channels, including building the hotline interface on encrypted messaging platforms like Signal. We spoke with William about how RAINN's engineering team uses Claude Code to build infrastructure for crisis support, while still keeping the crisis support itself fully human. As RAINN has adopted Claude across its operations, their guiding principle is that AI's role is to connect survivors with human support faster, not to replace people. The following conversation has been edited for length and clarity.

## Anthropic: You're CTO of an organization that has supported survivors of sexual violence for over 30 years. What is the role of technology and AI in that mission?

**William Bondurant, RAINN:** The mission has been the same for 30 years: connect survivors with confidential, anonymous support. What's changed is how people reach out, and that's where technology comes in. Every channel we build has to be anonymous, confidential, and encrypted, because the people reaching out are navigating a crisis and need to trust us completely. And the efficiency matters as much as the reach: when we don't have to spend on building a channel by hand, that funding can go to supporting RAINN’s victim services. RAINN support specialists are highly trained, trauma-informed professionals who staff the National Sexual Assault Hotline. They provide free, confidential, 24/7 crisis interventions and support for survivors of sexual violence and their loved ones. That's how I think about technology here. It's always in service of the mission to stop sexual violence and get support to more people, more of the time.

## Anthropic: RAINN has expanded from the traditional phone, online, and text hotline to encrypted messaging platforms like Signal. For survivors specifically, why does the choice of channel matter so much?

**Bondurant:** For a survivor, there can be real fear of repercussions in reaching out for help. When a survivor works up the courage to make contact, maybe they’re ready and maybe they’re not, and they need to know they can trust the channel completely. We have an obligation, from a safety and a trust perspective, to be completely anonymous and completely confidential. That's why we've been adding ways for survivors to reach us through Signal, WhatsApp, and coming soon, Telegram. You don't have to give us any information about who you are. When you're ready, we're here.

"We're not putting a bot up to triage people. Our mission is to put a survivor in contact with a trained human. Everything Claude does at RAINN is on the way to that connection, not in place of it."

William Bondurant

CTO, RAINN

## Anthropic: What's the standard you hold yourselves to for any new channel you bring online?

**Bondurant:** Your privacy and your anonymity. These conversations are 100% encrypted. I don't know who you are. You don't know who you're talking to on the other end. But we're here to provide that support. That's the standard. It has to be like that for the medium to be aligned with our mission.

That trust has to extend to the platform itself, not just our promise to the survivor. Platforms like Signal, WhatsApp, and Telegram work because no one, whether employees or bad actors, can see the messages.

## Anthropic: RAINN runs on AWS and uses Claude Code through Amazon Bedrock. Walk us through how your engineering team uses Claude Code to build new integrations.

**Bondurant:** We're an AWS shop, so we go through Amazon Bedrock. What Claude Code changes is how much my engineers can take on, and how fast. They can spin up a council of agents to cut code for an integration like Signal, with Telegram next, working from a clear spec and reviewing everything before it ships. An integration like that used to be months of engineering work. Now our small team can stand it up in a fraction of the time. That speed is the whole point for us: the faster we can build a channel, the sooner survivors have one more safe way to reach a support specialist. We're not a large engineering organization. We have to move fast and do more with what we have.

## Anthropic: Tell us about the Signal Messenger integration. What did it take to build, and what does it look like for the survivor and the support specialist?

**Bondurant:** Signal provides a command-line interface that developers can use to build connectors into support platforms. The work is taking that CLI, wiring it into AWS, piping the conversation into our victim services console, and implementing the redaction logic. In our particular case, everything has to be anonymous and confidential. If a survivor puts in "I live at 123 Maple Lane," we have to redact that and wipe it to make sure it's not transmitted, logged, or stored. That's not a small thing to get right.

When you reach out, it's anonymous and confidential. We're not looking at your IP address, and we're not looking at the content of why you reached out. Keeping messages from being logged or stored, and redacting personal details in real time, took real engineering, and we built that pipeline ourselves, with Claude Code’s help. The redaction runs entirely in our own system; the survivor’s message is never sent to or stored by Claude. Claude Code let us build to our anonymity and confidentiality standards without compromising them.

From the survivor's side, you're messaging on Signal. You can find RAINN there the same way you'd find anyone else on the app. From the victim services side, the message comes into the same console that support specialists already use. They're not logged into Signal. They're not switching between tools. The conversation just shows up where they work. End-to-end encrypted, no survivor PII retained in our system, no break in anonymity.

With Claude Code, we shipped the full Signal integration in roughly 30 days. We're one of the first crisis hotlines where people can actually reach out directly to us over Signal.

## Anthropic: You also recently stood up a full WhatsApp, text, and phone service suite with a higher education institution in one week. How did Claude Code make that possible?

**Bondurant:** This university approached us as they were expanding services for students affected by sexual violence on campus. But the timing shifted. They weren’t sure when exactly they'd be ready. Normally that's a problem because development timelines don't bend to moving deadlines. With Claude Code, we could move on their schedule. When they said go, my principal engineers tasked Claude Code with building out the connectors, and we deployed a full WhatsApp, text, and phone service within a week. That velocity is not something I could have delivered otherwise.

## Anthropic: Beyond engineering, you run much of RAINN’s operations on Claude. What made it the right fit across the whole organization?

**Bondurant:** Claude is our connector. It enables us to run one suite instead of a stack of separate solutions, integrated with the applications we already use. Our finance team works inside Excel with connectors Claude provides to our accounting and personnel management tools.

The communications team uses Claude connectors for fast-tracking everything from presentations to creative briefs. Having Claude help with administrative tasks allows you to free up resources to focus on your core services. For my own day-to-day, I don't schedule my own meetings anymore. Cowork does it.

## Anthropic: You've come up through AOL, AWS, and Facebook. What's different about the AI shift, and how have you helped your team navigate it?

**Bondurant:** I came up through America Online in the late nineties and early 2000s, then Amazon Web Services, then I built out the AI network for Facebook. So I'd already seen the leap from dial-up, broadband, on-prem to virtualization to cloud, and the leap to AI inside AWS and Facebook. By the time I came over to RAINN, I didn't need any convincing to implement AI.

Every efficiency on the tech side is capacity we can put back into people. Every new channel we add, like Signal or WhatsApp, means more contacts coming in, which means we need to scale our support specialists staffing appropriately. Solutions like Claude Code allow us to scale rapidly from a tech perspective, while we are cost efficient to ensure our contact agents can scale appropriately as we expand our reachability.

## Anthropic: How do you address concerns from stakeholders about AI in a sensitive domain like crisis support?

**Bondurant:** The headlines around AI are usually about layoffs or replacing people, and in the crisis support world that overlaps with the documented and dire danger of using AI to replace humans in crisis intervention. Both are very real concerns. My approach as the builder of the tech infrastructure that makes human engagement possible has been to keep the framing on automation, not replacement. The tech does more so the mission can have more human connection, not less.

We've also been clear philosophically: AI is not going in front of the survivor. We're not putting a bot up to triage people. Our mission is to put a survivor in contact with a trained human. Everything Claude does at RAINN is on the way to that connection, not in place of it.

Nonprofits

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698f525504b02eec936ac514_692e248602b0e973666dc35b_og-nonprofit.jpeg)

Turn limited resources into lasting impact. Generate grant proposals, track program outcomes, and free your team to focus on serving your community.

Read more

[Read more](https://claude.com/solutions/nonprofits)Read more

Nonprofits

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Turn limited resources into lasting impact. Generate grant proposals, track program outcomes, and free your team to focus on serving your community.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Nonprofits

Turn limited resources into lasting impact. Generate grant proposals, track program outcomes, and free your team to focus on serving your community.

"The role of the technology is to clear the path between the survivor and that human being."

William Bondurant

CTO, RAINN

## Anthropic: RAINN's work extends beyond direct support into policy. Does that shape how you approach building AI tools in this domain?

**Bondurant:**  It does. We have a policy team that works on legislation like the Take It Down Act, so we understand tech-enabled sexual abuse (TESA) from the legislative side, not just the support side. That perspective shapes how we build. We know what survivors are up against, and we build survivor-facing tools accordingly: every channel is encrypted end to end, and survivor conversations stay inside our own environment—they’re never sent to the AI tools we build with.

## Anthropic: RAINN has been firm that AI will not replace your victim services staff. Why is that line so important?

**Bondurant:** We are not going to replace our victim services staff with AI. How we're going to use AI is to automate and get that human being to a human being quicker, faster, and better.

The hotline has been around for 32 years, and what's made it work is that on the other end of the line, when someone finds the courage to call, there's a person. A trained person who knows what they're doing. The role of the technology is to clear the path between the survivor and that human being.

## Anthropic: What's next on your roadmap?

**Bondurant:** The next build I want to do is a real-time search sidebar for our support specialists. Think about how the Claude plugin appears in Excel, Word or PowerPoint. I want that for the support specialists. It would surface what the support specialist needs, right when they need it, without storing anything, and without Claude ever reading the survivor’s side of the conversation. The specialist asks a question; the sidebar answers from our own information database.

As an example: what's the statute of limitations in a given state? Today, the support specialist has to swivel over to the information database we maintain internally, look it up, and come back to the conversation. Same thing with local resources. The goal is if someone needs to know where the nearest shelter is in a given city, the sidebar would surface the address. The survivor doesn't wait.

## Anthropic: What advice would you give to other nonprofit leaders thinking about adopting AI for mission-critical work?

**Bondurant:** Two things. First, don't let the headlines convince you AI is just about cutting headcount. If you approach it that way internally, you'll lose your team. Instead, approach it as automation that frees your people to do more of what they're trained to do. That's a different conversation.

Second, take your encryption and confidentiality requirements seriously when you pick platforms. The technology has to be aligned with your mission. For us, that meant going with platforms where the privacy story is end-to-end. If you skip that step, the rest of what you build doesn't matter.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Prev](#)Prev

[Next](#)Next

## Related stories

[The Epilepsy Foundation turns years of expert content into a personal epilepsy assistant with Claude](https://claude.com/customers/epilepsy-foundation)The Epilepsy Foundation turns years of expert content into a personal epilepsy assistant with Claude

The Epilepsy Foundation turns years of expert content into a personal epilepsy assistant with Claude

Customer story

[Customer story](https://claude.com/customers/epilepsy-foundation)Customer story

[How the Epilepsy Foundation uses Claude across the organization](https://claude.com/customers/epilepsy-foundation-qa)How the Epilepsy Foundation uses Claude across the organization

How the Epilepsy Foundation uses Claude across the organization

Customer story

[Customer story](https://claude.com/customers/epilepsy-foundation-qa)Customer story

[Building dignity-driven AI: A conversation with the National Domestic Workers Alliance](https://claude.com/customers/national-domestic-workers-alliance-qa)Building dignity-driven AI: A conversation with the National Domestic Workers Alliance

Building dignity-driven AI: A conversation with the National Domestic Workers Alliance

Customer story

[Customer story](https://claude.com/customers/national-domestic-workers-alliance-qa)Customer story

[National Domestic Workers Alliance helps domestic workers advocate for better pay with Claude](https://claude.com/customers/national-domestic-workers-alliance)National Domestic Workers Alliance helps domestic workers advocate for better pay with Claude

National Domestic Workers Alliance helps domestic workers advocate for better pay with Claude

Customer story

[Customer story](https://claude.com/customers/national-domestic-workers-alliance)Customer story
