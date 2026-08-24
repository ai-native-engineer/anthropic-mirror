<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/project-setup -->

Lesson 50 of 65 · Claude with Amazon BedrockProject setup

We're going to build our own CLI-based chatbot to better understand how MCP clients and servers work together. This hands-on project will give you practical experience with both sides of the MCP architecture.

## What We're Building

Our chatbot will be a command-line interface that allows users to chat with a set of documents. Here's what the system will include:

* A CLI-based chatbot interface
* Document reading and editing capabilities for Claude
* Document "mention" functionality using `@doc_name` syntax
* Command execution with `/command_name` syntax
* A collection of fake documents stored in memory

![](https://academy.claude.com/assets/media/d46a61c16751d7e35792bfa377ae844576ea6143bc2a3c771498df206e2c3de5.png)

## System Architecture

The project consists of three main components working together:

* **Our MCP Client** - Handles user interaction and chat interface
* **Our MCP Server** - Provides tools for document operations
* **Document Storage** - In-memory collection of various file types

![](https://academy.claude.com/assets/media/1107d9787fc784464d22b16d654648dbe1d667fccc7aca95d7c85583c84285c8.png)

The MCP server will implement two core tools:

* Tool to read document contents
* Tool to update document contents

All documents (PDFs, spreadsheets, text files, markdown files) will be stored in memory rather than on disk, keeping the project simple and focused on MCP concepts.

## Important Architecture Note

In real-world projects, you typically implement either an MCP client or an MCP server - not both. You might:

* Build an MCP server to distribute a service to other developers
* Build an MCP client that connects to existing third-party MCP servers

![](https://academy.claude.com/assets/media/6909714683204404437ee6148c256e16adab43c03cc7f0bde89420a840cc1e7d.png)

Our project implements both components in a single codebase purely for educational purposes, so you can see how clients and servers interact with each other.
