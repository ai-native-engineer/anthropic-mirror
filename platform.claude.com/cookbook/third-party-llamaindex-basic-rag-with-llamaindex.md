<!-- source: https://platform.claude.com/cookbook/third-party-llamaindex-basic-rag-with-llamaindex -->

# RAG Pipeline with LlamaIndex

In this notebook we will look into building Basic RAG Pipeline with LlamaIndex. The pipeline has following steps.

1. Setup LLM and Embedding Model.
2. Download Data.
3. Load Data.
4. Index Data.
5. Create Query Engine.
6. Querying.

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
import os

os.environ["ANTHROPIC_API_KEY"] = "YOUR Claude API KEY"
```

### Setup LLM and Embedding model

We will use anthropic latest released `Claude 3 Opus` models

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

```
config.json:   0%|          | 0.00/777 [00:00<?, ?B/s]
model.safetensors:   0%|          | 0.00/438M [00:00<?, ?B/s]
tokenizer_config.json:   0%|          | 0.00/366 [00:00<?, ?B/s]
vocab.txt:   0%|          | 0.00/232k [00:00<?, ?B/s]
tokenizer.json:   0%|          | 0.00/711k [00:00<?, ?B/s]
special_tokens_map.json:   0%|          | 0.00/125 [00:00<?, ?B/s]
```

python

```
from llama_index.core import Settings

Settings.llm = llm
Settings.embed_model = embed_model
Settings.chunk_size = 512
```

### Download Data

python

```
!mkdir -p 'data/paul_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/paul_graham/paul_graham_essay.txt' -O 'data/paul_graham/paul_graham_essay.txt'
```

```
--2024-03-08 06:51:30--  https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/paul_graham/paul_graham_essay.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.109.133, 185.199.108.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.109.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 75042 (73K) [text/plain]
Saving to: ‘data/paul_graham/paul_graham_essay.txt’

data/paul_graham/pa 100%[===================>]  73.28K  --.-KB/s    in 0.002s

2024-03-08 06:51:30 (34.6 MB/s) - ‘data/paul_graham/paul_graham_essay.txt’ saved [75042/75042]
```

python

```
from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
)
```

### Load Data

python

```
documents = SimpleDirectoryReader("./data/paul_graham").load_data()
```

### Index Data

python

```
index = VectorStoreIndex.from_documents(
    documents,
)
```

### Create Query Engine

python

```
query_engine = index.as_query_engine(similarity_top_k=3)
```

### Test Query

python

```
response = query_engine.query("What did author do growing up?")
```

python

```
print(response)
```

```
Based on the information provided, the author worked on two main things outside of school before college: writing and programming.

For writing, he wrote short stories as a beginning writer, though he felt they were awful, with hardly any plot and just characters with strong feelings.

In terms of programming, in 9th grade he tried writing his first programs on an IBM 1401 computer that his school district used. He and his friend got permission to use it, programming in an early version of Fortran using punch cards. However, he had difficulty figuring out what to actually do with the computer at that stage given the limited inputs available.
```
