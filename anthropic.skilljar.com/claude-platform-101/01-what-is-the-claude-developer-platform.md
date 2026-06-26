<!-- https://anthropic.skilljar.com/claude-platform-101/486250 -->
<!-- youtube: RfeC02NmLqs -->

<!-- vid-ref:RfeC02NmLqs -->
[![Watch on YouTube](https://img.youtube.com/vi/RfeC02NmLqs/hqdefault.jpg)](https://www.youtube.com/watch?v=RfeC02NmLqs)


# What is the Claude Developer Platform?

The Claude platform is Anthropic's infrastructure for building with Claude programmatically. It's a REST API, SDKs for different programming languages, command line interfaces, and a console where you manage keys, monitor usage, deploy managed agents, and test prompts. It's where developers send structured requests, get structured responses, and it control every detail. Which model, how many tokens, what tools Claude can use, and what system instructions it follows. Picture the Claude platform as three layers. First, we have primitives, which is the API building blocks that is tuned into Claude. The messages API, the tool use, profiles, web search, code execution, MCP servers, skills, the pieces you actually call. Then you have the infrastructure, what you need to build and scale agentic systems past just a prototype. Manage agents, retries, queues, observability, the plumbing that keeps things running when one Claude call becomes a thousand. And then you have controls for running those systems in production, like dashboards, evals, the dials your team uses once it's live. The shorthand is build with primitives, scale on infrastructure, and then run with control. So, I manage a basic help desk app. I've been tasked with having to draft a reply based on the contents of a ticket, our tone and guidelines. So, let's wire up this button. Now, this is a perfect use case for the messages API. I define a client. I retrieve the ticket that this chat refers to, and do a messages.create call. First, we define the model we want to use. I'm using Haiku since this is a simple drafting task. Max tokens caps how long Claude's response can be. The system prompt is where we define the role that Claude has. I have already put the relevant tone and information here. Then the messages key takes an array of objects. For this use case, the user role lets Claude know that this is a user input. Here we put the ticket content in there. And then we retrieve the response and return it to the button to render.
>> [music]
>> Awesome.
>> [music]
>> You're not building a chatbot from
scratch. You're adding Claude into a product that already exists, and the API is how you wire it in. The Claude platform is your API level access to Claude's models, tools, and infrastructure. It's how you go from ask Claude a question to Claude is part of my product. And when your product needs agents, the platform doesn't just give you the model. With managed agents, it runs them for you.
