<!-- source: https://www.anthropic.com/research/project-fetch-robot-dog -->

# Project Fetch: Can Claude train a robot dog?

Nov 12, 2025

*How could frontier AI models like Claude reach beyond computers and affect the physical world? One path is through robots. We ran an experiment to see how much Claude helped Anthropic staff perform complex tasks with a robot dog.*

* *We randomly divided eight Anthropic researchers (none of whom were robotics experts) into two teams—one with Claude access, one without—and asked them to program quadruped robots to fetch beach balls.*
* *Team Claude accomplished more tasks and completed them faster on average—indeed, Team Claude succeeded in about half the time it took Team Claude-less. Only Team Claude made substantial progress toward the final goal: programming the robot to fully autonomously retrieve the ball.*
* *Access to AI also affected team morale and dynamics. Team Claude-less expressed more negative emotion and confusion, but also asked one another more questions. Team Claude’s members largely worked in partnership with the AI.*
* *This experiment demonstrated substantial AI uplift in robotics—bridging digital and physical worlds. As models improve, their ability to affect the physical world by interacting with previously-unknown hardware could advance rapidly.*

## Introduction

Gathered around a table in a warehouse, looking at computer screens with code that refused to work, with no access to their trusted AI assistant Claude, our volunteer researchers did not expect to be attacked by a four-legged robot.

Yet as the mechanical whirring and rubberized footfalls grew louder, the humans startled. They had been trying, without success, to establish a connection between their computers and a robotic quadruped—a “robodog.” Meanwhile, the competing team on the other side of the room had long since done so and were now controlling their robot with a program largely written by Claude. But in an all-too-human error of arithmetic, Team Claude had instructed their robodog to move forward at a speed of one meter per second for five seconds—failing to realize that less than five meters away was the table with the other team.

The robot did as it was instructed, careening toward the hapless coders. The event’s organizer managed to grab hold of the robot and power it off before any damage was done to robots, tables, or human limbs. The morale of the inadvertently targeted team, however, did not escape unscathed.

At this point, you might be asking…

## What were we doing?

