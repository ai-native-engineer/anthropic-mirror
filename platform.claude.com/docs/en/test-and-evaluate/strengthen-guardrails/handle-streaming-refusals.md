<!-- source: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals -->

# Streaming refusals
Detect and handle refusal stop reasons in streaming responses, and retry refused requests on a fallback model.
Starting with Claude 4 models, streaming responses from Claude's API return **`stop_reason`:`"refusal"`** when streaming classifiers intervene to handle potential policy violations. This safety feature helps maintain content compliance during real-time streaming.

This page covers how refusals appear in streaming responses. For every `stop_reason` value and how to handle it, see [Stop reasons and fallback](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons). To retry refused requests on another Claude model, see [Refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback).
API response format
When streaming classifiers detect content that violates Anthropic's policies, the API returns this response:

  "role": "assistant",
  "content": [
      "type": "text",
      "text": "Hello.."
  ],
  "stop_reason": "refusal"


No additional refusal message is included. You must handle the response and provide appropriate user-facing messaging.
Reset context after refusal
When you receive **`stop_reason`:`refusal`** , you must reset the conversation context before continuing. You can remove or rephrase the turn that triggered the refusal, or clear the conversation history entirely. Attempting to continue without resetting will result in continued refusals.
Usage metrics are still provided in the response, even when the response is refused.
When a refusal arrives before Claude generates any output, you are not billed for the request on the Claude API, and the usage counts in that response are informational only. When Claude generates output before the refusal, you are billed for that request.

Resetting context is not the only way to recover. You can also retry the refused request on a different Claude model, and the [Refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback) page shows how to set that up with server-side fallback, the SDK middleware, or a manual retry.
Implementation guide
Here's how to detect and handle streaming refusals in your application:
cURLPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()
messages = []

def reset_conversation():
    """Reset conversation context after refusal"""
    global messages
    messages = []
    print("Conversation reset due to refusal")

try:
    with client.messages.stream(
        max_tokens=1024,
        messages=messages + [{"role": "user", "content": "Hello"}],
        model="claude-opus-4-8",
    ) as stream:
        for event in stream:
            # Check for refusal in message delta
            if event.type == "message_delta":
                if event.delta.stop_reason == "refusal":
                    reset_conversation()
                    break
except Exception as e:
    print(f"Error: {e}")

Current refusal types
The API currently handles refusals in three different ways:  
| Refusal Type  | Response Format  | When It Occurs  |  
| --- | --- | --- |  
| Streaming classifier refusals  | **`stop_reason`:`refusal`**  | During streaming when content violates policies  |  
| API input and copyright validation  | 400 error codes  | When input fails validation checks  |  
| Model-generated refusals  | Standard text responses  | When the model itself decides to refuse  |  
Future API versions will expand the **`stop_reason`:`refusal`** pattern to unify refusal handling across all types.
Best practices
  * **Monitor for refusals:** Include **`stop_reason`:`refusal`** checks in your error handling
  * **Reset automatically:** Implement automatic context reset when refusals are detected
  * **Fall back to another model:** Configure [server-side fallback or the SDK middleware](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback) so refused requests are retried on another Claude model instead of surfacing a refusal to the user
  * **Redeem fallback credit on manual retries:** If you build the retry yourself, pass the refusal's [fallback credit](https://platform.claude.com/docs/en/build-with-claude/fallback-credit) token so the retry doesn't pay the prompt-cache cost twice
  * **Provide custom messaging:** Create user-friendly messages for better UX when refusals occur
  * **Track refusal patterns:** Monitor refusal frequency to identify potential issues with your prompts

