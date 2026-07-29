<!-- https://anthropic.skilljar.com/claude-in-amazon-bedrock/276809 -->

# Claude Code setup

<!-- jwplayer-srt: https://cdn.jwplayer.com/tracks/g98YWoZ7.srt -->

<details>
<summary>자막: Claude Code setup</summary>

Let's take a look at Claude Code. We'll do some setup, learn how it works, and see some advanced use cases. Claude Code is a terminal-based coding assistant. This is a program running in your terminal that can help with a wide variety of code-related tasks. To help you with coding projects, Claude Code has access to many different tools, so it has many basic tools like the ability to search, read, and edit files. But it also has many advanced tools, like web fetching and terminal access. Finally, Claude Code can act as an MCP client. And you know what that means? It means it can consume tools that are provided by MCP servers, so we can easily expand the capabilities of Claude Code by adding in some additional MCP servers. Let's now go through a little bit of setup and install Claude Code on your machine. Setup is easy. We're going to first install a copy of Node.js. You might already have Node installed on your machine, and to figure out whether or not you do, open up your terminal and execute the command npm help. If you see a result come back, that means you probably already have Node installed. Once you have Node installed, you'll do a npm install command that will install Claude Code itself. Finally, by default, Claude Code tries to access Anthropic's API. So we need to update a little bit of configuration just to get Claude Code to make use of Bedrock. This takes the form of setting three different environment variables, which I've listed on here at the bottom of the screen. One last thing to just keep in mind, you also need to set up your AWS credentials, or alternatively, set the AWS access key and secret key. Now, a full setup guide can be found at the official Anthropic documentation at docs.anthropic.com. Now, I'm going to let you go through this setup process on your own, again, just these three steps right here. As soon as you are done, we're going to walk through a little project together and see what Claude Code can really do for us.

</details>
