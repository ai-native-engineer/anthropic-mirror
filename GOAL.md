# Goal Plan Instructions

Long-running agent work that continues until a verifiable condition holds.
Start the loop with `/goal @GOAL.md`.

## Goal

Extract every image-bearing asset from the Anthropic mirror into a reusable lecture media catalog with copied assets, one-line descriptions, source links, and simple concept YouTube recommendations.

## Proof

Run:

```bash
python3 tools/build_lecture_media_catalog.py --check
```

The check passes only when `lecture-media/images.tsv`, `lecture-media/images.md`, `lecture-media/youtube.tsv`, and `lecture-media/youtube.md` exist, every detected source image reference or local image file has a catalog row, every catalog row has a one-line description and source pointer, and every recommended concept video points to an existing mirrored YouTube entry or source URL.

## Context

This repository is a generated Anthropic/Claude mirror. Domain directories such as `www.anthropic.com/`, `claude.com/`, `platform.claude.com/`, `support.claude.com/`, `anthropic.skilljar.com/`, `transformer-circuits.pub/`, and `youtube.com/` are generated archive content and must not be hand-edited. Fix generators only when changing crawl behavior; this goal is downstream extraction, so generated content is read-only input.

Observed baseline from the repo root on 2026-06-28:

- 5,287 Markdown files.
- 544 local image files: 542 under `transformer-circuits.pub/`, 2 under `assets/`.
- Markdown contains many remote image references and YouTube references; previous mirror work established that repo-wide video checks should not use a tiny `rg --max-filesize` cap.
- `pdfimages` is installed, `PIL` is available, and Python `fitz`/`pypdf` are not installed. Use existing tools before adding dependencies.

Relevant repo rules: read `AGENTS.md` before editing; keep `README.md` and `README.ko.md` in sync only if changing README; do not push without explicit user approval.

## Scope

- Build a reusable extraction/catalog layer under `lecture-media/`.
- Inventory all local image files and all Markdown image references, including remote URLs.
- Copy local image files into `lecture-media/assets/` with stable names; download remote image URLs only if needed for the catalog and only into `lecture-media/assets/remote/`.
- Generate `images.tsv` for machine use and `images.md` for lecture-material browsing: image preview/path, one-line Korean description, source document, source URL when available, and topic hints.
- Generate `youtube.tsv` and `youtube.md` with simple concept-explanation videos drawn from mirrored official YouTube/channel pages and embedded transcripts where available.
- Include PDF-bearing source documents in the inventory and use `pdfimages` for PDF image extraction when it works without adding new dependencies.
- Add the smallest verification script/check needed to prove catalog coverage.

## Out of Scope

- Hand-editing generated Markdown under domain directories.
- Re-crawling Anthropic/Claude pages unless extraction reveals missing generated data.
- Publishing or pushing changes to the public repo.
- Producing final slide decks or rewriting lesson text.
- Adding new Python packages unless the existing CLI/stdlib path cannot satisfy PDF/image extraction.

## Constraints

- May touch only `GOAL.md`, `progress.tsv`, `tools/`, and `lecture-media/` unless a repo rule or generator bug requires otherwise.
- Treat existing domain directories as read-only input.
- Use `rg`, Python stdlib, existing shell tools, `pdfimages`, and `PIL` before considering anything else.
- Network downloads of remote image URLs are allowed only for public source URLs already present in the mirror and only into `lecture-media/`; record failures instead of retrying forever.
- No `git reset --hard`, no force-push, no deletion outside this goal branch.
- End each meaningful step with `goal_log.py done ...` and a git commit.

## Bounds

Stop after a first complete, check-passing catalog pass. For slow media work, cap a single extraction/download step at 30 minutes; record skipped/failing assets in the TSV and keep the loop moving.

## Acceptance Criteria

- `lecture-media/images.md` lets a human browse extracted images with one-line Korean descriptions and source pointers.
- `lecture-media/images.tsv` has one row per detected local image file or Markdown image reference, with no blank description/source fields.
- `lecture-media/youtube.md` lists concise official Anthropic/Claude concept videos suitable for lecture inserts, with one-line Korean explanations.
- `python3 tools/build_lecture_media_catalog.py --check` reports counts and exits 0.

## How Progress Is Tracked

- `progress.tsv` is the plan and progress table; the task breakdown lives in its rows. Edit it ONLY through the helper so rows never break on tab matching:
  `python3 /Users/seungwonan/.agents/skills/shared/goal-plan/scripts/goal_log.py <add|start|done|block|drop|set|show> ...` (flags: `<cmd> --help`).
- This plan lives on its own `goal/<tag>` branch (a worktree, or a dedicated goal repo). Each loop step ends in a commit, so the commit history is the durable record. `goal_log.py done` stamps the current `HEAD` as the row checkpoint; the commit you make immediately after records the row update. The checkpoint plus git history is your resume point: on resume, recover state with `pwd`, `goal_log.py show`, `git log`, then re-run the Proof.
- On a long run, watch the context window and compact old turns when it fills, keeping the Proof output and `progress.tsv` intact (in Claude Code, `/context` to check and `/compact` to summarize); repeated compaction lets the loop run for many more hours.

## Loop Protocol

Run as an autonomous loop until the Goal holds.

1. `goal_log.py show` to see where you are.
2. Take the next row (or `goal_log.py add --task ...`), then `goal_log.py start <id>`. Pick the row most likely to advance the Goal or unblock the rest, not just the next in line.
3. Do the work within Scope and Constraints, then run the Proof.
4. `goal_log.py done <id> --decision keep|discard|crash --artifact "<proof>"` (keep if it advanced the goal; discard if it did not but did no harm; crash if it caused a regression). Be skeptical of your own success -- if the Proof passed quietly, rerun it before marking done. Every done row needs artifact or notes evidence; for discard/crash, put WHY it failed and what to try instead in notes so a later session does not repeat the dead end.
5. Commit the changed files plus `progress.tsv`: `git add <files> progress.tsv && git commit -m "<keep|discard>: <what you did>"`.
6. Surface the Proof in your reply as evidence, not a claim: paste the actual command output (pass/fail, line numbers, exact errors), then name the checkpoint, what you verified this step, what remains, and whether you are blocked. The `/goal` evaluator reads the conversation, not the files.
7. To undo a change that made things worse, revert with git, sparingly. Do not `git reset` away failed attempts you have already committed -- the commit log is the full record, including discards.

Do not ask "should I continue?" once the loop starts. Stop only when the Goal holds, when you hit a Bound, or when blocked by missing access, destructive risk, or an explicit user choice -- when blocked, report what specific input or access would unblock you. Budget or turn exhaustion is not completion.

## Completion

Complete only when the Goal holds and is shown with the Proof output in the conversation or logs, and required rows in `progress.tsv` are `done` or intentionally `dropped`.
