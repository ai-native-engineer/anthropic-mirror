<!-- https://anthropic.skilljar.com/claude-101/383392 -->

**Estimated time:** 15 minutes

### Learning objectives

By the end of this lesson, you will be able to:

* Recognize common challenges when starting out with AI and use troubleshooting techniques to overcome them
* Define AI Fluency and know where to go to learn more about working with AI in a fluent way
* Explain how you might set up evals to better understand how Claude might perform with your unique workflows

---

### Common challenges and how to fix them

As you start working with Claude, you'll likely encounter moments where the response isn't quite what you expected. This is normal—and it's an opportunity to refine your approach. Here are some of the most common challenges and how to address them.

| Challenge | What's happening | Try this |
| --- | --- | --- |
| **Claude's response is too generic** | Your prompt didn't include enough context about your specific situation | Add details about your audience, role, or constraints. Instead of "Write an email about the project delay," try "Write an email to our enterprise client explaining that the software integration will be delayed by two weeks. They've been patient so far but this is the second delay. Keep it professional but apologetic." |
| **The response is too long (or too short)** | Claude is guessing at appropriate length | Be explicit: "Give me a two-paragraph summary" or "Keep this under 100 words" or "I need a comprehensive analysis—length isn't a concern." |
| **Claude didn't follow my format** | Claude understood *what* you want but not *how* you want it presented | Show, don't just tell. Provide an example of the format, or describe the structure explicitly: "Use bullet points with bold headers for each section." |
| **I got confident-sounding information that turned out to be wrong** | Claude occasionally generates plausible but incorrect information, especially with specific facts or niche topics | For high-stakes work, verify key facts independently. Ask Claude to cite sources or indicate confidence level. Enable web search to ground responses in current information. |
| **The tone isn't right** | Claude defaults to helpful and professional, which may not match your needs | Describe the tone in plain language: "Make this more conversational" or "This should sound authoritative and formal." Provide an example of writing in the style you want. |

### The iteration mindset

One of the most important shifts when working with Claude is recognizing that your first prompt rarely produces a perfect result—and that's okay. Think of your initial prompt as the start of a conversation, not a one-shot request.

Effective Claude users:

* **Treat first drafts as starting points.** Review what Claude produces, identify what's working and what isn't, then refine.
* **Give specific feedback.** "Make it shorter" is fine, but "Cut the first two paragraphs and make the conclusion more action-oriented" is better.
* **Know when to start fresh.** If a conversation has gone off track, sometimes it's faster to open a new chat with a clearer prompt than to try to redirect.

### What is AI Fluency?

AI Fluency is the ability to collaborate effectively with AI tools—not just knowing which buttons to click, but developing the judgment to use AI well across different situations.

The **4D Framework for AI Fluency**, developed through research collaboration between Professor Rick Dakan (Ringling College of Art and Design) and Professor Joseph Feller (University College Cork), identifies four core competencies that, when combined, can help you make the most of your AI interactions:

* **Delegation:** Deciding on what work should be done by humans, what work should be done by AI, and how to distribute tasks between them. Includes understanding your goals, AI capabilities, and making strategic choices about collaboration.
* **Description:** Effectively communicating with AI systems. Includes clearly defining outputs, guiding AI processes, and specifying desired AI behaviors and interactions.
* **Discernment:** Thoughtfully and critically evaluating AI outputs, processes, behaviors and interactions. Includes assessing quality, accuracy, appropriateness, and determining areas for improvement.
* **Diligence:** Using AI responsibly and ethically. Includes making thoughtful choices about AI systems and interactions, maintaining transparency, and taking accountability for AI-assisted work.

You've already been practicing these skills throughout this course. The prompt framework from Lesson 2 (setting the stage, defining the task, specifying rules) is rooted in Description. The troubleshooting techniques above draw on Discernment and Diligence.

