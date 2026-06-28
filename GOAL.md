# Goal Plan Instructions

Long-running agent work that continues until a verifiable condition holds.
Start the loop with `/goal @GOAL.md`.

## Goal

Curate the lecture media catalog by visually reviewing image assets, reading their source document context, removing duplicate or useless entries, and replacing heuristic descriptions with context-grounded Korean one-line descriptions.

## Proof

Run from this worktree:

```bash
python3 tools/validate_curated_media_catalog.py --check
```

The check must pass only when `lecture-media/curated/images.tsv`, `lecture-media/curated/images.md`, `lecture-media/curated/assets/`, and `lecture-media/curated/semantic-review.tsv` exist; every original image row is classified as `keep`, `duplicate`, or `drop`; every kept canonical image has an actual inspected asset, a context-grounded Korean one-line description, source document context, and a non-generic visual note; duplicate rows point to a kept canonical row; dropped rows have a concrete drop reason; and a semantic review sample covers representative kept, duplicate, and dropped items.

## Acceptance Criteria

- The curated catalog is the usable deliverable: `lecture-media/curated/images.md` shows only kept canonical images, not every raw extraction row.
- Each kept canonical image has a Korean one-line description based on both visual inspection and the source document context, not generic text like "문서에 포함된 이미지" or filename-only guesses.
- Duplicate, placeholder, tracking, broken, tiny UI chrome, map control, repeated logo-only, and low-value decorative assets are excluded from the curated deliverable with an explicit reason in TSV.
- Visual review is done on image assets themselves, preferably by deduplicated visual clusters first; a cluster can be reviewed once only when all members are exact or near duplicates.
- Semantic quality gate: representative rows must show image preview/path, source context, decision, and rationale; generic keyword matches or alt-text-only explanations are not enough.

## Context

This branch starts from `goal/lecture-media-catalog` at commit `154543c`, which already created the raw lecture media extraction. Main `main` is unchanged and should stay clean.

Current raw input under `lecture-media/`:

- `lecture-media/images.tsv`: 8,175 image rows.
- Kinds: 3,293 `remote_ref`, 2,835 `pdf_image`, 1,479 `missing_local_ref`, 544 `local_file`, 24 `data_uri`.
- Assets: 6,694 rows currently have an asset path; 3,291 of 3,293 remote images downloaded; 2 remote failures are recorded.
- Asset footprint: about 921MB total, including PDF-extracted images, local copies, downloaded remote images, and data URI images.
- Existing descriptions are mostly heuristic from alt/title/source path. They are not acceptable as final lecture descriptions.

Generated mirror rules still apply: do not hand-edit generated domain files (`www.anthropic.com/`, `claude.com/`, `platform.claude.com/`, `support.claude.com/`, `anthropic.skilljar.com/`, `transformer-circuits.pub/`, `youtube.com/`). Use them as read-only source context.

## Scope

- Build the smallest curation pass needed on top of the existing raw catalog.
- Use exact hashes and simple perceptual/size checks to group exact and near-duplicate image assets before review.
- Visually inspect each kept visual cluster using local assets/contact sheets or individual image views.
- Read the source document context around each image occurrence before writing the kept image description.
- Produce a curated deliverable under `lecture-media/curated/`:
  - `images.tsv`: all original rows with decision metadata.
  - `images.md`: kept canonical images only, for browsing and lecture use.
  - `assets/`: copied kept canonical assets only.
  - `semantic-review.tsv`: representative reviewed rows with rationale and evidence.
- Add or update the minimal validation script needed for the Proof.

## Out of Scope

- Re-crawling Anthropic/Claude sites.
- Changing generated source Markdown or PDFs.
- Producing final slides, lecture script, or Korean full lesson material.
- Deleting the raw `lecture-media/assets/` extraction store in this run. The curated deliverable excludes bad/duplicate items; raw asset cleanup can be a later disk-space task.
- Using paid APIs or sending assets to external services without explicit approval.

## Constraints

- May touch `GOAL.md`, `progress.tsv`, `tools/`, and `lecture-media/curated/`. May read all existing mirror content and raw `lecture-media/`.
- Do not mutate or delete generated source directories.
- Prefer stdlib, existing `PIL`, and existing local files. No new dependencies unless there is no workable local path.
- Do not push. Do not force-push. Do not use `git reset --hard`.
- If a curation pass needs to delete raw assets rather than exclude them from `curated/`, stop and ask first.
- For image review, batch with contact sheets where useful, but do not mark a kept image complete without viewing the actual visual content or a contact sheet that clearly contains it.
- Descriptions should be concise Korean, grounded in source context, and avoid overclaiming beyond what the image and source document support.

