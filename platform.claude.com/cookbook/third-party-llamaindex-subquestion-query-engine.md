<!-- source: https://platform.claude.com/cookbook/third-party-llamaindex-subquestion-query-engine -->

#  SubQuestionQueryEngine

Often, we encounter scenarios where our queries span across multiple documents.

In this notebook, we delve into addressing complex queries that extend over various documents by breaking them down into simpler sub-queries and generate answers using the `SubQuestionQueryEngine`.

###  Installation

%pip install llama-index

%pip install llama-index-llms-anthropic

%pip install llama-index-embeddings-huggingface

###  Setup API Key

import os

os.environ["ANTHROPIC\_API\_KEY"] = "YOUR Claude API KEY"

###  Setup LLM and Embedding model

We will use anthropic latest released `Claude-3 Opus` LLM.

from llama\_index.embeddings.huggingface import HuggingFaceEmbedding

from llama\_index.llms.anthropic import Anthropic

llm = Anthropic(temperature=0.0, model="claude-opus-4-8")

embed\_model = HuggingFaceEmbedding(model\_name="BAAI/bge-base-en-v1.5")

from llama\_index.core import Settings

Settings.llm = llm

Settings.embed\_model = embed\_model

Settings.chunk\_size = 512

###  Setup logging

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

###  Download Data

We will use Uber and Lyft 2021 10K SEC Filings

!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/examples/data/10k/uber\_2021.pdf' -O './uber\_2021.pdf'

!wget 'https://raw.githubusercontent.com/run-llama/llama\_index/main/docs/examples/data/10k/lyft\_2021.pdf' -O './lyft\_2021.pdf'

```
--2024-03-08 07:07:32--  https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/10k/uber_2021.pdf
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.109.133, 185.199.108.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.109.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1880483 (1.8M) [application/octet-stream]
Saving to: ‘./uber_2021.pdf’

./uber_2021.pdf     100%[===================>]   1.79M  --.-KB/s    in 0.02s

2024-03-08 07:07:32 (87.4 MB/s) - ‘./uber_2021.pdf’ saved [1880483/1880483]

--2024-03-08 07:07:33--  https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/10k/lyft_2021.pdf
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.111.133, 185.199.109.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1440303 (1.4M) [application/octet-stream]
Saving to: ‘./lyft_2021.pdf’

./lyft_2021.pdf     100%[===================>]   1.37M  --.-KB/s    in 0.02s

2024-03-08 07:07:33 (74.9 MB/s) - ‘./lyft_2021.pdf’ saved [1440303/1440303]
```

###  Load Data

from llama\_index.core import SimpleDirectoryReader

lyft\_docs = SimpleDirectoryReader(input\_files=["lyft\_2021.pdf"]).load\_data()

uber\_docs = SimpleDirectoryReader(input\_files=["uber\_2021.pdf"]).load\_data()

print(f"Loaded lyft 10-K with {len(lyft\_docs)} pages")

print(f"Loaded Uber 10-K with {len(uber\_docs)} pages")

```
Loaded lyft 10-K with 238 pages
Loaded Uber 10-K with 307 pages
```

###  Index Data

from llama\_index.core import VectorStoreIndex

lyft\_index = VectorStoreIndex.from\_documents(lyft\_docs[:100])

uber\_index = VectorStoreIndex.from\_documents(uber\_docs[:100])

###  Create Query Engines

lyft\_engine = lyft\_index.as\_query\_engine(similarity\_top\_k=5)

uber\_engine = uber\_index.as\_query\_engine(similarity\_top\_k=5)

###  Querying

response = await lyft\_engine.aquery(

"What is the revenue of Lyft in 2021? Answer in millions with page reference"

)

display(HTML(f'<p style="font-size:20px">{response.response}</p>'))

```
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"

<IPython.core.display.HTML object>
```

response = await uber\_engine.aquery(

"What is the revenue of Uber in 2021? Answer in millions, with page reference"

)

display(HTML(f'<p style="font-size:20px">{response.response}</p>'))

```
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"

<IPython.core.display.HTML object>
```

###  Create Tools

from llama\_index.core.query\_engine import SubQuestionQueryEngine

from llama\_index.core.tools import QueryEngineTool, ToolMetadata

