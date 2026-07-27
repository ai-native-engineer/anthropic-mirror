<!-- source: https://platform.claude.com/cookbook/misc-pdf-upload-summarization -->

# "Uploading" PDFs to Claude Via the API

One really nice feature of [Claude.ai](https://www.claude.ai) is the ability to upload PDFs. Let's mock up that feature in a notebook, and then test it out by summarizing a long PDF.

We'll start by installing the Anthropic client and create an instance of it we will use throughout the notebook.

python

```
%pip install anthropic
```

python

```
from anthropic import Anthropic
# While PDF support is in beta, you must pass in the correct beta header
client = Anthropic(default_headers={
    "anthropic-beta": "pdfs-2024-09-25"
  }
)
# For now, only claude-sonnet-4-6 supports PDFs
MODEL_NAME = "claude-sonnet-4-6"
```

We already have a PDF available in the `../multimodal/documents` directory. We'll convert the PDF file into base64 encoded bytes. This is the format required for the [PDF document block](https://docs.claude.com/en/docs/build-with-claude/pdf-support) in the Claude API. Note that this type of extraction works for both text and visual elements (like charts and graphs).

python

```
import base64

# Start by reading in the PDF and encoding it as base64
file_name = "../multimodal/documents/constitutional-ai-paper.pdf"
with open(file_name, "rb") as pdf_file:
  binary_data = pdf_file.read()
  base64_encoded_data = base64.standard_b64encode(binary_data)
  base64_string = base64_encoded_data.decode("utf-8")
```

With the paper downloaded and in memory, we can ask Claude to perform various fun tasks with it. We'll pass the document ot the model alongside a simple question.

python

```
prompt = """
Please do the following:
1. Summarize the abstract at a kindergarten reading level. (In <kindergarten_abstract> tags.)
2. Write the Methods section as a recipe from the Moosewood Cookbook. (In <moosewood_methods> tags.)
3. Compose a short poem epistolizing the results in the style of Homer. (In <homer_results> tags.)
"""
messages = [
    {
        "role": 'user',
        "content": [
            {"type": "document", "source": {"type": "base64", "media_type": "application/pdf", "data": base64_string}},
            {"type": "text", "text": prompt}
        ]
    }
]
```

python

```
def get_completion(client, messages):
    return client.messages.create(
        model=MODEL_NAME,
        max_tokens=2048,
        messages=messages
    ).content[0].text
```

python

```
completion = get_completion(client, messages)
print(completion)
```

```
<kindergarten_abstract>
The scientists wanted to make computer helpers that are nice and don't do bad things. They taught the computer how to check its own work and fix its mistakes without humans having to tell it what's wrong every time. It's like teaching the computer to be its own teacher! They gave the computer some basic rules to follow, like "be kind" and "don't hurt others." Now the computer can answer questions in a helpful way while still being nice and explaining why some things aren't okay to do.
</kindergarten_abstract>

<moosewood_methods>
Constitutional AI Training Stew
A nourishing recipe for teaching computers to be helpful and harmless

Ingredients:
- 1 helpful AI model, pre-trained
- A bundle of constitutional principles
- Several cups of training data
- A dash of human feedback (for helpfulness only)
- Chain-of-thought reasoning, to taste

Method:
1. Begin by gently simmering your pre-trained AI model in a bath of helpful training data until it responds reliably to instructions.

2. In a separate bowl, combine your constitutional principles with some example conversations. Mix well until principles are evenly distributed.

3. Take your helpful AI and ask it to generate responses to challenging prompts. Have it critique its own responses using the constitutional principles, then revise accordingly. Repeat this process 3-4 times until responses are properly seasoned with harmlessness.

4. For the final garnish, add chain-of-thought reasoning and allow the model to explain its decisions step by step.

5. Let rest while training a preference model using AI feedback rather than human labels.

Serves: All users seeking helpful and harmless AI assistance
Cook time: Multiple training epochs
Note: Best results come from consistent application of principles throughout the process
</moosewood_methods>

<homer_results>
O Muse! Sing of the AI that learned to be
Both helpful and harmless, guided by philosophy
Without human labels marking right from wrong
The model learned wisdom, grew capable and strong

Through cycles of critique and thoughtful revision
It mastered the art of ethical decision
Better than models trained by human hand
More transparent in purpose, more clear in command

No longer evasive when faced with hard themes
But engaging with wisdom that thoughtfully deems
What counsel to give, what bounds to maintain
Teaching mortals while keeping its principles plain

Thus did the researchers discover a way
To scale up alignment for use every day
Through constitutional rules and self-guided learning
The path to safe AI they found themselves earning
</homer_results>
```
