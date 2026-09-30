<!-- source: https://support.claude.com/en/articles/12449294-understanding-sonnet-4-5-s-api-safety-filters -->

# Understanding Sonnet 4.5's API Safety Filters

March 16, 2026

Table of contents

Claude Sonnet 4.5 includes new AI Safety Level 3 (ASL-3) protections designed to prevent misuse related to chemical, biological, radiological, and nuclear (CBRN) weapons. These safety measures use Constitutional Classifiers that monitor inputs and outputs to block a narrow category of harmful content.

## Why was my API request blocked?

Sonnet 4.5's safety filters are narrowly focused on preventing assistance with CBRN weapons-related tasks. If your request was blocked, the filters detected content that matched patterns associated with these specific threats.

**These filters are still being refined.** As with any automated system, false positives can occur—meaning legitimate requests may occasionally be flagged incorrectly. We're actively working to improve the precision of these classifiers to minimize disruption while maintaining safety.

## What you can do

If your API request is blocked, here are steps you can take:

### Avoid patterns that trigger false positives

The classifiers are sensitive to certain patterns that may resemble jailbreak attempts or obfuscation techniques:

* **Avoid cipher-like content**: Base64-encoded strings, git commit hashes, hexadecimal sequences, and other encoded data can trigger the filters. If you need to include such content, consider whether it's essential to your use case.
* **Simplify system instructions**: Overly long or complex system prompts that include intricate conditional logic may resemble attempts to obfuscate behavior. Keep system instructions clear and straightforward.
* **Be cautious with biology-related content**: If your application doesn't specifically require biological or chemical information, consider rephrasing requests to avoid these topics when possible.

### Switch to Sonnet 4

Use Sonnet 4 instead of Sonnet 4.5 in your API calls. Sonnet 4 uses different safety measures and may be able to process your request successfully.

### Implement fallback logic

Build error handling into your application that can:

* Detect when a request is blocked by safety filters.
* Automatically retry with Sonnet 4 as a fallback.
* Log incidents for your review to identify patterns in false positives.

### Provide feedback

If you believe your request was incorrectly blocked, contact our [API support team](https://support.claude.com/en/articles/9015913-how-to-get-support#h_beb6d0c9ce). Your feedback helps us improve filter accuracy and reduce false positives for legitimate use cases.

## Why the new filters?

As AI models become more capable, they require stronger protections against potential misuse. Sonnet 4.5's ASL-3 deployment measures are part of Anthropic's [Responsible Scaling Policy](https://www.anthropic.com/news/activating-asl3-protections), which ensures that increasingly capable models have appropriate safeguards.

The filters are specifically designed to prevent extended, end-to-end CBRN workflows that could pose catastrophic risks. They are **not** intended to block general scientific discussion, educational content, or commonly available information.

## For researchers and dual-use applications

If you're building applications for scientific research or dual-use technology fields and need access for legitimate purposes, we've established access control systems for vetted users. Contact our [API support team](https://support.claude.com/en/articles/9015913-how-to-get-support#h_beb6d0c9ce) to learn more about exemptions.

---

Related Articles

* [Model Safety Bug Bounty Program](https://support.claude.com/en/articles/12119250-model-safety-bug-bounty-program)
* [Real-time cyber safeguards on Claude Opus and Sonnet](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude-opus-and-sonnet)
* [Why Claude switched models in your conversation with Fable 5 or Fable 5.1](https://support.claude.com/en/articles/15363606-why-claude-switched-models-in-your-conversation-with-fable-5-or-fable-5-1)
* [Why Claude switched models in your conversation with Opus 5 or Opus 5.5](https://support.claude.com/en/articles/16049681-why-claude-switched-models-in-your-conversation-with-opus-5-or-opus-5-5)
* [Why Claude switched models in your conversation with Sonnet 5.5](https://support.claude.com/en/articles/17161993-why-claude-switched-models-in-your-conversation-with-sonnet-5-5)

Disappointed Reaction😞Neutral Reaction😐Smiley Reaction😃

Table of contents
