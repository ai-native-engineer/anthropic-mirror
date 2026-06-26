<!-- source: https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8 -->

# What's new in Claude Opus 4.8
Overview of new features and behavior changes in Claude Opus 4.8.
Claude Opus 4.8 is Anthropic's most capable Opus-tier model. It builds on Claude Opus 4.7. This page summarizes everything new at launch, including fast mode (research preview on the Claude API) and a lower 1,024-token minimum cacheable prompt length.
New model  
| Model  | API model ID  | Description  |  
| --- | --- | --- |  
| Claude Opus 4.8  | claude-opus-4-8  | Anthropic's most capable Opus-tier model for complex reasoning, long-horizon agentic coding, and high-autonomy work  |  
Claude Opus 4.8 supports the [1M token context window](https://platform.claude.com/docs/en/build-with-claude/context-windows) by default on the Claude API, Amazon Bedrock, and Google Cloud (200k on Microsoft Foundry), 128k max output tokens, [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking), and the same set of tools and platform features as Claude Opus 4.7.
For complete pricing and specs, see the [models overview](https://platform.claude.com/docs/en/about-claude/models/overview).
New features
### 
Mid-conversation system messages
Claude Opus 4.8 accepts `role: "system"` messages immediately after a user turn in the `messages` array (subject to [placement rules](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#limitations)). This lets you append updated instructions later in a long-running conversation without restating the full system prompt. Updating instructions this way preserves [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) hits on the earlier turns and reduces input cost on agentic loops. No beta header is required. See [Mid-conversation system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages) for usage details.
### 
Refusal stop details
The `stop_details` object on refusal responses (available since Claude Opus 4.7) is now publicly documented. When Claude declines to complete a request, this object describes the category of refusal, in addition to the existing `refusal` stop reason. Your application can use it to tell apart different classes of declined request and route the user to the right next step. No beta header is required. See [Refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#refusal-response) for the category list and [Stop reasons and fallback](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons) for handling guidance.
### 
Effort defaults
The [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort) default on Claude Opus 4.8 is `high` on all surfaces, including the Claude API and Claude Code. If you set effort explicitly today, your setting is unchanged. See [Effort](https://platform.claude.com/docs/en/build-with-claude/effort) for per-level guidance.
### 
Fast mode
[Fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode) is now available for Claude Opus 4.8 as a research preview on the Claude API. Set `speed: "fast"` with the `fast-mode-2026-02-01` beta header to get up to 2.5x higher output tokens per second from the same model at premium pricing. See [Fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode) for access, supported models, and pricing.
### 
Lower prompt cache minimum
The minimum cacheable prompt length on Claude Opus 4.8 is 1,024 tokens, down from 2,048 tokens on Claude Opus 4.7. Prompts that were too short to cache on Claude Opus 4.7 can now create cache entries with no code changes. See [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#cache-limitations) for per-model minimums.
API constraints inherited from Claude Opus 4.7
These constraints are unchanged from Claude Opus 4.7, so code that already runs on Claude Opus 4.7 needs no changes. They apply to the Messages API only. Claude Managed Agents are unaffected.
### 
Sampling parameters not supported
Setting `temperature`, `top_p`, or `top_k` to a non-default value returns a 400 error on Claude Opus 4.8, same as on Claude Opus 4.7. Omit these parameters and use prompting to guide the model's behavior.
### 
Adaptive thinking is the only thinking mode
Like Claude Opus 4.7, Claude Opus 4.8 does not support extended thinking budgets. Setting `thinking: {type: "enabled", budget_tokens: N}` returns a 400 error.
The following diff updates a request written for Claude Opus 4.6 or earlier to run on Claude Opus 4.8. The removed lines (`-`) set the old model ID and the manual thinking budget that Claude Opus 4.8 rejects. The added lines (`+`) set the new model ID, switch to [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking), and control thinking depth with the [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort), passed in the top-level `output_config` field. The model determines when and how much to think on each turn. If you remove the `thinking` field entirely, requests run without thinking:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

 import anthropic

 client = anthropic.Anthropic()

 response = client.messages.create(
-    model="claude-opus-4-6",
+    model="claude-opus-4-8",
     max_tokens=16000,
-    thinking={"type": "enabled", "budget_tokens": 10000},
+    thinking={"type": "adaptive"},
+    output_config={"effort": "high"},
     messages=[
             "role": "user",
             "content": "Explain why the sum of two even numbers is always even.",
     ],
 )

Capability improvements
### 
Improvement areas
Compared with Claude Opus 4.7, Claude Opus 4.8 targets behavioral improvements in:
  * **Long-horizon agentic coding** , including better long-context handling, fewer compactions, and better [compaction](https://platform.claude.com/docs/en/build-with-claude/compaction) recovery.
  * **Reasoning effort calibration** , with more reliable behavior at each effort level across a range of domains.
  * **Tool triggering** , with fewer cases of skipping a tool call that the task required.

### 
Adaptive thinking
With [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) enabled, Claude Opus 4.8 triggers reasoning only when it determines the turn needs it. On simple lookups and short agentic steps it responds directly. On complex multi-step problems it reasons before answering. This reduces wasted thinking tokens on bimodal workloads compared to Claude Opus 4.7 at the same effort level. As on Claude Opus 4.7, thinking is off unless you explicitly set `thinking: {type: "adaptive"}` in your request.
Behavior changes
These are not API breaking changes but might require prompt updates. See [Migrating to Claude Opus 4.8](https://platform.claude.com/docs/en/about-claude/models/migration-guide#migrating-from-claude-opus-47) for full guidance.
  * **Fewer wasted thinking tokens** at the same effort level when adaptive thinking is enabled, because the model determines per turn whether to think.
  * **Better tool triggering.** The model is less likely to skip a tool call the task required, an issue some users reported on Claude Opus 4.7.
  * **Better compaction handling and long-context quality.** Long agentic traces stay on task with fewer derailments after compaction.
  * **Effort levels recalibrated.** The token allocation behind each effort level changes compared to Claude Opus 4.7: `medium` allows somewhat more thinking, `high` somewhat less, and `xhigh` substantially more. If you tuned an effort level against Claude Opus 4.7, re-baseline cost and latency at that level before adjusting it.

Migration guide
For step-by-step migration instructions and the full migration checklist, see [Migrating to Claude Opus 4.8](https://platform.claude.com/docs/en/about-claude/models/migration-guide#migrating-from-claude-opus-47). If you are upgrading from Claude Opus 4.6 or earlier, also apply the [Claude Opus 4.7 migration steps](https://platform.claude.com/docs/en/about-claude/models/migration-guide#migrating-to-claude-opus-4-7). Those steps cover breaking changes that the Claude Opus 4.8 upgrade alone does not. If you use Claude Code or the Agent SDK, the [Claude API skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill) can apply these migration steps to your code base automatically.
Next steps
[  Migration guide Guide for migrating to the latest Claude models from previous Claude versions. ](https://platform.claude.com/docs/en/about-claude/models/migration-guide#migrating-from-claude-opus-47)[ Effort Control how many tokens Claude uses when responding with the effort parameter, trading off between response thoroughness and token efficiency. ](https://platform.claude.com/docs/en/build-with-claude/effort)[ Adaptive thinking Let Claude dynamically determine when and how much to use extended thinking with adaptive thinking mode. ](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)[ Prompt caching How mid-conversation system messages preserve cache hits. ](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)[  Stop reasons and fallback Learn what each stop_reason value means and how to handle truncation, tool use, paused turns, and refusals in your application. ](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)[  Fast mode (research preview) Get up to 2.5x higher output tokens per second from Claude Opus models. ](https://platform.claude.com/docs/en/build-with-claude/fast-mode)
  * [New model](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8#new-model)
  * [New features](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8#new-features)
  * [Mid-conversation system messages](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8#mid-conversation-system-messages)
  * [Refusal stop details](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8#refusal-stop-details)
  * [Effort defaults](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8#effort-defaults)
  * [Fast mode](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8#fast-mode)
  * [Lower prompt cache minimum](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8#lower-prompt-cache-minimum)
  * [API constraints inherited from Claude Opus 4.7](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8#api-constraints-inherited-from-claude-opus-4-7)
  * [Sampling parameters not supported](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8#sampling-parameters-not-supported)
  * [Adaptive thinking is the only thinking mode](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8#adaptive-thinking-is-the-only-thinking-mode)
  * [Capability improvements](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8#capability-improvements)
  * [Improvement areas](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8#improvement-areas)
  * [Adaptive thinking](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8#adaptive-thinking)
  * [Behavior changes](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8#behavior-changes)
  * [Migration guide](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8#migration-guide)
  * [Next steps](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8#next-steps)

Models & pricing/Models
# What's new in Claude Opus 4.8
Overview of new features and behavior changes in Claude Opus 4.8.
Claude Opus 4.8 is Anthropic's most capable Opus-tier model. It builds on Claude Opus 4.7. This page summarizes everything new at launch, including fast mode (research preview on the Claude API) and a lower 1,024-token minimum cacheable prompt length.
New model  
| Model  | API model ID  | Description  |  
| --- | --- | --- |  
| Claude Opus 4.8  | claude-opus-4-8  | Anthropic's most capable Opus-tier model for complex reasoning, long-horizon agentic coding, and high-autonomy work  |  
Claude Opus 4.8 supports the [1M token context window](https://platform.claude.com/docs/en/build-with-claude/context-windows) by default on the Claude API, Amazon Bedrock, and Google Cloud (200k on Microsoft Foundry), 128k max output tokens, [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking), and the same set of tools and platform features as Claude Opus 4.7.
For complete pricing and specs, see the [models overview](https://platform.claude.com/docs/en/about-claude/models/overview).
New features
### 
Mid-conversation system messages
Claude Opus 4.8 accepts `role: "system"` messages immediately after a user turn in the `messages` array (subject to [placement rules](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#limitations)). This lets you append updated instructions later in a long-running conversation without restating the full system prompt. Updating instructions this way preserves [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) hits on the earlier turns and reduces input cost on agentic loops. No beta header is required. See [Mid-conversation system messages](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages) for usage details.
### 
Refusal stop details
The `stop_details` object on refusal responses (available since Claude Opus 4.7) is now publicly documented. When Claude declines to complete a request, this object describes the category of refusal, in addition to the existing `refusal` stop reason. Your application can use it to tell apart different classes of declined request and route the user to the right next step. No beta header is required. See [Refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#refusal-response) for the category list and [Stop reasons and fallback](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons) for handling guidance.
### 
Effort defaults
The [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort) default on Claude Opus 4.8 is `high` on all surfaces, including the Claude API and Claude Code. If you set effort explicitly today, your setting is unchanged. See [Effort](https://platform.claude.com/docs/en/build-with-claude/effort) for per-level guidance.
### 
Fast mode
[Fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode) is now available for Claude Opus 4.8 as a research preview on the Claude API. Set `speed: "fast"` with the `fast-mode-2026-02-01` beta header to get up to 2.5x higher output tokens per second from the same model at premium pricing. See [Fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode) for access, supported models, and pricing.
### 
Lower prompt cache minimum
The minimum cacheable prompt length on Claude Opus 4.8 is 1,024 tokens, down from 2,048 tokens on Claude Opus 4.7. Prompts that were too short to cache on Claude Opus 4.7 can now create cache entries with no code changes. See [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#cache-limitations) for per-model minimums.
API constraints inherited from Claude Opus 4.7
These constraints are unchanged from Claude Opus 4.7, so code that already runs on Claude Opus 4.7 needs no changes. They apply to the Messages API only. Claude Managed Agents are unaffected.
### 
Sampling parameters not supported
Setting `temperature`, `top_p`, or `top_k` to a non-default value returns a 400 error on Claude Opus 4.8, same as on Claude Opus 4.7. Omit these parameters and use prompting to guide the model's behavior.
### 
Adaptive thinking is the only thinking mode
Like Claude Opus 4.7, Claude Opus 4.8 does not support extended thinking budgets. Setting `thinking: {type: "enabled", budget_tokens: N}` returns a 400 error.
The following diff updates a request written for Claude Opus 4.6 or earlier to run on Claude Opus 4.8. The removed lines (`-`) set the old model ID and the manual thinking budget that Claude Opus 4.8 rejects. The added lines (`+`) set the new model ID, switch to [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking), and control thinking depth with the [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort), passed in the top-level `output_config` field. The model determines when and how much to think on each turn. If you remove the `thinking` field entirely, requests run without thinking:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

 import anthropic

 client = anthropic.Anthropic()

 response = client.messages.create(
-    model="claude-opus-4-6",
+    model="claude-opus-4-8",
     max_tokens=16000,
-    thinking={"type": "enabled", "budget_tokens": 10000},
+    thinking={"type": "adaptive"},
+    output_config={"effort": "high"},
     messages=[
             "role": "user",
             "content": "Explain why the sum of two even numbers is always even.",
     ],
 )

Capability improvements
### 
Improvement areas
Compared with Claude Opus 4.7, Claude Opus 4.8 targets behavioral improvements in:
  * **Long-horizon agentic coding** , including better long-context handling, fewer compactions, and better [compaction](https://platform.claude.com/docs/en/build-with-claude/compaction) recovery.
  * **Reasoning effort calibration** , with more reliable behavior at each effort level across a range of domains.
  * **Tool triggering** , with fewer cases of skipping a tool call that the task required.

### 
Adaptive thinking
With [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) enabled, Claude Opus 4.8 triggers reasoning only when it determines the turn needs it. On simple lookups and short agentic steps it responds directly. On complex multi-step problems it reasons before answering. This reduces wasted thinking tokens on bimodal workloads compared to Claude Opus 4.7 at the same effort level. As on Claude Opus 4.7, thinking is off unless you explicitly set `thinking: {type: "adaptive"}` in your request.
Behavior changes
These are not API breaking changes but might require prompt updates. See [Migrating to Claude Opus 4.8](https://platform.claude.com/docs/en/about-claude/models/migration-guide#migrating-from-claude-opus-47) for full guidance.
  * **Fewer wasted thinking tokens** at the same effort level when adaptive thinking is enabled, because the model determines per turn whether to think.
  * **Better tool triggering.** The model is less likely to skip a tool call the task required, an issue some users reported on Claude Opus 4.7.
  * **Better compaction handling and long-context quality.** Long agentic traces stay on task with fewer derailments after compaction.
  * **Effort levels recalibrated.** The token allocation behind each effort level changes compared to Claude Opus 4.7: `medium` allows somewhat more thinking, `high` somewhat less, and `xhigh` substantially more. If you tuned an effort level against Claude Opus 4.7, re-baseline cost and latency at that level before adjusting it.

Migration guide
For step-by-step migration instructions and the full migration checklist, see [Migrating to Claude Opus 4.8](https://platform.claude.com/docs/en/about-claude/models/migration-guide#migrating-from-claude-opus-47). If you are upgrading from Claude Opus 4.6 or earlier, also apply the [Claude Opus 4.7 migration steps](https://platform.claude.com/docs/en/about-claude/models/migration-guide#migrating-to-claude-opus-4-7). Those steps cover breaking changes that the Claude Opus 4.8 upgrade alone does not. If you use Claude Code or the Agent SDK, the [Claude API skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill) can apply these migration steps to your code base automatically.
Next steps
[  Migration guide Guide for migrating to the latest Claude models from previous Claude versions. ](https://platform.claude.com/docs/en/about-claude/models/migration-guide#migrating-from-claude-opus-47)[ Effort Control how many tokens Claude uses when responding with the effort parameter, trading off between response thoroughness and token efficiency. ](https://platform.claude.com/docs/en/build-with-claude/effort)[ Adaptive thinking Let Claude dynamically determine when and how much to use extended thinking with adaptive thinking mode. ](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)[ Prompt caching How mid-conversation system messages preserve cache hits. ](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)[  Stop reasons and fallback Learn what each stop_reason value means and how to handle truncation, tool use, paused turns, and refusals in your application. ](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)[  Fast mode (research preview) Get up to 2.5x higher output tokens per second from Claude Opus models. ](https://platform.claude.com/docs/en/build-with-claude/fast-mode)
