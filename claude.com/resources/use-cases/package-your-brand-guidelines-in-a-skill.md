<!-- source: https://claude.com/resources/use-cases/package-your-brand-guidelines-in-a-skill -->

Professional

Skills

# Package your brand guidelines in a skill

Package your brand guidelines into a skill to create presentations, spreadsheets, or documents that automatically match your preferred style.

Try in Claude

[Try in Claude](https://claude.com/download)Try in Claude

* Author

  Anthropic

  Professional
* Model

  Sonnet 4.5
* Features

  Skills
* Share

  [Copy link](#)

  https://claude.com/resources/use-case/package-your-brand-guidelines-in-a-skill

1

## Describe the task

[Skills](https://support.claude.com/en/articles/12512176-what-are-skills) let you package expertise, like your complete brand identity, for Claude to automatically apply across conversations. Upload your color palette, define your typography standards, and specify when to use which elements. Claude can then apply your brand guidelines automatically in any chat, whether it's for a quarterly report, client presentation, or internal spreadsheet.  
‍

[Creating this skill](https://support.claude.com/en/articles/12599426-how-to-create-a-skill-with-claude-through-conversation) takes minutes. To start, walk through your brand fonts, colors, and other stylistic choices. Ask Claude to structure the information into a reusable skill that activates whenever you need brand-consistent outputs.

I want to create a skill that applies our company's brand styling to any presentation, document, or spreadsheet I create in Claude. Here's what I need to encode:

###### **Color Palette:**

Dark: #141413 (primary text, dark backgrounds)

Light: #faf9f5 (light backgrounds, text on dark)

Mid Gray: #b0aea5 (secondary elements)

Light Gray: #e8e6dc (subtle backgrounds)

Orange: #d97757 (primary accent for important elements)

Blue: #6a9bcc (secondary accent)

Green: #788c5d (tertiary accent)

###### **Typography:**

Headings (24pt and larger): Poppins font, bold weight

Body text: Lora font, regular weight

Fallbacks: Arial for headings if Poppins unavailable, Georgia for body if Lora unavailable

###### **Application Rules:**

* Apply Poppins to all slide titles and document headings
* Apply Lora to body text and paragraphs
* Use accent colors (orange, blue, green) for shapes, charts, and visual elements
* Cycle through accent colors to maintain visual interest
* Use dark color for primary text on light backgrounds
* Use light color for text on dark backgrounds

Create a complete skill with proper structure that I can use whenever I need brand-consistent presentations. Include the SKILL.md file with clear instructions for when to use it and how it applies the styling.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

2

## Give Claude context

Upload any existing brand guidelines, style sheets, or design documentation to serve as examples that Claude can reference within the skill. Enable file creation and Skills in your [settings](https://claude.ai/settings/capabilities) so Claude can build the complete skill package with proper structure, code, and documentation.

‍

## Required context

Enable the [Google Drive](https://support.claude.com/en/articles/10166901-using-the-google-drive-integration) integration so Claude can access your brand reference file to further enhance your skill.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68efe427f3a0ebdeb2c3a468_google_drive.svg)

Google Drive

brand-reference-file

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68eff599f02e8d84f204b878_google_doc.svg)

DOC

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

brand-reference-file

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

DOC

## Optional context

Turn on [Extended Thinking](https://support.claude.com/en/articles/10574485-using-extended-thinking) to help Claude make sophisticated decisions about when to apply which brand elements based on visual hierarchy and content importance.

‍

Extended Thinking

3

## What Claude creates

Claude produces a complete, working skill package with clear instructions for when the skill applies, brand color specifications with hex values, typography guidelines with fallback fonts, and implementation details. The skill activates automatically when you request your brand styling.

From Claude

I've created a comprehensive skill that will automatically apply your company's brand guidelines to every presentation, document, and spreadsheet you create in Claude.

*View your brand-guidelines.skill*

The skill includes:

1. SKILL.md - The core skill document with complete brand specifications
2. color-typography-specs.md - Detailed technical specifications with Python code examples
3. usage-examples.md - Practical examples showing how the skill works
4. brand\_utils.py - Python utility module for easy implementation

### **Your Brand System**

Color Palette:

* Dark (#141413) - primary text
* Light (#faf9f5) - backgrounds
* Orange (#d97757) - primary accent
* Blue (#6a9bcc) - secondary accent
* Green (#788c5d) - tertiary accent
* Plus mid gray and light gray for supporting elements

**T**ypography:

* Poppins Bold for all headings (fallback: Arial)
* Lora Regular for all body text (fallback: Georgia)

### **How It Works**

The skill activates automatically whenever you:

* Create a new presentation, document, or spreadsheet
* Edit existing .pptx, .docx, or .xlsx files
* Request any business document creation

You don't need to mention brand guidelines - it just works! Just ask for what you need:

* "Create a 10-slide presentation about Q4 results"
* "Write a project proposal document"
* "Make a budget tracking spreadsheet"

And the brand guidelines are automatically applied with:

* Correct fonts and sizes
* Brand color palette
* Proper contrast ratios
* Professional spacing
* Accent colors in sequence

### **Additional Resources**

I've also created helpful reference materials:

* View README - Complete package overview
* View Quick Reference - Color and typography at a glance

**Key Features**

Smart & Automatic:

* Triggers on document creation/editing without explicit commands
* Applies brand standards seamlessly
* Cycles through accent colors intelligently

Comprehensive:

* Covers presentations, documents, and spreadsheets
* Includes Python code utilities for advanced users
* Provides fallback fonts when needed

Professional Quality:

* WCAG AA accessible color contrasts
* Typography hierarchy that scales
* Consistent visual identity across all outputs

### **Next Steps**

1. Install the skill - Upload brand-guidelines.skill to Claude
2. Start creating - Just ask for documents normally
3. Watch the magic - Brand guidelines apply automatically!

You can also upload the brand PDF you mentioned if you'd like me to cross-reference or enhance the skill with additional assets from it. But as it stands, the skill is fully functional and ready to use with all the specifications you provided!

‍

4

## Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Test the skill

Create new content and watch your brand apply automatically without specifying colors or fonts. Claude handles all visual styling decisions based on your uploaded guidelines, letting you focus on content rather than formatting details.

Create a quarterly business review presentation covering revenue growth, customer acquisition, and market expansion. Use our brand guidelines.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Update the skill

Make changes or add additional visual standards to your skill as your brand evolves. Simply tell Claude your desired output, and it will edit your Skills as your needs evolve.

Update my brand guidelines skill. Use the dark background with light text for all title slides, but keep content slides light. Make the heading font size 28pt instead of 24pt. Also, add our new product colors to the brand guidelines skill: Purple #8B7AB8 for premium features, Teal #4A9B9B for analytics content. These should be used in charts when presenting those specific topics.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Stack your skills

Skills are [composable](https://www.anthropic.com/news/skills), meaning they can reference each other for Claude to use them together. Your ‘brand-guidelines’ skill can work with other skills you've created—like product-research or writing-standards—to produce work that's both visually sophisticated and aligned with your other requirements

Create a pitch deck for our new product launch. Use my brand-guidelines skill for formatting and apply the product-research skill to find relevant information.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

5

## Tricks, tips, and troubleshooting

### Understand how progressive disclosure works**‍**

When Claude evaluates a task, it first scans skill metadata (the description at the top) to see if the skill is relevant. Only if it matches does Claude load the full instructions. Reference files load only when actually needed. This means you can have many skills available without overwhelming Claude's context.

### Add bundled scripts for deterministic execution

Instructions allow interpretation variance. Scripts execute identically every time. If your brand skill says "apply orange accent `#d97757`," Claude interprets how to apply it. If your skill includes `scripts/apply_brand_colors.py` with exact RGB values and application logic, execution is deterministic. Use scripts for specific color application, file transformations, data formatting, or anything where consistency matters more than flexibility. Keep instructions for decision-making, creative choices, and context-dependent behavior.

### Learn more about skill creation

When you ask Claude to create a skill, Claude is using a skill-creator skill under the hood. This skill teaches Claude how to package your workflow into proper SKILL.md format, organize your files correctly, and package everything into a ZIP file. You describe your process in conversation and Claude uses the skill-creator skill to handle the translation of "I want bullets here and prose there" into the proper structure. To learn more about creating skills in Claude.ai, see [*How to create a skill with Claude*.](https://support.claude.com/en/articles/12599426-how-to-create-a-skill-with-claude-through-conversation)

## Ready to try for yourself?

Create a skill once, and Claude applies that expertise automatically. Start with something you explain often, like your brand colors or your preferred report format, and watch how the skill activates exactly when you need it.

Try in Claude

[Try in Claude](/download)Try in Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690b2d4b8554b697ab0271e1_Frame%201430106298.png)

Open artifact in new window

[Open artifact in new window](#)Open artifact in new window

## Related use cases

[Source insights from your tools to build a deck](/resources/use-cases/source-insights-from-your-tools-to-build-a-deck)Source insights from your tools to build a deck

Source insights from your tools to build a deck

Use case

[Use case](/resources/use-cases/source-insights-from-your-tools-to-build-a-deck)Use case

[Evaluate a company from the science to the balance sheet](/resources/use-cases/evaluate-a-company-from-the-science-to-the-balance-sheet)Evaluate a company from the science to the balance sheet

Evaluate a company from the science to the balance sheet

Use case

[Use case](/resources/use-cases/evaluate-a-company-from-the-science-to-the-balance-sheet)Use case

[Build analysis from browser charts and folder data](/resources/use-cases/build-analysis-from-browser-charts-and-folder-data)Build analysis from browser charts and folder data

Build analysis from browser charts and folder data

Use case

[Use case](/resources/use-cases/build-analysis-from-browser-charts-and-folder-data)Use case

[Build a daily briefing across your tools](/resources/use-cases/build-a-daily-briefing-across-your-tools)Build a daily briefing across your tools

Build a daily briefing across your tools

Use case

[Use case](/resources/use-cases/build-a-daily-briefing-across-your-tools)Use case
