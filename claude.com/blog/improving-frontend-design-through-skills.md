<!-- source: https://claude.com/blog/improving-frontend-design-through-skills -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22dc2ead61fff4f6e1d_589b94b913c4cee1c3c1ce2cb04f638d09c465b1-1000x1000.svg)

# Improving frontend design through Skills

Best practices for building richer, more customized frontend design with Claude and Skills.

  [Claude Code](https://claude.com/blog/category/claude-code)
* Product

  Claude apps
* Date

  November 12, 2025
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/improving-frontend-design-through-skills

You might notice that when you ask an LLM to build a landing page without guidance, it will almost always conform to Inter fonts, purple gradients on white backgrounds, and minimal animations.

The issue?  [Distributional convergence.](https://en.wikipedia.org/wiki/Convergence_of_random_variables) During sampling, models predict tokens based on statistical patterns in training data. Safe design choices–those that work universally and offend no one–dominate web training data. Without direction, Claude samples from this high-probability center.

For developers building customer-facing products, this generic aesthetic undermines brand identity and makes AI-generated interfaces immediately recognizable—and dismissible.

### The steerability challenge

The good news is that Claude is highly steerable with the right prompting. Tell Claude to "avoid Inter and Roboto" or "use atmospheric backgrounds instead of solid colors," and results improve immediately. This sensitivity to guidance is a feature; it means Claude can adapt to different design contexts, constraints, and aesthetic preferences.

But this creates a practical challenge: the more specialized the task, the more context you need to provide. For frontend design, effective guidance spans typography principles, color theory, animation patterns, and background treatment. You need to specify which defaults to avoid and which alternatives to prefer across multiple dimensions.

You could pack all this into a system prompt, but then every request–debugging Python, analyzing data, writing emails–carries frontend design context. The question becomes: how do you provide Claude with domain-specific guidance exactly when needed, without permanent context overhead for unrelated tasks?

## **Skills: dynamic context loading**

This is precisely what [Skills](https://www.anthropic.com/news/skills) were designed for: delivering specialized context on demand without permanent overhead. A skill is a document (often markdown) containing instructions, constraints, and domain knowledge, stored in a designated directory that Claude can access through simple file-reading tools. Claude can leverage these skills to dynamically load in information it needs at runtime, progressively enhancing its context instead of loading everything upfront.

When equipped with these skills and the necessary tools to read them, Claude can autonomously identify and load relevant skills based on the task at hand. For instance, when asked to build a landing page or create a React component, Claude can load a frontend design skill and apply its instructions just-in-time. This is the essential mental model: skills are prompts and contextual resources that activate on demand, providing specialized guidance for specific task types without incurring permanent context overhead.

This allows developers to reap the benefits of Claude’s steerability without overloading the context window by stuffing disparate instructions across many tasks into the system prompt. As we’ve [previously explained,](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) too many tokens in the context window can result in degradation of performance, so keeping the contents of the context window lean and focused is extremely important for eliciting the best performance from the model. Skills solve for this by making effective prompts reusable and contextual.

## **Prompting for better frontend output**

We can unlock significantly better UI generations from Claude, without permanent context overhead, by creating a frontend design skill.  The core insight is to think about frontend design the way a frontend engineer would. The more you can map aesthetic improvements to implementable frontend code, the better Claude can execute.

Leveraging this insight, we identified several areas where targeted prompting works well: typography, animations, background effects, and themes. These all translate cleanly to code that Claude can write. Implementing this in your prompts does not require detailed technical instructions, just using targeted language that engages the model to think more critically about these design axes is enough to elicit stronger outputs. This maps closely with the guidance we provided in our [context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) blog article, about prompting the model at the right altitude, avoiding the two extremes of low-altitude hardcoded logic like specifying exact hex codes and vague high-altitude guidance that assumes shared context.

### **Typography**

To see this in action, let's start by viewing typography as one dimension we can influence via prompting. The prompt below specifically steers Claude to use more interesting fonts:

```
<use_interesting_fonts>
Typography instantly signals quality. Avoid using boring, generic fonts.

Never use: Inter, Roboto, Open Sans, Lato, default system fonts

Here are some examples of good, impactful choices:
- Code aesthetic: JetBrains Mono, Fira Code, Space Grotesk
- Editorial: Playfair Display, Crimson Pro
- Technical: IBM Plex family, Source Sans 3
- Distinctive: Bricolage Grotesque, Newsreader

Pairing principle: High contrast = interesting. Display + monospace, serif + geometric sans, variable font across weights.

Use extremes: 100/200 weight vs 800/900, not 400 vs 600. Size jumps of 3x+, not 1.5x.

Pick one distinctive font, use it decisively. Load from Google Fonts.
</use_interesting_fonts>
```

**Output generated with base prompt:**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/691366f388193282b0213316_image11.png)

**Output generated with base prompt and typography section**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913679c9a202c88b680873b_image13.png)

‍

Interestingly, the mandate to use more interesting fonts seems to encourage the model to improve other aspects of the design as well.

Typography alone leads to significant improvement, but fonts are just one dimension. What about cohesive aesthetics across the entire interface?

### **Themes**

Another dimension we can prompt for is designs inspired by well-known themes and aesthetics. Claude has a rich understanding of popular themes; we can use this to communicate the specific aesthetics we want our frontend to embody. Here’s an example:

```
<always_use_rpg_theme>
Always design with RPG aesthetic:
- Fantasy-inspired color palettes with rich, dramatic tones
- Ornate borders and decorative frame elements
- Parchment textures, leather-bound styling, and weathered materials
- Epic, adventurous atmosphere with dramatic lighting
- Medieval-inspired serif typography with embellished headers
</always_use_rpg_theme>
```

This produces the following RPG-themed UI:

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913cec4181329835d1da27f_image2.png)

