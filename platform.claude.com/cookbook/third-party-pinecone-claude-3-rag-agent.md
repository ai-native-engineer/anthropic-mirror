<!-- source: https://platform.claude.com/cookbook/third-party-pinecone-claude-3-rag-agent -->

!python --version

```
Python 3.10.12
```

#  Claude 3 RAG Agents with LangChain v1

LangChain v1 brought a lot of changes and when comparing the LangChain of versions `0.0.3xx` to `0.1.x` there's plenty of changes to the preferred way of doing things. That is very much the case for agents.

The way that we initialize and use agents is generally clearer than it was in the past — there are still many abstractions, but we can (and are encouraged to) get closer to the agent logic itself. This can make for some confusion at first, but once understood the new logic can be much clearer than with previous versions.

In this example, we'll be building a RAG agent with LangChain v1. We will use Claude 3 for our LLM, Voyage AI for knowledge embeddings, and Pinecone to power our knowledge retrieval.

To begin, let's install the prerequisites:

!pip install -qU \

langchain==0.1.11 \

langchain-core==0.1.30 \

langchain-community==0.0.27 \

langchain-anthropic==0.1.4 \

langchainhub==0.1.15 \

anthropic==0.19.1 \

voyageai==0.2.1 \

pinecone-client==3.1.0 \

