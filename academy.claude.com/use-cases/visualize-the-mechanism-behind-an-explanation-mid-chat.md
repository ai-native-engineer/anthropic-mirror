<!-- source: https://academy.claude.com/use-cases/visualize-the-mechanism-behind-an-explanation-mid-chat -->

Loading

## 1. Describe the task

Claude can build a visual as part of its answer — a diagram, a chart, something interactive — built for the question you asked and woven into the explanation around it. You drag things, click into what's still unclear, and Claude builds the next one in response. It triggers on its own when a visual would help; you can also ask for one directly. Rather than a full artifact, the diagram streams in where the text would have been, and the conversation keeps going.

Here a student knows a planet speeds up near the sun but not why. Claude builds an animated trade-off they can run themselves, with buttons to go deeper into whatever's still fuzzy.

I'm learning orbital mechanics and I understand that the planet speeds up when it's close to the sun and slows down when it's far. But I don't understand *why* that trade-off exists. Why can't it just go fast the whole time? Help me understand with a well crafted, interactive, dynamic visualization.



Open in Claude

## 2. Give Claude context

No files needed — the prompt carries it. Stating what you already know tells Claude where not to start; naming what isn't clicking tells it what to build around.

### Required context

Nothing to upload.

## 3. What Claude creates

Claude builds three linked views of the same mechanism tied to one slider — the trade-off runs in all three at once. The slider hands you the variable. Drag it and the answer to "why can't it just go fast" shows itself: the energy bar pins the total, so speed and distance trade against each other.

![Claude's response with an interactive orbit visualization: an elliptical orbit showing equal-area sectors at aphelion and perihelion, a Kepler's second law note, gravity well and energy budget panels, an orbit eccentricity slider, and buttons for angular momentum, escape velocity, and changing orbits](https://academy.claude.com/assets/v1/orbital-tradeoff-o007te4a.png)

## 4. Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Click a button in the visual to go deeper

The buttons at the bottom of the visual send follow-up prompts — click one and a second visual streams in below, built around that narrower question. The first stays; you scroll between them.

Explain angular momentum conservation in orbits — why does the planet sweep equal areas in equal times?



Open in Claude

### Ask Claude to redraw it with one thing changed

Name a change and Claude redraws — same three panels, different input, so you see what holds and what shifts.

Would this same speed-distance trade-off work for a comet with a really eccentric orbit? Rebuild the same visual with that orbit instead and show me what changes.



Open in Claude

### Ask Claude to turn the explainer into a quiz

Claude builds a quiz using the same three panels — it asks what happens at different points in the orbit, you answer, it tells you what you got right.

Quiz me on what this animation shows. Ask me what happens at different points in the orbit and tell me if I've got the trade-off right.



Open in Claude

## 5. Tricks, tips, and troubleshooting

### How you word your prompt shapes what you get

Words like "interactive," "let me adjust," or "something I can play with" steer Claude toward sliders and controls; a plainer description tends to get a static image. The prompt above uses "interactive, dynamic visualization" — that phrasing is what gets a mechanism you can run. If what comes back is cramped, asking Claude to clean up the formatting usually fixes it next turn.

### Tell Claude what you already understand

Mentioning what you already understand tells Claude what to skip — more of the visual ends up on the part that's unclear. One line does it: the student above already knows the planet speeds up; what they want is the *why*, and that's what gets animated.

### What to do with the visual next

Hover over the visual for options. Copy as image drops it into your notes next to the concept. Save as Artifact keeps the interactive version if you'd reopen the sliders later. Or ask Claude to write up what clicked — you get a paragraph to edit into your notes.

## 6. Ready to try for yourself?

Try it on whatever concept isn't clicking — say where you're stuck and let Claude build something to watch. Hover over what Claude drew for options: copy an image for your notes, or save it as an Artifact if it's worth keeping past the conversation.

I'm learning orbital mechanics and I understand that the planet speeds up when it's close to the sun and slows down when it's far. But I don't understand why that trade-off exists. Why can't it just go fast the whole time? Help me understand with a well crafted, interactive, dynamic visualization.

Try in Claude
