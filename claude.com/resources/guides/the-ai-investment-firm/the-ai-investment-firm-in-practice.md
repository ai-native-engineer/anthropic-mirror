<!-- source: https://claude.com/resources/guides/the-ai-investment-firm/the-ai-investment-firm-in-practice -->

Chapter 024 min read

# The AI investment firm in practice

4 min read

45 min remaining

*Most investment firms now use AI. The firms getting the most from it organize their work around six best practices.*

A firm already has an edge in its proprietary data, house methods, and the judgment of its senior people. But senior people only have so many hours. When they write down how they work, Claude can apply their methods to more names, deals, and decisions than they could cover alone, and draw on more sources for each one. To do that, the firm needs connected data, methods written as skills, evals that score the agent’s work, and a memory of past work. All of it belongs to the firm, and teams refine it as they work. Each new model starts from everything the firm has built.

## **Practices at leading firms**

### **Record baselines**

Before an agent takes on a core process, the firm records how long the work takes the people doing it today and how often they get it right, with measures like days to close the books or hours to get from an earnings print to a position.

### **Test agents on the team’s work**

For each core process, the team builds a test set from its real work and scores the agent against a human baseline or a desired output. These scored tests, called evals, show when an agent can be trusted with more and which model should run a task. When a new model comes out, the same evals show whether it’s ready to adopt.

### **Write down methods as skills**

Senior people write down how they build a model or clear a break as a skill (a set of instructions that Claude follows much like an employee would). Once a skill is written down, the whole team can work from it and the firm can improve it over time. Because the skills encode the firm’s best practices, junior employees don’t have to start from zero and senior ones spend more of their time on judgment calls and coaching than on checking their work.

### **Redesign roles for human-agent work**

Leading firms expand existing roles and add new ones, such as skill authors, eval owners, and agent operators, and they rethink how junior staff learn the job. Because an agent can take a task through several steps, handoffs between people, within a team or between teams, become simpler.

### **Have Claude write the code for calculations that must be exact**

Some tasks are rule-based calculations with exactly one right answer, such as whether a position breaches a risk limit or how much an investor owes in fees. These tasks run as deterministic code, so the same data always gets the same answer, and the logic can be tested and audited. Claude can write that program and the tests that check it. When the program flags a problem, such as a limit breach, Claude looks into it and explains which trades caused it.

### **Switch to a new model once it matches the current one on evals**

When a new model is released, firms run the same evals and compare its work with the current model’s. They keep skills current and connect Claude to their data providers and internal systems, so these evals run smoothly. If the scores hold, they upgrade to the new model; if the scores drop, they adjust the instructions and skills and test again until the new model meets or exceeds the performance of its predecessor.
