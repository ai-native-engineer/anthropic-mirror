<!-- source: https://claude.com/customers/epilepsy-foundation -->

Case study | Claude Platform

# The Epilepsy Foundation turns years of expert content into a personal epilepsy assistant with Claude

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a5f65c6fd705dd371878f31_Epilepsy-foundation_light.png)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a5f65bf5bef5e4e2da75b45_epilepsy-foundation_dark.png)

Industry:

Beneficial Deployments

Company size:

Medium

Product:

[Claude Platform](https://claude.com/platform/api)

Partner:

AWS

Location:

North America

60,000 interactions with Sage

reached in under a year, before any major promotion

2.5x more interactions per session

From 1.2 to 3 since launch, as trust in Sage grew

[The Epilepsy Foundation](https://www.epilepsy.com/) is the leading nonprofit serving people with epilepsy across the United States. The organization is built around a simple mission: no one should face epilepsy alone. For more than two decades, its website, epilepsy.com, has been the authoritative source for epilepsy and seizure information. Today, a Claude-powered assistant named Sage turns that library into a personal conversation for anyone who needs one.

## With Claude, the Epilepsy Foundation achieved:

* 60,000 interactions with Sage, the Foundation's AI epilepsy assistant, in under a year, before any major promotion push
* 2.5x more interactions per session since launch, from 1.2 to 3 since launch, as trust in Sage increased
* Every answer grounded in 3,200 pages of medically reviewed content, with helpline and partner fallbacks
* Half a day to test and deploy each new Claude model, using a 20-question clinical benchmark
* Weekly, at-scale analysis of Sage conversations to surface community needs and refine guardrails

## The challenge

Q&A: The Epilepsy Foundation

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a59cacb6a5ea34a1b7ab877_og_case-study-EP%20Foundation%20(1).jpg)

How the Epilepsy Foundation uses Claude across the organization

Read more

[Read more](https://claude.com/customers/epilepsy-foundation-qa)Read more

Q&A: The Epilepsy Foundation

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

How the Epilepsy Foundation uses Claude across the organization

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Q&A: The Epilepsy Foundation

How the Epilepsy Foundation uses Claude across the organization

## People getting lost in 20 years of content

[Epilepsy.com](http://epilepsy.com) is the source people turn to when epilepsy enters their lives, whether they have just been diagnosed, are caring for a child, or are supporting a loved one. Somewhere between 8 to 10 million unique visitors come to the site each year, with about 35% coming from outside the United States. It’s trusted because every page is reviewed by the Foundation's expert editorial board, which is drawn from the nation's leading epileptologists and neurologists. These editors write or review every page and ensure that nothing is published without their sign-off. "There's no other place anywhere that has the depth and breadth of content that we have," said Sarah Klein, Chief Engagement Officer at the Epilepsy Foundation.

With such a wealth of content, the challenge arose when visitors needed to find the right information. The library consisted of tens of thousands of pages, and finding the right answer took real persistence. "People got lost in the rabbit hole of what was at one point 50,000 pages of content," Klein recalled. "You would have to be really committed to finding what you needed to find."

No fixed path could fit everyone. "No two people have the same epilepsy journey," Klein added. The site was strong at guiding a visitor to the right page, but building a route through content that met each person where they were proved much harder. At the scariest moments—a parent up at night or someone still absorbing a diagnosis—that gap sent people away from the one expert-vetted source and into the rest of the internet, where nothing had been checked.

## The solution

Beneficial Deployments

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a57d4749f1d659f155a38d4_Screenshot%202026-07-15%20at%2011.41.43%E2%80%AFAM.png)

Accelerate the work that matters most

Read more

[Read more](https://www.anthropic.com/news/claude-for-nonprofits)Read more

Beneficial Deployments

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Accelerate the work that matters most

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Beneficial Deployments

Accelerate the work that matters most

## Choosing a model with empathy built in

To tackle this challenge, the Foundation decided to build Sage. Sage itself is an AI epilepsy assistant: a conversational agent, built on Claude. The team started by treating model selection as a clinical question. They wrote 20 baseline questions, 10 a caregiver might ask and 10 from a person with epilepsy, and had its medical editors and researchers write the answer an expert would give. They ran the same questions through five models and scored each on accuracy, empathy, tone, and recommendations.

What they needed was a model that could handle sensitive medical questions with care, not just return accurate facts. Claude stood out on the dimension that mattered most for a vulnerable audience. "I think it was the empathy at the core of the model," said David-Alexandre Jost, the Foundation's Chief Technology and Innovations Officer. "Even though we didn't bake this into our own prompt, at the core, the Claude models were very empathetic."

On healthcare questions, the difference was just as clear: where other models stayed general, Claude went into the specifics and offered real recommendations. Reaching that feel with another model would have meant heavy prompt engineering. Claude arrived with it, so the team could focus on the experience instead of coaxing the model into the right tone.

With the model selected, where to run Sage was the next decision. The Foundation had already partnered with Amazon Web Services (AWS) and moved to the cloud to build a governed foundation three years prior. Security, access controls, and HIPAA compliance were in place before any application sat on top of it. So when Sage was ready, running it on Claude through Amazon Bedrock was the natural next step. Amazon Bedrock also gave them room to grow: Sage could scale from a few hundred conversations a day to several thousand without rebuilding. And because AWS runs the underlying systems, the Foundation's small team can spend its time on the Sage experience itself. Bedrock is model-agnostic, so the team can move fast when a new Claude model ships.

"When a new version of your Claude models comes out, it's usually available the same day on AWS," Jost said. "We just deploy it into our environment, create a test agent, and that takes about half a day." Getting a brand-new model into a working test in half a day is quick, and Jost noted it would be far harder on a system less tightly integrated. Every new Claude Opus and Claude Haiku release then goes through the same 20-question benchmark, and the same human reviewers, before it reaches production.

## Grounding every answer in vetted content

Sage is built on Claude Haiku 4.5 and runs as a widget on epilepsy.com. Every session is anonymous, and every question is answered only from a knowledge base of 3,200 pages of editorial-board-approved content. When the answer is not there, Sage says so and points the person to the Foundation's Helpline or a partner such as a local Affiliate office or the Rare Epilepsy Network, rather than guessing. "Our goal is to bring hallucinations to zero," as Jost put it. That grounding is what lets the Foundation stand behind every response.

Jost is careful not to call Sage a chatbot. "A chatbot is usually a one-way conversation,” he said. “I have a question, it matches the question to some content and delivers an answer. But Sage wants to have a conversation with you. It will not only answer your question but dig deeper on the why, so it can move you in the right direction." If someone asks about a type of seizure and mentions a pregnancy, Sage asks what medication they take, because that combination can matter.

Over time, the team noticed Sage doing useful things no one had explicitly programmed. For example, Sage began offering guidance pulled from the Foundation's vetted articles, like how to handle a situation at school or how to make the most of a few minutes with a neurologist. "We don't have to prompt everything into our agent," he added. "A lot of this is prompted from the knowledge base we created."

"Even though we didn't bake this into our own prompt, at the core, the Claude models were very empathetic."

David-Alexandre Jost,

Chief Technology and Innovations Officer, The Epilepsy Foundation

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## The outcome

## 60,000 interactions driven organically

In less than a year, Sage passed 60,000 conversations, before the Foundation had done much to promote it. A typical week now brings about 1,000 unique sessions and 2,700 interactions, comfortably ahead of the team's early goal of 200 a day. Depth grew with volume, too: the average session has grown from 1.2 interactions at launch to 3, and power users go 20 to 25 turns deep in a single session. "People are trusting Sage more and more, because it gives them value in the conversation," Jost said. "Once you have that trust, they share more, and that context helps the next step."

The conversations that stay with the team are the ones the count does not capture. One Sunday night, a mother typed in: "My daughter just had a seizure. How long will she be confused? She's 19." Sage explained what was happening, that the confusion could last minutes to hours, walked her through how to keep her daughter safe, and offered the Helpline.

Another user had lived with uncontrolled seizures for two years, along with severe anxiety and worsening ADHD, and had just left an appointment where her neurologist waved off her symptoms. She spent an hour with Sage working through her history, then asked it to save the chat as a reference for her next visit, because she did not want to forget anything and knew she would. Sage generated a structured document organized by symptom, with a timeline and her questions. "This is actually spectacular," she wrote back. "I'm so glad I found this feature." Jost added that this wasn’t actually a feature, but Sage’s behavior adjusting in real time. "This is Sage creating a tool based on the need of that user," Jost said.

That pattern points to where the Foundation is headed. Power users are treating Sage as a diary, which matters most for community members with cognitive challenges, and the current version cannot carry memory across sessions yet. The next iteration, Sage Next, is being built on [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) with authentication and short-term and long-term memory, so Sage can carry what someone shared weeks ago into a later conversation. "The vision for Sage was to really help you navigate all of that content,” Jost said. “But now Sage is more than this. It's your companion in your epilepsy journey."

"When a new version of your Claude models comes out, it's usually available the same day on AWS."

David-Alexandre Jost,

Chief Technology and Innovations Officer, The Epilepsy Foundation

## Related stories

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

[RAINN brings crisis support to encrypted messaging platforms with Claude](https://claude.com/customers/rainn)RAINN brings crisis support to encrypted messaging platforms with Claude

RAINN brings crisis support to encrypted messaging platforms with Claude

Customer story

[Customer story](https://claude.com/customers/rainn)Customer story
