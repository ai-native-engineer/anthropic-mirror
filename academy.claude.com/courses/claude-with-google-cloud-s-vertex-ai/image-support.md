<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/image-support -->

Lesson 44 of 66 · Claude with Google Cloud's Vertex AIImage support

Claude's vision capabilities let you include images in your messages and ask Claude to analyze them in sophisticated ways. You can ask Claude to describe image contents, compare multiple images, count objects, or perform complex visual analysis tasks.

## Image Handling Basics

![](https://academy.claude.com/assets/media/c7b1cb42c0c5f46b5bf09f44253dd36437835d6302d817dd9f04345498dbd6c0.png)

When working with images in Claude, you need to understand several key limitations:

* Up to 100 images across all messages in a single request
* Max size of 5MB per image
* When sending one image: max height/width of 8000px
* When sending multiple images: max height/width of 2000px
* Images can be included as base64 encoding or a URL to the image
* Each image counts as tokens based on dimensions: `tokens = (width px × height px) / 750`

To include an image, you add an image block to your user message alongside text blocks. Here's the structure:

python

```
with open("image.png", "rb") as f:
    image_bytes = base64.standard_b64encode(
        f.read()
    ).decode("utf-8")

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

![](https://academy.claude.com/assets/media/89621a94c5d850a7741c336f51d220402877da316e72bcc34de53826768d8cb8.png)

The conversation works just like text-only interactions. Your server sends a user message containing both image and text blocks to Claude, and Claude responds with a text message analyzing the image.

## Prompting Techniques

![](https://academy.claude.com/assets/media/7822fde09008ecaaef45a499a4c64544727208168ee8e58cb4b75ccc0151695f.png)

The most important thing to understand about Claude's vision capabilities is that good prompting techniques are absolutely critical. Simple prompts often produce poor results, even with clear images.

For example, asking "How many marbles are in this image?" with an image containing 12 marbles might return an incorrect count of 13. You can dramatically improve accuracy by applying the same prompting engineering techniques you'd use for text:

* Providing detailed guidelines and analysis steps
* Using one-shot or multi-shot examples
* Breaking down complex tasks into smaller steps

### Step-by-Step Analysis

![](https://academy.claude.com/assets/media/5cd168f34e55480f8d3b7a9b76f65fcda3f8d4c498dca282a14c72a6c4f20947.png)

Instead of a simple question, provide Claude with a methodology:

```
Analyze this image of marbles and determine the exact count using this methodology:
1. Begin by identifying each unique marble one at a time. Assign each a number as you identify it.
2. Verify your result by counting with a different method. Start from the bottom-left corner and work row by row, from left to right.

What is the exact, verified number of marbles in this image?
```



This structured approach helps Claude get the correct count of 12 marbles.

### One-Shot Examples

![](https://academy.claude.com/assets/media/9b02f763819da04216b0ab891e75ffca026fc66cf28f979ce70269ce0c8d1274.png)

You can also use one-shot prompting by including multiple image-text pairs in a single message:

```
[Image of 11 marbles]
The image above has 11 marbles in it.

[Image of 12 marbles]
How many marbles are in this image?
```



Providing an example significantly improves Claude's accuracy on the target image.

## Real-World Example: Fire Risk Assessment

![](https://academy.claude.com/assets/media/d71061d0c67d9ece85db6c5a354f08bbb66dbc6ff83dd4a13d7d118d914841fa.png)

Here's a practical application: automating fire risk assessments for home insurance. Insurance companies often require homeowners to trim trees around their property to reduce wildfire risk. Instead of sending inspectors to each property, you can use satellite imagery with Claude.

The system analyzes satellite images to identify:

* Dense, close-packed trees near the residence
* Difficult access routes for emergency services
* Branches overhanging the residence

Rather than a simple prompt like "provide a fire risk score," you create a detailed analysis framework:

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
   - Rating 1 (Low Risk): No tree branches overhanging the roof, good defensible space around
   - Rating 2 (Moderate Risk): Minimal overhang (<25% of roof), some separation between tree canopies
   - Rating 3 (High Risk): Significant overhang (25-50% of roof), connected tree canopies, multiple points of vulnerability
   - Rating 4 (Severe Risk): Extensive overhang (>50% of roof), dense vegetation against structure

For each item above (1-5), write one sentence summarizing your findings, with your final response being the numerical rating.
```



This comprehensive prompt guides Claude through a systematic analysis, resulting in accurate and actionable fire risk assessments. When tested with a heavily tree-covered property, Claude correctly identified it as a "3 (High Risk)" due to significant tree overhang and connected canopies around the structure.

The key takeaway is that Claude's vision capabilities are powerful, but they require the same careful prompt engineering you'd use for any complex task. Invest time in creating detailed, structured prompts rather than relying on simple questions.
