<!-- source: https://platform.claude.com/cookbook/third-party-llamaindex-multi-document-agents -->

#  Multi-Document Agents

In this notebook we will look into Building RAG when you have a large number of documents using `DocumentAgents` concept with `ReAct Agent`.

###  Installation

!pip install llama-index

!pip install llama-index-llms-anthropic

!pip install llama-index-embeddings-huggingface

###  Set Logging

# NOTE: This is ONLY necessary in jupyter notebook.

# Details: Jupyter runs an event-loop behind the scenes.

# This results in nested event-loops when we start an event-loop to make async queries.

# This is normally not allowed, we use nest\_asyncio to allow it for convenience.

import nest\_asyncio

nest\_asyncio.apply()

import logging

import sys

# Set up the root logger

logger = logging.getLogger()

logger.setLevel(logging.INFO) # Set logger level to INFO

# Clear out any existing handlers

logger.handlers = []

# Set up the StreamHandler to output to sys.stdout (Colab's output)

handler = logging.StreamHandler(sys.stdout)

handler.setLevel(logging.INFO) # Set handler level to INFO

# Add the handler to the logger

logger.addHandler(handler)

from IPython.display import HTML, display

###  Set Claude API Key

import os

os.environ["ANTHROPIC\_API\_KEY"] = "YOUR Claude API KEY"

###  Set LLM and Embedding model

We will use anthropic latest released `Claude-3 Opus` LLM.

from llama\_index.embeddings.huggingface import HuggingFaceEmbedding

from llama\_index.llms.anthropic import Anthropic

llm = Anthropic(temperature=0.0, model="claude-opus-4-1")

embed\_model = HuggingFaceEmbedding(model\_name="BAAI/bge-base-en-v1.5")

from llama\_index.core import Settings

Settings.llm = llm

Settings.embed\_model = embed\_model

Settings.chunk\_size = 512

###  Download Documents

We will use Wikipedia pages of `Toronto`, `Seattle`, `Chicago`, `Boston`, `Houston` cities and build RAG pipeline.

wiki\_titles = ["Toronto", "Seattle", "Chicago", "Boston", "Houston"]

from pathlib import Path

import requests

for title in wiki\_titles:

response = requests.get(

"https://en.wikipedia.org/w/api.php",

params={

"action": "query",

"format": "json",

"titles": title,

"prop": "extracts",

# 'exintro': True,

"explaintext": True,

},

timeout=30,

).json()

page = next(iter(response["query"]["pages"].values()))

wiki\_text = page["extract"]

data\_path = Path("data")

if not data\_path.exists():

Path.mkdir(data\_path)

with open(data\_path / f"{title}.txt", "w") as fp:

fp.write(wiki\_text)

###  Load Document

# Load all wiki documents

from llama\_index.core import SimpleDirectoryReader

city\_docs = {}

for wiki\_title in wiki\_titles:

city\_docs[wiki\_title] = SimpleDirectoryReader(

input\_files=[f"data/{wiki\_title}.txt"]

).load\_data()

####  Build ReAct Agent for each city

from llama\_index.core import SummaryIndex, VectorStoreIndex

from llama\_index.core.agent import ReActAgent

from llama\_index.core.tools import QueryEngineTool, ToolMetadata

# Build agents dictionary

agents = {}

for wiki\_title in wiki\_titles:

# build vector index

vector\_index = VectorStoreIndex.from\_documents(

city\_docs[wiki\_title],

)

# build summary index

summary\_index = SummaryIndex.from\_documents(

city\_docs[wiki\_title],

)

# define query engines

vector\_query\_engine = vector\_index.as\_query\_engine()

summary\_query\_engine = summary\_index.as\_query\_engine()

# define tools

query\_engine\_tools = [

QueryEngineTool(

query\_engine=vector\_query\_engine,

metadata=ToolMetadata(

name="vector\_tool",

description=(f"Useful for retrieving specific context from {wiki\_title}"),

),

),

QueryEngineTool(

query\_engine=summary\_query\_engine,

metadata=ToolMetadata(

name="summary\_tool",

description=(f"Useful for summarization questions related to {wiki\_title}"),

),

),

]

