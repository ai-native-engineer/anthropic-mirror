<!-- source: https://claude.com/customers/pratham-international -->

Case study | Claude Platform

# How Pratham delivers personalized assessment feedback to thousands of students across India with Claude

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6992a5400e1c7f195d6d23f9_second%20edit%20light%20mode%20converted.png)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6992a54433e0821a6801a39d_second%20edit%20dark%20mode%20converted.png)

Industry:

Beneficial Deployments

Company size:

Large

Product:

Location:

India

1,500+ student assessments

completed across 20 schools

30% → 80% grading accuracy

through iterative prompt engineering with Anthropic

Nonprofits

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698f525504b02eec936ac514_692e248602b0e973666dc35b_og-nonprofit.jpeg)

Turn limited resources into lasting impact. Generate grant proposals, track program outcomes, and free your team to focus on serving your community.

Read more

[Read more](/solutions/nonprofits)Read more

Nonprofits

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Turn limited resources into lasting impact. Generate grant proposals, track program outcomes, and free your team to focus on serving your community.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Nonprofits

Turn limited resources into lasting impact. Generate grant proposals, track program outcomes, and free your team to focus on serving your community.

Education

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698f5245ff22e3ab8e64405f_68c469d2d09b203c164ad8e6_og-claude-education.jpeg)

Trusted, responsible AI tools for students and educators, from personalized learning to research assistance.

Read more

[Read more](/solutions/education)Read more

Education

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Trusted, responsible AI tools for students and educators, from personalized learning to research assistance.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Education

Trusted, responsible AI tools for students and educators, from personalized learning to research assistance.

