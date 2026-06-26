<!-- source: https://claude.com/customers/magicschool-qa -->

Q&A | Claude Platform

# MagicSchool on building a safety layer for millions of student conversations

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0b7959f6481138607f2de6_logo_magicschool-light-mode%20(1).png)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0b79661e044e7194e4e56d_logo_magicschool-dark-mode%20(1).png)

Industry:

Education

Beneficial Deployments

Company size:

Small

Product:

Claude Code

Location:

North America

8 to 10 million student messages

moderated in real time each month

7 million educators

use the MagicSchool platform across 13,000 schools and districts

Case Study: MagicSchool transforms K-12 education for 7 million educators

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0b7a5608aec6888cf76c81_Screenshot%202026-05-18%20at%201.44.55%E2%80%AFPM.png)

With Claude, MagicSchool supports 13,000+ schools and districts and millions of students.

Read more

[Read more](https://claude.com/customers/magicschool)Read more

Case Study: MagicSchool transforms K-12 education for 7 million educators

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

With Claude, MagicSchool supports 13,000+ schools and districts and millions of students.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Case Study: MagicSchool transforms K-12 education for 7 million educators

With Claude, MagicSchool supports 13,000+ schools and districts and millions of students.

[Prev](#)Prev

[Next](#)Next

*Q&A with Keanon O'Keefe, Senior Product Manager, AI Trust, Safety, and Quality, and Chris Rohlfs, Staff Data Scientist, AI Trust, Safety, and Quality at MagicSchool*

[MagicSchool](https://www.magicschool.ai/) is a K-12 AI platform used by more than 7 million educators across 13,000 schools and districts. MagicSchool’s AI-powered platform helps teachers save time by streamlining lesson planning, providing personalized student feedback, and creating engaging content for students. MagicSchool recently built a Claude-powered safety layer that moderates 8 to 10 million student messages in real time each month, reducing the false positive rate of self-harm and mental distress signals by 3x. Because students are minors, the deployment follows Claude's API requirements for minor users. We spoke with Keanon O'Keefe, Senior Product Manager for AI Trust, Safety, and Quality, and Chris Rohlfs, Staff Data Scientist for AI Trust, Safety, and Quality, about how it works, why precision matters more than recall, and what happens after a flag goes off. The following conversation has been edited for length and clarity.

## Anthropic: Set the stage for us. What is MagicSchool, what are students actually doing on it, and where does the new safety moderation layer fit in?

**Keanon O'Keefe, MagicSchool:** MagicSchool is the most widely used AI platform in K-12 education, supporting millions of educators worldwide. Built by educators, we serve as the AI Operating System for schools, bringing together teacher tools, student-safe learning experiences, and district-level governance in one connected platform. We leverage Claude to power our safe, student-facing AI experiences. This includes, but is not limited to, our tutoring and study tools, as well as chatbots, which account for millions of student interactions a month. The new safety moderation layer was rolled out as part of the existing interface, with better signals and responses for crisis, not a separate, bespoke tool for students.

## Anthropic: Even with a platform built for the classroom, K-12 is a hard moderation problem. What's the core challenge?

**Chris Rohlfs, MagicSchool:** One of the challenges we face is that K-12 students naturally explore and push boundaries. We need the AI we provide to the classroom to be robust and to adhere to strict guidelines we set for safety, fairness, and educational value.

## Anthropic: What did your safety approach look like before this layer, and where was it falling short?

**O'Keefe:** We've been using off-the-shelf third-party systems to help us flag student messages, but as we grew and reviewed more message threads, we began to see where context awareness was not always flagged appropriately. The existing systems were not able to specialize to our specific educational use cases and we found ourselves fighting false positive and false negative results across various categories.

## Anthropic: When you say "safety moderation," what is the layer actually looking for, and how does it work?

**O'Keefe:** The Haiku-based moderation prompt specifically identifies indicators of student self-harm or mental distress. For moderating student messages, we started leveraging Haiku 4.5 as an LLM Judge specifically focused on self-harm and mental distress concerns, as the off-the-shelf solutions we were using struggled with the nuance and complex language in these messages. As a student interacts with one of our tools, their inputted messages are moderated in real time. We send the message text to the LLM Judge via the API. If the LLM Judge or one of our moderation tools flags the message, we alert the teacher immediately.

## Anthropic: Over-flagging has its own cost. What does that look like in practice?

**O'Keefe:** It's immensely critical. We owe it to students and teachers to ensure their AI interactions are safe and monitored. We alert when we detect potential critical issues in student interactions, such as violence or self-harm, and teachers expect to be alerted where they can be acted on immediately. However, flagging the wrong issues or flagging unnecessary concerns creates noise, erodes trust, and risks missing a true concern. When incorrect alerts requiring rapid response reach designated action channels, the reputational harm extends well beyond noise. And, missing a dangerous message prevents a teacher or administrator from being able to address a student and intervene quickly and appropriately.

## Anthropic: Walk us through the model choice. Why Haiku 4.5 specifically as the judge?

**Rohlfs:** We put every model through extensive red-teaming before it goes into the platform. For our student-facing tools, where the stakes are highest, Claude has consistently been the strongest choice, most notably for its high performance against our safety benchmarks. MagicSchool has multiple layers of defense, including prompting that we regularly test across real and synthetic edge cases. The Haiku-driven moderation layer is an additional check that helps teachers identify when students enter potentially concerning content. We've validated it against established external benchmarks and our own user data, and found it accurately flags concerning cases without overflagging benign content, outperforming alternative moderation services at the speed and volume we require.

‍

"Our separate Claude-powered student AI tools provide a response directly to the student, which may include relevant resources or recommendations as appropriate."

Keanon O'Keefe

Senior Product Manager, AI Trust, Safety, and Quality

## Anthropic: What is the impact when moderation tools flag too many false positives?

**Rohlfs:** If a moderation tool raises too many flags for perfectly normal content, educators stop looking to it as a meaningful signal. Being precise, both in terms of when there's an issue and why it's troubling, is key for safety.

Our moderation tool has consistently been effective at identifying real signals of self-harm and mental distress, but it used to also give false alarms. Through our partnership with Anthropic and advances to our moderation system, we've achieved a 3x reduction in incorrect flagging across key categories. Now when a teacher gets an alert, they can trust it and act on it with confidence.

## Anthropic: What happens when the system flags a message, and is there a mandated process from there?

**O'Keefe:** Two things happen. First, the teacher receives an in-app alert. Site or district admins control if they get notified via email. Second, our separate Claude-powered student AI tools provide a response directly to the student, which may include relevant resources or recommendations as appropriate. Each district is governed by its own policies and protocols, so the rest of the process varies by district. One option is to pause the interactive student chat rooms to prevent any student interaction after classes. For after-hours monitoring, some schools and districts employ additional platforms or companies that offer human review of flagged messages.

## Anthropic: What other safeguards are in place beyond this moderation layer?

**O'Keefe:** Regular in-chat reminders of the AI's role, potential inaccuracy, and prompts to take a break. Structured prompting around each tool, separate from the moderation layer, that enforces boundaries and task focus. An auto-eval pipeline that flags issues from model and usage drift, plus regular testing against real and edge-case scenarios.

## Anthropic: Walk us through what implementation actually looked like.

**O'Keefe:** We already had the API integration in place for supporting our main application.  Next, we looked at prior conversations, developed a judge prompt that could help us effectively identify high-risk interactions and tested its performance. After just a few iterations of the prompt, we began to see a 3x reduction in false positives.

**Rohlfs:** Out of the box, Claude is solid, but our customized prompts are what get it to meet the needs of our user base. We've found Claude to be highly effective at sticking to the guidelines we set, and it's absolutely critical that we're crystal clear on exactly what we're looking for. We feel and appreciate Anthropic's leadership in API design. When Anthropic upgrades its models, we don't have to rearchitect how we talk to them. Everything just works the same way. That kind of stability matters a lot when you're running millions of classroom interactions a week.

## Anthropic: Beyond the safety work, your engineering team has been adopting Claude Code. What does that look like?

**Rohlfs:** Claude Code is an integral part of our AI Assisted Coding initiative. We are focusing on infrastructure to enable and amplify Claude Code in our development process. Creating agents, rule sets, skills and plugins. There's a wide variety of ways MagicSchool engineers use it. Some folks hook it up to Notion and Linear for project management. I use it to create and simplify documentation or check that content follows our style guides. Some team members have even assigned it simpler, low-stakes tickets that it handled without incident. One important measure of impact is, when you give developers a choice, what do they use? Based on survey results of the engineering team, leadership upgraded us to an Anthropic enterprise account.

## Anthropic: What does this approach to safety let you do that you couldn't before?

**O'Keefe:** With moderations, I can sleep better knowing we have a solution in place that effectively detects high-risk messages on our student platform. A 3x reduction in the false positive rate of self harm and mental distress signals helps us earn the trust of our customers and ensure we're creating a responsible and safe AI experience for students. MagicSchool and Anthropic share similar values and methodologies with advancing AI and its impact on people. We focus on creating healthy and safe AI interactions that drive meaningful value.

Education

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698f5245ff22e3ab8e64405f_68c469d2d09b203c164ad8e6_og-claude-education.jpeg)

Trusted, responsible AI tools for students and educators, from personalized learning to research assistance.

Read more

[Read more](/solutions/education)Read more

Education

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Trusted, responsible AI tools for students and educators, from personalized learning to research assistance.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Education

Trusted, responsible AI tools for students and educators, from personalized learning to research assistance.

"MagicSchool and Anthropic share similar values and methodologies with advancing AI and its impact on people."

Keanon O'Keefe

Senior Product Manager, AI Trust, Safety, and Quality

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Prev](#)Prev

[Next](#)Next

## Related stories

[How the Garvan Institute is changing the way it does science with Claude](/customers/garvan-institute-qa)How the Garvan Institute is changing the way it does science with Claude

How the Garvan Institute is changing the way it does science with Claude

Customer story

[Customer story](/customers/garvan-institute-qa)Customer story

[How YMCA South Australia is building an AI-powered nonprofit with Claude](/customers/ymca-south-australia)How YMCA South Australia is building an AI-powered nonprofit with Claude

How YMCA South Australia is building an AI-powered nonprofit with Claude

Customer story

[Customer story](/customers/ymca-south-australia)Customer story

[How Syracuse University deployed Claude to every student, faculty member, and staff](/customers/syracuse)How Syracuse University deployed Claude to every student, faculty member, and staff

How Syracuse University deployed Claude to every student, faculty member, and staff

Customer story

[Customer story](/customers/syracuse)Customer story

[How a philanthropy veteran built an AI fundraising tool for nonprofits with Claude Code](/customers/kindora)How a philanthropy veteran built an AI fundraising tool for nonprofits with Claude Code

How a philanthropy veteran built an AI fundraising tool for nonprofits with Claude Code

Customer story

[Customer story](/customers/kindora)Customer story
