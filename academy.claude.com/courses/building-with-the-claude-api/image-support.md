<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/image-support -->

Lesson 40 of 67 · Building with the Claude APIImage support

Claude's vision capabilities let you include images in your messages and ask Claude to analyze them in countless ways. You can ask Claude to describe what's in an image, compare multiple images, count objects, or perform complex visual analysis tasks.

## Image Handling Basics

![](https://academy.claude.com/assets/media/98c768b5f76c2323de2b36964b308e2de4ad89ee155b489ac419e0aeab21b045.jpg)

There are several important limitations to keep in mind when working with images:

* Up to 100 images across all messages in a single request
* Max size of 5MB per image
* When sending one image: max height/width of 8000px
* When sending multiple images: max height/width of 2000px
* Images can be included as base64 encoding or a URL to the image
* Each image counts as tokens based on its dimensions: `tokens = (width px × height px) / 750`

To send an image to Claude, you include an image block in your user message alongside text blocks. Here's the structure:

python

```
with open("image.png", "rb") as f:
    image_bytes = base64.standard_b64encode(f.read()).decode("utf-8")

add_user_message(messages, [
    # Image Block
    {
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": "image/png",
            "data": image_bytes,
        }
    },
    # Text Block
    {
        "type": "text",
        "text": "What do you see in this image?"
    }
])
```

## Message Flow

![](https://academy.claude.com/assets/media/2e3de7bc759472bad884263d83f216e3b4a429052afd5a01a1359acd4137788a.jpg)

The conversation works just like text-only interactions. Your server sends a user message containing both image and text blocks to Claude, and Claude responds with a text block containing its analysis.

## Prompting Techniques

![](https://academy.claude.com/assets/media/89054de9a3667eb929a019f59efb5db86e9f3a95713b6fa67925a98be65293ee.jpg)

The key to getting good results with images is applying the same prompting engineering techniques you'd use with text. Simple prompts often lead to poor results. For example, asking "How many marbles are in this image?" might return an incorrect count.

You can dramatically improve Claude's accuracy by:

* Providing detailed guidelines and analysis steps
* Using one-shot or multi-shot examples
* Breaking down complex tasks into smaller steps

### Step-by-Step Analysis

![](https://academy.claude.com/assets/media/6cec588debfe41c1968153ee66e3a161fa086e614f9ef28ba0cfb5176e2cff58.jpg)

Instead of a simple question, provide Claude with a methodology:

```
Analyze this image of marbles and determine the exact count using this methodology:
1. Begin by identifying each unique marble one at a time. Assign each a number as you identify it.
2. Verify your result by counting with a different method. Start from the bottom-left corner and work row by row, from left to right.

What is the exact, verified number of marbles in this image?
```



### One-Shot Examples

![](https://academy.claude.com/assets/media/0dd5c0bdeb2a02989bf35771a4fabb86e4c6cc8acc45ba3e74d887f1e9825931.jpg)

You can also improve accuracy by providing examples within your message. Include an image with a known count, state the correct answer, then ask about your target image. This gives Claude a reference point for the type of analysis you want.

## Real-World Example: Fire Risk Assessment

![](https://academy.claude.com/assets/media/cee23b7082e886a69fbe447eb40637e2c9d1bb60fafbd7b04756588c3439f043.jpg)

Here's a practical application: automating fire risk assessments for home insurance. Instead of sending inspectors to every property, insurance companies can use satellite imagery and Claude's analysis.

The system analyzes satellite images to identify:

* Dense, close-packed trees near the residence
* Difficult access routes for emergency services
* Branches overhanging the residence

Rather than a simple prompt like "provide a fire risk score," a well-structured prompt breaks down the analysis into specific steps:

```
Analyze the attached satellite image of a property with these specific steps:

1. Residence identification: Locate the primary residence on the property by looking for:
   - The largest roofed structure
   - Typical residential features (driveway connection, regular geometry)
   - Distinction from other structures (garages, sheds, pools)

2. Tree overhang analysis: Examine all trees near the primary residence:
   - Identify any trees whose canopy extends directly over any portion of the roof
   - Estimate the percentage of roof covered by overhanging branches (0-25%, 25-50%, 50-75%, 75%+)
   - Note particularly dense areas of overhang

3. Fire risk assessment: For any overhanging trees, evaluate:
   - Potential wildfire vulnerability (ember catch points, continuous fuel paths to structure)
   - Proximity to chimneys, vents, or other roof openings if visible
   - Areas where branches create a "bridge" between wildland vegetation and the structure

4. Defensible space identification: Assess the property's overall vegetative structure:
   - Identify if trees connect to form a continuous canopy over or near the home
   - Note any obvious fuel ladders (vegetation that can carry fire from ground to tree to roof)

5. Fire risk rating: Based on your analysis, assign a Fire Risk Rating from 1-4:
   - Rating 1 (Low Risk): No tree branches overhanging the roof, good defensible space around the home
   - Rating 2 (Moderate Risk): Minimal overhang (<25% of roof), some separation between tree canopies
   - Rating 3 (High Risk): Significant overhang (25-50% of roof), connected tree canopies, multiple vulnerability points
   - Rating 4 (Severe Risk): Extensive overhang (>50% of roof), dense vegetation against structure

For each item above (1-5), write one sentence summarizing your findings, with your final response being the numerical rating.
```



This detailed prompt guides Claude through a systematic analysis, resulting in much more accurate and useful assessments than a simple request would provide.

Remember: the same prompting techniques that work for text apply to images. Invest time in crafting detailed, structured prompts rather than relying on simple questions if you want reliable results.
