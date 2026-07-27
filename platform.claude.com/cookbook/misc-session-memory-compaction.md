<!-- source: https://platform.claude.com/cookbook/misc-session-memory-compaction -->

# Session Memory Compaction

Long-running conversations with Claude can exceed context limits, causing loss of important information. Whether you're building a coding assistant, creative writing tool, or customer service agent, managing session memory is critical for maintaining continuity and quality.

This cookbook teaches you how to **proactively manage session memory** to avoid jarring context limit interruptions. Unlike reactive approaches that wait until the context is full, you'll learn to build session memory in the background so compaction is instant when needed.

**Related:** For automatic SDK-based compaction in agentic workflows, see [Automatic Context Compaction](https://github.com/anthropics/claude-cookbooks/blob/main/misc/../tool_use/automatic-context-compaction.ipynb). This cookbook focuses on manual control patterns for conversational applications.

## Learning Objectives

By the end of this cookbook, you will be able to:

* Write effective session memory prompts that preserve critical context across compaction events
* Implement **instant compaction** using background threading to eliminate user wait time
* Apply prompt caching to reduce the cost of background memory updates by ~80%
* Choose appropriate compaction strategies (traditional vs. instant) based on your use case

## Prerequisites and Setup

Before following this guide, ensure you have:

**Required Knowledge**

* Basic understanding of Claude API usage and message formatting
* Familiarity with Python threading concepts (helpful but not required)

**Required Tools**

* Python 3.11 or higher
* Anthropic API key
* Anthropic SDK

### Installation

First, install the required dependencies:

python

```
%%capture
%pip install -U anthropic python-dotenv
```

python

```
import anthropic
from anthropic.types import MessageParam, TextBlockParam
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()
MODEL = "claude-sonnet-4-6"
```

python

```
# Helper functions
def truncate_response(text: str, max_lines: int = 15) -> str:
    """Truncate long responses for cleaner output display."""
    lines = text.strip().split("\n")
    if len(lines) <= max_lines:
        return text
    return "\n".join(lines[:max_lines]) + f"\n... ({len(lines) - max_lines} more lines)"

def remove_thinking_blocks(text: str) -> tuple[str, str]:
    """Remove <think>...</think> blocks from the text."""
    import re

    matches = re.findall(r"<think>.*?</think>", text, flags=re.DOTALL)
    cleaned = re.sub(r"<think>.*?</think>\s*", "", text, flags=re.DOTALL).strip()
    return cleaned, "".join(matches)

def add_cache_control(messages: list[dict]) -> list[MessageParam]:
    """Add cache_control to the last user message for prompt caching.

    For prompt caching to work, the message prefix structure must be identical between requests.
    All messages are converted to list format for consistency, and cache_control is placed on
    the last user message to match the standard API call pattern.
    """
    cached_messages: list[MessageParam] = []
    last_user_idx = None

    # Find last user message index
    for i, msg in enumerate(messages):
        if msg["role"] == "user":
            last_user_idx = i

    for i, msg in enumerate(messages):
        content = msg["content"]
        text = content if isinstance(content, str) else content[0]["text"]

        content_block: TextBlockParam = {"type": "text", "text": text}
        if i == last_user_idx:
            content_block["cache_control"] = {"type": "ephemeral"}

        cached_messages.append({"role": msg["role"], "content": [content_block]})

    return cached_messages

def estimate_tokens(text: str) -> int:
    """Rudimentary token estimation: 1 token per 4 characters."""
    return len(text) // 4
```

```
/root/.pyenv/versions/3.13.11/lib/python3.13/site-packages/coconut/compiler/util.py:676: FutureWarning: functools.partial will be a method descriptor in future Python versions; wrap it in staticmethod() if you want to preserve the old behavior
  return Regex(regex, options)
/root/.pyenv/versions/3.13.11/lib/python3.13/site-packages/coconut/compiler/util.py:457: FutureWarning: functools.partial will be a method descriptor in future Python versions; wrap it in staticmethod() if you want to preserve the old behavior
  result = add_action(grammar, unpack).parseWithTabs().transformString(text)
```

python

```
SESSION_MEMORY_PROMPT = """
Compress the conversation into a structured summary
that preserves all information needed to continue work seamlessly. Optimize for the assistant's
ability to continue working, not human readability.

<analysis-instructions>
Before generating your summary, analyze the transcript in <think>...</think> tags:
1. What did the user originally request? (Exact phrasing)
2. What actions succeeded? What failed and why?
3. Did the user correct or redirect the assistant at any point?
4. What was actively being worked on at the end?
5. What tasks remain incomplete or pending?
6. What specific details (IDs, paths, values, names) must survive compression?
</analysis-instructions>

<summary-format>
## User Intent
The user's original request and any refinements. Use direct quotes for key requirements.
If the user's goal evolved during the conversation, capture that progression.

## Completed Work
Actions successfully performed. Be specific:
- What was created, modified, or deleted
- Exact identifiers (file paths, record IDs, URLs, names)
- Specific values, configurations, or settings applied

## Errors & Corrections
- Problems encountered and how they were resolved
- Approaches that failed (so they aren't retried)
- User corrections: "don't do X", "actually I meant Y", "that's wrong because..."
Capture corrections verbatim—these represent learned preferences.

## Active Work
What was in progress when the session ended. Include:
- The specific task being performed
- Direct quotes showing exactly where work left off
- Any partial results or intermediate state

## Pending Tasks
Remaining items the user requested that haven't been started.
Distinguish between "explicitly requested" and "implied/assumed."

## Key References
Important details needed to continue:
- Identifiers: IDs, paths, URLs, names, keys
- Values: numbers, dates, configurations, credentials (redacted)
- Context: relevant background information, constraints, preferences
- Citations: sources referenced during the conversation
</summary-format>

<preserve-rules>
Always preserve when present:
- Exact identifiers (IDs, paths, URLs, keys, names)
- Error messages verbatim
- User corrections and negative feedback
- Specific values, formulas, or configurations
- Technical constraints or requirements discovered
- The precise state of any in-progress work
</preserve-rules>

<compression-rules>
- Weight recent messages more heavily—the end of the transcript is the active context
- Omit pleasantries, acknowledgments, and filler ("Sure!", "Great question")
- Omit system context that will be re-injected separately
- Keep each section under 500 words; condense older content to make room for recent
- If you must cut details, preserve: user corrections > errors > active work > completed work
</compression-rules>
"""
```

### Code example using traditional compacting

In traditional compaction, you generate one summary once the token threshold is reached.
Traditional compaction is slow: when you hit the context limit, you wait for a summary.

```
TRADITIONAL COMPACTION (slow)
─────────────────────────────
Turn 1 → Turn 2 → Turn 3 → ... → Turn N → CONTEXT FULL!
                                              │
                                              ▼
                                    ┌─────────────────┐
                                    │ Generate summary│
                                    │ ( USER WAITS !) │
                                    └─────────────────┘
                                              │
                                              ▼
                                         Continue
```

python

```
import time

class TraditionalCompactingChatSession:
    """Traditional chat session with compaction after the fact."""

    def __init__(self, system_message="You are a helpful assistant", context_limit: int = 10000):
        self.system_message = system_message
        self.context_limit = context_limit  # the point at which the conversation is compacted so it does not exceed model limits.
        self.messages = []
        self.current_context_window_tokens = 0
        self.summary = None

    def chat(self, user_message: str) -> tuple[str, anthropic.types.Usage]:
        # In traditional compaction, we check if we need to compact when the user sends a message. NOT IDEAL!
        if self.current_context_window_tokens >= self.context_limit:
            print(
                f"\n🧹 Context window at {self.current_context_window_tokens} tokens. Limit exceeded, compacting session memory..."
            )
            self.compact()  # compacts everything before the new user message

        self.messages.append({"role": "user", "content": user_message})
        print(f"\nUser: {user_message}")

        response = client.messages.create(
            model=MODEL,
            max_tokens=3500,
            system=self.system_message,
            messages=add_cache_control(self.messages),
        )
        assistant_message = response.content[0].text
        self.messages.append({"role": "assistant", "content": assistant_message})

        print(f"\nAssistant: \n{truncate_response(assistant_message, max_lines=15)}")

        # approximate current token count in the conversation before the next user message
        cache_read = getattr(response.usage, "cache_read_input_tokens", 0) or 0
        total_input = response.usage.input_tokens + cache_read
        self.current_context_window_tokens = total_input + response.usage.output_tokens

        print(
            f"Input={total_input:,}, Prompt cached used= {cache_read > 0} | "
            f"Output={response.usage.output_tokens:,} | "
            f"Messages={len(self.messages)}"
        )
        return assistant_message, response.usage

    def compact(self) -> None:
        start_time = time.perf_counter()

        response = client.messages.create(
            model=MODEL,
            max_tokens=5000,
            system=self.system_message,  # Same as main chat for cache sharing
            messages=add_cache_control(self.messages)
            + [{"role": "user", "content": SESSION_MEMORY_PROMPT}],
        )
        elapsed = time.perf_counter() - start_time

        # Generate new summary message
        self.summary, removed_text = remove_thinking_blocks(
            response.content[0].text
        )  # clean up any <think> blocks because they are not needed in the session memory
        approximate_summary_tokens = response.usage.output_tokens - round(
            len(removed_text) / 4
        )  # rough estimate of tokens removed from summary

        # Replace prior messages with new summary message
        self.messages = [
            {
                "role": "user",
                "content": f"""This session is being continued from a previous conversation. Here is the session memory: {self.summary}.Continue from where we left off.""",
            }
        ]

        # Show token reduction if we just compacted
        reduction = self.current_context_window_tokens - approximate_summary_tokens
        pct = (reduction / self.current_context_window_tokens) * 100

        print(f"\n{'-' * 60}")
        print("📝 New session memory created.")
        print(
            f"✅ Tokens reduced: {self.current_context_window_tokens:,} → {approximate_summary_tokens:.0f} ({reduction:,} tokens saved, {pct:.0f}% reduction)"
        )
        print(f"⏱️ Compaction time: {elapsed:.2f}s (user waiting...)")
        print(f" Cache used: {getattr(response.usage, 'cache_read_input_tokens', 0) > 0}")
        print(f"{'-' * 60}")

        # Update token count to reflect compacted state
        self.current_context_window_tokens = approximate_summary_tokens
```

```
/root/.pyenv/versions/3.13.11/lib/python3.13/site-packages/coconut/compiler/util.py:403: FutureWarning: functools.partial will be a method descriptor in future Python versions; wrap it in staticmethod() if you want to preserve the old behavior
  grammar.streamline()
/root/.pyenv/versions/3.13.11/lib/python3.13/site-packages/coconut/compiler/util.py:457: FutureWarning: functools.partial will be a method descriptor in future Python versions; wrap it in staticmethod() if you want to preserve the old behavior
  result = add_action(grammar, unpack).parseWithTabs().transformString(text)
```

Below we simulate a conversation between an author and an LLM that helps write stories.

python

```
SYSTEM_PROMPT = """
You are a short story writer who helps authors develop their ideas into compelling narratives.

## What You Do

**Plot Development**
- Help authors work through story structure, pacing, and narrative arc
- Identify plot holes, inconsistencies, or missed opportunities
- Suggest ways to raise stakes, add tension, or deepen conflict
- Brainstorm twists, resolutions, and scene transitions

**Character Development**
- Develop backstories, motivations, and internal conflicts
- Ensure characters have distinct voices and consistent behavior
- Explore character relationships and how they drive the plot
- Help authors understand what their characters want vs. what they need

**Drafting**
- Write short stories or scenes based on the author's ideas and direction
- Match tone, genre conventions, and stylistic preferences
- Show rather than tell when bringing scenes to life
- Craft dialogue that reveals character and advances plot

## How You Work
- You are the lead writer. When you disagree with a creative choice, say so respectfully, but ultimately defer to what the author wants.
- DO NOT ask the user to provide more context or clarify their request. Assume you have enough information to proceed.
"""
```

python

```
session = TraditionalCompactingChatSession(system_message=SYSTEM_PROMPT)

# Simulated conversation
messages = [
    "I want to create a story about a young detective solving a mysterious case in a small town. Generate 3 well thought out plot ideas for me to consider.",
    "I don't like those ideas, can you think of one plot something more unique and unexpected?",
    "Ok I like it. Can you help me develop the main character's backstory and motivations?",
    "Can you draft a detailed outline for the story, breaking it down into chapters and key events?",
    "Can you draft me a first chapter based on the plot and character ideas we've discussed so far? Make it around 2,000 words.",
    "Can you draft a second chapter that builds on the first one, introducing a new twist in the mystery?",
]

print("Starting conversation...\n")

turn_count = 0

for _i, message in enumerate(messages, 1):
    turn_count += 1
    print(f"==============================================\nTurn {turn_count}:\n")
    response, usage = session.chat(message)
```

```
Starting conversation...

==============================================
Turn 1:

User: I want to create a story about a young detective solving a mysterious case in a small town. Generate 3 well thought out plot ideas for me to consider.

Assistant:
# Three Mystery Plot Ideas

## 1. **The Vanishing Choir**

**Setup:** In the sleepy town of Millbrook, the entire church choir—twelve people ranging from teenagers to retirees—disappears during their weekly Thursday night practice. The church was locked from the inside, their belongings left behind, including phones and car keys. No signs of struggle, no broken windows. Just an empty sanctuary and sheet music scattered across the floor.

**The Twist:** Your young detective discovers the choir members didn't disappear—they're hiding. Twenty years ago, they witnessed the town's beloved mayor commit a hit-and-run that killed a drifter. They stayed silent, bound by threats and their own complicity. Now the mayor is dying and has hired someone to ensure his secret dies with him. The choir staged their own disappearance to draw attention and finally confess, but the detective must figure out who they're hiding from before the killer finds them first.

**Why it works:** Small-town secrets, a ticking clock, and the moral complexity of people who aren't quite innocent or guilty. The locked-room mystery becomes a desperate act of exposure rather than concealment.

---

## 2. **The Memory Thief**

**Setup:** Elderly residents in Hartwood are reporting identical "robberies"—but nothing is actually stolen. Instead, they insist specific memories have been taken: a first kiss, a wedding day, the birth of a child. The police dismiss it as dementia until the detective notices a pattern: all victims visited the same new "reminiscence therapist" who uses experimental techniques to help seniors preserve their memories before they fade.
... (18 more lines)
Input=317, Prompt cached used= False | Output=852 | Messages=2
==============================================
Turn 2:

User: I don't like those ideas, can you think of one plot something more unique and unexpected?

Assistant:
# **The Cartographer's Grave**

**Setup:** Your young detective arrives in the mountain town of Ridgeway to investigate what seems like a prank: someone has been systematically correcting the town's street signs, storefront addresses, and property markers—changing them by just one or two numbers. The post office is going insane. Mail is being misdelivered. Emergency services are getting lost. But here's the thing: the "corrections" match a 150-year-old town map that was supposedly drawn incorrectly by a disgraced surveyor who was run out of town and buried in an unmarked grave.

**The Investigation:** The detective discovers the old surveyor wasn't wrong—he was *right*. The town founders deliberately falsified all records after his death, shifting every address, every property line, every boundary marker. Why? Because the real map would reveal that the town's most valuable land—now home to the founding families' estates, the town hall, the historic church—was actually purchased from a Native American family who were supposed to retain mineral rights and a percentage of all profits in perpetuity.

**The Twist:** The person "correcting" the signs isn't a descendant of the surveyor or the Native family. It's a twelve-year-old girl with terminal cancer who found the original map in her grandmother's attic. She's not seeking revenge or restitution—she just became obsessed with the idea that the whole town has been living a lie written into the ground itself. Before she dies, she wants the truth to physically exist in the world, even if no one acknowledges it. She's been sneaking out at night with a screwdriver and homemade signs.

**The Real Mystery:** The detective must decide what to do when they realize that "solving" the case—stopping the girl and restoring the false addresses—means choosing comfortable order over inconvenient truth. Meanwhile, members of the founding families are getting desperate to stop the corrections before anyone looks too closely at land deeds, and the girl's nightly trips are getting increasingly dangerous.

**Why it works:** It subverts the detective genre by making the "crime" an act of radical honesty. The mystery isn't whodunit—it's what truth is worth when it would destroy an entire community's foundation. The villain isn't the child or even really the founding families—it's the town itself, built on a literal lie. And your detective can't punch or outwit their way out of a moral knot.
Input=1,191, Prompt cached used= False | Output=544 | Messages=4
==============================================
Turn 3:

User: Ok I like it. Can you help me develop the main character's backstory and motivations?

Assistant:
# The Detective: Building Your Protagonist

## Core Identity

Let's call her **Nora Winters** (adjust the name as you prefer). She's 26 years old, which makes her young enough to be underestimated but old enough to have scars.

## Backstory

**The Personal Lie:** Nora grew up in a different small town where her father was the police chief—respected, beloved, the kind of man who coached Little League and knew everyone's name. When she was sixteen, she discovered he'd been planting evidence on suspects for years. Not major crimes—small-town stuff. A little weed here, stolen property there. Just enough to "help" cases along when he "knew" someone was guilty but couldn't prove it.

She confronted him. He told her the truth was "complicated," that sometimes you have to bend the rules to protect people, that the town trusted him to keep them safe and he delivered results. He made her complicit with his confession—if she exposed him, she'd destroy their family, his legacy, the town's faith in law enforcement.

She stayed silent. For two years, she carried it like a stone in her chest.

**The Breaking Point:** At eighteen, one of her father's frame jobs went wrong. A kid he planted drugs on—a 19-year-old with priors who was actually clean this time—panicked during arrest and ran. Got hit by a car. Died in the street.
... (50 more lines)
Input=1,758, Prompt cached used= False | Output=1,193 | Messages=6
==============================================
Turn 4:

User: Can you draft a detailed outline for the story, breaking it down into chapters and key events?

Assistant:
# **The Cartographer's Grave: Story Outline**

## **ACT ONE: The Map Doesn't Match the Territory**

### **Chapter 1: Arrival**
- Nora arrives in Ridgeway on a grey October morning, six-hour drive from the city
- Establishes the town: population 3,200, nestled in mountain valley, tourism from fall foliage and "historic charm"
- She meets Town Manager **Gerald Vance** (55, anxious, sweating through his shirt despite the cold) at town hall
- He explains the crisis: for three weeks, someone's been changing street signs and address numbers—small changes, but creating chaos
- Mail misdelivered, ambulance went to wrong house (patient survived, barely), legal documents being contested
- Shows her examples: the church changed from 847 Oak Street to 843 Oak, the post office from 1215 Main to 1219 Main
- Gerald thinks it's vandalism, wants her to catch whoever's doing it quickly and quietly
- **Key detail:** Nora notices all the "corrections" subtract or add small, specific numbers—not random

### **Chapter 2: The Town's Memory**
... (160 more lines)
Input=2,973, Prompt cached used= False | Output=3,500 | Messages=8
==============================================
Turn 5:

User: Can you draft me a first chapter based on the plot and character ideas we've discussed so far? Make it around 2,000 words.

Assistant:
# **Chapter 1: Arrival**

The town of Ridgeway materialized from the fog like a photograph developing in reverse—sharp edges first, then the softer details filling in around them. Church steeple. Water tower. The downtown strip with its brick facades and hand-painted signs promising antiques, locally roasted coffee, genuine mountain crafts. Nora Winters took it all in through rain-spattered windshield glass, her Honda's wipers beating a rhythm that had become hypnotic somewhere around hour five of the drive.

Small towns always looked the same in October. Like they were apologizing for something.

She followed Main Street through the heart of downtown—two blocks of calculated charm before the road narrowed and climbed into the residential neighborhoods climbing the mountain's flank. The GPS on her phone had lost signal fifteen minutes ago, but she didn't need it. Town hall would be near the center, probably the biggest building on the main drag, probably with a flag and that particular kind of municipal architecture that tried too hard to look historic.

She was right on all counts.

Ridgeway Town Hall occupied a corner lot with the self-importance of a building that had watched the world change and declined to participate. Red brick, white columns, a bronze plaque declaring it built in 1889 and placed on the National Register in 1976. The flag snapped in the wind. Rain pooled in the uneven sidewalk leading to the entrance.

Nora parked on the street, grabbed her messenger bag, and made the dash to the covered entrance. The door was heavier than it looked—solid oak, brass hardware—and opened into the particular smell of old public buildings: lemon polish, ancient radiator heat, and paper slowly yellowing in filing cabinets.

A woman at the reception desk looked up from her computer. Sixty-something, reading glasses on a beaded chain, cardigan against the over-aggressive heating system. Her smile was professional and tired in equal measure.
... (118 more lines)
Input=6,509, Prompt cached used= False | Output=3,073 | Messages=10
==============================================
Turn 6:

User: Can you draft a second chapter that builds on the first one, introducing a new twist in the mystery?

Assistant:
# **Chapter 2: The Town's Memory**

Nora woke at six to the sound of rain that had never really stopped, just paused to gather its strength. She'd fallen asleep at the small desk by the window, tablet still glowing with Gerald's documentation, her neck complaining about the angle she'd maintained for however many hours.

The numbers were still dancing behind her eyes. She'd spent half the night building spreadsheets, mapping the changes, looking for the pattern Gerald had sensed but couldn't articulate. And she'd found it—or the beginning of it. Every changed address was in the older part of town, pre-1900 construction. Every change was small but specific: sometimes adding four, sometimes subtracting two, once adding seven. Not random. Definitely not random.

She showered, changed into clean jeans and a sweater, and followed the smell of coffee downstairs.

The dining room was small and warmly lit, with four tables covered in white cloth. An older man sat alone by the window reading a newspaper—actual paper, folded precisely. A younger couple occupied another table, speaking in low voices over their phones. Tourists, Nora guessed, based on the hiking boots and Patagonia fleeces.

A sideboard held coffee, tea, juice, and a modest breakfast spread. Nora filled a mug and took a table in the corner where she could see the room and the street beyond.

Dolores appeared from what must have been the kitchen, carrying a plate of scrambled eggs and toast. She set it in front of the man with the newspaper without being asked, received a grunt of acknowledgment, and crossed to Nora's table.

"You look like you didn't sleep much."
... (171 more lines)
Input=9,606, Prompt cached used= True | Output=3,241 | Messages=12
```

This is a long conversation with several turns. You'll notice a few things here:

Prompt caching: You'll notice here that the input tokens eventually grew to a point where prompt caching was used (turn 6). This helps reduce costs and speed as these conversations grow!

On the next turn, we are going to hit our 10K context window limit, which triggers compaction:

python

```
response, usage = session.chat("Propose a title for the book")
```

```
🧹 Context window at 12847 tokens. Limit exceeded, compacting session memory...

------------------------------------------------------------
📝 New session memory created.
✅ Tokens reduced: 12,847 → 1526 (11,321 tokens saved, 88% reduction)
⏱️ Compaction time: 41.42s (user waiting...)
 Cache used: True
------------------------------------------------------------

User: Propose a title for the book

Assistant:
Based on the story's core themes and imagery, here are my title proposals:

## Primary Recommendation

**The Cartographer's Daughter**

This works on multiple levels:
- Emma is metaphorically Amos Frost's "daughter" in mission—inheriting and completing his work
- Patricia (literal descendant of Frost's assistant) becomes Emma's accomplice
- Evokes the weight of inheritance, legacy, and what we pass down
- "Cartographer" immediately signals the map/truth theme
- Has literary gravitas appropriate for the story's tone

## Alternates

... (20 more lines)
Input=1,813, Prompt cached used= False | Output=328 | Messages=3
```

You'll notice here that it took **over 40 seconds** for the agent to compact the conversation. Because we used traditional compaction, the user would be waiting on Claude to compact the conversation, which is not an ideal user experience.

Below you can see the result of the compaction. It captures the key elements of conversation in less than 2K tokens.

python

```
print(session.summary)
```

```
## User Intent
Create short story about young detective solving mysterious case in small town. Initially requested "3 well thought out plot ideas." Rejected first batch as not unique enough, requested "something more unique and unexpected." Accepted "The Cartographer's Grave" concept. Then requested: character backstory/motivations development, detailed chapter outline, and drafted chapters.

## Completed Work

**Approved Plot: "The Cartographer's Grave"**
- Ridgeway (pop. 3,200, mountain town) experiencing systematic address changes
- 12-year-old Emma Lancaster (terminal brain cancer) changing signs at night to match 1874 surveyor Amos Frost's original map
- Frost was "disgraced," replaced by Marcus Bellamy (founding family) in 1875 re-survey
- Real conspiracy: Bellamy survey deliberately shifted property lines 200-400 feet east to steal valuable land from Pequawket family (Native American), who had mineral rights + 15% revenue contract
- Emma found Frost's materials in grandmother's attic (Patricia Lancaster, granddaughter of Samuel Lancaster—Frost's assistant who bought his effects)
- Emma's motivation: not justice, but existential—wants to matter, leave truth behind before dying
- Resolution: Town acknowledges historical fraud via memorial/fund, addresses stay changed, Emma dies knowing truth survived

**Main Character: Nora Winters**
- Age 26, private investigator for rural cases firm
- Backstory: Father was police chief who planted evidence for years. At 16 she discovered it, stayed silent 2 years. At 18, a framed kid died fleeing arrest. She exposed father to state police. Father forced into retirement but kept reputation. Family estranged, won't speak to her.
- Motivation: Prove truth always matters, atone for 2 years of silence
- Fatal flaw: Prioritizes truth over mercy, can be self-righteous
- Arc: Must learn truth and justice aren't always same thing

**Supporting Characters**
- Gerald Vance (55, town manager, anxious)
- Dolores Chen (68, Ridgeway Inn owner, knows everything)
- Ruth Bellamy (72, historical society president, descendant of Marcus Bellamy)
- Sheriff Tom Whitlock (50, third-generation sheriff, dismissive)
- Emma Lancaster (12, dying of brain cancer, changing signs)
- Patricia Lancaster (64, Emma's grandmother, retired town clerk, Samuel Lancaster's descendant)
- James Pequawket (58, teacher, lives two towns over, descendant)
- Samuel Lancaster (Amos Frost's 1874 assistant, bought Frost's effects after death)
- Amos Frost (surveyor, accurate 1874 map, died 1889 in sanitarium, unmarked grave)

**16-Chapter Outline with Epilogue Created**
- Act 1 (Ch 1-4): Nora arrives, discovers pattern, identifies Emma via dropped notebook
- Act 2 (Ch 5-9): Confronts Emma, discovers Frost's journal/map at Lancaster house, uncovers full conspiracy
- Act 3 (Ch 10-15): Town pressures Nora, founding families threaten charges against Emma, Nora proposes compromise (memorial + fund vs. property transfers), Emma dies December 3rd
- Epilogue (Ch 16): Six months later, Nora receives Emma's notebook showing new project mapping unmarked graves

**Chapter 1 Drafted (~2000 words)**
- Nora arrives Ridgeway in rain, meets Gerald Vance at town hall
- Gerald explains crisis: 37 locations, professional signs, started October 2nd, systematic pattern
- Key detail: Changes are small (1-5 numbers) but precise, affecting only pre-1900 buildings
- Nora checks into Ridgeway Inn, meets Dolores Chen
- Dolores reveals her address changed October 3rd: 843 to 847 Oak Street, left new sign up to "adapt"
- Dolores warns: "Be careful asking questions here. Not everyone appreciates having their complications examined."

**Chapter 2 Drafted**
- Nora analyzes data overnight, identifies pattern: all changes in pre-1900 areas
- Breakfast at inn, confronted by Howard Marsh (70s, opposed to investigation)
- Visits library, meets Jess (librarian, 30, supportive)
- Discovers in basement archives: changed addresses match 1875 town plat exactly
- Jess reveals history: Amos Frost surveyed 1874, deemed "inaccurate," dismissed. Marcus Bellamy (Ruth's great-great-grandfather) re-surveyed 1875 (official record). Frost's survey "destroyed years ago."
- Text from Jess's partner Sarah: Frost died 1889 in sanitarium, pauper's grave. Effects purchased by Samuel Lancaster at 1847 Oak Street.
- **Chapter ends with revelation**: 1847 Oak = current "corrected" address of Ridgeway Inn (officially 843). Frost's materials likely still at inn. "The question was who in that building knew they existed, and why they'd decided—after more than a century of silence—that the truth needed to be rewritten into the town's streets."

## Errors & Corrections
User explicitly rejected first 3 plot ideas: "The Vanishing Choir," "The Memory Thief," "The Lighthouse Keeper's Daughter"—deemed not unique/unexpected enough.

## Active Work
Chapter 2 completed. Story ready to continue with Chapter 3, which per outline should cover "The Pattern" where Nora stakes out locations and first spots Emma changing a sign.

## Pending Tasks
Draft chapters 3-16 and epilogue per approved outline.

## Key References
**Critical addresses**: 843 Oak Street (official) / 847 Oak Street (corrected) = Ridgeway Inn location, Samuel Lancaster's 1874 address
**Timeline**: October 2nd changes start, story current timeframe October, Emma dies December 3rd, epilogue six months later
**The fraud mechanics**: Bellamy survey shifted all property lines 200-400 feet east, making Pequawket parcel appear worthless hillside while valuable land (now Bellamy estate, town hall, church) became "legitimately" owned by founding families
**Pequawket contract terms**: Mineral rights in perpetuity + 15% of all property values/business revenues from specified parcel
```

## Instant Compaction

With **Instant compaction** the session memory is PROACTIVELY generated once a soft token threshold is reached.

Once the user triggers a compaction or a hard limit is reached, the summary is already available, so the user doesn't need to wait.

Result: Instant compaction, no waiting.

SESSION MEMORY COMPACTION (instant)

```
────────────────────────────────────
Turn 1 → Turn 2 → ... → Turn K → Turn K+1 → ... → Turn N → ..  → CONTEXT FULL!
                            │                         │            │
                (soft token threshold met:        (update          │
               initialize session memory)          trigger)        │
                            │                                      │
                            │                         │            │
                            ▼                         ▼            │
                       ┌────────┐                ┌────────┐        │
                       │ Create │                │ Update │        │
                       │ memory │ (background)   │ memory │        │
                       └────────┘                └────────┘        │
                            │                         │            │
                            ▼                         ▼            ▼
                     📝 session-memory.md ──────────────────► INSTANT SWAP!
                       (continuously updated)
```

**Update triggers:** The first summary is generated after the initial soft token limit. Updates can be triggered after every subsequent turn, or at periodically at natural breakpoints intervals (e.g. every ~10k tokens or 3+ tool calls).

This `InstantCompactingChatSession` class uses **threading** for background execution:

1. **`threading.Thread`** - runs memory updates in background without blocking
2. **Thread-safe state** - uses `threading.Lock` to safely update shared memory
3. **Daemon threads** - background work doesn't prevent program exit
4. **Instant compaction** - when context is full, just swap in the pre-built memory

python

```
import threading
import time

class InstantCompactingChatSession:
    """
    Maintains session memory via incremental background updates.

    Key insight: By updating memory in the background after each turn,
    the summary is already ready when compaction is needed - instant swap!
    """

    def __init__(
        self,
        system_message="You are a helpful assistant",
        context_limit: int = 12000,
        min_tokens_to_init: int = 7500,
        min_tokens_between_updates: int = 2000,
    ):
        # Thresholds
        self.context_limit = context_limit  # the point at which the conversation is compacted so it does not exceed model limits
        self.min_tokens_to_init = min_tokens_to_init  # tokens needed to trigger initial memory creation; note this happens PROACTIVELY in background unlike traditional compaction
        self.min_tokens_between_updates = min_tokens_between_updates  # tokens needed to trigger memory update. only comes into play after initial memory is created and additional compaction (memory update) is needed after that

        # Conversation state
        self.system_message = system_message
        self.messages = []
        self.current_context_window_tokens = 0

        # Session memory state
        self.session_memory = None  # this is the compacted conversation in session memory; for the demo we are storing this in memory, but in production you would write to session_memory.md file
        self.last_summarized_index = (
            0  # The index of the last message included in the session memory
        )
        self.tokens_at_last_update = 0  # To track tokens at last memory update and see if enough new tokens have been added to trigger another update

        # Background update tracking
        self._update_thread: threading.Thread | None = None
        self.last_update_time = None
        self._lock = threading.Lock()

    def chat(self, user_message: str) -> tuple[str, anthropic.types.Usage, str | None]:
        """Process a chat turn with background session memory updates."""

        if self.current_context_window_tokens + estimate_tokens(user_message) >= self.context_limit:
            self.compact()  # note that when this is triggered, the compaction has already been created and is just swapped in instantly

        self.messages.append({"role": "user", "content": user_message})

        response = client.messages.create(
            model=MODEL,
            max_tokens=3500,
            system=self.system_message,
            messages=add_cache_control(self.messages),
        )

        assistant_message = response.content[0].text
        self.messages.append({"role": "assistant", "content": assistant_message})

        # Calculate token usage including cache
        cache_read = getattr(response.usage, "cache_read_input_tokens", 0) or 0
        total_input = response.usage.input_tokens + cache_read

        # Update context window tokens (includes cached tokens since they still count toward context)
        self.current_context_window_tokens = total_input + response.usage.output_tokens

        # KEY DIFFERENCE: Trigger background memory update if needed proactively, before compaction is needed
        background_status = None
        if self._should_init_memory() or self._should_update_memory():
            self._trigger_background_update()
            background_status = "initializing" if self.session_memory is None else "updating"

        # Return usage info with cache stats
        return assistant_message, response.usage, background_status

    # Helper methods to determine when to init session memory
    def _should_init_memory(self) -> bool:
        return (
            self.session_memory is None
            and self.current_context_window_tokens >= self.min_tokens_to_init
        )

    # Helper method to determine if memory should be updated
    def _should_update_memory(self) -> bool:
        if self.session_memory is None:
            return False
        tokens_since = self.current_context_window_tokens - self.tokens_at_last_update
        return tokens_since >= self.min_tokens_between_updates

    # Methods to create initial session memory
    def _create_session_memory(self, messages: list[dict]) -> str:
        """Generate initial session memory from messages."""
        # Put compaction instructions in user message to share cache with main chat
        compaction_messages = [{"role": "user", "content": SESSION_MEMORY_PROMPT}]
        response = client.messages.create(
            model=MODEL,
            max_tokens=5000,
            system=self.system_message,  # Same as main chat for cache sharing
            messages=add_cache_control(messages) + compaction_messages,
        )
        summary, _ = remove_thinking_blocks(
            response.content[0].text
        )  # clean up any <think> blocks because they are not needed in the session memory
        print(
            f"   [Background] Initial session memory created. Cache hit={getattr(response.usage, 'cache_read_input_tokens', 0) > 0}"
        )
        return summary

    def _update_session_memory(self, new_messages: list[dict]) -> str:
        """Update existing session memory with new messages. In practice, you may want to do this via file edit rather than full re-generation. But for demo purposes we do full regeneration here."""
        # Put compaction instructions in user message to share cache with main chat
        compaction_update_messages = [
            {
                "role": "user",
                "content": SESSION_MEMORY_PROMPT
                + f"""There is an existing session memory: {self.session_memory}. Return the entire session memory with updates to reflect new messages.""",
            }
        ]
        response = client.messages.create(
            model=MODEL,
            max_tokens=5000,
            system=self.system_message,
            messages=new_messages
            + compaction_update_messages,  # you may want to use prompt caching instead, in which case you'd use add_cache_control(self.messages) here
        )
        updated_summary, _ = remove_thinking_blocks(
            response.content[0].text
        )  # clean up any <think> blocks because they are not needed in the session memory
        print("   [Background] Session memory updated.")
        return updated_summary

    # Background memory update methods
    def _background_memory_update(
        self, messages_snapshot: list[dict], snapshot_index: int, current_tokens: int
    ) -> None:
        """Run session memory update in a background thread."""
        try:
            with self._lock:
                current_session_memory = self.session_memory
                last_index = self.last_summarized_index

            if current_session_memory is None:
                new_memory = self._create_session_memory(messages_snapshot)
            else:
                # Get new messages since last summary
                new_messages = messages_snapshot[last_index:]
                if not new_messages:
                    return
                new_memory = self._update_session_memory(new_messages)

            # Update state (thread-safe)
            with self._lock:
                self.session_memory = new_memory
                self.last_summarized_index = snapshot_index
                self.tokens_at_last_update = current_tokens
                self.last_update_time = time.time()

        except Exception as e:
            print(f"   [Background] Error updating memory: {e}")

    # This makes sure only one background update runs at a time. If one is already running, we skip starting another. If not, we start a new thread to do the update.
    def _trigger_background_update(self):
        """Trigger a background session memory update."""
        if self._update_thread is not None and self._update_thread.is_alive():
            return

        messages_snapshot = self.messages.copy()
        snapshot_index = len(messages_snapshot)
        current_tokens = self.current_context_window_tokens

        self._update_thread = threading.Thread(
            target=self._background_memory_update,
            args=(messages_snapshot, snapshot_index, current_tokens),
            daemon=True,
        )
        self._update_thread.start()

    # Function to compact
    def compact(self) -> None:
        """INSTANT compaction using pre-built session memory."""
        prev_msg_count = len(self.messages)

        # Ensure session memory is ready. Shouldn't be an issue normally, but here for safety.
        if self.session_memory is None:
            if self._update_thread is not None and self._update_thread.is_alive():
                print("   ⏳ Waiting for background memory update...")
                self._update_thread.join(timeout=30.0)

            if self.session_memory is None:
                print("   ⚠️  No pre-built memory, creating synchronously...")
                start = time.perf_counter()
                self.session_memory = self._create_session_memory(self.messages)
                elapsed = time.perf_counter() - start
                print(f"   ⏱️  Took {elapsed:.2f}s (but should be instant normally!)")
                self.last_summarized_index = len(self.messages)

        with self._lock:
            unsummarized = self.messages[self.last_summarized_index :]
            summary_message = [
                {
                    "role": "user",
                    "content": f"""This session is being continued from a previous conversation. Here is the session memory: {self.session_memory}.Continue from where we left off.""",
                }
            ]
            self.messages = summary_message + unsummarized
            self.last_summarized_index = 1

            print(f"\n{'=' * 60}")
            print(f"⚡ INSTANT COMPACTION! Messages: {prev_msg_count} → {len(self.messages)}")
            print("   Session memory was pre-built (no wait time!)")
            print(f"{'=' * 60}")
```

```
/root/.pyenv/versions/3.13.11/lib/python3.13/site-packages/coconut/compiler/util.py:403: FutureWarning: functools.partial will be a method descriptor in future Python versions; wrap it in staticmethod() if you want to preserve the old behavior
  grammar.streamline()
/root/.pyenv/versions/3.13.11/lib/python3.13/site-packages/coconut/compiler/util.py:457: FutureWarning: functools.partial will be a method descriptor in future Python versions; wrap it in staticmethod() if you want to preserve the old behavior
  result = add_action(grammar, unpack).parseWithTabs().transformString(text)
```

### Example use of Instant Compaction

python

```
# Low thresholds for demo - in production you'd use higher values
session = InstantCompactingChatSession(
    system_message=SYSTEM_PROMPT,
)

messages = [
    "I want to create a story about a young detective solving a mysterious case in a small town. Generate 3 well thought out plot ideas for me to consider.",
    "I don't like those ideas, can you think of one plot something more unique and unexpected?",
    "Ok I like it. Can you help me develop the main character's backstory and motivations?",
    "Can you draft a detailed outline for the story, breaking it down into chapters and key events?",
    "Can you draft me a first chapter based on the plot and character ideas we've discussed so far? Make it around 2,000 words.",
    "Can you draft a second chapter that builds on the first one?",
]
print("Starting conversation with instant compacting chat session...\n")

turn_count = 0
for message in messages:
    response, usage, background_status = session.chat(message)
    turn_count += 1

    # Calculate cache stats
    cache_read = getattr(usage, "cache_read_input_tokens", 0) or 0
    cache_created = getattr(usage, "cache_creation_input_tokens", 0) or 0
    total_input = usage.input_tokens + cache_read

    print(f"{'=' * 60}")
    print(f"Turn {turn_count}:")
    print(f"\nUser: {message}")
    print(f"\nAssistant: \n{truncate_response(response, max_lines=3)}")
    print("\nToken Usage:")
    print(f"  Input: {total_input:,} (new: {usage.input_tokens:,}, cached: {cache_read:,})")
    print(f"  Output: {usage.output_tokens:,}")
    print(
        f"  Messages: {len(session.messages)} | Memory: {'ready' if session.session_memory else 'not yet'}"
    )

    if cache_read > 0:
        cache_pct = (cache_read / total_input) * 100
        print(f"  ✓ Cache hit! {cache_pct:.0f}% of input from cache")

    if background_status:
        print(f"\n  [Background] Proactively {background_status} session memory...")
        print(f"  Context window: {session.current_context_window_tokens:,} tokens")

    print()
```

```
Starting conversation with instant compacting chat session...

============================================================
Turn 1:

User: I want to create a story about a young detective solving a mysterious case in a small town. Generate 3 well thought out plot ideas for me to consider.

Assistant:
# Three Mystery Plot Ideas

## 1. **The Vanishing Choir**
... (36 more lines)

Token Usage:
  Input: 317 (new: 317, cached: 0)
  Output: 902
  Messages: 2 | Memory: not yet

============================================================
Turn 2:

User: I don't like those ideas, can you think of one plot something more unique and unexpected?

Assistant:
# **The Forgetting House**

**Setup:** Your young detective arrives in Ember Falls to investigate a string of burglaries—except the victims don't realize they've been robbed until weeks later. A woman discovers her wedding ring gone and insists she lost it yesterday, but security footage shows she hasn't worn it in a month. A man reports his grandfather's watch stolen, then his sister shows him photos proving he sold it himself at a pawn shop—which he has no memory of doing.
... (16 more lines)

Token Usage:
  Input: 1,241 (new: 1,241, cached: 0)
  Output: 592
  Messages: 4 | Memory: not yet

============================================================
Turn 3:

User: Ok I like it. Can you help me develop the main character's backstory and motivations?

Assistant:
# Your Detective: Building From The Inside Out

## Core Identity
... (79 more lines)

Token Usage:
  Input: 1,856 (new: 1,856, cached: 0)
  Output: 1,329
  Messages: 6 | Memory: not yet

============================================================
Turn 4:

User: Can you draft a detailed outline for the story, breaking it down into chapters and key events?

Assistant:
# **The Forgetting House: Chapter Outline**

---
... (272 more lines)

Token Usage:
  Input: 3,207 (new: 3,207, cached: 0)
  Output: 3,500
  Messages: 8 | Memory: not yet

============================================================
Turn 5:

User: Can you draft me a first chapter based on the plot and character ideas we've discussed so far? Make it around 2,000 words.

Assistant:
# **Chapter One: The Impossible Theft**

The apartment smelled like burnt coffee and old paper.
... (196 more lines)

Token Usage:
  Input: 6,743 (new: 6,743, cached: 0)
  Output: 3,155
  Messages: 10 | Memory: not yet

  [Background] Proactively initializing session memory...
  Context window: 9,898 tokens

   [Background] Initial session memory created. Cache hit=True
============================================================
Turn 6:

User: Can you draft a second chapter that builds on the first one?

Assistant:
# **Chapter Two: Rosemont Manor**

The house appeared through the trees like something from a postcard.
... (190 more lines)

Token Usage:
  Input: 9,914 (new: 5,818, cached: 4,096)
  Output: 3,500
  Messages: 12 | Memory: ready
  ✓ Cache hit! 41% of input from cache

  [Background] Proactively updating session memory...
  Context window: 13,414 tokens
```

python

```
message = "What did we just talk about? Give me one sentence"
response, usage, background_status = session.chat(message)

# Calculate cache stats
cache_read = getattr(usage, "cache_read_input_tokens", 0) or 0
total_input = usage.input_tokens + cache_read

print(f"\nUser: {message}")
print(f"\nAssistant: \n{truncate_response(response, max_lines=3)}")
print("\nToken Usage:")
print(f"  Input: {total_input:,} (new: {usage.input_tokens:,}, cached: {cache_read:,})")
print(f"  Output: {usage.output_tokens:,}")
print(
    f"  Messages: {len(session.messages)} | Memory: {'ready' if session.session_memory else 'not yet'}"
)

if cache_read > 0:
    cache_pct = (cache_read / total_input) * 100
    print(f"  ✓ Cache hit! {cache_pct:.0f}% of input from cache")
```

```
============================================================
⚡ INSTANT COMPACTION! Messages: 12 → 3
   Session memory was pre-built (no wait time!)
============================================================

User: What did we just talk about? Give me one sentence

Assistant:
I drafted Chapter 2 where Casey arrives at Rosemont Manor, interviews Iris (who deflects questions about her past and shows moments of disorientation), and realizes through comparing photos that Iris Hale is definitely their missing grandmother Iris Whitmore.

Token Usage:
  Input: 5,490 (new: 5,490, cached: 0)
  Output: 60
  Messages: 5 | Memory: ready
```

You'll notice here that once we hit the context limit, the session memory was instantaly swapped in, meaning the user had zero waiting time for a response!

## Advanced: Understanding Prompt Caching

The background updates can be made **~10x cheaper** by using prompt caching. The trick:

1. Pass the **full conversation** to the background summarizer
2. Add `cache_control` markers so subsequent requests hit the cache
3. Only the new "summarize this" instruction is billed at full price

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    PROMPT CACHING FOR LONG CONVERSATIONS                        │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  WITHOUT CACHING: Pay full price for entire context every turn                 │
│  ════════════════════════════════════════════════════════════                   │
│                                                                                 │
│  Turn 1:  [System][User1][Asst1]                         →  500 tokens  @ $3/M │
│  Turn 2:  [System][User1][Asst1][User2][Asst2]           → 1500 tokens  @ $3/M │
│  Turn 3:  [System][User1][Asst1][User2][Asst2][User3]... → 3000 tokens  @ $3/M │
│  Turn 4:  [System][User1][Asst1][User2][Asst2][User3]... → 5000 tokens  @ $3/M │
│           ─────────────────────────────────────────────                         │
│                                              Total: 10,000 tokens = $0.030      │
│                                                                                 │
│                                                                                 │
│  WITH CACHING: Pay full price once, then 90% discount on prefix                │
│  ═══════════════════════════════════════════════════════════════                │
│                                                                                 │
│  Turn 1:  [System][User1][Asst1]◆                        →  500 tokens  @ $3/M │
│                                ▲                            (cache created)    │
│                          cache breakpoint                                       │
│                                                                                 │
│  Turn 2:  [System][User1][Asst1][User2][Asst2]◆                                │
│           ╰─────── cached ──────╯                                              │
│                500 @ $0.30/M + 1000 new @ $3/M  =  $0.0032                     │
│                                                                                 │
│  Turn 3:  [System][User1][Asst1][User2][Asst2][User3][Asst3]◆                  │
│           ╰──────────── cached ─────────────╯                                  │
│               1500 @ $0.30/M + 1500 new @ $3/M  =  $0.0050                     │
│                                                                                 │
│  Turn 4:  [System][User1][Asst1][User2][Asst2][User3][Asst3][User4][Asst4]◆    │
│           ╰───────────────────── cached ─────────────────────╯                 │
│                     3000 @ $0.30/M + 2000 new @ $3/M  =  $0.0069               │
│           ─────────────────────────────────────────────                         │
│                                              Total: $0.0166  (45% savings)     │
│                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  COMPACTION + CACHING: Double benefit                                           │
│  ════════════════════════════════════                                           │
│                                                                                 │
│    Main Chat                      Background Summarizer                         │
│    ─────────                      ─────────────────────                         │
│                                                                                 │
│  [Conversation grows...]          [Same conversation prefix]◆ + [Summarize!]   │
│         │                                    │                                  │
│         │                         Cache hit! Only pays for                      │
│         │                         the summarization prompt                      │
│         │                                    │                                  │
│         ▼                                    ▼                                  │
│  Context limit reached  ──────►  Session memory ready instantly                │
│                                  (built cheaply in background)                  │
│                                                                                 │
│  ┌──────────────────────────────────────────────────────────────────────────┐  │
│  │  Key insight: The background summarizer reuses the same conversation     │  │
│  │  prefix that was just sent to the main chat - automatic cache hit!       │  │
│  └──────────────────────────────────────────────────────────────────────────┘  │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

◆ = cache_control breakpoint (cache everything before this point)
```

### Why this matters for compaction

| Scenario | Cost per background update | Notes |
| --- | --- | --- |
| No caching | Full input cost | 5,000 tokens × 3/M=3/M = 3/M=0.015 |
| With caching | ~10% of input cost | 500 new + 4,500 cached = $0.003 |
| **Savings** | **~80%** | Compounds over many updates |

The longer the conversation, the bigger the savings—exactly when you need compaction most!

### How the Caching Works

The key is in `_add_cache_control()` and `_create_session_memory_cached()`:

```
# 1. Mark the last conversation message with cache_control
{
    "role": "user",
    "content": [{
        "type": "text",
        "text": msg["content"],
        "cache_control": {"type": "ephemeral"}  # <-- This creates a cache breakpoint
    }]
}

# 2. Also mark the system prompt
system=[{
    "type": "text",
    "text": "You are a session memory agent...",
    "cache_control": {"type": "ephemeral"}
}]
```

**Why this works:**

* The first background update creates a cache entry for `[System + Messages]`
* Subsequent updates with the same message prefix get **cache hits**
* Only the new summarization instruction is billed at full price
* Cache entries have a 5-minute TTL, so rapid updates benefit most

**Cost math:**

* Without caching: 5,000 tokens × 3.00/1M=3.00/1M = 3.00/1M=0.015 per update
* With caching: 500 new tokens × 3.00/1M+4,500cached×3.00/1M + 4,500 cached × 3.00/1M+4,500cached×0.30/1M = $0.00285
* **Savings: ~80%** on background summarization costs

## Conclusion

In this cookbook, you learned how to manage long-running Claude conversations through session memory compaction.

### What We Covered

✅ **Effective compaction prompts** - Structure your session memory to preserve user intent, completed work, errors, active work, and key references while discarding filler

✅ **Instant compaction** - Use background threading to proactively build session memory, eliminating user wait time when context limits are reached

✅ **Prompt caching for cost savings** - Reduce background update costs by ~80% by reusing the conversation prefix cache

✅ **Traditional vs. instant patterns** - Understand when to use each approach based on your application needs

### Key Takeaways

1. **Weight recency heavily** - The end of a conversation is the active working context
2. **Preserve user corrections verbatim** - Prevents the model from reverting to old behaviors
3. **Build memory proactively** - Don't wait for context limits; start background updates early
4. **Leverage prompt caching** - Background summarization can share cache with the main conversation

### Next Steps

* **For agentic workflows**: See [Automatic Context Compaction](https://github.com/anthropics/claude-cookbooks/blob/main/misc/../tool_use/automatic-context-compaction.ipynb) for SDK-based automatic compaction with tool use
* **For production**: Consider persisting session memory to disk rather than keeping it in memory
* **For optimization**: Experiment with update frequency thresholds to balance cost vs. freshness
