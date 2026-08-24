<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/routing-workflows -->

Lesson 63 of 66 · Claude with Google Cloud's Vertex AIRouting workflows

When building AI applications, you'll often need different approaches for different types of user requests. A routing workflow solves this by categorizing user input first, then directing it to specialized processing pipelines.

## The Problem with One-Size-Fits-All Prompts

Consider a social media marketing tool that generates video scripts from user topics. If someone enters "programming" versus "surfing", you'd want very different outputs:

* **Programming topic** - Educational script with clear definitions, examples, and structured explanations
* **Surfing topic** - Entertainment-focused script with engaging hooks and trendy language, not technical definitions

![](https://academy.claude.com/assets/media/1580d75445986d7c7622eda18603cd9077e70a3fe3c55046aba5a79a89a209a4.png)

Using the same generic prompt for both topics would produce mediocre results that don't match the content's natural style.

## Setting Up Content Categories

Start by defining the different types of content your application might need to handle. For video scripts, you might use categories like:

* Entertainment
* Educational
* Comedy
* Personal vlog
* Reviews
* Storytelling

![](https://academy.claude.com/assets/media/1fa6e445c825dbe4d1c4fe65b98843f5e3e5abd26bd023215aad36d6b8e7eeff.png)

## Creating Specialized Prompts

For each category, write a specific prompt that captures the right tone and approach. Here's what the educational prompt might look like:

`Develop a clear, engaging script about [TOPIC] that transforms complex information into digestible insights using relatable examples and thought-provoking questions.`

Compare that to an entertainment prompt:

`Write a high-energy, culturally-relevant script about [TOPIC] using trendy language and engaging hooks that balance entertainment value with insider insights.`

## The Two-Step Process

A routing workflow uses two separate calls to Claude:

### Step 1: Categorization

Send the user's topic to Claude with a categorization prompt asking it to classify the content type.

![](https://academy.claude.com/assets/media/bb151a9f0e4b2a2f5ebc0bbbc183d04c62e225706b0725e795e115a787e59fd2.png)

For example, "Python functions" would likely be categorized as "Educational".

### Step 2: Specialized Processing

Based on Claude's categorization, use the appropriate specialized prompt to generate the actual content.

![](https://academy.claude.com/assets/media/8568c4c90e858a79b13237e9e553b0ff9ea4386de76ee87cf3b286137eb00884.png)

## Routing Workflow Architecture

The general pattern looks like this:

![](https://academy.claude.com/assets/media/2f9761cde059187081ce9d20c188c918b56223f28bc9107fc1be44f1b3a45ee4.png)

1. User provides input
2. Router (usually Claude) categorizes the request
3. Input gets forwarded to exactly one specialized pipeline
4. Each pipeline has its own workflow, prompts, or tools

## Key Benefits

* **Better output quality** - Each category gets prompts designed for that specific use case
* **Specialized tools** - Different categories can use different APIs, databases, or processing steps
* **Scalable design** - Easy to add new categories without affecting existing ones
* **Cost efficiency** - Only run the processing that's actually needed

## When to Use Routing

Routing workflows work best when:

* Your application handles distinctly different types of requests
* Different request types need different processing approaches
* You want to optimize for quality over simplicity
* You can clearly define 3-10 meaningful categories

The upfront complexity of building multiple specialized pipelines pays off with significantly better results than trying to handle everything with a single generic approach.
