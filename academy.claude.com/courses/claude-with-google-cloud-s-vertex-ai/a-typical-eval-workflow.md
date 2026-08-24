<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/a-typical-eval-workflow -->

Lesson 11 of 66 · Claude with Google Cloud's Vertex AIA typical eval workflow

A typical prompt evaluation workflow follows five key steps that help you systematically improve your prompts through objective measurement. While there are many different ways to assemble these workflows and various open source and paid tools available, understanding the core process helps you start small and scale up as needed.

![](https://academy.claude.com/assets/media/c7dc99eee2300e25b5e601d4873fb6fc50dd72ef7781e054a2da3139d7087179.png)

## Step 1: Draft a Prompt

Start by writing an initial prompt that you want to improve. For this example, we'll use a simple prompt:

python

```
prompt = f"""
Please answer the user's question:

{question}
"""
```

![](https://academy.claude.com/assets/media/1d125564307d10c1fce46b50e731bd38b8ef51381dd330927f826d17d698f007.png)

This basic prompt will serve as our baseline for testing and improvement.

## Step 2: Create an Evaluation Dataset

Your evaluation dataset contains sample inputs that you'll feed into your prompt. Since our prompt only has one input (the user's question), we need a collection of different questions to test with.

![](https://academy.claude.com/assets/media/204aa70281126d75cbe56bb5b8925018ba22f69d862b09c5d33b05e508dc5620.png)

The dataset contains questions that we will merge with our prompt. You can assemble these datasets by hand or generate them using Claude. In real-world evaluations, you might have tens, hundreds, or even thousands of different records, but we'll start with just three questions for this example:

* What's 2+2?
* How do I make oatmeal?
* How far away is the Moon?

## Step 3: Feed Through Claude

Take each question from your dataset and merge it with your prompt template to create complete prompts. Then send each one to Claude and collect the responses.

![](https://academy.claude.com/assets/media/cbbc8e6ec17e34a40c891f578de10dbe3642a10e0de6a0a863df5db43759bed3.png)

For example, the first question becomes a complete prompt that Claude processes and returns an answer like "2 + 2 = 4". You repeat this process for all questions in your dataset, building a collection of question-answer pairs.

## Step 4: Feed Through a Grader

Now comes the crucial step of objectively measuring the quality of Claude's responses. You take each question-answer pair and feed them into a grader that scores the responses.

![](https://academy.claude.com/assets/media/d78f04e3f2294bee5d220762184603602cb18750c969c3e0c547d017f78a8068.png)

The grader assigns scores (typically 1-10) based on answer quality:

* 10 = Perfect answer with no room for improvement
* 4 = Adequate but definitely room for improvement
* Lower scores indicate poor responses

After scoring all responses, you average the scores together. In our example, scores of 10, 4, and 9 average to 7.66, giving you an objective measurement of your prompt's performance.

![](https://academy.claude.com/assets/media/0e9f812d824c4b31dfaa72e4983983fa9c519b253da93fc2501323e178157ee1.png)

## Step 5: Change Prompt and Repeat

With your baseline score established, you can now modify your prompt and run the entire process again to see if your changes improve performance.

![](https://academy.claude.com/assets/media/8ea9ee875981cf215a529a826e10a560adeede1df88e88a22c4670ffce24845e.png)

For example, you might enhance the original prompt by adding more specific instructions:

python

```
prompt = f"""
Please answer the user's question:

{question}

Answer the question with ample detail
"""
```

## Prompt Scoring

The power of this workflow lies in getting objective measurements of prompt performance. You can compare scores between different prompt versions to determine which performs better.

![](https://academy.claude.com/assets/media/b0a62f4f11b13c7465479f01619c313baac6f88f43b133557f8a3dfd90faccad.png)

In our example:

* Prompt v1 scored 7.66
* Prompt v2 scored 8.7

The higher score for v2 provides objective evidence that adding "Answer the question with ample detail" improved the prompt's performance. You can then use the better-performing version or continue iterating to achieve even higher scores.

This systematic approach removes guesswork from prompt improvement and gives you a reliable framework for optimization. While there's complexity in implementing effective graders, this workflow provides a solid foundation for building your own evaluation system.
