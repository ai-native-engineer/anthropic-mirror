<!-- source: https://academy.claude.com/courses/model-context-protocol-advanced-topics -->

[Courses](https://academy.claude.com/courses)

# Model Context Protocol: Advanced Topics

Go beyond MCP basics: sampling, notifications, and roots, with interactive walkthroughs of each protocol flow.

11 lessons1.5 hr1 quizCompletion badge

[Start course](https://academy.claude.com/courses/model-context-protocol-advanced-topics/sampling)[Sign in to save progress](https://academy.claude.com/login?returnTo=https%3A%2F%2Facademy.claude.com%2Fcourses%2Fmodel-context-protocol-advanced-topics)

![](https://academy.claude.com/assets/v1/thumbnail.light-oippap07.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-pe7rwjtj.png)

11 lessons · 1 quizModel Context Protocol: Advanced Topics

What you’ll learnBy the end of this course, you’ll be able to

* Understand how MCP servers can request language model calls through connected clients via sampling, shifting AI costs and complexity from server to client
* Implement real-time feedback using context objects, logging callbacks, and progress reporting for long-running operations
* Use roots to grant MCP servers access to specific directories with security boundaries and user-friendly file discovery
* Distinguish between request-result pairs and notification messages in the MCP message specification, and understand bidirectional communication patterns
* Understand how MCP clients and servers communicate over standard input/output streams, including the required initialization handshake sequence
* Explain how Server-Sent Events (SSE) enable server-to-client communication over HTTP, including session management and dual-connection architectures
* Recognize how configuration flags affect functionality, particularly server-initiated requests and streaming capabilities
* Decide when to use stateless HTTP for horizontal scaling with load balancers, weighing the trade-offs between stateful and stateless server configurations
* Choose appropriate transport methods based on deployment requirements, functionality needs, and scaling constraints

Who it’s for

Engineers building production MCP servers who need to understand the protocol's advanced capabilities

Before you start

* Basic understanding of MCP servers and clients
* Familiarity with async programming patterns

This course covers the technical implementation of MCP servers and clients, from basic message passing to production deployment strategies. You'll learn how MCP enables language models like Claude to interact with external tools and data sources through standardized protocols, transports, and message formats.

## Inside the course

### Core MCP features

6 lessons

Learn the advanced features that make MCP servers more powerful. Covers sampling to offload AI costs to clients, implementing progress notifications for better UX, and using roots to safely handle file access.

![](https://academy.claude.com/assets/media/5bdcc9418bd07c5514ede460169762602818f352a497bb5389d5e08a1907e376.webp)![](https://academy.claude.com/assets/media/f9b2a456fc8a67e74c926b9657c97e15a9b36d6a1f50676256d0d75e919ca6ce.webp)![](https://academy.claude.com/assets/media/561a207951198432f78adb5e96d75fd561580e6137f029938708744b0d2f38ff.webp)

### Transports and communication

5 lessons

Understand how MCP messages flow between clients and servers. Explores the JSON message protocol, STDIO transport for local development, and the complexities of StreamableHTTP including when to sacrifice features for scalability.

![](https://academy.claude.com/assets/media/19e52532332101ba2897a869fd8863891b38f603c8e9286b0ea3a55ad6ba9637.webp)![](https://academy.claude.com/assets/media/834d063d1f71a0a1f2df2aeac1f4da0b2f3929e74af70ab0c234dd327cbe5986.webp)![](https://academy.claude.com/assets/media/d729ba2e72f1ed18852a81918d0a2e8c3f9d40b033c67d114d47572c44272bea.webp)

Core MCP features

* [Sampling](https://academy.claude.com/courses/model-context-protocol-advanced-topics/sampling)
* [Sampling walkthrough](https://academy.claude.com/courses/model-context-protocol-advanced-topics/sampling-walkthrough)
* [Log and progress notifications](https://academy.claude.com/courses/model-context-protocol-advanced-topics/log-and-progress-notifications)
* [Notifications walkthrough](https://academy.claude.com/courses/model-context-protocol-advanced-topics/notifications-walkthrough)
* [Roots](https://academy.claude.com/courses/model-context-protocol-advanced-topics/roots)
* [Roots walkthrough](https://academy.claude.com/courses/model-context-protocol-advanced-topics/roots-walkthrough)

Transports and communication

* [JSON message types](https://academy.claude.com/courses/model-context-protocol-advanced-topics/json-message-types)
* [The STDIO transport](https://academy.claude.com/courses/model-context-protocol-advanced-topics/the-stdio-transport)
* [The StreamableHTTP transport](https://academy.claude.com/courses/model-context-protocol-advanced-topics/the-streamablehttp-transport)
* [StreamableHTTP in depth](https://academy.claude.com/courses/model-context-protocol-advanced-topics/streamablehttp-in-depth)
* [State and the StreamableHTTP transport](https://academy.claude.com/courses/model-context-protocol-advanced-topics/state-and-the-streamablehttp-transport)

Assessment and next steps

* [Assessment on MCP conceptsQuiz](https://academy.claude.com/courses/model-context-protocol-advanced-topics/assessment-on-mcp-concepts)

* [Completion badge](https://academy.claude.com/courses/model-context-protocol-advanced-topics/badge)
