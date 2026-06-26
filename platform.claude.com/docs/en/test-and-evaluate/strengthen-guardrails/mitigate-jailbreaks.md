<!-- source: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks -->

# Mitigate jailbreaks and prompt injections
Jailbreaking and prompt injection are attempts to make Claude ignore its guidelines or your instructions. While Claude is inherently resilient to such attacks, the additional steps on this page strengthen your guardrails, particularly against uses that violate our [Terms of Service](https://www.anthropic.com/legal/commercial-terms) or [Usage Policy](https://www.anthropic.com/legal/aup).
These attacks fall into two categories with different threat models:
  * **Jailbreaks and direct prompt injection** , where the _user_ of your application is the adversary and crafts inputs intended to bypass your guardrails.
  * **Indirect prompt injection** , where the user is trusted but Claude processes _third-party content_ (web pages, emails, documents, tool results) that contains adversarial instructions.

Jailbreaks and direct prompt injection
In this threat model, a user is deliberately crafting inputs to manipulate your application into producing content or taking actions you don't want it to. These mitigations strengthen your application's guardrails:
  * **Harmlessness screens:** Use a lightweight model like Claude Haiku 4.5 to pre-screen user input before it reaches your main conversation. Use [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) to constrain the response to a simple classification.
### Example: Harmlessness screen for content moderation
  * **Input validation:** Filter user input for known injection patterns before it reaches Claude. You can use an LLM to create a generalized validation screen by providing known jailbreaking language as examples.
  * **Prompt engineering:** Craft system prompts that emphasize ethical and legal boundaries, and that explicitly tell Claude how to refuse.
### Example: Ethical system prompt for an enterprise chatbot
  * **Respond to repeat offenders:** Adjust responses and consider throttling or banning users who repeatedly attempt to circumvent your application's guardrails. For example, if a particular user triggers the same kind of refusal multiple times (such as "output blocked by content filtering policy"), tell the user that their actions violate the relevant usage policies and take action accordingly.

Indirect prompt injection
In this threat model, you're protecting your users from instructions embedded in content that Claude reads on their behalf: the body of an inbound email, a fetched web page, OCR output from an uploaded file, or the result of a tool call. An attacker who can influence that content may embed instructions that try to redirect Claude.
Structure your application so that Claude can reliably distinguish untrusted content from your instructions:
  * **Put untrusted content only in tool results.** Deliver third-party content to Claude inside `tool_result` blocks, never in `system` prompts or plain user `text` blocks. Claude is trained to treat instructions that appear inside tool results with appropriate skepticism. See [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls) for the `tool_result` format.
  * **Tell Claude what the content is and where it came from.** In the tool's `description`, or in the structure of the result itself, make the nature and source of the content explicit: for example, that it is the body of an inbound email from an unknown sender, or OCR text extracted from a user-uploaded image. This context helps Claude calibrate how much to trust embedded directives.
  * **State the policy in your system prompt.** Tell Claude explicitly that content returned from tools, documents, or searches is untrusted data and must never override the system prompt or the user's original request.
### Example: System prompt guidance for a document-processing agent
  * **JSON-encode untrusted content.** Where possible, wrap third-party strings in a JSON object rather than concatenating them into free-form text. JSON escaping provides unambiguous delimiters between the untrusted payload and the surrounding structure, so an attacker cannot close a quote or tag to "break out" into an instruction context.
### Example: JSON-encoded tool result for an inbound email
  * **Don't put your own instructions in tool results.** Because Claude treats tool-result content as untrusted data, instructions you place there may be ignored or flagged as a potential injection. Send your instructions in a `user` turn that follows the `tool_result` block. On Claude Opus 4.8 and later, you can also use a [mid-conversation system message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages).
  * **Limit Claude's access to sensitive data and actions.** Apply the principle of least privilege so that a successful injection can do minimal damage: don't give Claude access to secrets it doesn't need, run tools in sandboxed environments, and scope permissions as narrowly as possible.
  * **Screen tool outputs before Claude acts on them.** Apply the same lightweight-model screening pattern you use for user input to the content your tools return. Run each tool, pass its raw output to a small classifier call with Claude Haiku 4.5, and only return the content as a `tool_result` block if the screen reports no injection attempt. Use [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) so the classifier's verdict is a parseable value your application can branch on.
### Example: Injection screen for tool output
You can also apply the input-validation patterns from the previous section to tool results before passing them to Claude.
  * **Red-team your own agent.** Before deploying, test your workflow with documents, emails, and tool outputs that deliberately contain injection attempts, and confirm that Claude ignores them and that your screening and confirmation steps catch the rest.

If you're using the [computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool), Anthropic runs additional classifiers that detect potential prompt injections in screenshots and steer Claude to ask for user confirmation before acting. See that page for details and opt-out information.
Continuous monitoring
Regularly analyze outputs for signs of successful injection. Use this monitoring to iteratively refine your prompts, validation, and filtering strategies.
Advanced: Chain safeguards
Combine strategies for robust protection. Here's an enterprise-grade example with tool use:
### Example: Multi-layered protection for a financial advisor chatbot
By layering these strategies, you create a robust defense against jailbreaking and prompt injections, ensuring your Claude-powered applications maintain the highest standards of safety and compliance.
  * [Jailbreaks and direct prompt injection](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks#jailbreaks-and-direct-prompt-injection)
  * [Indirect prompt injection](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks#indirect-prompt-injection)
  * [Continuous monitoring](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks#continuous-monitoring)
  * [Advanced: Chain safeguards](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks#advanced-chain-safeguards)
  * [Bot system prompt](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks#bot-system-prompt)
  * [Prompt within harmlessness_screen tool](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks#prompt-within-harmlessness-screen-tool)

Best practices/Strengthen guardrails
# Mitigate jailbreaks and prompt injections
Jailbreaking and prompt injection are attempts to make Claude ignore its guidelines or your instructions. While Claude is inherently resilient to such attacks, the additional steps on this page strengthen your guardrails, particularly against uses that violate our [Terms of Service](https://www.anthropic.com/legal/commercial-terms) or [Usage Policy](https://www.anthropic.com/legal/aup).
These attacks fall into two categories with different threat models:
  * **Jailbreaks and direct prompt injection** , where the _user_ of your application is the adversary and crafts inputs intended to bypass your guardrails.
  * **Indirect prompt injection** , where the user is trusted but Claude processes _third-party content_ (web pages, emails, documents, tool results) that contains adversarial instructions.

Jailbreaks and direct prompt injection
In this threat model, a user is deliberately crafting inputs to manipulate your application into producing content or taking actions you don't want it to. These mitigations strengthen your application's guardrails:
  * **Harmlessness screens:** Use a lightweight model like Claude Haiku 4.5 to pre-screen user input before it reaches your main conversation. Use [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) to constrain the response to a simple classification.
### Example: Harmlessness screen for content moderation
  * **Input validation:** Filter user input for known injection patterns before it reaches Claude. You can use an LLM to create a generalized validation screen by providing known jailbreaking language as examples.
  * **Prompt engineering:** Craft system prompts that emphasize ethical and legal boundaries, and that explicitly tell Claude how to refuse.
### Example: Ethical system prompt for an enterprise chatbot
  * **Respond to repeat offenders:** Adjust responses and consider throttling or banning users who repeatedly attempt to circumvent your application's guardrails. For example, if a particular user triggers the same kind of refusal multiple times (such as "output blocked by content filtering policy"), tell the user that their actions violate the relevant usage policies and take action accordingly.

Indirect prompt injection
In this threat model, you're protecting your users from instructions embedded in content that Claude reads on their behalf: the body of an inbound email, a fetched web page, OCR output from an uploaded file, or the result of a tool call. An attacker who can influence that content may embed instructions that try to redirect Claude.
Structure your application so that Claude can reliably distinguish untrusted content from your instructions:
  * **Put untrusted content only in tool results.** Deliver third-party content to Claude inside `tool_result` blocks, never in `system` prompts or plain user `text` blocks. Claude is trained to treat instructions that appear inside tool results with appropriate skepticism. See [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls) for the `tool_result` format.
  * **Tell Claude what the content is and where it came from.** In the tool's `description`, or in the structure of the result itself, make the nature and source of the content explicit: for example, that it is the body of an inbound email from an unknown sender, or OCR text extracted from a user-uploaded image. This context helps Claude calibrate how much to trust embedded directives.
  * **State the policy in your system prompt.** Tell Claude explicitly that content returned from tools, documents, or searches is untrusted data and must never override the system prompt or the user's original request.
### Example: System prompt guidance for a document-processing agent
  * **JSON-encode untrusted content.** Where possible, wrap third-party strings in a JSON object rather than concatenating them into free-form text. JSON escaping provides unambiguous delimiters between the untrusted payload and the surrounding structure, so an attacker cannot close a quote or tag to "break out" into an instruction context.
### Example: JSON-encoded tool result for an inbound email
  * **Don't put your own instructions in tool results.** Because Claude treats tool-result content as untrusted data, instructions you place there may be ignored or flagged as a potential injection. Send your instructions in a `user` turn that follows the `tool_result` block. On Claude Opus 4.8 and later, you can also use a [mid-conversation system message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages).
  * **Limit Claude's access to sensitive data and actions.** Apply the principle of least privilege so that a successful injection can do minimal damage: don't give Claude access to secrets it doesn't need, run tools in sandboxed environments, and scope permissions as narrowly as possible.
  * **Screen tool outputs before Claude acts on them.** Apply the same lightweight-model screening pattern you use for user input to the content your tools return. Run each tool, pass its raw output to a small classifier call with Claude Haiku 4.5, and only return the content as a `tool_result` block if the screen reports no injection attempt. Use [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) so the classifier's verdict is a parseable value your application can branch on.
### Example: Injection screen for tool output
You can also apply the input-validation patterns from the previous section to tool results before passing them to Claude.
  * **Red-team your own agent.** Before deploying, test your workflow with documents, emails, and tool outputs that deliberately contain injection attempts, and confirm that Claude ignores them and that your screening and confirmation steps catch the rest.

If you're using the [computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool), Anthropic runs additional classifiers that detect potential prompt injections in screenshots and steer Claude to ask for user confirmation before acting. See that page for details and opt-out information.
Continuous monitoring
Regularly analyze outputs for signs of successful injection. Use this monitoring to iteratively refine your prompts, validation, and filtering strategies.
Advanced: Chain safeguards
Combine strategies for robust protection. Here's an enterprise-grade example with tool use:
### Example: Multi-layered protection for a financial advisor chatbot
By layering these strategies, you create a robust defense against jailbreaking and prompt injections, ensuring your Claude-powered applications maintain the highest standards of safety and compliance.
