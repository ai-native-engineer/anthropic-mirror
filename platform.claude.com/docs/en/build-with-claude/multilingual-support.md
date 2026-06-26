<!-- source: https://platform.claude.com/docs/en/build-with-claude/multilingual-support -->

# Multilingual support
Claude excels at tasks across multiple languages, maintaining strong cross-lingual performance relative to English.
Overview
Claude demonstrates robust multilingual capabilities, with particularly strong performance in zero-shot tasks across languages. The model maintains consistent relative performance across both widely spoken and lower-resource languages, making it a reliable choice for multilingual applications.
Claude is capable in many languages beyond those benchmarked in the following table. Test with any languages relevant to your specific use cases.
Performance data
The following table shows zero-shot chain-of-thought evaluation scores for Claude models across languages, expressed as a percentage relative to English performance (100%):  
| Language  | Claude Opus 4.1 (deprecated)1  | Claude Sonnet 4.51  | Claude Haiku 4.51  |  
| --- | --- | --- | --- |  
| English (baseline, fixed to 100%)  | 100%  | 100%  | 100%  |  
| Spanish  | 98.1%  | 98.2%  | 96.4%  |  
| Portuguese (Brazil)  | 97.8%  | 97.8%  | 96.1%  |  
| Italian  | 97.7%  | 97.9%  | 96.0%  |  
| French  | 97.9%  | 97.5%  | 95.7%  |  
| Indonesian  | 97.3%  | 97.3%  | 94.2%  |  
| German  | 97.7%  | 97.0%  | 94.3%  |  
| Arabic  | 97.1%  | 97.2%  | 92.5%  |  
| Chinese (Simplified)  | 97.1%  | 96.9%  | 94.2%  |  
| Korean  | 96.6%  | 96.7%  | 93.3%  |  
| Japanese  | 96.9%  | 96.8%  | 93.5%  |  
| Hindi  | 96.8%  | 96.7%  | 92.4%  |  
| Bengali  | 95.7%  | 95.4%  | 90.4%  |  
| Swahili  | 89.8%  | 91.1%  | 78.3%  |  
| Yoruba  | 80.3%  | 79.7%  | 52.7%  |  
1 With [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking).
These metrics are based on [MMLU (Massive Multitask Language Understanding)](https://en.wikipedia.org/wiki/MMLU) English test sets that were translated into 14 additional languages by professional human translators, as documented in [OpenAI's simple-evals repository](https://github.com/openai/simple-evals/blob/main/multilingual_mmlu_benchmark_results.md). The use of human translators for this evaluation ensures high-quality translations, particularly important for languages with fewer digital resources.
* * *
Set the response language
Claude infers the response language from the conversation, but for production applications you should state the target language explicitly. The most reliable place to do this is the system prompt, which keeps the instruction stable across every turn of a conversation.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    system="Always respond in French, regardless of the language the user writes in.",
    messages=[{"role": "user", "content": "How do I reset my password?"}],
)

print(message.content)