Typography and themes show targeted prompting works. But manually specifying each dimension is tedious. What if we could combine all these improvements into one reusable asset?

### **A general-purpose prompt**

The same principle extends to other design dimensions: prompting for motion (animations and micro-interactions) adds polish that static designs lack, while guiding the model toward more interesting background choices creates depth and visual interest. This is where a comprehensive skill shines.

Bringing this all together, we developed a ~400 token prompt – compact enough to load without bloating context (even when loaded as a skill) – that dramatically improves frontend output across typography, color, motion, and backgrounds:

```
<frontend_aesthetics>
You tend to converge toward generic, "on distribution" outputs. In frontend design,this creates what users call the "AI slop" aesthetic. Avoid this: make creative,distinctive frontends that surprise and delight. 

Focus on:
- Typography: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics.
- Color & Theme: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes. Draw from IDE themes and cultural aesthetics for inspiration.
- Motion: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions.
- Backgrounds: Create atmosphere and depth rather than defaulting to solid colors. Layer CSS gradients, use geometric patterns, or add contextual effects that match the overall aesthetic.

Avoid generic AI-generated aesthetics:
- Overused font families (Inter, Roboto, Arial, system fonts)
- Clichéd color schemes (particularly purple gradients on white backgrounds)
- Predictable layouts and component patterns
- Cookie-cutter design that lacks context-specific character

Interpret creatively and make unexpected choices that feel genuinely designed for the context. Vary between light and dark themes, different fonts, different aesthetics. You still tend to converge on common choices (Space Grotesk, for example) across generations. Avoid this: it is critical that you think outside the box!
</frontend_aesthetics>
```

In the example above, we start by giving Claude general context on the problem and what we're trying to solve for. We've found that giving the model this type of high-level context is a helpful prompting tactic to calibrate outputs. We then identify the vectors of improved design we discussed before and give targeted advice to encourage the model to think more creatively across all of these dimensions.

We also include additional guidance at the end to prevent Claude from converging to a different local maximum. Even with explicit instructions to avoid certain patterns, the model can default to other common choices (like Space Grotesk for typography). The final reminder to "think outside the box" reinforces creative variation.

