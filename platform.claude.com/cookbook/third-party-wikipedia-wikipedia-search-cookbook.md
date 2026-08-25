<!-- source: https://platform.claude.com/cookbook/third-party-wikipedia-wikipedia-search-cookbook -->

#  Iteratively Searching Wikipedia with Claude

[DISCLAIMER: This notebook was created using Claude 2 models and is considered legacy.]

Some questions can't be answered by Claude off the top of Claude's head. Maybe they're about current events. Maybe you have an intensely detailed question that Claude hasn't memorized the answer to. No worries! With some prompting and scaffolding, Claude can search the web to find answers. In this notebook, we will create a virtual research assistant who has the ability to search Wikipedia to find answers to your question. The same approach can be used to allow Claude to search the broader web, or a set of documents you provide.

What is the approach? Broadly it falls under the category of "tool use". We create a search tool, tell Claude about it, and let it go to work. In pseudocode:

1. Prompt Claude with a description of the search tool, how it's best used, and how to "call" it (by issuing a special string).
2. Tell Claude your question.
3. Claude produces tokens like normal. If it produces the special string, terminate the token production stream, and issue a query to a search API.
4. Construct a new prompt which consists of the prompt from step 1, plus everything Claude generated up to the search call string, plus the results of the API call.
5. Repeat until Claude decides it's done.

Let's zoom in on the prompts for tool use and retrieval.

###  Prompts

# Tool Description Prompt

wikipedia\_prompt = """You will be asked a question by a human user. You have access to the following tool to help answer the question. <tool\_description> Search Engine Tool \* The search engine will exclusively search over Wikipedia for pages similar to your query. It returns for each page its title and full page content. Use this tool if you want to get up-to-date and comprehensive information on a topic to help answer queries. Queries should be as atomic as possible -- they only need to address one part of the user's question. For example, if the user's query is "what is the color of a basketball?", your search query should be "basketball". Here's another example: if the user's question is "Who created the first neural network?", your first query should be "neural network". As you can see, these queries are quite short. Think keywords, not phrases. \* At any time, you can make a call to the search engine using the following syntax: <search\_query>query\_word</search\_query>. \* You'll then get results back in <search\_result> tags.</tool\_description>"""

print(wikipedia\_prompt)

```
You will be asked a question by a human user. You have access to the following tool to help answer the question. <tool_description> Search Engine Tool * The search engine will exclusively search over Wikipedia for pages similar to your query. It returns for each page its title and full page content. Use this tool if you want to get up-to-date and comprehensive information on a topic to help answer queries. Queries should be as atomic as possible -- they only need to address one part of the user's question. For example, if the user's query is "what is the color of a basketball?", your search query should be "basketball". Here's another example: if the user's question is "Who created the first neural network?", your first query should be "neural network". As you can see, these queries are quite short. Think keywords, not phrases. * At any time, you can make a call to the search engine using the following syntax: <search_query>query_word</search_query>. * You'll then get results back in <search_result> tags.</tool_description>
```

Notice that there is a lot of advice in this prompt about how to search Wikipedia properly. We're all used to just typing random nonsense into Google and getting decent results because the query parsing logic is so good. Wikipedia search is not like that. As an example: consider the query "What's the best way to purchase potatoes in the United Arab Emirates". The [top hits for this on Wikipedia(opens in new tab)](https://en.wikipedia.org/w/index.php?search=What%27s+the+best+way+to+purchase+potatoes+in+the+United+Arab+Emirates&title=Special:Search&profile=advanced&fulltext=1&ns0=1) are for Slavery in the United States, 1973 Oil Crisis, Wendy's, and Tim Horton's (??). Meanwhile Google correctly takes you straight to Carrefour UAE.

Another difference is that Wikipedia search returns entire pages. With vector search, you might be getting narrower chunks, so you might want to ask for more results, use a more specific query, or both. The big-picture takeaway is that your results can vary a lot on your choices here so pay attention!

retrieval\_prompt = """Before beginning to research the user's question, first think for a moment inside <scratchpad> tags about what information is necessary for a well-informed answer. If the user's question is complex, you may need to decompose the query into multiple subqueries and execute them individually. Sometimes the search engine will return empty search results, or the search results may not contain the information you need. In such cases, feel free to try again with a different query.

After each call to the Search Engine Tool, reflect briefly inside <search\_quality></search\_quality> tags about whether you now have enough information to answer, or whether more information is needed. If you have all the relevant information, write it in <information></information> tags, WITHOUT actually answering the question. Otherwise, issue a new search.

Here is the user's question: <question>{query}</question> Remind yourself to make short queries in your scratchpad as you plan out your strategy."""

