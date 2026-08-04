<!-- source: https://claude.com/blog/tool-use-ga -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22b8840b2f6f9a40fe0_8925ac952fa2cb8eb5e845b2e44f3e71b33fd695-1000x1000.svg)

# Claude can now use tools

Claude now connects with external tools and APIs to perform tasks, manipulate data, and deliver more accurate responses.

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  Claude Platform
* Date

  May 30, 2024
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/tool-use-ga

Tool use, which enables Claude to interact with external tools and APIs, is now generally available across the entire Claude 3 model family on the Anthropic Messages API, Amazon Bedrock, and Google Cloud's Vertex AI. With tool use, Claude can perform tasks, manipulate data, and provide more dynamic—and accurate—responses.

## Tool use

Define a toolset for Claude and specify your request in natural language. Claude will then select the appropriate tool to fulfill the task and, when appropriate, execute the corresponding action:

* **Extract structured data from unstructured text**: Pull names, dates, and amounts from invoices to reduce manual data entry.
* **Convert natural language requests into structured API calls**: Enable teams to self-serve common actions (e.g., "cancel subscription") with simple commands.
* **Answer questions by searching databases or using web APIs**: Provide instant, accurate responses to customer inquiries in support chatbots.
* **Automate simple tasks through software APIs**: Save time and minimize errors in data entry or file management.
* **Orchestrate multiple fast Claude subagents for granular tasks**: Automatically find the optimal meeting time based on attendee availability.

## Improved developer experience

To make it easier to leverage the intelligence of the Claude 3 models with tools, we’ve also built in features that help developers further customize the end-user experience.

* **Tool use with streaming reduces wait times to create more engaging interactions**: Streaming enables real-time responses in applications like customer support chatbots for smoother, more natural conversations.
* **Forced tool use allows developers to instruct Claude on tool selection**: Developers can specify which tools Claude should use or leave the choice with Claude, helping create more targeted and efficient applications.
* **Tools also work with images**:Claude can incorporate image inputs in live applications.

During our beta many developers used Opus to build sophisticated user-facing assistants. To further enhance this experience, Opus will now include <thinking> tags in its outputs, clarifying Claude’s reasoning and simplifying the debugging process for developers. Our Claude 3 models are currently unable to support parallel tool calls.

## Customer spotlight: StudyFetch

AI-native learning platform [StudyFetch](https://www.claude.com/customers/studyfetch) uses Claude's tool use capabilities to power its personalized AI tutor, Spark.E. By integrating tools to track student progress, navigate course materials and lectures, and create interactive user interfaces, StudyFetch has created a more engaging educational environment for students globally.

"Claude with tool use is accurate and cost-effective, and now powers our live voice-enabled AI tutoring sessions. Within just a few days, we integrated tools into our platform,” said Ryan Trattner, CTO and Co-Founder at StudyFetch. “As a result, our AI tutor, Spark.E, acts agentically—displaying interactive UIs, tracking student progress in context, and navigating through lectures and materials. Since implementing Claude with tool use, we've observed a 42% increase in positive human feedback."

## Customer spotlight: Intuned

Intuned, the browser automation platform, uses Claude to power data extraction within their cloud platform. With AI-powered data extraction, Intuned is able to drastically improve the developer experience in building and executing more reliable browser automations.

"Claude 3 Haiku with tool use has been a game changer for us. After accessing the model and running our benchmarks on it, we realized the quality, speed, and price combination is unmatched,” said Faisal Ilaiwi, Co-Founder at Intuned. “Haiku is helping us scale our customers' data extraction tasks to a completely new level."

## Customer spotlight: Hebbia

[Hebbia](https://www.claude.com/customers/hebbia) is building the AI knowledge worker for leading financial and legal services firms. They use Claude 3 Haiku to help power several complex, multi-step customer workflows.

"We leverage Claude 3 Haiku for generating live suggestions, automating prompt writing, and extracting key metadata from long documents,” shared Divya Mehta, Product Manager at Hebbia. “Claude 3 Haiku's tool use feature has unlocked capabilities and speed for our platform to generate reliable suggestions and prompts in real-time."

## Get started

You can get started with tool use today on the Anthropic Messages API, Amazon Bedrock, and Google Cloud's Vertex AI. To learn more, explore our [documentation](https://docs.anthropic.com/en/docs/tool-use), [tool use tutorial](https://github.com/anthropics/courses/tree/master/tool_use), and [Anthropic Cookbooks on tool use](https://platform.claude.com/cookbook/tool-use-calculator-tool).

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229b7f170bab528846d_0df729ce74e4c9dd62c3342c9549ce6c7cef1202-1000x1000.svg)

Jul 28, 2026

### Bringing MCP 2026-07-28 to Claude

Product announcements

[Bringing MCP 2026-07-28 to Claude](#)Bringing MCP 2026-07-28 to Claude

[Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude)Bringing MCP 2026-07-28 to Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22349f86cd1968deab7_f06ca06f9d08ca4a85f26357eb896c3730274507-1000x1000.svg)

Jul 2, 2026

### Giving admins more visibility and control over Claude spend

Product announcements

[Giving admins more visibility and control over Claude spend](#)Giving admins more visibility and control over Claude spend

[Giving admins more visibility and control over Claude spend](https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend)Giving admins more visibility and control over Claude spend

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d23008bbc20c0ffaeb6f_43abe7e54b56a891e74a8542944dfbd33f07f49c-1000x1000.svg)

Jun 18, 2026

### Centrally manage authorization for MCP connectors

Enterprise AI

[Centrally manage authorization for MCP connectors](#) Centrally manage authorization for MCP connectors

[Centrally manage authorization for MCP connectors](https://claude.com/blog/enterprise-managed-auth) Centrally manage authorization for MCP connectors

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

Sep 10, 2024

### Claude for Enterprise

Product announcements

[Claude for Enterprise](#)Claude for Enterprise

[Claude for Enterprise](https://claude.com/blog/claude-for-enterprise)Claude for Enterprise

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Claude Platform

Business

Agents
