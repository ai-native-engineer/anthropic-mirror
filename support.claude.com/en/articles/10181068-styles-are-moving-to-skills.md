<!-- source: https://support.claude.com/en/articles/10181068-styles-are-moving-to-skills -->

# Styles are moving to skills

Updated over 3 weeks ago

Styles in Claude are becoming skills. This article explains what's changing, how your existing styles will be handled, and what to do if you used one of the default styles.

## What's changing

**Your custom styles will become skills.** Any custom styles you've created will be migrated to skills automatically. After the migration runs, your styles will be available as skills in your account. These skills will be disabled by default, so go to **[Customize > Skills](http://claude.ai/customize/skills)** to enable any of the migrated styles you want to use.

**Most default styles are being removed.** The Concise, Explanatory, and Formal default styles will no longer be available after the migration. The Learning style is being preserved as a skill (see **[The Learning skill](#h_87710ea950)** below).

**The styles menu will be removed.** Once the migration is complete, the styles menu will no longer appear in Claude. Until that point, your existing styles remain available alongside the new skills, so you can switch over at your own pace.

## Using your migrated style

To activate one of your migrated styles in a conversation, type a slash command in the chat input using this format: `/{style-name}-style`

When your custom styles are migrated to skills, the style names are automatically converted into commands by:

* Switching letters to lowercase
* Replacing spaces with hyphens
* Removing punctuation, emoji, and accent marks
* Adding -style to the end

If the resulting command runs past the length limit, it's trimmed. If two of your styles would otherwise produce the same command, a number will be added to one of them.

For example, if you had a custom style named “concise pirate,” you'd type "/concise-pirate-style" to apply it.

## The Learning skill

Learning, formerly a default style, is now available as a skill. To use it, add the Learning skill from the skills marketplace and activate it in any conversation.

1. Navigate to **[Customize > Skills](http://claude.ai/customize/skills)**.
2. Click the “+” button to add a skill.
3. Select “Browse skills” to open the directory.
4. Search for the “Learning” skill.
5. Click “+” or “Install” to add it.

## Update your instructions instead

If you'd rather not use skills, you can describe the same response behavior in your instructions for Claude. Instructions apply to all your conversations and can describe the same tone, format, and approach guidance you would have set with a style.

Learn more about **[Claude's personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)**.

[What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)[Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)[How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)[Browse skills, connectors, and plugins in one directory](https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory)[Claude Code power user tips](https://support.claude.com/en/articles/14554000-claude-code-power-user-tips)
