<!-- source: https://platform.claude.com/cookbook/third-party-mongodb-rag-using-mongodb -->

#  How to Build A RAG System Using Claude 3 And MongoDB

This tutorial implements a chatbot prompted to take on the role of a Venture capital tech Analyst. The chatbot is a naive RAG system with a collection of tech news articles acting as its knowledge source.
This notebook covers the following:

1. Follow a comprehensive tutorial on setting up your development environment, from installing necessary libraries to configuring a MongoDB database.
2. Learn efficient data handling methods, including creating vector search indexes and preparing data for ingestion and query processing.
3. Understand how to employ Claude 3 models within the RAG system for generating precise responses based on contextual information retrieved from the database.

You will need the following:

* Claude API Key
* VoyageAI API Key
* Hugging Face Access Token

##  Step 1: Library installation, data loading and preparation

Below are brief explanations of the tools and libraries utilised within the implementation code:

* anthropic: The official Python library for Anthropic that enables access to state-of-the-art language models. This library provides access to the Claude 3 family models, which can understand text and images.
* datasets: This library is part of the Hugging Face ecosystem. By installing 'datasets', we gain access to a number of pre-processed and ready-to-use datasets, which are essential for training and fine-tuning machine learning models or benchmarking their performance.
* pandas: This data science library provides robust data structures and methods for data manipulation, processing, and analysis.
* voyageai: This is the official Python client library for accessing VoyageAI's suite of embedding models.
* pymongo: PyMongo is a Python toolkit for MongoDB. It enables interactions with a MongoDB database.

!pip install pymongo datasets pandas anthropic voyageai

The code snippet below executes the following steps:

1. Import Necessary Libraries:

* `os` for interacting with the operating system,
* `requests` for making HTTP requests,
* `BytesIO` from the io module to handle bytes objects like files in memory,
* `pandas` (as pd) for data manipulation and analysis, and
* `userdata` from google.colab enables access to environment variables stored in Google Colab secrets.

1. Function Definition: The `download_and_combine_parquet_files` function is defined with two parameters:

* `parquet_file_urls`: a list of URLs as strings, each pointing to a Parquet file that contains a sub-collection of the tech-news-embedding dataset.
* `hf_token` is a string representing a Hugging Face authorization token. Access tokens can be created or copied from the [Hugging Face platform(opens in new tab)](https://huggingface.co/docs/hub/en/security-tokens#:~:text=To%20create%20an%20access%20token,you%27re%20ready%20to%20go!)

1. Download and Read Parquet Files: The function iterates over each URL in parquet\_file\_urls. For each URL, it:

* Makes a GET request using the requests.get method, passing the URL and the headers for authorization.
* Checks if the response status code is 200 (OK), indicating the request was successful.
* If successful, it reads the content of the response into a BytesIO object (to handle it as a file in memory), then uses pandas.read\_parquet to read the Parquet file from this object into a Pandas DataFrame.
* Appends the DataFrame to the list all\_dataframes.

1. Combine DataFrames: After downloading and reading all Parquet files into DataFrames, there’s a check to ensure that `all_dataframes` is not empty. If there are DataFrames to work with, then all DataFrames are concatenated into a single DataFrame using pd.concat, with ignore\_index=True to reindex the new combined DataFrame. This combined DataFrame is the overall process output in the `download_and_combine_parquet_files` function.

from io import BytesIO

import pandas as pd

import requests

from google.colab import userdata

def download\_and\_combine\_parquet\_files(parquet\_file\_urls, hf\_token):

"""

Downloads Parquet files from the provided URLs using the given Hugging Face token,

and returns a combined DataFrame.

Parameters:

- parquet\_file\_urls: List of strings, URLs to the Parquet files.

- hf\_token: String, Hugging Face authorization token.

Returns:

- combined\_df: A pandas DataFrame containing the combined data from all Parquet files.

"""

headers = {"Authorization": f"Bearer {hf\_token}"}

all\_dataframes = []

for parquet\_file\_url in parquet\_file\_urls:

response = requests.get(parquet\_file\_url, headers=headers, timeout=60)

if response.status\_code == 200:

parquet\_bytes = BytesIO(response.content)

df = pd.read\_parquet(parquet\_bytes)

all\_dataframes.append(df)

else:

print(

f"Failed to download Parquet file from {parquet\_file\_url}: {response.status\_code}"

)

if all\_dataframes:

combined\_df = pd.concat(all\_dataframes, ignore\_index=True)

return combined\_df

else:

print("No dataframes to concatenate.")

return None

Below is a list of the Parquet files required for this tutorial. The complete list of all files is located [here(opens in new tab)](https://huggingface.co/datasets/MongoDB/tech-news-embeddings/tree/refs%2Fconvert%2Fparquet/default/train). Each Parquet file represents approximately 45,000 data points.

In the code snippet below, a subset of the tech-news-embeddings dataset is grouped into a single DataFrame, which is then assigned to the variable `combined_df`.

# Uncomment the links below to load more data

# For the full list of data visit: https://huggingface.co/datasets/MongoDB/tech-news-embeddings/tree/refs%2Fconvert%2Fparquet/default/train

parquet\_files = [

"https://huggingface.co/api/datasets/AIatMongoDB/tech-news-embeddings/parquet/default/train/0000.parquet",

# "https://huggingface.co/api/datasets/AIatMongoDB/tech-news-embeddings/parquet/default/train/0001.parquet",

# "https://huggingface.co/api/datasets/AIatMongoDB/tech-news-embeddings/parquet/default/train/0002.parquet",

# "https://huggingface.co/api/datasets/AIatMongoDB/tech-news-embeddings/parquet/default/train/0003.parquet",

# "https://huggingface.co/api/datasets/AIatMongoDB/tech-news-embeddings/parquet/default/train/0004.parquet",

# "https://huggingface.co/api/datasets/AIatMongoDB/tech-news-embeddings/parquet/default/train/0005.parquet",

]

hf\_token = userdata.get("HF\_TOKEN")

combined\_df = download\_and\_combine\_parquet\_files(parquet\_files, hf\_token)

As a final phase in data preparation, the code snippet below shows the step to remove the `_id` column from the grouped dataset, as it is unnecessary for subsequent steps in this tutorial. Additionally, the data within the embedding column for each data point is converted from a numpy array to a Python list to prevent errors related to incompatible data types during the data ingestion.

# Remove the \_id coloum from the intital dataset

combined\_df = combined\_df.drop(columns=["\_id"])

# Remove the initial embedding coloumn as we are going to create new embeddings with VoyageAI embedding model

combined\_df = combined\_df.drop(columns=["embedding"])

combined\_df.head()

# Limiting the amount of document used to 500 for this demo due to the rate limit on VoyageAI API

# Read more on VoyageAI rate limits: https://docs.voyageai.com/docs/rate-limits

max\_documents = 500

if len(combined\_df) > max\_documents:

combined\_df = combined\_df[:max\_documents]

import voyageai

vo = voyageai.Client(api\_key=userdata.get("VOYAGE\_API\_KEY"))

def get\_embedding(text: str) -> list[float]:

if not text.strip():

print("Attempted to get embedding for empty text.")

return []

embedding = vo.embed(text, model="voyage-large-2", input\_type="document")

return embedding.embeddings[0]

combined\_df["embedding"] = combined\_df["description"].apply(get\_embedding)

combined\_df.head()

##  Step 2: Database and collection creation

**To create a new MongoDB database, set up a database cluster:**

1. Register for a [free MongoDB Atlas account(opens in new tab)](https://www.mongodb.com/cloud/atlas/register?utm_campaign=devrel&utm_source=community&utm_medium=cta&utm_content=Partner%20Cookbook&utm_term=richmond.alake), or existing users, [sign into MongoDB Atlas(opens in new tab)](https://account.mongodb.com/account/login?utm_campaign=devrel&utm_source=community&utm_medium=cta&utm_content=Partner%20Cookbook&utm_term=richmond.alake)
2. Select the “Database” option on the left-hand pane, which will navigate to the Database Deployment page with a deployment specification of any existing cluster. Create a new database cluster by clicking on the "+Create" button.
3. For assistance with database cluster setup and obtaining the URI, refer to our guide for setting up a MongoDB cluster and getting your connection string.
   Note: Don’t forget to whitelist the IP for the Python host or 0.0.0.0/0 for any IP when creating proof of concepts.
4. After successfully creating and deploying the cluster, the cluster becomes accessible on the ‘Database Deployment’ page.
5. Click on the “Connect” button of the cluster to view the option to set up a connection to the cluster via various language drivers.
6. This tutorial only requires the cluster’s URI(unique resource identifier). Grab the URI and copy it into the Google Colabs Secrets environment in a variable named MONGO\_URI or place it in a .env file or equivalent.

Once you have created a cluster, navigate to the cluster page and create a database and collection within the MongoDB Atlas cluster by clicking + Create Database.
The database will be named `tech_news`, and the collection will be named `hacker_noon_tech_news`.

##  Step 3: Vector search index creation

By this point, you have created a cluster, database and collection.

The steps in this section are crucial to ensure that a vector search can be conducted using the queries entered into the chatbot and searched against the records within the hacker\_noon\_tech\_news collection. The objective of this step is to create a vector search index. To achieve this, refer to the official [vector search index creation guide(opens in new tab)](https://www.mongodb.com/docs/atlas/atlas-vector-search/create-index/).

In the creation of a vector search index using the JSON editor on MongoDB Atlas, ensure your vector search index is named vector\_index and the vector search index definition is as follows:

{

"fields": [{

"numDimensions": 1536,

"path": "embedding",

"similarity": "cosine",

"type": "vector"

}]

}

##  Step 4: Data ingestion

To ingest data into the MongoDB database created in previous steps. The following operations have to be carried out:

* Connect to the database and collection
* Clear out the collection of any existing records
* Convert the Pandas DataFrame of the dataset into dictionaries before ingestion
* Ingest dictionaries into MongoDB using a batch operation

This tutorial requires the cluster's URI (unique resource identifier). Grab the URI and copy it into the Google Colab Secrets environment in a variable named MONGO\_URI, or place it in a .env file or equivalent.

import pymongo

from google.colab import userdata

def get\_mongo\_client(mongo\_uri):

"""Establish connection to the MongoDB."""

try:

client = pymongo.MongoClient(mongo\_uri)

print("Connection to MongoDB successful")

return client

except pymongo.errors.ConnectionFailure as e:

print(f"Connection failed: {e}")

return None

mongo\_uri = userdata.get("MONGO\_URI")

if not mongo\_uri:

print("MONGO\_URI not set in environment variables")

mongo\_client = get\_mongo\_client(mongo\_uri)

DB\_NAME = "tech\_news"

COLLECTION\_NAME = "hacker\_noon\_tech\_news"

db = mongo\_client[DB\_NAME]

collection = db[COLLECTION\_NAME]

```
Connection to MongoDB successful
```

# To ensure we are working with a fresh collection

# delete any existing records in the collection

collection.delete\_many({})

```
DeleteResult({'n': 228012, 'electionId': ObjectId('7fffffff000000000000000e'), 'opTime': {'ts': Timestamp(1709660559, 7341), 't': 14}, 'ok': 1.0, '$clusterTime': {'clusterTime': Timestamp(1709660559, 7341), 'signature': {'hash': b'jT\xf1\xb4\xa9\xd3\xe3suu\x03`\x15(}\x8f\x00\x9f\xe9\x8a', 'keyId': 7320226449804230661}}, 'operationTime': Timestamp(1709660559, 7341)}, acknowledged=True)
```

# Data Ingestion

combined\_df\_json = combined\_df.to\_dict(orient="records")

collection.insert\_many(combined\_df\_json)

##  Step 5: Vector Search

This section showcases the creation of a vector search custom function that accepts a user query, which corresponds to entries to the chatbot. The function also takes a second parameter, `collection`, which points to the database collection containing records against which the vector search operation should be conducted.

The `vector_search` function produces a vector search result derived from a series of operations outlined in a MongoDB aggregation pipeline. This pipeline includes the `$vectorSearch` and `$project` stages and performs queries based on the vector embeddings of user queries. It then formats the results, omitting any record attributes unnecessary for subsequent processes.

The code snippet below conducts the following operations to allow semantic search for movies:

1. Define the `vector_search` function that takes a user's query string and a MongoDB collection as inputs and returns a list of documents that match the query based on vector similarity search.
2. Generate an embedding for the user's query by calling the previously defined function, `get_embedding`, which converts the query string into a vector representation.
3. Construct a pipeline for MongoDB's aggregate function, incorporating two main stages: `$vectorSearch` and `$project`.
4. The `$vectorSearch` stage performs the actual vector search. The index field specifies the vector index to utilise for the vector search, and this should correspond to the name entered in the vector search index definition in previous steps. The queryVector field takes the embedding representation of the use query. The path field corresponds to the document field containing the embeddings. The `numCandidates` specifies the number of candidate documents to consider and the limit on the number of results to return.
5. The $project stage formats the results to excludes the \_id the `embedding` field.
6. The aggregate executes the defined pipeline to obtain the vector search results. The final operation converts the returned cursor from the database into a list.

def vector\_search(user\_query, collection):

"""

Perform a vector search in the MongoDB collection based on the user query.

Args:

user\_query (str): The user's query string.

collection (MongoCollection): The MongoDB collection to search.

Returns:

list: A list of matching documents.

"""

# Generate embedding for the user query

query\_embedding = get\_embedding(user\_query)

if query\_embedding is None:

return "Invalid query or embedding generation failed."

# Define the vector search pipeline

pipeline = [

{

"$vectorSearch": {

"index": "vector\_index",

"queryVector": query\_embedding,

"path": "embedding",

"numCandidates": 150, # Number of candidate matches to consider

"limit": 5, # Return top 5 matches

}

},

{

"$project": {

"\_id": 0, # Exclude the \_id field

"embedding": 0, # Exclude the embedding field

"score": {

"$meta": "vectorSearchScore" # Include the search score

},

}

},

]

# Execute the search

results = collection.aggregate(pipeline)

return list(results)

##  Step 6: Handling user queries with Claude 3 models

The final section of the tutorial outlines the sequence of operations performed as follows:

* Accept a user query in the form of a string.
* Utilize the VoyageAI embedding model to generate embeddings for the user query.
* Load the Anthropic Claude 3, specifically the ‘claude-opus-4-1’ model, to serve as the base model for the RAG system.
* Execute a vector search using the embeddings of the user query to fetch relevant information from the knowledge base, which provides additional context for the base model.
* Submit both the user query and the gathered additional information to the base model to generate a response.

An important note is that the dimensions of the user query embedding match the dimensions set in the vector search index definition on MongoDB Atlas.

The next step in this section is to import the anthropic library and load the client to access the anthropic’s methods for handling messages and accessing Claude models. Ensure you obtain an Claude API key located within the settings page on the [official Anthropic website(opens in new tab)](https://console.anthropic.com/settings/keys).

import anthropic

client = anthropic.Client(api\_key=userdata.get("ANTHROPIC\_API\_KEY"))

Below is a more detailed description of the operations in the code snippet below:

1. Vector Search Execution: The function begins by calling `vector_search` with the user's query and a specified collection as arguments. This performs a search within the collection, leveraging vector embeddings to find relevant information related to the query.
2. Compile Search Results: `search_result` is initialized as an empty string to aggregate information from the search. The search results are compiled by iterating over the results returned by the `vector_search` function, formates each item's details (title, company name, URL, publication date, article URL, and description) into a human-readable string, appending this information to search\_result with a newline character \n at the end of each entry.
3. Generate Response Using Anthropic Client: The function then constructs a request to the Claude API (through a client object, presumably an instance of the anthropic. Client class created earlier). It specifies:

* The model to use ("claude-opus-4-1") indicates a specific version of the Claude 3 model.
* The maximum token limit for the generated response (max\_tokens=1024).
* A system description guides the model to behave as a "Venture Capital Tech Analyst" with access to tech company articles and information, using this context to advise.
* The actual message for the model to process combines the user query with the aggregated search results as context.

1. Return the Generated Response and Search Results: It extracts and returns the response text from the first item in the response's content, alongside the compiled search results.

def handle\_user\_query(query, collection):

get\_knowledge = vector\_search(query, collection)

search\_result = ""

for result in get\_knowledge:

search\_result += (

f"Title: {result.get('title', 'N/A')}, "

f"Company Name: {result.get('companyName', 'N/A')}, "

f"Company URL: {result.get('companyUrl', 'N/A')}, "

f"Date Published: {result.get('published\_at', 'N/A')}, "

f"Article URL: {result.get('url', 'N/A')}, "

f"Description: {result.get('description', 'N/A')}, \n"

)

response = client.messages.create(

model="claude-opus-4-1",

max\_tokens=1024,

system="You are Venture Captital Tech Analyst with access to some tech company articles and information. You use the information you are given to provide advice.",

messages=[

{

"role": "user",

"content": "Answer this user query: "

+ query

+ " with the following context: "

+ search\_result,

}

],

)

return (response.content[0].text), search\_result

The final step in this tutorial is to initialize the query, pass it into the `handle_user_query` function and print the response returned.

# Conduct query with retrieval of sources

query = "Give me the best tech stock to invest in and tell me why"

response, source\_information = handle\_user\_query(query, collection)

print(f"Response: {response}")

print(f"\\nSource Information: \\n{source\_information}")

```
Response: Based on the information provided in the article titles and descriptions, Alibaba Group Holding Limited appears to be a top technology stock pick for 2023 according to renowned investor Ray Dalio. The article "Top 10 Technology Stocks to Buy in 2023 According to Ray Dalio" suggests that Alibaba is one of Dalio's favored tech investments for the year.

As a venture capital tech analyst, I would recommend considering an investment in Alibaba for the following reasons:

1. Endorsement from a respected investor: Ray Dalio, known for his successful investment strategies, has included Alibaba in his top 10 technology stock picks for 2023. His backing lends credibility to the investment potential of the company.

2. Strong market position: Alibaba is a leading e-commerce company in China with a significant market share. It has a diversified business model spanning e-commerce, cloud computing, digital media, and entertainment.

3. Growth potential: With China's large and growing middle class, Alibaba is well-positioned to benefit from increasing consumer spending and the shift towards online shopping.

However, it's essential to consider the following points as well:

1. Regulatory risks: Chinese tech companies, including Alibaba, have faced increased regulatory scrutiny in recent times. Changes in government policies could impact the company's growth and profitability.

2. Competition: While Alibaba is a dominant player, it faces competition from other tech giants like Tencent and JD.com in various business segments.

3. Geopolitical tensions: Ongoing tensions between the U.S. and China could lead to market volatility and impact investor sentiment towards Chinese stocks.

As with any investment, it's crucial to conduct thorough research, consider your risk tolerance, and diversify your portfolio. Keep in mind that the information provided here is based on limited data points, and stock prices can be influenced by various factors beyond the scope of this context.
Source Information: \nTitle: Top 10 Technology Stocks to Buy in 2023 According to Ray Dalio, Company Name: ALIBABA GROUP HOLDING LIMITED, Company URL: https://hackernoon.com/company/alibabagroupholdinglimited, Date Published: 2023-04-21 11:58:00, Article URL: https://uk.finance.yahoo.com/news/top-10-technology-stocks-buy-155830366.html, Description: In this article we discuss the top 10 technology stocks to buy in 2023 according to Ray Dalio. If you want to skip our detailed analysis of Dalio’s investment philosophy and portfolio construction,
Title: 3 Tech Stocks I Love Right Now, Company Name: 10Clouds, Company URL: https://hackernoon.com/company/10clouds, Date Published: 2023-04-02 11:30:00, Article URL: https://www.msn.com/en-xl/money/other/3-tech-stocks-i-love-right-now/ar-AA19n9Ht, Description: These are tech giants but they''re also great investments.,
Title: 3 Millionaire-Maker Hydrogen Stocks to Buy Before the Window Closes, Company Name: Air Products & Chemicals, Company URL: https://hackernoon.com/company/airproductschemicals, Date Published: 2023-07-28 12:18:00, Article URL: https://www.msn.com/en-us/money/topstocks/3-millionaire-maker-hydrogen-stocks-to-buy-before-the-window-closes/ar-AA1etN8O, Description: These are the best hydrogen stocks to buy with multibagger returns potential.More From InvestorPlace Buy This $5 Stock BEFORE This Apple Project Goes Live Wall Street Titan: Here’s My #1 Stock for 2023 The $1 Investment You MUST Take Advantage of Right Now It doesn’t matter if you have $500 or $5 million.,
Title: Why it may be time to sell the pop in tech stocks: BlackRock, Company Name: BlackRock, Company URL: https://hackernoon.com/company/blackrock, Date Published: 2023-02-13 19:06:00, Article URL: https://news.yahoo.com/why-it-may-be-time-to-sell-the-pop-in-tech-stocks-blackrock-190606866.html, Description: Household tech names like Apple Meta and Netflix have soared so far in 2023 but one strategist says the gains aren''t likely to last. It''s time to take profits on tech stocks — the early sector winner of 2023 — as the Federal Reserve may soon dash hopes for a pivot on interest rates,
Title: The harsh reality for investors eyeing tech stocks in 2023: Morning Brief, Company Name: 10Clouds, Company URL: https://hackernoon.com/company/10clouds, Date Published: 2023-01-02 11:18:00, Article URL: https://news.yahoo.com/the-harsh-reality-for-investors-eyeing-tech-stocks-in-2023-morning-brief-111854804.html, Description: Curious on how to buy battered tech stocks? Here''s a quick tip. More on that and what else to watch in business on Monday.,
```