## Input Stability

The input set is frozen to this worktree at branch start: raw catalog commit `154543c` plus the files present under `lecture-media/` in this branch. Do not re-run crawling or pull newer source data during the goal. If the raw generator is rerun, record the new input commit and restart coverage counts.

## Target Change Tracking

All target edits are committed in this git worktree on branch `goal/lecture-media-curation`. Each loop step commits `progress.tsv` plus any changed `tools/` or `lecture-media/curated/` artifacts.

## Bounds

Stop after a first proof-passing curated catalog. If a single visual-review batch takes more than 45 minutes, commit progress and continue with the next batch. If full visual review proves too large for one run, preserve completed clusters and report exact remaining counts rather than pretending completion.

## Curation Policy

- `keep`: visually meaningful and useful for explaining an Anthropic/Claude concept, product, workflow, research result, customer example, event, or safety/policy idea.
- `duplicate`: same or near-same visual content as another kept row; point to `canonical_key`.
- `drop`: placeholder, broken download, UI/control artifact, map marker/control, tracking badge, repeated logo-only decoration, tiny icon with no teaching value, visually unreadable crop, or asset whose source context gives no useful lecture concept.
- For logos/headshots/customer screenshots, keep only when the source context makes the image useful for a teaching point; otherwise drop as low-value decorative media.
- For PDF images, prefer figures/charts/diagrams/tables that support concepts; drop blank fragments, page furniture, tiny icons, and repeated branding.

## How Progress Is Tracked

- `progress.tsv` is the plan and progress table; the task breakdown lives in its rows. Edit it ONLY through the helper so rows never break on tab matching:
  `python3 /Users/seungwonan/.agents/skills/shared/goal-plan/scripts/goal_log.py <add|start|done|block|drop|set|show> ...` (flags: `<cmd> --help`).
- This plan lives on its own `goal/<tag>` branch (a worktree, or a dedicated goal repo). Each loop step ends in a commit, so the commit history is the durable record. `goal_log.py done` stamps the current `HEAD` as the row checkpoint; the commit you make immediately after records the row update. The checkpoint plus git history is your resume point: on resume, recover state with `pwd`, `goal_log.py show`, `git log`, then re-run the Proof.
- On a long run the context window fills and Claude Code auto-compacts old turns on its own; you do not run `/compact` yourself (it is an interactive command, not a turn action). What lets the loop survive compaction is externalized state: `progress.tsv` and git hold the plan and checkpoints, and the Proof output stays in the transcript, so you resume cleanly with `goal_log.py show` + `git log` after any compaction.

## Loop Protocol

Run as an autonomous loop until the Goal holds.

1. `goal_log.py show` to see where you are.
2. Take the next row (or `goal_log.py add --task ...`), then `goal_log.py start <id>`. Pick the row most likely to advance the Goal or unblock the rest, not just the next in line.
3. Do the work within Scope and Constraints, then run the Proof.
4. `goal_log.py done <id> --decision keep|discard|crash --artifact "<proof>"` (keep if it advanced the goal; discard if it did not but did no harm; crash if it caused a regression). Be skeptical of your own success -- if the Proof passed quietly, rerun it before marking done. Every done row needs artifact or notes evidence; for discard/crash, put WHY it failed and what to try instead in notes so a later session does not repeat the dead end.
5. Commit the changed files plus `progress.tsv`: `git add <files> progress.tsv && git commit -m "<keep|discard>: <what you did>"`. If target code changes live outside this repo, also commit the target repo or commit patch/snapshot artifacts here, according to Target Change Tracking.
6. Surface the Proof in your reply as evidence, not a claim: paste the actual command output (pass/fail, line numbers, exact errors), then name the checkpoint, what you verified this step, what remains, and whether you are blocked. The `/goal` evaluator reads the conversation, not the files.
7. To undo a change that made things worse, revert with git, sparingly. Do not `git reset` away failed attempts you have already committed -- the commit log is the full record, including discards.

Do not ask "should I continue?" once the loop starts. Stop only when the Goal holds, when you hit a Bound, or when blocked by missing access, destructive risk, or an explicit user choice -- when blocked, report what specific input or access would unblock you. Budget or turn exhaustion is not completion.

## Completion

Complete only when the Goal holds and is shown with the Proof output in the conversation or logs, and required rows in `progress.tsv` are `done` or intentionally `dropped`.
