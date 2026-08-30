<!-- source: https://academy.claude.com/use-cases/build-interactive-diagram-tools -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Build interactive diagram tools

From body systems to molecular structures, turn a detailed prompt into a working reference app with the depth and design you specify.

15 minPersonalClaude.ai

Try in ClaudeCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-lmzl8w8i.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-b11puwfg.png)

![Build interactive diagram tools result](https://academy.claude.com/assets/v1/build-interactive-diagram-tools-dbg1inft.png)[Open artifact](https://claude.ai/public/artifacts/f83ae1ec-6136-4b37-a502-4405235ebb05)

## 1. Describe the task[](#1-describe-the-task)

Claude can build interactive tools that let you engage with material directly, whether that's anatomy, chemistry diagrams, or historical timelines. The precision of your prompt shapes the sophistication of the result.

Describe the experience you want: what you're learning, how you want to interact with it, where the data comes from, and your aesthetic standards. Think of your prompt as a design brief.

You don't need to start this specific. Begin with the experience you want, then fold in technical constraints like the SVG fill and UBERON notes as you discover what trips the build up.

Build an **interactive anatomy explorer** using @ebi-gene-expression-group/anatomogram from npm. Use homo\_sapiens.male.svg and homo\_sapiens.brain.svg. Don't generate diagrams yourself—these SVGs contain accurate illustrations with UBERON ontology IDs already embedded. Embed the SVGs directly into the HTML—no fetch requests needed.

**Critical:** The SVGs style all elements with fill:none;stroke:none by default, making them invisible. After loading, apply default fills and strokes before any other styling. Also set cleanupIds: false when optimizing (the UBERON IDs are how you target elements) and remove the visibility:hidden attribute in JavaScript.

**Design requirements:** Restrained and sophisticated. No glows, no emojis, no neon. Warm colors over cold. Serif headings, sans-serif body, monospace for data. Think premium medical reference, not generic AI output.

Add tabbed information panels, physical-feeling sound feedback, and content rich enough to actually learn from. Build to flagship quality from the start—I'll iterate until this is exceptional.

Open in Claude

## 2. Give Claude context[](#2-give-claude-context)

The prompt above supplies its own context: the data source (the anatomogram package with its UBERON IDs), the interaction model (hover, click, tabbed body systems), and the design standard (premium medical reference, warm colors, serif headings). Claude builds from exactly what you pin down, so each of those choices shows up in the result.

### Required context[](#required-context)

Artifacts are standalone, interactive outputs that Claude creates in a dedicated window alongside your conversation. When you ask for an interactive tool like this anatomy explorer, Claude typically builds it as an artifact automatically, rendered and ready to use.

### Optional context[](#optional-context)

For complex multi-component apps, turn on [Extended Thinking(opens in new tab)](https://support.claude.com/en/articles/10574485-using-extended-thinking) so Claude can plan architecture before building.

[

Extended Thinking](https://support.claude.com/en/articles/10574485-using-extended-thinking)

## 3. What Claude creates[](#3-what-claude-creates)

Claude builds a fully functional React application with the visual design, interaction patterns, and educational content you specified, ready to use immediately in the artifact viewer.

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

## 4. Follow up prompts[](#4-follow-up-prompts)

Continue the conversation with Claude to refine, expand, or explore further.

### Add self-testing[](#add-self-testing)

Layer in more functionality, like an active learning mode that reinforces retention.

Add a quiz mode where I'm shown a description or function and have to identify the correct structure. Track my accuracy and show which systems I struggle with.

Open in Claude

### Add advanced features[](#add-advanced-features)

Ask Claude to expand anatomical detail where you want more granularity.

Add more body systems to the diagram. Also make the brain view more detailed.

Open in Claude

### Generate companion materials from the same session[](#generate-companion-materials-from-the-same-session)

Continue learning from different mediums. The app and study materials can share a source of truth.

From the anatomical data in this explorer, generate a printable PDF study guide with the same structures organized by system, plus a set of Anki-compatible flashcards I can import. Keep the terminology and clinical correlations consistent with what's in the app.

Open in Claude

## 5. Tricks, tips, and troubleshooting[](#5-tricks-tips-and-troubleshooting)

### Paste errors directly into chat[](#paste-errors-directly-into-chat)

When something breaks, like a structure that won't highlight or a system tab that stops filtering, paste the error message or describe what you're seeing. Claude can trace the logic and identify the issue so you don't need to debug the code yourself.

### Long sessions compound rather than drift[](#long-sessions-compound-rather-than-drift)

Opus 4.5 maintains your design decisions and technical context across extended conversations. Your tenth iteration still remembers your original aesthetic requirements, technical constraints, and every refinement in between. You can plan for sustained building sessions rather than trying to specify everything upfront.

### Include known troubleshooting upfront[](#include-known-troubleshooting-upfront)

If you've hit quirks before—from previous Claude sessions or your own debugging—mention them in the prompt. This example notes that the anatomogram SVGs render invisible by default and that UBERON IDs get stripped during optimization. Without those notes, Claude writes working code that produces a blank screen, then spends iterations diagnosing.

### Spot-check the panels before you study from them[](#spot-check-the-panels-before-you-study-from-them)

The anatomogram package supplies the accurate illustrations, but Claude writes the text in the information panels: each structure's function, clinical relevance, and quick facts. Before relying on the explorer as a study tool, click through a few structures and compare what the panels say against your textbook or lecture notes. Flag anything that doesn't match and ask Claude to correct it.

### Add sources to make it yours[](#add-sources-to-make-it-yours)

Opus 4.5's context window handles substantial material. If you have a textbook chapter, lecture notes, or syllabus you want the app to cover, paste the whole thing rather than summarizing. Claude extracts structure and prioritizes content more effectively from complete sources than from your condensed version.

## 6. Ready to try for yourself?[](#6-ready-to-try-for-yourself)

Pick something you've been meaning to understand. Claude builds the tool; you do the learning.

Build an interactive anatomy explorer using @ebi-gene-expression-group/anatomogram from npm. Use homo\_sapiens.male.svg and homo\_sapiens.brain.svg. Don't generate diagrams yourself—these SVGs contain accurate illustrations with UBERON ontology IDs already embedded. Embed the SVGs directly into the HTML—no fetch requests needed.

Critical: The SVGs style all elements with fill:none;stroke:none by default, making them invisible. After loading, apply default fills and strokes before any other styling. Also set cleanupIds: false when optimizing (the UBERON IDs are how you target elements) and remove the visibility:hidden attribute in JavaScript.

Design requirements: Restrained and sophisticated. No glows, no emojis, no neon. Warm colors over cold. Serif headings, sans-serif body, monospace for data. Think premium medical reference, not generic AI output.

Add tabbed information panels, physical-feeling sound feedback, and content rich enough to actually learn from. Build to flagship quality from the start—I'll iterate until this is exceptional.

Try in Claude

* [1. Describe the task](#1-describe-the-task)
* [2. Give Claude context](#2-give-claude-context)
* [3. What Claude creates](#3-what-claude-creates)
* [4. Follow up prompts](#4-follow-up-prompts)
* [5. Tricks, tips, and troubleshooting](#5-tricks-tips-and-troubleshooting)
* [6. Ready to try for yourself?](#6-ready-to-try-for-yourself)