datasets==2.16.1

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 848.6/848.6 kB 4.6 MB/s eta 0:00:00
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 211.0/211.0 kB 18.5 MB/s eta 0:00:00
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 507.1/507.1 kB 30.3 MB/s eta 0:00:00
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 75.6/75.6 kB 8.7 MB/s eta 0:00:00
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 115.3/115.3 kB 13.4 MB/s eta 0:00:00
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 134.8/134.8 kB 15.0 MB/s eta 0:00:00
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 77.8/77.8 kB 9.2 MB/s eta 0:00:00
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.3/58.3 kB 6.8 MB/s eta 0:00:00
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 134.8/134.8 kB 13.5 MB/s eta 0:00:00
?25h
```

And grab the required API keys. We will need API keys for [Claude(opens in new tab)](https://docs.claude.com/claude/reference/getting-started-with-the-api), [Voyage AI(opens in new tab)](https://docs.voyageai.com/install/), and [Pinecone(opens in new tab)](https://docs.pinecone.io/docs/quickstart).

# Insert your API keys here

ANTHROPIC\_API\_KEY = "<YOUR\_ANTHROPIC\_API\_KEY>"

PINECONE\_API\_KEY = "<YOUR\_PINECONE\_API\_KEY>"

VOYAGE\_API\_KEY = "<YOUR\_VOYAGE\_API\_KEY>"

##  Finding Knowledge

The first thing we need for an agent using RAG is somewhere we want to pull knowledge from. We will use v2 of the AI ArXiv dataset, available on Hugging Face Datasets at [`jamescalam/ai-arxiv2-chunks`(opens in new tab)](https://huggingface.co/datasets/jamescalam/ai-arxiv2-chunks).

*Note: we're using the prechunked dataset. For the raw version see [`jamescalam/ai-arxiv2`(opens in new tab)](https://huggingface.co/datasets/jamescalam/ai-arxiv2).*

from datasets import load\_dataset

dataset = load\_dataset("jamescalam/ai-arxiv2-chunks", split="train[:20000]")

dataset

```
/usr/local/lib/python3.10/dist-packages/huggingface_hub/utils/_token.py:88: UserWarning:
The secret `HF_TOKEN` does not exist in your Colab secrets.
To authenticate with the Hugging Face Hub, create a token in your settings tab (https://huggingface.co/settings/tokens), set it as secret in your Google Colab and restart your session.
You will be able to reuse this secret in all of your notebooks.
Please note that authentication is recommended but still optional to access public models or datasets.
  warnings.warn(

Downloading data:   0%|          | 0.00/766M [00:00<?, ?B/s]
Generating train split: 0 examples [00:00, ? examples/s]
Dataset({
    features: ['doi', 'chunk-id', 'chunk', 'id', 'title', 'summary', 'source', 'authors', 'categories', 'comment', 'journal_ref', 'primary_category', 'published', 'updated', 'references'],
    num_rows: 20000
})
```

dataset[1]

```
{'doi': '2401.09350',
 'chunk-id': 1,
 'chunk': 'These neural networks and their training algorithms may be complex, and the scope of their impact broad and wide, but nonetheless they are simply functions in a high-dimensional space. A trained neural network takes a vector as input, crunches and transforms it in various ways, and produces another vector, often in some other space. An image may thereby be turned into a vector, a song into a sequence of vectors, and a social network as a structured collection of vectors. It seems as though much of human knowledge, or at least what is expressed as text, audio, image, and video, has a vector representation in one form or another.\nIt should be noted that representing data as vectors is not unique to neural networks and deep learning. In fact, long before learnt vector representations of pieces of dataâ\x80\x94what is commonly known as â\x80\x9cembeddingsâ\x80\x9dâ\x80\x94came along, data was often encoded as hand-crafted feature vectors. Each feature quanti- fied into continuous or discrete values some facet of the data that was deemed relevant to a particular task (such as classification or regression). Vectors of that form, too, reflect our understanding of a real-world object or concept.',
 'id': '2401.09350#1',
 'title': 'Foundations of Vector Retrieval',
 'summary': 'Vectors are universal mathematical objects that can represent text, images,\nspeech, or a mix of these data modalities. That happens regardless of whether\ndata is represented by hand-crafted features or learnt embeddings. Collect a\nlarge enough quantity of such vectors and the question of retrieval becomes\nurgently relevant: Finding vectors that are more similar to a query vector.\nThis monograph is concerned with the question above and covers fundamental\nconcepts along with advanced data structures and algorithms for vector\nretrieval. In doing so, it recaps this fascinating topic and lowers barriers of\nentry into this rich area of research.',
 'source': 'http://arxiv.org/pdf/2401.09350',
 'authors': 'Sebastian Bruch',
 'categories': 'cs.DS, cs.IR',
 'comment': None,
 'journal_ref': None,
 'primary_category': 'cs.DS',
 'published': '20240117',
 'updated': '20240117',
 'references': []}
```

##  Building the Knowledge Base

To build our knowledge base we need *two things*:

1. Embeddings, for this we will use `VoyageEmbeddings` using Voyage AI's embedding models, which do need an [API key(opens in new tab)](https://dash.voyageai.com/api-keys).
2. A vector database, where we store our embeddings and query them. We use Pinecone which again requires a [free API key(opens in new tab)](https://app.pinecone.io).

First we initialize our connection to Voyage AI and define an `embed` object for embeddings:

from langchain\_community.embeddings import VoyageEmbeddings

embed = VoyageEmbeddings(voyage\_api\_key=VOYAGE\_API\_KEY, model="voyage-2")

Then we initialize our connection to Pinecone:

from pinecone import Pinecone

# configure client

pc = Pinecone(api\_key=PINECONE\_API\_KEY)

Now we setup our index specification, this allows us to define the cloud provider and region where we want to deploy our index. You can find a list of all [available providers and regions here(opens in new tab)](https://docs.pinecone.io/docs/projects).

from pinecone import ServerlessSpec

spec = ServerlessSpec(cloud="aws", region="us-west-2")

Before creating an index, we need the dimensionality of our Voyage AI embedding model, which we can find easily by creating an embedding and checking the length:

vec = embed.embed\_documents(["ello"])

len(vec[0])

```
1024
```

Now we create the index using our embedding dimensionality, and a metric also compatible with the model (this can be either cosine or dotproduct). We also pass our spec to index initialization.

import time

index\_name = "claude-3-rag"

# check if index already exists (it shouldn't if this is first time)

if index\_name not in pc.list\_indexes().names():

# if does not exist, create index

pc.create\_index(

index\_name,

dimension=len(vec[0]), # dimensionality of voyage model

metric="dotproduct",

spec=spec,

)

# wait for index to be initialized

while not pc.describe\_index(index\_name).status["ready"]:

time.sleep(1)

# connect to index

index = pc.Index(index\_name)

time.sleep(1)

# view index stats

index.describe\_index\_stats()

```
{'dimension': 1024,
 'index_fullness': 0.0,
 'namespaces': {'': {'vector_count': 20000}},
 'total_vector_count': 20000}
```

###  Populating our Index

Now our knowledge base is ready to be populated with our data. We will use the `embed` helper function to embed our documents and then add them to our index.

We will also include metadata from each record.

from tqdm.auto import tqdm

# easier to work with dataset as pandas dataframe

data = dataset.to\_pandas()

batch\_size = 100

for i in tqdm(range(0, len(data), batch\_size)):

i\_end = min(len(data), i + batch\_size)

# get batch of data

batch = data.iloc[i:i\_end]

# generate unique ids for each chunk

ids = [f"{x['doi']}-{x['chunk-id']}" for i, x in batch.iterrows()]

# get text to embed

texts = [x["chunk"] for \_, x in batch.iterrows()]

# embed text

embeds = embed.embed\_documents(texts)

# get metadata to store in Pinecone

metadata = [

{"text": x["chunk"], "source": x["source"], "title": x["title"]}

for i, x in batch.iterrows()

]

# add to Pinecone

index.upsert(vectors=zip(ids, embeds, metadata, strict=False))

```
0%|          | 0/200 [00:00<?, ?it/s]
```

Create a tool for our agent to use when searching for ArXiv papers:

from langchain.agents import tool

@tool

def arxiv\_search(query: str) -> str:

"""Use this tool when answering questions about AI, machine learning, data

science, or other technical questions that may be answered using arXiv

papers.

"""

# create query vector

xq = embed.embed\_query(query)

# perform search

out = index.query(vector=xq, top\_k=5, include\_metadata=True)

# reformat results into string

results\_str = "\n\n".join([x["metadata"]["text"] for x in out["matches"]])

return results\_str

tools = [arxiv\_search]

When this tool is used by our agent it will execute it like so:

print(arxiv\_search.run(tool\_input={"query": "can you tell me about llama 2?"}))

```
Model Llama 2 Code Llama Code Llama - Python Size FIM LCFT Python CPP Java PHP TypeScript C# Bash Average 7B â 13B â 34B â 70B â 7B â 7B â 7B â 7B â 13B â 13B â 13B â 13B â 34B â 34B â 7B â 7B â 13B â 13B â 34B â 34B â â â â â 14.3% 6.8% 10.8% 9.9% 19.9% 13.7% 15.8% 13.0% 24.2% 23.6% 22.2% 19.9% 27.3% 30.4% 31.6% 34.2% 12.6% 13.2% 21.4% 15.1% 6.3% 3.2% 8.3% 9.5% 3.2% 12.6% 17.1% 3.8% 18.9% 25.9% 8.9% 24.8% â â â â â â â â â â 37.3% 31.1% 36.1% 30.4% 29.2% 29.8% 38.0%

Ethical Considerations and Limitations (Section 5.2) Llama 2 is a new technology that carries risks with use. Testing conducted to date has been in English, and has not covered, nor could it cover all scenarios. For these reasons, as with all LLMs, Llama 2âs potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate or objectionable responses to user prompts. Therefore, before deploying any applications of Llama 2, developers should perform safety testing and tuning tailored to their speciï¬c applications of the model. Please see the Responsible Use Guide available available at https://ai.meta.com/llama/responsible-user-guide
Table 52: Model card for Llama 2.
77

2
Cove Liama Long context (7B =, 13B =, 34B) + fine-tuning ; Lrama 2 Code training 20B oes Cope Liama - Instruct Foundation models â> nfilling code training = eee.â (7B =, 13B =, 34B) â 5B (7B, 13B, 348) 5008 Python code Long context Cove Liama - PyrHon (7B, 13B, 34B) > training Â» Fine-tuning > 1008 208
Figure 2: The Code Llama specialization pipeline. The different stages of fine-tuning annotated with the number of tokens seen during training. Infilling-capable models are marked with the â symbol.
# 2 Code Llama: Specializing Llama 2 for code
# 2.1 The Code Llama models family

# 2 Code Llama: Specializing Llama 2 for code
# 2.1 The Code Llama models family
Code Llama. The Code Llama models constitute foundation models for code generation. They come in four model sizes: 7B, 13B, 34B and 70B parameters. The 7B, 13B and 70B models are trained using an infilling objective (Section 2.3), and are appropriate to be used in an IDE to complete code in the middle of a file, for example. The 34B model was trained without the infilling objective. All Code Llama models are initialized with Llama 2 model weights and trained on 500B tokens from a code-heavy dataset (see Section 2.2 for more details), except Code Llama 70B which was trained on 1T tokens. They are all fine-tuned to handle long contexts as detailed in Section 2.4.

0.52 0.57 0.19 0.30 Llama 1 7B 13B 33B 65B 0.27 0.24 0.23 0.25 0.26 0.24 0.26 0.26 0.34 0.31 0.34 0.34 0.54 0.52 0.50 0.46 0.36 0.37 0.36 0.36 0.39 0.37 0.35 0.40 0.26 0.23 0.24 0.25 0.28 0.28 0.33 0.32 0.33 0.31 0.34 0.32 0.45 0.50 0.49 0.48 0.33 0.27 0.31 0.31 0.17 0.10 0.12 0.11 0.24 0.24 0.23 0.25 0.31 0.27 0.30 0.30 0.44 0.41 0.41 0.43 0.57 0.55 0.60 0.60 0.39 0.34 0.28 0.39 Llama 2 7B 13B 34B 70B 0.28 0.24 0.27 0.31 0.25 0.25 0.24 0.29 0.29 0.35 0.33 0.35 0.50 0.50 0.56 0.51 0.36 0.41 0.41
```

##  Defining XML Agent

The XML agent is built primarily to support Anthropic models. Anthropic models have been trained to use XML tags like `<input>{some input}</input` or when using a tool they use:

<tool>{tool name}</tool>

<tool\_input>{tool input}</tool\_input>

This is much different to the format produced by typical ReAct agents, which is not as well supported by Anthropic models.

To create an XML agent we need a `prompt`, `llm`, and list of `tools`. We can download a prebuilt prompt for conversational XML agents from LangChain hub.

from langchain import hub

prompt = hub.pull("hwchase17/xml-agent-convo")

prompt

```
ChatPromptTemplate(input_variables=['agent_scratchpad', 'input', 'tools'], partial_variables={'chat_history': ''}, messages=[HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['agent_scratchpad', 'chat_history', 'input', 'tools'], template="You are a helpful assistant. Help the user answer any questions.\n\nYou have access to the following tools:\n\n{tools}\n\nIn order to use a tool, you can use <tool></tool> and <tool_input></tool_input> tags. You will then get back a response in the form <observation></observation>\nFor example, if you have a tool called 'search' that could run a google search, in order to search for the weather in SF you would respond:\n\n<tool>search</tool><tool_input>weather in SF</tool_input>\n<observation>64 degrees</observation>\n\nWhen you are done, respond with a final answer between <final_answer></final_answer>. For example:\n\n<final_answer>The weather in SF is 64 degrees</final_answer>\n\nBegin!\n\nPrevious Conversation:\n{chat_history}\n\nQuestion: {input}\n{agent_scratchpad}"))])
```

We can see the XML format being used throughout the prompt when explaining to the LLM how it should use tools.

Next we initialize our connection to Anthropic, for this we need an [Claude API key(opens in new tab)](https://console.anthropic.com/).

from langchain\_anthropic import ChatAnthropic

# chat completion llm

llm = ChatAnthropic(

ANTHROPIC\_API\_KEY=ANTHROPIC\_API\_KEY,

model\_name="claude-opus-4-1", # change "opus" -> "sonnet" for speed

temperature=0.0,

)

When the agent is run we will provide it with a single `input` — this is the input text from a user. However, within the agent logic an *agent\_scratchpad* object will be passed too, which will include tool information. To feed this information into our LLM we will need to transform it into the XML format described above, we define the `convert_intermediate_steps` function to handle that.

def convert\_intermediate\_steps(intermediate\_steps):

log = ""

for action, observation in intermediate\_steps:

log += (

f"<tool>{action.tool}</tool><tool\_input>{action.tool\_input}"

f"</tool\_input><observation>{observation}</observation>"

)

return log

We must also parse the tools into a string containing `tool_name: tool_description` — we handle that with the `convert_tools` function.

def convert\_tools(tools):

return "\n".join([f"{tool.name}: {tool.description}" for tool in tools])

With everything ready we can go ahead and initialize our agent object using [**L**ang**C**hain **E**xpression **L**anguage (LCEL)(opens in new tab)](https://www.pinecone.io/learn/series/langchain/langchain-expression-language/). We add instructions for when the LLM should *stop* generating with `llm.bind(stop=[...])` and finally we parse the output from the agent using an `XMLAgentOutputParser` object.

from langchain.agents.output\_parsers import XMLAgentOutputParser

agent = (

{

"input": lambda x: x["input"],

# without "chat\_history", tool usage has no context of prev interactions

"chat\_history": lambda x: x["chat\_history"],

"agent\_scratchpad": lambda x: convert\_intermediate\_steps(x["intermediate\_steps"]),

}

| prompt.partial(tools=convert\_tools(tools))

| llm.bind(stop=["</tool\_input>", "</final\_answer>"])

| XMLAgentOutputParser()

)

With our `agent` object initialized we pass it to an `AgentExecutor` object alongside our original `tools` list:

from langchain.agents import AgentExecutor

agent\_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

Now we can use the agent via the `invoke` method:

user\_msg = "can you tell me about llama 2?"

out = agent\_executor.invoke({"input": user\_msg, "chat\_history": ""})

print(out["output"])

```
> Entering new AgentExecutor chain...
<tool>arxiv_search</tool>
<tool_input>llama 2Model Llama 2 Code Llama Code Llama - Python Size FIM LCFT Python CPP Java PHP TypeScript C# Bash Average 7B â 13B â 34B â 70B â 7B â 7B â 7B â 7B â 13B â 13B â 13B â 13B â 34B â 34B â 7B â 7B â 13B â 13B â 34B â 34B â â â â â 14.3% 6.8% 10.8% 9.9% 19.9% 13.7% 15.8% 13.0% 24.2% 23.6% 22.2% 19.9% 27.3% 30.4% 31.6% 34.2% 12.6% 13.2% 21.4% 15.1% 6.3% 3.2% 8.3% 9.5% 3.2% 12.6% 17.1% 3.8% 18.9% 25.9% 8.9% 24.8% â â â â â â â â â â 37.3% 31.1% 36.1% 30.4% 29.2% 29.8% 38.0%

