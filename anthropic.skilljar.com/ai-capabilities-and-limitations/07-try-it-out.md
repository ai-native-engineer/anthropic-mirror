<!-- https://anthropic.skilljar.com/ai-capabilities-and-limitations/456454 -->

Visualizing 1024D Space


# Visualizing 1024D Space

How multidimensional "nearness" works



## The Problem with Strings

Search "car" and you'll find every document containing the word "car." You won't find "automobile." Or "vehicle." Or "my Civic needs new brakes."

For decades, that was search, returning results based on string similarity rather than meaning. Google continuously made incremental improvements with engineering: Synonym dictionaries mapped "car" to "automobile," Stemming rules connected "running" to "run," and click-pattern mining surfaced that people who search "NYC apartments" want the same results as "Manhattan rentals." The connections between non-matching strings had to be mapped more or less by hand.

**Embeddings** challenged all of this with the idea that **meaning** could be a *place*. By converting text into coordinates, similar concepts end up near each other. This mapping of semantic space isn't manual, but rather **emergent** from training data.

## Encoding

Let's start with a simplified example.

Imagine you were to score every document in a corpus of knowledge on two dimensions: how much it relates to dinosaurs, and how much it relates to roller coasters. Documents about similar topics would end up near each other.

Let's start with just three sources. Place each of these where you think they belong.

How much does this relate to **roller coasters**? →

not at all
very
very
click to place selected item

How much does this relate to **dinosaurs**? →

Sources

🦕

A children's book about dinosaursclick to select


🎢

The Velocicoaster web pageclick to select


📚

An entire encyclopediaclick to select

You've just mapped meaning in 2D space, plotting our collection of items based on what they're about.

## Retrieval

Now let's search this space.

Plot a question on the same graph with the same axes. By mapping your question with the same logic you used to map sources, you can be sure that the nearest items will be the most relevant. Bonus feature: Use the slider to control how many get retrieved.

Sources to retrieve (k):

2

How much does this relate to **roller coasters**? →

not at all
very
very
click to place the question

How much does this relate to **dinosaurs**? →

Question

❓ "What's the best dinosaur-themed roller coaster?"

click graph to place

That's **similarity search** in a nutshell. We plot the question and find the nearest k items. Instead of keyword matching or synonym tables, we use multi-dimensional proximity.

Two axes is a start. But two dimensions can only capture two concepts. The real world has more than two topics, so we need more **dimensions**.

## More Dimensions

What if we added a third axis? Let's use **biology**.

The children's book scores high (species, habitats, diets). The encyclopedia covers some. The Velocicoaster page barely mentions it.

Drag to rotate.

Three dimensions, three coordinates per document. The Velocicoaster page is now (0.50, 0.90, 0.05) instead of (0.50, 0.90).

Now try to picture a fourth axis.

Since I only exist in 3 dimensions, I personally can't 😔 but that actually doesn't matter! Each new dimension just adds another coordinate to each point and another squared term to the distance formula. The spatial representation stops working at 4D, but the math keeps working.

We're going to have to push well past 4D, because real **embedding models** use around a thousand dimensions. Each document and each query becomes a point in that thousand-dimensional space. "Find the nearest documents" still means the same thing it meant on the 2D graph. It's just a longer distance calculation.

## Unlabeled Axes

We chose the axes: dinosaurs, roller coasters, biology. But who determines which 1,024 topics make it into a real embedding model?

In point of fact, no one decides. The meaning of each axis is emergent (meaning it just shows up in training), and more of a black box. You can't look at dimension 847 and say "that's the dinosaur axis." The dimensions don't correspond to anything a human could name.

This makes the space harder to reason about. We can't interrogate dimension 847 to understand why two texts landed near each other, or why something we expected to be close ended up far away.

## Text as Coordinates

So who assigns the coordinates? An **embedding model**. Any string in, a fixed-length list of numbers out.

Text

"work from home"

→

Embedding

[0.23, -0.87, 0.41, ...]

1,024 values

Text

"Employees may work remotely up to two days per week with manager approval."

→

Embedding

[0.71, 0.09, -0.33, ...]

1,024 values

The output is always the same length (1,024 values in our specific case, since we're using VoyageAI's embeddings model) and this is true whether the input is three words or three paragraphs. One chunk of text corresponds to one point in space. The embedding model reads the text and outputs a single **vector**.

The math-eyed among you will recognize that "vector" and "coordinate set" aren't actually interchangeable, but for our purposes, it's appropriate to think of the vector as the address where this text lives relative to everything else.

## Similarity

"Nearest" on our 2D graph meant straight-line distance. In practice, similarity search uses **cosine similarity** instead. Cosine similarity is just another measure of how similar two pieces of text are, based on the direction their vectors point rather than how far apart they sit.

Try it yourself! Pick two sources to see their cosine similarity.

Source A

❓
🦕
🎢
📚

❓ Best dinosaur roller coaster?

Source B

❓
🦕
🎢
📚

🦕 Children's dinosaur book

Cosine similarity
0.2894

-1 *opposite*
0 *unrelated*
1 *identical*

Try comparing the Velocicoaster page to the dinosaur book — their vectors point in very different directions. The encyclopedia lands somewhere in between everything, which fits, since it's a jack of all trades but a master of none.