print(retrieval\_prompt)

```
Before beginning to research the user's question, first think for a moment inside <scratchpad> tags about what information is necessary for a well-informed answer. If the user's question is complex, you may need to decompose the query into multiple subqueries and execute them individually. Sometimes the search engine will return empty search results, or the search results may not contain the information you need. In such cases, feel free to try again with a different query.

After each call to the Search Engine Tool, reflect briefly inside <search_quality></search_quality> tags about whether you now have enough information to answer, or whether more information is needed. If you have all the relevant information, write it in <information></information> tags, WITHOUT actually answering the question. Otherwise, issue a new search.

Here is the user's question: <question>{query}</question> Remind yourself to make short queries in your scratchpad as you plan out your strategy.
```

We use a scratchpad here for the normal chain-of-thought reasons -- it makes Claude come up with a coherent plan to answer the question. The search quality reflection is used to induce Claude to be persistent and not jump the gun by answering the question before gathering all the relevant information. But why are we telling Claude to synthesize the information and not answer right away?

answer\_prompt = "Here is a user query: <query>{query}</query>. Here is some relevant information: <information>{information}</information>. Please answer the question using the relevant information."

print(answer\_prompt)

```
Here is a user query: <query>{query}</query>. Here is some relevant information: <information>{information}</information>. Please answer the question using the relevant information.
```

By extracting the information and presenting it to Claude in a new query, we allow Claude to focus all its attention on synthesizing the information into the right answer. Without this step, we found that Claude would sometimes precommit to an answer and then "justify" it with the search results, rather than allowing the results to guide it.

Now follows a bunch of code that implements the pseudocode for searching + retrieving + reprompting.

###  Search Implementation

import re

from abc import abstractmethod

from dataclasses import dataclass

import wikipedia

from anthropic import AI\_PROMPT, HUMAN\_PROMPT, Anthropic

@dataclass

class SearchResult:

"""

A single search result.

"""

content: str

class SearchTool:

"""

A search tool that can run a query and return a formatted string of search results.

"""

def \_\_init\_\_():

pass

@abstractmethod

def raw\_search(self, query: str, n\_search\_results\_to\_use: int) -> list[SearchResult]:

"""

Runs a query using the searcher, then returns the raw search results without formatting.

:param query: The query to run.

:param n\_search\_results\_to\_use: The number of results to return.

"""

raise NotImplementedError()

@abstractmethod

def process\_raw\_search\_results(

self,

results: list[SearchResult],

) -> list[str]:

"""

Extracts the raw search content from the search results and returns a list of strings that can be passed to Claude.

:param results: The search results to extract.

"""

raise NotImplementedError()

def search\_results\_to\_string(self, extracted: list[str]) -> str:

"""

Joins and formats the extracted search results as a string.

:param extracted: The extracted search results to format.

"""

result = "\n".join(

[

f'<item index="{i + 1}">\n<page\_content>\n{r}\n</page\_content>\n</item>'

for i, r in enumerate(extracted)

]

)

return result

def wrap\_search\_results(self, extracted: list[str]) -> str:

"""

Formats the extracted search results as a string, including the <search\_results> tags.

:param extracted: The extracted search results to format.

"""

return f"\n<search\_results>\n{self.search\_results\_to\_string(extracted)}\n</search\_results>"

def search(self, query: str, n\_search\_results\_to\_use: int) -> str:

raw\_search\_results = self.raw\_search(query, n\_search\_results\_to\_use)

processed\_search\_results = self.process\_raw\_search\_results(raw\_search\_results)

displayable\_search\_results = self.wrap\_search\_results(processed\_search\_results)

return displayable\_search\_results

@dataclass

class WikipediaSearchResult(SearchResult):

title: str

class WikipediaSearchTool(SearchTool):

def \_\_init\_\_(self, truncate\_to\_n\_tokens: int | None = 5000):

self.truncate\_to\_n\_tokens = truncate\_to\_n\_tokens

if truncate\_to\_n\_tokens is not None:

self.tokenizer = Anthropic().get\_tokenizer()

def raw\_search(self, query: str, n\_search\_results\_to\_use: int) -> list[WikipediaSearchResult]:

search\_results = self.\_search(query, n\_search\_results\_to\_use)

return search\_results

def process\_raw\_search\_results(self, results: list[WikipediaSearchResult]) -> list[str]:

processed\_search\_results = [

f"Page Title: {result.title.strip()}\nPage Content:\n{self.truncate\_page\_content(result.content)}"

for result in results

]