2
Cove Liama Long context (7B =, 13B =, 34B) + fine-tuning ; Lrama 2 Code training 20B oes Cope Liama - Instruct Foundation models â> nfilling code training = eee.â (7B =, 13B =, 34B) â 5B (7B, 13B, 348) 5008 Python code Long context Cove Liama - PyrHon (7B, 13B, 34B) > training Â» Fine-tuning > 1008 208
Figure 2: The Code Llama specialization pipeline. The different stages of fine-tuning annotated with the number of tokens seen during training. Infilling-capable models are marked with the â symbol.
# 2 Code Llama: Specializing Llama 2 for code
# 2.1 The Code Llama models family

0.52 0.57 0.19 0.30 Llama 1 7B 13B 33B 65B 0.27 0.24 0.23 0.25 0.26 0.24 0.26 0.26 0.34 0.31 0.34 0.34 0.54 0.52 0.50 0.46 0.36 0.37 0.36 0.36 0.39 0.37 0.35 0.40 0.26 0.23 0.24 0.25 0.28 0.28 0.33 0.32 0.33 0.31 0.34 0.32 0.45 0.50 0.49 0.48 0.33 0.27 0.31 0.31 0.17 0.10 0.12 0.11 0.24 0.24 0.23 0.25 0.31 0.27 0.30 0.30 0.44 0.41 0.41 0.43 0.57 0.55 0.60 0.60 0.39 0.34 0.28 0.39 Llama 2 7B 13B 34B 70B 0.28 0.24 0.27 0.31 0.25 0.25 0.24 0.29 0.29 0.35 0.33 0.35 0.50 0.50 0.56 0.51 0.36 0.41 0.41