query\_engine\_tools = [

QueryEngineTool(

query\_engine=lyft\_engine,

metadata=ToolMetadata(

name="lyft\_10k", description="Provides information about Lyft financials for year 2021"

),

),

QueryEngineTool(

query\_engine=uber\_engine,

metadata=ToolMetadata(

name="uber\_10k", description="Provides information about Uber financials for year 2021"

),

),

]

###  Create `SubQuestionQueryEngine`

sub\_question\_query\_engine = SubQuestionQueryEngine.from\_defaults(

query\_engine\_tools=query\_engine\_tools

)

###  Querying

response = await sub\_question\_query\_engine.aquery(

"Compare revenue growth of Uber and Lyft from 2020 to 2021"

)

```
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
Generated 4 sub questions.
[uber_10k] Q: What was Uber's revenue in 2020?
[uber_10k] Q: What was Uber's revenue in 2021?
[lyft_10k] Q: What was Lyft's revenue in 2020?
[lyft_10k] Q: What was Lyft's revenue in 2021?
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
[lyft_10k] A: According to Lyft's consolidated statements of operations data, Lyft's total revenue in 2020 was $2,364,681,000.
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
[uber_10k] A: According to Uber's consolidated statements of operations, Uber's revenue in 2021 was $17,455 million.
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
[uber_10k] A: According to Uber's consolidated statements of operations, Uber's revenue in 2020 was $11,139 million.
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
[lyft_10k] A: According to Lyft's consolidated statements of operations, Lyft's total revenue in 2021 was $3,208,323,000. This consisted of:

- Revenue from contracts with customers (under ASC 606) of $2,957,979,000
- Rental revenue (under ASC 842) of $250,344,000

So in total, Lyft generated revenue of $3,208,323,000 in the year ended December 31, 2021.
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
```

display(HTML(f'<p style="font-size:20px">{response.response}</p>'))

```
<IPython.core.display.HTML object>
```

response = await sub\_question\_query\_engine.aquery("Compare the investments made by Uber and Lyft")

```
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
Generated 4 sub questions.
[uber_10k] Q: What investments did Uber make in 2021
[uber_10k] Q: What was the total amount invested by Uber in 2021
[lyft_10k] Q: What investments did Lyft make in 2021
[lyft_10k] Q: What was the total amount invested by Lyft in 2021
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
[uber_10k] A: Based on the context provided, in 2021 Uber invested:

- $2.3 billion in acquisition of businesses, net of cash acquired
- $1.1 billion in purchases of marketable securities
- $982 million in purchases of non-marketable equity securities
- $297 million in purchases of notes receivable
- $298 million in purchases of property and equipment

So in total, Uber invested approximately $5.0 billion in 2021 across business acquisitions, marketable and non-marketable securities, notes receivable, and property and equipment purchases.
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
[lyft_10k] A: Based on the context provided, in 2021 Lyft invested in marketable securities and term deposits:

- Lyft purchased marketable securities of $3.8 billion in 2021. The marketable securities consisted of investment grade available-for-sale debt securities.

- Lyft also invested in term deposits of $0.5 billion in 2021. The term deposits were at cost, which approximated fair value.

As of December 31, 2021, Lyft's investment portfolio had a weighted-average remaining maturity of less than one year. Lyft's investment policy is designed to minimize exposure to credit losses.
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
[uber_10k] A: Based on the provided context, in 2021 Uber made investments to:

- Increase the number of Drivers, consumers, merchants, shippers, and carriers using their platform through incentives, discounts, and promotions
- Expand within existing markets and into new markets
- Increase research and development expenses
- Expand marketing channels and operations
- Hire additional employees
- Add new products and offerings to their platform

The context indicates Uber expected to incur losses in the near term as a result of substantial increases in operating expenses from continuing to make these types of investments.
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
[lyft_10k] A: Based on the financial information provided in the context, the cash flow statement shows that Lyft had net cash provided by investing activities of $267.0 million for the year ended December 31, 2021. This primarily consisted of:

- Proceeds from sales and maturities of marketable securities of $3.8 billion
- Maturities of term deposits of $675.5 million
- Partially offset by purchases of marketable securities of $3.8 billion and term deposits of $0.5 billion

So while the total proceeds from sales/maturities was around $4.5 billion, Lyft reinvested most of that, with net new investments of approximately $267 million in 2021.
HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
```

display(HTML(f'<p style="font-size:20px">{response.response}</p>'))

```
<IPython.core.display.HTML object>
```