return processed\_search\_results

def truncate\_page\_content(self, page\_content: str) -> str:

if self.truncate\_to\_n\_tokens is None:

return page\_content.strip()

else:

return self.tokenizer.decode(

self.tokenizer.encode(page\_content).ids[: self.truncate\_to\_n\_tokens]

).strip()

def \_search(self, query: str, n\_search\_results\_to\_use: int) -> list[WikipediaSearchResult]:

results: list[str] = wikipedia.search(query)

search\_results: list[WikipediaSearchResult] = []

for result in results:

if len(search\_results) >= n\_search\_results\_to\_use:

break

try:

page = wikipedia.page(result)

print(page.url)

except wikipedia.exceptions.WikipediaException:

# The Wikipedia API is a little flaky, so we just skip over pages that fail to load

continue

content = page.content

title = page.title

search\_results.append(WikipediaSearchResult(content=content, title=title))

return search\_results

def extract\_between\_tags(tag: str, string: str, strip: bool = True) -> list[str]:

ext\_list = re.findall(rf"<{tag}\s?>(.+?)</{tag}\s?>", string, re.DOTALL)

if strip:

ext\_list = [e.strip() for e in ext\_list]

return ext\_list

class ClientWithRetrieval(Anthropic):

def \_\_init\_\_(self, search\_tool: SearchTool, verbose: bool = True, \*args, \*\*kwargs):

super().\_\_init\_\_(\*args, \*\*kwargs)

self.search\_tool = search\_tool

self.verbose = verbose

# Helper methods

def \_search\_query\_stop(

self, partial\_completion: str, n\_search\_results\_to\_use: int

) -> tuple[list[SearchResult], str]:

search\_query = extract\_between\_tags("search\_query", partial\_completion + "</search\_query>")

if search\_query is None:

raise Exception(

"Completion with retrieval failed as partial completion returned mismatched <search\_query> tags."

)

print(f"Running search query against SearchTool: {search\_query}")

search\_results = self.search\_tool.raw\_search(search\_query, n\_search\_results\_to\_use)

extracted\_search\_results = self.search\_tool.process\_raw\_search\_results(search\_results)

formatted\_search\_results = self.search\_tool.wrap\_search\_results(extracted\_search\_results)

return search\_results, formatted\_search\_results

def retrieve(

self,

query: str,

model: str,

n\_search\_results\_to\_use: int = 3,

stop\_sequences: list[str] = None,

max\_tokens\_to\_sample: int = 1000,

max\_searches\_to\_try: int = 5,

temperature: float = 1.0,

) -> tuple[list[SearchResult], str]:

if stop\_sequences is None:

stop\_sequences = [HUMAN\_PROMPT]

prompt = (

f"{HUMAN\_PROMPT} {wikipedia\_prompt} {retrieval\_prompt.format(query=query)}{AI\_PROMPT}"

)

starting\_prompt = prompt

print("Starting prompt:", starting\_prompt)

token\_budget = max\_tokens\_to\_sample

all\_raw\_search\_results: list[SearchResult] = []

for tries in range(max\_searches\_to\_try):

partial\_completion = self.completions.create(

prompt=prompt,

stop\_sequences=stop\_sequences + ["</search\_query>"],

model=model,

max\_tokens\_to\_sample=token\_budget,

temperature=temperature,

)

partial\_completion, stop\_reason, stop\_seq = (

partial\_completion.completion,

partial\_completion.stop\_reason,

partial\_completion.stop,

)

print(partial\_completion)

token\_budget -= self.count\_tokens(partial\_completion)

prompt += partial\_completion

if stop\_reason == "stop\_sequence" and stop\_seq == "</search\_query>":

print(f"Attempting search number {tries}.")

raw\_search\_results, formatted\_search\_results = self.\_search\_query\_stop(

partial\_completion, n\_search\_results\_to\_use

)

prompt += "</search\_query>" + formatted\_search\_results

all\_raw\_search\_results += raw\_search\_results

else:

break

final\_model\_response = prompt[len(starting\_prompt) :]

return all\_raw\_search\_results, final\_model\_response

# Main methods

def completion\_with\_retrieval(

self,

query: str,

model: str,

n\_search\_results\_to\_use: int = 3,

stop\_sequences: list[str] = None,

max\_tokens\_to\_sample: int = 1000,

max\_searches\_to\_try: int = 5,

temperature: float = 1.0,

) -> str:

if stop\_sequences is None:

stop\_sequences = [HUMAN\_PROMPT]

