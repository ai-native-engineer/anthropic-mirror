<!-- source: https://platform.claude.com/cookbook/third-party-llamaindex-react-agent -->

# ReAct Agent

In this notebook we will look into creating ReAct Agent over tools.

1. ReAct Agent over simple calculator tools.
2. ReAct Agent over QueryEngine (RAG) tools.

### Installation

python

```
!pip install llama-index
!pip install llama-index-llms-anthropic
!pip install llama-index-embeddings-huggingface
```

### Setup API Keys

python

```
# llama-parse is async-first, running the async code in a notebook requires the use of nest_asyncio
import nest_asyncio

nest_asyncio.apply()

import os

# Using Anthropic LLM API for LLM
os.environ["ANTHROPIC_API_KEY"] = "YOUR Claude API KEY"

from IPython.display import HTML, display
```

### Set LLM and Embedding model

We will use anthropic latest released `Claude-3 Opus` LLM.

python

```
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.anthropic import Anthropic
```

python

```
llm = Anthropic(temperature=0.0, model="claude-opus-4-1")
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
```

python

```
from llama_index.core import Settings

Settings.llm = llm
Settings.embed_model = embed_model
Settings.chunk_size = 512
```

## ReAct Agent over Tools

### Define Tools

python

```
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool
```

python

```
def multiply(a: int, b: int) -> int:
    """Multiply two integers and returns the result integer"""
    return a * b

def add(a: int, b: int) -> int:
    """Add two integers and returns the result integer"""
    return a + b

add_tool = FunctionTool.from_defaults(fn=add)
multiply_tool = FunctionTool.from_defaults(fn=multiply)
```

### Create ReAct Agent

Create agent over tools and test out queries

python

```
agent = ReActAgent.from_tools([multiply_tool, add_tool], llm=llm, verbose=True)
```

python

```
response = agent.chat("What is 20+(2*4)? Calculate step by step ")
```

```
Thought: I need to use the multiply tool to calculate 2*4 first, then use the add tool to add that result to 20.
Action: multiply
Action Input: {'a': 2, 'b': 4}
Observation: 8
Thought: Now that I have the result of 2*4, which is 8, I can add that to 20 to get the final answer.
Action: add
Action Input: {'a': 20, 'b': 8}
Observation: 28
Thought: I can answer without using any more tools.
Answer: 20+(2*4) equals 28.

To calculate it step-by-step:
1. First, calculate 2*4 which equals 8.
2. Then, add 20 to that result of 8.
3. 20 + 8 = 28

Therefore, 20+(2*4) = 28.
```

python

```
display(HTML(f'<p style="font-size:20px">{response.response}</p>'))
```

```
20+(2*4) equals 28.

To calculate it step-by-step:
1. First, calculate 2*4 which equals 8.
2. Then, add 20 to that result of 8.
3. 20 + 8 = 28

Therefore, 20+(2*4) = 28.
```

### Visit Prompts

You can check prompts that the agent used to select the tools.

python

```
prompt_dict = agent.get_prompts()
for k, v in prompt_dict.items():
    print(f"Prompt: {k}\n\nValue: {v.template}")
```

```
Prompt: agent_worker:system_prompt

Value:
You are designed to help with a variety of tasks, from answering questions     to providing summaries to other types of analyses.

## Tools
You have access to a wide variety of tools. You are responsible for using
the tools in any sequence you deem appropriate to complete the task at hand.
This may require breaking the task into subtasks and using different tools
to complete each subtask.

You have access to the following tools:
{tool_desc}

## Output Format
To answer the question, please use the following format.

```
Thought: I need to use a tool to help me answer the question.
Action: tool name (one of {tool_names}) if using a tool.
Action Input: the input to the tool, in a JSON format representing the kwargs (e.g. {{"input": "hello world", "num_beams": 5}})
```

Please ALWAYS start with a Thought.

Please use a valid JSON format for the Action Input. Do NOT do this {{'input': 'hello world', 'num_beams': 5}}.

If this format is used, the user will respond in the following format:

```
Observation: tool response
```

You should keep repeating the above format until you have enough information
to answer the question without using any more tools. At that point, you MUST respond
in the one of the following two formats:

```
Thought: I can answer without using any more tools.
Answer: [your answer here]
```

```
Thought: I cannot answer the question with the provided tools.
Answer: Sorry, I cannot answer your query.
```

## Current Conversation
Below is the current conversation consisting of interleaving human and assistant messages.
```

## ReAct Agent over `QueryEngine` Tools

python

```
from llama_index.core.tools import QueryEngineTool, ToolMetadata
```

### Download data

We will define ReAct agent over tools created on QueryEngines with Uber and Lyft 10K SEC Filings.

python

```
!mkdir -p 'data/10k/'
!wget 'https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/10k/uber_2021.pdf' -O 'data/10k/uber_2021.pdf'
!wget 'https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/10k/lyft_2021.pdf' -O 'data/10k/lyft_2021.pdf'
```

```
--2024-03-08 06:58:18--  https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/10k/uber_2021.pdf
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.109.133, 185.199.111.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1880483 (1.8M) [application/octet-stream]
Saving to: ‘data/10k/uber_2021.pdf’

data/10k/uber_2021. 100%[===================>]   1.79M  --.-KB/s    in 0.02s

2024-03-08 06:58:18 (90.6 MB/s) - ‘data/10k/uber_2021.pdf’ saved [1880483/1880483]

--2024-03-08 06:58:19--  https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/10k/lyft_2021.pdf
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.109.133, 185.199.108.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1440303 (1.4M) [application/octet-stream]
Saving to: ‘data/10k/lyft_2021.pdf’

data/10k/lyft_2021. 100%[===================>]   1.37M  --.-KB/s    in 0.02s

2024-03-08 06:58:19 (60.1 MB/s) - ‘data/10k/lyft_2021.pdf’ saved [1440303/1440303]
```

