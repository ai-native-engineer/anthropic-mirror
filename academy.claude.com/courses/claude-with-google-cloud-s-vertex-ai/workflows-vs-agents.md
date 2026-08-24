<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/workflows-vs-agents -->

Lesson 66 of 66 · Claude with Google Cloud's Vertex AIWorkflows vs agents

When building AI-powered applications, you'll need to choose between two main architectural patterns: workflows and agents. Each has distinct advantages and trade-offs that make them suitable for different scenarios.

![](https://academy.claude.com/assets/media/a3bd1241321dbde88a34137efc0d46c07aab7d8c6b4d893fe5d2f04b2259a7be.png)

## Workflows

Workflows are a predefined series of calls to Claude designed to solve a known problem or set of problems. Think of them as a recipe - you know exactly what ingredients you need and what steps to follow.

You'll want to use workflows when you can picture the flow of steps ahead of time. The key insight is breaking down a big task into much smaller, more specific subtasks.

### Benefits of Workflows

* Claude can focus on one subtask at a time, generally leading to higher accuracy
* Far easier to evaluate and test, since you know each exact step
* More predictable and reliable execution

### Downsides of Workflows

* Far less flexible - dedicated to solving specific types of tasks
* Generally more constrained user experience - you need to know the exact inputs to the flow

## Agents

With agents, Claude is given a set of basic tools and we expect it to formulate a plan to use these tools to complete a task. Instead of following a predetermined path, Claude creatively figures out how to handle challenges.

### Benefits of Agents

* Allow for more flexible user experience
* Far more flexible task completion - Claude can combine tools in unexpected ways to complete a wide variety of tasks
* Can create their own inputs based on user queries and ask for more input when needed

### Downsides of Agents

* Lower successful task completion rate compared to workflows
* More challenging to instrument, test, and evaluate since you often don't know what series of steps the agent will execute

## Choosing the Right Approach

While agents are really interesting from a technical perspective, remember that your primary goal as an engineer is to solve problems reliably. Users probably don't care that you've built a fancy agent - they want a product that works 100% of the time.

The general recommendation is to always focus on implementing workflows where possible, and only resort to agents when they are truly required. Workflows give you the predictability and reliability that most production applications need, while agents provide flexibility for scenarios where the exact solution path can't be predetermined.