\_, retrieval\_response = self.retrieve(

query,

model=model,

n\_search\_results\_to\_use=n\_search\_results\_to\_use,

stop\_sequences=stop\_sequences,

max\_tokens\_to\_sample=max\_tokens\_to\_sample,

max\_searches\_to\_try=max\_searches\_to\_try,

temperature=temperature,

)

information = extract\_between\_tags("information", retrieval\_response)[-1]

prompt = f"{HUMAN\_PROMPT} {answer\_prompt.format(query=query, information=information)}{AI\_PROMPT}"

print("Summarizing:\n", prompt)

answer = self.completions.create(

prompt=prompt, model=model, temperature=temperature, max\_tokens\_to\_sample=1000

).completion

return answer

###  Running a Query

We're ready to execute a query! Let's pick something:

* recent, so it's less likely to be in Claude's training data, and
* compound/complex so it requires multiple searches.

import os

# Create a searcher

wikipedia\_search\_tool = WikipediaSearchTool()

ANTHROPIC\_SEARCH\_MODEL = "claude-2"

client = ClientWithRetrieval(

api\_key=os.environ["ANTHROPIC\_API\_KEY"], verbose=True, search\_tool=wikipedia\_search\_tool

)

query = "Which movie came out first: Oppenheimer, or Are You There God It's Me Margaret?"

augmented\_response = client.completion\_with\_retrieval(

query=query,

model=ANTHROPIC\_SEARCH\_MODEL,

n\_search\_results\_to\_use=1,

max\_searches\_to\_try=5,

max\_tokens\_to\_sample=1000,

temperature=0,

)

print(augmented\_response)

```
Starting prompt:

Human: You will be asked a question by a human user. You have access to the following tool to help answer the question. <tool_description> Search Engine Tool * The search engine will exclusively search over Wikipedia for pages similar to your query. It returns for each page its title and full page content. Use this tool if you want to get up-to-date and comprehensive information on a topic to help answer queries. Queries should be as atomic as possible -- they only need to address one part of the user's question. For example, if the user's query is "what is the color of a basketball?", your search query should be "basketball". Here's another example: if the user's question is "Who created the first neural network?", your first query should be "neural network". As you can see, these queries are quite short. Think keywords, not phrases. * At any time, you can make a call to the search engine using the following syntax: <search_query>query_word</search_query>. * You'll then get results back in <search_result> tags.</tool_description> Before beginning to research the user's question, first think for a moment inside <scratchpad> tags about what information is necessary for a well-informed answer. If the user's question is complex, you may need to decompose the query into multiple subqueries and execute them individually. Sometimes the search engine will return empty search results, or the search results may not contain the information you need. In such cases, feel free to try again with a different query.

After each call to the Search Engine Tool, reflect briefly inside <search_quality></search_quality> tags about whether you now have enough information to answer, or whether more information is needed. If you have all the relevant information, write it in <information></information> tags, WITHOUT actually answering the question. Otherwise, issue a new search.

Here is the user's question: <question>Which movie came out first: Oppenheimer, or Are You There God It's Me Margaret?</question> Remind yourself to make short queries in your scratchpad as you plan out your strategy.

Assistant:
 <scratchpad>
To answer this question, I need to find the release dates for the two movies:
- Oppenheimer release date
- Are You There God It's Me Margaret release date
I can search for each movie title individually to get the release date.
</scratchpad>

<search_query>Oppenheimer movie
Attempting search number 0.
Running search query against SearchTool: ['Oppenheimer movie']
https://en.wikipedia.org/wiki/Oppenheimer_(film)

The search results indicate that Oppenheimer is scheduled for theatrical release on July 21, 2023. This provides the release date for Oppenheimer.

<search_quality>The search results directly provided the release date for Oppenheimer, so I now have enough information to answer this part of the question.</search_quality>

<search_query>Are You There God It's Me Margaret movie
Attempting search number 1.
Running search query against SearchTool: ["Are You There God It's Me Margaret movie"]
https://en.wikipedia.org/wiki/Are_You_There_God%3F_It%27s_Me,_Margaret.

The search results indicate that the film adaptation of Are You There God? It's Me, Margaret was released on April 28, 2023. This provides the release date for Are You There God? It's Me, Margaret.

<search_quality>The search results directly stated the release date for the Are You There God? It's Me, Margaret movie adaptation, so I now have enough information to fully answer the question.</search_quality>

<information>
- Oppenheimer was released on July 21, 2023
- Are You There God? It's Me, Margaret was released on April 28, 2023
</information>

Based on the release dates found through my searches, Oppenheimer came out first, being released on July 21, 2023, while Are You There God? It's Me, Margaret was released later on April 28, 2023.
Summarizing:

Human:Here is a user query: <query>Which movie came out first: Oppenheimer, or Are You There God It's Me Margaret?</query>. Here is some relevant information: <information>- Oppenheimer was released on July 21, 2023
- Are You There God? It's Me, Margaret was released on April 28, 2023</information>. Please answer the question using the relevant information.

Assistant:
 Based on the information provided, Are You There God? It's Me, Margaret was released first, on April 28, 2023. Oppenheimer was released later, on July 21, 2023.
```

