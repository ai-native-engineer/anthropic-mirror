<!-- source: https://platform.claude.com/cookbook/tool-use-calculator-tool -->

#  Using a Calculator Tool with Claude

In this recipe, we'll demonstrate how to provide Claude with a simple calculator tool that it can use to perform arithmetic operations based on user input. We'll define the calculator tool and show how Claude can interact with it to solve mathematical problems.

##  Step 1: Set up the environment

First, let's install the required libraries and set up the Claude API client.

%pip install anthropic

from anthropic import Anthropic

client = Anthropic()

MODEL\_NAME = "claude-opus-4-8"

##  Step 2: Define the calculator tool

We'll define a simple calculator tool that can perform basic arithmetic operations. The tool will take a mathematical expression as input and return the result.

Note that we are calling `eval` on the outputted expression. This is bad practice and should not be used generally but we are doing it for the purpose of demonstration.

import re

def calculate(expression):

# Remove any non-digit or non-operator characters from the expression

expression = re.sub(r"[^0-9+\-\*/().]", "", expression)

try:

# Evaluate the expression using the built-in eval() function

# Note: eval is used here for demonstration purposes only.

# In production, use a safer alternative like ast.literal\_eval or a math parser.

result = eval(expression) # noqa: S307

return str(result)

except (SyntaxError, ZeroDivisionError, NameError, TypeError, OverflowError):

return "Error: Invalid expression"

tools = [

{

"name": "calculator",

"description": "A simple calculator that performs basic arithmetic operations.",

"input\_schema": {

"type": "object",

"properties": {

"expression": {

"type": "string",

"description": "The mathematical expression to evaluate (e.g., '2 + 3 \* 4').",

}

},

"required": ["expression"],

},

}

]

In this example, we define a calculate function that takes a mathematical expression as input, removes any non-digit or non-operator characters using a regular expression, and then evaluates the expression using the built-in eval() function. If the evaluation is successful, the result is returned as a string. If an error occurs during evaluation, an error message is returned.

We then define the calculator tool with an input schema that expects a single expression property of type string.

##  Step 3: Interact with Claude

Now, let's see how Claude can interact with the calculator tool to solve mathematical problems.

def process\_tool\_call(tool\_name, tool\_input):

if tool\_name == "calculator":

return calculate(tool\_input["expression"])

def chat\_with\_claude(user\_message):

print(f"\n{'=' \* 50}\nUser Message: {user\_message}\n{'=' \* 50}")

message = client.messages.create(

model=MODEL\_NAME,

max\_tokens=4096,

messages=[{"role": "user", "content": user\_message}],

tools=tools,

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

tool\_result = process\_tool\_call(tool\_name, tool\_input)

print(f"Tool Result: {tool\_result}")

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

"content": tool\_result,

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

##  Step 4: Try it out!

Let's try giving Claude a few example math questions now that it has access to a calculator.

chat\_with\_claude("What is the result of 1,984,135 \* 9,343,116?")

chat\_with\_claude("Calculate (12851 - 593) \* 301 + 76")

chat\_with\_claude("What is 15910385 divided by 193053?")

```
==================================================
User Message: What is the result of 1,984,135 * 9,343,116?
==================================================

Initial Response:
Stop Reason: tool_use
Content: [ContentBlock(text='<thinking>\nThe calculator function is the relevant tool to answer this request, since it involves evaluating a mathematical expression.\n\nThe required parameter for the calculator function is:\nexpression: The mathematical expression to evaluate.\n\nThe human has directly provided the full expression to evaluate in their request: "1,984,135 * 9,343,116". This contains all the information needed for the required expression parameter.\n\nSo I have the necessary information to invoke the calculator tool.\n</thinking>', type='text'), ContentBlockToolUse(id='toolu_01V2mzqp5qkB5QucRFjJUJLD', input={'expression': '1984135 * 9343116'}, name='calculator', type='tool_use')]

Tool Used: calculator
Tool Input: {'expression': '1984135 * 9343116'}
Tool Result: 18538003464660
[ContentBlock(text='Therefore, the result of 1,984,135 * 9,343,116 is 18,538,003,464,660.', type='text')]

Final Response: Therefore, the result of 1,984,135 * 9,343,116 is 18,538,003,464,660.

==================================================
User Message: Calculate (12851 - 593) * 301 + 76
==================================================

Initial Response:
Stop Reason: tool_use
Content: [ContentBlock(text='<thinking>\nThe user has provided a mathematical expression to be evaluated: (12851 - 593) * 301 + 76\nThis can be handled by the calculator tool. Let\'s check if the required "expression" parameter is provided:\nexpression: "(12851 - 593) * 301 + 76" - This is directly provided by the user.\nSince the required parameter is present, we can proceed with calling the calculator tool.\n</thinking>', type='text'), ContentBlockToolUse(id='toolu_01Mrrfy9adBzzxvhfZwnyJAe', input={'expression': '(12851 - 593) * 301 + 76'}, name='calculator', type='tool_use')]

Tool Used: calculator
Tool Input: {'expression': '(12851 - 593) * 301 + 76'}
Tool Result: 3689734
[ContentBlock(text='So the final result of evaluating the expression (12851 - 593) * 301 + 76 is 3689734.', type='text')]

Final Response: So the final result of evaluating the expression (12851 - 593) * 301 + 76 is 3689734.

==================================================
User Message: What is 15910385 divided by 193053?
==================================================

Initial Response:
Stop Reason: tool_use
Content: [ContentBlock(text='<thinking>\nThe calculator function is the appropriate tool to answer this request, since it can perform basic arithmetic operations like division.\n\nThe calculator function requires a single parameter:\n- expression: The mathematical expression to evaluate\n\nIn this case, the user has provided the full expression to evaluate (15910385 divided by 193053). Since all the required information has been provided, we can proceed with calling the calculator function.\n</thinking>', type='text'), ContentBlockToolUse(id='toolu_01BfnN4LKp7oPRgmRzWeYdBG', input={'expression': '15910385 / 193053'}, name='calculator', type='tool_use')]

Tool Used: calculator
Tool Input: {'expression': '15910385 / 193053'}
Tool Result: 82.41459599177428
[ContentBlock(text='So 15910385 divided by 193053 equals 82.41459599177428.', type='text')]

Final Response: So 15910385 divided by 193053 equals 82.41459599177428.

'So 15910385 divided by 193053 equals 82.41459599177428.'
```