# build agent

agent = ReActAgent.from\_tools(

query\_engine\_tools,

llm=llm,

verbose=True,

)

agents[wiki\_title] = agent

####  Define IndexNode for each of these Agents

from llama\_index.core.schema import IndexNode

# define top-level nodes

objects = []

for wiki\_title in wiki\_titles:

# define index node that links to these agents

wiki\_summary = (

f"This content contains Wikipedia articles about {wiki\_title}. Use"

" this index if you need to lookup specific facts about"

f" {wiki\_title}.\nDo not use this index if you want to analyze"

" multiple cities."

)

node = IndexNode(text=wiki\_summary, index\_id=wiki\_title, obj=agents[wiki\_title])

objects.append(node)

####  Define Top-Level Retriever to choose an Agent

vector\_index = VectorStoreIndex(

objects=objects,

)

query\_engine = vector\_index.as\_query\_engine(similarity\_top\_k=1, verbose=True)

####  Test Queries

Should choose a vector tool/ summary tool for a specific agent based on the query.

# should use Toronto agent -> vector tool

response = query\_engine.query("What is the population of Toronto?")

```
Retrieval entering Toronto: ReActAgent
Retrieving from object ReActAgent with query What is the population of Toronto?
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
Thought: I need to use a tool to help me answer the question.
Action: vector_tool
Action Input: {'input': 'What is the population of Toronto?'}
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
Observation: According to the context information, the population of Toronto in 2021 was 2,794,356, making it the fourth-most populous city in North America.
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
Thought: I can answer without using any more tools.
Answer: According to the information provided, the population of Toronto in 2021 was 2,794,356, making it the fourth-most populous city in North America.
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
```

display(HTML(f'<p style="font-size:20px">{response.response}</p>'))

```
<IPython.core.display.HTML object>
```

# should use Houston agent -> vector tool

response = query\_engine.query("Who and when was Houston founded?")

```
Retrieval entering Houston: ReActAgent
Retrieving from object ReActAgent with query Who and when was Houston founded?
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
Thought: I need to use a tool to help me answer the question about who founded Houston and when it was founded.
Action: vector_tool
Action Input: {'input': 'Who founded Houston and when was it founded?'}
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
Observation: Houston was founded by land investors on August 30, 1836, at the confluence of Buffalo Bayou and White Oak Bayou, a point now known as Allen's Landing. The city was incorporated on June 5, 1837 and named after former General Sam Houston, who was president of the Republic of Texas at the time.
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
Thought: The vector_tool provided the key information needed to answer the question of who founded Houston and when it was founded. I can now provide a complete answer without using any more tools.
Answer: Houston was founded by land investors on August 30, 1836. The city was incorporated on June 5, 1837 and named after Sam Houston, who was the president of the Republic of Texas at the time. The location where Houston was founded is at the confluence of Buffalo Bayou and White Oak Bayou, which is now known as Allen's Landing.
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
```

display(HTML(f'<p style="font-size:20px">{response.response}</p>'))

```
<IPython.core.display.HTML object>
```

# should use Boston agent -> summary tool

response = query\_engine.query("Summarize about the sports teams in Boston")

```
Retrieval entering Boston: ReActAgent
Retrieving from object ReActAgent with query Summarize about the sports teams in Boston
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
Thought: I need to use a tool to help me answer the question.
Action: summary_tool
Action Input: {'input': 'Summarize the sports teams in Boston'}
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
Observation: Boston has teams in the four major North American men's professional sports leagues plus Major League Soccer, and has won 39 championships in these leagues:

- The Boston Red Sox (MLB) play at Fenway Park. They are one of the most storied franchises in baseball.

- The Boston Celtics (NBA) play at TD Garden. Along with the Los Angeles Lakers, they have won the most NBA championships with 17.

- The Boston Bruins (NHL) also play at TD Garden. They were the first American NHL team and are an Original Six franchise.

- The New England Patriots (NFL) play in nearby Foxborough. They have won 6 Super Bowls in the 2000s and 2010s.

- The New England Revolution (MLS) also play in Foxborough.

Boston also has several other professional sports teams like the Boston Breakers (women's soccer) and Boston Cannons (lacrosse). The area's many colleges field competitive NCAA Division I teams, especially in ice hockey. The annual Boston Marathon is one of the world's most famous running events.
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
Thought: The summary tool provided a good overview of the major sports teams in Boston. I think I can provide a concise summary answer to the original question based on this information.
Answer: Boston is home to successful professional sports teams in baseball (Red Sox), basketball (Celtics), hockey (Bruins), football (Patriots), and soccer (Revolution). The Red Sox, Celtics, and Bruins are some of the most historic franchises in their respective leagues. In total, Boston teams have won 39 championships in the four major North American sports leagues and MLS. The area also hosts the famous Boston Marathon each year and has many competitive college sports programs, especially in ice hockey.
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
```

