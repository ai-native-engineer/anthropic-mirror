<!-- source: https://academy.claude.com/courses/ai-capabilities-and-limitations -->

13 lessons · 1 quizAI Capabilities and Limitations

What you’ll learnBy the end of this course, you’ll be able to

* Distinguish generative AI from classification and prediction AI, and frame its four core properties as capability-to-limitation continuums
* Explain the two-stage training process (pretraining and fine-tuning) and recognize the behavioral fingerprints it leaves: sycophancy, verbosity, over-caution, and loose confidence calibration
* Explain Next Token Prediction as the core generative mechanism and identify where fabrication concentrates
* Describe how the knowledge cutoff and uneven training coverage shape what a model knows, and recognize when web search, retrieval, or tool use is the fix
* Explain the context window as a hard-edged limit and apply context-placement strategies like front-loading, chunking, and re-supplying critical information
* Predict where instruction-following is tight versus loose, and recognize reasoning drift and letter-over-spirit as steerability failures
* Diagnose real-world AI failures by naming which properties are colliding and choose a targeted fix
* Connect the four properties to the 4D Framework and practice calibrated trust by locating tasks on each continuum

Most people's first experience with a generative AI system is a mix of delight and confusion. It produces a polished summary of a dense report in seconds, then confidently invents a citation that doesn't exist. It follows a detailed instruction perfectly, then ignores a simple one in the very next message. Without a mental model of what's happening underneath, these moments feel random — and it's hard to know whether to trust the next output, or how to fix the last one.

This course gives learners that mental model. It's the companion to [AI Fluency: Framework & Foundations(opens in new tab)](https://academy.claude.com/courses/ai-fluency-framework-foundations): where that course teaches the human competencies (Delegation, Description, Discernment, Diligence), this one teaches the machine properties those competencies are responding to. The two are designed to be taken in either order, and together they form a complete picture of effective human-AI collaboration.

We organize the course around four properties that shape what an AI system can and can't do for you: **Next Token Prediction** (where AI answers come from), **Knowledge** (what the model actually knows, and why it can be confidently wrong), **Working Memory** (what it's paying attention to right now, and what falls off the edge), and **Steerability** (how much control your instructions really give you). Each property sits on a spectrum from capability to limitation, and each section pairs a short explanation with a hands-on exercise so you can feel where the edges are rather than just read about them.

The final section looks at what happens when these properties collide — because in real use, they always do. A long document pushes against working memory while also straying into knowledge the model doesn't have; a vague instruction tests steerability at the same moment next-token prediction is reaching for whatever sounds most plausible. We close with a practical diagnostic: how to look at an unexpected output, recognize which kind of unexpected it is, locate roughly where on the capability-to-limitation continuum your task landed, and respond with a targeted fix instead of a generic retry.

## Recommended prerequisites

None. This course assumes no technical background and no prior experience with AI tools. If you've already completed AI Fluency: Framework & Foundations, you'll recognize where each property connects to the 4Ds — but it's not required.

## Who this is for

Anyone who uses, or is about to start using, generative AI in their work or studies and wants to understand why it behaves the way it does. Educators, students, knowledge workers, and team leads will all find the same core model useful, because the properties it describes don't change across use cases.

## Inside the course

### Getting started

3 lessons

The word 'AI' covers a lot of ground. This section narrows it to the kind of system you'll actually be working with — large language models — and explains how two training stages, pretraining and fine-tuning, turn a raw text predictor into the helpful assistant you interact with. Along the way you'll meet the four-property framework that organizes the rest of the course.

![](https://academy.claude.com/assets/media/12c0541b9a7cf924dd0f9816614e728951342fa99e2386fd9d626a72bc0b91bc.png)![](https://academy.claude.com/assets/media/400df184525ec6697d5c4e53e63ef1cc311f64eb4dfa358d142dbae3a4471050.png)![](https://academy.claude.com/assets/media/e0b78194bc4e4e9f9adac2f73acb9cc12f87f0d962928b0f584bf79e255a5d3d.png)

### Next Token Prediction

2 lessons

Every answer an AI gives is built one token at a time, by predicting what should come next. This section shows what that means in practice: why the model is excellent at well-worn paths like summarizing or reformatting, why it can produce things that sound true but aren't, and how to recognize when a task is pushing into territory where prediction alone isn't enough.

![](https://academy.claude.com/assets/media/7e77e5624f401975964ed33f88ce0530e0b7962ccaf3b2a6a2cdef75e78961b8.png)![](https://academy.claude.com/assets/media/a11c5f181bf051291e21977d7fc1f9e9254fe7c4116d540d4fd47023c67d5dc5.png)

### Knowledge

2 lessons

A model knows what was in its training data — frequently, recently, and consistently. This section unpacks what that implies: it's strong on mainstream topics and popular languages, weaker on anything rare, recent, niche, or contested. You'll practice judging where a question sits on that spectrum, so you know when to trust the answer and when to bring your own sources.

![](https://academy.claude.com/assets/media/cb500f5543c6ee92b5dd91f4509a74eb8539463227d59bc065305b11b9fbffd1.png)![](https://academy.claude.com/assets/media/afe66a1e099d8231f6e0101d75439f2e9d0856b169c3446d3521756b0481c138.png)

### Working Memory

2 lessons

The context window is the model's working memory: everything it can pay attention to right now, and nothing else. This section covers what fits, what quietly falls off the edge, why attention isn't uniform across a long document, and why a fresh session doesn't remember the last one. You'll learn to size up a task against the window before you start, instead of discovering the limit mid-conversation.

![](https://academy.claude.com/assets/media/d4f72ca50184dc0e934193f7ae8cfc8f715e6c027450cf371ce5ac2c61bcab99.png)![](https://academy.claude.com/assets/media/64b37801eae32925fe0b55fea06b2a574670e673cd7993e0063eb62a66779b42.png)

### Steerability

2 lessons

Your instructions are how you steer — but not all instructions land equally. Short, concrete, verifiable asks ('respond as a table', 'under 100 words') work reliably; long reasoning chains, abstract requests, and demands for native precision are where steering starts to slip. This section helps you tell the difference and rewrite a wobbly instruction into one the model can actually follow.

![](https://academy.claude.com/assets/media/d0b76dcb06c0f7900bf67eff0f0f80c59c212c3aedebfa07aab76d7ac3e7db8f.png)![](https://academy.claude.com/assets/media/004276a0d85ae21acb5026a00d8d03dc646dda85f7d7b128c0115e649964c54f.png)

### Putting it all together and next steps

3 lessons

Real tasks rarely test one property at a time. A long contract review strains working memory while reaching past the model's knowledge; a vague creative brief tests steerability right where next-token prediction wants to fill in something plausible. This section shows you how the four properties collide, and gives you a diagnostic for any unexpected output: name which property is in play, place the task on its spectrum, and apply a targeted fix instead of just trying again.

![](https://academy.claude.com/assets/media/3ed895df4051eea55084388e6fa3d95829cf0baf3126ea8a07a07f65c288583a.png)![](https://academy.claude.com/assets/media/5bbcf48c033c840bc679be5a639323a5b4e26519518861e66a9bb883bf84a49a.png)
