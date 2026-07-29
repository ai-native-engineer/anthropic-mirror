<!-- https://anthropic.skilljar.com/claude-with-google-vertex/289245 -->

# Workflows vs agents

_(등록 또는 권한이 필요한 레슨)_

<!-- jwplayer-srt: https://cdn.jwplayer.com/tracks/iGhxwWnS.srt -->

<details>
<summary>자막: Workflows vs agents</summary>

Let's wrap up by comparing and contrasting some different aspects of workflows and agents. First, recall that workflows are a predefined series of calls to Claude. We often use workflows when we have a good idea of the exact series of steps that are needed to complete a task. With agents, on the other hand, we don't know exactly what task will be provided, so we instead provide a solid set of basic tools and expect Claude to combine these tools together to complete a given task. You might have noticed that a common theme around workflows is that we take a big task and we divide it up into much smaller tasks. Each of these smaller tasks are much more specific in nature, allowing Claude to focus on a single area at a time. This increased focus generally leads to higher accuracy for completing a task compared to agents. Because we know the exact series of steps that a workflow executes, they're also far easier to test and evaluate. With Agents, we aren't constrained to a series of steps etched in stone. Instead, Claude can creatively figure out how to handle a wide variety of challenges. Along with this flexibility, we also get flexibility in the user experience. While workflows expect to receive a very particular set of inputs, Agents can create their own inputs based on queries received from the user, and Agents can also ask user for more input when it's needed. The downside to agents is that they generally have a lower successful task completion rate compared to workflows because we are delegating so much work to Claude. In addition, they're also harder to test and evaluate, since we often don't have a good idea of what series of steps an agent will execute to complete a given task. At the end of the day, agents are really interesting, but remember, your primary goal as an engineer is to solve problems reliably. Users probably don't care that you've made a fancy agent. They really just want a product that's built to work 100% of the time. So with this in mind, the general recommendation is to always focus on implementing workflows where possible and only resort to agents when they are truly required.

</details>
