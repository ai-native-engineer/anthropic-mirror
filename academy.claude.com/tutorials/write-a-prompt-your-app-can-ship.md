<!-- source: https://academy.claude.com/tutorials/write-a-prompt-your-app-can-ship -->

2. /[Tutorials](https://academy.claude.com/tutorials)

[Tutorials](https://academy.claude.com/tutorials)

# Write a prompt your app can ship

A one-line prompt can leave Claude guessing, and a wrong guess gives your app a reply it can't use. Add context, the output format you want, and constraints to a dentist's reminder prompt, then make a new prompt clear and direct yourself.

10 minClaude Platform

When your app sends Claude's reply straight to a user, nobody checks it first. Whatever Claude writes is what the user gets. So Claude needs to know where the reply goes, how it should look, and what to leave out.

**To make a prompt clear and direct, give Claude those three things: context, the output format you want, and constraints.** Each one answers a question that a new colleague would ask you before starting the task.

## A prompt that leaves Claude guessing[](#a-prompt-that-leaves-claude-guessing)

Say a dentist's booking app texts each patient a reminder the day before their visit. The app sends Claude a one-line task and four lines of data, then texts the patient whatever comes back. Here's the prompt for one patient:

Write a reminder for this appointment.

Patient: Dana Okafor
Date: Thursday, March 12
Time: 2:30 PM
Treatment: Root canal, second visit

Copy prompt

Claude sent back this reply. It's shown as raw text, so you can see every character the app would send:

\*\*Appointment Reminder\*\*

Hi Dana,

This is a friendly reminder of your upcoming dental appointment:

\*\*Date:\*\* Thursday, March 12
\*\*Time:\*\* 2:30 PM
\*\*Treatment:\*\* Root canal (second visit)

\*\*Before your visit:\*\*
- Please arrive about 10 minutes early.
- Eat a light meal beforehand, since your mouth may be numb for a few hours afterward.
- Continue taking any medications as prescribed unless your dentist has told you otherwise.
- Let us know if you've had any pain, swelling, or issues with your temporary filling since your last visit.

If you need to reschedule or have any questions, please call us at [phone number] at least 24 hours in advance.

We look forward to seeing you!

[Practice Name]

The app would text all of that to Dana, and much of it doesn't belong on her phone:

* The asterisks and hyphens are Markdown syntax for bold text and a list. A phone shows them as plain characters.
* The tips on eating and arriving early are advice about the visit, and advice should come from the dentist.
* "Root canal (second visit)" can show on Dana's locked phone, where other people can see it.
* "[phone number]" and "[Practice Name]" are blanks, and nobody fills them in before the text goes out.

Each of these faults traces back to something the prompt left out. It never says that the reminder is a text, that nobody checks it first, or that other people can see it on a locked phone. It doesn't say what the reminder should cover, and gives no practice name or phone number. So Claude wrote a general reminder and left blanks where it had no facts.

**What you get back depends mostly on what you put in.** Before you rework the wording of a prompt, give Claude the facts it's missing.

## Ask what a colleague would ask[](#ask-what-a-colleague-would-ask)

To find what's missing, picture handing the prompt to a colleague who has never seen the app. They have to write the reminder from the prompt alone. If they'd be confused, Claude will be too.

Before writing a word, the colleague would have questions for you. Each question points to one of three parts you can add to the prompt:

| Part | What it tells Claude | What the colleague asks |
| --- | --- | --- |
| Context | What the reply is for, where it goes, and who reads it | "Is this a text or an email? Who is it from? Does anyone check it before it goes out?" |
| Output format | What the reply looks like, such as its length and whether it can use Markdown | "How long should it be? Can it have bold text or a list?" |
| Constraints | What the reply must stick to or leave out | "Should it name the treatment? Should it give advice?" |

Answer each of the colleague's questions in the prompt, in the part where it belongs.

## Add context, format, and constraints[](#add-context-format-and-constraints)

**State the context as facts, and write the output format and constraints as instructions.** Add the reason to any instruction whose purpose Claude couldn't guess.

The booking app's finished prompt below answers the colleague's questions in three paragraphs, one each for the context, the output format, and the constraints.

Try the prompt with and without each part. Every reply is a real one, recorded from Claude for that exact prompt.

## Try it on a new prompt[](#try-it-on-a-new-prompt)

Now make a prompt clear and direct yourself. Say a weather app sends Claude's reply as written, in a push notification that people read on their lock screen at 7 AM. The app's prompt gives Claude only a one-line task and some data:

Write a notification for this forecast.

City: Portland
Morning: cloudy, 48°F
Afternoon: heavy rain from 3 PM
Wind: gusts to 35 mph

Copy prompt

Think about what a colleague who has never seen this app would ask you. Then pick the context, the output format, and the constraints that answer those questions. After each pick, read why it's right or wrong.

Quick check

The weather app's prompt says only "Write a notification for this forecast." Which line would you add to give Claude context?

Morning notifications bring people back to the app, so this one matters a great deal to our team.Your reply goes out unedited as a push notification. People read it on a lock screen at 7 AM.Our app has two million users in 40 cities and has sent forecasts every day since 2019.

Quick check

The notification has to fit on a lock screen. Which line would you add as the output format?

Keep it short and easy to read, because people glance at their phone for a second.Write a bold headline, then two bullets for the morning and the afternoon.Write one sentence of plain text, under 100 characters, with no Markdown.

Quick check

The same prompt runs every morning, with a new forecast each day. Which line would you add as a constraint?

Mention the weather that changes what people wear or carry. Skip the rest.Leave out the wind, because most people want to know whether it will rain.Choose your words with care, so that the forecast doesn't alarm anyone.

## Where to go next[](#where-to-go-next)

**Whenever a reply needs fixing before your app can use it, look for the question your prompt left unanswered.** To fix the prompt in your own code, work through it step by step:

1. Picture a colleague who has never seen your app, and think of what they'd ask before doing the task.
2. In the prompt, answer each question as context, output format, or constraints. State the context as facts, and add the reason to any instruction whose purpose Claude couldn't guess.
3. Send the new prompt with several inputs from your app.
4. Read each reply as raw text, so you can see every character your app would send. Look for the faults you set out to fix, such as Markdown your app can't show, a blank nobody fills in, or a detail your users shouldn't see.

If a fault is still there, find the question the prompt still leaves open, and answer it too.

Reading a few replies can't tell you how well the prompt works across all your app's inputs. For that, you need an eval, a test on your own cases that gives you a number to decide from. From here, take the Introduction to evals course.

* [A prompt that leaves Claude guessing](#a-prompt-that-leaves-claude-guessing)
* [Ask what a colleague would ask](#ask-what-a-colleague-would-ask)
* [Add context, format, and constraints](#add-context-format-and-constraints)
* [Try it on a new prompt](#try-it-on-a-new-prompt)
* [Where to go next](#where-to-go-next)
