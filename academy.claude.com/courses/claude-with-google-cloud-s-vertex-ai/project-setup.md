<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/project-setup -->

Lesson 51 of 66 · Claude with Google Cloud's Vertex AIProject setup

We're going to build a CLI-based chatbot that demonstrates how MCP clients and servers work together. This hands-on project will give you practical experience with both sides of the MCP architecture.

## What We're Building

Our chatbot will allow users to interact with a collection of documents through natural language. The system consists of two main components:

* An MCP client that handles user interactions and communicates with Claude
* An MCP server that provides tools for reading and updating documents

![](https://academy.claude.com/assets/media/64226d5d22dbeb8af1c41085ed118e4c1f7319166b5ab2f17945e8135bece6b0.png)

The server will expose two tools to Claude:

* Tool to read a document's contents
* Tool to update a document's contents

All documents are stored in memory for simplicity - they include files like document.pdf, spreadsheet.xlsx, report.txt, and spec.md.

## Important Architecture Note

In real-world projects, you typically implement either an MCP client or an MCP server, not both. You might build:

* Just an MCP server to expose your service's capabilities to AI models
* Just an MCP client to connect to existing MCP servers built by other developers

![](https://academy.claude.com/assets/media/255c982da24359c7bf040bce9332b011a99def1dff920e38b1351a878881c9d4.png)

We're building both components in this project purely for educational purposes - to understand how they communicate and work together.

## Project Setup

Download the CLI\_project.zip file attached to this video and extract it to your preferred development directory. Open your code editor in the project folder.

## Configuration

The project includes a README.md file with detailed setup instructions. You'll need to:

1. Add your Anthropic API key to the .env file
2. Install dependencies using either UV (recommended) or pip

![](https://academy.claude.com/assets/media/81b4c8f4398237590110db4cc2dc362374c422a62fc75ae99096a4d76d6dc00c.png)

The .env file should contain:

bash

```
ANTHROPIC_API_KEY="your-api-key-here"
```

## Running the Project

Once setup is complete, navigate to your project directory in the terminal and run:

bash

```
# If using UV (recommended)
uv run main.py

# If using standard Python
python main.py
```

You should see a chat prompt appear. Test it by asking a simple question like "what's 1+1?" to verify everything is working correctly.

The starter project already includes basic chat functionality with Claude. In the following videos, we'll add MCP server capabilities and document management features to create a fully functional document-aware chatbot.