Ethical Considerations and Limitations (Section 5.2) Llama 2 is a new technology that carries risks with use. Testing conducted to date has been in English, and has not covered, nor could it cover all scenarios. For these reasons, as with all LLMs, Llama 2âs potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate or objectionable responses to user prompts. Therefore, before deploying any applications of Llama 2, developers should perform safety testing and tuning tailored to their speciï¬c applications of the model. Please see the Responsible Use Guide available available at https://ai.meta.com/llama/responsible-user-guide
Table 52: Model card for Llama 2.
77

Model Size FIM LCFT HumanEval MBPP pass@1 pass@10 pass@100 pass@1 pass@10 pass@100 Llama 2 Code Llama Code Llama - Python 7B â 13B â 34B â 70B â 7B â 7B â 7B â 7B â 13B â 13B â 13B â 13B â 34B â 34B â 7B â 7B â 13B â 13B â 34B â 34B â â â â â â â â â â â â â â â â â â â â â 12.2% 25.2% 20.1% 34.8% 22.6% 47.0% 30.5% 59.4% 32.3% 63.9% 34.1% 62.6% 34.1% 62.5% 33.5% 59.6% 36.6% 72.9% 36.6% 71.9% 37.8% 70.6% 36.0% 69.4% 48.2% 77.7% 48.8% 76.8% 40.2% 70.0% 38.4% 70.3% 45.7% 80.0%Based on the information from the arXiv search, here are the key points about Llama 2:

