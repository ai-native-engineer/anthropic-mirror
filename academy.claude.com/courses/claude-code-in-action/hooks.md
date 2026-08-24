<!-- source: https://academy.claude.com/courses/claude-code-in-action/hooks -->

Lesson 5 of 9 · Claude Code in ActionHooks

Loading

Hooks

Here's the problem with telling Claude to do something in a CLAUDE.md file:
it's a request, not a guarantee. You can write "always format after
editing" and Claude will usually listen. Usually. But on a long run you're
not watching, "usually" isn't good enough. A hook fixes that. A hook is
deterministic code that runs at a fixed point in the loop, so it can
guarantee behavior instead of hoping for it. It turns a rule from "Claude
usually listens" into "Claude can't skip it."

That's the whole pitch. Now let's look at how it actually works.

## The hook events

Claude Code fires around 30 hook events over the course of a session. You don't need to know all of them. There's a small handful you'll reach for again and again, and they line up with points in the agentic loop where you'd want to step in.

Here's how they sit in the loop. A session starts, prompts come in, tools get called, and the turn eventually ends. Each of those moments has a hook you can hang code on.

The ones worth knowing:

* **PreToolUse** fires before a tool call. This is your enforcement primitive. It's the one that can stop something before it happens.
* **PostToolUse** fires after a successful tool call. This is usually where auto-formatting or an auto-lint goes.
* **Stop** fires when Claude wants to end its turn. You can refuse and say "no, you're not done yet" if some condition isn't met. There's a matching **SubagentStop** for when a sub-agent finishes.
* **PreCompact** and **PostCompact** fire before and after compaction.
* **InstructionsLoaded** fires when a CLAUDE.md or rule file loads. Handy for auditing what actually made it into context.
* **SessionStart** fires at the start and primes the environment. Use the `startup` source if you only want it on fresh starts.

One thing that trips people up: to re-inject context after compaction, don't use PostCompact. Use SessionStart with the `compact` matcher. That's the one that actually gets its output back into the conversation.

## PreToolUse: returning a decision as JSON

PreToolUse is where the real power is, because it can block a tool call before it runs. The way you talk back to Claude is by printing JSON and exiting zero. The key field is `permissionDecision`, and it takes one of three values:

* `allow` — let the call through
* `deny` — stop the call
* `ask` — hand it back to the user to decide

There's technically a fourth value, `defer`, but it only applies to non-interactive `-p` runs where a calling process pauses the tool and resumes it later. You'll rarely reach for it.

The shape looks like this:

json

```
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "...",
    "updatedInput": {
      "command": "..."
    }
  }
}
```

Notice `updatedInput`. Instead of blocking a call, you can rewrite it. That's how you'd redact a secret out of a bash command and still let it run. One catch: `updatedInput` replaces the *whole* input object, so you have to echo back the fields you aren't changing, or you'll lose them.

## Exit codes, for hooks that don't return JSON

Not every hook needs to speak JSON. For simpler hooks, exit codes do the job. There are three numbers that matter.

* **0 is success.** If standard out is JSON, Claude parses it. Plain text is ignored on most events, but on SessionStart, UserPromptSubmit, and UserPromptExpansion, plain text gets added to context. That's exactly what makes a state-preserver hook work.
* **2 is a blocking error.** Standard error gets fed back to Claude as context. This is the blocking exit code almost everywhere.
* **Anything else** is non-blocking. Standard error gets logged, and Claude carries on.

The one that catches people out is exit code 1. It *feels* like an error, but it does not block. Claude runs the command anyway. So if you meant to stop something, exit 2, not 1.

A couple more wrinkles. Exit 2 can even block Stop, which is how you tell Claude it's not done. But PostToolUse fires after the tool already ran, so blocking there is too late to stop the call, though it can still feed text back to Claude. And a few events ignore blocking entirely, like Notification and SessionStart. They'll show your standard error and carry on regardless.

## A real guardrail: redact instead of block

Let's tie it together with something practical. Say you want a PreToolUse guardrail on the Bash tool. The matcher picks the tool to watch, and an optional `if` clause can narrow it to a specific command.

The obvious move is to return `deny` and stop a dangerous call. That's good. But the lesser-known and more interesting move is to return `updatedInput` to rewrite the call. That's how you strip a secret out of a command and still let it run, instead of just refusing.

Here's what that looks like in practice. Claude is asked to run a command that includes a live-looking secret. The hook intercepts it, spots the `sk_live_` pattern, and swaps it for a placeholder before the command ever executes.

The command still ran. The work still got done. But the secret never made it through. That's the difference between blocking and redacting, and it's the kind of thing a hook can enforce every single time.

## Preserving state across a compact

One more pattern worth setting up. When Claude compacts a long conversation, it drops a lot of detail. A SessionStart hook with the `compact` matcher runs right after compaction. Have it print a short summary of the files you've been working on. That summary goes back into context, so Claude picks up where it left off instead of starting cold.

## Wrapping up

Hooks turn a rule Claude usually follows into one it always follows. Reach past auto-formatting: guard tools with PreToolUse, gate the turn with Stop, and preserve state across a compact. The setup takes a little effort up front, but it pays back the first time it catches something on a run you weren't even watching.
