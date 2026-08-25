<!-- source: https://platform.claude.com/cookbook/managed-agents-cma-use-skills-from-a-repo -->

#  Skills: pick up a repo's `.claude/skills` automatically

A team that already writes skills for Claude Code keeps them in the repository, under `.claude/skills/<skill-name>/SKILL.md`, versioned next to the code they describe. Uploading each of those to the Skills API and pinning versions on every agent duplicates that work and drifts the moment someone edits the repo.

When a session mounts a GitHub repository, the harness scans the repository's root `.claude/skills/` directory at session start and injects every skill it finds into the agent's system prompt: the skill's name, its description, and its path inside the sandbox. The model reads a skill's `SKILL.md` with the built-in `read` tool the moment a request matches the skill's description, then follows it, including any scripts or reference files the skill ships. No upload, no `skills` field on the agent, no version bookkeeping. The skill you get is the one on the branch you checked out.

This notebook walks through:

* the on-disk layout the scanner expects
* mounting a repository so its skills are discovered
* confirming discovery and watching the read-then-follow protocol
* where the boundaries are: layout rules, the skill cap, and mid-session changes

##  1. Set up the client

You'll need `GITHUB_TOKEN` in your environment. A fine-grained personal access token with public-repo read access is enough, because the repository this notebook mounts is public. Repository skills are discovered only on Anthropic-hosted environments (`anthropic_cloud`). Self-hosted sandboxes don't clone GitHub repositories, so the feature is out of scope there.

%%capture

%pip install -qU "anthropic>=0.121.0" python-dotenv

import os

import anthropic

from dotenv import load\_dotenv

load\_dotenv()

BETAS = ["managed-agents-2026-04-01"]

MODEL = os.environ.get("COOKBOOK\_MODEL", "claude-sonnet-5")

GH\_TOKEN = os.environ.get("GITHUB\_TOKEN")

if not GH\_TOKEN:

raise SystemExit(

"Set GITHUB\_TOKEN in your environment (a fine-grained PAT with public-repo read)."

)

client = anthropic.Anthropic()

##  2. The layout the scanner looks for

Skills are discovered from one place: `.claude/skills/` at the repository root, one directory per skill, each with a `SKILL.md` at its top level. The same convention Claude Code uses.

your-repo/

└── .claude/

└── skills/

├── cookbook-audit/

│ ├── SKILL.md <- name + description frontmatter, then instructions

│ ├── style\_guide.md <- reference file the instructions point at

│ └── validate\_notebook.py <- script the instructions run

└── another-skill/

└── SKILL.md

`SKILL.md` opens with YAML frontmatter carrying `name` and `description`. The description is what the model matches against when deciding whether to open the file, so it should read like a trigger: what the skill does and when to reach for it.

---

name: cookbook-audit

description: Audit an Anthropic Cookbook notebook based on a rubric. Use whenever a notebook review or audit is requested.

---

# Cookbook Audit

...

The public `anthropics/claude-cookbooks` repository ships exactly this skill, with a scoring rubric in `style_guide.md` and a `validate_notebook.py` script. Mounting that repository gets you a skill with instructions, a reference file, and a runnable script in one go.

##  3. Create an agent with no skills attached

Nothing about the agent references skills. It gets the standard toolset and a general-purpose prompt. The skills arrive with the repository, not with the agent definition.

env = client.beta.environments.create(

name="repo-skills-demo",

config={"type": "anthropic\_cloud", "networking": {"type": "unrestricted"}},

betas=BETAS,

)

reviewer = client.beta.agents.create(

name="cookbook\_reviewer",

description="Reviews notebooks in a mounted cookbook repository.",

model={"id": MODEL},

system="You review notebooks in the repository mounted under /workspace. "

"When the repository provides a process for a task, follow it.",

tools=[{"type": "agent\_toolset\_20260401"}],

betas=BETAS,

)

print(f"{reviewer.name}: {reviewer.id} v{reviewer.version}")

##  4. Mount the repository

The `github_repository` resource clones the repo into the container at session start. `url` is the plain `https://github.com/{owner}/{repo}` form (no `.git` suffix, no SSH form). `checkout` pins a branch or a commit and `mount_path` overrides the default `/workspace/<repo-name>`. Skill discovery follows the checked-out ref, so a branch with different skills yields different skills.

session = client.beta.sessions.create(

agent=reviewer.id,

environment\_id=env.id,

title="Cookbook audit",

resources=[

{

"type": "github\_repository",

"url": "https://github.com/anthropics/claude-cookbooks",

"authorization\_token": GH\_TOKEN,

"checkout": {"type": "branch", "name": "main"},

# mount\_path defaults to /workspace/claude-cookbooks

}

],

betas=BETAS,

)