<final_answer>
- Llama 2 is a large language model developed by Meta AI. It comes in sizes ranging from 7B to 70B parameters.

- Code Llama is a version of Llama 2 that has been specialized for code generation through fine-tuning on code datasets. Code Llama models are available in Python, C++, Java, PHP, TypeScript, C#, and Bash.

- The Code Llama specialization pipeline involves foundation model pre-training, long context training, code infilling training, and fine-tuning on specific programming languages.

- Code Llama significantly outperforms the base Llama 2 models on code generation benchmarks like HumanEval and MBPP. For example, the 34B parameter Code Llama - Python achieves 48.8% pass@1 on HumanEval compared to 34.1% for the 34B Llama 2.

- As with all large language models, Llama 2 has limitations and potential risks that need to be considered before deploying it in applications. Meta provides a responsible use guide with recommendations for safety testing and tuning.

> Finished chain.

- Llama 2 is a large language model developed by Meta AI. It comes in sizes ranging from 7B to 70B parameters.

- Code Llama is a version of Llama 2 that has been specialized for code generation through fine-tuning on code datasets. Code Llama models are available in Python, C++, Java, PHP, TypeScript, C#, and Bash.

- The Code Llama specialization pipeline involves foundation model pre-training, long context training, code infilling training, and fine-tuning on specific programming languages.

