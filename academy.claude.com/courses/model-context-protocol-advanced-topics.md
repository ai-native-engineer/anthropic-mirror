<!-- source: https://academy.claude.com/courses/model-context-protocol-advanced-topics -->

11 lessons · 1 quizModel Context Protocol: Advanced Topics

What you’ll learnBy the end of this course, you’ll be able to

* Understand how MCP servers can request language model calls through connected clients via sampling, shifting AI costs and complexity from server to client
* Implement real-time feedback using context objects, logging callbacks, and progress reporting for long-running operations
* Use roots to grant MCP servers access to specific directories with security boundaries and user-friendly file discovery
* Distinguish between request-result pairs and notification messages in the MCP message specification, and understand bidirectional communication patterns
* Understand how MCP clients and servers communicate over standard input/output streams, including the required initialization handshake sequence
* Explain how Server-Sent Events (SSE) enable server-to-client communication over HTTP, including session management and dual-connection architectures
* Recognize how configuration flags affect functionality, particularly server-initiated requests and streaming capabilities
* Decide when to use stateless HTTP for horizontal scaling with load balancers, weighing the trade-offs between stateful and stateless server configurations
* Choose appropriate transport methods based on deployment requirements, functionality needs, and scaling constraints

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
