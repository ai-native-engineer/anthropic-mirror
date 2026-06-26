<!-- source: https://claude.com/resources/use-cases/build-interactive-diagram-tools -->

Personal

Extended Thinking

# Build interactive diagram tools

From body systems to molecular structures, turn a detailed prompt into a working reference app with the depth and design you specify.

Try in Claude

[Try in Claude](https://claude.com/download)Try in Claude

* Author

  Anthropic

  Personal
* Model

  Opus 4.5
* Features

  Extended Thinking
* Share

  [Copy link](#)

  https://claude.com/resources/use-case/build-interactive-diagram-tools

1

## Describe the task

Claude can build interactive tools that let you engage with material directly, whether that's anatomy, chemistry diagrams, or historical timelines. The precision of your prompt shapes the sophistication of the result.

Describe the experience you want: what you're learning, how you want to interact with it, where the data comes from, and your aesthetic standards. Think of your prompt as a design brief.

Build an **interactive anatomy explorer** using @ebi-gene-expression-group/anatomogram from npm. Use homo\_sapiens.male.svg and homo\_sapiens.brain.svg. Don't generate diagrams yourself—these SVGs contain accurate illustrations with UBERON ontology IDs already embedded. Embed the SVGs directly into the HTML—no fetch requests needed.

**Critical:** The SVGs style all elements with fill:none;stroke:none by default, making them invisible. After loading, apply default fills and strokes before any other styling. Also set cleanupIds: false when optimizing (the UBERON IDs are how you target elements) and remove the visibility:hidden attribute in JavaScript.

**Design requirements:** Restrained and sophisticated. No glows, no emojis, no neon. Warm colors over cold. Serif headings, sans-serif body, monospace for data. Think premium medical reference, not generic AI output.

Add tabbed information panels, physical-feeling sound feedback, and content rich enough to actually learn from. Build to flagship quality from the start—I'll iterate until this is exceptional.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

2

## Give Claude context

For creating interactive learning tools, after describing both what you want to learn and how you want to interact with it, make sure you have the correct capabilities and features enabled.

## Required context

Make sure file creation is enabled in settings for Claude to create artifacts.

No items found.

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

## Optional context

For complex multi-component apps, turn on [Extended Thinking](https://support.claude.com/en/articles/10574485-using-extended-thinking) so Claude can plan architecture before building.

Extended Thinking

3

## What Claude creates

Claude builds a fully functional React application with the visual design, interaction patterns, and educational content you specified, ready to use immediately in the artifact viewer.

From Claude

Done! I've built your anatomy explorer with the medical-grade SVGs, proper UBERON targeting, and the restrained design system you described.

What's included:

**1. Dual-view explorer**

Toggle between full-body and brain views. The full-body view organizes systems by color (skeletal, muscular, nervous, circulatory, respiratory, digestive) with proper anatomical positioning.

**2. Interactive elements**

Hover any structure to see its name, UBERON ID, and primary function. Click for deeper information: clinical relevance, related structures, and quick facts. I've populated approximately 40 structures with learning-grade content.

**3. System filters**

Tabs let you isolate individual body systems. When you select "Skeletal," non-skeletal structures fade while relevant bones gain emphasis and become interactive.

**4. Sound design**

Subtle audio feedback on hover and selection. Soft clicks and tones that feel physical, not digital. Muted by default; toggle in the corner.

**5. Design details**

Warm beige background, terracotta and slate accents, no harsh colors. Playfair Display for headings, Inter for body text, IBM Plex Mono for data. Generous whitespace, no visual clutter.

4

## Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Add self-testing

Layer in more functionality, like an active learning mode that reinforces retention.

Add a quiz mode where I'm shown a description or function and have to identify the correct structure. Track my accuracy and show which systems I struggle with.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Add advanced features

Ask Claude to expand anatomical detail where you want more granularity.

Add more body systems to the diagram. Also make the brain view more detailed.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Generate companion materials from the same session

Continue learning from different mediums. The app and study materials can share a source of truth.

From the anatomical data in this explorer, generate a printable PDF study guide with the same structures organized by system, plus a set of Anki-compatible flashcards I can import. Keep the terminology and clinical correlations consistent with what's in the app.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

5

## Tricks, tips, and troubleshooting

### Paste errors directly into chat

When something breaks, share the error message or describe the issue. Claude can trace the logic and troubleshoot to identify the issue so you don't need to debug yourself.

### Long sessions compound rather than drift

Opus 4.5 maintains your design decisions and technical context across extended conversations. Your tenth iteration still remembers your original aesthetic requirements, technical constraints, and every refinement in between. You can plan for sustained building sessions rather than trying to specify everything upfront.

### **Include known troubleshooting upfront**

**‍**If you've hit quirks before—from previous Claude sessions or your own debugging—mention them in the prompt. This example notes that the anatomogram SVGs render invisible by default and that UBERON IDs get stripped during optimization. Without those notes, Claude writes working code that produces a blank screen, then spends iterations diagnosing.

### Add sources to make it yours

Opus 4.5's context window handles substantial material. If you have a textbook chapter, lecture notes, or syllabus you want the app to cover, paste the whole thing rather than summarizing. Claude extracts structure and prioritizes content more effectively from complete sources than from your condensed version.

## Ready to try for yourself?

Pick something you've been meaning to understand. Claude builds the tool; you do the learning.

Try in Claude

[Try in Claude](/download)Try in Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6924a785986e6eef5ac26cb2_Screenshot%202025-11-24%20at%2010.44.16%E2%80%AFAM.png)

Open artifact in new window

[Open artifact in new window](https://claude.ai/public/artifacts/f83ae1ec-6136-4b37-a502-4405235ebb05)Open artifact in new window

## Related use cases

[Map your understanding and build lessons from the gaps](/resources/use-cases/map-your-understanding-and-build-lessons-from-the-gaps)Map your understanding and build lessons from the gaps

Map your understanding and build lessons from the gaps

Use case

[Use case](/resources/use-cases/map-your-understanding-and-build-lessons-from-the-gaps)Use case

[Stress-test your financial plan across scenarios](/resources/use-cases/stress-test-your-financial-plan-across-scenarios)Stress-test your financial plan across scenarios

Stress-test your financial plan across scenarios

Use case

[Use case](/resources/use-cases/stress-test-your-financial-plan-across-scenarios)Use case

[Organize files across your desktop](/resources/use-cases/organize-files-by-whats-in-them)Organize files across your desktop

Organize files across your desktop

Use case

[Use case](/resources/use-cases/organize-files-by-whats-in-them)Use case

[Thoughtful gift giving with Claude](/resources/use-cases/thoughtful-gift-giving-with-claude)Thoughtful gift giving with Claude

Thoughtful gift giving with Claude

Use case

[Use case](/resources/use-cases/thoughtful-gift-giving-with-claude)Use case
