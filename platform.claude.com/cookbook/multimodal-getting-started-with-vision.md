<!-- source: https://platform.claude.com/cookbook/multimodal-getting-started-with-vision -->

#  Getting started - how to pass images into Claude

The Claude 3 model family supports image inputs in the API. Here’s how you can pass images to Claude:

%pip install anthropic IPython

from IPython.display import Image

Image(filename="../images/sunset.jpeg")

![Output image](https://platform.claude.com/cookbook/images/notebooks/multimodal-getting-started-with-vision/multimodal-getting-started-with-vision_cell2_out0_fe5c0f12.jpeg)

import base64

from anthropic import Anthropic

client = Anthropic()

MODEL\_NAME = "claude-opus-4-1"

with open("../images/sunset.jpeg", "rb") as image\_file:

binary\_data = image\_file.read()

base\_64\_encoded\_data = base64.b64encode(binary\_data)

base64\_string = base\_64\_encoded\_data.decode("utf-8")

message\_list = [

{

"role": "user",

"content": [

{

"type": "image",

"source": {"type": "base64", "media\_type": "image/jpeg", "data": base64\_string},

},

{"type": "text", "text": "Write a sonnet based on this image."},

],

}

]

response = client.messages.create(model=MODEL\_NAME, max\_tokens=2048, messages=message\_list)

print(response.content[0].text)

```
Upon the rocky shore, a beacon bright,
Its steadfast light a guide through darkest night.
While sun descends in hues of pink and red,
The lighthouse stands, a stalwart figure head.

The waves crash 'gainst the weathered stone below,
A ceaseless rhythm, ancient ebb and flow.
Yet still the tower remains, resolute,
A guardian watching, ever vigilant mute.

The vast expanse of sea and sky surround,
Horizon's line where heaven meets the ground.
This timeless scene, a testament to might,
Of nature's power and the human fight.

The lighthouse, proud amid the fading day,
Eternal symbol, showing safe the way.
```

##  Passing an image through a url

If you only have a URL of the image you can still pass it to Claude with just a few short lines of code.

IMAGE\_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Machu\_Picchu%2C\_Peru\_%282018%29.jpg/2560px-Machu\_Picchu%2C\_Peru\_%282018%29.jpg"

Image(url=IMAGE\_URL)

```
<IPython.core.display.Image object>
```

import httpx

IMAGE\_DATA = base64.b64encode(httpx.get(IMAGE\_URL).content).decode("utf-8")

message\_list = [

{

"role": "user",

"content": [

{

"type": "image",

"source": {"type": "base64", "media\_type": "image/jpeg", "data": IMAGE\_DATA},

},

{"type": "text", "text": "Describe this image in two sentences."},

],

}

]

response = client.messages.create(model=MODEL\_NAME, max\_tokens=2048, messages=message\_list)

print(response.content[0].text)

```
The image depicts the ancient Inca city of Machu Picchu, perched high in the Andes Mountains of Peru. The well-preserved stone ruins, including terraces, plazas, and buildings, are set against a stunning backdrop of steep, verdant mountains under a partly cloudy sky.
```