Cool, Claude was able to make a plan, execute the queries, and synthesize the information into an accurate answer. Note: without the extra information extraction step, Claude would sometimes determine the release dates of the movies correctly but then get the ordering wrong in its final answer. Let's do another.

augmented\_response = client.completion\_with\_retrieval(

query="Who won the 2023 NBA championship? Who was that team's best player in the year 2009?",

model=ANTHROPIC\_SEARCH\_MODEL,

n\_search\_results\_to\_use=1,

max\_searches\_to\_try=5,

max\_tokens\_to\_sample=1000,

temperature=0,

)

print(augmented\_response)

```
Starting prompt:

Human: You will be asked a question by a human user. You have access to the following tool to help answer the question. <tool_description> Search Engine Tool * The search engine will exclusively search over Wikipedia for pages similar to your query. It returns for each page its title and full page content. Use this tool if you want to get up-to-date and comprehensive information on a topic to help answer queries. Queries should be as atomic as possible -- they only need to address one part of the user's question. For example, if the user's query is "what is the color of a basketball?", your search query should be "basketball". Here's another example: if the user's question is "Who created the first neural network?", your first query should be "neural network". As you can see, these queries are quite short. Think keywords, not phrases. * At any time, you can make a call to the search engine using the following syntax: <search_query>query_word</search_query>. * You'll then get results back in <search_result> tags.</tool_description> Before beginning to research the user's question, first think for a moment inside <scratchpad> tags about what information is necessary for a well-informed answer. If the user's question is complex, you may need to decompose the query into multiple subqueries and execute them individually. Sometimes the search engine will return empty search results, or the search results may not contain the information you need. In such cases, feel free to try again with a different query.

After each call to the Search Engine Tool, reflect briefly inside <search_quality></search_quality> tags about whether you now have enough information to answer, or whether more information is needed. If you have all the relevant information, write it in <information></information> tags, WITHOUT actually answering the question. Otherwise, issue a new search.

Here is the user's question: <question>Who won the 2023 NBA championship? Who was that team's best player in the year 2009?</question> Remind yourself to make short queries in your scratchpad as you plan out your strategy.

Assistant:
 <scratchpad>
To answer this question, I need to find:
1. The team that won the 2023 NBA championship
2. The best player on that team in 2009
I can search for these things separately.
</scratchpad>

<search_query>2023 nba championship winner
Attempting search number 0.
Running search query against SearchTool: ['2023 nba championship winner']
https://en.wikipedia.org/wiki/List_of_NBA_champions

<search_quality>The search results contain the team that won the 2023 NBA championship, so I have the information I need to answer the first part of the question.</search_quality>

<information>
The Denver Nuggets won the 2023 NBA championship.
</information>

<search_query>denver nuggets best player 2009
Attempting search number 1.
Running search query against SearchTool: ['denver nuggets best player 2009']
https://en.wikipedia.org/wiki/2009%E2%80%9310_Denver_Nuggets_season

<search_quality>The search results indicate that Carmelo Anthony was the Nuggets' best player in 2009, so I now have all the information needed to fully answer the question.</search_quality>

<information>
- The Denver Nuggets won the 2023 NBA championship.
- Carmelo Anthony was the Nuggets' best player in 2009.
</information>
Summarizing:

Human:Here is a user query: <query>Who won the 2023 NBA championship? Who was that team's best player in the year 2009?</query>. Here is some relevant information: <information>- The Denver Nuggets won the 2023 NBA championship.
- Carmelo Anthony was the Nuggets' best player in 2009.</information>. Please answer the question using the relevant information.

Assistant:
 <response>
Based on the provided information:
- The Denver Nuggets won the 2023 NBA championship.
- Carmelo Anthony was the Nuggets' best player in 2009.
</response>
```

And there you have it! You may notice that the search tool code is nice and abstract and can be adapted to use a search API of your choice with minor modifications. Just remember to explain to Claude any tips it needs to use the tool well. You can even give Claude some few-shot examples of ideal query plans and query structure to improve performance further.
