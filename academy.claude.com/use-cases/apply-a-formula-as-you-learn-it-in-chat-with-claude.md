<!-- source: https://academy.claude.com/use-cases/apply-a-formula-as-you-learn-it-in-chat-with-claude -->

Loading

## 1. Describe the task

There's a gap between doing a formula and having a feel for it. You can compute correctly and still not know what one weird value will do to the answer — that sense comes from handling: moving a point, watching what changes. Claude can build a blank canvas right in the conversation. You place the points, drag any one, watch the fit respond. Quick enough to do mid-study, and when it clicks you move on.

Here a stats student can do the calculation but doesn't have a sense of why a single bad point moves the whole fit. Claude hands them a scatter to build from scratch, with toggles for residuals and influence so the distinction shows up by dragging.

I'm learning linear regression and I can do the formula but I don't get it. Can you give me something where I can mess with the data points myself and watch what happens to the line? I want to actually feel why one weird point can throw the whole thing off. Can you help me visualize?



Open in Claude

## 2. Give Claude context

No files. The prompt's verbs do the work — "mess with," "watch what happens," "feel why." That language is what gets you a blank canvas to fill rather than a pre-loaded demonstration to watch.

### Required context

Nothing to upload.

## 3. What Claude creates

Claude hands you an empty canvas. You click to place points, drag to break things, watch the line respond. Placing the outlier yourself and watching the line pull toward it is what makes the squared-distance weighting click — you've read that big misses count more, and now you can see the counting happen. The influence toggle draws a halo around whichever point the fit depends on most, which is a different question from how far off the point is. Drag one to the edge and the halo grows even when the point sits right on the line.

![Claude's response with an interactive regression canvas: a scatter plot with draggable points, slope, intercept, and R² readouts, toggles for residuals and influence, and an outlier labeled 'drag me'](https://academy.claude.com/assets/v1/regression-canvas-iir2n6w7.png)

## 4. Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Ask Claude to show the math behind what you noticed

Something you noticed while dragging raises a question — ask for the math behind it, and Claude builds a second visual below showing the formula in action.

The influence halo grew when I moved the point sideways but barely changed when I moved it up. Show me the leverage formula and where horizontal distance shows up in it.



Open in Claude

### Ask Claude to overlay a second thing on the same canvas

Ask Claude to overlay a second thing on the canvas you built — both stay visible, and dragging shows you how they respond differently.

Overlay a robust regression on the same points I made. I want to drag the outlier and watch both lines move.



Open in Claude

### Ask Claude to turn the canvas into a prediction test

Claude generates test scatters, you predict what happens before dragging, and it tells you if your instinct was right.

Give me a few test patterns — show me a scatter and ask me to predict what one outlier will do before I drag it.



Open in Claude

## 5. Tricks, tips, and troubleshooting

### How you word your prompt shapes what you get

"Mess with," "watch what happens," "feel why" — that language is what gets a blank canvas. Claude reads verbs of interaction as a signal to build something you manipulate; a plain "explain" tends to produce a pre-loaded demo you watch.

### Tell Claude what to adjust and it redraws

If what streams in is close but missing something — a second variable, a simpler version, a toggle for a concept the first pass skipped — say so. Claude redraws. The back-and-forth is how you get to the version that fits what you're trying to feel.

### What to do with the visual next

Hover for options: copy as image drops it into your notes, Save as Artifact keeps the canvas interactive for later. Or ask Claude to write up what you now understand — the visual surfaced one gap, and putting it in words often surfaces the next.

## 6. Ready to try for yourself?

Try it on any formula you can do but don't yet have a feel for — regression, probability, anything where you can compute the answer but can't predict how it'll move. Describe the gap and let Claude build something to manipulate.

I'm learning linear regression and I can do the formula but I don't get it. Can you give me something where I can mess with the data points myself and watch what happens to the line? I want to actually feel why one weird point can throw the whole thing off. Can you help me visualize?

Try in Claude