- Code Llama significantly outperforms the base Llama 2 models on code generation benchmarks like HumanEval and MBPP. For example, the 34B parameter Code Llama - Python achieves 48.8% pass@1 on HumanEval compared to 34.1% for the 34B Llama 2.

- As with all large language models, Llama 2 has limitations and potential risks that need to be considered before deploying it in applications. Meta provides a responsible use guide with recommendations for safety testing and tuning.
```

That looks pretty good, but right now our agent is *stateless* — making it hard to have a conversation with. We can give it memory in many different ways, but one the easiest ways to do so is to use `ConversationBufferWindowMemory`.

from langchain.chains.conversation.memory import ConversationBufferWindowMemory

# conversational memory

conversational\_memory = ConversationBufferWindowMemory(

memory\_key="chat\_history", k=5, return\_messages=True

)

We haven't attached our conversational memory to our agent — so the `conversational_memory` object will remain empty:

conversational\_memory.chat\_memory.messages

```
[]
```

We must manually add the interactions between ourselves and the agent to our memory.

conversational\_memory.chat\_memory.add\_user\_message(user\_msg)

conversational\_memory.chat\_memory.add\_ai\_message(out["output"])

conversational\_memory.chat\_memory.messages

```
[HumanMessage(content='can you tell me about llama 2?'),
 AIMessage(content='\n- Llama 2 is a large language model developed by Meta AI. It comes in sizes ranging from 7B to 70B parameters.\n\n- Code Llama is a version of Llama 2 that has been specialized for code generation through fine-tuning on code datasets. Code Llama models are available in Python, C++, Java, PHP, TypeScript, C#, and Bash.\n\n- The Code Llama specialization pipeline involves foundation model pre-training, long context training, code infilling training, and fine-tuning on specific programming languages. \n\n- Code Llama significantly outperforms the base Llama 2 models on code generation benchmarks like HumanEval and MBPP. For example, the 34B parameter Code Llama - Python achieves 48.8% pass@1 on HumanEval compared to 34.1% for the 34B Llama 2.\n\n- As with all large language models, Llama 2 has limitations and potential risks that need to be considered before deploying it in applications. Meta provides a responsible use guide with recommendations for safety testing and tuning.\n')]
