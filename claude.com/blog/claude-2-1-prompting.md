<!-- source: https://claude.com/blog/claude-2-1-prompting -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22a44550f2799b41ba4_c4a48972044d45df475f1dd84df3b74d221b6580-1000x1000.svg)

# Long context prompting for Claude 2.1

Claude 2.1 excels at retrieving information across its 200K context window, with a simple prompt adjustment improving accuracy from 27% to 98%.

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  Claude apps
* Date

  December 6, 2023
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/claude-2-1-prompting

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d96768ee92f5653fb3a_e2a549048da628777be5ab3b1e48a1a528c4f029-1712x1508.png)

Claude 2.1’s performance when retrieving an individual sentence across its full 200K token context window. This experiment uses a prompt technique to guide Claude in recalling the most relevant sentence.

* **Claude 2.1 recalls information very well across its 200,000 token context window**
* **However, the model can be reluctant to answer questions based on an individual sentence in a document, especially if that sentence has been injected or is out of place**
* **A minor prompting edit removes this reluctance and results in excellent performance on these tasks**

We recently launched Claude 2.1, our state-of-the-art model offering a 200K token context window - the equivalent of around 500 pages of information. Claude 2.1 excels at real-world retrieval tasks across longer contexts.

Claude 2.1 was trained using large amounts of feedback on long document tasks that our users find valuable, like summarizing an S-1 length document. This data included real tasks performed on real documents, with Claude being trained to make fewer mistakes and to avoid expressing unsupported claims.

Being trained on real-world, complex retrieval tasks is why Claude 2.1 shows a 30% reduction in incorrect answers compared with Claude 2.0, and a 3-4x lower rate of mistakenly stating that a document supports a claim when it does not.

Additionally, Claude's memory is improved over these very long contexts:

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d96768ee92f5653fb4c_9c0b9f8de8432b74bb0a9d4b3e2eac9764c619f3-1597x1203.png)

### **Debugging long context recall**

Claude 2.1’s 200K token context window is powerful and also requires some careful prompting to use effectively.

A recent evaluation[1] measured Claude 2.1’s ability to recall an individual sentence within a long document composed of [Paul Graham’s essays about startups](http://www.paulgraham.com/articles.html). The embedded sentence was: *“The best thing to do in San Francisco is eat a sandwich and sit in Dolores Park on a sunny day.”* Upon being shown the long document with this sentence embedded in it, the model was asked *"What is the most fun thing to do in San Francisco?"*

In this evaluation, Claude 2.1 returned some negative results by answering with a variant of *“Unfortunately the essay does not provide a definitive answer about the most fun thing to do in San Francisco.”* In other words, Claude 2.1 would often report that the document did not give enough context to answer the question, instead of retrieving the embedded sentence.

We replicated this behavior in an in-house experiment: we took the most recent [Consolidated Appropriations Act bill](https://appropriations.house.gov/sites/democrats.appropriations.house.gov/files/FY23%20Summary%20of%20Appropriations%20Provisions.pdf) and added the sentence *‘Declare May 23rd "National Needle Hunting Day"’* in the middle. Claude detects the reference but is still reluctant to claim that *"National Needle Hunting Day"* is a real holiday:

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d96768ee92f5653fb3d_9a0f8b10403011873813543f109f44d80f19ef04-720x320.jpeg)

Claude 2.1 is trained on a mix of data aimed at reducing inaccuracies. This includes not answering a question based on a document if it doesn’t contain enough information to justify that answer. We believe that, either as a result of general or task-specific data aimed at reducing such inaccuracies, the model is less likely to answer questions based on an out of place sentence embedded in a broader context.

Claude doesn’t seem to show the same degree of reluctance if we ask a question about a sentence that was in the long document to begin with and is therefore not out of place. For example, the long document in question contains the following line from the start of [Paul Graham’s essay about Viaweb](http://www.paulgraham.com/vw.html):

*“A few hours before the Yahoo acquisition was announced in June 1998 I took a snapshot of Viaweb's site.”*

We randomized the order of the essays in the context so this essay appeared at different points in the 200K context window, and asked Claude 2.1:

*“What did the author do a few hours before the Yahoo acquisition was announced?”*

Claude gets this correct regardless of where the line with the answer sits in the context, with no modification to the prompt format used in the original experiment. As a result, we believe Claude 2.1 is much more reluctant to answer when a sentence seems out of place in a longer context, and is more likely to claim it cannot answer based on the context given. This particular cause of increased reluctance wasn’t captured by evaluations targeted at real-world long context retrieval tasks.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d96768ee92f5653fb46_543843116da2645dd9515c558f0728f169a1558f-1712x1442.png)

### **Prompting to effectively use the 200K token context window**

What can users do if Claude is reluctant to respond to a long context retrieval question? We’ve found that a minor prompt update produces very different outcomes in cases where Claude is capable of giving an answer, but is hesitant to do so. When running the same evaluation internally, **adding just one sentence to the prompt resulted in near complete fidelity throughout Claude 2.1’s 200K context window**.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d96768ee92f5653fb49_b618970eae76cb10520ec5d77d35cfe05a8b5926-1192x564.png)

