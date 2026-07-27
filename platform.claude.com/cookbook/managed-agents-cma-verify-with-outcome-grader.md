<!-- source: https://platform.claude.com/cookbook/managed-agents-cma-verify-with-outcome-grader -->

# Outcomes: agents that verify their own work

Agents are good at producing things that *look* done. Ask one for a cited research brief and you'll get a tidy document with footnotes. Look closer and there's usually room to improve: a topic gets thin coverage, a quote drifts from the source, a citation leans on a press release instead of the original filing. Catching those takes a manual review loop: you read the output, spot what's off, and prompt again. And most of what you say in those rounds is feedback you could have written down before the agent started.

[Outcomes](https://platform.claude.com/docs/en/managed-agents/define-outcomes) in Claude Managed Agents gives the session a second agent whose only job is to check. You write a **rubric** that spells out what "done" looks like and how to verify it, and the platform provisions a **grader** in its own context window. The grader can't see the writer's reasoning and has no idea what shortcuts were taken. After each writer turn it rereads the artifact against the rubric and either passes it or hands back a per-criterion list of gaps. The writer revises and the loop runs again, up to a cap you set.

In this guide you'll watch that loop run end to end. The writer drafts a one-page brief on EV fast-charging economics with verbatim quotes from its sources. The grader independently fetches every cited URL, searches each page for the quoted string, checks the quote actually supports the claim, and scores coverage against a seven-item checklist. You'll see it catch a real problem (a press-release exhibit cited where a 10-K was required) and you'll see the writer go find the right document.

## What you'll learn

* Write a rubric the grader can act on
* Start a session with an Outcome and let the agent work toward it
* Follow the grade-and-revise loop and read the grader's feedback
* Recognize when Outcomes is the right tool

## 1. Set up the environment

First, let's install the SDK and set up the Anthropic client. The `define_outcome` event and the outcome-evaluation span types are part of the Managed Agents beta.

python

```
%%capture
%pip install -q anthropic python-dotenv
```

python

```
import os
import re
import time

import anthropic
from dotenv import load_dotenv

load_dotenv()

BETAS = ["managed-agents-2026-04-01"]
MODEL = os.environ.get("COOKBOOK_MODEL", "claude-sonnet-4-6")
client = anthropic.Anthropic()
```

## 2. Create the writer and start a session

Next, we'll create the writer agent and open a session. The writer's system prompt asks it to cite no more than six sources, each with a short verbatim quote so the grader has something concrete to check.

python

```
env = client.beta.environments.create(
    name="research-brief",
    config={"type": "anthropic_cloud", "networking": {"type": "unrestricted"}},
)

writer = client.beta.agents.create(
    name="Research Analyst",
    model=MODEL,
    system="""You are a research analyst. You write one-page business briefs.

Cite every factual claim with an inline footnote [n]. End the brief with a Sources section in this exact format, one entry per line:

[n] "verbatim quote from the page, 25 words or fewer" - Title - URL

Only cite pages you actually fetched and read. The quote must be copied character-for-character from the page. Cite no more than 6 sources total. Pick the strongest; do not pad. Save the brief to /mnt/session/outputs/brief.md.""",
    tools=[
        {
            "type": "agent_toolset_20260401",
            "configs": [
                {"name": "web_search"},
                {"name": "web_fetch"},
                {"name": "read"},
                {"name": "write"},
            ],
        }
    ],
    betas=BETAS,
)

session = client.beta.sessions.create(
    agent={"type": "agent", "id": writer.id, "version": writer.version},
    environment_id=env.id,
    title="Brief: EV fast-charging unit economics",
    betas=BETAS,
)
print(f"Session {session.id}")
```

```
Session sesn_011CakRYQjc4NMXdRy4qKZy5
```

## 3. Write a rubric the grader can act on

The `define_outcome` event hands the session two things: a **description** of the deliverable, which the writer reads, and a **rubric**, which the grader reads. After each writer turn the platform spins up a fresh grader with the same model and tools as the writer, gives it the rubric, and lets it inspect the artifact. The grader returns a per-criterion verdict, and if anything fails, the explanation goes straight back to the writer for the next revision.

The rubric is the only lever you have on the grader, and how it's worded determines whether the grader actually checks anything. The default failure mode is a grader that approves everything. A rubric that says *"check that the brief covers demand charges"* lets the grader skim the brief, see a paragraph about demand charges, and write a sentence confirming it's there. It can do all of that without opening a single source. Most first drafts pass on that basis and the loop never runs. A rubric that says *"open the brief, find the demand-charges section, and confirm it states a $/kW figure or a % of operating cost"* forces the grader to produce evidence. That grader is the one that catches a press release masquerading as a 10-K.

A few things worth doing in every rubric:

| Principle | In practice |
| --- | --- |
| **Make each criterion checkable** | The task says "named-operator economics." The rubric pins it down: GAAP net loss from a 10-K or 10-Q, cited to the filing on `sec.gov`. The rubric should always be more specific than the task. |
| **Make the grader earn `satisfied`** | Require concrete evidence (a fetched page, a traced formula, a `file:line` reference) before the grader passes anything. A grader that's too strict costs you an extra loop. One that's too lenient ends the loop with the bad version still in place. |
| **Describe the goal, not the steps** | A rubric that prescribes a specific command fails silently when it isn't available, and the check you cared about never runs. Define what counts as proof; the grader has the writer's full toolset and can find it. |
| **Anticipate the writer's shortcuts** | "Do NOT corroborate via mirrors, reposts, or search snippets." Without that line, a dead source gets swapped for a scraper page and the grader passes it. |
| **Mandate the feedback format** | The grader's explanation is the writer's only signal. Ask for a one-line scoreboard, then one bullet per failure with what's wrong and what to do. |
| **Tell the grader what to ignore** | Without a no-fire list, the grader thrashes on style nits, pre-existing issues, and scope creep. Spell out what's out of bounds and have it self-check each finding before raising it. |

> **Don't have a rubric yet?** Hand Claude a known-good example of the artifact and ask it to analyze what makes it good, then turn that analysis into criteria. That middle ground reliably beats writing criteria from a blank page.

Here's the task and rubric for our brief. Read them side by side and notice how much more specific the rubric is. Each place it adds detail the task didn't have is a check the grader can actually run.

python

```
TASK = """Write a brief on the unit economics of public DC fast charging in the United States.
The brief should cover:
  1. Capex range
  2. Demand charges
  3. Utilization breakeven
  4. Subsidy programs
  5. Named-operator economics
  6. A contrarian or skeptical source
  7. Hardware vs install cost split
"""

RUBRIC = """
You are reviewing a research brief at /mnt/session/outputs/brief.md against a coverage checklist and verifying its citations. The writer was told the seven topics to cover; this rubric defines what counts as sufficient coverage for each topic, and how to verify citations.

COVERAGE CHECKLIST. Each item has a specific area:
  1. Capex range: a dollar range for installed cost per DC fast-charging stall or station.
  2. Demand charges: quantified impact on opex (a $/kW figure or a % of operating cost).
  3. Utilization breakeven: a breakeven or target utilization threshold (% or kWh/day).
  4. Subsidy programs: NEVI or another public funding program, named.
  5. Named operator: the GAAP net income or net loss from a specific public charging operator's most recent 10-K or 10-Q, and the citation for it must be the SEC filing itself (sec.gov), not a press release, earnings-call recap, or news article.
  6. Contrarian source: at least one cited source whose thesis is that the economics are unfavorable or structurally challenged.
  7. Cost split: a hardware vs soft-cost (install, permitting, grid) breakdown or ratio.

CITATION CHECK. For every [n] entry in the Sources section:
  a. LIVE: Fetch the URL with web_fetch. Mark LIVE only if web_fetch returns the readable page directly. Mark DEAD if 404, parked, login-walled, paywalled, returns a bot-block/403, or renders only via JavaScript. Do NOT corroborate via mirrors, reposts, or search snippets; the cited URL itself must fetch.
  b. VERBATIM: Search the fetched page for the quoted string. Mark QUOTE_MATCH if the exact string appears (treat curly vs straight quotes as equivalent); NOT_FOUND otherwise.
  c. SUPPORTS CLAIM: Mark SUPPORTS_CLAIM if the quoted passage actually backs the claim it's cited on in the brief; UNSUPPORTED if it's tangential, contradicts the claim, or is just a general statement of fact.

OUTPUT FORMAT:

Line 1: Coverage N/7. Citations M/K verified.

Then, for each failed item in the coverage checklist, create a new bullet, name the item and say what specific bar it failed in one sentence max per bullet. For example: "Item 3 Utilization breakeven - MISSING. <what's missing>".

Then, for each failed citation, create a new bullet with the format: "[n] domain - REASON. <what's wrong and what to do>". One sentence max per bullet. For example: "[3] evgo.com - DEAD. The URL returns a 403 error and appears to be behind a bot block. No mirrors or reposts; the cited URL itself must fetch."
"""

client.beta.sessions.events.send(
    session.id,
    betas=BETAS,
    events=[
        {
            "type": "user.define_outcome",
            "description": TASK,
            "rubric": {"type": "text", "content": RUBRIC},
            "max_iterations": 5,
        },
    ],
)
```

```
BetaManagedAgentsSendSessionEvents(data=[BetaManagedAgentsUserDefineOutcomeEvent(id='sevt_011CakRYTKNkXJN7eh4kRs1r', description='Write a brief on the unit economics of public DC fast charging in the United States.\nThe brief should cover:\n  1. Capex range\n  2. Demand charges\n  3. Utilization breakeven\n  4. Subsidy programs\n  5. Named-operator economics\n  6. A contrarian or skeptical source\n  7. Hardware vs install cost split\n', max_iterations=5, outcome_id='outc_011CakRYTKNkJ83CBexcz13e', processed_at=datetime.datetime(2026, 5, 6, 1, 10, 30, 512206, tzinfo=TzInfo(0)), rubric=BetaManagedAgentsTextRubric(content='\nYou are reviewing a research brief at /mnt/session/outputs/brief.md against a coverage checklist and verifying its citations. The writer was told the seven topics to cover; this rubric defines what counts as sufficient coverage for each topic, and how to verify citations.\n\nCOVERAGE CHECKLIST. Each item has a specific area:\n  1. Capex range: a dollar range for installed cost per DC fast-charging stall or station.\n  2. Demand charges: quantified impact on opex (a $/kW figure or a % of operating cost).\n  3. Utilization breakeven: a breakeven or target utilization threshold (% or kWh/day).\n  4. Subsidy programs: NEVI or another public funding program, named.\n  5. Named operator: the GAAP net income or net loss from a specific public charging operator\'s most recent 10-K or 10-Q, and the citation for it must be the SEC filing itself (sec.gov), not a press release, earnings-call recap, or news article.\n  6. Contrarian source: at least one cited source whose thesis is that the economics are unfavorable or structurally challenged.\n  7. Cost split: a hardware vs soft-cost (install, permitting, grid) breakdown or ratio.\n\nCITATION CHECK. For every [n] entry in the Sources section:\n  a. LIVE: Fetch the URL with web_fetch. Mark LIVE only if web_fetch returns the readable page directly. Mark DEAD if 404, parked, login-walled, paywalled, returns a bot-block/403, or renders only via JavaScript. Do NOT corroborate via mirrors, reposts, or search snippets; the cited URL itself must fetch.\n  b. VERBATIM: Search the fetched page for the quoted string. Mark QUOTE_MATCH if the exact string appears (treat curly vs straight quotes as equivalent); NOT_FOUND otherwise.\n  c. SUPPORTS CLAIM: Mark SUPPORTS_CLAIM if the quoted passage actually backs the claim it\'s cited on in the brief; UNSUPPORTED if it\'s tangential, contradicts the claim, or is just a general statement of fact.\n\nOUTPUT FORMAT: \n\nLine 1: Coverage N/7. Citations M/K verified.\n\nThen, for each failed item in the coverage checklist, create a new bullet, name the item and say what specific bar it failed in one sentence max per bullet. For example: "Item 3 Utilization breakeven - MISSING. <what\'s missing>".\n\nThen, for each failed citation, create a new bullet with the format: "[n] domain - REASON. <what\'s wrong and what to do>". One sentence max per bullet. For example: "[3] evgo.com - DEAD. The URL returns a 403 error and appears to be behind a bot block. No mirrors or reposts; the cited URL itself must fetch."\n', type='text'), type='user.define_outcome')])
```

A few notes on the call above:

* **The description and rubric have separate jobs.** The description tells the writer what to make. The rubric tells the grader how to check it. They should agree on the artifact's location and format; if they contradict each other (say the description asks for inline output and the rubric grades a file at `/mnt/session/outputs/`), the loop returns `failed` instead of thrashing.
* **`max_iterations` defaults to 3 (max 20).** We set it to 5 since this rubric is strict and the writer needs room. If every run hits the cap with the grader finding the same kind of issue each time, the writer can't act on the feedback and you're paying for iterations that don't converge.
* **Inline rubric vs. file rubric.** Inline text is fine for a notebook. In production you'd upload the rubric once via the Files API and pass `rubric: {"type": "file", "file_id": ...}` so it's reusable across sessions and reviewable like code.

**Why not just put the rubric in the system prompt?** You can, and it helps the writer aim better. But a writer that knows the criteria is still grading its own work. It will say it passed whenever it believes it did, and it will not go back and refetch a URL it already cited or notice that the quote it remembers is slightly different from the quote on the page. The grader has no choice but to do those checks. It opens with a fresh context window and nothing but the rubric and the artifact, and the platform does not let the loop continue until it produces a verdict on every criterion. You cannot get that kind of separation from a single prompt, however well you write it.

## 4. Watch the review loop

Let's stream events and render each phase as it happens. We'll print a banner when the writer finishes a draft and show the grader's feedback after each evaluation.

Two display helpers for the loop below: `banner` draws a labeled divider, and `render_feedback` strips the boilerplate the server wraps around each grader explanation.

python

```
HR = "━" * 46

def banner(label, tag=""):
    print(f"\n{HR}\n{label}  {tag}".rstrip())

def render_feedback(fb: str):
    # Strip the server's per-criterion wrapper and trailer.
    s = re.sub(
        r"^An independent grader found.*?:\n\n- .*?\((?:partially |not )?met\): ",
        "",
        fb,
        count=1,
        flags=re.S,
    )
    s = re.sub(r"\n\nPlease revise your work.*$", "", s, flags=re.S)
    print(s)
```

python

```
TERMINAL = {"satisfied", "max_iterations_reached", "failed", "interrupted"}
t0, res, iters = time.time(), None, 0
n_search, last_len = 0, 0

with client.beta.sessions.events.stream(session.id, betas=BETAS) as stream:
    for ev in stream:
        if ev.type == "agent.tool_use":
            if ev.name in ("web_search", "web_fetch"):
                n_search += 1
            if ev.name == "write" and ev.input["file_path"].endswith("brief.md"):
                last_len = len(ev.input["content"])
        elif ev.type == "span.outcome_evaluation_start":
            banner("writer · " + ("draft" if iters == 0 else f"revision {iters}"))
            print(f"searched/fetched {n_search}× · wrote brief.md ({last_len:,} chars)")
            n_search = 0
        elif ev.type == "span.outcome_evaluation_end":
            res = ev.result
            banner(
                f"grader · pass {iters}",
                "✓ satisfied" if res == "satisfied" else "⟳ needs_revision",
            )
            render_feedback(ev.explanation)
            iters += 1
            if res in TERMINAL:
                break

m, s = divmod(int(time.time() - t0), 60)
print(f"\ndone: {res} after {iters} pass{'es' if iters != 1 else ''} · {m}m {s:02d}s")
```

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
writer · draft
searched/fetched 18× · wrote brief.md (7,607 chars)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
grader · pass 0  ⟳ needs_revision
The brief covers 5 of 7 required topics adequately. Item 2 (Demand charges) fails the quantification bar: the brief describes demand charges qualitatively as the 'single largest operational wildcard' but never states a $/kW figure (McKinsey's footnote of $20/kW is never quoted in the text) or a % of operating cost. Item 5 (Named operator) fails the citation requirement: EVgo's Q1 2024 net loss of $28.2M is cited to evchargingstations.com [6], a third-party news article, not an SEC filing from sec.gov as the rubric explicitly requires. All 6 citations are LIVE, and all 6 quoted strings match the fetched pages and support the claims they are attached to — but [6] is the wrong source type for the Named Operator criterion.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
writer · revision 1
searched/fetched 6× · wrote brief.md (7,989 chars)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
grader · pass 1  ⟳ needs_revision
Six of seven coverage items are fully met: (1) capex range with hardware $45K–$100K and install $40K–$150K per charger; (2) demand charges quantified at $20/kW and $9,600/month for a 480kW station; (3) utilization breakeven at 20% vs. 7.5% national average; (4) NEVI Formula Program named with $5B allocation; (6) contrarian source—Great Plains Institute 'nearly all DCFC scenarios lose money' fully cited and live; (7) hardware vs. install cost split clearly broken out. All six citations fetch live, every quoted string matches exactly, and all citations support the claims they are attached to (6/6 verified). Item 5 (Named operator) fails the rubric's specific requirement: the rubric demands GAAP net income/loss from a 10-K or 10-Q, and the citation must be the SEC filing itself—not a press release. The brief cites EVgo's FY2024 GAAP net loss of $126.7M, but the citation [6] is an 8-K EX-99.1 (earnings press release exhibit), explicitly labelled '(8-K EX-99.1)' in the Sources section. The rubric specifically excludes press releases, and an 8-K EX-99.1 is precisely that—a press release filed with the SEC—not a 10-K or 10-Q annual/quarterly report.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
writer · revision 2
searched/fetched 7× · wrote brief.md (7,989 chars)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
grader · pass 2  ✓ satisfied
All 7 coverage items are fully met: (1) Capex range gives hardware $45K-$100K+ and installation $40K-$150K+ per charger, plus NEVI average $915,420/station. (2) Demand charges quantified at $20/kW (explicit $/kW figure) with $9,600/month example. (3) Utilization breakeven at 20% or $0.53/kWh threshold explicitly modeled. (4) NEVI and IRA Section 30C named as subsidy programs. (5) EVgo GAAP net loss of $126.7M for FY2024 cited from the SEC filing itself (sec.gov XBRL R4.htm), not a press release. (6) Great Plains Institute contrarian source cited with thesis that 'nearly all DCFC scenarios lose money.' (7) Hardware vs. install cost split explicitly broken out. All 6 citations are LIVE (URLs return readable pages), all quoted strings appear verbatim in the fetched pages, and all support the claims they are cited on.

done: satisfied after 3 passes · 12m 56s
```

### What just happened

The loop ran for three grading passes.

The first draft covered five of seven items. The grader sent it back for two misses: demand charges were described qualitatively with no dollars-per-kW figure, and the named-operator section cited a third-party news article rather than an SEC filing. The writer added the $20/kW number and went to sec.gov for EVgo's FY2024 net loss.

The second pass cleared six of seven. The sec.gov document the writer cited was an 8-K Exhibit 99.1, the earnings press release as filed, not the 10-K or 10-Q the rubric asks for. The grader read the URL, identified it as a press-release exhibit, and rejected it on exactly that distinction. On the third pass the writer found EVgo's actual 10-K on EDGAR and the grader cleared it: 7/7 coverage, 6/6 citations live, quote-matching, and supportive.

Both rejections happened because the rubric drew a line the grader could check. "A $/kW figure or a % of operating cost" and "the SEC filing itself, not a press release" are decisions the rubric author made; the task itself ("cover demand charges," "named-operator economics") would have waved both through. The second rejection is the one to study. The writer found a `sec.gov` URL, which on its face satisfies the task, and the grader still bounced it because the rubric distinguished an 8-K press-release exhibit from a 10-K. Without that distinction the loop ends one pass early with a worse brief.

**Note** that the trace above is from the original cookbook run. If you run this yourself, your results will likely differ.

## 5. Read the final brief

Finally, let's pull the last version of `brief.md` the writer produced and look at what it covers and what it cited. Print `content` itself if you want to read the full prose.

python

```
# Reconstruct the final brief from the event log: full content on `write`,
# then apply each `edit` (old_string -> new_string) in order.
content = ""
for ev in client.beta.sessions.events.list(session.id, limit=1000, betas=BETAS):
    if ev.type != "agent.tool_use" or "brief.md" not in str(ev.input.get("file_path", "")):
        continue
    if ev.name == "write":
        content = ev.input["content"]
    elif ev.name == "edit":
        content = content.replace(ev.input["old_string"], ev.input["new_string"], 1)

# Show the structure and sources rather than the full prose.
for line in content.splitlines():
    if line.startswith(("#", "[")):
        print(line)
```

```
# Unit Economics of Public DC Fast Charging in the United States
## 1. Capex Range
## 2. Demand Charges
## 3. Utilization Breakeven
## 4. Subsidy Programs
## 5. Named-Operator Economics
## 6. Contrarian / Skeptical View
## 7. Hardware vs. Installation Cost Split
## Sources
[1] "A 150 to 350kW DCFC charging unit can cost anywhere from $45,000 to over $100,000, and installation costs can range from $40,000 to over $150,000." - Can public EV fast-charging stations be profitable in the United States? - https://www.mckinsey.com/features/mckinsey-center-for-future-mobility/our-insights/can-public-ev-fast-charging-stations-be-profitable-in-the-united-states
[2] "Waiving demand charges for fast chargers will shift costs to all ratepayers, including non-EV drivers." - Fast charging, high costs: Eliminating demand charges won't solve the problem - https://www.utilitydive.com/news/eliminating-demand-charges-wont-solve-EV-station-problems/689395/
[3] "the average total NEVI project cost is $915,420. The median total cost is $802,267" - NEVI DC Fast Charging Station Total Project Cost Averages $915,000 - https://www.paren.app/blog/nevi-dc-fast-charging-station-total-project-cost-averages-915-000
[4] "Today's economics and the average electric utility rates mean that nearly all DCFC scenarios lose money" - 'Nearly all' high voltage EV charging stations lose money: Report - https://www.utilitydive.com/news/nearly-all-high-voltage-ev-charging-stations-lose-money-report/561026/
[5] "apportions a total of $5 billion to States, D.C., and Puerto Rico over five years, from Fiscal Year 2022 through 2026" - Federal Funding Programs - https://www.transportation.gov/rural/ev/toolkit/ev-infrastructure-funding-and-financing/federal-funding-programs
[6] "Consolidated Statements of Operations - USD ($)$ in Thousands | 12 Months Ended Dec. 31, 2024 | Dec. 31, 2023" - EVgo Inc. Form 10-K, Consolidated Statements of Operations (XBRL), Period: 2024-12-31 - https://www.sec.gov/Archives/edgar/data/1821159/000155837025002400/R4.htm
```

## What you learned

* **Outcomes fits when you can write down what good looks like.** Attention-to-detail and exhaustive-coverage tasks are the clearest fit; subjective quality works too if the rubric pins down the bar.
* **The rubric has to make the grader produce evidence.** Without that, it approves whatever it's shown.
* **The grader is independent and stateless.** It runs in its own context window so the writer can't talk it into anything, and a fresh one re-checks the whole artifact every iteration.
* **One outcome at a time, but you can chain them.** Once a loop terminates, the session is conversational again and the next `user.define_outcome` starts a new one.

For more, see the [Outcomes documentation](https://platform.claude.com/docs/en/managed-agents/define-outcomes).