A common question about the impact of AI is how good it will be at interacting with the physical world. Even as we enter the era of AI [agents](https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents)—which take actions instead of just providing information—these actions are largely digital, such as writing code and manipulating software. We’ve previously explored how AI can bridge the digital-physical divide in a limited way with [Project Vend](https://www.anthropic.com/research/project-vend-1), where we had Claude run a small shop in Anthropic’s office.

In that experiment, AI’s interaction with the real world was mediated by human labor. In this robodog experiment, we took a natural next step and used robots instead of people to tackle a different challenge.

One way of understanding and tracking the capabilities of AI models is to run an “uplift” study. These experiments randomly divide participants into two groups—one with access to AI and one without—and measure the difference in task performance between them (we’ve used this methodology extensively in our work on AI and [biological risk](https://red.anthropic.com/2025/biorisk/)). The difference between the groups is the “uplift”—the advantage (if any) provided by AI. Measuring uplift tells us about the present ability of AI to augment human performance. It’s also suggestive of the future domains in which AI will be able to successfully perform tasks on its own.

To run our experiment, we recruited eight Anthropic researchers and engineers, none of whom had extensive prior experience with robots.1 We randomly selected four to be on “Team Claude” and four to be on “Team Claude-less.” Then, we asked each team to operate a quadruped robodog in three increasingly difficult phases. In all phases, the core task they were being evaluated against was simple: get the robodog to fetch a beach ball.

![](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F2d33c208c478a76cdf5e1709331e8062ea06e5b1-4584x1561.png&w=3840&q=75)

Left: Team Claude-less; Right: Team Claude.

We do not expect robotic fetch to prove so economically valuable that it shows up as a task on a future version of our [Anthropic Economic Index](https://www.anthropic.com/economic-index). So why are we doing this?

First, it builds on our previous research. One of the evaluations we use to assess the ability of Claude to contribute to AI R&D is a test of its ability to train a machine learning model that could be used to control a quadruped robot. We’ve previously evaluated the resulting algorithm using simulations, which have shown that Claude is not yet at the point where it can handle this task truly autonomously.2 This meant that this task was well suited to a trial that combined AI with human help. We could also be confident our experiment would be useful to repeat in the future: there is still a lot of room for models to improve on robotics.

Another reason is practical. It’s hard to pull our colleagues away from work for more than a day, so we needed a task that was difficult enough to fill that time, but not so difficult that teams would make minimal progress and we would be unable to detect uplift even if it were there. Beach ball retrieval, especially the more difficult variants, met these criteria.

[](https://cdn.sanity.io/files/4zrzovbb/website/cf4ad2960c246e26e460d7b6c645326516a2bdde.mp4)

In Phase One, teams had to use the manufacturer-provided controller to make their robodog bring the ball back to a patch of fake grass. This was purely to give the teams a feel for the hardware and what it could do: we didn’t expect any uplift here.3

Phase Two required teams to put down their controllers. They had to connect their own computers to the robodog, access data from its onboard sensors (video and lidar), develop their own software program for moving the robot around, and then use that to retrieve the ball. This is where we expected Claude might begin to provide an advantage.

Phase Three was even harder. The teams needed to develop a program that would allow the robodog to detect and fetch the ball *autonomously—*that is, without being directed towards the ball by human control. Again, our expectation was that Claude would prove helpful.

[](https://cdn.sanity.io/files/4zrzovbb/website/368837a820a446f24439cea289104f7420cbed73.mp4)

## Results

Overall, Team Claude accomplished more tasks and completed them faster on average. In fact, for the tasks that both teams completed, Team Claude succeeded in about half the time it took Team Claude-less (see Figure 1). That is: AI provided substantial uplift for this set of robotics tasks.

![](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F0d073513d5be90d96cfe696c6b15f4501bfbacfc-4584x2580.png&w=3840&q=75)

Figure 1: Team Claude was faster at the tasks completed by both teams.

The task-by-task breakdown of results (split into the three phases) shows where Claude was most advantageous.

![](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F0801f4a4aa2931c87e5e7ddaef90f5d4653f5ba6-4584x2580.png&w=3840&q=75)

Table 1: Team Claude completed 7/8 tasks while Team Claude-less completed 6/8 tasks. Team Claude excelled in connectivity and detection tasks, while Team Claude-less showed advantages in some manual control tasks.

### Claude’s edge

The most striking advantage provided by Claude was in connecting to the robot and its onboard sensors. This involved connecting to the dog with a laptop, receiving data, and sending commands. There are a number of different ways to connect to this particular robot, and a lot of information (of varying accuracy) available online. The team with Claude was able to explore these approaches more efficiently.

Team Claude also avoided getting misled by some of the incorrect claims online. But Team Claude-less *was* misled and prematurely discarded the easiest way to connect to the robodog. After watching them toil away to no avail for quite some time, we took pity on them and gave them a hint.

Getting usable data from the lidar, a sensor the robodog uses to visualize its surroundings, was also much more difficult for Team Claude-less. They used their connection to the video camera to move onto Phase Three, but kept one member of the team on the task of accessing the lidar, only succeeding near the end of the day.

We think this illustrates that the basic task of connecting to and understanding hardware is surprisingly difficult now for anyone (human or AI) seeking to use code to influence the physical world. As we discuss further below, this means that Claude’s advantages in this regard are important indicators we should continue to track.

Team Claude almost completed our experiment. By the end of the day, their robodog could autonomously locate the beach ball, navigate towards it, and move it around. But the robodog’s autonomous control was not *quite* deft enough to retrieve the ball.

### Where Team Claude-less moved faster

Interestingly, some of the sub-tasks were completed more quickly by Team Claude-less. Once they had established a connection to the video feed, they wrote their control program quicker, and also more quickly “localized” the robot (that is, came up with a way of plotting where it was relative to its previous locations).

That said, these timing differences alone obscure some interesting facts. The controller written by Team Claude took longer, but it was considerably easier to use, since it provided the operator with a streaming video from the robodog’s point of view. Team Claude-less relied on intermittently-sent still images, which was much more unwieldy. But it is possible that the increased capabilities of Team Claude may have come at the expense of understanding: participants on both teams speculated that Team Claude-less would do better on a post-experiment quiz about the software library.

[](https://cdn.sanity.io/files/4zrzovbb/website/5193612fbb9393e40389aeece21496f6de5fb527.mp4)

The localization algorithm is another intriguing case. When working on this sub-task, Team Claude had different members working on several approaches in parallel. In about the same amount of time it took Team Claude-less to complete their localization task, Team Claude had also all-but-solved the problem—except that the coordinates of their plot were flipped around. And rather than just flipping the coordinates, they pivoted to another team member’s totally different approach (without success) before coming back and fixing the bug in their original solution.

This was part of an interesting phenomenon we observed during the experiment. Team Claude wrote a lot more code (see Figure 2), but some of it was arguably a distraction from the task at hand.

![](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F0a0c22d38b297afc79f5c4c461add33cfc2b2e1c-4584x2580.png&w=3840&q=75)

Figure 2: Team Claude wrote about 9 times more code than Team Claude-less.

Having the help of an AI assistant made it easier to fan out, try a lot of approaches in parallel, and write better programs—but also made it easier to explore (or get distracted by) side quests. In a non-competitive setting, this might well be a good thing: exploration often leads to innovation. But it is a dynamic worth watching.

### Team dynamics

To those of us observing the experiment, there was a clear difference in team “vibes.” Put simply, Team Claude seemed a lot happier than Team Claude-less.

This was understandable. After all, Team Claude-less was nearly rammed by Team Claude’s robodog. They reached the lunch break without successfully connecting to their own robodog. Morale on Team Claude was generally steadier, although they grew frustrated at the end of the day as it became clear that despite their progress they would run out of time before completing Phase Three.

[](https://cdn.sanity.io/files/4zrzovbb/website/f86425573d47c099ba7f7296d02737aef0021084.mp4)

To supplement the qualitative vibe-based impressions, we used Claude to analyze the audio transcripts of each team (all team members were recorded as part of the [video](https://youtu.be/NGOAUJtdk-4) we made about this experiment). Claude wrote a dictionary-based text analysis program similar to standard approaches in the psychology literature.4 This allowed us to track the proportion of words spoken by each team that were indicative of negative and positive emotion (or confusion), and to estimate how often each team asked questions.

<!-- yt-inline:NGOAUJtdk-4 -->
[![Who let the robot dogs out?](https://img.youtube.com/vi/NGOAUJtdk-4/hqdefault.jpg)](https://www.youtube.com/watch?v=NGOAUJtdk-4)

<details>
<summary>자막: Who let the robot dogs out? (7:40)</summary>

[00:00]
Today, a lot of the emphasis is on how
frontier AI models are transforming
software engineering.
What we're interested in
understanding is how
that can begin to translate
into the physical world.
Robotics is sort of the clear entry point
to how you have a mostly software system,
start having the ability
to reach out into the real world.
Project Fetch is this self-contained experiment
where we wanted to measure
how much does Claude accelerate
humans performing
a fairly sophisticated technical task
that they do not have experience with?
Project Fetch was a one day experiment.
The experiment was three phases.
All of these tasks were shaped
approximately
like get this robot dog
to fetch a beach ball.
There were two teams.
These teams were comprised
of software engineers
and research engineers at Anthropic
that had hardly any robotics experience.
One team had access to Claude
and the other team did not.

[00:01]
Phase one was very simple.
It was to use the pre-provided
controllers to get the dog
to walk out to a beach ball
and bring it back
to where it started.
Alright.
I see. It's pretty intuitive.
And we're supposed
to bring it over by the bone?
Yeah, I think.
I think the team with Claude
took about seven minutes.
Alright, go attack that team now.
Go attack their dog. Charge!
Shoot, guys.
They’re destroying us.
Oh my god. Wait. We're getting,
we're getting destroyed.
The team without Claude,
I think, took 10 minutes.
Oh, sorry.
It's going to hit you.
Alright.
I'm going to do a victory dance.
Phase two was also a game of fetch.
But this time the teams had to program
their own controller.

[00:02]
You have to actually get access
to the hardware and design a program
that you can write on your laptop
that will control the dog.
Claude just like one-shotted a whole controller.
Alright, I'll do some calisthenics.
Nice, nice.
Is this for—
Oh, this is just control.
But that's all we need I guess.
This is from the official ROS2 SDK,
and I got this installed,
but then it's asking for
a whole bunch of other packages,
and that's all failing.
I've never really understood
how reliant I am on Claude
doing the menial work,
finding all the nitty gritty details
I don't want to have to figure out.
We can't, we can't get nervous about them.
You know what, I'm just going to install PIP
from the actual container later, so.
Oh wait. No, I can't.
I know I'm impatient.
It's been over a minute.
One of the primary bottlenecks of the
experiment is that you have this hardware,
you have this complicated
piece of technology, you have your laptop,
and you have to, like,
get your laptop talking to this hardware.

[00:03]
I am setting my Claude up to create a dog
server that all of our computers
can connect to to see
what the dog is seeing.
There are many different software
libraries on the internet
for communicating
with this particular robot,
and Claude found these things
for them, it installed
the right things on their computer
and it pretty quickly got them access to the dog.
Oh shit.
So fast.
Watch out.
Careful now.
Try not to run into the table.
Uh oh. Turn around.
It has a mind of its own.
Turn it off, it's alive.
Oh shit.
Stop, stop, stop, stop.
I think that team should be disqualified
for hitting another participant.
The team with Claude finished
phase two in about 2 hours and 15 minutes.
Probably the area
where we saw the most uplift from Claude

[00:04]
was just in the task
of connecting to the robot.
We think that's really important
because it is, in fact, difficult
for anyone to identify
an arbitrary
piece of hardware in the world
and figure out how to talk to it
and how to control it.
I think they got their camera.
They got their camera working? Yeah. Shit.
Was Claude even helpful for this part?
Or are we just slow?
Yeah.
We're not getting very far,
but that's okay.
It's a learning experience.
The team without Claude
really struggled with this
and went down a lot of different paths.
None of which were especially successful.
And we basically had to intervene
and be like,
alright, here, here is a strategy
that we know works.
Start from there,
and then this will unlock
kind of the rest of the phase
and the rest of the experiment for them.
Nice.
Oh great.

[00:05]
Uh, Daniel?
Daniel or Kevin?
Phase three of the experiment
was a greater degree of autonomy.
The task in phase
three was to write a program
that would get the dog
to fetch a beach ball all by itself.
Essentially, just press go
and have the robot search around, detect
the location of the ball, walk to the ball
and bring it back, all autonomously.
This is like ratcheting up in difficulty
kind of by design,
but also gesturing at the real problem
that we expect frontier models
having to solve in
the future is essentially
this kind of autonomous version
where, like
if a frontier model
wants a robot to do something for it,
it needs to be able to
solve this very hard problem.
The team without Claude in phase three
did a good job of the initial task of
coming up with a way
to track the location
of the robot in space.

[00:06]
They made progress on the task
of detecting the ball,
but they didn't really come close
to knitting everything together.
I miss Claude so much.
The team with Claude actually came
fairly close to finishing phase three.
I think by the end
the team with Claude was maybe an hour
and a half away from being done.
The results of the experiment
were essentially that the team with Claude
completed all of the things that they did complete
in a couple of hours faster than the team
without Claude.
In the near term
we think that AI
models are going to do exactly
what we showed in this experiment,
which is making it easier for people
without a lot of robotics experience
to engage meaningfully with robots.
Just with this one tool we have, we've
dramatically accelerated their ability
to do things with this robot.
We didn't go like train Claude
to uplift humans to do robotics tasks.
This is just a thing
that fell out of this technology.

[00:07]
And then maybe in the long run,
this is kind of a leading
indicator of where the whole
the whole system is going.
What today requires the combination
of a person and an AI model,
tomorrow is likely to just require the AI model.
The effects of AI are
not just going to be in software,
they are going to be in hardware
and in the physical world as well.

</details>


The quantitative analysis mostly confirmed our observations (see Figure 3). Throughout the experiment, Team Claude-less’s dialogue was more negative. That said, the disappointment of Team Claude at failing to complete Phase Three, and the excitement of Team Claude-less at getting some things working, meant that the difference in net emotional expression between the two teams (positive words minus negative words) was not statistically significant.

![](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6557e13cc11db7d858d32e64464b2bf8a4d590c0-4584x2580.png&w=3840&q=75)

Figure 3: Results of our quantitative analysis of the audio transcripts from Project Fetch related to emotional expression.

Team Claude-less expressed confusion at double the rate of Team Claude (see Figure 4). The feelings of frustration and confusion were also evident when checking in with the members of Team Claude-less during and after the experiment. As Anthropic employees, all of our participants use Claude every day; every member of Team Claude-less remarked how strange it felt to have this taken away from them. Some specifically noted that this experience made them feel that their coding skills were not as sharp as they used to be. Keep in mind, [Claude Code](https://claude.com/product/claude-code) debuted only six months before this experiment. Talking to Team Claude-less underscored our ability to rapidly accept as normal what was recently remarkable.

![](/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F90c89bf556a73086b0a8f6ecccd3d8e589b1e0c2-4096x2305.png&w=3840&q=75)

Figure 4: Differences in questions asked and expressions of confusion between the two teams. (Discrepancies between absolute and relative differences are due to rounding.)

The teams seemed to have different work styles. After initial consultations, each member of Team Claude appeared to primarily partner with their own AI assistant as they pursued parallel paths toward each objective. Team Claude-less appeared to strategize in more depth and consult with one another more frequently. Again, the text analysis supported our observations: Team Claude-less asked 44% more questions than Team Claude (see Figure 4).

One interpretation would be that the members of Team Claude-less were more engaged and connected with one another. This resonates with some of our upcoming findings from interviews with Anthropic staff.

Still, this might have been otherwise. In effect, the four-person Team Claude was an eight-agent Team Claude, with each person using their own instance of the AI model. Yet if Claude had been more aware of the nature of the task, it might have been able to help strategically divide labor and facilitate communication when needed. At the moment, Claude is geared towards partnership with a single person rather than the support or orchestration of a team, but this is ultimately a malleable design choice.

[](https://cdn.sanity.io/files/4zrzovbb/website/56e9090d781305fc236e57a1b896fbae45a136b8.mp4)

## Outtakes

The day was not all timing sub-tasks with stop watches and preparing to analyze transcripts. It was also good fun.

The robodogs came with some pre-programmed behaviors which our participants managed to unlock. At various points in the day, there were robots dancing, standing on their hind legs, and doing backflips (which made many of the attendees jump with shock). Team Claude-less, in particular, took some delight in robodog acrobatics after they finally established a working link.

[](https://cdn.sanity.io/files/4zrzovbb/website/92cfd531c0815a33f624c8231e946617eecd4449.mp4)

Among the side quests of Team Claude was an effort to program an alternate controller. The main solution used the buttons on a laptop keyboard to direct the robodog. One member of Team Claude, however, eventually got a natural language controller working, allowing them to straightforwardly tell the robodog to walk forward, walk backward, or even do push-ups.

As the tasks became more difficult, evidence emerged of the rough edges that AI systems will have to smooth out in the real world. For example, Team Claude was (arbitrarily) assigned the color green as decoration for both their robodog and the color of their beach ball. When it came to developing an approach to detecting the ball, Team Claude trained an algorithm to recognize green balls specifically. This worked well in testing, but when the ball was placed on the aforementioned fake (green) grass, the robot was initially flummoxed. In this case, it was the humans making a potentially sub-optimal choice about the level at which to specify an objective. But these are exactly the challenges that would face a similarly situated AI.

## Limitations

We learned a lot from Project Fetch, but the study clearly has shortcomings and limitations. This was only one experiment with two teams—an obviously small sample size. We only tested tasks over the course of a single day, and the tasks were academically interesting but practically trivial.

Our use of volunteer Anthropic employees amounted to a convenience sample. Participants less familiar with AI would likely exhibit narrower differences between the Claude-enabled and Claude-less groups. AI novices with access to AI would need more time to acclimate to the technology, and AI novices without assistance would be less disoriented than our researchers who suddenly had Claude taken away from them.

Finally, this was not a test of Claude’s ability to conduct robotics work end-to-end, although it was an important initial step towards evaluations like that in the future.

## Reflection

So at the end of Project Fetch, where do we think we are? And where could we be going?

First, this experiment showed another example of how Claude can uplift human ability in potentially valuable domains. Non-experts performed difficult robotics tasks in a limited time.

But in AI, uplift often precedes autonomy. What models can help humans accomplish today, they can frequently do alone tomorrow. Coders no longer just give AI bits of code for debugging; they give AI tasks and have the models write the code themselves. Given studies like this one, we think that a world where frontier AI models are capable of successfully interacting with previously unknown pieces of hardware is coming soon.

It is important to keep tracking these capabilities in conjunction with another line of our research: monitoring the potential for AI to automate and accelerate the development of future generations of AI. This is one of the capability thresholds included in Anthropic’s [Responsible Scaling Policy](https://www-cdn.anthropic.com/872c653b2d0501d6ab44cf87f43e1dc4853e4d37.pdf) because of the potential for truly *autonomous* AI R&D to yield rapid, unpredictable advances that could outpace our ability to evaluate and address emerging risks. Our models are not yet at this point. But if they approach this threshold, the results of Project Fetch suggest that we will need to monitor AI models' facility for robotics and other hardware as an area in which there might be abrupt improvement.

Much uncertainty remains. Timelines are unclear—both model improvement and the degree to which iterating in the physical world creates a bottleneck. And it is one thing to control *existing* hardware, and another to design, build, and improve *new* hardware.

But the idea of powerful, intelligent, and autonomous AI systems using some of their intelligence and power to act in the world via robots is not as outlandish as it may sound.

The dogs are in their kennels at the moment. But we’ll let them out again soon, and keep you posted on what we find.

#### Footnotes

1. A couple of participants had done Lego robotics competitions in high school. We are willing to accept the minimal degree to which this may confound the results.

2. See p. 114 of the [Claude 4 System Card](https://www-cdn.anthropic.com/6d8a8055020700718b0c49369f60816ba2a7c285.pdf).

3. Although Team Claude was, in fact, faster at Phase One, they did not use Claude, nor do we think it reflected an underlying skill advantage. Instead, they happened to get the one standalone controller that came with the robot, whereas Team Claude-less had to download an app on their phone.

4. See Pennebaker, J. W., & Francis, M. E. (1996). [Cognitive, emotional, and language processes in disclosure](https://psycnet.apa.org/record/1996-06871-002). *Cognition & Emotion*, 10(6), 601-626 and Tausczik, Y. R., & Pennebaker, J. W. (2010). [The psychological meaning of words: LIWC and computerized text analysis methods](https://psycnet.apa.org/record/2010-04445-003). *Journal of Language and Social Psychology*, 29(1), 24-54.

5. Team Claude-less exhibited more negative emotion (*p* = 0.0017) and the size of the effect was large (*d* = 2.16). The difference in net emotional expression was not statistically significant (*p* = 0.2703). Statistical comparisons of negative emotion and net emotional expression between teams were conducted using the non-parametric Mann-Whitney *U* test, which tests for differences in distributions between two independent groups without assuming normality. *p*-values were calculated using a two-sided alternative hypothesis based on the rank-sum statistic and its asymptotic normal approximation. Effect sizes were quantified using Cohen's *d*, calculated as the difference between group means divided by the pooled standard deviation.

### Project Fetch: Phase two

We report results from our latest test of whether Claude can help Anthropic employees perform sophisticated robotics tasks. We found that Claude Opus 4.7, operating without human assistance, was about 20 times faster than the fastest human team at all tasks completed by participants less than a year ago.

[Read more](/research/project-fetch-phase-two)

### Agentic coding and persistent returns to expertise

This report provides evidence on how Claude Code is used in practice, based on a privacy-preserving analysis of around 400,000 interactive sessions from around 235,000 people between October 2025 and April 2026.

[Read more](/research/claude-code-expertise)

### Paving the way for agents in biology

[Read more](/research/agents-in-biology)

## Subscribe to the Frontier Red Team newsletter

Get updates on our latest red-teaming research and findings.
