<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/project-setup -->

Lesson 49 of 67 · Building with the Claude APIProject setup

We're going to build a CLI-based chatbot to better understand how MCP clients and servers work together. This hands-on project will give you practical experience with both sides of the MCP architecture.

When the setup is done, you should be able to do two things: say what the client does and what the server does, and tell whether a reply came through a tool or straight from the model.

## What We're Building

Our chatbot will allow users to interact with a collection of documents through a command-line interface. The system consists of two main components:

* An MCP client that handles user interactions
* A custom MCP server that manages document operations

![](https://academy.claude.com/assets/media/d0ad72fc54e43e107b684b528bf7e47d626f4ae14b3be7462942e5c75f9772d8.jpg)

The server will provide two essential tools: one for reading document contents and another for updating them. All documents will be stored in memory for simplicity - no database required.

## Important Architecture Note

In real-world projects, you typically implement either an MCP client or an MCP server, not both. You might create:

* An MCP server to expose your service to other developers
* An MCP client to connect to existing MCP servers

![](https://academy.claude.com/assets/media/7bfe22eedd2e29cbc789c11373941d64f342dd94001fcfa7a60b980315d6bd58.jpg)

We're building both components in this project purely for educational purposes - to understand how they communicate and work together.

## Project Setup

Download the `cli_project.zip` file attached to this lesson and extract it to your preferred development directory. Open your code editor in the project folder.

The project includes a comprehensive README file with setup instructions. Follow these steps:

1. Add your Anthropic API key to the `.env` file
2. Install dependencies using either UV (recommended) or pip
3. Run the starter application to verify everything works

## Running the Application

Navigate to your project directory in the terminal. You'll see the main project files including `main.py`, `mcp_client.py`, and `mcp_server.py`.

To start the application, use one of these commands:

bash

```
# If using UV (recommended)
uv run main.py

# If using standard Python
python main.py
```

When the application starts successfully, you'll see a chat prompt.

**Check the baseline yourself.** Type a question you can verify on sight, like "what's 1+1?". Don't settle for a reply appearing: confirm the answer is actually 2. A correct reply proves your API key, dependencies, and chat loop all work.

Then type a second question, something like "what do the documents say?". Whatever comes back, it can't have come from the document tools, because you haven't built them yet. The reply is the model answering on its own. Notice which component will own that work once it exists: the server manages document operations, and the client handles your side of the conversation.

The habit behind this check: match how carefully you verify to the cost of being wrong. A broken setup here costs you every later lesson built on top of it; checking costs two questions.

## A check worth keeping

The behavior to carry beyond this project: every time you add a new layer to an API project, whether a tool, a data source, or an MCP server, ask the running system one question whose answer you already know before you build the next layer. A baseline you have verified is the only baseline you can debug against.

With the basic setup complete, we're ready to start implementing MCP features and exploring how clients and servers communicate through the Model Context Protocol.
