<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/image-support -->

Lesson 43 of 65 · Claude with Amazon BedrockImage support

Claude's vision capabilities allow you to include images in your messages and ask Claude to analyze, compare, count objects, or perform virtually any visual task you can imagine. This opens up powerful possibilities for applications ranging from document analysis to automated assessments.

## Image Handling Basics

When working with images in Claude, you need to understand a few key limitations:

* Up to 20 images across all messages in a single request
* Max size of 3.75MB
* Max height/width of 8000px
* Each image counts as a certain number of tokens: `tokens = (width px × height px) / 750`

![](https://academy.claude.com/assets/media/526d6a757d8d880fe2d248896cf82c9fcab501795d46eed54dc629dcd228399f.png)

To include an image, you add it as another type of message part. For each image you want to send, you include one image part in your user message. The structure looks like this:

python

```
with open("image.png", "rb") as f:
    image_bytes = f.read()

add_user_message(messages, [
    {
        "image": {
            "format": "png",
            "source": {"bytes": image_bytes}
        }
    },
    {"text": "What do you see in this image?"}
])
```

## Multiple Images

You can send multiple images in a single message by adding multiple image parts. Claude can then analyze relationships between images, compare them, or answer questions that require understanding multiple visual inputs.

![](https://academy.claude.com/assets/media/eb3d93da4c6eae9dfbb42c81d9af0310645c111350adb26c2940b3906eb97d9d.png)

## Prompting Techniques

The most important thing to understand about Claude's vision capabilities is that all the same prompting engineering techniques apply to images. You can dramatically increase Claude's vision accuracy by providing guidelines, analysis steps, or using one-shot/multi-shot examples.

![](https://academy.claude.com/assets/media/a44d1b913150f04b56211cbb5236f2ea95cae516f182aa779715df8a4512d478.png)

For example, instead of simply asking "How many marbles are in this image?", you can provide a structured approach:

```
Analyze this image of marbles and determine the exact count using this methodology:
1. Begin by identifying each unique marble one at a time. Assign each a number as you identify it.
2. Verify your result by counting with a different method. Start from the bottom-left corner and work row by row, from left to right.
What is the exact, verified number of marbles in this image?
```



![](https://academy.claude.com/assets/media/6f2b0e93d9c939e8aaac277640ff521cfe27d54a8bc87a1b71b8e5dba06c61cf.png)

Another effective technique is one-shot prompting, where you provide an example image with the correct analysis before asking Claude to analyze your target image:

![](https://academy.claude.com/assets/media/2c5f3cf4f134638be4f1040e7c813ec8a27d3fc0e8d68c5b995a8e7c265d32b0.png)

## Real-World Example: Fire Risk Assessments

A practical application of Claude's vision capabilities is automated fire risk assessment for insurance companies. Instead of sending inspectors to each property, companies can use high-resolution satellite imagery and ask Claude to evaluate fire risks.

![](https://academy.claude.com/assets/media/80ed96dcab575198d37f2de1bf938f5613e751b5f7047e83eca7b57e2e4108dd.png)

The system can analyze several key factors:

* Dense, close-packed trees near the residence
* Difficult access routes for emergency vehicles
* Branches overhanging the residence
* Overall tree density and spacing

Here's how you might structure such an analysis:

python

```
with open('./images/prop7.png', 'rb') as f:
    image_bytes = f.read()

messages = []

add_user_message(messages, [
    {"image": {"format": "png", "source": {"bytes": image_bytes}}},
    {"text": prompt}
])

response = chat(messages)
```

The key to success with this type of complex visual analysis is providing detailed, structured prompts that guide Claude through specific analysis steps rather than asking for a simple assessment.

Remember: when working with images, don't fall into the trap of using simple prompts. Apply the same prompt engineering techniques you've learned for text-based interactions to dramatically improve Claude's visual analysis accuracy.
