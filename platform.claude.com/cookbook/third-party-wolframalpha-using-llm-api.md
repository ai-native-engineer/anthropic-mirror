<!-- source: https://platform.claude.com/cookbook/third-party-wolframalpha-using-llm-api -->

#  Using the Wolfram Alpha LLM API as a Tool with Claude

In this recipe, we'll show you how to integrate the Wolfram Alpha LLM API as a tool for Claude to use. Claude will be able to send queries to the Wolfram Alpha API and receive computed responses, which it can then use to provide answers to user questions.

##  Step 1: Set up the environment

First, let's install the required libraries and set up the Claude API client. We also will need to set our APP ID for using WolframAlpha. You can sign up and create a new App ID for this project for free [here(opens in new tab)](https://developer.wolframalpha.com/access).



import json

import urllib.parse

import requests

from anthropic import Anthropic

client = Anthropic()

# Replace 'YOUR\_APP\_ID' with your actual Wolfram Alpha AppID

WOLFRAM\_APP\_ID = "YOUR\_APP\_ID"

MODEL\_NAME = "claude-haiku-4-5"

##  Step 2: Define the Wolfram Alpha LLM API tool

We'll define a tool that allows Claude to send queries to the Wolfram Alpha LLM API and receive the computed response.



import urllib.parse

import requests

def wolfram\_alpha\_query(query):

# URL-encode the query

encoded\_query = urllib.parse.quote(query)

# Make a request to the Wolfram Alpha LLM API

url = (

f"https://www.wolframalpha.com/api/v1/llm-api?input={encoded\_query}&appid={WOLFRAM\_APP\_ID}"

)

response = requests.get(url, timeout=30)

if response.status\_code == 200:

return response.text

else:

return f"Error: {response.status\_code}: {response.text}"

tools = [

{

"name": "wolfram\_alpha",

"description": "A tool that allows querying the Wolfram Alpha knowledge base. Useful for mathematical calculations, scientific data, and general knowledge questions.",

"input\_schema": {

"type": "object",

"properties": {

"search\_query": {

"type": "string",

"description": "The query to send to the Wolfram Alpha API.",

}

},

"required": ["query"],

},

}

]

In this code, we define a wolfram\_alpha\_query function that takes a query as input, URL-encodes it, and sends a request to the Wolfram Alpha LLM API using the provided AppID. The function returns the computed response from the API if the request is successful, or an error message if there's an issue.

We then define the wolfram\_alpha tool with an input schema that expects a single query property of type string.

##  Step 3: Interact with Claude

Now, let's see how Claude can interact with the Wolfram Alpha tool to answer user questions.



def process\_tool\_call(tool\_name, tool\_input):

if tool\_name == "wolfram\_alpha":

return wolfram\_alpha\_query(tool\_input["search\_query"])

def chat\_with\_claude(user\_message):

print(f"\n{'=' \* 50}\nUser Message: {user\_message}\n{'=' \* 50}")

prompt = f"""Here is a question: {user\_message}. Please use the Wolfram Alpha tool to answer it. Do not reflect on the quality of the returned search results in your response."""

message = client.beta.tools.messages.create(

model=MODEL\_NAME,

max\_tokens=4096,

tools=tools,

messages=[{"role": "user", "content": prompt}],

)

print("\nInitial Response:")

print(f"Stop Reason: {message.stop\_reason}")

print(f"Content: {message.content}")

if message.stop\_reason == "tool\_use":

tool\_use = next(block for block in message.content if block.type == "tool\_use")

tool\_name = tool\_use.name

tool\_input = tool\_use.input

print(f"\nTool Used: {tool\_name}")

print("Tool Input:")

print(json.dumps(tool\_input, indent=2))

tool\_result = process\_tool\_call(tool\_name, tool\_input)

print("\nTool Result:")

print(str(json.dumps(tool\_result, indent=2)))

response = client.beta.tools.messages.create(

model=MODEL\_NAME,

max\_tokens=2000,

tools=tools,

messages=[

{"role": "user", "content": prompt},

{"role": "assistant", "content": message.content},

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

],

)

print("\nResponse:")

print(f"Stop Reason: {response.stop\_reason}")

print(f"Content: {response.content}")

else:

response = message

final\_response = None

for block in response.content:

if hasattr(block, "text"):

final\_response = block.text

break

