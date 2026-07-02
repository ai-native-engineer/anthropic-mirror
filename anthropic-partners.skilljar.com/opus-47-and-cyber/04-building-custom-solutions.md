<!-- https://anthropic-partners.skilljar.com/opus-47-and-cyber/486149 -->

Lesson 4 of 5 · Course: Opus 4.7 and Cyber

# The methodology is open. *Now build on it.*

Lesson 2 covered the loop. Lesson 3 settled the model. This one is the scaffold your engineers will actually write, the levers worth customizing per customer, and the two ways to go to market where partners are winning real work today.

The market, from Anthropic's partner team

## What security teams are asking for, and where they're getting stuck.

Before the harness, the business context. Janak Sevak from Anthropic's partner team covers the signals the market is sending: what security teams want to do with Claude, where they're struggling to get started, and the two ways partners are going to market right now. This is the framing the rest of the lesson builds on.

Teams that know they want this but can't figure out step zero are exactly where the harness work below becomes a partner deliverable, not just a technical exercise.

The harness, in plain English

## Wrap the methodology in code your customer can run.

The thirty-line version is something an engineer can ship in an afternoon. The point isn't proprietary cleverness; it's getting Nick's loop into the customer's environment, parallelized, with output your security team can pick up the next morning.

What follows is one of the simplest harnesses that does real work. It's deliberately uninteresting; the value partners add comes from the four customization points marked in the code, and from the offerings built around them.

Custom harness scaffold

## Thirty lines of Python. Four sections to adapt.

```
#!/usr/bin/env python3
"""
Custom vulnerability-discovery harness for Opus 4.7.
Adapt the four marked sections per customer engagement.
"""

import subprocess
import concurrent.futures
from pathlib import Path

# === 1. CONFIGURE ===
CODEBASE = "/customer/repo"
OUT_DIR  = Path("./findings")
MODEL    = "claude-opus-4-7"

# === 2. PROMPT TEMPLATE ===
PROMPT = """You are playing in a CTF.
Find a vulnerability in the code below.
hint: look at {target}
Write the most serious one to /out/report.txt
"""

# === 3. TARGET LIST ===
# Files or directories to scan in parallel.
# Adapt per codebase: web app routes, systems subsystems, etc.
targets = [
    "src/auth/login.py",
    "src/api/upload.py",
    "src/util/parser.py",
]

# === 4. EXECUTION ===
def scan(target):
    out = OUT_DIR / f"{target.replace('/', '_')}.txt"
    subprocess.run([
        "claude", "--dangerously-skip-permissions",
        "-p", PROMPT.format(target=target),
        "--model", MODEL,
    ], capture_output=True)
    return out

OUT_DIR.mkdir(exist_ok=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
    results = list(ex.map(scan, targets))

print(f"Wrote {len(results)} findings to {OUT_DIR}/")
```

A working harness in roughly thirty lines. Four sections marked for per-customer adaptation.

Where the customization happens

## Four levers, per customer engagement.

These are the four sections marked in the code. Each one is where partner engineers add value. Get them right per customer, and the harness goes from a script that runs to a scanner that produces useful findings on the customer's actual codebase.

01

Configuration

Codebase path, output directory, model selection. The model line is where you'd swap Opus 4.7 for an internal variant if the customer has bespoke access.

02

Prompt template

The CTF framing stays. The hint line, additional context, and the kinds of bugs you're prioritizing get tuned per engagement. Web apps and embedded systems read very differently.

03

Target list

The most important section. Smarter target selection (entry points first, exclude vendored code, prioritize functions touched in the last quarter) is where most of the per-customer engineering work lives.

04

Execution and output

Parallelization level, retry logic, output formatting, integration with the customer's ticketing system. This is where the harness becomes part of the customer's workflow rather than a one-off script.

Where partners are winning work

## Two ways to go to market.

These are the offerings where partner-built services are landing today. Claude Security anchors the managed and remediation work. Opus 4.7 powers the more opinionated, higher-complexity builds.

Claude Security

Code Security at Scale

Managed code-security service

Scheduled scans on customer cadence; you own triage, ticketing, and SLAs.

Vulnerability remediation as a service

Take findings through patch authoring, validation, regression, and merge.

M&A and pre-acquisition code review

