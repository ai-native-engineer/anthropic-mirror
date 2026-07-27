<!-- https://anthropic.skilljar.com/claude-code-101/469794 -->

### Video



### Code Review

Claude Code has a few built-in features that make your git workflow faster. Let's go through them.

## Review with a Subagent

Before you push a PR, ask Claude to use a **subagent** to review your changes. The subagent runs in its own context window with fresh eyes — it doesn't carry the bias of the main agent that just spent the session writing the code.

When creating a code-reviewer subagent, restrict it to read-only tools. A reviewer should flag issues, not edit files. Check the subagent configuration into your repo so your whole team uses the same reviewer.

## The /commit-push-pr Skill

The `/commit-push-pr` skill handles the commit, push, and PR creation all in one step. Instead of doing each manually, just run the skill and Claude takes care of it.

If you have a Slack MCP server configured with channels listed in your CLAUDE.md, it will automatically post the PR link to your team's channel.

## Session Linking with --from-pr

When Claude creates a PR through `gh pr create`, the session gets linked to that PR automatically. If you need to come back to it later — maybe to address review comments or fix a failing build — run:

```
claude --from-pr <PR_NUMBER>
```

This picks up right where you left off.

## Recap

Use a subagent for an unbiased code review before pushing. Use `/commit-push-pr` to handle the full commit-to-PR flow in one step. And use `--from-pr` to resume work on a PR later. These are small features, but they remove a lot of friction from your daily workflow.

<!-- yt-pending: RKsADl0ZC3Y -->

_(영상 자막 없음 또는 추출 실패)_
