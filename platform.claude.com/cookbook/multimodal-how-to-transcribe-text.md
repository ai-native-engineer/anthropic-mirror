<!-- source: https://platform.claude.com/cookbook/multimodal-how-to-transcribe-text -->

#  How to transcribe documents with Claude

Claude 3 is great at reading unstructured text and information within images and PDFs and turning it into structured text. We'll take a look at a few examples but first let's setup the code we need to run the notebook.

%pip install anthropic IPython

import base64

from anthropic import Anthropic

client = Anthropic()

MODEL\_NAME = "claude-opus-4-8"

def get\_base64\_encoded\_image(image\_path):

with open(image\_path, "rb") as image\_file:

binary\_data = image\_file.read()

base\_64\_encoded\_data = base64.b64encode(binary\_data)

base64\_string = base\_64\_encoded\_data.decode("utf-8")

return base64\_string

##  Transcribing typed text

The advantage of using Claude 3 over traditional OCR systems is that you can specify exactly what you want to transcribe due to Claude 3's advanced reasoning capabilities. For this image, let’s transcribe just the code in the answer.

from IPython.display import Image

Image(filename="../images/transcribe/stack\_overflow.png")

![Output image](https://platform.claude.com/cookbook/images/notebooks/multimodal-how-to-transcribe-text/multimodal-how-to-transcribe-text_cell4_out0_36902276.png)

message\_list = [

{

"role": "user",

"content": [

{

"type": "image",

"source": {

"type": "base64",

"media\_type": "image/png",

"data": get\_base64\_encoded\_image("../images/transcribe/stack\_overflow.png"),

},

},

{"type": "text", "text": "Transcribe the code in the answer. Only output the code."},

],

}

]

response = client.messages.create(model=MODEL\_NAME, max\_tokens=2048, messages=message\_list)

print(response.content[0].text)

```
import os
import base64

image = 'test.jpg'

encoded_string = ""
with open(image, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
file = encoded_string
```

##  Transcribing handwritten text

That's good but let's try something a little harder. Claude 3 excels at transcribing handwritten text as well. Let's ask Claude 3 to transcribe this handwritten prescription note.

Image(filename="../images/transcribe/school\_notes.png")

![Output image](https://platform.claude.com/cookbook/images/notebooks/multimodal-how-to-transcribe-text/multimodal-how-to-transcribe-text_cell7_out0_a28fbe7d.png)

message\_list = [

{

"role": "user",

"content": [

{

"type": "image",

"source": {

"type": "base64",

"media\_type": "image/png",

"data": get\_base64\_encoded\_image("../images/transcribe/school\_notes.png"),

},

},

{

"type": "text",

"text": "Transcribe this text. Only output the text and nothing else.",

},

],

}

]

response = client.messages.create(model=MODEL\_NAME, max\_tokens=2048, messages=message\_list)

print(response.content[0].text)

```
Levels of Cellular Organization
1) Cells group together to make tissue.
2) Tissues group together to make an organ.
3) Organs group together to make an organ system
4) Organ systems group together to make an organism

Organism -> a living thing that can
carry out life processes by itself.

- Multicellular organisms have specialized
cells to perform specific functions.
> This makes them more efficient
and typically have a longer life span.

Tissue = a group of similar cells
that perform a common function.
1) Animals are made of four
basic types of tissue
> nervous, epithelial, connective,
and muscle
2) Plants have three types
of tissue
> transport, protective, and
ground
```

##  Transcribing forms

How about we try a combination of typed and handwritten text? This is common across a variety of documents like insurance and report forms.

Image(filename="../images/transcribe/vehicle\_form.jpg")

![Output image](https://platform.claude.com/cookbook/images/notebooks/multimodal-how-to-transcribe-text/multimodal-how-to-transcribe-text_cell10_out0_592ce176.jpeg)

message\_list = [

{

"role": "user",

"content": [

{

"type": "image",

"source": {

"type": "base64",

"media\_type": "image/jpeg",

"data": get\_base64\_encoded\_image("../images/transcribe/vehicle\_form.jpg"),

},

},

{"type": "text", "text": "Transcribe this form exactly."},

],

}

]

response = client.messages.create(model=MODEL\_NAME, max\_tokens=2048, messages=message\_list)

print(response.content[0].text)

```
VEHICLE INCIDENT REPORT FORM

Use this form to report accidents, injuries, medical situations, criminal activities, traffic incidents, or student behavior incidents. If possible, a report should be completed within 24 hours of the event.

Date of Report: 02/29, 2024

PERSON INVOLVED

Full Name: John Doe Address: 123 Main St

Identification: ■ Driver's License No. 474921 □ Passport No. ___________
□ Other: ____________________

Phone: (678) 999-8212 E-Mail: john@gmail.com

THE INCIDENT

Date of Incident: 02/29/2024 ■ Time: 9:01 ■ AM □ PM

Location: Corner of 2nd and 3rd

Describe the Incident: Red car t-boned blue car
_______________________________________________________
_______________________________________________________

INJURIES

Was anyone injured? □ Yes ■ No

If yes, describe the injuries: ________________________________________
_______________________________________________________________
_______________________________________________________________

WITNESSES

Were there witnesses to the incident? □ Yes ■ No

If yes, enter the witnesses' names and contact info: __________________________
_______________________________________________________________
_______________________________________________________________

Page 1 of 2
```

##  Complicated document QA

With Claude 3 we can go beyond just transcription and ask specific questions about our information in our unstructured documents.

Image(filename="../images/transcribe/page.jpeg")

![Output image](https://platform.claude.com/cookbook/images/notebooks/multimodal-how-to-transcribe-text/multimodal-how-to-transcribe-text_cell13_out0_bedb4922.jpeg)

message\_list = [

{

"role": "user",

"content": [

{

"type": "image",

"source": {

"type": "base64",

"media\_type": "image/jpeg",

"data": get\_base64\_encoded\_image("../images/transcribe/page.jpeg"),

},

},

{"type": "text", "text": "Which is the most critical issue for live rep support?"},

],

}

]

response = client.messages.create(model=MODEL\_NAME, max\_tokens=2048, messages=message\_list)

print(response.content[0].text)

```
According to the hierarchy of importance pyramid for Live Rep Support shown in the image, the most critical issue is Product Quality/Liability Issues. This is positioned at the very bottom of the pyramid, indicating it is the most critical or important issue for live rep support to handle.
```

##  Unstructured information -> JSON

Let's take a look at how you can use Claude to turn unstructured information in an image into a structured JSON output.

Image(filename="../images/transcribe/org\_chart.jpeg")

![Output image](https://platform.claude.com/cookbook/images/notebooks/multimodal-how-to-transcribe-text/multimodal-how-to-transcribe-text_cell16_out0_12c40e24.jpeg)

message\_list = [

{

"role": "user",

"content": [

{

"type": "image",

"source": {

"type": "base64",

"media\_type": "image/jpeg",

"data": get\_base64\_encoded\_image("../images/transcribe/org\_chart.jpeg"),

},

},

{

"type": "text",

"text": "Turn this org chart into JSON indicating who reports to who. Only output the JSON and nothing else.",

},

],

}

]

response = client.messages.create(model=MODEL\_NAME, max\_tokens=2048, messages=message\_list)

print(response.content[0].text)

```
{
  "President": {
    "name": "John Smith",
    "directReports": [
      {
        "name": "Susan Jones",
        "title": "VP Marketing",
        "directReports": [
          {
            "name": "Alice Johnson",
            "title": "Manager"
          },
          {
            "name": "Tim Moore",
            "title": "Manager"
          }
        ]
      },
      {
        "name": "Rachel Parker",
        "title": "VP Sales",
        "directReports": [
          {
            "name": "Michael Gross",
            "title": "Manager"
          },
          {
            "name": "Kim Dole",
            "title": "Manager"
          }
        ]
      },
      {
        "name": "Tom Allen",
        "title": "VP Production",
        "directReports": [
          {
            "name": "Kathy Roberts",
            "title": "Manager"
          },
          {
            "name": "Betsy Foster",
            "title": "Manager"
          }
        ]
      }
    ]
  }
}
```