To learn more, check out our free [AI Fluency course](https://www.anthropic.com/ai-fluency) that explore all four competencies in depth, with practical exercises and real-world applications.

### Evaluating Claude for your workflows

As you start integrating Claude into more of your work, you might wonder: how do I know if Claude is actually good at this particular task?

This is where Discernment becomes essential. Evals (short for evaluations) are a way to develop intuition for assessing Claude's outputs on the tasks that matter to you. They're systematic ways to test how well Claude performs on specific types of tasks that matter to you.

#### Why evals matter

Your work is unique. Claude might excel at drafting marketing copy but need more guidance for technical documentation in your specific domain. Running simple evals helps you:

* Understand where Claude adds the most value in your workflow
* Identify tasks where you'll need to provide more context or examples
* Build confidence in Claude's outputs for recurring tasks

#### A simple eval approach

You don't need complex infrastructure to evaluate Claude. Here's a practical approach:

1. **Gather examples.** Collect 5-10 examples of a task you do regularly—emails you've written, reports you've created, analyses you've done. 2. **Create test prompts.** Write prompts that would generate similar outputs. Include the context you'd naturally have when doing this work. 3. **Compare outputs.** Run your prompts and compare Claude's responses to your examples. Ask yourself:
   * Does Claude capture the key information?
   * Is the tone and style appropriate?
   * What's missing or could be improved?
4. **Refine your approach.** Based on what you learn, adjust your prompts, add examples to show Claude what good looks like, or identify where human review is essential.

#### Example: Using Claude for data analysis

The video above is taken from our AI Fluency for nonprofits course, but the example is relevant for anyone working with data in AI. To evaluate how Claude might work with your data:

* Find a dataset you've manually analyzed
* Create prompts that request Claude to do the analysis on your behalf
* Compare Claude's results to your originals
* Note patterns and refine your prompt accordingly: Maybe Claude gets the right numbers but misses the overall patterns

This kind of lightweight evaluation helps you develop intuition for how to work with Claude on tasks that matter to you—and where to focus your review and refinement energy.

### Lesson reflection

Before moving on, consider:

* Which of the common challenges have you already encountered? What techniques might you try next time?
* Where in your work would a simple eval help you understand if Claude is a good fit for a recurring task?
* How might the 4D Framework help you think about your collaboration with Claude?

### What's next

In the next lesson, you'll explore the Claude desktop app and its three interaction modes: Chat, Cowork, and Code.

#### Feedback

As you progress through the course, we'd love to hear from you about how you are using concepts from the course in your work and any feedback you may have. Share your feedback [here](https://forms.gle/sY9ou5fqZBd3TjHF8).

#### Acknowledgments and license

*Copyright 2025 Anthropic. All rights reserved.*

<!-- youtube: Zzn-g8lvLMA -->

## 자막 (영상 전사)

[music] In our last lesson, we dealt with data privacy and security. What you absolutely need to protect and how to do it. So, now let's talk about the question that's probably stopped you from using AI for data analysis in the first place. How can I trust the results? Today's lesson is about the delegation diligence loop. Specifically, building confidence in AI's analytical capabilities for your specific work by systematically testing it against data you already understand. By doing this, you can better understand how AI will support your specific circumstances. The process starts with delegation. Here's how this works. First, identify a specific analytical task you do regularly that you want to delegate to AI. Find past data where you already completed the analysis and then work with AI to reproduce what you did, evaluating what works and what doesn't. Refine your approach and test again. If AI can match your known results, you know how to use it and trust it for similar future tasks. And if not, you've learned that this task is something you shouldn't delegate. So, let me show you what this looks like in practice, and then we'll talk through what to do if you're not that data savvy to begin with. Meet Rio, the program director at Valley Veterans Services. Every quarter, he analyzes program attendance alongside employment outcomes, calculating participation rates, tracking monthly changes, and determining whether attendance correlates with job placement success. This analysis consistently takes him hours. Considering delegation, Rio knows he wants to continue using the results of this analysis to improve his program. He wants to interpret the results himself, but he could do without the data cleaning and formula mayhem he usually finds himself in to do the actual analysis. So, in order to test whether AI is appropriate in this scenario, he's going to evaluate it using last quarter's data. He knows exactly what this data showed after he analyzed it without AI, and he has the raw messy data from before he started. This is his test case. Rio uploads the data and starts to work with AI using description and discernment to perform his analysis. Only each time the AI responds, Rio is going to check the results against what he knows to be true and jot down potential gaps in AI's reasoning. Sometimes additional description helps AI get the outcome he's looking for. In these cases, Rio knows he has to include that kind of information for future data analysis tasks. Other times, Rio might find legitimate capability gaps. This is the delegation diligence loop in action. Rio's diligence to evaluate the model's capabilities can change what he chooses to delegate to AI in the future. His first attempt might look like, I'm sharing attendance data and employment outcome data from our job training program last quarter. Please analyze the participation patterns across the three months and graph the correlations between attendance levels and employment success. I'm particularly interested in understanding whether consistent attendance predicts better job placement outcomes. AI responds with a summary, but rather than assuming this is fact, Rio checks this against his records and notes what's good and what's not. AI correctly identified the correlation between program attendance and job placement, but it missed a critical insight around the combined housing assistance and job placement program. So Rio refineses his description asking AI to try again but pay special attention to the program type. This time AI catches its mistake. So Rio notes that for future quarters he'll need to specifically request the AI to consider the program type when performing its analysis. Then he tests something harder. Can you also look at this based on when participants enrolled? AI responds as Rio observes that despite not knowing the enrollment data, AI could help extract it. He makes a note to cross reference these results later on. By going through this process, Rio has systematically validated what AI can and can't do for his quarterly reporting. He's learned that with the right description, AI can accurately reproduce the analysis he used to do manually. But he's also identified clear limitations and areas for follow-up. AI needs enrollment dates in the data to do cohort analysis. Otherwise, it'll try to infer them, which he doesn't want. And most importantly, Rio now has a tested approach that he can confidently use with this quarter's data and clear notes about what information he needs to include and what context he still needs to add himself. When Rio uses this validated approach with new data, his diligence continues. He'll check whether numbers make sense based on what he knows about his programs. He'll take accountability for the final report and he'll be transparent about AI's role if asked. But now he's working from validated confidence, not guesswork. So here's the framework. Identify a specific analytical task that you want to delegate. Be precise about what you need. Then find past data where you already completed that analysis. You need the right answers to evaluate whether AI can arrive at them. Work with AI to reproduce your past analysis and systematically evaluate the results. What did AI produce? How did it approach the task? How did it communicate findings? Identify gaps, refine your delegation, and then test again. If you can validate that AI produces correct results, you've built an approach that you can confidently use on new data. But if you can't get there after several refinements, you've learned that this isn't a task you should delegate. So, this is all great, but what if you're not very comfortable with the data to begin with and wouldn't be able to spot those process gaps yourself? AI can also be a useful tool to brainstorm and implement solutions you might not have thought of on your own. Because AI models are uniquely good at coding, they can help with things like writing Excel formulas, reformatting messy data, and more. In these cases, you can simply bring your question or idea to AI and specifically ask for help understanding what a solution could look like, just like how you would work with a data analyst on your team. As you work with AI, just keep asking for clarifications and explanations so that you can follow the process and understand the final output. Just remember, validation builds confidence, but it doesn't eliminate responsibility. you're still accountable for checking that these results make sense and being transparent about AI's role in your analysis process. This testing works for any analytical task you're considering. Donor analysis, budget forecasting, survey synthesis, outcome tracking. Test first, validate what works, then apply with more confidence, or learn what you shouldn't delegate at all. In our next lesson, we'll look at workflow augmentation and how to apply these same principles when AI handles routine tasks on your behalf.