print(session.id, session.status)

##  5. Ask the agent what skills it has

Discovery already happened when the session started, so this question needs no file exploration to answer. The agent names `cookbook-audit` and the path of its `SKILL.md` straight from its system prompt.

from utilities import stream\_until\_end\_turn

client.beta.sessions.events.send(

session.id,

events=[

{

"type": "user.message",

"content": [{"type": "text", "text": "What skills are available to you in this repo?"}],

}

],

betas=BETAS,

)

stream\_until\_end\_turn(client, session.id)

##  6. Trigger the skill without naming it

The point of the description is that the model routes on intent. This request never says "skill" or "cookbook-audit". It asks for the outcome the skill produces.

Watch the tool events. The first `read` in the turn opens the skill's `SKILL.md`. The agent then follows what the skill tells it to do: read `style_guide.md`, run `validate_notebook.py`, and score against the rubric, rather than inventing an audit process of its own.

client.beta.sessions.events.send(

session.id,

events=[

{

"type": "user.message",

"content": [

{

"type": "text",

"text": "Do a notebook audit of "

"managed\_agents/CMA\_iterate\_fix\_failing\_tests.ipynb "

"against the cookbook style guide, and give me the score.",

}

],

}

],

betas=BETAS,

)

with client.beta.sessions.events.stream(session.id, betas=BETAS) as stream:

for ev in stream:

if ev.type == "agent.tool\_use":

target = ev.input.get("file\_path") or ev.input.get("command") or ""

print(f"[{ev.name}] {str(target)[:100]}")

elif ev.type == "agent.message":

print("".join(b.text for b in ev.content if b.type == "text"), end="")

elif ev.type == "session.status\_idle":

print(f"\n[idle] stop\_reason={ev.stop\_reason.type}")

break

Pull out the `read` calls to see the protocol on its own: the skill's `SKILL.md` first, then the reference and script the skill ships, then whatever repository files the work touches.

reads = [

ev.input.get("file\_path")

for ev in client.beta.sessions.events.list(session.id, limit=1000, betas=BETAS)

if ev.type == "agent.tool\_use" and ev.name == "read"

]

for path in reads:

print(path)

##  7. The rules the scanner enforces

**Layout is strict.** Only `.claude/skills/<name>/SKILL.md` at the repository root is announced at session start. A bare `.claude/skills/SKILL.md` with no subdirectory, a doubly nested `.claude/skills/a/b/SKILL.md`, and a `skills/<name>/SKILL.md` missing the `.claude` parent are all ignored.

**Frontmatter is lenient.** A `SKILL.md` with no frontmatter is still announced, with the directory name as its name and an empty description. A long description is flattened to one line and truncated past 2,000 characters. CRLF line endings parse fine.

**There is a cap.** The first 64 skill directories are announced. Directories past that are dropped without an error, so a repository with a large skill library should keep the ones sessions rely on early and few.

**The scan runs once.** Discovery happens at session start and is persisted for that session. Pushing a new skill to the repository mid-session does nothing for the running session. The next session created against that repository sees it.

**Nested skills are found lazily.** A repository with `packages/foo/.claude/skills/lint/SKILL.md` and no root-level skills announces nothing at start. Once the agent reads a file under `packages/foo/` with the built-in `read` tool, the harness notices the nested `.claude/skills/` directory and surfaces `lint` for the rest of the session. Reading the same file through `bash` (`cat`) does not trigger it. Only the `read` tool does.

##  8. Repository skills next to the Skills API

Both mechanisms coexist on one session, and both kinds of skill show up in the agent's list.

Use repository skills when the skill belongs with the code: build and test conventions, review checklists, deploy runbooks, anything you'd want a pull request to change together with the source. Whoever clones the repo, human or agent, gets the same instructions.

Use the [Skills API(opens in new tab)](https://platform.claude.com/docs/en/managed-agents/skills) (`skills=[{"type": "custom", "skill_id": ...}]` on the agent) when the skill is an organization-wide asset that spans repositories, needs its own versioning independent of any codebase, or has to be available in sessions that mount no repository at all.

A name collision between the two is allowed: a repository `verify` skill and an org `verify` skill both appear, at different paths, and the model picks based on the request. If two mounted repositories both ship a same-named skill, both are announced with their distinct mount paths.

##  9. Clean up

from utilities import wait\_for\_idle\_status

wait\_for\_idle\_status(client, session.id)

client.beta.sessions.archive(session.id, betas=BETAS)

client.beta.environments.archive(env.id, betas=BETAS)

print("archived")
