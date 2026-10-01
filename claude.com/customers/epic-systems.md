<!-- source: https://claude.com/customers/epic-systems -->

Q&A | Claude Code

# A conversation with Seth Hain about Epic’s internal AI adoption

[Contact sales](https://claude.com/contact-sales)

![Epic logo](https://assets.claude.com/eba99cadd0dd874d08d32b4f4c0cfbea1596372e.png)

Industry:
:   Healthcare

Company size:
:   Large

Product:
:   Claude Code

Location:
:   North America

195 million

patients globally use MyChart

Over half

of Claude Code usage is from non-developers

The Enterprise AI Transformation Guide for Healthcare & Life Sciences

![The Enterprise AI Transformation Guide for Healthcare & Life Sciences](https://assets.claude.com/c5ab9a4570d97f2864fdab84b83b2ae79e618f39.jpg?w=2400&q=75&fm=webp&fit=max)

Accelerate your enterprise AI transformation with proven strategies from Anthropic's customers.

[Read more](https://resources.anthropic.com/hcls-transformation-guide)

Advancing Claude in healthcare and the life sciences

![Advancing Claude in healthcare and the life sciences](https://assets.claude.com/2245c8d44d57bbbd808ee21e2a14a250946d583b.png?w=2400&q=75&fm=webp&fit=max)

Transform healthcare from insight to action

[Read more](https://www.anthropic.com/news/healthcare-life-sciences)

At Anthropic’s *“The Briefing: Enterprise Agents”,* leaders from some of the world’s largest organizations shared how they’re scaling AI adoption. One of those leaders was Seth Hain, SVP of R&D at Epic—the healthcare technology company behind MyChart, which is used by over 195 million patients around the world to access lab results, schedule appointments, communicate with their doctors, and more.

Seth sat down with Jonathan Dahlberg, head of Anthropic’s applied AI team, to discuss how Epic is deploying AI, what’s surprised them along the way, and what’s ahead for healthcare in 2026. The following conversation has been edited for length and clarity.

**Jonathan Dahlberg, Anthropic: How did AI adoption spread across Epic, internally?**

**Seth Hain, Epic:** It was a very natural progression, because we gave everyone at Epic the ability to explore AI. Pockets of learning would develop. It would often start with an individual, and then their teammates and neighbors. We're famously an in-person company, and a key part of that is the natural interactions in the break room or hallway—quick ideas traded back and forth. The excitement of something you build over the weekend and show to a colleague generates momentum. We ended up creating internal tools to help people see who was using AI and what they were doing with it, so others could adopt it quickly and try more.

And the pace kept picking up. When you're using AI personally, you end up having moments of surprise—when you realize what the AI is now capable of. Over the last five or six years, those moments started coming faster and faster, building on each other. Both the core models and the agentic tooling—the layer above the models—are improving. Because we gave everyone the ability to explore AI, everyone saw this happen.

**Dahlberg: Over half of your Claude Code usage is from non-developers. What surprised you about that?**

**Hain:** The folks on the ground have the best ideas, so it’s really important for them to have the opportunity to openly explore how AI works. Some of the most exciting things I’ve seen are non-developers taking tools like Claude Code and applying it to their own workflows.

Here’s a great example. One of my friends is a pharmacist at Epic, and he came back with a full prototype of some new pieces of functionality he wanted in MyChart. With AI, he was able to show everyone what he wanted in a whole new, interactive way—going beyond slides or written documentation. And now it’s a quick link that folks are exploring and then iterating on together.

**Dahlberg: How do you get people across the company to find the time for exploration?**

**Hain:** It starts with leaders spending time with these tools every day. They need to have that familiarity and sense of where things are developing and then use that to extend time to their employees to explore. We have a Friday afternoon meeting with many of our development leads across the company. We took an entire one of those meetings and said, you need to sit down and experience this for yourself. You need to have that aha moment. And it wasn’t just about those four hours, it was about establishing a foundation for our leadership to continue to iterate.

**Dahlberg: How do you build trust in AI in a clinical setting?**

**Hain:** There are multiple layers here. First, clinicians and health systems need to trust that you truly understand their needs. We’ve long required our developers to do immersion—they get on-site, in person. They spend time at the elbow with clinicians and staff to develop an understanding of workflows step by step, where the software fits, where human interactions take place.

And because we work in healthcare, we take “do no harm” seriously. That starts with our own development pipelines. Understanding how we can improve the level of quality of the code as it goes out the door, and how to use new capabilities—like skills and MCP servers—to carry out additional checks we could not do before.

Next, organizations need to be able to evaluate AI before taking it into production, and they need to be able to monitor it on an ongoing basis. Some examples:

* An early capability we released was a summarization of the medical record, and it included links to the parts of the record where clinicians could go verify. That provided a foundation so that as you move to more agentic capabilities, the organization and the users already have confidence.
* We have a capability for physicians and nurses to quickly respond to messages from patients. If you have an individual that is a hundred percent of the time using those drafts without any edit, that’s incorrect. And if you have an individual that zero percent of the time is using any of them, that’s also incorrect. So you have to be able to monitor that.

And the user experience needs to continue to adapt. The AI we use today needs to help acclimate folks across healthcare to what is continuing to come. And that’s where a number of us spend a lot of time at the company—helping think about how product design evolves through these different stages, as both the models and the agentic capabilities continue to improve, and helping users be able to activate these tools effectively.

**Dahlberg: What skills matter most as this technology evolves?**

**Hain:** Openness to adapting. The people who are moving ahead in leaps and bounds are the ones who are exploring and quickly adapting to what the technology makes possible. When you’re thinking about a medical record moving from the ED up to the back office and then to the patient taking care of themselves as they go home with follow-ups, there’s over a hundred handoffs between individuals just in that type of care. The individual that understands that and has spent time immersed in it is going to be able to guide these tools to create the next generation of software and capabilities.

**Dahlberg: Something feels like it’s shifted recently. What’s changed?**

**Hain:** One of the things I’ve noticed both internally as well as with health systems, if you go back 12, 24 months, was that AI was productively helping in segments of a person’s day or segments of a person’s workflow. It would save them time—for example, it would save a physician time in regards to completing their notes based on the conversation in the exam room. Or it would save time for folks at Epic in regards to finding information from some knowledge base. But it was narrow. The result of that was that folks still sort of spent the same total amount of time. They couldn’t insert truly new work into that day.

I think in the last eight to 12 weeks, that has started to shift. Those moments where the human had to jump into the middle have become fewer and fewer. And so now you have this contiguous block where the agents are able to do work and produce a result that somebody can engage with and spend time on. And so I think that’s why it feels qualitatively different now.

One example: we have a team working with customers on operationalizing access to care—making sure patients get scheduled with the right specialist right out of the gate. They built a shared Claude project to have conversations about what was happening across each of their customers. Now, whenever I ask for a status update, I get a link to a Claude conversation that answers the question. It’s functioning as part of the team, not just as an assistant.

**Dahlberg: What advice would you give enterprise leaders who are just getting started?**

**Hain:** Leaders need to be spending time in it. If they’re not, that needs to change right now, and not just at work but also personally. The second thing is to really look at your governance processes and make sure you don’t have unnecessary roadblocks.

Imagine an organization saying, “We don’t really give Excel out to our employees—we don’t trust that they have enough understanding of math and stats to be able to use it to analyze data, so we don’t provide it to them.” I think everybody would agree that that’s not going to be a recipe for success long-term. The same goes for AI. Start with leadership, and open the door to exploration.

**Dahlberg: What’s ahead for healthcare and AI?**

**Hain:** There is an immediate opportunity for agentic AI to help every patient, clinician, and health system operator. From patients getting their medical questions answered in MyChart, to insights for clinicians at the point of care based on the conversation in the exam room, to increased automation in the back office—all on the same integrated platform. This is moving quickly, with 85% of organizations we work with already using AI in production.

Beyond that, we’re building medical event models internally at Epic—AI trained specifically on real-world health records rather than general web text. And we’re seeing scaling laws apply to these models in the same way they apply to natural language models. There’s so much potential here.

‍

> "There is an immediate opportunity for agentic AI to help every patient, clinician, and health system operator."

Seth HainSVP of R&D, Epic

[![League](https://assets.claude.com/7360d174acf8827f869d92d50d49e0add1c58c2c.png)

### How League went all in on Claude in a regulated industry](https://claude.com/customers/league-qa)[![League](https://assets.claude.com/7360d174acf8827f869d92d50d49e0add1c58c2c.png)

### League cuts product development cycle times in half with Claude](https://claude.com/customers/league)[![Arkana Labs](https://assets.claude.com/825b44bd9f2704f71fd53f5125cb92c31b32bd73.svg)

### How can a medical lab keep patients at the center of its work while the caseload keeps growing?](https://claude.com/customers/arkana-labs)[![Zingage](https://assets.claude.com/7a6b9b092d1ec61d938402cc6744e4d94ed2564a.svg)

### How Zingage automates care coordination for 400+ home care agencies with Claude](https://claude.com/customers/zingage)
