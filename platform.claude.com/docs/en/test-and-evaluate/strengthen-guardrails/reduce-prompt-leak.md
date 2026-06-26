<!-- source: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak -->

# Reduce prompt leak
Prompt leaks can expose sensitive information that you expect to be "hidden" in your prompt. While no method is foolproof, the strategies below can significantly reduce the risk.
Before you try to reduce prompt leak
Consider using leak-resistant prompt engineering strategies only when **absolutely necessary**. Attempts to leak-proof your prompt can add complexity that may degrade performance in other parts of the task due to increasing the complexity of the LLM’s overall task.
If you decide to implement leak-resistant techniques, be sure to test your prompts thoroughly to ensure that the added complexity does not negatively impact the model’s performance or the quality of its outputs.

Try monitoring techniques first, like output screening and post-processing, to try to catch instances of prompt leak.
* * *
Strategies to reduce prompt leak
  * **Separate context from queries:** You can try using system prompts to isolate key information and context from user queries. You can emphasize key instructions in the `User` turn, then reemphasize those instructions by prefilling the `Assistant` turn. (Note: prefilling is not supported on Claude Fable 5, [Claude Mythos 5](https://anthropic.com/glasswing), [Claude Mythos Preview](https://anthropic.com/glasswing), Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6.)

### Example: Safeguarding proprietary analytics
  * **Use post-processing** : Filter Claude's outputs for keywords that might indicate a leak. Techniques include using regular expressions, keyword filtering, or other text processing methods. 
You can also use a prompted LLM to filter outputs for more nuanced leaks.
  * **Avoid unnecessary proprietary details** : If Claude doesn't need it to perform the task, don't include it. Extra content distracts Claude from focusing on "no leak" instructions.
  * **Regular audits** : Periodically review your prompts and Claude's outputs for potential leaks.

Remember, the goal is not just to prevent leaks but to maintain Claude's performance. Overly complex leak-prevention can degrade results. Balance is key.
  * [Before you try to reduce prompt leak](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak#before-you-try-to-reduce-prompt-leak)
  * [Strategies to reduce prompt leak](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak#strategies-to-reduce-prompt-leak)

Best practices/Strengthen guardrails
# Reduce prompt leak
Prompt leaks can expose sensitive information that you expect to be "hidden" in your prompt. While no method is foolproof, the strategies below can significantly reduce the risk.
Before you try to reduce prompt leak
Consider using leak-resistant prompt engineering strategies only when **absolutely necessary**. Attempts to leak-proof your prompt can add complexity that may degrade performance in other parts of the task due to increasing the complexity of the LLM’s overall task.
If you decide to implement leak-resistant techniques, be sure to test your prompts thoroughly to ensure that the added complexity does not negatively impact the model’s performance or the quality of its outputs.

Try monitoring techniques first, like output screening and post-processing, to try to catch instances of prompt leak.
* * *
Strategies to reduce prompt leak
  * **Separate context from queries:** You can try using system prompts to isolate key information and context from user queries. You can emphasize key instructions in the `User` turn, then reemphasize those instructions by prefilling the `Assistant` turn. (Note: prefilling is not supported on Claude Fable 5, [Claude Mythos 5](https://anthropic.com/glasswing), [Claude Mythos Preview](https://anthropic.com/glasswing), Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6.)

### Example: Safeguarding proprietary analytics
  * **Use post-processing** : Filter Claude's outputs for keywords that might indicate a leak. Techniques include using regular expressions, keyword filtering, or other text processing methods. 
You can also use a prompted LLM to filter outputs for more nuanced leaks.
  * **Avoid unnecessary proprietary details** : If Claude doesn't need it to perform the task, don't include it. Extra content distracts Claude from focusing on "no leak" instructions.
  * **Regular audits** : Periodically review your prompts and Claude's outputs for potential leaks.

Remember, the goal is not just to prevent leaks but to maintain Claude's performance. Overly complex leak-prevention can degrade results. Balance is key.
