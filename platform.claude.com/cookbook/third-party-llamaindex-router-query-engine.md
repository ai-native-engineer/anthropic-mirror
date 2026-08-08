<!-- source: https://platform.claude.com/cookbook/third-party-llamaindex-router-query-engine -->

#  RouterQuery Engine

In this notebook we will look into `RouterQueryEngine` to route the user queries to one of the available query engine tools. These tools can be different indices/ query engine on same documents/ different documents.

###  Installation



!pip install llama-index

!pip install llama-index-llms-anthropic

!pip install llama-index-embeddings-huggingface

###  Set Logging



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

###  Set Claude API Key



import os

os.environ["ANTHROPIC\_API\_KEY"] = "YOUR Claude API KEY"

###  Set LLM and Embedding model

We will use anthropic latest released `Claude-3 Opus` LLM.



from llama\_index.embeddings.huggingface import HuggingFaceEmbedding

from llama\_index.llms.anthropic import Anthropic



llm = Anthropic(temperature=0.0, model="claude-opus-4-1")

embed\_model = HuggingFaceEmbedding(model\_name="BAAI/bge-base-en-v1.5")



from llama\_index.core import Settings

Settings.llm = llm

Settings.embed\_model = embed\_model

Settings.chunk\_size = 512

###  Download Document



!mkdir -p 'data/paul\_graham/'

!wget 'https://raw.githubusercontent.com/jerryjliu/llama\_index/main/docs/examples/data/paul\_graham/paul\_graham\_essay.txt' -O 'data/paul\_graham/paul\_graham\_essay.txt'



```
--2024-03-08 07:04:27--  https://raw.githubusercontent.com/jerryjliu/llama_index/main/docs/examples/data/paul_graham/paul_graham_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.109.133, 185.199.110.133, 185.199.108.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.109.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) [text/plain]
Saving to: ‘data/paul_graham/paul_graham_essay.txt’

data/paul_graham/pa 100%[===================>]  73.28K  --.-KB/s    in 0.002s

2024-03-08 07:04:27 (28.6 MB/s) - ‘data/paul_graham/paul_graham_essay.txt’ saved [75042/75042]
```

###  Load Document



# load documents

from llama\_index.core import SimpleDirectoryReader

documents = SimpleDirectoryReader("data/paul\_graham").load\_data()

###  Create Indices and Query Engines.



from llama\_index.core import SummaryIndex, VectorStoreIndex

# Summary Index for summarization questions

summary\_index = SummaryIndex.from\_documents(documents)

# Vector Index for answering specific context questions

vector\_index = VectorStoreIndex.from\_documents(documents)



# Summary Index Query Engine

summary\_query\_engine = summary\_index.as\_query\_engine(

response\_mode="tree\_summarize",

use\_async=True,

)

# Vector Index Query Engine

vector\_query\_engine = vector\_index.as\_query\_engine()

###  Create tools for summary and vector query engines.



from llama\_index.core.tools.query\_engine import QueryEngineTool

# Summary Index tool

summary\_tool = QueryEngineTool.from\_defaults(

query\_engine=summary\_query\_engine,

description="Useful for summarization questions related to Paul Graham eassy on What I Worked On.",

)

# Vector Index tool

vector\_tool = QueryEngineTool.from\_defaults(

query\_engine=vector\_query\_engine,

description="Useful for retrieving specific context from Paul Graham essay on What I Worked On.",

)

###  Create Router Query Engine



from llama\_index.core.query\_engine.router\_query\_engine import RouterQueryEngine

from llama\_index.core.selectors.llm\_selectors import LLMSingleSelector



# Create Router Query Engine

query\_engine = RouterQueryEngine(

selector=LLMSingleSelector.from\_defaults(),

query\_engine\_tools=[

summary\_tool,

vector\_tool,

],

)

###  Test Queries



response = query\_engine.query("What is the summary of the document?")



```
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
Selecting query engine 0: The question is asking for a summary of the document. Choice 1 specifically mentions that it is useful for summarization questions related to Paul Graham's essay on What I Worked On, making it the most relevant choice for answering the given question..
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
```



display(HTML(f'<p style="font-size:20px">{response.response}</p>'))



```
<IPython.core.display.HTML object>
```



response = query\_engine.query("What did Paul Graham do growing up?")



```
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
Selecting query engine 1: The question asks about specific details from Paul Graham's life, which would likely be found in the original essay. A summary of the essay may not include all the relevant details about what he did growing up..
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
```



display(HTML(f'<p style="font-size:20px">{response.response}</p>'))



```
<IPython.core.display.HTML object>
```