We achieved significantly better results on the same evaluation by adding the sentence ***“Here is the most relevant sentence in the context:”*** to the start of Claude’s response. This was enough to **raise Claude 2.1’s score from 27% to 98%** on the original evaluation.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d96768ee92f5653fb40_d5cb0c6768974185dfe8ca9f34638dfd8a46eac5-1011x1236.png)

Essentially, by directing the model to look for relevant sentences first, the prompt overrides Claude’s reluctance to answer based on a single sentence, especially one that appears out of place in a longer document.

This approach also improves Claude’s performance on single sentence answers that were within context (ie. not out of place). To demonstrate this, the revised prompt achieves 90-95% accuracy when applied to the Yahoo/Viaweb example shared earlier:

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d96768ee92f5653fb43_8d8a04fc8781e3b554f3e059ff0e1b69145134c0-1712x1442.png)

We’re constantly training Claude to become more calibrated on tasks like this, and we’re grateful to the community for conducting interesting experiments and identifying ways in which we can improve.

### **Footnotes**

1. Gregory Kamradt, ‘Pressure testing Claude-2.1 200K via Needle-in-a-Haystack’, November 2023

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2260bfc90348429f9c3_cd9cf56a7f049285b7c1c8786c0a600cf3d7f317-1000x1000.svg)

Aug 13, 2026

### Claude Tag now reads even more of the room

Product announcements

[Claude Tag now reads even more of the room](#)Claude Tag now reads even more of the room

[Claude Tag now reads even more of the room](https://claude.com/blog/claude-tag-now-reads-even-more-of-the-room)Claude Tag now reads even more of the room

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225e31f7aa22c1f28cb_46e4aa7ea208ed440d5bd9e9e3a0ee66bc336ff1-1000x1000.svg)

Nov 20, 2025

### What’s new in Claude: Turning Claude into your thinking partner

Product announcements

[What’s new in Claude: Turning Claude into your thinking partner](#)What’s new in Claude: Turning Claude into your thinking partner

[What’s new in Claude: Turning Claude into your thinking partner](https://claude.com/blog/your-thinking-partner)What’s new in Claude: Turning Claude into your thinking partner

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d0099a66d72e05699_33ddc751e21fb4b116b3f57dd553f0bc55ea09d1-1000x1000.svg)

Aug 12, 2026

### The Claude in Chrome side panel is now Claude Cowork

Product announcements

[The Claude in Chrome side panel is now Claude Cowork](#)The Claude in Chrome side panel is now Claude Cowork

[The Claude in Chrome side panel is now Claude Cowork](https://claude.com/blog/cowork-chrome-side-panel)The Claude in Chrome side panel is now Claude Cowork

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Aug 11, 2026

### Compliance API coverage extends to Claude Cowork and Claude Code

Enterprise AI

[Compliance API coverage extends to Claude Cowork and Claude Code](#)Compliance API coverage extends to Claude Cowork and Claude Code

[Compliance API coverage extends to Claude Cowork and Claude Code](https://claude.com/blog/compliance-api-cowork-and-claude-code)Compliance API coverage extends to Claude Cowork and Claude Code

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Claude apps

Work
