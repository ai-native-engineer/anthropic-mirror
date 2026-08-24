<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/accessing-the-api -->

Lesson 2 of 65 · Claude with Amazon BedrockAccessing the API

When building applications with AI models, you need to understand the flow of data from user input to AI-generated response. Let's walk through how this works with AWS Bedrock and see what happens behind the scenes of a typical chat application.

## How Chat Applications Work

Imagine you're building a web app with a simple chat interface. A user types "Define quantum computing" and clicks send. Here's what actually happens:

![](https://academy.claude.com/assets/media/a9c72daeb24f83fa87d52cfed393802d1f0eec02321d33ca62ec1157b2209994.png)

The user sees a clean interface, but there's a whole system working behind the scenes to generate that response.

![](https://academy.claude.com/assets/media/a284df9b084d1be4f287063287e0921d7d7a0b72b76b356133441a1ae560aefb.png)

## The Request Flow

When a user submits text, here's the journey that message takes:

![](https://academy.claude.com/assets/media/b3679770256fc4a3265da2a03f6de06166c3e11bf774a363e346b490b342609e.png)

1. User submits their message through your web interface
2. Your server receives the request containing that text
3. Your server uses the Bedrock client to make a request to AWS Bedrock
4. The request includes the user message and a model ID (like Claude Haiku or Claude Sonnet)
5. The chosen model processes the request and generates text
6. AWS Bedrock sends back an assistant message containing the generated response
7. Your server forwards this response back to the user's browser

![](https://academy.claude.com/assets/media/690c3eacfdc89aa2c8ec08c3e65d62f3fbea86d0f6aa218b18c10b3031620d9e.png)
