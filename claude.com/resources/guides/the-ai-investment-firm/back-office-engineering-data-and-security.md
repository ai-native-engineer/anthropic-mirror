<!-- source: https://claude.com/resources/guides/the-ai-investment-firm/back-office-engineering-data-and-security -->

Chapter 143 min read

# Back office: Engineering, data, and security

3 min read

12 min remaining

Engineering and data teams build the systems the other teams’ agents depend on, and they work with Claude more than any other team. They write code with it and rebuild the firm’s systems and data so that agents can work with them too.

## Main use cases

### Running Claude Code under the firm’s controls

Developers and quants work in Claude Code with per-user attribution, sandboxing, and a shared library of approved skills. Analysts, operators, and support staff are starting to work in it too.

### Building systems for agents as well as people

Most systems of record were built for a person looking at a screen. Now, data teams make tick stores, the security master, positions, the deal pipeline, portfolio-company metrics, and data warehouses available to agents as tools, with access set by team and business unit. They connect Claude to these systems through the Model Context Protocol (MCP), and each agent gets only the access its task needs. New systems are designed so that an agent can work with them as easily as a person can.

### Modernizing legacy systems

Agents work best on systems they can read, so modernization starts with Claude mapping a legacy system and pulling out the business rules buried in its code. From there, the firm can upgrade the system in place, port it module by module, or rebuild it on a modern architecture. On each path, the firm runs the old and new versions side by side to confirm that the outputs match. Refactors can run overnight as fleets of agents, each in an isolated workspace with a budget cap. Anthropic’s code modernization plugin packages these steps. More ready-made plugins are in the plugin directory and the financial services and knowledge work marketplaces.

### Working with Claude across the software lifecycle

Engineers work with Claude at each stage of the software lifecycle. It writes code along with unit and smoke tests, reviews changes, and checks them for security issues. Security teams work with it in red-team, blue-team, and purple-team exercises, and agents enrich and triage alerts for the security operations team.

#### Outcome: Engineering teams build more, and junior engineers start from the house standard. The security team can inspect the controls around Claude.
