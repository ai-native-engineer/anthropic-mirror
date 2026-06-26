<!-- source: https://support.claude.com/en/articles/15363606-why-claude-switched-models-in-your-conversation-with-fable-5 -->

# Why Claude switched models in your conversation with Fable 5

Updated over a week ago

**Update June 12:** We've suspended access to Claude Fable 5. **[Learn more here](https://anthropic.com/news/fable-mythos-access)**.

This article explains why a request might be blocked, what happens when your conversation switches to a different Claude model, and how to manage automatic switching.

## Why some requests get blocked

Claude Fable 5's capabilities far exceed those of every model we've previously made generally available. It is state-of-the-art on nearly all tested benchmarks of AI capability, showing exceptional performance in software engineering, knowledge work, vision, and many other areas.

Releasing a model this capable comes with risks. Without strong safeguards, Claude Fable 5's advanced capabilities in areas like cybersecurity and biology could be misused by users to create large-scale cyberattacks or bioweapons that could result in catastrophic damage. These capabilities are the reason we’ve previously only released Mythos-class models (like Mythos Preview) to a small number of selected and vetted partners.

Recognizing these risks, to allow general users to access the vast majority of Fable 5's capabilities, we've launched the model with safeguards that block its responses in some specific areas in line with our **[Terms of Service](https://www.anthropic.com/legal/commercial-terms)** and **[Acceptable Use Policy](https://www.anthropic.com/legal/aup)**.

Most user queries blocked by these safeguards on Fable 5 will instead receive a response from our next-most-capable model, Claude Opus 4.8. We're working on making these safeguards more discerning to precisely block uses of the model that directly relate to targeting risks, with fewer false positives than there are today.

## What requests get blocked

Claude Fable 5 runs automated safety checks on every user request. These checks are intended to block requests in four areas:

* Offensive cybersecurity techniques, such as building exploits, malware, or attack tooling
* Biology and life sciences queries, such as lab methods or molecular mechanisms
* Extraction of the model’s **[summarized thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#summarized-thinking)**
* A narrow set of frontier LLM development tasks, such as distributed training infrastructure, ML accelerator design, and kernel development for certain non-standard chips

These blocking safeguards are intentionally broad. They may block legitimate work in these areas, including authorized security testing and benign biology research, and normal, safe conversations that only touch on these topics—such as biotech business documentation, medical imaging and diagnostics, clinical and diagnostic healthcare questions, or basic educational content in biology.

The checks also review everything the model reads, not just your latest message—including memory, content from connectors, web search results, and files, so a block can be triggered by content you didn't type.

## What happens after a block

By default, automatic model switching is active in Claude, Claude Cowork, Claude Code, Claude Design, and Claude for Microsoft 365. When automatically switching models, Claude re-runs your blocked Claude Fable 5 request on Claude Opus 4.8 in the same conversation. You’ll see a notice explaining that the model switched, and the response will be labeled with the model that answered. Opus is a highly capable model with strong safeguards of its own, and for most otherwise legitimate requests blocked on Fable 5—including most biology questions—Opus should give you a helpful answer.

After the switch, the model picker stays on Opus for the rest of the conversation. You can switch back to Claude Fable 5 anytime from the model picker.

**Note:** If you switch back to Claude Fable 5 after an automatic model switch occurs, note that the same Fable 5 safeguards may block the conversation again because the original request is still part of it. Editing your previous message before retrying often helps.

### If the request is also blocked on Opus

Opus has its own safety systems. If your request is also blocked on Opus, you can edit your message and retry. For cyber specifically, if your use case has a legitimate defensive purpose and is being affected by these safeguards, you can apply for the Cyber Verification Program (CVP) for Opus. Learn more about **[real-time cyber safeguards and the Cyber Verification Program](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude)**.

## Manage automatic model switching

Automatic switching is enabled by default the first time you select Claude Fable 5. It stays on by default, and you can turn it off anytime:

1. Go to **[Settings > Capabilities](http://claude.ai/settings/capabilities)** (or **Config > MODEL & OUTPUT** in Claude Code).
2. Toggle **Switch models when a message is flagged** off.

With automatic model switching off, a blocked request pauses the conversation instead of switching models. You can then:

* Edit your message and retry onClaude Fable 5
* Send the same message to Opus manually

## Usage and billing

Blocked requests are billed differently depending on when the block happens:

* **Blocked on input:** If a request is blocked before Claude Fable 5 produces any output, the conversation switches to Opus immediately. You're charged only at Opus rates, and the Opus response counts toward your usage limit or consumption.
* **Blocked midstream:** If a request is blocked midstream, the input and the tokens streamed before the block are charged at Claude Fable 5 rates. The rest of the response is charged at Opus rates.

## Give feedback

If your blocked request seems unrelated to security or biology topics, or if your legitimate work in these areas keeps getting blocked, let us know. Use "Send feedback" to report it. Reports of incorrectly blocked requests help us narrow and improve these safeguards.

## Stay tuned for updates

Moving forward, we plan to consider ways to open up allocations for dual-use cyberdefense and biology research. As our safety systems mature, we aim to support legitimate biology and defensive cybersecurity work while keeping strong protections against misuse in place.

We'll share more details about the program, including eligibility and how to apply, as they become available. Watch this Help Center for updates, or **[sign up for notifications here](https://claude.com/form/mythos-access-interest)**.

## Where automatic model switching applies

Automatic model switching works the same way everywhere you can use Claude Fable 5:

* Claude on the web
* Claude Mobile
* Claude Desktop
* Claude Cowork
* Claude Code
* Claude Design
* Claude for Microsoft 365
* Claude for Teams
* Claude in Slack

**Important:** If you're using the Claude API, model switching works differently. Automatic switching isn't automatic, and API customers must opt into and configure the switching in the API. See the developer documentation for details.

Read our blog to learn more about Claude Fable 5: **[Claude Fable 5 and Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)**.

[How up-to-date is Claude's training data?](https://support.claude.com/en/articles/8114494-how-up-to-date-is-claude-s-training-data)[How large is the Claude API’s context window?](https://support.claude.com/en/articles/8606395-how-large-is-the-claude-api-s-context-window)[Claude Code model configuration](https://support.claude.com/en/articles/11940350-claude-code-model-configuration)[Real-time cyber safeguards on Claude](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude)[Data retention practices for Mythos-class models](https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models)