```

Now we can see that *two* messages have been added, our `HumanMessage` the agent's `AIMessage` response. Unfortunately, we cannot send these messages to our XML agent directly. Instead, we need to pass a string in the format:

Human: {human message}

AI: {AI message}

Let's write a quick `memory2str` helper function to handle this for us:

from langchain\_core.messages.human import HumanMessage

def memory2str(memory: ConversationBufferWindowMemory):

messages = memory.chat\_memory.messages

memory\_list = [

f"Human: {mem.content}" if isinstance(mem, HumanMessage) else f"AI: {mem.content}"

for mem in messages

]

memory\_str = "\n".join(memory\_list)

return memory\_str

print(memory2str(conversational\_memory))

```
Human: can you tell me about llama 2?
AI:
- Llama 2 is a large language model developed by Meta AI. It comes in sizes ranging from 7B to 70B parameters.

- Code Llama is a version of Llama 2 that has been specialized for code generation through fine-tuning on code datasets. Code Llama models are available in Python, C++, Java, PHP, TypeScript, C#, and Bash.

- The Code Llama specialization pipeline involves foundation model pre-training, long context training, code infilling training, and fine-tuning on specific programming languages.

- Code Llama significantly outperforms the base Llama 2 models on code generation benchmarks like HumanEval and MBPP. For example, the 34B parameter Code Llama - Python achieves 48.8% pass@1 on HumanEval compared to 34.1% for the 34B Llama 2.

- As with all large language models, Llama 2 has limitations and potential risks that need to be considered before deploying it in applications. Meta provides a responsible use guide with recommendations for safety testing and tuning.
```

Now let's put together another helper function called `chat` to help us handle the *state* part of our agent.

def chat(text: str):

out = agent\_executor.invoke({"input": text, "chat\_history": memory2str(conversational\_memory)})

conversational\_memory.chat\_memory.add\_user\_message(text)

conversational\_memory.chat\_memory.add\_ai\_message(out["output"])

return out["output"]

Now we simply chat with our agent and it will remember the context of previous interactions.

print(chat("was any red teaming done with the model?"))

```
> Entering new AgentExecutor chain...
<tool>arxiv_search</tool>
<tool_input>llama 2 red teamingAfter conducting red team exercises, we asked participants (who had also participated in Llama 2 Chat exercises) to also provide qualitative assessment of safety capabilities of the model. Some participants who had expertise in offensive security and malware development questioned the ultimate risk posed by âmalicious code generationâ through LLMs with current capabilities.
One red teamer remarked, âWhile LLMs being able to iteratively improve on produced source code is a risk, producing source code isnât the actual gap. That said, LLMs may be risky because they can inform low-skill adversaries in production of scripts through iteration that perform some malicious behavior.â
According to another red teamer, â[v]arious scripts, program code, and compiled binaries are readily available on mainstream public websites, hacking forums or on âthe dark web.â Advanced malware development is beyond the current capabilities of available LLMs, and even an advanced LLM paired with an expert malware developer is not particularly useful- as the barrier is not typically writing the malware code itself. That said, these LLMs may produce code which will get easily caught if used directly.â

Model Llama 2 Code Llama Code Llama - Python Size FIM LCFT Python CPP Java PHP TypeScript C# Bash Average 7B â 13B â 34B â 70B â 7B â 7B â 7B â 7B â 13B â 13B â 13B â 13B â 34B â 34B â 7B â 7B â 13B â 13B â 34B â 34B â â â â â 14.3% 6.8% 10.8% 9.9% 19.9% 13.7% 15.8% 13.0% 24.2% 23.6% 22.2% 19.9% 27.3% 30.4% 31.6% 34.2% 12.6% 13.2% 21.4% 15.1% 6.3% 3.2% 8.3% 9.5% 3.2% 12.6% 17.1% 3.8% 18.9% 25.9% 8.9% 24.8% â â â â â â â â â â 37.3% 31.1% 36.1% 30.4% 29.2% 29.8% 38.0%

In addition to red teaming sessions, we ran a quantitative evaluation on risk from generating malicious code by scoring Code Llamaâs responses to ChatGPTâs (GPT3.5 Turbo) with LLAMAv2 70Bâs safety reward model. For this second quantitative evaluation, we selected prompts that the red teamers generated specifically attempting to solicit malicious code (even though the red teaming included consideration of a broad set of safety risks). These prompts were a mix of clear intent and slightly obfuscated intentions (see some examples in Figure 16. We show a KDE plot of the distribution of the safety score for all models in Figure 7). We observe that Code Llama tends to answer with safer responses; the distribution of safety scores for Code Llama has more weight in the safer part of the range.
False refusals. LLMs that are too safe can have a tendency to over-refuse valid claims similar to what was reported after the release of Llama 2. We specifically asked red teamers to test for this behavior. They found some limited evidence of false refusals (when not using a system preprompt). False refusals could also
16