### Load Data

python

```
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

lyft_docs = SimpleDirectoryReader(input_files=["./data/10k/lyft_2021.pdf"]).load_data()
uber_docs = SimpleDirectoryReader(input_files=["./data/10k/uber_2021.pdf"]).load_data()
```

### Build Index

python

```
lyft_index = VectorStoreIndex.from_documents(lyft_docs)
uber_index = VectorStoreIndex.from_documents(uber_docs)
```

### Create QueryEngines

python

```
lyft_engine = lyft_index.as_query_engine(similarity_top_k=3)
uber_engine = uber_index.as_query_engine(similarity_top_k=3)
```

#### Create QueryEngine Tools

python

```
query_engine_tools = [
    QueryEngineTool(
        query_engine=lyft_engine,
        metadata=ToolMetadata(
            name="lyft_10k",
            description=(
                "Provides information about Lyft financials for year 2021. "
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    ),
    QueryEngineTool(
        query_engine=uber_engine,
        metadata=ToolMetadata(
            name="uber_10k",
            description=(
                "Provides information about Uber financials for year 2021. "
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    ),
]
```

### ReAct Agent

python

```
agent = ReActAgent.from_tools(
    query_engine_tools,
    llm=llm,
    verbose=True,
)
```

### Querying with ReAct Agent

python

```
response = agent.chat("What was Lyft's revenue growth in 2021?")
```

```
Thought: I need to use a tool to help me answer the question.
Action: lyft_10k
Action Input: {'input': "What was Lyft's revenue growth in 2021?"}
Observation: According to the context provided, Lyft's revenue increased by $843.6 million, or 36%, in 2021 compared to 2020. This growth was primarily driven by a significant increase in the number of Active Riders in 2021 as vaccines became more widely distributed and more communities reopened. The revenue growth in 2021 was partially offset by increased driver incentives recorded as a reduction to revenue.
Thought: The provided observation directly answers the question about Lyft's revenue growth in 2021. I have enough information to provide a final answer without using additional tools.
Answer: Lyft's revenue grew by $843.6 million, or 36%, in 2021 compared to 2020. The growth was mainly driven by a significant increase in Active Riders as COVID-19 vaccines became more widely available and communities reopened. However, the revenue growth was partially offset by higher driver incentives which were recorded as a reduction to revenue.
```

python

```
display(HTML(f'<p style="font-size:20px">{response.response}</p>'))
```

```
Lyft's revenue grew by $843.6 million, or 36%, in 2021 compared to 2020. The growth was mainly driven by a significant increase in Active Riders as COVID-19 vaccines became more widely available and communities reopened. However, the revenue growth was partially offset by higher driver incentives which were recorded as a reduction to revenue.
```

python

```
response = agent.chat(
    "Compare and contrast the revenue growth of Uber and Lyft in 2021, then give an analysis"
)
```

```
Thought: I need to use the lyft_10k and uber_10k tools to find information about Lyft and Uber's revenue growth in 2021 to compare and contrast them.

Action: lyft_10k
Action Input: {"input": "What was Lyft's revenue growth in dollars and percentage in 2021 compared to 2020?"}

Observation: Lyft's revenue grew by $843.6 million, or 36%, from $2.4 billion in 2020 to $3.2 billion in 2021.

Thought: Now I need to find Uber's revenue growth in 2021 to compare to Lyft's.

Action: uber_10k
Action Input: {"input": "What was Uber's revenue growth in dollars and percentage in 2021 compared to 2020?"}

Observation: Uber's revenue grew by $8.5 billion, or 57%, from $14.1 billion in 2020 to $22.6 billion in 2021.

Thought: I can now compare the revenue growth figures and provide an analysis.
Answer: In comparing Lyft and Uber's revenue growth in 2021:

Lyft's revenue grew by $843.6 million, or 36%, from $2.4 billion in 2020 to $3.2 billion in 2021.

Uber's revenue grew by a much larger $8.5 billion, or 57%, from $14.1 billion in 2020 to $22.6 billion in 2021.

So while both companies saw strong revenue growth as they recovered from the impacts of the pandemic in 2020, Uber's growth was significantly higher than Lyft's in both dollar and percentage terms.

A few key factors likely contributed to Uber's higher growth rate:

1) Uber has a more diversified business with significant food delivery and freight segments in addition to ridesharing. These segments grew rapidly in 2021.

2) Uber operates in many more international markets than Lyft. As global travel recovered in 2021, this provided a boost to Uber.

3) Uber's overall scale is much larger than Lyft's, so similar percentage growth translates
```

python

```
display(HTML(f'<p style="font-size:20px">{response.response}</p>'))
```

```
In comparing Lyft and Uber's revenue growth in 2021:

Lyft's revenue grew by $843.6 million, or 36%, from $2.4 billion in 2020 to $3.2 billion in 2021.

Uber's revenue grew by a much larger $8.5 billion, or 57%, from $14.1 billion in 2020 to $22.6 billion in 2021.

So while both companies saw strong revenue growth as they recovered from the impacts of the pandemic in 2020, Uber's growth was significantly higher than Lyft's in both dollar and percentage terms.

A few key factors likely contributed to Uber's higher growth rate:

1) Uber has a more diversified business with significant food delivery and freight segments in addition to ridesharing. These segments grew rapidly in 2021.

2) Uber operates in many more international markets than Lyft. As global travel recovered in 2021, this provided a boost to Uber.

3) Uber's overall scale is much larger than Lyft's, so similar percentage growth translates
```
