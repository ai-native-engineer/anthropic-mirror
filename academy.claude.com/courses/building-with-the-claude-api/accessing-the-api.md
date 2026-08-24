<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/accessing-the-api -->

Lesson 1 of 67 · Building with the Claude APIAccessing the API

When building applications with Claude, understanding the complete request lifecycle helps you make better architectural decisions and debug issues more effectively. Let's walk through what happens from the moment a user clicks "send" in your chat interface to when Claude's response appears on screen.

![](https://academy.claude.com/assets/media/2a8244ea430c62fdba1dc04c5a8be19c3521ef69da5867972b57cffa5330668a.png)

## The Five-Step Request Flow

Every interaction with Claude follows a predictable pattern with five distinct phases: request to server, request to Anthropic API, model processing, response to server, and response to client.

![](https://academy.claude.com/assets/media/f2be1422feb4399a4ecba83971b60af28f5e24d17216187cc556c028010e81c0.png)

## Why You Need a Server

You should never make requests to the Anthropic API directly from client-side code. Here's why:

* API requests require a secret API key for authentication
* Exposing this key in client code creates a serious security vulnerability
* Anyone could extract the key and make unauthorized requests

Instead, your web or mobile app sends requests to your own server, which then communicates with the Anthropic API using the securely stored key.

## Making API Requests

When your server contacts the Anthropic API, you can use either an official SDK or make plain HTTP requests. Anthropic provides SDKs for Python, TypeScript, JavaScript, Go, and Ruby.

![](https://academy.claude.com/assets/media/0493a78d946db722b5fbc9f4159087862d456795fbf9fe40e36810953d7752d1.png)

Every request must include these essential fields:

* **API Key** - Identifies your request to Anthropic
* **Model** - Name of the model to use (like "claude-sonnet-4-5")
* **Messages** - List containing the user's input text
* **Max Tokens** - Limit for how many tokens Claude can generate

## Inside Claude's Processing

Once Anthropic receives your request, Claude processes it through four main stages: tokenization, embedding, contextualization, and generation.

![](https://academy.claude.com/assets/media/704feacd29e60dae08515ac27f3e9ddcb3eddb08106d4f7f3b002d15cd0b313f.png)

### Tokenization

Claude first breaks your input text into smaller chunks called tokens. These can be whole words, parts of words, spaces, or symbols. For simplicity, think of each word as one token.

### Embedding

Each token gets converted into an embedding - a long list of numbers that represents all possible meanings of that word. Think of embeddings as numerical definitions that capture semantic relationships.

![](https://academy.claude.com/assets/media/15f619b73e9b8952cc63089b361503b08988f46c87d5697006a6b3c9387ab916.png)

Words often have multiple meanings. For example, "quantum" could refer to:

* A discrete unit of physical quantity (physics)
* Quantum mechanics or quantum physics concepts
* Something extremely small or subatomic
* Quantum computing applications

### Contextualization

Claude refines each embedding based on surrounding words to determine the most likely meaning in context. This process adjusts the numerical representations to highlight the appropriate definition.

![](https://academy.claude.com/assets/media/e2001111a3cedb337f59a6d1768fef3e42b173f2d6179906efb70a5d30e72ded.png)

### Generation

The contextualized embeddings pass through an output layer that calculates probabilities for each possible next word. Claude doesn't always pick the highest probability word - it uses a mix of probability and controlled randomness to create natural, varied responses.

![](https://academy.claude.com/assets/media/05f4f7ac62981908ebfab9b6c1e9275063d2f9bbe9803e8044701d315659283a.png)

After selecting each word, Claude adds it to the sequence and repeats the entire process for the next word.

## When Claude Stops Generating

After each token, Claude checks several conditions to decide whether to continue:

![](https://academy.claude.com/assets/media/03c7c33b48f1a1fa54cdc99021b279a5626fe6156e80a8bd122c9fef23799f16.png)

* **Max tokens reached** - Has it hit the limit you specified?
* **Natural ending** - Did it generate an end-of-sequence token?
* **Stop sequence** - Did it encounter a predefined stop phrase?

## The API Response

When generation completes, the API sends back a structured response containing:

* **Message** - The generated text
* **Usage** - Count of input and output tokens
* **Stop Reason** - Why generation ended

![](https://academy.claude.com/assets/media/e23c1a9b0b32516371d83b64dfa477347342a7de1fa33781bb3edacdfe9af1c6.png)

Your server receives this response and forwards the generated text back to your client application, where it appears in the user interface.

![](https://academy.claude.com/assets/media/76fd18d820096e675367b412d908db48d94e83ba107b5fea7a7fa2495ea4dd47.png)

## Key Takeaways

Understanding this flow helps you:

* Design secure architectures that protect your API keys
* Set appropriate token limits for your use case
* Handle different stop reasons in your application logic
* Debug issues by understanding where they might occur in the pipeline

Don't worry about memorizing every detail - the goal is familiarizing yourself with the terminology and overall process you'll encounter when working with Claude's API.