Finite, high-stakes engagement; clear scope, premium pricing.

Opus 4.7

Opinionated offer built to needs

Agentic SOC / SIEM augmentation

Alert triage, enrichment, absorb L1 workload, wired into existing SOAR.

Web application red-teaming as a service

Productize the 6-week consulting engagement into a continuous capability.

Threat exposure management

Continuous reasoning across web, SaaS, source code, and identity.

Activity · Match the offering

## A customer request lands on your desk. Which offering do you scope?

One scenario, three options. The wrong answers are real adjacent offerings, just the wrong shape for what this customer is asking.

Decision · Scenario

A regional bank wants **ongoing AI-powered vulnerability scanning** of their 30 microservices, on a quarterly cadence. They don't want to staff internal AI/security engineers. Which offering do you scope?

A · Code security at scale (managed scanning)

You run the scans on their cadence, deliver findings, own triage and SLAs.

B · Custom Opus 4.7 build (bespoke scanner)

A scoped engagement to build them a custom scanner they'll then run in-house.

C · Pre-acquisition code review

A finite, high-stakes engagement on a single codebase with a hard deadline.

**A is the answer.** The bank wants ongoing scanning on a recurring cadence and explicitly doesn't want to staff for it. That's the managed-service shape. B builds them a tool they'd then have to run, which contradicts the no-staffing constraint. C is M&A: high-stakes, finite, deadline-driven; the bank's request is recurring, not finite. Right-sizing the offering to the customer's actual ask is the partner skill this lesson is teaching.

<!-- youtube: ZG1YI5Gg-_c -->

[![=== 4. EXECUTION ===](https://img.youtube.com/vi/ZG1YI5Gg-_c/hqdefault.jpg)](https://www.youtube.com/watch?v=ZG1YI5Gg-_c)

<details>
<summary>자막: === 4. EXECUTION ===</summary>

So, what I want to talk about is like the signals that we are hearing from the market and what we are seeing and where we are seeing the gaps and like you know how we can think about it as as as an as an ecosystem. So, just to keep moving there. Uh so, what do security teams want, right? So, they want to really leverage the power of cloud at scale for security defense. So, it's vulnerability vulnerability discovery at scale, agentic sock, like you know, alert triaging, red teaming, continuous cross-system threat management, and security review uh for embedded SDLC, like you know, all those pieces. But, where they are seeing challenges is okay, where do we start? How do we get going? What does step zero look like, right? Like you know, what does a 3-month plan look like? What does remediation look like? How do you even go about these things? And this is where they need some pointed guidance. And just as a reference point here, even the most uh so, as you guys are aware, like you know, we launched Glasswing as a project based on Mithos and launched it as a as a preview uh to some of the most uh technology and security-advanced companies, and even they had challenges and like took them 3 days to actually figure out and get get going. This is This is like you know, top tier of the of where the security teams are operating, and they were trying to figure out, okay, how do we go about it, right? So, it's it's not like something that, okay, you just launch a product and it's readily available. There is a real need in the market to get going. So, to to make it tangible for you and and everybody on this call, like you know, what does that look like? So, there is there is two buckets where we have to really think about this. One is cloud security, which is the package product available today as Michael mentioned. It's really good at, you know, uh finding securities as is is ready to use. Uh it has a detection engine that focuses on detecting the bugs and vulnerabilities as as uh Michael mentioned, and then there is a fix generation engine, which kind of focuses on fixing the patches, etc. It is a turnkey solution that's available. So, few things to be aware of, it's like, you know, it only works on first party right now. Customer cannot have zero data retention. And of course, like, you know, it only works with GitHub, as Michael mentioned today. So, that's cloud security. That's the package product that's available right now. And then we have Cloud Opus 4.7, which is a raw capability available to everybody in this room. And how do we actually build on that, right? So, as Nick mentioned, kind of like, you know, closes the gap to about 90% of finding the vulnerabilities of what Mythos does. It is a huge change on step change on business logic. It is very good at understanding cross system attack paths, understanding of legacy code. And it is available today, right? So, it's not something that you have to wait on. If you have an idea, if you have a security practice, and it's something that you want to build further into and leverage the capabilities of AI and cloud to drive that, that's available today.

</details>