display(HTML(f'<p style="font-size:20px">{response.response}</p>'))

```
<IPython.core.display.HTML object>
```

# should use Seattle agent -> summary tool

response = query\_engine.query("Give me a summary on all the positive aspects of Chicago")

```
Retrieval entering Chicago: ReActAgent
Retrieving from object ReActAgent with query Give me a summary on all the positive aspects of Chicago
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
Thought: I need to use a tool to help me summarize the positive aspects of Chicago.
Action: summary_tool
Action Input: {'input': 'Provide a summary of the positive aspects and attributes of the city of Chicago'}
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
Observation: Based on the provided information, some of the positive aspects and attributes of Chicago include:

- Chicago is the third most populous city in the U.S. and a major transportation hub. It is an important component in global distribution.

- The city has a diverse economy, with major industries including finance, commerce, industry, technology, telecommunications, and transportation. Chicago has the second largest central business district in the U.S.

- Chicago is an international hub for finance, culture, commerce, and industry. It has the largest derivatives market in the world and is a major financial center.

- The city is a popular tourist destination known for its architecture, skyscrapers, parks, museums, and unique cuisine. Major attractions include Millennium Park, Navy Pier, the Magnificent Mile, and numerous cultural institutions.

- Chicago has a rich history in the visual and performing arts, literature, film, theater, and music. It has influential art museums, a strong tradition of jazz and blues music, and acclaimed theater, dance, and comedy scenes.

- The city has an extensive public transportation system including rail lines and buses. It also has a large network of parks and open spaces.

- Chicago is home to several top universities, numerous major company headquarters, and a variety of unique neighborhoods and communities reflecting its diverse population and history.

In summary, Chicago stands out for its economic strength, cultural vibrancy, tourist appeal, transportation infrastructure, higher education, and cosmopolitan character. The context portrays Chicago in an overall positive light as a thriving, world-class American city.
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
Thought: The summary tool provided a good overview of the positive aspects of Chicago. I think I can provide a satisfactory answer to the original question based on the information given.
Answer: Chicago has many positive attributes that make it a vibrant and appealing city:

Economy and Business: Chicago has a diverse and thriving economy, serving as a major hub for industries like finance, commerce, telecommunications, and transportation. It is home to the second largest central business district in the U.S. and the world's largest derivatives market.

Tourism and Culture: Chicago is a popular tourist destination known for its iconic architecture, world-class museums, unique cuisine, and beautiful parks like Millennium Park. The city has a rich artistic heritage in visual arts, music (especially jazz and blues), theater, dance and comedy.

Transportation: Chicago is a critical transportation center for the U.S. with an extensive public transit network of trains and buses. Its airports and rail lines make it an important link in the nation's distribution network.

Education: Numerous prestigious universities call Chicago home, adding to its intellectual capital.

Diversity: Chicago's many neighborhoods reflect the diverse backgrounds and cultures of its residents, resulting in a cosmopolitan, international character.

Overall, Chicago stands out as a world-class city known for its robust economy, vibrant cultural scene, strong transportation infrastructure, acclaimed educational institutions, and global status. The city has many strengths and positive qualities that make it an attractive place to live, work, and visit.
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
```

display(HTML(f'<p style="font-size:20px">{response.response}</p>'))

```
<IPython.core.display.HTML object>
```
