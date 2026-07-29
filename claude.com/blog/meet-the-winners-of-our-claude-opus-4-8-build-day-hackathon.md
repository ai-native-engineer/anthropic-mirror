<!-- source: https://claude.com/blog/meet-the-winners-of-our-claude-opus-4-8-build-day-hackathon -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6909386cc7ad3ed2a7ec8eed_Object-ThoughtBubble.svg)

# Meet the winners of our Claude Opus 4.8 Build Day hackathon

From reconstructing Tang Dynasty architecture to polling a synthetic San Francisco, see what the winners of our latest hackathon built with Claude Opus 4.8 in a day.

Get Claude Code

curl -fsSL https://claude.ai/install.sh | bash

Copy command to clipboard

irm https://claude.ai/install.ps1 | iex

Copy command to clipboard

Or read the [documentation](https://code.claude.com/docs/en/overview)

Try Claude Code

[Try Claude Code](https://claude.ai/code)Try Claude Code

Developer docs

[Developer docs](https://code.claude.com/docs/en/overview)Developer docs

  [Claude Code](https://claude.com/blog/category/claude-code)
* Product

  Claude Code
* Date

  June 17, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/meet-the-winners-of-our-claude-opus-4-8-build-day-hackathon

On June 13, we brought more than 300 founders and builders to San Francisco for a 12-hour hackathon with Claude Opus 4.8. More than 1,500 people had applied; 310 took part, many traveling from around the world, each with $500 in credits and one day to turn an idea into a working demo.

We caught up with the three winning teams about what they built and how they used Claude to do it.

Congratulations to the winners and everyone who took part. We hope their projects give you a few ideas of your own.

## First place: [Tekton](https://tekton-build.vercel.app/), Holly Tang and Austin Burgess

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a32e20130b0c237d85e1c09_Claude_Build_Day_258_compressed.jpg)

*Holly Tang and Austin Burgess built Tekton, a 3D reconstruction platform that brings Tang Dynasty architecture back to life, with every component traceable to its historical source.*

When a historic wooden building burns, centuries of craftsmanship can disappear with it. Tekton reconstructs those buildings in 3D and traces every piece back to a documented source.

Give Tekton a historical building and Claude researches it, pulling together schematics, construction documents, photographs, and diagrams, then assembles a 3D model across 339 incremental construction states. When you click any component in the model, Tekton shows where the detail came from and why it was placed there. The team calls this an evidence chain, running from source material to verified model. They built it for academic validation, restoration work, and cultural preservation, starting with Tang Dynasty architecture and the spire of Notre-Dame.

The verification ran entirely on Opus 4.8. Independent verifier sub-agents graded each reconstruction in isolated context windows, and self-correction loops rechecked component placement until all 20 tests passed. Every build was measured against the historical record and its citations, so the finished model follows the documented rules of how the structure was originally built.

Holly Tang and Austin Burgess met a month earlier, in line for coffee at a Code with Claude event. Holly, a designer, has been helping with Austin's startup, [Pearl](https://joinpearl.co/). "I love watching documentaries, and it always upset me to see beautiful buildings lost to fire," Holly says. She had prototyped a single reconstruction on her own; Austin's contribution was scaling it to work on any building, end to end.

To build Tekton, the two worked in stages: they got the spire of Notre-Dame rendering at scale first, then added finer detail, then expanded toward the rest of the structure. Time ran out before the full cathedral was done. Even so, several hackathon attendees asked about it or offered to help make it more accurate. Holly and Austin want to make Tekton open source, so museums, historians, nonprofits, and governments can build on it.

**Advice to other builders:** Map the whole project before you build any of it.

"We built an entire PRD and a Notion board with around 50 tickets, one for each specific task," Austin says. "It was almost like, here's the complete project end to end, and this is exactly what we want for each step." With the plan set, he broke the build into separate workflows and ran them in parallel.

[Tekton on GitHub](https://github.com/tangxiya-star/Tekton)

## Second place: [Sim Francisco](https://simfrancisco.org/), Tanmayi Priya Dasari and Tejas Prabhune

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a32e670a9a0ae0844278fec_Claude_Build_Day_280_cropped_native.jpg)

*Tanmayi Priya Dasari and Tejas Prabhune built Sim Francisco, a Census-seeded digital twin of San Francisco's population that can poll a synthetic city in seconds and forecast real-world outcomes.*

Sim Francisco is a working model of San Francisco's population. It has 10,000 synthetic residents drawn from US Census data, each with their own demographics, personal history, and worldview, placed on a map of the city and reacting to the news in real time.

Ask the city a question and it polls the entire synthetic electorate, neighborhood by neighborhood. Running on models with an October 2023 knowledge cutoff, it forecast the 2024 presidential vote at 81.3% Democratic against an actual 83.8%, and San Francisco's March 2024 Prop A at 70% against an actual 70.38%. It tracks prediction markets like Kalshi and Polymarket within a couple of points.\*

Opus 4.8 wrote the entire front and back end and verified the backend's behavior end to end. To verify the model’s work, the team had Claude work alongside a verifier and an adversarial agent to build a backend that reproduced the city's real demographic distributions.

Tanmayi Priya Dasari and Tejas Prabhune are electrical engineering and computer science majors at UC Berkeley who met through the Machine Learning club on campus. For Tejas, Sim Francisco doubles as a test for the post-training company he's building, where he's working out whether simulated personas can stay consistent enough to train models on long-horizon tasks.

**Advice to other builders:** Don't settle for the first approach that works, especially when it's expensive.

The team's first version made a separate inference call for each of the 10,000 residents, which got costly. "Over time, Claude ran an evolutionary clustering algorithm it created itself," Tejas says, batching residents into about 300 representative personas. The grouped version held the same accuracy against Kalshi, Polymarket, and historical results while cutting inference cost by 10 to 100 times.

[*Sim Francisco on GitHub*](https://github.com/tejasprabhune/simfrancisco)

## **Third place:** [**Custom Universe**](https://www.luminal.com/realtime-edit-demo)**, Jake Stevens and Mauricio Pereira**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a32eb3be6cc4dc20abf6ba5_Claude_Build_Day_241_compressed.jpg)

*Jake Stevens and Mauricio Pereira built Custom Universe, a real-time engine that turns a single phone photo into a fully editable, photorealistic 3D scene.*

Snap a phone photo of a chair, and Custom Universe turns it into a 3D object you can drop into a scene, restyle with a text prompt, and move around while the rendered image updates in real time.

The project is aimed at robotics labs, which need large volumes of synthetic data to train robots for specific tasks and settings. A lab can scan a machine from a factory floor, drop it into a scene, and generate data to fine-tune a robotics model for that exact environment. Building that kind of setup usually means hiring physicists and engineers to handle the physics and collision geometry. Custom Universe lets you arrange a scene by dragging objects around instead, and the team plans to add precise placement, like nudging an object 30 centimeters across a kitchen counter.

Opus 4.8 built the project end to end and operated the remote NVIDIA H100 that ran the model throughout the hackathon. The team also used Claude to work out which models produced the right output and to build the pipeline that brings phone-scanned objects, captured with Apple's RealityKit, into the web app.

Jake Stevens and Mauricio Pereira met at the event. Jake is a Rochester Institute of Technology (RIT) computer-vision graduate who runs [Luminal](https://www.luminal.com/), a startup focused on speeding up AI models; the scene builder started as a side project he had wanted to try. Mauricio, an MIT robotics graduate who runs [Coat Robotics](https://www.coatrobotics.com/), brought the problem he knew firsthand: robotics still lacks training data, and building synthetic environments is hard. Custom Universe relies on open-source models and algorithms and is free to use; the team says users can run it on their own GPUs.

**Advice to other builders:** Use Claude to choose your tools, not just to write the code.

"A lot of the iteration was looking at which model was giving us the right output, so we used Claude to do a lot of the research," Mauricio says. The team also handed Claude unfamiliar technologies to integrate. "For example, Apple RealityKit, and how we were going to make sure people can input their scanned objects to our website. We asked Claude: add this to the pipeline."

[*Custom Universe on GitHub*](https://github.com/jss8649/image-edit-realtime-hackathon)

[*Learn*](http://claude.com/community) *about our Claude Community programs, including meetups, hackathons, and more.*

*\*Sim Francisco is an independent hackathon project that uses forecasting election outcomes as an example. This does not represent an Anthropic endorsement of using AI-simulated election predictions as a use case.*

‍

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225e31f7aa22c1f28cb_46e4aa7ea208ed440d5bd9e9e3a0ee66bc336ff1-1000x1000.svg)

Jul 24, 2026

### Claude models explained: choosing the best model for your use case

Enterprise AI

[Claude models explained: choosing the best model for your use case](#)Claude models explained: choosing the best model for your use case

[Claude models explained: choosing the best model for your use case](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case)Claude models explained: choosing the best model for your use case

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d222061abf091318fb82_423062049d4676b41d52b16068cbb5e21603190e-1000x1000.svg)

Jul 24, 2026

### The new rules of context engineering for Claude 5 generation models

Claude Code

[The new rules of context engineering for Claude 5 generation models](#) The new rules of context engineering for Claude 5 generation models

[The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) The new rules of context engineering for Claude 5 generation models

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d224d39f9b8e905d1823_b68cbb43d7c8f56f0b14cc867e8d4d74445f78b0-1000x1000.svg)

Jul 22, 2026

### Building verification loops in Claude Code with skills

Claude Code

[Building verification loops in Claude Code with skills](#)Building verification loops in Claude Code with skills

[Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills)Building verification loops in Claude Code with skills

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22824d4124c2e33ba8e_b1ce510c468b2920d4f8f61c17a50906801f939a-1000x1000.svg)

Jul 21, 2026

### How Anthropic secures its AI-native software development lifecycle

Claude Code

[How Anthropic secures its AI-native software development lifecycle](#)How Anthropic secures its AI-native software development lifecycle

[How Anthropic secures its AI-native software development lifecycle](https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle)How Anthropic secures its AI-native software development lifecycle

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

Coding