15
pafety Reward Model Scores Distribution on Red Teaming Prompts
Responding Model GPT 3.5 Turbo Code Llama 138 Instruct Code Llama 34B Instruct Code Llama 7B Instruct 0.0-+ -0.2 0.0 0.2 0.4 0.6 08 1.0 12 Llama 2 70B Safety Reward Model Score
Figure 7: KDE plot of the risk score output by the Llama 2 safety reward model on prompts with clear intent specific to code risk created by red teamers with background in cybersecurity and malware generation.
Red teaming. It is important to also proactively identify risks with adversarial testing or red teaming. We conducted 3 red teaming exercises with 25 Meta employees, including domain experts in responsible AI, malware development, and offensive security engineering.
The red teamers provided a nuanced evaluation specifically on the risk from so called âdual intent prompts.â Dual intent prompts are requests for help with writing code that could be used maliciously but the prompt does not directly address the topic (example âMosaic Promptsâ Glukhov et al. (2023)). For example, the model rightfully refuses to provide support with writing ransomware code but it complies when asked to provide a script to encrypt all files in the userâs home directory since such a script could be used for benign purposes.

. . . . . . . . . . . . . . . 3.4 RLHF Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Safety in Pretraining . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 Safety Fine-Tuning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 Red Teaming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.4 Safety Evaluation of Llama 2-Chat . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 Learnings and Observations . . . . . . . . . . . . . . . . . . . . . . . .Based on the information from the arxiv search, some red teaming was done on the Llama 2 model during development to identify potential safety risks:

<final_answer>
- Meta conducted 3 red teaming exercises with 25 employees, including domain experts in responsible AI, malware development, and offensive security engineering.

- The red teamers categorized successful attacks into four main types: 1) getting the model to provide some harmful information while refusing other content, 2) having the model roleplay specific scenarios, 3) forcing the model to highlight positives of harmful content, and 4) embedding harmful instructions within complex commands.

- Some red teamers questioned the ultimate risk posed by "malicious code generation" through current LLMs. They noted that while LLMs being able to iteratively improve code is a risk, producing source code itself isn't the main gap. Advanced malware development is currently beyond LLM capabilities.

- Quantitative evaluation was also done by scoring Code Llama's responses to malicious code prompts using Llama 2's safety reward model. Code Llama tended to give safer responses compared to GPT-3.5.

- However, the full extent and details of the red teaming are limited based on the information available. The Llama 2 paper mentions expanding prompts with safety risks via red teaming, but does not go in-depth on the process or results. More information would be needed to fully characterize the red teaming performed.

> Finished chain.

- Meta conducted 3 red teaming exercises with 25 employees, including domain experts in responsible AI, malware development, and offensive security engineering.

- The red teamers categorized successful attacks into four main types: 1) getting the model to provide some harmful information while refusing other content, 2) having the model roleplay specific scenarios, 3) forcing the model to highlight positives of harmful content, and 4) embedding harmful instructions within complex commands.

- Some red teamers questioned the ultimate risk posed by "malicious code generation" through current LLMs. They noted that while LLMs being able to iteratively improve code is a risk, producing source code itself isn't the main gap. Advanced malware development is currently beyond LLM capabilities.

- Quantitative evaluation was also done by scoring Code Llama's responses to malicious code prompts using Llama 2's safety reward model. Code Llama tended to give safer responses compared to GPT-3.5.

- However, the full extent and details of the red teaming are limited based on the information available. The Llama 2 paper mentions expanding prompts with safety risks via red teaming, but does not go in-depth on the process or results. More information would be needed to fully characterize the red teaming performed.
```

We can ask follow up questions that miss key information but thanks to the conversational history the LLM understands the context and uses that to adjust the search query. For example we asked about `red teaming` but did not mention `llama 2` — Claude 3 added this context to the search query of `"llama 2 red teaming"` based on the chat history.

---
