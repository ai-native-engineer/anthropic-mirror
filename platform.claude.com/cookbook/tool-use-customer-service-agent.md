<!-- source: https://platform.claude.com/cookbook/tool-use-customer-service-agent -->

#  Creating a Customer Service Agent with Client-Side Tools

In this recipe, we'll demonstrate how to create a customer service chatbot using Claude 3 plus client-side tools. The chatbot will be able to look up customer information, retrieve order details, and cancel orders on behalf of the customer. We'll define the necessary tools and simulate synthetic responses to showcase the chatbot's capabilities.

##  Step 1: Set up the environment

First, let's install the required libraries and set up the Claude API client.

%pip install anthropic

import anthropic

client = anthropic.Client()

MODEL\_NAME = "claude-opus-4-8"

##  Step 2: Define the client-side tools

Next, we'll define the client-side tools that our chatbot will use to assist customers. We'll create three tools: get\_customer\_info, get\_order\_details, and cancel\_order.

tools = [

{

"name": "get\_customer\_info",

"description": "Retrieves customer information based on their customer ID. Returns the customer's name, email, and phone number.",

"input\_schema": {

"type": "object",

"properties": {

"customer\_id": {

"type": "string",

"description": "The unique identifier for the customer.",

}

},

"required": ["customer\_id"],

},

},

{

"name": "get\_order\_details",

"description": "Retrieves the details of a specific order based on the order ID. Returns the order ID, product name, quantity, price, and order status.",

"input\_schema": {

"type": "object",

"properties": {

"order\_id": {

"type": "string",

"description": "The unique identifier for the order.",

}

},

"required": ["order\_id"],

},

},

{

"name": "cancel\_order",

"description": "Cancels an order based on the provided order ID. Returns a confirmation message if the cancellation is successful.",

"input\_schema": {

"type": "object",

"properties": {

"order\_id": {

"type": "string",

"description": "The unique identifier for the order to be cancelled.",

}

},

"required": ["order\_id"],

},

},

]

##  Step 3: Simulate synthetic tool responses

Since we don't have real customer data or order information, we'll simulate synthetic responses for our tools. In a real-world scenario, these functions would interact with your actual customer database and order management system.

def get\_customer\_info(customer\_id):

# Simulated customer data

customers = {

"C1": {"name": "John Doe", "email": "john@example.com", "phone": "123-456-7890"},

"C2": {"name": "Jane Smith", "email": "jane@example.com", "phone": "987-654-3210"},

}

return customers.get(customer\_id, "Customer not found")

def get\_order\_details(order\_id):

# Simulated order data

orders = {

"O1": {

"id": "O1",

"product": "Widget A",

"quantity": 2,

"price": 19.99,

"status": "Shipped",

},

"O2": {

"id": "O2",

"product": "Gadget B",

"quantity": 1,

"price": 49.99,

"status": "Processing",

},

}

return orders.get(order\_id, "Order not found")

def cancel\_order(order\_id):

# Simulated order cancellation

if order\_id in ["O1", "O2"]:

return True

else:

return False

##  Step 4: Process tool calls and return results

We'll create a function to process the tool calls made by Claude and return the appropriate results.

def process\_tool\_call(tool\_name, tool\_input):

if tool\_name == "get\_customer\_info":

return get\_customer\_info(tool\_input["customer\_id"])

elif tool\_name == "get\_order\_details":

return get\_order\_details(tool\_input["order\_id"])

elif tool\_name == "cancel\_order":

return cancel\_order(tool\_input["order\_id"])

##  Step 5: Interact with the chatbot

Now, let's create a function to interact with the chatbot. We'll send a user message, process any tool calls made by Claude, and return the final response to the user.

import json

def chatbot\_interaction(user\_message):

print(f"\n{'=' \* 50}\nUser Message: {user\_message}\n{'=' \* 50}")

messages = [{"role": "user", "content": user\_message}]

response = client.messages.create(

model=MODEL\_NAME, max\_tokens=4096, tools=tools, messages=messages

)

print("\nInitial Response:")

print(f"Stop Reason: {response.stop\_reason}")

print(f"Content: {response.content}")

while response.stop\_reason == "tool\_use":

tool\_use = next(block for block in response.content if block.type == "tool\_use")

tool\_name = tool\_use.name

tool\_input = tool\_use.input

print(f"\nTool Used: {tool\_name}")

print("Tool Input:")

print(json.dumps(tool\_input, indent=2))

tool\_result = process\_tool\_call(tool\_name, tool\_input)

print("\nTool Result:")

print(json.dumps(tool\_result, indent=2))