print(f"\nFinal Response: {final\_response}")

return final\_response

##  Step 4: Try it out!

Let's try giving Claude a few example questions now that it has access to Wolfram Alpha.



# Example usage

print(chat\_with\_claude("What are the 5 largest countries in the world by population?"))

print(chat\_with\_claude("Calculate the square root of 1764."))

print(chat\_with\_claude("What is the distance between Earth and Mars?"))



```
==================================================
User Message: What are the 5 largest countries in the world by population?
==================================================

Initial Response:
Stop Reason: tool_use
Content: [ContentBlock(text='<thinking>\nThe query "What are the 5 largest countries in the world by population?" can be answered well using the wolfram_alpha tool, which has knowledge about countries and populations. The search_query parameter is the only required parameter, and the query text provided by the user can be used directly as the search_query value without any additional information needed. \n</thinking>', type='text'), ContentBlockToolUse(id='toolu_01VCQ5xAzMNdyXYsepbSAJLY', input={'search_query': 'What are the 5 largest countries in the world by population?'}, name='wolfram_alpha', type='tool_use')]

Tool Used: wolfram_alpha
Tool Input:
{
  "search_query": "What are the 5 largest countries in the world by population?"
}

Tool Result:
"Query:\n\"What are the 5 largest countries in the world by population?\"\n\nInput interpretation:\n5 largest countries | by population\nin all countries, dependencies, and territories\n\nResult:\n1 | India | 1.43 billion people | \n2 | China | 1.43 billion people | \n3 | United States | 340 million people | \n4 | Indonesia | 278 million people | \n5 | Pakistan | 241 million people | \n\nNames:\n | full name | full native name\nIndia | Republic of India | Bh\u0101rat\u012bya Ga\u1e47ar\u0101jya\nChina | People's Republic of China | Zhonghua Renmin Gongheguo\nUnited States | United States of America | \nIndonesia | Republic of Indonesia | Republik Indonesia\nPakistan | Islamic Republic of Pakistan | Isl\u0101m\u012b Jumh\u016br\u012b-ye P\u0101kist\u0101n\n\nFlags:\nimage: https://www6b3.wolframalpha.com/Calculate/MSP/MSP2444241bhh00e1he97fd0000383004g53722f9bd?MSPStoreType=image/png&s=14\nWolfram Language code: Dataset[EntityValue[{Entity[\"Country\", \"India\"], Entity[\"Country\", \"China\"], Entity[\"Country\", \"UnitedStates\"], Entity[\"Country\", \"Indonesia\"], Entity[\"Country\", \"Pakistan\"]}, EntityProperty[\"Country\", \"Flag\"], \"EntityAssociation\"]]\n\nLocations:\nimage: https://www6b3.wolframalpha.com/Calculate/MSP/MSP2445241bhh00e1he97fd00002684a23aaahea47d?MSPStoreType=image/png&s=14\n\nGeographic properties:\ntotal area | total | 9.736 million mi^2 (square miles)\n | largest | 3.719 million mi^2 (square miles) (world rank: 3rd) (United States)\n | smallest | 307374 mi^2 (square miles) (world rank: 36th) (Pakistan)\nland area | total | 9.283 million mi^2 (square miles)\n | largest | 3.601 million mi^2 (square miles) (world rank: 2nd) (China)\n | smallest | 297637 mi^2 (square miles) (world rank: 36th) (Pakistan)\ncontinent | all | Asia | North America\n\nDemographics:\npopulation | total | 3.71 billion people\n | highest | 1.43 billion people (world rank: 1st) (2023 estimate) (India)\n | lowest | 241 million people (world rank: 5th) (2023 estimate) (Pakistan)\npopulation density | average | 390 people/mi^2\n | median | 385 people/mi^2\n | highest | 1226 people/mi^2 (world rank: 31st) (2021 estimate) (India)\n | lowest | 95.4 people/mi^2 (world rank: 183rd) (2021 estimate) (United States)\npopulation growth | average | 0.455 %/yr\n | median | 0.631 %/yr\n | highest | 1.83 %/yr (world rank: 56th) (2021 estimate) (Pakistan)\n | lowest | 0.004 %/yr (world rank: 188th) (2021 estimate) (China)\nlife expectancy | mean | 73 yr\n | median | 71.9 yr\n | highest | 78.9 yr (world rank: 66th) (2020 estimate) (United States)\n | lowest | 67.4 yr (world rank: 186th) (2020 estimate) (Pakistan)\nmedian age | median | 29.4 yr\n | highest | 37.9 yr (world rank: 70th) (2021 estimate) (China)\n | lowest | 20.2 yr (world rank: 191st) (2021 estimate) (Pakistan)\n\nCapital cities:\nIndia | New Delhi, Delhi\nChina | Beijing\nUnited States | Washington, District of Columbia\nIndonesia | Jakarta\nPakistan | Islamabad, F.C.T.\n\nEconomic properties:\nGDP | total | $48.51 trillion per year\n | median | $3.385 trillion per year\n | highest | $25.46 trillion per year (world rank: 1st) (2022 estimates) (United States)\n | lowest | $376.5 billion per year (world rank: 43rd) (2022 estimates) (Pakistan)\nGDP at parity | total | $73.22 trillion per year\n | median | $11.87 trillion per year\n | highest | $30.33 trillion per year (world rank: 1st) (2022 estimates) (China)\n | lowest | $1.518 trillion per year (world rank: 22nd) (2022 estimates) (Pakistan)\nreal GDP | total | $41.72 trillion per year\n | median | $2.955 trillion per year\n | highest | $20.95 trillion per year (world rank: 1st) (2022 estimates) (United States)\n | lowest | $362.2 billion per year (world rank: 37th) (2022 estimates) (Pakistan)\nGDP per capita | average | $13203 per year per person\n | median | $4788 per year per person\n | highest | $76399 per year per person (world rank: 12th) (2022 estimates) (United States)\n | lowest | $1597 per year per person (world rank: 197th) (2022 estimates) (Pakistan)\nGDP real growth | mean | +4.71% per year\n | median | +5.309% per year\n | highest | +7.003% per year (world rank: 38th) (2022 estimates) (India)\n | lowest | +2.062% per year (world rank: 157th) (2022 estimates) (United States)\nGini index | median | 0.371\n | highest | 0.398 (world rank: 102nd) (2018, 2020, 2021, and 2022 estimates) (United States)\n | lowest | 0.296 (world rank: 24th) (2018, 2020, 2021, and 2022 estimates) (Pakistan)\n | distribution | \nconsumer price inflation | mean | +8.15% per year\n | median | +6.7% per year\n | highest | +19.87% per year (world rank: 21st) (2022 estimates) (Pakistan)\n | lowest | +1.97% per year (world rank: 175th) (2022 estimates) (China)\n\nEmployment:\nunemployment rate | mean | 5.16%\n | median | 4.89%\n | highest | 7.33% (world rank: 74th highest) (2022 estimates) (India)\n | lowest | 3.55% (world rank: 162nd highest) (2022 estimates) (Indonesia)\nlong-term unemployment rate | mean | 1.57%\n | median | 1.42%\n | highest | 3.18% (world rank: 44th highest) (2010 and 2014 estimates) (India)\n | lowest | 0.127% (world rank: 111th highest) (2010 and 2014 estimates) (Pakistan)\nlabor force | highest | 781.8 million people (58.24% of population) (world rank: 1st) (2022 estimates) (China)\n | lowest | 78.91 million people (35.22% of population) (world rank: 6th) (2022 estimates) (Pakistan)\n | distribution | \neconomically active children | median | 3.7%\n | highest | 13% (world rank: 50th) (2010, 2011, and 2012 estimates) (Pakistan)\n | lowest | 1.7% (world rank: 90th) (2010, 2011, and 2012 estimates) (India)\n\nUN Human Development Index:\n | India | China | United States | Indonesia | Pakistan\nhealth | 0.743 (world rank: 131st) | 0.861 (world rank: 58th) | 0.911 (world rank: 36th) | 0.755 (world rank: 126th) | 0.713 (world rank: 137th)\neducation | 0.535 (world rank: 131st) | 0.631 (world rank: 108th) | 0.9 (world rank: 8th) | 0.622 (world rank: 112th) | 0.395 (world rank: 169th)\nliving standards | 0.61 (world rank: 126th) | 0.739 (world rank: 82nd) | 0.948 (world rank: 11th) | 0.696 (world rank: 103rd) | 0.592 (world rank: 133rd)\ntotal | 0.624 (world rank: 131st) | 0.738 (world rank: 90th) | 0.92 (world rank: 10th) | 0.689 (world rank: 113th) | 0.55 (world rank: 147th)\n(2015 estimate)\n\nWikipedia page hits history:\nimage: https://www6b3.wolframalpha.com/Calculate/MSP/MSP2448241bhh00e1he97fd00006a6g1ee3gbhghh18?MSPStoreType=image/png&s=14\n\nWolfram|Alpha website result for \"What are the 5 largest countries in the world by population?\":\nhttps://www6b3.wolframalpha.com/input?i=What+are+the+5+largest+countries+in+the+world+by+population%3F"

Response:
Stop Reason: end_turn
Content: [ContentBlock(text='According to Wolfram Alpha, the 5 largest countries in the world by population are:\n\n1. India - 1.43 billion people\n2. China - 1.43 billion people \n3. United States - 340 million people\n4. Indonesia - 278 million people\n5. Pakistan - 241 million people\n\nTogether these 5 countries account for about 3.71 billion people. India and China have the largest populations, each with around 1.43 billion people. The United States has the 3rd largest population at 340 million. Indonesia and Pakistan round out the top 5 with 278 million and 241 million people respectively.', type='text')]

Final Response: According to Wolfram Alpha, the 5 largest countries in the world by population are:

1. India - 1.43 billion people
2. China - 1.43 billion people
3. United States - 340 million people
4. Indonesia - 278 million people
5. Pakistan - 241 million people

Together these 5 countries account for about 3.71 billion people. India and China have the largest populations, each with around 1.43 billion people. The United States has the 3rd largest population at 340 million. Indonesia and Pakistan round out the top 5 with 278 million and 241 million people respectively.
According to Wolfram Alpha, the 5 largest countries in the world by population are:

1. India - 1.43 billion people
2. China - 1.43 billion people
3. United States - 340 million people
4. Indonesia - 278 million people
5. Pakistan - 241 million people

Together these 5 countries account for about 3.71 billion people. India and China have the largest populations, each with around 1.43 billion people. The United States has the 3rd largest population at 340 million. Indonesia and Pakistan round out the top 5 with 278 million and 241 million people respectively.

==================================================
User Message: Calculate the square root of 1764.
==================================================

Initial Response:
Stop Reason: tool_use
Content: [ContentBlock(text='<thinking>\nThe relevant tool to use for this query is wolfram_alpha, since the question is asking for a mathematical calculation. The wolfram_alpha tool takes a single required parameter:\nsearch_query: The query to send to the Wolfram Alpha API\n\nThe user\'s request directly provides the search query needed, which is "square root of 1764". So all the required parameters are available to make the API call.\n</thinking>', type='text'), ContentBlockToolUse(id='toolu_011CkyJcwahqGaL513uFhdYJ', input={'search_query': 'square root of 1764'}, name='wolfram_alpha', type='tool_use')]

Tool Used: wolfram_alpha
Tool Input:
{
  "search_query": "square root of 1764"
}

Tool Result:
"Query:\n\"square root of 1764\"\n\nInput:\nsqrt(1764)\n\nResult:\n42\n\nNumber line:\nimage: https://www6b3.wolframalpha.com/Calculate/MSP/MSP191312396298479fhh7a0000212h885f5h3d6gig?MSPStoreType=image/png&s=4\nWolfram Language code: NumberLinePlot[42]\n\nNumber name:\nforty-two\n\nAll 2nd roots of 1764:\n42 e^0 = 42 (real, principal root)\n\n42 e^(i \u03c0) = -42 (real root)\n\nPlot of all roots in the complex plane:\nimage: https://www6b3.wolframalpha.com/Calculate/MSP/MSP191412396298479fhh7a0000282bg11dc3e822ca?MSPStoreType=image/png&s=4\n\nWolfram|Alpha website result for \"square root of 1764\":\nhttps://www6b3.wolframalpha.com/input?i=square+root+of+1764"

Response:
Stop Reason: end_turn
Content: [ContentBlock(text='So the square root of 1764 is 42.', type='text')]

Final Response: So the square root of 1764 is 42.
So the square root of 1764 is 42.

==================================================
User Message: What is the distance between Earth and Mars?
==================================================

Initial Response:
Stop Reason: tool_use
Content: [ContentBlock(text='<thinking>\nThe wolfram_alpha tool is the relevant tool for answering this question about the distance between Earth and Mars, as it can provide scientific data like astronomical distances.\nThe search_query parameter can be filled in directly with the user\'s question "What is the distance between Earth and Mars?". No additional information is needed to fill the parameter.\nSince the search_query parameter is provided, the function can be called to answer the question.\n</thinking>', type='text'), ContentBlockToolUse(id='toolu_01PotM7Z1ooJ1PdK8QK1WgEu', input={'search_query': 'What is the distance between Earth and Mars?'}, name='wolfram_alpha', type='tool_use')]

Tool Used: wolfram_alpha
Tool Input:
{
  "search_query": "What is the distance between Earth and Mars?"
}

Tool Result:
"Query:\n\"What is the distance between Earth and Mars?\"\n\nInput interpretation:\nMars | distance from Earth\n\nCurrent result:\n2.078 au (astronomical units)\n\nHistory:\nimage: https://www6b3.wolframalpha.com/Calculate/MSP/MSP101d6f8bccif83bf9800004259ii3cbcih744h?MSPStoreType=image/png&s=19\n\nUnit conversions:\n3.109\u00d710^8 km (kilometers)\n\n3.109\u00d710^11 meters\n\n193.2 million miles\n\nComparisons as distance:\n \u2248 ( 0.024 \u2248 1/42 ) \u00d7 smallest distance from the Sun to the heliosheath ( 79 to 100 au )\n\n \u2248 2.1 \u00d7 mean Earth-Sun distance ( 1.0000010178 au )\n\nCorresponding quantities:\nLight travel time t in vacuum from t = x/c:\n | 17 minutes\n\nLight travel time t in an optical fiber t = 1.48x/c:\n | 26 minutes\n\nSolar radiation pressure from P = L_\u2609/(c4\u03c0r^2):\n | 1.1 \u03bcPa (micropascals)\n | (assuming solar constant \u2248 1.36 kW/m^2)\n\nOrbital properties:\ncurrent distance from Earth | 2.078 au\n17.29 light minutes\naverage distance from Earth | 1.7 au\n14.1 light minutes\ncurrent distance from Sun | 1.39 au\n11.56 light minutes\nlargest distance from Sun | 154.863553 million mi\n1.66599116 au\nsmallest distance from Sun | 128.402967 million mi\n1.38133346 au\norbital period | 1.8808476 a\n\nWolfram|Alpha website result for \"What is the distance between Earth and Mars?\":\nhttps://www6b3.wolframalpha.com/input?i=What+is+the+distance+between+Earth+and+Mars%3F"

Response:
Stop Reason: end_turn
Content: [ContentBlock(text='The current distance between Earth and Mars is 2.078 astronomical units (au), which is equivalent to 3.109×10^8 km or 193.2 million miles. \n\nThe average distance between the two planets is about 1.7 au or 140 million miles.\n\nMars orbits the Sun at an average distance of 1.52 au, ranging from a minimum of 1.38 au to a maximum of 1.67 au. Its orbital period is 1.88 Earth years.\n\nAt the current Earth-Mars distance of 2.078 au, light takes about 17 minutes to travel between the two planets. The solar radiation pressure at that distance is approximately 1.1 μPa (micropascals).', type='text')]

Final Response: The current distance between Earth and Mars is 2.078 astronomical units (au), which is equivalent to 3.109×10^8 km or 193.2 million miles.

The average distance between the two planets is about 1.7 au or 140 million miles.

Mars orbits the Sun at an average distance of 1.52 au, ranging from a minimum of 1.38 au to a maximum of 1.67 au. Its orbital period is 1.88 Earth years.

At the current Earth-Mars distance of 2.078 au, light takes about 17 minutes to travel between the two planets. The solar radiation pressure at that distance is approximately 1.1 μPa (micropascals).
The current distance between Earth and Mars is 2.078 astronomical units (au), which is equivalent to 3.109×10^8 km or 193.2 million miles.

The average distance between the two planets is about 1.7 au or 140 million miles.

Mars orbits the Sun at an average distance of 1.52 au, ranging from a minimum of 1.38 au to a maximum of 1.67 au. Its orbital period is 1.88 Earth years.

At the current Earth-Mars distance of 2.078 au, light takes about 17 minutes to travel between the two planets. The solar radiation pressure at that distance is approximately 1.1 μPa (micropascals).
```
