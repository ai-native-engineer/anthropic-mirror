<!-- source: https://platform.claude.com/cookbook/tool-use-tool-use-with-pydantic -->

#  Note-Saving Tool with Pydantic and Anthropic Tool Use

In this example, we'll create a tool that saves a note with the author and metadata, and use Pydantic to validate the model's response when calling the tool. We'll define the necessary Pydantic models, process the tool call, and ensure that the model's response conforms to the expected schema.

##  Step 1: Set up the environment

First, let's install the required libraries and set up the Claude API client.

%pip install anthropic pydantic 'pydantic[email]'

from anthropic import Anthropic

from pydantic import BaseModel, EmailStr, Field

client = Anthropic()

MODEL\_NAME = "claude-opus-4-8"

##  Step 2: Define the Pydantic models

We'll define Pydantic models to represent the expected schema for the note, author, and the model's response. This will allow us to validate and type-check the model's response when saving a note.

class Author(BaseModel):

name: str

email: EmailStr

class Note(BaseModel):

note: str

author: Author

tags: list[str] | None = None

priority: int = Field(ge=1, le=5, default=3)

is\_public: bool = False

class SaveNoteResponse(BaseModel):

success: bool

message: str

##  Step 3: Define the client-side tool

Next, we'll define the client-side tool that our chatbot will use to save notes.

tools = [

{

"name": "save\_note",

"description": "A tool that saves a note with the author and metadata.",

"input\_schema": {

"type": "object",

"properties": {

"note": {"type": "string", "description": "The content of the note to be saved."},

"author": {

"type": "object",

"properties": {

"name": {"type": "string", "description": "The name of the author."},

"email": {

"type": "string",

"format": "email",

"description": "The email address of the author.",

},

},

"required": ["name", "email"],

},

"priority": {

"type": "integer",

"minimum": 1,

"maximum": 5,

"default": 3,

"description": "The priority level of the note (1-5).",

},

"is\_public": {

"type": "boolean",

"default": False,

"description": "Indicates whether the note is publicly accessible.",

},

},

"required": ["note", "author"],

},

}

]

##  Step 4: Implement the note-saving tool

We'll create a dummy note saving function that just prints out that the note was saved successfully. If you actually want this note to be saved somewhere, you can implement this function.

def save\_note(note: str, author: dict, priority: int = 3, is\_public: bool = False) -> None:

print("Note saved successfully!")

##  Step 5: Process the tool call and generate the response

We'll create functions to process the tool call made by Claude and generate the response indicating the success of saving the note.

def process\_tool\_call(tool\_name, tool\_input):

if tool\_name == "save\_note":

note = Note(

note=tool\_input["note"],

author=Author(name=tool\_input["author"]["name"], email=tool\_input["author"]["email"]),

priority=tool\_input.get("priority", 3),

is\_public=tool\_input.get("is\_public", False),

)

save\_note(note.note, note.author.model\_dump(), note.priority, note.is\_public)

return SaveNoteResponse(success=True, message="Note saved successfully!")

def generate\_response(save\_note\_response):

return f"Response: {save\_note\_response.message}"

##  Step 6: Interact with the chatbot

Now, let's create a function to interact with the chatbot. We'll send a user message, process the tool call made by Claude, generate the response, validate the model's response using Pydantic, and return the final response to the user.

def chatbot\_interaction(user\_message):

print(f"\n{'=' \* 50}\nUser Message: {user\_message}\n{'=' \* 50}")

messages = [{"role": "user", "content": user\_message}]

message = client.messages.create(

model=MODEL\_NAME, max\_tokens=4096, tools=tools, messages=messages

)

print("\nInitial Response:")

print(f"Stop Reason: {message.stop\_reason}")

print(f"Content: {message.content}")

if message.stop\_reason == "tool\_use":

tool\_use = next(block for block in message.content if block.type == "tool\_use")

tool\_name = tool\_use.name

tool\_input = tool\_use.input

print(f"\nTool Used: {tool\_name}")

print(f"Tool Input: {tool\_input}")

save\_note\_response = process\_tool\_call(tool\_name, tool\_input)

print(f"Tool Result: {save\_note\_response}")

response = client.messages.create(

model=MODEL\_NAME,

max\_tokens=4096,

messages=[

{"role": "user", "content": user\_message},

{"role": "assistant", "content": message.content},

{

"role": "user",

"content": [

{

"type": "tool\_result",

"tool\_use\_id": tool\_use.id,

"content": str(save\_note\_response),

}

],

},

],

tools=tools,

)

else:

response = message

final\_response = next(

(block.text for block in response.content if hasattr(block, "text")),

None,

)

print(response.content)

print(f"\nFinal Response: {final\_response}")

return final\_response

##  Step 7: Test the chatbot

Let's test our chatbot with a sample query to save a note.

chatbot\_interaction("""

Can you save a private note with the following details?

Note: Remember to buy milk and eggs.

Author: John Doe (johndoe@gmail.com)

Priority: 4

""")

```
==================================================
User Message:
Can you save a private note with the following details?
Note: Remember to buy milk and eggs.
Author: John Doe (johndoe@gmail.com)
Priority: 4

==================================================

Initial Response:
Stop Reason: tool_use
Content: [ContentBlock(text='<thinking>\nThe relevant tool to use here is save_note, as the request is to save a note with specific details.\n\nLet\'s go through the parameters one-by-one:\n\nnote: The user provided the note content: "Remember to buy milk and eggs."\nauthor: The user provided the author details: \n{\n  "name": "John Doe",\n  "email": "johndoe@gmail.com"\n}\nis_public: While the user didn\'t explicitly specify, they asked for a "private note", so we can infer is_public should be false.\npriority: The user specified a priority of 4.\n\nAll the required parameters have been provided or can be reasonably inferred from the request. We have enough information to make the save_note call.\n</thinking>', type='text'), ContentBlockToolUse(id='toolu_015iteV2eC1C7aUodbkotfiS', input={'note': 'Remember to buy milk and eggs.', 'author': {'name': 'John Doe', 'email': 'johndoe@gmail.com'}, 'is_public': False, 'priority': 4}, name='save_note', type='tool_use')]

Tool Used: save_note
Tool Input: {'note': 'Remember to buy milk and eggs.', 'author': {'name': 'John Doe', 'email': 'johndoe@gmail.com'}, 'is_public': False, 'priority': 4}
Note saved successfully!
Tool Result: success=True message='Note saved successfully!'
[ContentBlock(text='Your private note has been saved successfully with the following details:\n\nNote: Remember to buy milk and eggs. \nAuthor: John Doe (johndoe@gmail.com)\nPriority: 4\nVisibility: Private\n\nPlease let me know if you need anything else!', type='text')]

Final Response: Your private note has been saved successfully with the following details:

Note: Remember to buy milk and eggs.
Author: John Doe (johndoe@gmail.com)
Priority: 4
Visibility: Private

Please let me know if you need anything else!

'Your private note has been saved successfully with the following details:\n\nNote: Remember to buy milk and eggs. \nAuthor: John Doe (johndoe@gmail.com)\nPriority: 4\nVisibility: Private\n\nPlease let me know if you need anything else!'
```

In this example, we've created a tool that saves a note with the author and metadata. The chatbot uses the save\_note tool to save the note, and Pydantic is used to validate the model's response when calling the tool. The Note, Author, and SaveNoteResponse models ensure that the tool input and the model's response conform to the expected schema.

By defining clear Pydantic models and using them to validate the model's response, we add an extra layer of reliability and safety when interacting with the chatbot and saving notes.