messages = [

{"role": "user", "content": user\_message},

{"role": "assistant", "content": response.content},

{

"role": "user",

"content": [

{

"type": "tool\_result",

"tool\_use\_id": tool\_use.id,

"content": str(tool\_result),

}

],

},

]

response = client.messages.create(

model=MODEL\_NAME, max\_tokens=4096, tools=tools, messages=messages

)

print("\nResponse:")

print(f"Stop Reason: {response.stop\_reason}")

print(f"Content: {response.content}")

final\_response = next(

(block.text for block in response.content if hasattr(block, "text")),

None,

)

print(f"\nFinal Response: {final\_response}")

return final\_response

##  Step 6: Test the chatbot

Let's test our customer service chatbot with a few sample queries.

chatbot\_interaction("Can you tell me the email address for customer C1?")

chatbot\_interaction("What is the status of order O2?")

chatbot\_interaction("Please cancel order O1 for me.")

```
==================================================
User Message: Can you tell me the email address for customer C1?
==================================================

Initial Response:
Stop Reason: tool_use
Content: [ContentBlock(text='<thinking>The get_customer_info function retrieves a customer\'s name, email, and phone number given their customer ID. To call this function, I need the customer_id parameter. The user provided the customer ID "C1" in their request, so I have the necessary information to make the API call.</thinking>', type='text'), ContentBlockToolUse(id='toolu_019F9JHokMkJ1dHw5BEh28sA', input={'customer_id': 'C1'}, name='get_customer_info', type='tool_use')]

Tool Used: get_customer_info
Tool Input:
{
  "customer_id": "C1"
}

Tool Result:
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "123-456-7890"
}

Response:
Stop Reason: end_turn
Content: [ContentBlock(text='The email address for customer C1 (John Doe) is john@example.com.', type='text')]

Final Response: The email address for customer C1 (John Doe) is john@example.com.

==================================================
User Message: What is the status of order O2?
==================================================

Initial Response:
Stop Reason: tool_use
Content: [ContentBlock(text='<thinking>\nBased on the provided functions, the most relevant one for this request is get_order_details, which takes an order_id parameter and returns details about that specific order, including the order status.\n\nThe user has provided an order ID in their request - "O2". So the required order_id parameter can be filled with this value.\n\nSince the required parameter is available, I can proceed with calling the get_order_details function to retrieve the order status for order O2.\n</thinking>', type='text'), ContentBlockToolUse(id='toolu_01K1u68uC94edXx8MVT35eR3', input={'order_id': 'O2'}, name='get_order_details', type='tool_use')]

Tool Used: get_order_details
Tool Input:
{
  "order_id": "O2"
}

Tool Result:
{
  "id": "O2",
  "product": "Gadget B",
  "quantity": 1,
  "price": 49.99,
  "status": "Processing"
}

Response:
Stop Reason: end_turn
Content: [ContentBlock(text='Based on the details returned from the get_order_details function, the status of order O2 is "Processing".', type='text')]

Final Response: Based on the details returned from the get_order_details function, the status of order O2 is "Processing".

==================================================
User Message: Please cancel order O1 for me.
==================================================

Initial Response:
Stop Reason: tool_use
Content: [ContentBlock(text='<thinking>\nThe relevant tool to cancel an order is the cancel_order function. \nThis function requires an order_id parameter.\nThe user provided the order ID "O1" in their request, so we have the necessary parameter to call the cancel_order function.\n</thinking>', type='text'), ContentBlockToolUse(id='toolu_01W3ZkP2QCrjHf5bKM6wvT2s', input={'order_id': 'O1'}, name='cancel_order', type='tool_use')]

Tool Used: cancel_order
Tool Input:
{
  "order_id": "O1"
}

Tool Result:
true

Response:
Stop Reason: end_turn
Content: [ContentBlock(text='Based on the confirmation received, your order O1 has been successfully cancelled. Please let me know if there is anything else I can assist you with.', type='text')]

Final Response: Based on the confirmation received, your order O1 has been successfully cancelled. Please let me know if there is anything else I can assist you with.

'Based on the confirmation received, your order O1 has been successfully cancelled. Please let me know if there is anything else I can assist you with.'
```

And that's it! We've created a customer service chatbot using Claude 3 models and client-side tools. The chatbot can look up customer information, retrieve order details, and cancel orders based on the user's requests. By defining clear tool descriptions and schemas, we enable Claude to effectively understand and utilize the available tools to assist customers.

Feel free to expand on this example by integrating with your actual customer database and order management system, and by adding more tools to handle a wider range of customer service tasks.
