<!-- source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use -->

# Troubleshooting tool use
Fix the most common tool-use errors with symptom-to-fix diagnostic tables.
Symptom-to-fix tables for the most common tool-use errors. Each fix cross-references the page that owns the feature.
Claude calls the wrong tool  
| Symptom  | Likely cause  | Fix  |  
| --- | --- | --- |  
| Claude calls tool A when you wanted tool B  | Description ambiguity  | Sharpen descriptions. Differentiate tools by WHEN to use them, not only WHAT they do. See [Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools).  |  
| Claude never calls your tool  | Tool name collision or overly-generic schema  | Check for duplicate names across your tool list. Add `input_examples` to make the intended use concrete.  |  
| Claude calls with wrong parameter types  | Model guessing at ambiguous schema  | Add `strict: true` (if your schema is in the supported subset) or add `input_examples`.  |  
Claude invents tool parameters  
| Symptom  | Likely cause  | Fix  |  
| --- | --- | --- |  
| Parameter that doesn't exist in your schema  | Model over-generation without strict mode  | Add `strict: true` if your schema is in the [supported subset](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use).  |  
| Parameter values outside your enum  | Missing strict mode or too-large enum  | Shrink the enum or add `input_examples` showing valid choices.  |  
Parallel tool calls don't work  
| Symptom  | Likely cause  | Fix  |  
| --- | --- | --- |  
| Claude calls tools sequentially when parallel would be better  | Message history formatting  | Send multiple `tool_result` blocks in ONE user message, not one per turn. See [Parallel tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use).  |  
|  `disable_parallel_tool_use` seems ignored  | Set too late in the conversation  | Must be set on the request that returns `tool_use`. Setting it on a later request has no effect on earlier tool calls.  |  
Cache keeps invalidating  
| Symptom  | Likely cause  | Fix  |  
| --- | --- | --- |  
| Every request is a cache miss  |  `tool_choice` varying between requests  | Keep `tool_choice` stable or place the `cache_control` breakpoint before the variation point. See [Tool use with prompt caching](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching).  |  
| Adding a tool mid-conversation breaks cache  | Tool prepended to the tools array  | Use `defer_loading: true` with tool search to append the tool inline instead of modifying the array head.  |  
Errors at request time  
| Error  | Cause  | Fix  |  
| --- | --- | --- |  
| `tool_use ids were found without tool_result blocks immediately after`  | Missing `tool_result` for some `tool_use` ids, or `tool_result` is not the first content block in the user message  | Return one `tool_result` for every `tool_use` block in the assistant response. Put `tool_result` blocks before any text. See [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls) and [Parallel tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use).  |  
| `Input schema is not compatible with strict mode: string patterns are not supported`  | Using `pattern` with `strict: true`  | Remove the pattern or drop `strict: true`. The `pattern` keyword is not in the supported JSON Schema subset yet.  |  
| `All tools have defer_loading: true`  | No tools visible to the model  | At least one tool must be immediately loaded. The tool search tool itself must never have `defer_loading: true`.  |  
Error: thinking blocks cannot be modified
If a request fails with a 400 `invalid_request_error` whose message contains ``thinking` or `redacted_thinking` blocks in the latest assistant message cannot be modified` when continuing a conversation after a tool call, your application is altering the assistant's thinking blocks before sending them back. Send the entire assistant message back unchanged, then append your `tool_result`.
See [Thinking blocks cannot be modified](https://platform.claude.com/docs/en/api/errors#thinking-blocks-cannot-be-modified) for the full error and fix steps.
Claude flags tool results as prompt injection  
| Symptom  | Likely cause  | Fix  |  
| --- | --- | --- |  
| Claude refuses to act on a tool result, or asks the user to confirm instructions that came from it  | Your own instructions are being delivered inside the `tool_result` content  | Claude is trained to treat instructions inside tool results as potentially untrusted third-party content. Move your instructions out of the tool result: send them in a `user` turn after the `tool_result` block, or (on Claude Opus 4.8 and later) in a [mid-conversation system message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages). Keep the tool result to just the data. See [Mitigate jailbreaks and prompt injections](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks#indirect-prompt-injection).  |  
JSON escaping differences (Opus 4.6+)  
| Symptom  | Cause  | Fix  |  
| --- | --- | --- |  
| String comparison on tool inputs fails with newer models  | Unicode and forward-slash escaping differs between model versions  | Parse with `json.loads()` or `JSON.parse()`. Never do raw string matching on serialized input.  |  
Next steps
[ Define tools Write schemas and descriptions that steer Claude toward the right tool. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)[ Handle tool calls Execute tools and return results in the required message format. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)[ Tool reference Full directory of Anthropic-schema tools and their version strings. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)
  * [Claude calls the wrong tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use#claude-calls-the-wrong-tool)
  * [Claude invents tool parameters](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use#claude-invents-tool-parameters)
  * [Parallel tool calls don't work](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use#parallel-tool-calls-dont-work)
  * [Cache keeps invalidating](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use#cache-keeps-invalidating)
  * [Errors at request time](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use#errors-at-request-time)
  * [Error: thinking blocks cannot be modified](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use#error-thinking-blocks-cannot-be-modified)
  * [Claude flags tool results as prompt injection](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use#claude-flags-tool-results-as-prompt-injection)
  * [JSON escaping differences (Opus 4.6+)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use#json-escaping-differences-opus-4-6)
  * [Next steps](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use#next-steps)

Messages/Tools
# Troubleshooting tool use
Fix the most common tool-use errors with symptom-to-fix diagnostic tables.
Symptom-to-fix tables for the most common tool-use errors. Each fix cross-references the page that owns the feature.
Claude calls the wrong tool  
| Symptom  | Likely cause  | Fix  |  
| --- | --- | --- |  
| Claude calls tool A when you wanted tool B  | Description ambiguity  | Sharpen descriptions. Differentiate tools by WHEN to use them, not only WHAT they do. See [Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools).  |  
| Claude never calls your tool  | Tool name collision or overly-generic schema  | Check for duplicate names across your tool list. Add `input_examples` to make the intended use concrete.  |  
| Claude calls with wrong parameter types  | Model guessing at ambiguous schema  | Add `strict: true` (if your schema is in the supported subset) or add `input_examples`.  |  
Claude invents tool parameters  
| Symptom  | Likely cause  | Fix  |  
| --- | --- | --- |  
| Parameter that doesn't exist in your schema  | Model over-generation without strict mode  | Add `strict: true` if your schema is in the [supported subset](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use).  |  
| Parameter values outside your enum  | Missing strict mode or too-large enum  | Shrink the enum or add `input_examples` showing valid choices.  |  
Parallel tool calls don't work  
| Symptom  | Likely cause  | Fix  |  
| --- | --- | --- |  
| Claude calls tools sequentially when parallel would be better  | Message history formatting  | Send multiple `tool_result` blocks in ONE user message, not one per turn. See [Parallel tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use).  |  
|  `disable_parallel_tool_use` seems ignored  | Set too late in the conversation  | Must be set on the request that returns `tool_use`. Setting it on a later request has no effect on earlier tool calls.  |  
Cache keeps invalidating  
| Symptom  | Likely cause  | Fix  |  
| --- | --- | --- |  
| Every request is a cache miss  |  `tool_choice` varying between requests  | Keep `tool_choice` stable or place the `cache_control` breakpoint before the variation point. See [Tool use with prompt caching](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching).  |  
| Adding a tool mid-conversation breaks cache  | Tool prepended to the tools array  | Use `defer_loading: true` with tool search to append the tool inline instead of modifying the array head.  |  
Errors at request time  
| Error  | Cause  | Fix  |  
| --- | --- | --- |  
| `tool_use ids were found without tool_result blocks immediately after`  | Missing `tool_result` for some `tool_use` ids, or `tool_result` is not the first content block in the user message  | Return one `tool_result` for every `tool_use` block in the assistant response. Put `tool_result` blocks before any text. See [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls) and [Parallel tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use).  |  
| `Input schema is not compatible with strict mode: string patterns are not supported`  | Using `pattern` with `strict: true`  | Remove the pattern or drop `strict: true`. The `pattern` keyword is not in the supported JSON Schema subset yet.  |  
| `All tools have defer_loading: true`  | No tools visible to the model  | At least one tool must be immediately loaded. The tool search tool itself must never have `defer_loading: true`.  |  
Error: thinking blocks cannot be modified
If a request fails with a 400 `invalid_request_error` whose message contains ``thinking` or `redacted_thinking` blocks in the latest assistant message cannot be modified` when continuing a conversation after a tool call, your application is altering the assistant's thinking blocks before sending them back. Send the entire assistant message back unchanged, then append your `tool_result`.
See [Thinking blocks cannot be modified](https://platform.claude.com/docs/en/api/errors#thinking-blocks-cannot-be-modified) for the full error and fix steps.
Claude flags tool results as prompt injection  
| Symptom  | Likely cause  | Fix  |  
| --- | --- | --- |  
| Claude refuses to act on a tool result, or asks the user to confirm instructions that came from it  | Your own instructions are being delivered inside the `tool_result` content  | Claude is trained to treat instructions inside tool results as potentially untrusted third-party content. Move your instructions out of the tool result: send them in a `user` turn after the `tool_result` block, or (on Claude Opus 4.8 and later) in a [mid-conversation system message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages). Keep the tool result to just the data. See [Mitigate jailbreaks and prompt injections](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks#indirect-prompt-injection).  |  
JSON escaping differences (Opus 4.6+)  
| Symptom  | Cause  | Fix  |  
| --- | --- | --- |  
| String comparison on tool inputs fails with newer models  | Unicode and forward-slash escaping differs between model versions  | Parse with `json.loads()` or `JSON.parse()`. Never do raw string matching on serialized input.  |  
Next steps
[ Define tools Write schemas and descriptions that steer Claude toward the right tool. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)[ Handle tool calls Execute tools and return results in the required message format. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)[ Tool reference Full directory of Anthropic-schema tools and their version strings. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)
