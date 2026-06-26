<!-- source: https://claude.com/blog/meet-the-winners-of-built-with-opus-4-7-claude-code-hackathon -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229061abf091318fc81_6905c83d0735e1bc430025fdd1748d1406079036-1000x1000.svg)

# Meet the winners of the Built with Opus 4.7 Claude Code hackathon

*From medical training and electronics repair to coding education and factory maintenance, see the projects built by the winners of our latest virtual hackathon.*

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

  June 15, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/meet-the-winners-of-built-with-opus-4-7-claude-code-hackathon

Last week, we hosted [Claude Build Day](https://cerebralvalley.ai/e/claude-startups-build-day), our latest hackathon where builders got together in San Francisco to put their ideas to work using Claude Opus 4.8.

While we wait to see what they built, we chatted with the winners of our Built with Opus 4.7 hackathon about their projects. They tackled medical training, electronics repair, computer science education, interactive play, home repair, and factory maintenance.

Congratulations to the winners and to everyone who participated! We hope their ideas will inspire you.

## First place: [Medkit](https://bedirhankeskin.com/), Bedirhan Keskin

Bedirhan Keskin, an Istanbul-based physician-turned-software engineer, used Claude Managed Agents to build Medkit: a learning tool for medical residents or junior doctors, simulating real-life patient encounters in a gamified medical clinic.

"When you're alone in an emergency department with 50 patients waiting and you realize there are cases you never practiced in medical school, you end up practicing them on real patients in real time," says Bedirhan.

With Medkit, medical students practice diagnosing and treating simulated patients, using the tool to take medical history, order labs, read imaging, diagnose, and prescribe treatment. At the end, an agentic grader assesses the full encounter against the same published clinical guidelines that a board examiner would use.

Bedirhan built Medkit across four separate Claude Code sessions (voice engine, content generation, 3D game layer, and a core app), keeping each context clean and progressing on all at once. He followed a “talk, don’t type” approach, working almost entirely by voice.

Medkit is already gaining traction, with three medical faculties and a pharma company, all based in Istanbul, set to start running pilots in the coming weeks.

**Advice to other builders:** Work with Claude as a thought partner, not just a coding agent.

Bedirhan’s first instinct was to self-host the voice engine, but Claude suggested using a cloud provider to move faster. “What I value most about Claude is it’s not just a code generator, but a thought partner helping me see options I'd otherwise miss,” he says.

[*Medkit on Github*](https://github.com/bedriyan/medkit-app)

## Second place: [Wrench Board](https://wrenchboard.cloud/), Alexis Chapellier

Alexis Chapellier from Reignier-Ésery, France, spent years fixing electronics before creating [RepairMind](https://repairmind.io/), an AI-powered management platform for repair shops. His Opus 4.7 hackathon project, [Wrench Board](https://wrenchboard.cloud/), helps independent technicians figure out complex repairs. Users drop in a schematic and a boardview and describe the symptoms, and the agent creates a unified electrical graph, reasons over it, points to the exact pad to probe, reads measurements, and updates its hypotheses until it diagnoses the issue.

Alexis prototyped Wrench Board in Claude Design, separating the app’s responsibilities (design, schematic ingestion, boardview, diagnostic agent) and producing first a spec and then a plan for each one. He executed in Claude Code’s multi-agent mode, benchmarking at every step by running five or six agents in parallel during debugging, with one dedicated agent per domain.

Alexis’s big bet was on Opus 4.7’s new ability to understand visual schematics; he says he knew it was working when he asked the model to trace a power path on a motherboard.

“I watched Wrench Board’s boardview light up step by step, arrows appearing, components getting pointed at, names surfacing. At that moment, I understood the idea was holding up," he says.

Wrench Board’s next phase is to build a community of electronics repairers interested in trying the app and experts able to enrich the tool with their field experience. His Claude credits will go toward RepairMind, those first users, and all the infrastructure currently in flight.

“This hackathon is proof that a self-taught person coming out of a repair shop can ship an ambitious system in five days,” says Alexis, who was applying for “survival jobs” when he entered. “Claude Code amplifies whoever has an idea and the endurance to execute on it, regardless of their starting point.”

**Advice to other builders:** Go deep in the brainstorm and push back on the model.

Alexis uses [Superpowers](https://claude.com/plugins/superpowers), a skills framework integrated into Claude that structures the brainstorm-then-plan steps, sometimes running brainstorms in parallel to make progress on different fronts. He starts in Claude Design, then hands off to Claude Code using the built-in button that shares the project directly, and pushes the model when it tells him no.

“During the hackathon, Claude told me several times that this or that wouldn't fit in the time available. In reality, I had plenty of time,” he says. “You have to know how to tell it, *I'm going to try anyway.*"

[*Wrench Board on GitHub*](https://github.com/Junkz3/wrench-board)

## Third place: [Maieutic](https://maieutic.dev/), Paula Vásquez-Henríquez

Paula Vásquez-Henríquez, who teaches computer science at Universidad del Desarrollo in Concepción, Chile, says over the past two years she is seeing more students pass tests without understanding their own code.

"Students now use AI to manufacture code, but they have no idea what the code does," she says. “They never learn to state a problem precisely, to draft a plan before coding, or to read their own code critically and notice where it drifted from what they intended. The autocomplete delivers working code before they've even finished forming the question, so the metacognitive loop, the thinking-about-your-thinking that actually creates a programmer, never closes. They graduate able to generate code but not reason about it.”

Paula, who is currently working on a PhD in Artificial Intelligence researching student–AI interaction patterns, entered the hackathon to solve this problem from both student and instructor perspectives.

Maieutic is an IDE designed to make students slow down at key moments. Students must describe in plain language what their program should do before writing any code; Claude asks targeted clarifying questions and keeps the editor locked until the spec is detailed enough that a competent programmer could implement it without guessing.

Students can then start writing Python but autocomplete is off; a chat panel answers reference questions directly but responds to reasoning questions with counter-questions rather than fixes, refusing to do the student's thinking for them.

The Intent-Diff Review, the core of the tool, has Claude compare the spec against the final code, classify each divergence as drift, revision, or bug, and then surface a neutral, non-accusatory question prompting the student to explain the issue themselves.

For instructors, a live dashboard shows one row per student with a one-sentence cognitive summary (e.g., "written the spec three times, still hasn't considered empty input").  Teachers can click on individual students to monitor their specific interactions with Claude, which also analyzes the full cohort to identify and surface any shared misunderstandings across the whole class so instructors can close that gap.

Since the hackathon ended, researchers at the University of Houston have reached out about co-authoring a paper, and Paula is putting her prize credits toward developing the tool further. She says hackathon week showed her that the gap between understanding a problem and shipping a tool for it has collapsed.

“I’m an educator in Concepcion, Chile, not Silicon Valley,” she says. “I shipped a working full-stack product in a week because the tools let me stay in the role I'm genuinely expert in while they handle the rest. The people closest to real problems can now build for them directly.”

**Advice to other builders:** Think before you build.

This project was Paula dogfooding her own philosophy: specify before you build. “Maieutic exists because students jump straight to code, and the only way I built it well was by refusing to do exactly that myself,” she says. She dedicated two days to pure thought work, creating the design spec and the technical spec before writing a single line of code.

“Those two days of spec felt slow at the time, there's real pressure in a hackathon to start shipping immediately, but they were what let the rest of the week move fast,” she says.

## Most Creative Use of Opus 4.7: Virtual Puppet Theater, Rene Hangstrup Møller

Intrigued with Opus 4.7’s spatial reasoning capabilities, full stack developer Rene Hangstrup Møller built Virtual Puppet Theater, a browser-based app that turns webcam video and voice into a dynamic interactive puppet show. A real-time animated puppet mirrors a user’s movements while a second AI-driven companion puppet banters with the user; spoken prompts can transform the scenery and spawn 3D props on the fly.

Rene used Claude across the full pipeline: concept discussion, planning, and code writing, while he handled direction, architecture, review, and decision-making. The app is based on Bun, Vite, and TypeScript, using MediaPipe hand tracking (running in WASM) and Three.js to render the puppet stage in 3D at 60 fps. A small WebSocket server connects to Claude Opus 4.7 via the Anthropic SDK to drive the AI puppet's dialogue and generate 3D props on the fly, while voice is handled by the Web Speech API for input and ElevenLabs for output (with browser speech synthesis as a fallback). Opus's spatial reasoning capabilities, refined through a screenshot-based feedback loop, handle the visual output.

There's no objective in Virtual Puppet Theater beyond open-ended play and Rene says she has no product plans for his winning project. For him, it was about learning and fun. "I tested it with my youngest son and he had a blast,” Rene says. “Seeing him interact with the puppet, describe scenes, and giggle at the responses was really the only user validation I needed.”

Virtual Puppet Theater’s source code is available on GitHub under MIT licensing, he adds, “if anyone wants to take it further.”

**Advice to other builders:** If you’re participating in a hackathon, plan time to create the demo video.

**‍**"It takes way longer than you think to produce a 3-minute video,” Rene says, noting that he went up against the hackathon deadline using Claude and Hyperframes to create and edit his Virtual Puppet Theater video. “Many people in the hackathon Discord warned about this, and they were right. Next time, I'd reserve that entire last day just for producing the demo."

[*Virtual Puppet Theater on Github*](https://github.com/rhmoller/virtual-puppet-theater)

## "Keep Thinking" Prize: [MaestrIA](https://www.youtube.com/watch?v=rkH4AjoTL5Q), Benjamin Torralbo

<!-- yt-inline:rkH4AjoTL5Q -->
[![Keep Thinking Prize Winner — Built with Opus 4.7 Hackathon | MaestrIA](https://img.youtube.com/vi/rkH4AjoTL5Q/hqdefault.jpg)](https://www.youtube.com/watch?v=rkH4AjoTL5Q)

<details>
<summary>자막: Keep Thinking Prize Winner — Built with Opus 4.7 Hackathon | MaestrIA (3:02)</summary>

[00:00]
In Chile, when something breaks in your
house, you either pay a handyman who
never shows up or you fix it badly.
A good craftsman knows what to look for.
A homeowner doesn't. I'm Benjamin,
apprentice carpenter, son of Juan
Rodrigo Toralbo, master mayor certified
by the Fundacion Iglesias Patrimoniales
de Chiloé.
30 years as a carpenter, eight of them
restoring UNESCO World Heritage
churches. I built the tool. The
knowledge is his.
We start by entering our location into
the analyzer.
I upload the photo of my wall. And now,
I can also describe my problem using the
microphone or by typing.
Then the analysis of the photo and given
context begins, taking into account the
location.
This isn't a loading spinner. It's Opus
4.7 reasoning live. It thinks like a
craftsman. Look first, diagnose second,
and here it locates the damage with real

[00:01]
coordinates on the photo, like an
architect's blueprint.
Four answers. What to fix, how much it
costs in your area, how long it takes,
and what happens if you don't fix it
soon. Also, based on the trades
required, you are recommended skilled
tradesmen near your home. And when you
pick a craftsman, a third agent writes
the WhatsApp message for you, in Chilean
Spanish with the full diagnosis
attached. You don't show up saying my
wall got wet. You show up with the
facts. Clients stop getting ripped off,
and skilled craftsmen who can't sell
themselves get work.
The specialists debate each other.
Carpenter versus mason, reasoning out
loud in Chilean Spanish.

[00:02]
A price without proof is worthless. So,
a second agent goes out to Sodimac and
Easy, looks up every line item, and
validates the budget against the real
market, live.
Before shipping this, I ran it past the
only filter that matters, my dad. 30
years as a carpenter, 25 as a site
foreman, and eight years restoring
Chiloé's UNESCO listed wooden churches.
12 photos, 12 diagnoses, match 81%.
Chile has over 280,000 informal
construction workers with no way to show
what they know. My dad restored churches
declared UNESCO World Heritage sites.
And yet, without a university degree,
he's invisible to the system. Maestro IA
codifies that expertise, so no one
overpays again, and the trade stops
being invisible.
Maestro IA. It sees, reasons, pinpoints,
debates, validates, connects. Built solo
with Opus 4.7.

</details>


Benjamin Torralbo grew up apprenticing alongside his father, Juan Rodrigo Torralbo, a certified *Maestro Mayor* carpenter in Chiloé, Chile. “My father has 30 years of craft, has restored UNESCO-listed churches, but is still invisible to the Chilean system, like hundreds of thousands of other tradespeople,” Benjamin says. “Meanwhile, people needing home repairs don't know what is wrong, what it costs, who to call, and whether they're being charged fairly.”

His [MaestrIA](https://maestriachile.cl/) hackathon project solves both sides as a web app that gives ordinary people master-level home repair diagnostics while giving skilled tradespeople a way to demonstrate expertise.

With MaestrIA, users photograph their problem, describe it in voice or text, and share their location. Claude streams its reasoning in real time with animated bounding boxes over the photos, then delivers structured diagnoses: what's broken, material, severity 1–5, project budget and time estimate. The agent then renders a map of nearby maestros filtered by trade while a second agent drafts a WhatsApp message to send.

MaestrIA’s technical heart is a JSON file, injected into every diagnosis, that contains 17 diagnostic rules, 7 native Chilote woods, 16 terms of local trade dialect, 19 benchmark prices, and 9 common mistakes of the craft all distilled from hours of interviews Benjamin did with his father. Without touching the system prompt, that single file lifted his eval seven points (74% to 81% against a human master's judgment) and is how MaestrIA can diagnose "rising damp on alerce wood siding" instead of generic "wood damage."

With no prior programming experience, Benjamin says his role was site foreman overseeing Claude’s technical execution. “Before writing any feature, I asked Claude Code to design the specs, the staged action plan, and the security model: input sanitization against prompt injection, rate limiting, origin validation, and Zod schemas as the single source of truth,” he says. “Then I reviewed each feature diff by diff.”

Benjamin wants MaestrIA to grow into new builds, hardware-store integration, formal budgets, contracts, reviews, and a certification system. Eventually, each trade will have its own Maestro Mayor encoded inside, including carpenters, architects, plumbers, electricians, and masons.

His prize credits go toward developing the app, digitizing his father's company as a live pilot, and his own technical growth. “Claude Code lets a 20-year-old from Chiloé with no programming experience build software that his own dad can use and that can help 280,000 more maestros like him in Chile,” he says. “And it opens the door for millions of people who've always had valuable ideas but no way to bring them to life."

**Advice to other builders:** Eval first, features later.

“The single most important thing I did was build an auditable 9-dimension eval against 12 real cases with ground truth recorded by my dad,” Benjamin says. “That eval, not my intuition, told me what was working and what wasn't. If I did another hackathon, the eval would be the first commit.”

## Best Use of Claude Managed Agents: [ARIA](https://www.youtube.com/watch?v=Hen24w2Jyz4&t=28s), Idriss Benguezzou & Adam Hnaien

<!-- yt-inline:Hen24w2Jyz4 -->
[![Aria: Built with Opus 4.7 Claude Code Hackathon](https://img.youtube.com/vi/Hen24w2Jyz4/hqdefault.jpg)](https://www.youtube.com/watch?v=Hen24w2Jyz4)

<details>
<summary>자막: Aria: Built with Opus 4.7 Claude Code Hackathon (3:00)</summary>

[00:00]
In every factory, every plant, every
water station in the world,
there's one person who knows.
He knows when a machine sounds
different. He knows it's going to break
2 days before it does. He just knows.
And when he retires, that knowledge
disappears forever.
Companies have tried to fix this for
years.
Setting it up costs half a million
dollars and takes 6 [music] months of
specialists. So, more than half of
industrial sites just [music] don't.
They wait for machines to break. We
built Aria to change that. [music] Five
agents, each with a single job, passing
the problem between them,
>> [music]
>> exactly like a real maintenance team
passes a ticket. Take a water bottling
factory. One line, [music] five
machines. Drop in the manual. Aria reads
it with Opus 4.7 vision, asks three
questions, [music] and then it's live.
Meanwhile, on the bottle capper, Aria
flags a potential breach.
But, look at what happens next.

[00:01]
Vibration is falling,
>> [music]
>> not rising. Aria reads the context,
checks the knowledge base, and
concludes, "No action required." It
didn't [music] just detect, it judged.
Now, let's see what happens when a real
breach hits. The operator sees an alert,
and that's where most systems [music]
stop. Alert sent, problem yours. Aria
doesn't. It fires the investigator
agent. And like a detective, [music] it
starts gathering clues with Opus 4.7
extended thinking. And here's the part
that cannot happen without managed
agents. The agent wrote Python, ran it
inside Anthropic's [music] cloud
sandbox, and computed the degradation
rate from the raw signal. That's not
guessing. That's a regression that
actually ran. And those exact [music]
numbers land in the work order. The
technician walks out with a detailed
sheet with a root cause [music] analysis
and step-by-step recommendations.
Another alert. This time on the bottle
[music] filler. And Aria remembers. Same

[00:02]
vibration pattern as January.
Tom Anderson closed that [music]
incident. Aria pulls his fix, matches
the part number, and tells the operator
exactly what worked 3 months ago.
It doesn't [music] start from zero. It
compounds.
Behind the scenes, 17 tools are
available to the agents. Logbook
entries,
shift notes from the operators,
signal trends, computed KPI, and past
[music] failures, all gathered and
scored in a knowledge base behind each
machine, built from the manual and the
operator's own experience. Everything
cross-referenced with Claude Opus
[music] 4.7 extended thinking and 1
million tokens of context. Five [music]
agents share 17 tools through MCP. The
investigator runs as a managed agent
with Claude Opus 4.7. [music]
From shop floor knowledge to diagnosis,
so the one who knows is never the last.

</details>


Most factories have that one veteran technician who can tell when a machine is about to break, just by the sound it makes. The Best Use of Claude Managed Agents prize-winning project, ARIA (Adaptive Runtime Intelligence) turns an experienced maintenance engineer’s instincts into an affordable, fast-to-set-up AI system that continuously watches factory machines and generates custom diagnostics and repair plans the moment trouble appears.

With ARIA, a maintenance engineer uploads a manufacturer's PDF, answers four plain-language calibration questions, and within 15 minutes the plant is profiled. From there, five agents watch live signals. If an agent detects a failure or predicts one is imminent, it produces a work order analyzing component, failure mode, urgency, parts, and intervention window

The project’s builders, both of whom have on-the-floor industrial experience, met in the hackathon’s teammate-finding Discord channel. Idriss Benguezzou, a French industrial-software engineer with a Master's in data/AI, had been mapping out the idea and most of its architecture for a while. Adam Hnaien, a self-taught engineering student experienced with Claude Code and multi-agent workflows, immediately recognized ARIA as a valuable solution for industrial maintenance.

Idriss and Adam spent all of the hackathon’s second day in planning mode with a GitHub Project board, scoping every milestone, issue, and acceptance criterion before writing the first line of code. “We wanted to go in at 200% from M2 onward,” Adam says. “One day of planning let us spend the rest of the week executing, not improvising.”

Both estimate that Claude Code wrote ~80% of the raw lines while they made domain logic and design decisions by hand. Idriss handled threshold evaluation, KB schema, and anomaly detection because, he says, “you can't prompt your way to knowing what a maintenance technician actually looks at." Adam took on UX, visual language, and ARIA’s constellation concept because, he says, “you can't prompt your way to taste.”

Managed Agents handled agent infrastructure. “Without Claude Managed Agents, we'd have spent the week building infrastructure that Anthropic already hosts: a sandboxed Python environment, secure execution, session persistence, MCP dispatching,” Adam says. “Instead, we spent that week building the product around that infrastructure. That's the difference between shipping ARIA in five days and shipping ARIA in five weeks.”

After the hackathon’s results were announced, companies working on exactly this problem reached out about the project. Idriss will fold ARIA's agent architecture, KB schema, and signal pipeline into his own industrial IoT platform; his credits will go toward more building and experimentation. As for Adam, his plan is to continue exploring opportunities in industrial agentic AI and use the API credits to continue building and experimenting.

**Advice to other builders:** Let Claude audit**.** Ask Claude to find if there’s anything wrong with what you've already built before building the next thing, says Idriss. “That loop is underrated.”

[*ARIA on GitHub*](https://github.com/zestones/Aria)

[*Learn*](http://claude.com/community) *about our Claude Community programs, including meetups, hackathons, and more.*

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225588ad176f7c4aafd_abc884c723daea810d2e986455358281a2f94102-1000x1000.svg)

Jun 24, 2026

### Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

Claude Code

[Agent identity in Claude Tag: a new access model for autonomous, team-wide AI](#)Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

[Agent identity in Claude Tag: a new access model for autonomous, team-wide AI](/blog/agent-identity-access-model)Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f7912d5b05a5c7ed8ae86_Object-CodeChatCode.svg)

Jun 3, 2026

### Running an AI-native engineering org

Claude Code

[Running an AI-native engineering org](#)Running an AI-native engineering org

[Running an AI-native engineering org](/blog/running-an-ai-native-engineering-org)Running an AI-native engineering org

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

May 12, 2026

### How Anthropic's cybersecurity team built a threat detection platform with Claude Code

Claude Code

[How Anthropic's cybersecurity team built a threat detection platform with Claude Code](#)How Anthropic's cybersecurity team built a threat detection platform with Claude Code

[How Anthropic's cybersecurity team built a threat detection platform with Claude Code](/blog/how-anthropic-uses-claude-cybersecurity)How Anthropic's cybersecurity team built a threat detection platform with Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2222403b092e0358b0e_cd4fd51deacd067d4e30aee4f4b149f6cba1b97b-1000x1000.svg)

Apr 20, 2026

### Meet the winners of our Built with Opus 4.6 Claude Code hackathon

Claude Code

[Meet the winners of our Built with Opus 4.6 Claude Code hackathon](#) Meet the winners of our Built with Opus 4.6 Claude Code hackathon

[Meet the winners of our Built with Opus 4.6 Claude Code hackathon](/blog/meet-the-winners-of-our-built-with-opus-4-6-claude-code-hackathon) Meet the winners of our Built with Opus 4.6 Claude Code hackathon

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