### **Impact on frontend design**

With this skill active, Claude's output improves across several types of frontend designs, including:

**Example 1: SaaS landing page**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f77b_6d547f28.png)

**Caption:** AI-generated SaaS landing page with generic Inter font, purple gradient, and standard layout. No skills were used.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f790_c47f37ab.png)

**Caption:** AI-generated frontend generated using the same prompt as the rendering above in addition to the frontend skill, now with distinctive typography, cohesive color scheme, and layered backgrounds.

**Example 2: Blog layout**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f78d_f7040147.png)

AI-generated blog layout with default system fonts and flat white background. No skills were used.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f77e_0ce357ff.png)

AI-generated blog layout using the same prompt as well as the frontend skill, featuring editorial typeface with atmospheric depth and refined spacing.

**Example 3: Admin dashboard**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f784_7beb17d0.png)

AI-generated admin dashboard with standard UI components with minimal visual hierarchy. No skills were used.

‍

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f781_3705adad.png)

AI-generated admin dashboard with bold typography, cohesive dark theme, and purposeful motion, using the same prompt in addition to the frontend skill.

## **Improving artifact quality in** [**claude.ai**](http://claude.ai) **with Skills**

Design taste isn't the only limitation. Claude also faces architectural constraints when building artifacts.[Artifacts](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them) are interactive, editable content (like code or documents) that Claude creates and displays alongside your chat.

In addition to the issue with design taste explored above, Claude has another default behavior that limits its ability to generate fantastic frontend artifacts in [claude.ai](http://claude.ai). Currently, when asked to create a frontend, Claude just builds a single HTML file with CSS and JS. This is because Claude understands that frontends must be single HTML files to be properly rendered as artifacts.

In the same way you’d expect a human developer to only be able to create very basic frontends if they could only write HTML/CSS/JS in a single file, we hypothesized that Claude would be able to generate more impressive frontend artifacts if we gave it instructions to use richer tooling.

This led us to create a [web-artifacts-builder skill](https://github.com/anthropics/skills/blob/main/web-artifacts-builder/SKILL.md) which leverages Claude’s ability to [use a computer](https://www.claude.com/blog/create-files) and guides Claude to build artifacts using multiple files and modern web technologies like [React](https://react.dev/), [Tailwind CSS](https://tailwindcss.com/) and [shadcn/ui](https://ui.shadcn.com/). Under the hood, the skill exposes scripts that (1) help Claude efficiently set up a basic React repo and (2) bundle everything into a single file using [Parcel](https://parceljs.org/) to meet the single-HTML-file requirement after it is done editing. This is one of the core benefits of skills - by giving Claude access to scripts to execute boilerplate actions, Claude is able to minimize token usage while increasing reliability and performance.

With the web-artifacts-builder skill, Claude could leverage shadcn/ui's form components and Tailwind's responsive grid system to create a more comprehensive artifact.

**Example 1: Whiteboard app**

For example, when prompted to create a whiteboard app without the web-artifacts-builder skill, Claude outputted a very basic interface:

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f787_b07e5190.png)

On the other hand, when using the new web-artifacts-builder skill, Claude generated a much cleaner and more featureful application out-of-the-box that included drawing different shapes and text:

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f78a_57c49993.png)

‍

**Example 2: Task Manager App**

Similarly, when asked to create a task management app, without the skill, Claude generated a functional but very minimal application:

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f793_875d1eef.png)

With the skill, Claude generated an app that was more featureful out of the box. For example, Claude included a “Create New Task” form component that allows users to set an associated Category and Due Date on tasks:

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f7c9_7ae52606.png)

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f7a1_4c4951af.png)

‍