Migration notes
If you built refusal handling when this feature first shipped, or you're adding it to an existing integration, check the following:
  * **Refusals are responses, not errors.** A refusal arrives as a successful HTTP 200 response with `stop_reason`: `"refusal"`, so monitoring built only on error rates won't surface it. Track refusals as their own signal.
  * **Newer models return more detail.** On Claude Fable 5, a refusal also includes a `stop_details` object that identifies the policy category behind the decline. See [Refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#refusal-response) for the full response shape.
  * **Retry on a different model.** Re-sending a refused request to the same model usually results in another refusal. Instead of only resetting context, retry on a fallback model with [server-side fallback, the SDK middleware, or a manual retry](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback), and redeem [fallback credit](https://platform.claude.com/docs/en/build-with-claude/fallback-credit) when you build the retry yourself.
  * **Check batch results for refusals.** A refused request in a [Message Batch](https://platform.claude.com/docs/en/build-with-claude/batch-processing) is returned as a succeeded result with `stop_reason`: `"refusal"`, not as an errored result.
  * **Centralize handling on`stop_reason`.** The API continues to consolidate refusal handling around `stop_reason`: `"refusal"`, so branch on the stop reason rather than on model-specific behavior.

Next steps
[ Refusals and fallback Retry refused requests on another Claude model, server-side or in your client. ](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)[  Stop reasons and fallback Every `stop_reason` value and how to handle it. ](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)[  Streaming messages Stream responses and read `stop_reason` from `message_delta` events as they arrive. ](https://platform.claude.com/docs/en/build-with-claude/streaming)[  Multilingual support Serve users across languages with Claude's cross-lingual capabilities. ](https://platform.claude.com/docs/en/build-with-claude/multilingual-support)
  * [API response format](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals#api-response-format)
  * [Reset context after refusal](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals#reset-context-after-refusal)
  * [Implementation guide](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals#implementation-guide)
  * [Current refusal types](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals#current-refusal-types)
  * [Best practices](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals#best-practices)
  * [Migration notes](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals#migration-notes)
  * [Next steps](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals#next-steps)

Messages/Model capabilities
# Streaming refusals
Detect and handle refusal stop reasons in streaming responses, and retry refused requests on a fallback model.
Starting with Claude 4 models, streaming responses from Claude's API return **`stop_reason`:`"refusal"`** when streaming classifiers intervene to handle potential policy violations. This safety feature helps maintain content compliance during real-time streaming.

This page covers how refusals appear in streaming responses. For every `stop_reason` value and how to handle it, see [Stop reasons and fallback](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons). To retry refused requests on another Claude model, see [Refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback).
API response format
When streaming classifiers detect content that violates Anthropic's policies, the API returns this response:

  "role": "assistant",
  "content": [
      "type": "text",
      "text": "Hello.."
  ],
  "stop_reason": "refusal"


No additional refusal message is included. You must handle the response and provide appropriate user-facing messaging.
Reset context after refusal
When you receive **`stop_reason`:`refusal`** , you must reset the conversation context before continuing. You can remove or rephrase the turn that triggered the refusal, or clear the conversation history entirely. Attempting to continue without resetting will result in continued refusals.
Usage metrics are still provided in the response, even when the response is refused.
When a refusal arrives before Claude generates any output, you are not billed for the request on the Claude API, and the usage counts in that response are informational only. When Claude generates output before the refusal, you are billed for that request.

Resetting context is not the only way to recover. You can also retry the refused request on a different Claude model, and the [Refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback) page shows how to set that up with server-side fallback, the SDK middleware, or a manual retry.
Implementation guide
Here's how to detect and handle streaming refusals in your application:
cURLPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()
messages = []

def reset_conversation():
    """Reset conversation context after refusal"""
    global messages
    messages = []
    print("Conversation reset due to refusal")

try:
    with client.messages.stream(
        max_tokens=1024,
        messages=messages + [{"role": "user", "content": "Hello"}],
        model="claude-opus-4-8",
    ) as stream:
        for event in stream:
            # Check for refusal in message delta
            if event.type == "message_delta":
                if event.delta.stop_reason == "refusal":
                    reset_conversation()
                    break
except Exception as e:
    print(f"Error: {e}")

Current refusal types
The API currently handles refusals in three different ways:  
| Refusal Type  | Response Format  | When It Occurs  |  
| --- | --- | --- |  
| Streaming classifier refusals  | **`stop_reason`:`refusal`**  | During streaming when content violates policies  |  
| API input and copyright validation  | 400 error codes  | When input fails validation checks  |  
| Model-generated refusals  | Standard text responses  | When the model itself decides to refuse  |  
Future API versions will expand the **`stop_reason`:`refusal`** pattern to unify refusal handling across all types.
Best practices
  * **Monitor for refusals:** Include **`stop_reason`:`refusal`** checks in your error handling
  * **Reset automatically:** Implement automatic context reset when refusals are detected
  * **Fall back to another model:** Configure [server-side fallback or the SDK middleware](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback) so refused requests are retried on another Claude model instead of surfacing a refusal to the user
  * **Redeem fallback credit on manual retries:** If you build the retry yourself, pass the refusal's [fallback credit](https://platform.claude.com/docs/en/build-with-claude/fallback-credit) token so the retry doesn't pay the prompt-cache cost twice
  * **Provide custom messaging:** Create user-friendly messages for better UX when refusals occur
  * **Track refusal patterns:** Monitor refusal frequency to identify potential issues with your prompts

Migration notes
If you built refusal handling when this feature first shipped, or you're adding it to an existing integration, check the following:
  * **Refusals are responses, not errors.** A refusal arrives as a successful HTTP 200 response with `stop_reason`: `"refusal"`, so monitoring built only on error rates won't surface it. Track refusals as their own signal.
  * **Newer models return more detail.** On Claude Fable 5, a refusal also includes a `stop_details` object that identifies the policy category behind the decline. See [Refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#refusal-response) for the full response shape.
  * **Retry on a different model.** Re-sending a refused request to the same model usually results in another refusal. Instead of only resetting context, retry on a fallback model with [server-side fallback, the SDK middleware, or a manual retry](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback), and redeem [fallback credit](https://platform.claude.com/docs/en/build-with-claude/fallback-credit) when you build the retry yourself.
  * **Check batch results for refusals.** A refused request in a [Message Batch](https://platform.claude.com/docs/en/build-with-claude/batch-processing) is returned as a succeeded result with `stop_reason`: `"refusal"`, not as an errored result.
  * **Centralize handling on`stop_reason`.** The API continues to consolidate refusal handling around `stop_reason`: `"refusal"`, so branch on the stop reason rather than on model-specific behavior.

Next steps
[ Refusals and fallback Retry refused requests on another Claude model, server-side or in your client. ](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)[  Stop reasons and fallback Every `stop_reason` value and how to handle it. ](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)[  Streaming messages Stream responses and read `stop_reason` from `message_delta` events as they arrive. ](https://platform.claude.com/docs/en/build-with-claude/streaming)[  Multilingual support Serve users across languages with Claude's cross-lingual capabilities. ](https://platform.claude.com/docs/en/build-with-claude/multilingual-support)
