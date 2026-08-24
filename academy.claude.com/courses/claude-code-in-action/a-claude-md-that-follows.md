<!-- source: https://academy.claude.com/courses/claude-code-in-action/a-claude-md-that-follows -->

Lesson 2 of 9 · Claude Code in ActionA CLAUDE.md that follows

Loading

A CLAUDE.md that follows

Here's a trap that catches almost everyone: your CLAUDE.md file keeps
growing. You hit a problem, you add a rule. You hit another, you add another
rule. Before long you've got one giant file, and Claude starts ignoring
parts of it. That's not a bug in Claude. It's how the file works.

The key thing to understand is that CLAUDE.md is not enforced configuration.
It's guidance. Every line competes with every other line for Claude's
attention. The longer the file gets, the more it competes with itself, and
the less reliably Claude follows any single rule. So the goal isn't to write
down everything. The goal is to keep the file tight. The leaner the file,
the more of it Claude actually follows.

## First, ask if CLAUDE.md is even the right tool

Before you write a rule, ask whether it belongs in CLAUDE.md at all. Some rules are guidance, and some rules are hard lines that must never be crossed. Those are two different jobs.

Take a rule like "never push to main." If you put that in CLAUDE.md, you're hoping Claude reads it and respects it. Most of the time it will. But "most of the time" isn't good enough for something that dangerous. A hard rule like that belongs in a pre-tool-use hook instead.

The difference matters. A hook is code that runs before Claude takes an action, and it can actually block the action. So even if Claude does try to push to main, the hook stops it. That's real enforcement, not a polite request. Move your hard rules to hooks and let CLAUDE.md handle the softer conventions.

## The four locations

CLAUDE.md isn't just one file sitting in your project. There are four places it can live, and Claude loads all of them together at launch. Nothing gets dropped, and they stack.

Here's what each one is for:

* **Managed policy** — the org-level file your platform team controls. You can't exclude it, so org policy is always in play.
* **User** — your personal preferences that follow you across every project on your machine.
* **Project** — the file shared with your team, checked into the repo.
* **Local** — ignored by git. Your personal notes for this one repository only.

That last one, local, is easy to overlook but really handy. Say you're refactoring off in your own branch and you want Claude to hold some architectural decisions in mind while you work. That doesn't belong in the shared project file where it'd affect your whole team. It goes in local, where it's just yours for this repo.

## Split up a big file with imports

When your project file starts getting long, you can break it into pieces using the path-to-file import syntax. Instead of one wall of text, you point to other files:

```
@.claude/conventions/code-style.md
@.claude/conventions/testing.md
@.claude/conventions/workflow.md
```



This is great for organizing. But know exactly what it buys you, because it's easy to get the wrong idea. When Claude launches, it expands those imported files inline, right where you referenced them. So imports help you keep things tidy, but everything still loads up front. They do not reduce the amount of context Claude has to read. Use imports to organize, not to shrink the load.

## Phrasing is what makes rules stick

Once you've decided a rule belongs in CLAUDE.md, whether Claude actually obeys it comes down to how you phrase it. Most rules fail because they're vague. Here's how to fix that.

### Be specific and checkable

Don't write "follow best practices." Do you even know exactly what that means? If you can't check whether it was followed, neither can Claude. Compare these two:

* Vague: *"Follow best practices for API routes."*
* Specific: *"Put new API routes in `src/api/handlers`, one per file."*

The second one is explicit. You can look at the result and immediately tell if it was done right. That's the bar every rule should clear.

### Name the replacement, don't just ban something

When you tell Claude not to do something, say what to do instead. Otherwise you've left the door open.

* Leaves it open: *"Don't use default exports."* Okay, but then what?
* Closes it: *"Use named exports, not default exports."*

The second version names the replacement, so there's nothing left to misinterpret.

### Emphasis is a budget

Words like "IMPORTANT" and "YOU MUST" do raise a rule's priority. But only relative to everything quieter around it. If every rule shouts, then nothing stands out and the emphasis means nothing. So treat emphasis like a budget. Spend it on the two or three rules that really hurt when they get broken, and let the rest sit at normal volume.

## Keep the file under revision

Your CLAUDE.md file is never finished. Treat it like living code that keeps getting edited.

When Claude does the wrong thing, don't just sigh and fix it by hand. Treat it as a bug report against your CLAUDE.md file. You can even tell Claude directly: "add that to the CLAUDE.md file," and it'll write the rule for you. That way the file gets better every time something goes wrong.

## The bottom line

Treat your CLAUDE.md like production code. If you can't justify a line, delete it. To keep the file lean and followable:

1. Move hard rules to hooks, where they're actually enforced.
2. Organize long files with imports (just remember they don't reduce context).
3. Make every rule specific and checkable, and name the replacement.
4. Spend your emphasis budget on the few rules that matter most.
5. Keep revising the file whenever Claude gets something wrong.

The whole idea is simple. The leaner the file, the more of it Claude follows.