To try out this new skill in [Claude.ai](http://claude.ai), simply enable the skill and then ask Claude to “use the web-artifacts-builder skill” when building artifacts.

## **Optimizing Claude’s frontend design capabilities with Skills**

This frontend design skill demonstrates a broader principle about language model capabilities: models often have the ability to do more than they express by default. Claude has strong design understanding, but distributional convergence obscures it without guidance. While you could add these instructions to your system prompt, this entails that every request carries frontend design context, even when this knowledge isn’t relevant to the task at hand. Instead, using Skills transforms Claude from a tool that needs constant guidance into one that brings domain expertise to every task.

Skills are also highly customizable – you can create your own tailored to your specific needs. This allows you to define the exact primitives you want to bake into the skill, whether that's your company's design system, specific component patterns, or industry-specific UI conventions. By encoding these decisions into a Skill, you transform component parts of an agent’s thinking into a reusable asset that your entire development team can leverage. The skill becomes organizational knowledge that persists and scales, ensuring consistent quality across projects.

This pattern extends beyond frontend work. Any domain where Claude produces generic outputs despite having more expansive understanding is a candidate for Skill development. The method is consistent: identify convergent defaults, provide concrete alternatives, structure guidance at the right altitude, and make it reusable through Skills.

For frontend development, this means Claude can generate distinctive interfaces without per-request prompt engineering. To get started, explore our [frontend design cookbook](https://github.com/anthropics/claude-cookbooks/blob/main/coding/prompting_for_frontend_aesthetics.ipynb) or try out our [new frontend design plugin in Claude Code](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design).

**Feeling inspired? To create your own frontend skills, check out our** [**skill-creator**](https://github.com/anthropics/skills/tree/main/skill-creator)**.**

‍

**Acknowledgements**  
Written by Anthropic's Applied AI team: Prithvi Rajasekaran, Justin Wei, and Alexander Bricken, alongside our marketing partners Molly Vorwerck and Ryan Whitehead.

‍

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

## Agent Skills

Start using Skills with Claude to build more powerful applications today.

Get started

[Get started](https://www.claude.com/blog/skills)Get started

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6915038fea2f5466c171c21f_Hand-NodeWeb.svg)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/691503928e574d7dc8407b4a_Hand-NodeWeb-1.svg)

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225588ad176f7c4aafd_abc884c723daea810d2e986455358281a2f94102-1000x1000.svg)

Jun 24, 2026

### Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

Claude Code

[Agent identity in Claude Tag: a new access model for autonomous, team-wide AI](#)Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

[Agent identity in Claude Tag: a new access model for autonomous, team-wide AI](/blog/agent-identity-access-model)Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f7912d5b05a5c7ed8ae86_Object-CodeChatCode.svg)

Jun 3, 2026

### Running an AI-native engineering org

Claude Code

[Running an AI-native engineering org](#)Running an AI-native engineering org

[Running an AI-native engineering org](/blog/running-an-ai-native-engineering-org)Running an AI-native engineering org

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

May 12, 2026

### How Anthropic's cybersecurity team built a threat detection platform with Claude Code

Claude Code

[How Anthropic's cybersecurity team built a threat detection platform with Claude Code](#)How Anthropic's cybersecurity team built a threat detection platform with Claude Code

[How Anthropic's cybersecurity team built a threat detection platform with Claude Code](/blog/how-anthropic-uses-claude-cybersecurity)How Anthropic's cybersecurity team built a threat detection platform with Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2222403b092e0358b0e_cd4fd51deacd067d4e30aee4f4b149f6cba1b97b-1000x1000.svg)

Apr 20, 2026

### Meet the winners of our Built with Opus 4.6 Claude Code hackathon

Claude Code

[Meet the winners of our Built with Opus 4.6 Claude Code hackathon](#) Meet the winners of our Built with Opus 4.6 Claude Code hackathon

[Meet the winners of our Built with Opus 4.6 Claude Code hackathon](/blog/meet-the-winners-of-our-built-with-opus-4-6-claude-code-hackathon) Meet the winners of our Built with Opus 4.6 Claude Code hackathon

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

    

    

    

    

    

    

    

    

    

    

Claude apps
