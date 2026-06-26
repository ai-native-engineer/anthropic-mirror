<!-- source: https://www.anthropic.com/news/3-5-models-and-computer-use -->

# Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku

Oct 22, 2024

![An illustration of Claude navigating a computer cursor](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fdb3165778de297272875d36a822f671d8009aaec-2880x1620.png&w=3840&q=75)

*Update (12/03/2024): We have revised the pricing for Claude 3.5 Haiku. The model is now priced at $0.80 MTok input / $4 MTok output.*

Today, we’re announcing an **upgraded Claude 3.5 Sonnet**, and a new model, **Claude 3.5 Haiku**. The upgraded Claude 3.5 Sonnet delivers across-the-board improvements over its predecessor, with particularly significant gains in coding—an area where it already led the field. Claude 3.5 Haiku matches the performance of Claude 3 Opus, our prior largest model, on many evaluations at a similar speed to the previous generation of Haiku.

We’re also introducing a groundbreaking new capability in public beta: **computer use**. Available [today on the API](https://docs.anthropic.com/en/docs/build-with-claude/computer-use), developers can direct Claude to use computers the way people do—by looking at a screen, moving a cursor, clicking buttons, and typing text. Claude 3.5 Sonnet is the first frontier AI model to offer computer use in public beta. At this stage, it is still [experimental](https://www.anthropic.com/news/developing-computer-use)—at times cumbersome and error-prone. We're releasing computer use early for feedback from developers, and expect the capability to improve rapidly over time.

Asana, Canva, Cognition, DoorDash, Replit, and The Browser Company have already begun to explore these possibilities, carrying out tasks that require dozens, and sometimes even hundreds, of steps to complete. For example, Replit is using Claude 3.5 Sonnet's capabilities with computer use and UI navigation to develop a key feature that evaluates apps as they’re being built for their Replit Agent product.

The upgraded Claude 3.5 Sonnet is now available for all users. Starting today, developers can build with the computer use beta on the Anthropic API, Amazon Bedrock, and Google Cloud’s Vertex AI. The new Claude 3.5 Haiku will be released later this month.

![](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F0eb9a1b7d5db74a6d21500e9f188c83beef3842e-2601x1932.png&w=3840&q=75)

## Claude 3.5 Sonnet: Industry-leading software engineering skills

The updated [Claude 3.5 Sonnet](https://www.anthropic.com/claude/sonnet) shows wide-ranging improvements on industry benchmarks, with particularly strong gains in agentic coding and tool use tasks. On coding, it improves performance on [SWE-bench Verified](https://www.swebench.com/) from 33.4% to 49.0%, scoring higher than all publicly available models—including reasoning models like OpenAI o1-preview and specialized systems designed for agentic coding. It also improves performance on [TAU-bench](https://github.com/sierra-research/tau-bench), an agentic tool use task, from 62.6% to 69.2% in the retail domain, and from 36.0% to 46.0% in the more challenging airline domain. The new Claude 3.5 Sonnet offers these advancements at the same price and speed as its predecessor.

Early customer feedback suggests the upgraded Claude 3.5 Sonnet represents a significant leap for AI-powered coding. GitLab, which tested the model for DevSecOps tasks, found it delivered stronger reasoning (up to 10% across use cases) with no added latency, making it an ideal choice to power multi-step software development processes. Cognition uses the new Claude 3.5 Sonnet for autonomous AI evaluations, and experienced substantial improvements in coding, planning, and problem-solving compared to the previous version. The Browser Company, in using the model for automating web-based workflows, noted Claude 3.5 Sonnet outperformed every model they’ve tested before.

As part of our continued effort to partner with external experts, joint pre-deployment testing of the new Claude 3.5 Sonnet model was conducted by the US AI Safety Institute (US AISI) and the UK Safety Institute (UK AISI).

We also evaluated the upgraded Claude 3.5 Sonnet for catastrophic risks and found that the ASL-2 Standard, as outlined in our [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy), remains appropriate for this model.

## Claude 3.5 Haiku: State-of-the-art meets affordability and speed

[Claude 3.5 Haiku](https://www.anthropic.com/claude/haiku) is the next generation of our fastest model. For a similar speed to Claude 3 Haiku, Claude 3.5 Haiku improves across every skill set and surpasses even Claude 3 Opus, the largest model in our previous generation, on many intelligence benchmarks. Claude 3.5 Haiku is particularly strong on coding tasks. For example, it scores 40.6% on SWE-bench Verified, outperforming many agents using publicly available state-of-the-art models—including the original Claude 3.5 Sonnet and GPT-4o.

With low latency, improved instruction following, and more accurate tool use, Claude 3.5 Haiku is well suited for user-facing products, specialized sub-agent tasks, and generating personalized experiences from huge volumes of data—like purchase history, pricing, or inventory records.

Claude 3.5 Haiku will be made available later this month across our first-party API, Amazon Bedrock, and Google Cloud’s Vertex AI—initially as a text-only model and with image input to follow.

## Teaching Claude to navigate computers, responsibly

With computer use, we're trying something fundamentally new. Instead of making specific tools to help Claude complete individual tasks, we're teaching it *general* computer skills—allowing it to use a wide range of standard tools and software programs designed for people. Developers can use this nascent capability to automate repetitive processes, [build and test software](https://www.youtube.com/watch?v=vH2f7cjXjKI), and [conduct open-ended tasks like research](https://youtu.be/jqx18KgIzAE).

<!-- yt-inline:vH2f7cjXjKI -->
[![Claude | Computer use for coding](https://img.youtube.com/vi/vH2f7cjXjKI/hqdefault.jpg)](https://www.youtube.com/watch?v=vH2f7cjXjKI)

<details>
<summary>📺 자막: Claude | Computer use for coding (3:03)</summary>

[00:00]
I'm Alex, I lead developer
relations at Anthropic,
and today I'm gonna be
showing you a coding task
with computer use.
So we're gonna be showing Claude
doing a website coding task
by actually controlling my laptop.
But before we start coding,
we need an actual website for
Claude to make changes to.
So, let's ask Claude to
navigate to claude.ai
within my Chrome browser,
and ask Claude within claude.ai
to create a fun, 90s themed
personal homepage for itself.
Claude opens Chrome,
searches for claude.ai,
and then types in a prompt
asking the other Claude
to create a personal homepage for itself.
Claude.ai returns some code,

[00:01]
and that gets nicely rendered
in an Artifact on the right-hand side.
That looks great,
but I want to make a few
changes to the website locally
on my own computer.
Let's ask Claude to download the file
and then open it up in VS Code.
Claude clicks the save to file button,
opens up VS Code,
and then finds the file
within my Downloads folder
and opens it up.
Perfect.
Now that the file's up and running,
let's ask Claude to start up a server
so that we can actually view
the file within our browser.
Claude opens up the VS Code terminal
and tries to start a server.
But it hits an error,
we don't actually have Python
installed on our machine.
But that's all right,
because Claude realizes this
by looking at the terminal output,

[00:02]
and then tries again with Python 3,
which we do have installed on our machine.
That works, so now the
server's up and running.
Now that we have the local server started,
we can go manually take
a look at the website
within the browser,
and it looks pretty good,
but I notice that
there's actually an error
in the terminal output,
and we also have this missing
file icon at the top here.
Let's ask Claude to identify this error
and then fix it within the file.
Claude visually reads the terminal output
and opens up the find and
replace tool in VS Code
to find the line that's
throwing the actual error.
In this case,
we just ask Claude to get
rid of the error entirely,
so it will just delete the whole line.
Then, Claude will save the file
and automatically rerun the website.
So now that the error is gone,
let's go take a final look at our website,
and we can see that the
file icon has disappeared
and the error is gone as well.
Perfect.
So that's coding with
computer use and Claude.
This took a few prompts now,
but we can imagine in the future
that Claude will be able to
do tasks like this end to end.

</details>


<!-- yt-inline:jqx18KgIzAE -->
[![Claude | Computer use for orchestrating tasks](https://img.youtube.com/vi/jqx18KgIzAE/hqdefault.jpg)](https://www.youtube.com/watch?v=jqx18KgIzAE)

<details>
<summary>📺 자막: Claude | Computer use for orchestrating tasks (2:04)</summary>

[00:00]
I'm Pujaa and I'm a
researcher at Anthropic.
I'm going to show you a simple example
of computer use today.
My friend is coming to
San Francisco next week
and I want to take him to
do some touristy stuff.
I think doing a sunrise hike
with a view of the Golden
Gate Bridge never gets old.
So I'll ask Claude to figure
out some logistics for us.
I'll ask Claude to find a
good place to see the sunrise
to help me figure out timing logistics,
and help drop a calendar invite
so I remember when I have to leave.
It's opening Chrome, going
to Google, searching...
...and it looks like it's found something.
Great. So how far away is
the location from my place?
It's opening Maps.
Searching for the distance between my area
and the hiking location.

[00:01]
Cool, so now it looks
like Claude is searching
for the sunrise time tomorrow.
And is now dropping it into my calendar.
And populating it with some details.
And great, it looks like Claude did it.
This is a simple example,
but we're sharing computer use early
to learn from what people build.

</details>


To make these general skills possible, we've built an API that allows Claude to perceive and interact with computer interfaces. Developers can integrate this API to enable Claude to translate instructions (e.g., “use data from my computer and online to fill out this form”) into computer commands (e.g. check a spreadsheet; move the cursor to open a web browser; navigate to the relevant web pages; fill out a form with the data from those pages; and so on). On [OSWorld](https://os-world.github.io/), which evaluates AI models' ability to use computers like people do, Claude 3.5 Sonnet scored 14.9% in the screenshot-only category—notably better than the next-best AI system's score of 7.8%. When afforded more steps to complete the task, Claude scored 22.0%.

While we expect this capability to improve rapidly in the coming months, Claude's current ability to use computers is imperfect. Some actions that people perform effortlessly—scrolling, dragging, zooming—currently present challenges for Claude and we encourage developers to begin exploration with low-risk tasks. Because computer use may provide a new vector for more familiar threats such as spam, misinformation, or fraud, we're taking a proactive approach to promote its safe deployment. We've developed new classifiers that can identify when computer use is being used and whether harm is occurring. You can read more about the research process behind this new skill, along with further discussion of safety measures, in our post on [developing computer use](http://anthropic.com/news/developing-computer-use).

## Looking ahead

Learning from the initial deployments of this technology, which is still in its earliest stages, will help us better understand both the potential and the implications of increasingly capable AI systems.

We’re excited for you to explore [our new models](https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf) and the public beta of computer use—and welcome you to [share your feedback](mailto:feedback@anthropic.com) with us. We believe these developments will open up new possibilities for how you work with Claude, and we look forward to seeing what you'll create.
