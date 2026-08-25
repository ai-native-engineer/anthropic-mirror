<!-- source: https://platform.claude.com/cookbook/tool-use-vision-with-tools -->

#  Using Vision with Tools

In this recipe, we'll demonstrate how to combine Vision with tool use to analyze an image of a nutrition label and extract structured nutrition information using a custom tool.

##  Setup

First, let's install the necessary libraries and set up the Claude API client:

%pip install anthropic IPython

import base64

from anthropic import Anthropic

from IPython.display import Image

client = Anthropic()

MODEL\_NAME = "claude-opus-4-1"

#  Defining the Nutrition Label Extraction Tool

Next, we'll define a custom tool called "print\_nutrition\_info" that extracts structured nutrition information from an image. The tool has properties for calories, total fat, cholesterol, total carbs, and protein:

nutrition\_tool = {

"name": "print\_nutrition\_info",

"description": "Extracts nutrition information from an image of a nutrition label",

"input\_schema": {

"type": "object",

"properties": {

"calories": {"type": "integer", "description": "The number of calories per serving"},

"total\_fat": {

"type": "integer",

"description": "The amount of total fat in grams per serving",

},

"cholesterol": {

"type": "integer",

"description": "The amount of cholesterol in milligrams per serving",

},

"total\_carbs": {

"type": "integer",

"description": "The amount of total carbohydrates in grams per serving",

},

"protein": {

"type": "integer",

"description": "The amount of protein in grams per serving",

},

},

"required": ["calories", "total\_fat", "cholesterol", "total\_carbs", "protein"],

},

}

##  Analyzing the Nutrition Label Image

Now, let's put it all together. We'll load a nutrition label image, pass it to Claude along with a prompt, and have Claude call the "print\_nutrition\_info" tool to extract the structured nutrition information into a nicely formatted JSON object:

Image(filename="../images/tool\_use/nutrition\_label.png")

![Output image](https://platform.claude.com/cookbook/images/notebooks/tool-use-vision-with-tools/tool-use-vision-with-tools_cell8_out0_9580cc29.png)

def get\_base64\_encoded\_image(image\_path):

with open(image\_path, "rb") as image\_file:

binary\_data = image\_file.read()

base\_64\_encoded\_data = base64.b64encode(binary\_data)

base64\_string = base\_64\_encoded\_data.decode("utf-8")

return base64\_string

message\_list = [

{

"role": "user",

"content": [

{

"type": "image",

"source": {

"type": "base64",

"media\_type": "image/png",

"data": get\_base64\_encoded\_image("../images/tool\_use/nutrition\_label.png"),

},

},

{

"type": "text",

"text": "Please print the nutrition information from this nutrition label image.",

},

],

}

]

response = client.messages.create(

model=MODEL\_NAME, max\_tokens=4096, messages=message\_list, tools=[nutrition\_tool]

)

if response.stop\_reason == "tool\_use":

last\_content\_block = response.content[-1]

if last\_content\_block.type == "tool\_use":

tool\_name = last\_content\_block.name

tool\_inputs = last\_content\_block.input

print(f"=======Claude Wants To Call The {tool\_name} Tool=======")

print(tool\_inputs)

else:

print("No tool was called. This shouldn't happen!")

```
=======Claude Wants To Call The print_nutrition_info Tool=======
{'calories': 200, 'total_fat': 15, 'cholesterol': 30, 'total_carbs': 30, 'protein': 5}
```