[Prev](#)Prev

[Next](#)Next

[Pratham](https://pratham.org/) is one of the world’s largest education nonprofits. Founded 30 years ago in India, the organization reaches millions of children annually through programs spanning early literacy to vocational training. Its methods have been validated through more than 10 randomized controlled trials, including studies by MIT's J-PAL. The World Bank has also recognized the Pratham method as one of the best investments in education for global education. Today, Pratham’s programs operate in nearly every Indian state and have been adopted in more than 30 countries.

## With Claude, Pratham achieved:

* **1,500+ student assessments** completed across 20 schools
* **30% → 80% grading accuracy** through iterative prompt engineering with Anthropic
* **90% accuracy** in generating questions aligned to Bloom's Taxonomy—the universal educational framework for assessing everything from basic factual recall to complex, higher-order reasoning

## The challenge: Thousands of practice exams, no way to give individual feedback

In classrooms across India, assessments tend to tell students their results but not how to improve. A teacher managing 60 or more students has little time to provide individualized feedback on each practice exam, and the students who need that feedback the most—those in under-resourced schools and communities—are the least likely to get it. The information exists in their answers, but the problem is turning it into something a student can actually act on.

Pratham has spent 30 years working on exactly these kinds of gaps. But even with a track record of large-scale impact, Pratham kept running into a fundamental constraint: there were never enough people to grade enough practice exams to give students the repetition and feedback they needed.

The issue became especially clear in Pratham's Second Chance program, which helps young women who dropped out of school prepare for India's 10th-grade board exam, a credential required for many jobs. The program serves women without access to trained subject-matter instructors. "These women didn’t get a chance to practice the exam enough times because we didn't have enough people to grade all those answers," said Nishant Baghel, Director of Technology Innovations at Pratham and a visiting scientist at MIT Media Lab. The bottleneck wasn't curriculum or motivation. It was grading.

Pratham's ATM had already reached more than 4,000 learners and auto-graded roughly 8,000 assessments across six Indian states through the Second Chance Program. But the system was challenging to scale: grading could be inconsistent, and there was no structured way to measure accuracy against curriculum standards.

## The solution: Designing an automated assessment and feedback engine for real classroom conditions

That constraint led Pratham to create the Anytime Testing Machine, or ATM: an end-to-end practice assessment system that uses Claude to generate curriculum-aligned questions, digitize handwritten student answers, grade them against structured rubrics, and deliver personalized feedback. The system is designed for the conditions Pratham actually works in. Students write answers by hand on paper and photograph them. The system converts those images to text, then Claude evaluates the responses for content, accuracy, and expression.

Pratham chose Claude after running evaluations across multiple models. "Claude did consistently well across tasks including question generation, checking the quality of generated questions, grading, and feedback," said Sravana Chandra, AI Lead at Pratham. "This, along with Anthropic's focus on safety and responsible AI, led us to choose Claude over other LLMs."

The collaboration was hands-on. Anthropic and Pratham teams met one to two times per week over several months, not just to integrate the model but to calibrate every stage of the pipeline. Grading accuracy started at around 30% when measured against expert-reviewed benchmarks. Through iterative prompt refinement and evaluation design, the teams brought that number to roughly 80%. “We implemented an LLM-as-a-judge framework, benchmarking model evaluations against internally developed golden datasets that were manually validated by subject matter experts,” Chandra explained.

On the feedback generation side, Claude's multilingual fluency was a key advantage. “Given Claude’s linguistic capabilities, it was readily able to handle feedback generation in a mix of Hindi and English, using English terms where relevant (such as for scientific terms) while keeping most of the text in Hindi,” Chandra said.

## The approach: Keeping teachers at the center

A core design principle throughout: teachers review and can refine AI-generated feedback before it reaches students. It reflects Pratham's belief that the teacher's role becomes more important, not less, when AI enters the classroom.

The response from educators has borne that out. Teachers report that automating the grading frees them to focus on targeted instruction rather than administrative work. "Teachers feel empowered because they remain the final evaluators who validate AI feedback before it reaches the student," Chandra noted. The system acts as a capacity multiplier: instead of replacing judgment, it gives teachers better information to exercise it.

For students, the shift is about dignity as much as scores. In these settings, receiving a grade without explanation can be discouraging. Claude's feedback gives learners something specific to work with. Rather than seeing a wrong answer with no context, a student receives a concrete explanation of the concept they missed, with a clear direction for what to study next.

"Human agency is something we focus on,” Baghel says. “Instead of asking what AI can do without teachers, we ask: how can AI help our teachers and students exactly where they're stuck?”

## The results: Personalized feedback reaching learners across six states

With Claude, the ATM now delivers 90% accuracy in generating questions aligned to Bloom's Taxonomy, the global educational framework. On the grading front, accuracy is roughly 80% aligned with content experts on rubric-based scoring. The Claude-powered system has completed more than 1,500 student assessments across 20 schools, with plans to expand to hundreds of thousands of students across India. Separately, the Second Chance program, which currently serves 15,000 women preparing for the grade 10 exam, plans to migrate fully to the Claude-powered pipeline by the end of 2026.

"AI tools like Claude give us a way to reimagine learning for students who do not have access to advanced educational resources," said Madhav Chavan, Pratham's co-founder. "In addition to providing personalized support to understand the textbook, the ATM innovation will help children verify and authenticate their knowledge beyond the textbooks."

## What’s next: Flipping the education system

Chavan sees assessment as just the starting point for something larger: a system where students can eventually be tested on any topic, not only what the curriculum prescribes, and receive a credential for what they actually know.

"Instead of asking children questions about the curriculum, ask them what they know," Chavan said. "If we flip that, we can flip the education system from being a filtration mechanism to one that offers differentiated pathways based on a child's interests and background knowledge. Before AI, this was not possible."

The partnership is already expanding. Anthropic will support Pratham's Tech in TaRL (Teaching at the Right Level) initiative, an AI-powered teacher support system with a randomized controlled trial planned for several thousand students.  The two organizations are also exploring educational digital public infrastructure (including knowledge graphs), as well as geographic expansion to Kenya, Rwanda, and communities across the Global South. Pratham's three-year goal is to evolve the ATM into a learning and credentialing engine that recognizes competencies gained through non-linear pathways, available to learners worldwide.

"AI tools like Claude give us a way to reimagine learning for students who do not have access to advanced educational resources."

Madhav Chavan

Co-founder, Pratham International

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Prev](#)Prev

[Next](#)Next

## Related stories

[How the Garvan Institute is changing the way it does science with Claude](/customers/garvan-institute-qa)How the Garvan Institute is changing the way it does science with Claude

How the Garvan Institute is changing the way it does science with Claude

Customer story

[Customer story](/customers/garvan-institute-qa)Customer story

[MagicSchool on building a safety layer for millions of student conversations](/customers/magicschool-qa)MagicSchool on building a safety layer for millions of student conversations

MagicSchool on building a safety layer for millions of student conversations

Customer story

[Customer story](/customers/magicschool-qa)Customer story

[How YMCA South Australia is building an AI-powered nonprofit with Claude](/customers/ymca-south-australia)How YMCA South Australia is building an AI-powered nonprofit with Claude

How YMCA South Australia is building an AI-powered nonprofit with Claude

Customer story

[Customer story](/customers/ymca-south-australia)Customer story

[How Syracuse University deployed Claude to every student, faculty member, and staff](/customers/syracuse)How Syracuse University deployed Claude to every student, faculty member, and staff

How Syracuse University deployed Claude to every student, faculty member, and staff

Customer story

[Customer story](/customers/syracuse)Customer story
