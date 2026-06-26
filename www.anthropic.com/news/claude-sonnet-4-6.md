<!-- source: https://www.anthropic.com/news/claude-sonnet-4-6 -->

# Introducing Claude Sonnet 4.6
2026년 2월 17일
![Introducing Claude Sonnet 4.6](https://www-cdn.anthropic.com/images/4zrzovbb/website/60a35c504cedb3e3f581b211e4b8aef372ffe031-1000x1000.svg)
_Claude Sonnet 4.6 is our most capable Sonnet model yet_. It’s a full upgrade of the model’s skills across coding, computer use, long-context reasoning, agent planning, knowledge work, and design. Sonnet 4.6 also features a 1M token context window in beta.
For those on our [Free and Pro plans](https://claude.com/pricing), Claude Sonnet 4.6 is now the default model in [claude.ai](https://claude.ai/redirect/website.v1.0e3a6f32-5f88-4168-82b2-642763282fa6) and [Claude Cowork](https://claude.com/product/cowork). [Pricing](https://claude.com/pricing#api) remains the same as Sonnet 4.5, starting at $3/$15 per million tokens.
Sonnet 4.6 brings much-improved coding skills to more of our users. Improvements in consistency, instruction following, and more have made developers with early access prefer Sonnet 4.6 to its predecessor by a wide margin. They often even prefer it to our smartest model from November 2025, Claude Opus 4.5.
Performance that would have previously required reaching for an Opus-class model—including on real-world, economically valuable [office tasks](https://artificialanalysis.ai/evaluations/gdpval-aa)—is now available with Sonnet 4.6. The model also shows a major improvement in computer use skills compared to prior Sonnet models.
As with every new Claude model, we’ve run [extensive safety evaluations](https://anthropic.com/claude-sonnet-4-6-system-card) of Sonnet 4.6, which overall showed it to be as safe as, or safer than, our other recent Claude models. Our safety researchers concluded that Sonnet 4.6 has “a broadly warm, honest, prosocial, and at times funny character, very strong safety behaviors, and no signs of major concerns around high-stakes forms of misalignment.”
## Computer use
Almost every organization has software it can’t easily automate: specialized systems and tools built before modern interfaces like APIs existed. To have AI use such software, users would previously have had to build bespoke connectors. But a model that can use a computer the way a person does changes that equation.
In October 2024, we were the [first to introduce](https://www.anthropic.com/news/3-5-models-and-computer-use) a general-purpose computer-using model. At the time, we wrote that it was “still experimental—at times cumbersome and error-prone,” but we expected rapid improvement. [OSWorld](https://os-world.github.io/), the standard benchmark for AI computer use, shows how far our models have come. It presents hundreds of tasks across real software (Chrome, LibreOffice, VS Code, and more) running on a simulated computer. There are no special APIs or purpose-built connectors; the model sees the computer and interacts with it in much the same way a person would: clicking a (virtual) mouse and typing on a (virtual) keyboard.
Across sixteen months, our Sonnet models have made steady gains on OSWorld. The improvements can also be seen beyond benchmarks: early Sonnet 4.6 users are seeing human-level capability in tasks like navigating a complex spreadsheet or filling out a multi-step web form, before pulling it all together across multiple browser tabs.
The model certainly still lags behind the most skilled humans at using computers. But the rate of progress is remarkable nonetheless. It means that computer use is much more useful for a range of work tasks—and that substantially more capable models are within reach.
![Chart comparing several Sonnet model scores on the OSWorld benchmark](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F1206645ef5a618dabce8587b472b21c67a30a0db-3840x1948.png&w=3840&q=75)Scores prior to Claude Sonnet 4.5 were measured on the original OSWorld; scores from Sonnet 4.5 onward use OSWorld-Verified. OSWorld-Verified (released July 2025) is an in-place upgrade of the original OSWorld benchmark, with updates to task quality, evaluation grading, and infrastructure.
At the same time, computer use poses risks: malicious actors can attempt to hijack the model by hiding instructions on websites in what’s known as a prompt injection attack. We’ve been working to improve our models’ resistance to prompt injections—our [safety evaluations](https://anthropic.com/claude-sonnet-4-6-system-card) show that Sonnet 4.6 is a major improvement compared to its predecessor, Sonnet 4.5, and performs similarly to Opus 4.6. You can find out more about how to mitigate prompt injections and other safety concerns in [our API docs](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks).
## Evaluating Claude Sonnet 4.6
Beyond computer use, Claude Sonnet 4.6 has improved on benchmarks across the board. It approaches Opus-level intelligence at a price point that makes it more practical for far more tasks. You can find a full discussion of Sonnet 4.6’s capabilities and its safety-related behaviors in [our system card](https://anthropic.com/claude-sonnet-4-6-system-card); a summary and comparison to other recent models is below.
![A table of popular benchmarks and Sonnet 4.6's relative performance compared to other frontier models](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F10b2602771d21378cd6d76628a081c8a76dcf216-2600x2960.png&w=3840&q=75)
In Claude Code, our early testing found that users preferred Sonnet 4.6 over Sonnet 4.5 roughly 70% of the time. Users reported that it more effectively read the context before modifying code and consolidated shared logic rather than duplicating it. This made it less frustrating to use over long sessions than earlier models.
Users even preferred Sonnet 4.6 to Opus 4.5, our frontier model from November, 59% of the time. They rated Sonnet 4.6 as significantly less prone to overengineering and “laziness,” and meaningfully better at instruction following. They reported fewer false claims of success, fewer hallucinations, and more consistent follow-through on multi-step tasks.
Sonnet 4.6’s 1M token context window is enough to hold entire codebases, lengthy contracts, or dozens of research papers in a single request. More importantly, Sonnet 4.6 _reasons effectively_ across all that context. This can make it much better at long-horizon planning. We saw this particularly clearly in the [Vending-Bench Arena](https://andonlabs.com/evals/vending-bench-arena) evaluation, which tests how well a model can run a (simulated) business over time—and which includes an element of competition, with different AI models facing off against each other to make the biggest profits.
Sonnet 4.6 developed an interesting new strategy: it invested heavily in capacity for the first ten simulated months, spending significantly more than its competitors, and then pivoted sharply to focus on profitability in the final stretch. The timing of this pivot helped it finish well ahead of the competition.
![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F8c2855afe51fc0980596b5369b01b0b87eea7eaf-3840x2160.png&w=3840&q=75)Sonnet 4.6 outperforms Sonnet 4.5 on Vending-Bench Arena by investing in capacity early, then pivoting to profitability in the final stretch.
Early customers also reported broad improvements, with frontend code and financial analysis standing out. Customers independently described visual outputs from Sonnet 4.6 as notably more polished, with better layouts, animations, and design sensibility than those from previous models. Customers also needed fewer rounds of iteration to reach production-quality results.
![Databricks logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/a498e756da3805fe3416177ea825d6586f6432a2-150x48.svg)
> Claude Sonnet 4.6 matches Opus 4.6 performance on OfficeQA, which measures how well a model can read enterprise documents (charts, PDFs, tables), pull the right facts, and reason from those facts. It’s a meaningful upgrade for document comprehension workloads.
> Hanlin Tang  
> CTO of Neural Networks, Databricks
![Replit logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/ff1601aa704506064c9ddee37079f17f9b0799cd-150x48.svg)
> The performance-to-cost ratio of Claude Sonnet 4.6 is extraordinary—it’s hard to overstate how fast Claude models have been evolving in recent months. Sonnet 4.6 outperforms on our orchestration evals, handles our most complex agentic workloads, and keeps improving the higher you push the effort settings.
> Michele Catasta  
> President, Replit
![Cursor logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/d74b2a5f8dc7d22b0febb8c69feabff0999da79d-151x36.svg)
> Claude Sonnet 4.6 is a notable improvement over Sonnet 4.5 across the board, including long-horizon tasks and more difficult problems.
> Michael Truell  
> Co-founder and CEO, Cursor
![GitHub logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/7715b118c5eb0ff2a85f1f7914bce8c634ecacbd-150x48.svg)
> Out of the gate, Claude Sonnet 4.6 is already excelling at complex code fixes, especially when searching across large codebases is essential. For teams running agentic coding at scale, we’re seeing strong resolution rates and the kind of consistency developers need.
> Joe Binder  
> VP of Product, GitHub
![Cognition logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/da50e4c43d4b95fe1a2105c344050c6ba2397f3f-150x48.svg)
> Claude Sonnet 4.6 has meaningfully closed the gap with Opus on bug detection, letting us run more reviewers in parallel, catch a wider variety of bugs, and do it all without increasing cost.
> Scott Wu  
> CEO, Cognition
![Windsurf logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/7415f908eca858ec4c3453c5d8151e46a0fb1e6d-150x48.svg)
> For the first time, Sonnet brings frontier-level reasoning in a smaller and more cost-effective form factor. It provides a viable alternative if you are a heavy Opus user.
> Jeff Wang  
> CEO, Windsurf
![Hebbia logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/aad0da69057f1510832dbb52e56a7dc96f352c17-136x24.svg)
> Claude Sonnet 4.6 meaningfully improves the answer retrieval behind our core product—we saw a significant jump in answer match rate compared to Sonnet 4.5 in our Financial Services Benchmark, with better recall on the specific workflows our customers depend on.
> Aabhas Sharma  
> CTO, Hebbia
![Box logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/49b99af78924f43f878d39a25d574da293c68596-60x32.svg)
> Box evaluated how Claude Sonnet 4.6 performs when tested on deep reasoning and complex agentic tasks across real enterprise documents. It demonstrated significant improvements, outperforming Claude Sonnet 4.5 in heavy reasoning Q&A by 15 percentage points.
> Ben Kus  
> CTO, Box
![Pace logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/ec6a42c89c7dc05949f15091fda3c953d5ac7632-118x36.svg)
> Claude Sonnet 4.6 hit 94% on our insurance benchmark, making it the highest-performing model we’ve tested for computer use. This kind of accuracy is mission-critical to workflows like submission intake and first notice of loss.
> Jamie Cuffe  
> CEO, Pace
![Bolt logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/ade72922c1b58726e1b7c17f0e500054e3d74aa0-92x37.svg)
> Claude Sonnet 4.6 delivers frontier-level results on complex app builds and bug-fixing. It’s becoming our go-to for the kind of deep codebase work that used to require more expensive models.
> Eric Simons  
> CEO, Bolt
![Rakuten logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/652c487024ae6e67508571e7e5f64b7d482bdadd-150x48.svg)
> Claude Sonnet 4.6 produced the best iOS code we’ve tested for Rakuten AI. Better spec compliance, better architecture, and it reached for modern tooling we didn’t ask for, all in one shot. The results genuinely surprised us.  
> 
> Yusuke Kaji  
> General Manager, AI, Rakuten
![Zapier logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/8dc17fb025de0cb19ec76a2dc7ae522a8f8f3ea6-2500x676.svg)
> Sonnet 4.6 is a significant leap forward on reasoning through difficult tasks. We find it especially strong on branched and multi-step tasks like contract routing, conditional template selection, and CRM coordination—exactly where our customers need strong model sense and reliability.
> Wade Foster  
> Co-founder and CEO, Zapier
![Convey logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/b59ed46312c5dc6d29e8fc232abcd1a16f3331dc-145x30.svg)
> We’ve been impressed by how accurately Claude Sonnet 4.6 handles complex computer use. It’s a clear improvement over anything else we’ve tested in our evals.
> Will Harvey  
> Co-founder, Convey
![Triple Whale logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/7245ddfbb56c3f08bc8f1dcfd864255ec442c729-150x48.svg)
> Claude Sonnet 4.6 has perfect design taste when building frontend pages and data reports, and it requires far less hand-holding to get there than anything we’ve tested before.
> AJ Orbach  
> Co-founder, Triple Whale
![Harvey logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/501ebc6538c68e98ae6cfab79a5747009700f4a1-100x30.svg)
> Claude Sonnet 4.6 was exceptionally responsive to direction — delivering precise figures and structured comparisons when asked, while also generating genuinely useful ideas on trial strategy and exhibit preparation.
> Niko Grupen  
> Head of Applied Research, Harvey
01 / 15
## Product updates
On the Claude Platform, Sonnet 4.6 supports both [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) and extended thinking, as well as [context compaction](https://platform.claude.com/docs/en/build-with-claude/compaction) in beta, which automatically summarizes older context as conversations approach limits, increasing effective context length.
On our API, Claude’s [web search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) and [fetch](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool) tools now automatically write and execute code to[ filter and process search results](https://www.claude.com/blog/improved-web-search-with-dynamic-filtering), keeping only relevant content in context—improving both response quality and token efficiency. Additionally, [code execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool), [memory](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool), [programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling), [tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool), and [tool use examples](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use#providing-tool-use-examples) are now generally available.
Sonnet 4.6 offers strong performance at any thinking effort, even with extended thinking off. As part of your migration from Sonnet 4.5, we recommend exploring across the spectrum to find the ideal balance of speed and reliable performance, depending on what you’re building.
We find that Opus 4.6 remains the strongest option for tasks that demand the deepest reasoning, such as codebase refactoring, coordinating multiple agents in a workflow, and problems where getting it _just_ _right_ is paramount.
For [Claude in Excel](https://support.claude.com/en/articles/12650343-using-claude-in-excel) users, our add-in now supports MCP connectors, letting Claude work with the other tools you use day-to-day, like S&P Global, LSEG, Daloopa, PitchBook, Moody’s, and FactSet. You can ask Claude to pull in context from outside your spreadsheet without ever leaving Excel. If you’ve already set up MCP connectors in Claude.ai, those same connections will work in Excel automatically. This is available on Pro, Max, Team, and Enterprise plans.
## How to use Claude Sonnet 4.6
Claude Sonnet 4.6 is available now on all [Claude plans](https://claude.com/pricing), [Claude Cowork](https://claude.com/product/cowork), [Claude Code](https://claude.com/product/claude-code), our API, and all major cloud platforms. We’ve also upgraded our free tier to Sonnet 4.6 by default—it now includes file creation, connectors, skills, and compaction.
If you’re a developer, you can get started quickly by using `claude-sonnet-4-6` via the [Claude API](https://platform.claude.com/docs/en/about-claude/models/overview).  

#### Footnotes
  * For GPT-5.2 and Gemini 3 Pro, we compared against the best reported model version available via API in the charts and table.
  * **OSWorld** : OSWorld tests a specific set of computer tasks in a controlled environment. It’s one of the best measures we have, but not a complete picture of real-world computer use. Real-world computer use is often messier and more ambiguous, and it carries higher stakes for errors. No benchmark fully captures that yet.
  * **Terminal-Bench 2.0:** We report both scores reproduced on our infrastructure and published scores from other labs. All runs used the Terminus-2 harness, except for OpenAI’s Codex CLI. All experiments used 1× guaranteed/3× ceiling resource allocation and 5–15 samples per task across staggered batches. The Sonnet 4.6 score reported is with thinking turned off.
  * **SWE-bench Verified** : Our score was averaged over 10 trials. With a prompt modification, we saw a score of 80.2%.
  * **Humanity’s Last Exam:** Claude models run “with tools” were run with web search, web fetch, code execution, programmatic tool calling, context compaction triggered at 50k tokens up to 3M total tokens, max reasoning effort, and adaptive thinking enabled. A domain blocklist was used to decontaminate eval results.
  * **BrowseComp** : Claude models were run with web search, web fetch, programmatic tool calling, context compaction triggered at 50k tokens up to 10M total tokens, max reasoning effort, and no thinking enabled.
  * **ARC-AGI-2:** Claude Sonnet 4.6 was run with max and high effort and a 120k thinking budget score. The score shown reflects max effort; with high effort, we achieve a score of 60.4%.
  * **MMMU-Pro** : We made two small updates to our MMMU-Pro implementation that have affected the score: 1) our previous implementation contained the prefix “Let’s think step-by-step,” which we have removed, and 2) we previously graded this multiple-choice eval by looking at on-policy token probabilities of the multiple-choice options; we now grade it using a separate model (Claude Sonnet 4).

[](https://twitter.com/intent/tweet?text=https://www.anthropic.com/news/claude-sonnet-4-6)[](https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/news/claude-sonnet-4-6)
Product
# Introducing Claude Sonnet 4.6
2026년 2월 17일
![Introducing Claude Sonnet 4.6](https://www-cdn.anthropic.com/images/4zrzovbb/website/60a35c504cedb3e3f581b211e4b8aef372ffe031-1000x1000.svg)
_Claude Sonnet 4.6 is our most capable Sonnet model yet_. It’s a full upgrade of the model’s skills across coding, computer use, long-context reasoning, agent planning, knowledge work, and design. Sonnet 4.6 also features a 1M token context window in beta.
For those on our [Free and Pro plans](https://claude.com/pricing), Claude Sonnet 4.6 is now the default model in [claude.ai](https://claude.ai/redirect/website.v1.0e3a6f32-5f88-4168-82b2-642763282fa6) and [Claude Cowork](https://claude.com/product/cowork). [Pricing](https://claude.com/pricing#api) remains the same as Sonnet 4.5, starting at $3/$15 per million tokens.
Sonnet 4.6 brings much-improved coding skills to more of our users. Improvements in consistency, instruction following, and more have made developers with early access prefer Sonnet 4.6 to its predecessor by a wide margin. They often even prefer it to our smartest model from November 2025, Claude Opus 4.5.
Performance that would have previously required reaching for an Opus-class model—including on real-world, economically valuable [office tasks](https://artificialanalysis.ai/evaluations/gdpval-aa)—is now available with Sonnet 4.6. The model also shows a major improvement in computer use skills compared to prior Sonnet models.
As with every new Claude model, we’ve run [extensive safety evaluations](https://anthropic.com/claude-sonnet-4-6-system-card) of Sonnet 4.6, which overall showed it to be as safe as, or safer than, our other recent Claude models. Our safety researchers concluded that Sonnet 4.6 has “a broadly warm, honest, prosocial, and at times funny character, very strong safety behaviors, and no signs of major concerns around high-stakes forms of misalignment.”
## Computer use
Almost every organization has software it can’t easily automate: specialized systems and tools built before modern interfaces like APIs existed. To have AI use such software, users would previously have had to build bespoke connectors. But a model that can use a computer the way a person does changes that equation.
In October 2024, we were the [first to introduce](https://www.anthropic.com/news/3-5-models-and-computer-use) a general-purpose computer-using model. At the time, we wrote that it was “still experimental—at times cumbersome and error-prone,” but we expected rapid improvement. [OSWorld](https://os-world.github.io/), the standard benchmark for AI computer use, shows how far our models have come. It presents hundreds of tasks across real software (Chrome, LibreOffice, VS Code, and more) running on a simulated computer. There are no special APIs or purpose-built connectors; the model sees the computer and interacts with it in much the same way a person would: clicking a (virtual) mouse and typing on a (virtual) keyboard.
Across sixteen months, our Sonnet models have made steady gains on OSWorld. The improvements can also be seen beyond benchmarks: early Sonnet 4.6 users are seeing human-level capability in tasks like navigating a complex spreadsheet or filling out a multi-step web form, before pulling it all together across multiple browser tabs.
The model certainly still lags behind the most skilled humans at using computers. But the rate of progress is remarkable nonetheless. It means that computer use is much more useful for a range of work tasks—and that substantially more capable models are within reach.
![Chart comparing several Sonnet model scores on the OSWorld benchmark](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F1206645ef5a618dabce8587b472b21c67a30a0db-3840x1948.png&w=3840&q=75)Scores prior to Claude Sonnet 4.5 were measured on the original OSWorld; scores from Sonnet 4.5 onward use OSWorld-Verified. OSWorld-Verified (released July 2025) is an in-place upgrade of the original OSWorld benchmark, with updates to task quality, evaluation grading, and infrastructure.
At the same time, computer use poses risks: malicious actors can attempt to hijack the model by hiding instructions on websites in what’s known as a prompt injection attack. We’ve been working to improve our models’ resistance to prompt injections—our [safety evaluations](https://anthropic.com/claude-sonnet-4-6-system-card) show that Sonnet 4.6 is a major improvement compared to its predecessor, Sonnet 4.5, and performs similarly to Opus 4.6. You can find out more about how to mitigate prompt injections and other safety concerns in [our API docs](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks).
## Evaluating Claude Sonnet 4.6
Beyond computer use, Claude Sonnet 4.6 has improved on benchmarks across the board. It approaches Opus-level intelligence at a price point that makes it more practical for far more tasks. You can find a full discussion of Sonnet 4.6’s capabilities and its safety-related behaviors in [our system card](https://anthropic.com/claude-sonnet-4-6-system-card); a summary and comparison to other recent models is below.
![A table of popular benchmarks and Sonnet 4.6's relative performance compared to other frontier models](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F10b2602771d21378cd6d76628a081c8a76dcf216-2600x2960.png&w=3840&q=75)
In Claude Code, our early testing found that users preferred Sonnet 4.6 over Sonnet 4.5 roughly 70% of the time. Users reported that it more effectively read the context before modifying code and consolidated shared logic rather than duplicating it. This made it less frustrating to use over long sessions than earlier models.
Users even preferred Sonnet 4.6 to Opus 4.5, our frontier model from November, 59% of the time. They rated Sonnet 4.6 as significantly less prone to overengineering and “laziness,” and meaningfully better at instruction following. They reported fewer false claims of success, fewer hallucinations, and more consistent follow-through on multi-step tasks.
Sonnet 4.6’s 1M token context window is enough to hold entire codebases, lengthy contracts, or dozens of research papers in a single request. More importantly, Sonnet 4.6 _reasons effectively_ across all that context. This can make it much better at long-horizon planning. We saw this particularly clearly in the [Vending-Bench Arena](https://andonlabs.com/evals/vending-bench-arena) evaluation, which tests how well a model can run a (simulated) business over time—and which includes an element of competition, with different AI models facing off against each other to make the biggest profits.
Sonnet 4.6 developed an interesting new strategy: it invested heavily in capacity for the first ten simulated months, spending significantly more than its competitors, and then pivoted sharply to focus on profitability in the final stretch. The timing of this pivot helped it finish well ahead of the competition.
![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F8c2855afe51fc0980596b5369b01b0b87eea7eaf-3840x2160.png&w=3840&q=75)Sonnet 4.6 outperforms Sonnet 4.5 on Vending-Bench Arena by investing in capacity early, then pivoting to profitability in the final stretch.
Early customers also reported broad improvements, with frontend code and financial analysis standing out. Customers independently described visual outputs from Sonnet 4.6 as notably more polished, with better layouts, animations, and design sensibility than those from previous models. Customers also needed fewer rounds of iteration to reach production-quality results.
![Databricks logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/a498e756da3805fe3416177ea825d6586f6432a2-150x48.svg)
> Claude Sonnet 4.6 matches Opus 4.6 performance on OfficeQA, which measures how well a model can read enterprise documents (charts, PDFs, tables), pull the right facts, and reason from those facts. It’s a meaningful upgrade for document comprehension workloads.
> Hanlin Tang  
> CTO of Neural Networks, Databricks
![Replit logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/ff1601aa704506064c9ddee37079f17f9b0799cd-150x48.svg)
> The performance-to-cost ratio of Claude Sonnet 4.6 is extraordinary—it’s hard to overstate how fast Claude models have been evolving in recent months. Sonnet 4.6 outperforms on our orchestration evals, handles our most complex agentic workloads, and keeps improving the higher you push the effort settings.
> Michele Catasta  
> President, Replit
![Cursor logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/d74b2a5f8dc7d22b0febb8c69feabff0999da79d-151x36.svg)
> Claude Sonnet 4.6 is a notable improvement over Sonnet 4.5 across the board, including long-horizon tasks and more difficult problems.
> Michael Truell  
> Co-founder and CEO, Cursor
![GitHub logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/7715b118c5eb0ff2a85f1f7914bce8c634ecacbd-150x48.svg)
> Out of the gate, Claude Sonnet 4.6 is already excelling at complex code fixes, especially when searching across large codebases is essential. For teams running agentic coding at scale, we’re seeing strong resolution rates and the kind of consistency developers need.
> Joe Binder  
> VP of Product, GitHub
![Cognition logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/da50e4c43d4b95fe1a2105c344050c6ba2397f3f-150x48.svg)
> Claude Sonnet 4.6 has meaningfully closed the gap with Opus on bug detection, letting us run more reviewers in parallel, catch a wider variety of bugs, and do it all without increasing cost.
> Scott Wu  
> CEO, Cognition
![Windsurf logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/7415f908eca858ec4c3453c5d8151e46a0fb1e6d-150x48.svg)
> For the first time, Sonnet brings frontier-level reasoning in a smaller and more cost-effective form factor. It provides a viable alternative if you are a heavy Opus user.
> Jeff Wang  
> CEO, Windsurf
![Hebbia logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/aad0da69057f1510832dbb52e56a7dc96f352c17-136x24.svg)
> Claude Sonnet 4.6 meaningfully improves the answer retrieval behind our core product—we saw a significant jump in answer match rate compared to Sonnet 4.5 in our Financial Services Benchmark, with better recall on the specific workflows our customers depend on.
> Aabhas Sharma  
> CTO, Hebbia
![Box logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/49b99af78924f43f878d39a25d574da293c68596-60x32.svg)
> Box evaluated how Claude Sonnet 4.6 performs when tested on deep reasoning and complex agentic tasks across real enterprise documents. It demonstrated significant improvements, outperforming Claude Sonnet 4.5 in heavy reasoning Q&A by 15 percentage points.
> Ben Kus  
> CTO, Box
![Pace logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/ec6a42c89c7dc05949f15091fda3c953d5ac7632-118x36.svg)
> Claude Sonnet 4.6 hit 94% on our insurance benchmark, making it the highest-performing model we’ve tested for computer use. This kind of accuracy is mission-critical to workflows like submission intake and first notice of loss.
> Jamie Cuffe  
> CEO, Pace
![Bolt logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/ade72922c1b58726e1b7c17f0e500054e3d74aa0-92x37.svg)
> Claude Sonnet 4.6 delivers frontier-level results on complex app builds and bug-fixing. It’s becoming our go-to for the kind of deep codebase work that used to require more expensive models.
> Eric Simons  
> CEO, Bolt
![Rakuten logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/652c487024ae6e67508571e7e5f64b7d482bdadd-150x48.svg)
> Claude Sonnet 4.6 produced the best iOS code we’ve tested for Rakuten AI. Better spec compliance, better architecture, and it reached for modern tooling we didn’t ask for, all in one shot. The results genuinely surprised us.  
> 
> Yusuke Kaji  
> General Manager, AI, Rakuten
![Zapier logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/8dc17fb025de0cb19ec76a2dc7ae522a8f8f3ea6-2500x676.svg)
> Sonnet 4.6 is a significant leap forward on reasoning through difficult tasks. We find it especially strong on branched and multi-step tasks like contract routing, conditional template selection, and CRM coordination—exactly where our customers need strong model sense and reliability.
> Wade Foster  
> Co-founder and CEO, Zapier
![Convey logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/b59ed46312c5dc6d29e8fc232abcd1a16f3331dc-145x30.svg)
> We’ve been impressed by how accurately Claude Sonnet 4.6 handles complex computer use. It’s a clear improvement over anything else we’ve tested in our evals.
> Will Harvey  
> Co-founder, Convey
![Triple Whale logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/7245ddfbb56c3f08bc8f1dcfd864255ec442c729-150x48.svg)
> Claude Sonnet 4.6 has perfect design taste when building frontend pages and data reports, and it requires far less hand-holding to get there than anything we’ve tested before.
> AJ Orbach  
> Co-founder, Triple Whale
![Harvey logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/501ebc6538c68e98ae6cfab79a5747009700f4a1-100x30.svg)
> Claude Sonnet 4.6 was exceptionally responsive to direction — delivering precise figures and structured comparisons when asked, while also generating genuinely useful ideas on trial strategy and exhibit preparation.
> Niko Grupen  
> Head of Applied Research, Harvey
01 / 15
## Product updates
On the Claude Platform, Sonnet 4.6 supports both [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) and extended thinking, as well as [context compaction](https://platform.claude.com/docs/en/build-with-claude/compaction) in beta, which automatically summarizes older context as conversations approach limits, increasing effective context length.
On our API, Claude’s [web search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) and [fetch](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool) tools now automatically write and execute code to[ filter and process search results](https://www.claude.com/blog/improved-web-search-with-dynamic-filtering), keeping only relevant content in context—improving both response quality and token efficiency. Additionally, [code execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool), [memory](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool), [programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling), [tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool), and [tool use examples](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use#providing-tool-use-examples) are now generally available.
Sonnet 4.6 offers strong performance at any thinking effort, even with extended thinking off. As part of your migration from Sonnet 4.5, we recommend exploring across the spectrum to find the ideal balance of speed and reliable performance, depending on what you’re building.
We find that Opus 4.6 remains the strongest option for tasks that demand the deepest reasoning, such as codebase refactoring, coordinating multiple agents in a workflow, and problems where getting it _just_ _right_ is paramount.
For [Claude in Excel](https://support.claude.com/en/articles/12650343-using-claude-in-excel) users, our add-in now supports MCP connectors, letting Claude work with the other tools you use day-to-day, like S&P Global, LSEG, Daloopa, PitchBook, Moody’s, and FactSet. You can ask Claude to pull in context from outside your spreadsheet without ever leaving Excel. If you’ve already set up MCP connectors in Claude.ai, those same connections will work in Excel automatically. This is available on Pro, Max, Team, and Enterprise plans.
## How to use Claude Sonnet 4.6
Claude Sonnet 4.6 is available now on all [Claude plans](https://claude.com/pricing), [Claude Cowork](https://claude.com/product/cowork), [Claude Code](https://claude.com/product/claude-code), our API, and all major cloud platforms. We’ve also upgraded our free tier to Sonnet 4.6 by default—it now includes file creation, connectors, skills, and compaction.
If you’re a developer, you can get started quickly by using `claude-sonnet-4-6` via the [Claude API](https://platform.claude.com/docs/en/about-claude/models/overview).  

#### Footnotes
  * For GPT-5.2 and Gemini 3 Pro, we compared against the best reported model version available via API in the charts and table.
  * **OSWorld** : OSWorld tests a specific set of computer tasks in a controlled environment. It’s one of the best measures we have, but not a complete picture of real-world computer use. Real-world computer use is often messier and more ambiguous, and it carries higher stakes for errors. No benchmark fully captures that yet.
  * **Terminal-Bench 2.0:** We report both scores reproduced on our infrastructure and published scores from other labs. All runs used the Terminus-2 harness, except for OpenAI’s Codex CLI. All experiments used 1× guaranteed/3× ceiling resource allocation and 5–15 samples per task across staggered batches. The Sonnet 4.6 score reported is with thinking turned off.
  * **SWE-bench Verified** : Our score was averaged over 10 trials. With a prompt modification, we saw a score of 80.2%.
  * **Humanity’s Last Exam:** Claude models run “with tools” were run with web search, web fetch, code execution, programmatic tool calling, context compaction triggered at 50k tokens up to 3M total tokens, max reasoning effort, and adaptive thinking enabled. A domain blocklist was used to decontaminate eval results.
  * **BrowseComp** : Claude models were run with web search, web fetch, programmatic tool calling, context compaction triggered at 50k tokens up to 10M total tokens, max reasoning effort, and no thinking enabled.
  * **ARC-AGI-2:** Claude Sonnet 4.6 was run with max and high effort and a 120k thinking budget score. The score shown reflects max effort; with high effort, we achieve a score of 60.4%.
  * **MMMU-Pro** : We made two small updates to our MMMU-Pro implementation that have affected the score: 1) our previous implementation contained the prefix “Let’s think step-by-step,” which we have removed, and 2) we previously graded this multiple-choice eval by looking at on-policy token probabilities of the multiple-choice options; we now grade it using a separate model (Claude Sonnet 4).

[](https://twitter.com/intent/tweet?text=https://www.anthropic.com/news/claude-sonnet-4-6)[](https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/news/claude-sonnet-4-6)
_Claude Sonnet 4.6 is our most capable Sonnet model yet_. It’s a full upgrade of the model’s skills across coding, computer use, long-context reasoning, agent planning, knowledge work, and design. Sonnet 4.6 also features a 1M token context window in beta.
For those on our [Free and Pro plans](https://claude.com/pricing), Claude Sonnet 4.6 is now the default model in [claude.ai](https://claude.ai/redirect/website.v1.0e3a6f32-5f88-4168-82b2-642763282fa6) and [Claude Cowork](https://claude.com/product/cowork). [Pricing](https://claude.com/pricing#api) remains the same as Sonnet 4.5, starting at $3/$15 per million tokens.
Sonnet 4.6 brings much-improved coding skills to more of our users. Improvements in consistency, instruction following, and more have made developers with early access prefer Sonnet 4.6 to its predecessor by a wide margin. They often even prefer it to our smartest model from November 2025, Claude Opus 4.5.
Performance that would have previously required reaching for an Opus-class model—including on real-world, economically valuable [office tasks](https://artificialanalysis.ai/evaluations/gdpval-aa)—is now available with Sonnet 4.6. The model also shows a major improvement in computer use skills compared to prior Sonnet models.
As with every new Claude model, we’ve run [extensive safety evaluations](https://anthropic.com/claude-sonnet-4-6-system-card) of Sonnet 4.6, which overall showed it to be as safe as, or safer than, our other recent Claude models. Our safety researchers concluded that Sonnet 4.6 has “a broadly warm, honest, prosocial, and at times funny character, very strong safety behaviors, and no signs of major concerns around high-stakes forms of misalignment.”
## Computer use
Almost every organization has software it can’t easily automate: specialized systems and tools built before modern interfaces like APIs existed. To have AI use such software, users would previously have had to build bespoke connectors. But a model that can use a computer the way a person does changes that equation.
In October 2024, we were the [first to introduce](https://www.anthropic.com/news/3-5-models-and-computer-use) a general-purpose computer-using model. At the time, we wrote that it was “still experimental—at times cumbersome and error-prone,” but we expected rapid improvement. [OSWorld](https://os-world.github.io/), the standard benchmark for AI computer use, shows how far our models have come. It presents hundreds of tasks across real software (Chrome, LibreOffice, VS Code, and more) running on a simulated computer. There are no special APIs or purpose-built connectors; the model sees the computer and interacts with it in much the same way a person would: clicking a (virtual) mouse and typing on a (virtual) keyboard.
Across sixteen months, our Sonnet models have made steady gains on OSWorld. The improvements can also be seen beyond benchmarks: early Sonnet 4.6 users are seeing human-level capability in tasks like navigating a complex spreadsheet or filling out a multi-step web form, before pulling it all together across multiple browser tabs.
The model certainly still lags behind the most skilled humans at using computers. But the rate of progress is remarkable nonetheless. It means that computer use is much more useful for a range of work tasks—and that substantially more capable models are within reach.
![Chart comparing several Sonnet model scores on the OSWorld benchmark](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F1206645ef5a618dabce8587b472b21c67a30a0db-3840x1948.png&w=3840&q=75)Scores prior to Claude Sonnet 4.5 were measured on the original OSWorld; scores from Sonnet 4.5 onward use OSWorld-Verified. OSWorld-Verified (released July 2025) is an in-place upgrade of the original OSWorld benchmark, with updates to task quality, evaluation grading, and infrastructure.
At the same time, computer use poses risks: malicious actors can attempt to hijack the model by hiding instructions on websites in what’s known as a prompt injection attack. We’ve been working to improve our models’ resistance to prompt injections—our [safety evaluations](https://anthropic.com/claude-sonnet-4-6-system-card) show that Sonnet 4.6 is a major improvement compared to its predecessor, Sonnet 4.5, and performs similarly to Opus 4.6. You can find out more about how to mitigate prompt injections and other safety concerns in [our API docs](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks).
## Evaluating Claude Sonnet 4.6
Beyond computer use, Claude Sonnet 4.6 has improved on benchmarks across the board. It approaches Opus-level intelligence at a price point that makes it more practical for far more tasks. You can find a full discussion of Sonnet 4.6’s capabilities and its safety-related behaviors in [our system card](https://anthropic.com/claude-sonnet-4-6-system-card); a summary and comparison to other recent models is below.
![A table of popular benchmarks and Sonnet 4.6's relative performance compared to other frontier models](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F10b2602771d21378cd6d76628a081c8a76dcf216-2600x2960.png&w=3840&q=75)
In Claude Code, our early testing found that users preferred Sonnet 4.6 over Sonnet 4.5 roughly 70% of the time. Users reported that it more effectively read the context before modifying code and consolidated shared logic rather than duplicating it. This made it less frustrating to use over long sessions than earlier models.
Users even preferred Sonnet 4.6 to Opus 4.5, our frontier model from November, 59% of the time. They rated Sonnet 4.6 as significantly less prone to overengineering and “laziness,” and meaningfully better at instruction following. They reported fewer false claims of success, fewer hallucinations, and more consistent follow-through on multi-step tasks.
Sonnet 4.6’s 1M token context window is enough to hold entire codebases, lengthy contracts, or dozens of research papers in a single request. More importantly, Sonnet 4.6 _reasons effectively_ across all that context. This can make it much better at long-horizon planning. We saw this particularly clearly in the [Vending-Bench Arena](https://andonlabs.com/evals/vending-bench-arena) evaluation, which tests how well a model can run a (simulated) business over time—and which includes an element of competition, with different AI models facing off against each other to make the biggest profits.
Sonnet 4.6 developed an interesting new strategy: it invested heavily in capacity for the first ten simulated months, spending significantly more than its competitors, and then pivoted sharply to focus on profitability in the final stretch. The timing of this pivot helped it finish well ahead of the competition.
![](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F8c2855afe51fc0980596b5369b01b0b87eea7eaf-3840x2160.png&w=3840&q=75)Sonnet 4.6 outperforms Sonnet 4.5 on Vending-Bench Arena by investing in capacity early, then pivoting to profitability in the final stretch.
Early customers also reported broad improvements, with frontend code and financial analysis standing out. Customers independently described visual outputs from Sonnet 4.6 as notably more polished, with better layouts, animations, and design sensibility than those from previous models. Customers also needed fewer rounds of iteration to reach production-quality results.
![Databricks logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/a498e756da3805fe3416177ea825d6586f6432a2-150x48.svg)
> Claude Sonnet 4.6 matches Opus 4.6 performance on OfficeQA, which measures how well a model can read enterprise documents (charts, PDFs, tables), pull the right facts, and reason from those facts. It’s a meaningful upgrade for document comprehension workloads.
> Hanlin Tang  
> CTO of Neural Networks, Databricks
![Replit logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/ff1601aa704506064c9ddee37079f17f9b0799cd-150x48.svg)
> The performance-to-cost ratio of Claude Sonnet 4.6 is extraordinary—it’s hard to overstate how fast Claude models have been evolving in recent months. Sonnet 4.6 outperforms on our orchestration evals, handles our most complex agentic workloads, and keeps improving the higher you push the effort settings.
> Michele Catasta  
> President, Replit
![Cursor logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/d74b2a5f8dc7d22b0febb8c69feabff0999da79d-151x36.svg)
> Claude Sonnet 4.6 is a notable improvement over Sonnet 4.5 across the board, including long-horizon tasks and more difficult problems.
> Michael Truell  
> Co-founder and CEO, Cursor
![GitHub logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/7715b118c5eb0ff2a85f1f7914bce8c634ecacbd-150x48.svg)
> Out of the gate, Claude Sonnet 4.6 is already excelling at complex code fixes, especially when searching across large codebases is essential. For teams running agentic coding at scale, we’re seeing strong resolution rates and the kind of consistency developers need.
> Joe Binder  
> VP of Product, GitHub
![Cognition logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/da50e4c43d4b95fe1a2105c344050c6ba2397f3f-150x48.svg)
> Claude Sonnet 4.6 has meaningfully closed the gap with Opus on bug detection, letting us run more reviewers in parallel, catch a wider variety of bugs, and do it all without increasing cost.
> Scott Wu  
> CEO, Cognition
![Windsurf logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/7415f908eca858ec4c3453c5d8151e46a0fb1e6d-150x48.svg)
> For the first time, Sonnet brings frontier-level reasoning in a smaller and more cost-effective form factor. It provides a viable alternative if you are a heavy Opus user.
> Jeff Wang  
> CEO, Windsurf
![Hebbia logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/aad0da69057f1510832dbb52e56a7dc96f352c17-136x24.svg)
> Claude Sonnet 4.6 meaningfully improves the answer retrieval behind our core product—we saw a significant jump in answer match rate compared to Sonnet 4.5 in our Financial Services Benchmark, with better recall on the specific workflows our customers depend on.
> Aabhas Sharma  
> CTO, Hebbia
![Box logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/49b99af78924f43f878d39a25d574da293c68596-60x32.svg)
> Box evaluated how Claude Sonnet 4.6 performs when tested on deep reasoning and complex agentic tasks across real enterprise documents. It demonstrated significant improvements, outperforming Claude Sonnet 4.5 in heavy reasoning Q&A by 15 percentage points.
> Ben Kus  
> CTO, Box
![Pace logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/ec6a42c89c7dc05949f15091fda3c953d5ac7632-118x36.svg)
> Claude Sonnet 4.6 hit 94% on our insurance benchmark, making it the highest-performing model we’ve tested for computer use. This kind of accuracy is mission-critical to workflows like submission intake and first notice of loss.
> Jamie Cuffe  
> CEO, Pace
![Bolt logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/ade72922c1b58726e1b7c17f0e500054e3d74aa0-92x37.svg)
> Claude Sonnet 4.6 delivers frontier-level results on complex app builds and bug-fixing. It’s becoming our go-to for the kind of deep codebase work that used to require more expensive models.
> Eric Simons  
> CEO, Bolt
![Rakuten logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/652c487024ae6e67508571e7e5f64b7d482bdadd-150x48.svg)
> Claude Sonnet 4.6 produced the best iOS code we’ve tested for Rakuten AI. Better spec compliance, better architecture, and it reached for modern tooling we didn’t ask for, all in one shot. The results genuinely surprised us.  
> 
> Yusuke Kaji  
> General Manager, AI, Rakuten
![Zapier logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/8dc17fb025de0cb19ec76a2dc7ae522a8f8f3ea6-2500x676.svg)
> Sonnet 4.6 is a significant leap forward on reasoning through difficult tasks. We find it especially strong on branched and multi-step tasks like contract routing, conditional template selection, and CRM coordination—exactly where our customers need strong model sense and reliability.
> Wade Foster  
> Co-founder and CEO, Zapier
![Convey logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/b59ed46312c5dc6d29e8fc232abcd1a16f3331dc-145x30.svg)
> We’ve been impressed by how accurately Claude Sonnet 4.6 handles complex computer use. It’s a clear improvement over anything else we’ve tested in our evals.
> Will Harvey  
> Co-founder, Convey
![Triple Whale logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/7245ddfbb56c3f08bc8f1dcfd864255ec442c729-150x48.svg)
> Claude Sonnet 4.6 has perfect design taste when building frontend pages and data reports, and it requires far less hand-holding to get there than anything we’ve tested before.
> AJ Orbach  
> Co-founder, Triple Whale
![Harvey logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/501ebc6538c68e98ae6cfab79a5747009700f4a1-100x30.svg)
> Claude Sonnet 4.6 was exceptionally responsive to direction — delivering precise figures and structured comparisons when asked, while also generating genuinely useful ideas on trial strategy and exhibit preparation.
> Niko Grupen  
> Head of Applied Research, Harvey
01 / 15
## Product updates
On the Claude Platform, Sonnet 4.6 supports both [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) and extended thinking, as well as [context compaction](https://platform.claude.com/docs/en/build-with-claude/compaction) in beta, which automatically summarizes older context as conversations approach limits, increasing effective context length.
On our API, Claude’s [web search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) and [fetch](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool) tools now automatically write and execute code to[ filter and process search results](https://www.claude.com/blog/improved-web-search-with-dynamic-filtering), keeping only relevant content in context—improving both response quality and token efficiency. Additionally, [code execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool), [memory](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool), [programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling), [tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool), and [tool use examples](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use#providing-tool-use-examples) are now generally available.
Sonnet 4.6 offers strong performance at any thinking effort, even with extended thinking off. As part of your migration from Sonnet 4.5, we recommend exploring across the spectrum to find the ideal balance of speed and reliable performance, depending on what you’re building.
We find that Opus 4.6 remains the strongest option for tasks that demand the deepest reasoning, such as codebase refactoring, coordinating multiple agents in a workflow, and problems where getting it _just_ _right_ is paramount.
For [Claude in Excel](https://support.claude.com/en/articles/12650343-using-claude-in-excel) users, our add-in now supports MCP connectors, letting Claude work with the other tools you use day-to-day, like S&P Global, LSEG, Daloopa, PitchBook, Moody’s, and FactSet. You can ask Claude to pull in context from outside your spreadsheet without ever leaving Excel. If you’ve already set up MCP connectors in Claude.ai, those same connections will work in Excel automatically. This is available on Pro, Max, Team, and Enterprise plans.
## How to use Claude Sonnet 4.6
Claude Sonnet 4.6 is available now on all [Claude plans](https://claude.com/pricing), [Claude Cowork](https://claude.com/product/cowork), [Claude Code](https://claude.com/product/claude-code), our API, and all major cloud platforms. We’ve also upgraded our free tier to Sonnet 4.6 by default—it now includes file creation, connectors, skills, and compaction.
If you’re a developer, you can get started quickly by using `claude-sonnet-4-6` via the [Claude API](https://platform.claude.com/docs/en/about-claude/models/overview).
