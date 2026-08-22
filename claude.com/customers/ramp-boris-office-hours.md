<!-- source: https://claude.com/customers/ramp-boris-office-hours -->

Q&A | Ramp

# Office Hours: Building for the model that doesn't exist yet

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Office Hours with Boris Cherny

[Office Hours with Boris Cherny](https://claude.com/office-hours)Office Hours with Boris Cherny

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7d059559429dfbc08f0905_OfficeHours-YT-Thumbnail-Ramp-F2.jpg)

Office Hours with Boris Cherny

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7ceba17e3c474c1e3f0fde_og_office-hours.webp)

The best engineering teams are rethinking how they work with AI. Boris Cherny talks with technical leaders to uncover what's changing for their teams, from how they’re building with Claude Code to organization design, and the shifting workflows that come with it.

Read more

[Read more](https://claude.com/office-hours)Read more

Office Hours with Boris Cherny

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

The best engineering teams are rethinking how they work with AI. Boris Cherny talks with technical leaders to uncover what's changing for their teams, from how they’re building with Claude Code to organization design, and the shifting workflows that come with it.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Office Hours with Boris Cherny

The best engineering teams are rethinking how they work with AI. Boris Cherny talks with technical leaders to uncover what's changing for their teams, from how they’re building with Claude Code to organization design, and the shifting workflows that come with it.

[Prev](#)Prev

[Next](#)Next

At [Ramp](https://claude.com/office-hours), more agent sessions are now kicked off by automations than by humans. [Boris Cherny sat down with CTO Rahul Sengottuvelu](https://claude.com/office-hours) and Staff Software Engineer Austin Ray to talk about treating agents like coworkers, loops versus dynamic workflows, and why they refuse to build for the model that exists today.

### Read the full transcript:

**Rahul Sengottuvelu, Chief Technology Officer, Ramp:** One of the first things I tried when I got my hands on Fable was I wanted to find a use case in Ramp that we can empirically verify. So it must be a large piece of code that I haven't read, that Fable wrote. It must be in a non-product place. So something in CI. So this is for us in our testing suite. And I wanted to empirically verify it. To be able to produce a lot of data and check if the code is acting like it should. It's been working really well. We're running it for a few weeks in shadow, and it's been consistently faster than what our current implementation is. But I threw the deep critical problems in our codebase. So we have this large monolithic Python code base, and I told Fable to fix all our import cycles. I also told it to make our app lazy. So the app boots up, and it's an enormous amount of Python modules, and Fable made a lot of progress in both of these. A lot of this code was merged. Really understanding what the boundary of where these models break is very important, because those are the problems that we would want our people to try when the next Fable comes out or the next release comes up.

**Boris Cherny, Creator of Claude Code, Anthropic:** I have these tests that I give every model when they come out. And no model ever was able to do all of these things. But this is the first model that just did all the things. And when Fable struggled, I just used a dynamic workflow, you guys have used it. This is where Claude has a bunch of subagents that it orchestrates, and using algebra in the sandbox. But essentially it's a new form of test time compute. And so you just tell Claude: use a workflow and Fable does it. Just yesterday, it actually reduced our CI time from, I think, 18 minute P50 to 6 minute P50. And just optimization after optimization after optimization. And they just kept profiling it. The code landed, then it waited a day and used a routine to schedule itself to run a day later to get that real production data. And then it just repeated this for days on end until it landed all these wins. And then it showed me a chart when it was done.

**Austin Ray, Staff Software Engineer, Ramp:** Rahul loves that. He's a huge CI time minimization advocate.

**Rahul:** It's all I think about.

**Austin:** I just have a follow-up question for you. So when you're doing these dynamic workflows, I would have to expect that you've already built up the familiarity with Fable as a main agent? Like a foreground agent, right? Because there's a lot of learning from what the 40 or 100 different agents are doing in the background that maybe you're not seeing, but you do have to have comfort by that point, because that's a big workload.

**Boris:** The agents have work translation, they might not, they're executed, you know, in parallel or serial. You might add more rounds of adversarial verification or whatever it feels this task needs. So yeah, I just trust it. Essentially my mental model for dynamic workflows is the test time compute. It goes from low to medium, to high, to extra high, to max. And essentially the way to think about this is ‘This is the maximum amount of thinking the model can use.’ It won't always use it, but it's the maximum.

**Austin:** That's why you have it on the thinking dial at the very end, right?

**Boris:** Exactly. And for me, dynamic workflows are just the next level. It's another form of test time compute. It's new.

**Austin:** How do you think about loops versus dynamic workflows for achieving some sort of long horizon thing?

**Boris:** So loops are repetitive work. And dynamic workflows are dynamic work. You don't exactly know what the steps are ahead of time. I use a loop, for example, for babysitting my pull requests, to fix the CI, and rebase them automatically. But then I use dynamic workflows for things like system optimization, where you don't necessarily know what the next optimization is.

**Austin:** It's a total mental model shift. It does feel like using Claude Code for the first time, where you have to start relinquishing a lot of the software engineering workflow, including running commands to this agent, right?

**Boris:** I feel like, if you have a bunch of engineers doing work, loops are slicing a horizontal off of it. If there's one task every engineer does every day, you can maybe take that and put it in a loop or in a routine. And this is something like a code review, babysitting a PR, addressing feedback. We just have dozens of these. I have one, for example, for deleting dead code. This is a routine that runs every day. And then on the flip side, you can do this vertical slice. And for us this is Claude Tag. An example of that is I'll have Tag ship an experiment. It'll make the experiment, it'll land the PR, and then it'll set a reminder for itself, using a routine to monitor and check in the next day, it'll make sure that the exposures are balanced. It'll crank up the exposure, make sure the experiment's running, and maybe a couple weeks later, it'll be like, all right, I'm going to ship this variant and it puts up another PR for that. And I wasn't in the loop at all. At the beginning I asked Claude to do this. I stamped the pull request, but the rest was just Claude. Okay, I want to detour a little bit. I want to hear about your coding setups.

“We’ve tried to build for what comes three to six months down the line, because when you're building for what's available today, it might already be too late by the time you ship.”

Rahul Sengottuvelu

Chief Technology Officer, Ramp

**Austin:** So iTerm2, pretty vanilla. No IDE these days. And as many panes as my monitors can handle. Pretty barebones Claude Code setups, so not a lot of plugins or skills or MCPs, pretty simple CLAUDE.md, inspired by your Twitter posts for the vanilla setup. I think it's the best way to learn the models. And then a good amount of subagent use, adversarial review.

**Rahul:** Yeah, mine's gotten increasingly background heavy, and most of my sessions are information gathering. It's like, why is the memory spiking on the service? Or how can we get this project done faster? And it's a great way to fan out a lot of sessions and gather a lot of context. When I do things local with Claude Code, it's usually more hands on programming, closer debugging, or I need more services or context on my computer.

**Boris:** Has that changed a lot over time? Do you start with an Austin setup of just terminal, terminal, terminal, terminal? And then you move to this?

**Rahul:** We have so many services, a lot going on: databases and message queues and Reddits and all that. And so having multiple instances of local dev running can become a constraint very quickly. Especially with the latest models, I think they require much less hand-holding. And sometimes you just gotta let them cook, get out of the way. And so I found myself carrying my laptop with the lid open a little bit too much. And so then we decided to move.

**Boris:** That's funny. I know exactly what you mean.

**Austin:** Yeah, make sure Caffeinate is running, right?

**Rahul:** So we've implemented agents at pretty much every part of our business, but especially in the engineering lifecycle. So if you take the process of building and shipping software, everything from coming up with ideas, figuring out where the bugs are, getting notified when there's problems in our logs and our systems, to writing the code, to reviewing it. And sometimes after they're deployed, looking for how they're doing in production and seeing if they're doing the thing you want. We've tried to build systems along this whole stack. We've also thought about it from the lens of security, trying to find bugs and other issues.

**Boris:** Okay, so now you're at the point where you're using the model everywhere throughout the whole lifecycle. How did you get there? What was the first place where you started using Claude Code? And then how did agents expand out of that?

**Rahul:** We slowly realized, clearly this thing's going to continue to improve and maybe we shouldn't build for 2.7, maybe we should build for whatever is coming next, or the model after that. And over time as we built these harnesses, we've learned to step back and just wait it out. Because a lot of time we end up removing this scaffolding over and over again, because the model has just outgrown the harness. At any given point, when there's a shortcoming with the harness or the model, we've tried and we're not perfect, we also need to make the product work today because otherwise we won't have a business, but we've tried our best to go the other direction and give the model more tools, more context, more agency with the goal of almost being able to treat our agents like a coworker. So, hey, can you go figure this out? There seems to be some sort of exception that's popping up. Or maybe this customer is complaining of a certain issue. And we want the models to be able to access the right systems, the right level of access, and produce the right amount of right code. And so just wanting that simple goal allows us to figure out what we need to do to give the model enough access to do these things.

**Austin:** I think it's a velocity bet in a lot of ways. Right? Because you're basically saying, I think the stuff we would put in place to make this work now really well is going to become technical debt really quickly. And that's going to slow us down. If we aim a little further in the future or sometimes a lot further in the future, we'll actually make it further with the resources we have.

**Boris:** I have so many questions. But maybe one direction we can take is, how do you make sure they have the right guardrails? They can access this data, but not this data, or how do you make sure the cost is under control? How do you make sure the code quality is good? And how have you guys thought about this as you scale up the systems?

**Rahul:** We've also, at various levels on the stack, tried to implement safeguards. We also studied the trace a lot. One of the things that I think we've tried to focus more on is studying individual traces and less on aggregate level benchmarks. Benchmarks do give us a lot of information cross model, but a lot of the time there's usually a correct trace. It's like, what is the command the model should have run in this scenario, and why did it not get there? Is this a context issue? Maybe it does not have access to the right tool? And just following these simple traces for workflows that should work allows us to get there in the right way. We've implemented a lot of layers of defense, and we'll continue to do that. How many layers we have also allows us to move faster and give it more agency and more access. And so again, at every part of the stack, we've done everything we can to give the model what it needs, but nothing more.

**Boris:** So essentially, you go to BigQuery or Datadog or whatever. And you give it a read-only service key. This is essentially how you think about it?

**Rahul:** That's right. Yeah, exactly. I just want to be able to talk to my agent like I talk to my coworker. And so we're almost focusing on the default experience, the iPhone experience. Where you open it up, there's a text box. You just say what you need to get done, not how to do it. The prompts must be declarative. We don't want people to instruct the agent to do it in a certain way. We just want people to say, implement this feature, or fix this bug, or help this person out. And over time, especially when you focus on the correct trace. So what must the agent do? It must first query the source and then it must query these other sources and read the code in these repos. Just by focusing on what the correct trace in your head is, you can then shape the agent trace purely through prompts and tools and skills to get there. And thankfully we're also on this exponential increase in model capabilities. So maybe if it's not working right now, you just got to trust that it will get there. With that belief alone, just ship it and wait.

**Austin:** And the one thing I'll add is good old fashioned hard controls on top of that, like you said, principle of least privilege stuff. The basics of not even giving it the opportunity to do certain things.

**Boris:** And how do you think about enforcing it? Is it the security team's job to do this, or are you federating out the design of these sorts of systems? How do you think about that?

**Rahul:** The really exciting part about this is the infrastructure has been built by the security team, and the security team is very closely related to this. So they helped us set up the network access policies. They helped us get the keys. And they're also regular users of these agents.

**Boris:** How do you think about cost controls? How do you think about code quality? What else do you think about as you scale it?

**Rahul:** We're continuing to look for cases where, again, we can guarantee we know for sure the worst thing that could happen if, for example, this code has a bug or something like that, the effects are extremely constrained and we do have an upside and we're finding more problems like that. And we're trying to use this hammer for that. We're also expecting a massive increase in the amount of productivity, especially with the next few models coming. And so we're readying our verification loops, especially with CI and CD.

**Austin:** I think also changing what our reviewers look for over time because as the models get smarter, they stop making certain classes of mistakes. And so it's not worth spending your reviewer tokens on that anymore, right?

**Rahul:** Yeah. We've invested in our own code review bot as well, which is also built on Inspect, our background agents API. We pull from some memories of things that we especially want to look for. We have certain teams that write their own skill files that look for certain things so that they can codify the knowledge that they have built up over the years into these files that allow people to move a little bit faster.

**Boris:** It sounds like it's not just Austin and Rahul going in and breaking down every bottleneck. Although I'm sure you're doing a lot of this, how do you create a culture where engineers feel empowered and have the visibility and the tools, whatever you need, to find the bottleneck and to break it down?

**Austin:** It's just Ramp, right? Yeah.

**Rahul:** I think a lot of it is the culture that the company has built: a culture of experimentation, a culture of building something that maybe didn't pan out, and that's okay. We've tried something. You move quickly. I think one of the things that has been helpful is, because we've had free access to all the tools, to all our engineers, we don't really like to impose a certain token budget or a tool budget, or tell people that they should use this thing or that thing. And in general, it becomes a lot easier to speak the same language.

**Boris:** It sounds like you guys just built a huge number of these background agents, various APIs and systems internally. So you mentioned Project Glass, you mentioned Inspect, walk me through these. What are these tools? How do you use them? How are they built?

**Austin:** Yeah. So Glass is the home base for our non-technical folks. It's where they interact with the coding agent on a daily basis. And it's been our belief since the beginning that everybody should have access to this power. And this velocity increases. But you got to meet people where they are. They don't want to be looking at code. All the technical detail is not going to help them go faster. And some things need to be set up ahead of time.

**Rahul:** Yeah. Inspect, at this point, is basically a digital coworker. We've tried to give Inspect all the tools that a Ramp builder, so a product engineer or design person, would have. So this includes access to GitHub, and Linear, and Slack, and Datadog, and Sentry, and various other tools. And at this point you can ask Inspect to solve a support ticket, or fix a GitHub issue, or look at a Sentry error, or Linear ticket or Zendesk ticket, whatever it may be. It runs on Modal in the background.

**Austin:** You access it via web. Yeah. And a lot of people kick off stuff from Slack. So if you're in a conversation with someone about something and you @Inspect, can you go handle this or can you put up a PR to fix this or investigate this? And that actually ended up being the main way that adoption was spread, because you would hop into someone else's thread and @Inspect. Can you help them with this? And they'd see it and go, oh, you can just do that? Great.

**Rahul:** Yeah. And every PR now comes with its own VM and it's running for a little while so people can take over sessions, collaborate, it's all link based. It's all multiplayer. It just works out of the box. And again we've tried to focus on the correct trace, like, what should this agent have done? And try to shape it that way, so that it can do a lot. At any given point, sometimes people feel the urge to move back to local dev. We haven't fully finished this project, but we've tried to give Inspect that additional tool, that additional repo or dependency that allows people to stay a little bit further in the background.

How Anthropic teams use Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6905133b69fcac6a5cbadb2f_og_how-anthropic-teams-use-claude-code.jpg)

From debugging production issues to navigating unfamiliar codebases to building custom automation—here's how teams across Anthropic use Claude Code.

Read more

[Read more](https://claude.com/blog/how-anthropic-teams-use-claude-code)Read more

How Anthropic teams use Claude Code

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

From debugging production issues to navigating unfamiliar codebases to building custom automation—here's how teams across Anthropic use Claude Code.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

How Anthropic teams use Claude Code

From debugging production issues to navigating unfamiliar codebases to building custom automation—here's how teams across Anthropic use Claude Code.

"We don't really like to impose a certain token budget or a tool budget, or tell people that they should use this thing or that thing."

Rahul Sengottuvelu

Chief Technology Officer, Ramp

**Austin:** I also do want to mention On-call Assistant, which has always run on Claude Code. And that's another instance of just taking what works really well locally, proving it out locally, building up the skills and MCPs and prompts that make, essentially, an AI SRE run really well on incidents to root cause them and put up PRs of fixes and then just packaging that and having it run in a container with safeguards and guardrails. So On-call Assistant runs on every incident that gets assigned to our engineers. So that includes customer support tickets that require an engineer, but also includes system-level incidents. We're working on it. And then it comes back in with a really solid root cause analysis in the Slack channel that we have for every incident. And then the incident responders interact with it. And we've had that running since late February or March. The stuff you can build on the primitives on this sort of Unix philosophy, Claude Code executable, it's just wild.

**Boris:** Yeah. We have a bunch of really similar tools internally. And now Claude Tag, which sounds pretty similar to Inspect in a lot of ways. It's also multiplayer. It's also proactive. It's in Slack. It's taken over a lot of these special purpose bots. I wonder if you guys are seeing the same thing?

**Rahul:** Yeah, we're seeing something similar. So more Inspect sessions are coming from automations than humans at this point. So every time, there is some sort of trigger. Sometimes they're scheduled at a certain time of the day, sometimes they're from other external systems. Then a session kicks off and sometimes notifies people in channels or by DM.

**Boris:** And I guess for this one also organizationally, culturally, how do you do it? Is it like each of these automations is built by different teams that's closest to it? Or do you have like a central dev infra or like AI team that is responsible for all of these?

**Rahul:** It's been, surprisingly, very decentralized, and we're very happy about that. There are teams that maintain certain abstractions, the Inspect team, as you mentioned, the Inspect abstraction, which is a bedrock for a lot of these automations. But there's also competing harnesses. And if you let everybody build what they would like to build, we're okay with that. And we want that, we want more of it. All we can do is build a great product, so other teams are incentivized to build on top of us. But we've tried to keep the culture of not preventing anybody from doing what they want.

**Austin:** It's also a mix of desire paths, of people expressing the want for the same sort of thing, or building the same thing separately, and then the platform team going, okay, let's make a solid thing for this. And vision from the platform team of we're going to need this when the model gets smarter.

**Rahul:** So taking a step back, one of the things that we've tried to do is not impose limits on how many tokens or dollars each individual spends. We want them to be able to access any level of intelligence without limits. So because of that, we've tried to do everything else in our power to make sure that people can step up and get that intelligence where they want. So that includes things like defaults. It's using batch and flex APIs. It's using cheaper models for automations when they're not human controlled. So we always expect to stay on the latest frontier. And so we don't want features or people to overfit on a certain model's behavior.

**Austin:** And then there's a good amount of just talking to people too. I think you and I have both done this where we see someone suddenly become a top spender in a certain month, way above what they normally do. And we reach out to them and say, hey, what are you working on? It looks like you're spending a lot. I'm curious. And if it's something that you're not planning on platformizing, but is platformizable, let's work together, let's do that, let's expand the impact. And if it's a mistake then I'll help you with that. And then we can work on getting the costs down later if it's something you do want to platformize.

**Boris:** So essentially it's this culture of experimentation and innovation. It's letting you just totally automate big swaths of work that used to be manual before. So obviously it works. And so then your job is to support people and optimize the use case after it takes off.

**Rahul:** Yeah. And so the other way to look at it almost is, if you are in the positive ROI section where you know that every dollar you spend on tokens, you're actually making more than $1, you actually don't want to be minimizing costs. We also expect the level of intelligence that Fable has, the cost of that to decrease over time as it has for the last few years. It's not anything new. And we'd rather have everybody at Ramp be familiar and really good at pushing the frontier and pushing with intelligence, making it sweat on hard problems sooner than later.

**Boris:** What is your advice to your peers, to other CTOs that are trying to figure out, what do you do? How do you adopt agents? How do you make your way through this thing that's happening in the industry?

**Rahul:** We've made a lot of progress in the models today. We have great tools at our disposal. But I think the thing that people don't pay as much attention to is also the rate of change and how much things are changing over the last few years. And if you pay more attention to that as opposed to the current snapshot, then you begin to see the pattern of rising intelligence and agency, the ability for models to do more things. And I think we've tried to build for what comes 3 to 6 months down the line, because sometimes when you're playing catch up and you're building for what's available today, it might already be too late by the time you ship. And so, paying attention to the scaling itself has been very helpful for us.

**Boris:** All right. So with that, Austin, Rahul, thank you guys so much for taking the time and for hosting us in this beautiful space. Thank you.

Claude Enterprise

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a4e8f1c4eb05b098011e591_claude%20ent%20marginalia.jpeg)

Put Claude to work across your organization. Help everyone think deeper, do more, and build securely.

Claude Enterprise

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Put Claude to work across your organization. Help everyone think deeper, do more, and build securely.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude Enterprise

Put Claude to work across your organization. Help everyone think deeper, do more, and build securely.

[Prev](#)Prev

[Next](#)Next

## Related stories

[How Notion ships and scales agents with Claude Managed Agents](https://claude.com/customers/notion-qa)How Notion ships and scales agents with Claude Managed Agents

How Notion ships and scales agents with Claude Managed Agents

Customer story

[Customer story](https://claude.com/customers/notion-qa)Customer story

[Deepgram ships 4–10x more durable code with Claude](https://claude.com/customers/deepgram) Deepgram ships 4–10x more durable code with Claude

Deepgram ships 4–10x more durable code with Claude

Customer story

[Customer story](https://claude.com/customers/deepgram)Customer story

[Office Hours: Building the case for leaders who ship with DoorDash](https://claude.com/customers/doordash-boris-office-hours) Office Hours: Building the case for leaders who ship with DoorDash

Office Hours: Building the case for leaders who ship with DoorDash

Customer story

[Customer story](https://claude.com/customers/doordash-boris-office-hours)Customer story

[Office Hours: Asynchronous coding and the end of the IDE with Spotify](https://claude.com/customers/spotify-boris-office-hours) Office Hours: Asynchronous coding and the end of the IDE with Spotify

Office Hours: Asynchronous coding and the end of the IDE with Spotify

Customer story

[Customer story](https://claude.com/customers/spotify-boris-office-hours)Customer story
