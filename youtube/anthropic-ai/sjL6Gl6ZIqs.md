---
title: "Claude 3 Opus as an economic analyst"
channel: anthropic-ai
url: https://www.youtube.com/watch?v=sjL6Gl6ZIqs
youtube_id: sjL6Gl6ZIqs
published: 2024-03-04
duration: "3:59"
---

# Claude 3 Opus as an economic analyst

[![Claude 3 Opus as an economic analyst](https://img.youtube.com/vi/sjL6Gl6ZIqs/hqdefault.jpg)](https://www.youtube.com/watch?v=sjL6Gl6ZIqs)

<details>
<summary>자막: Claude 3 Opus as an economic analyst (3:59)</summary>

[00:00]
in this video we're going to see if
Claude and a couple of friends can help
us analyze the world economy in a matter
of
minutes okay I've asked Claude 3 Opus
which is the largest model in anthropics
new Claude 3 family to look at the GDP
trends for the US and write down a
markdown table of what it sees we've
given Opus and all the other models in
the clae 3 family extensive training on
tool use and one of the major tools it's
using is this web view tool it goes to a
URL looks at what's on the page and
because it's multimodal it can use the
information on that page to solve
complex problems so here's the markdown
and it's important to note that CLA
doesn't have direct access to these
numbers it's literally looking at the
same browser you and I are seeing
looking at the trend line and trying to
estimate what the exact numbers
are let's see how accurate it was we've
asked the model to create a plot of the
data and it's used the second tool this

[00:01]
python interpreter to write out the code
and then render the image for us to
check and here's the image look it's
actually added helpful little tool tip
animations to explain some of the major
Peaks and troughs in the last decade or
two of the US economy and we can compare
that graph with the actual data and it
turns out it's pretty close it's
actually within 5%
accuracy and by the way claud's
transcription here isn't just coming
from its pre-existing knowledge of US
GDP we tried it with a large sample of
madeup GDP graphs and its transcription
accuracy was within 11% on
average next we asked the model to do
some statistical analysis projecting out
into the future performing simulations
to see where the GDP of the US might
head and we can see that it's run this
analysis using Python and it's able to
perform these Monte Carlo simulations to
see what the range of GDP possibilities
might look like for the next decade or

[00:02]
so but I wonder if we can go further
we're going to get the model to analyze
a more complicated question that is how
GDP might change across all of the
biggest world economies and then to help
it do that we're going to give it one
more tool called dispatch sub agents
this basically allows the model to break
down the problem into lots of sub
problems and then write prompts for
other versions of itself to help pick
out the slack the models can then
complete a more complex task by all
working together here you can see it's
written this prompt and given very
precise instructions that it wants the
other models to follow including a
format for the data that it's hoping to
return it's dispatched a version of this
prompt to one model that's going to look
at the US one for China One for Germany
Japan and so on we can see in these
progress bars that the sub agent models
are now completing the set task for each
of the individual economies

[00:03]
they're going to the relevant web pages
they're getting the information they're
running the code to analyze it just like
we saw in the previous US example but
all in
parallel let's just skip forward to see
what the model produced you can see it's
run the analysis it's produced a pre-
and post pie chart of how it expects the
world economy to look in 2030 versus
2020 and it's given us a written
analysis too where it makes variable
predictions that relate to the
statistical analysis that it ran it's
telling us that it thinks the GDP share
of particular economies will change and
which ones will be larger or smaller by
2030 so there we have it complex
multi-step multimodal analysis run by a
model that can create sub agents to get
even more tasks running in parallel
we're excited to see what you our
customers can do with these Advanced
Claude 3
capabilities

</details>
