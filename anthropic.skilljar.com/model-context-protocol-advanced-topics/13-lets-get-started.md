<!-- https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296349 -->
<!-- jwplayer-srt: https://content.jwplatform.com/tracks/3kN644eX.srt -->

# Let's get started!

<details>
<summary>자막: Let's get started!</summary>

Hello and welcome. My name is Stephen Grider and I'm a member of Technical Staff at Anthropic. In this course, you're going to learn a wide variety of advanced topics around model context protocol. Before we dive in, I want to give you a quick overview of some of the different topics we will be discussing. We will begin with sampling, which allows an MCP server to request a client to call a language model like Claude to generate some amount of text. We'll then take a look at providing better feedback to clients accessing your MCP server by using logging and progress notifications. After that, we'll spend some time discussing routes, which allow you to point an MCP server to specific files or folders that it should access. From there, we'll take a deeper look at the MCP spec itself to really help you understand the technical side of server client communication by looking at the specific message format that MCP uses. We will then immediately apply that knowledge to see how the standard IO transport works and then close out with a very deep dive on remotely hosted servers using the streamable HTTP transport. There is a lot of content here, so to make sure we can get through all these different topics, there are a couple of things that you need to know ahead of time. First, we will be looking at a lot of Python code. Now you don't need to be a Python expert, but you should at least be able to read Python. Second, you should already have a basic understanding of MCP, including clients, servers, and tools. So with that, let's dive into our first technical topic.

</details>
