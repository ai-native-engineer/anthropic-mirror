<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/qualities-of-agents -->

Lesson 65 of 65 · Claude with Amazon BedrockQualities of agents

After exploring Claude Code and Computer Use, we can identify key patterns that reveal what makes agents successful. Both tools demonstrate a systematic approach to problem-solving that relies on focused tool usage, environmental awareness, and iterative execution.

## How Agents Work in Practice

When Claude was asked to add a test for a specific corner case, it followed a clear pattern of tool usage. The agent made four distinct tool calls: two to read existing files, one to update a file, and one to run tests. This breakdown reveals something important about agent behavior.

![](https://academy.claude.com/assets/media/f5ad5bff08977290779432f4bf7ad736a0a15f0ff27771903c6e10b0af9ecc32.png)

Three of these calls were purely about gathering information from the environment - understanding the existing codebase before making changes. Only one call actually modified the environment. This pattern of "observe first, then act" appears consistently across both Claude Code and Computer Use.

Computer Use follows the same approach when testing web applications. Each tool call returns a screenshot, giving Claude immediate visual feedback about the current state of the interface. This constant feedback loop allows the agent to understand what's happening and adjust its next actions accordingly.

![](https://academy.claude.com/assets/media/f729ca3174769335bba7632b5af7b9b40bcdc9463cab2c57e19c20e8008d841f.png)

## Comparing Agent Approaches

Both Claude Code and Computer Use share several fundamental characteristics that make them effective:

![](https://academy.claude.com/assets/media/327fc00b2bcbbddd68c521a6666ea996e1e8fe62727634f0c9ec0c5584d57c7c.png)

* **Tool-based execution:** Both systems use tools extensively and run them in loops until reaching success criteria or hitting an error
* **Environmental context:** Rather than relying on detailed prompts or RAG processes, they gather context directly through tool interactions
* **Focused toolsets:** Each agent has a small, well-defined set of tools with clear purposes
* **High-value, low-risk tasks:** Both tackle complex problems where mistakes are manageable
* **Low error costs:** Computer Use has very low error costs, while Claude Code has low but not negligible costs

## Key Qualities of Effective Agents

Based on these observations, successful agents share four critical qualities:

### Focused Tool Sets Running in Loops

Agents work best with a small number of simple, well-defined tools. They keep executing these tools until reaching an iteration limit, encountering an error, or meeting success criteria. This iterative approach allows for course correction and refinement.

### Context is Everything

Claude has no inherent knowledge of your specific environment. It needs tools to read from and understand the current state of whatever system it's working with. The quality of context gathering directly impacts agent performance.

### High Value Tasks with Low Error Costs

Agents excel at complex, knowledge-intensive work where mistakes won't cause major damage. Writing code is a perfect example - it requires significant expertise, but errors can be caught and fixed without catastrophic consequences. Avoid using agents for high-stakes decisions where errors could have serious economic or safety impacts.

### Continuous Evaluation

The only reliable way to build effective agents is through rigorous testing. Create evaluation criteria and continuously test your agent's performance against real scenarios. This feedback loop is essential for identifying weaknesses and improving reliability.

![](https://academy.claude.com/assets/media/138be9580cf8b3ff3595fb0ff9355ca6dc8a61a70d7b13cae4fe0ce01be10a10.png)

Understanding these patterns helps explain why Claude Code and Computer Use work so well - they're designed around these fundamental principles of effective agent architecture. When building your own agents, keep these qualities in mind to create systems that are both powerful and reliable.