If your application lets users pick a language at runtime, interpolate that choice into the system prompt rather than relying on Claude to infer it from the user's message. To translate between two specific languages, name both: `Translate the user's message from German to Korean. Respond with only the translation.`
* * *
Best practices
When working with multilingual content:
  1. **Provide clear language context:** Although Claude can detect the target language automatically, explicitly stating the desired input and output languages improves reliability. For enhanced fluency, you can prompt Claude to use "idiomatic speech as if it were a native speaker."
  2. **Use native scripts:** Submit text in its native script rather than transliteration for optimal results.
  3. **Consider cultural context:** Effective communication often requires cultural and regional awareness beyond pure translation.

Also follow the general guidance in [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) to further improve output quality.
* * *
Language support considerations
  * Claude processes input and generates output in most world languages that use standard Unicode characters.
  * Performance varies by language, with particularly strong capabilities in widely spoken languages.
  * Even in languages with fewer digital resources, Claude maintains meaningful capabilities.

Next steps
[  Prompt engineering overview Apply general prompting techniques to improve multilingual output quality. ](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)[ Customer support agent Build a localized support chatbot using a language-constrained system prompt. ](https://platform.claude.com/docs/en/about-claude/use-case-guides/customer-support-chat)[ Models overview Compare model tiers to balance multilingual quality against cost and latency. ](https://platform.claude.com/docs/en/about-claude/models/overview)[ Define success criteria and build evaluations Evaluate translation and localization quality before you ship. ](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
  * [Overview](https://platform.claude.com/docs/en/build-with-claude/multilingual-support#overview)
  * [Performance data](https://platform.claude.com/docs/en/build-with-claude/multilingual-support#performance-data)
  * [Set the response language](https://platform.claude.com/docs/en/build-with-claude/multilingual-support#set-the-response-language)
  * [Best practices](https://platform.claude.com/docs/en/build-with-claude/multilingual-support#best-practices)
  * [Language support considerations](https://platform.claude.com/docs/en/build-with-claude/multilingual-support#language-support-considerations)
  * [Next steps](https://platform.claude.com/docs/en/build-with-claude/multilingual-support#next-steps)

Messages/Model capabilities
# Multilingual support
Claude excels at tasks across multiple languages, maintaining strong cross-lingual performance relative to English.
Overview
Claude demonstrates robust multilingual capabilities, with particularly strong performance in zero-shot tasks across languages. The model maintains consistent relative performance across both widely spoken and lower-resource languages, making it a reliable choice for multilingual applications.
Claude is capable in many languages beyond those benchmarked in the following table. Test with any languages relevant to your specific use cases.
Performance data
The following table shows zero-shot chain-of-thought evaluation scores for Claude models across languages, expressed as a percentage relative to English performance (100%):  
| Language  | Claude Opus 4.1 (deprecated)1  | Claude Sonnet 4.51  | Claude Haiku 4.51  |  
| --- | --- | --- | --- |  
| English (baseline, fixed to 100%)  | 100%  | 100%  | 100%  |  
| Spanish  | 98.1%  | 98.2%  | 96.4%  |  
| Portuguese (Brazil)  | 97.8%  | 97.8%  | 96.1%  |  
| Italian  | 97.7%  | 97.9%  | 96.0%  |  
| French  | 97.9%  | 97.5%  | 95.7%  |  
| Indonesian  | 97.3%  | 97.3%  | 94.2%  |  
| German  | 97.7%  | 97.0%  | 94.3%  |  
| Arabic  | 97.1%  | 97.2%  | 92.5%  |  
| Chinese (Simplified)  | 97.1%  | 96.9%  | 94.2%  |  
| Korean  | 96.6%  | 96.7%  | 93.3%  |  
| Japanese  | 96.9%  | 96.8%  | 93.5%  |  
| Hindi  | 96.8%  | 96.7%  | 92.4%  |  
| Bengali  | 95.7%  | 95.4%  | 90.4%  |  
| Swahili  | 89.8%  | 91.1%  | 78.3%  |  
| Yoruba  | 80.3%  | 79.7%  | 52.7%  |  
1 With [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking).
These metrics are based on [MMLU (Massive Multitask Language Understanding)](https://en.wikipedia.org/wiki/MMLU) English test sets that were translated into 14 additional languages by professional human translators, as documented in [OpenAI's simple-evals repository](https://github.com/openai/simple-evals/blob/main/multilingual_mmlu_benchmark_results.md). The use of human translators for this evaluation ensures high-quality translations, particularly important for languages with fewer digital resources.
* * *
Set the response language
Claude infers the response language from the conversation, but for production applications you should state the target language explicitly. The most reliable place to do this is the system prompt, which keeps the instruction stable across every turn of a conversation.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    system="Always respond in French, regardless of the language the user writes in.",
    messages=[{"role": "user", "content": "How do I reset my password?"}],
)

print(message.content)

If your application lets users pick a language at runtime, interpolate that choice into the system prompt rather than relying on Claude to infer it from the user's message. To translate between two specific languages, name both: `Translate the user's message from German to Korean. Respond with only the translation.`
* * *
Best practices
When working with multilingual content:
  1. **Provide clear language context:** Although Claude can detect the target language automatically, explicitly stating the desired input and output languages improves reliability. For enhanced fluency, you can prompt Claude to use "idiomatic speech as if it were a native speaker."
  2. **Use native scripts:** Submit text in its native script rather than transliteration for optimal results.
  3. **Consider cultural context:** Effective communication often requires cultural and regional awareness beyond pure translation.

Also follow the general guidance in [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) to further improve output quality.
* * *
Language support considerations
  * Claude processes input and generates output in most world languages that use standard Unicode characters.
  * Performance varies by language, with particularly strong capabilities in widely spoken languages.
  * Even in languages with fewer digital resources, Claude maintains meaningful capabilities.

Next steps
[  Prompt engineering overview Apply general prompting techniques to improve multilingual output quality. ](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)[ Customer support agent Build a localized support chatbot using a language-constrained system prompt. ](https://platform.claude.com/docs/en/about-claude/use-case-guides/customer-support-chat)[ Models overview Compare model tiers to balance multilingual quality against cost and latency. ](https://platform.claude.com/docs/en/about-claude/models/overview)[ Define success criteria and build evaluations Evaluate translation and localization quality before you ship. ](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
