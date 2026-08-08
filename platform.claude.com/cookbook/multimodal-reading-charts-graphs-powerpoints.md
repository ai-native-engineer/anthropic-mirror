<!-- source: https://platform.claude.com/cookbook/multimodal-reading-charts-graphs-powerpoints -->

#  Working with Charts, Graphs, and Slide Decks

Claude is highly capable of working with charts, graphs, and broader slide decks. Depending on your use case, there are a number of tips and tricks that you may want to take advantage of. This recipe will show you common patterns for using Claude with these materials.

##  Charts and Graphs

For the most part, using claude with charts and graphs is simple. Let's walk through how to ingest them and pass them to Claude, as well as some common tips to improve your results.

###  Ingestion and calling the Claude API

The best way to pass Claude charts and graphs is to take advantage of its vision capabilities and the PDF support feature. That is, give Claude a PDF document of the chart or graph, along with a text question about it.

At the moment, only `claude-sonnet-4-6` supports the PDF feature. Since the feature is still in beta, you will need to provide it with the `pdfs-2024-09-25` beta header.



# Install and create the Anthropic client.

%pip install anthropic



import base64

from anthropic import Anthropic

# While PDF support is in beta, you must pass in the correct beta header

client = Anthropic(default\_headers={"anthropic-beta": "pdfs-2024-09-25"})

# For now, only claude-sonnet-4-6 supports PDFs

MODEL\_NAME = "claude-sonnet-4-6"



# Make a useful helper function.

def get\_completion(messages):

response = client.messages.create(

model=MODEL\_NAME, max\_tokens=8192, temperature=0, messages=messages

)

return response.content[0].text



# To start, we'll need a PDF. We will be using the .pdf document located at cvna\_2021\_annual\_report.pdf.

# Start by reading in the PDF and encoding it as base64.

with open("./documents/cvna\_2021\_annual\_report.pdf", "rb") as pdf\_file:

binary\_data = pdf\_file.read()

base\_64\_encoded\_data = base64.b64encode(binary\_data)

base64\_string = base\_64\_encoded\_data.decode("utf-8")

Let's see how we can pass this document to the model alongside a simple question.



messages = [

{

"role": "user",

"content": [

{

"type": "document",

"source": {

"type": "base64",

"media\_type": "application/pdf",

"data": base64\_string,

},

},

{"type": "text", "text": "What's in this document? Answer in a single sentence."},

],

}

]

print(get\_completion(messages))



```
This is a page from Carvana's 2021 Annual Report showing four key metrics: retail units sold, total revenue, total markets at year end, and car vending machines, all displaying significant growth from 2014 to 2021.
```

That's pretty good! Now let's ask it some more useful questions.



questions = [

"What was CVNA revenue in 2020?",

"How many additional markets has Carvana added since 2014?",

"What was 2016 revenue per retail unit sold?",

]

for index, question in enumerate(questions):

messages = [

{

"role": "user",

"content": [

{

"type": "document",

"source": {

"type": "base64",

"media\_type": "application/pdf",

"data": base64\_string,

},

},

{"type": "text", "text": question},

],

}

]

print(f"\n----------Question {index + 1}----------")

print(get\_completion(messages))



```
----------Question 1----------
According to the graph showing Total Revenue ($M), Carvana's revenue in 2020 was $5,587 million (or approximately $5.59 billion).

----------Question 2----------
According to the "TOTAL MARKETS AT YEAR END" graph, Carvana started with 4 markets in 2014 and grew to 311 markets by 2021. Therefore, Carvana added 307 markets since 2014 (311 - 4 = 307 additional markets).

----------Question 3----------
Let me calculate this for you:

2016 Revenue: $365 million
2016 Retail Units Sold: 18,761 units

$365 million ÷ 18,761 units = $19,455 per unit (rounded to nearest dollar)

So in 2016, Carvana's revenue per retail unit sold was approximately $19,455.
```

As you can see, Claude is capable of answering fairly detailed questions about charts and graphs. However, there are some tips and tricks that will help you get the most out of it.

* Sometimes Claude's arithmetic capabilities get in the way. You'll notice that if you sample the third question above it will occasionally output an incorrect final answer because it messes up the arithmetic. Consider providing Claude with a calculator tool to ensure it doesn't make these types of mistakes.
* With super complicated charts and graphs, we can ask Claude to "First describe every data point you see in the document" as a way to elicit similar improvements to what we seen in traditional Chain of Thought.
* Claude occasionally struggles with charts that depend on lots of colors to convey information, such as grouped bar charts with many groups. Asking Claude to first identify the colors in your graph using HEX codes can boost its accuracy.

##  Slide Decks

Now that we know Claude is a charts and graphs wizard, it is only logical that we extend it to the true home of charts and graphs - slide decks!

Slides represent a critical source of information for many domains, including financial services. While you *can* use packages like PyPDF to extract text from slide decks, their chart/graph heavy nature often makes this a poor choice as models will struggle to access the information they actually need.

The PDF support feature can be a great replacement as a result. It uses both extracted text and vision in order when processing PDF documents. In this section we will go over how to use PDF documents in Claude to review slide decks, and how to deal with some common pitfalls of this approach.

The best way to get a typical slide deck into claude is to download it as a PDF and provide it directly to Claude.



# Open the multi-page PDF document the same way we did earlier.

with open("./documents/twilio\_q4\_2023.pdf", "rb") as pdf\_file:

binary\_data = pdf\_file.read()

base\_64\_encoded\_data = base64.b64encode(binary\_data)

base64\_string = base\_64\_encoded\_data.decode("utf-8")



# Now let's pass the document directly to Claude. Note that Claude will process both the text and visual elements of the document.

question = "What was Twilio y/y revenue growth for fiscal year 2023?"

content = [

{

"type": "document",

"source": {"type": "base64", "media\_type": "application/pdf", "data": base64\_string},

},

{"type": "text", "text": question},

]

messages = [{"role": "user", "content": content}]

print(get\_completion(messages))



```
According to the financial results shown in the presentation, Twilio's year-over-year revenue growth for fiscal year 2023 was 9%. This can be found in the "Total Company Results Highlights" section, which shows FY 2023 revenue growth of 9%.
```

This approach is a great way to get started, and for some use cases offers the best performance. However, there are some limitations.

* You can only include a total of 100 pages across all provided documents in a request (we intend to increase this limit over time).
* If you are using slide content as part of RAG, introducing multimodal PDFs into your embeddings can cause problems

Luckily, we can take advantage of Claude's vision capabilities to get a much higher quality representation of the slide deck **in text form** than normal pdf text extraction allows.

We find the best way to do this is to ask Claude to sequentially narrate the deck from start to finish, passing it the current slide and its prior narration. Let's see how.



# Define a prompt for narrating our slide deck. We would adjut this prompt based on the nature of the deck, but keep the structure largely the same.

prompt = """

You are the Twilio CFO, narrating your Q4 2023 earnings presentation.

The entire earnings presentation document is provided to you.

Please narrate this presentation from Twilio's Q4 2023 Earnings as if you were the presenter. Do not talk about any things, especially acronyms, if you are not exactly sure you know what they mean.

Do not leave any details un-narrated as some of your viewers are vision-impaired, so if you don't narrate every number they won't know the number.

Structure your response like this:

<narration>

<page\_narration id=1>

[Your narration for page 1]

</page\_narration>

<page\_narration id=2>

[Your narration for page 2]

</page\_narration>

... and so on for each page

</narration>

Use excruciating detail for each page, ensuring you describe every visual element and number present. Show the full response in a single message.

"""

messages = [

{

"role": "user",

"content": [

{

"type": "document",

"source": {

"type": "base64",

"media\_type": "application/pdf",

"data": base64\_string,

},

},

{"type": "text", "text": prompt},

],

}

]

# Now we use our prompt to narrate the entire deck. Note that this may take a few minutes to run (often up to 10).

completion = get\_completion(messages)



import re

# Next we'll parse the response from Claude using regex

pattern = r"<narration>(.\*?)</narration>"

match = re.search(pattern, completion.strip(), re.DOTALL)

if match:

narration = match.group(1)

else:

raise ValueError("No narration available. Likely due to the model response being truncated.")

Now that we have a text-based narration (it's far from perfect but it's pretty good), we have the ability to use this deck with any text-only workflow. Including vector search!

As a final sanity check, let's ask a few questions of our narration-only setup!



questions = [

"What percentage of q4 total revenue was the Segment business line?",

"Has the rate of growth of quarterly revenue been increasing or decreasing? Give just an answer.",

"What was acquisition revenue for the year ended december 31, 2023 (including negative revenues)?",

]

for index, question in enumerate(questions):

prompt = f"""You are an expert financial analyst analyzing a transcript of Twilio's earnings call.

Here is the transcript:

<transcript>

{narration}

</transcript>

Please answer the following question:

<question>

{question}

</question>"""

messages = [{"role": "user", "content": [{"type": "text", "text": prompt}]}]

print(f"\n----------Question {index + 1}----------")

print(get\_completion(messages))



```
----------Question 1----------
Let me calculate this:

Segment revenue in Q4 2023: $75 million
Total revenue in Q4 2023: $1,076 million

$75M ÷ $1,076M = 0.0697 or approximately 7%

Therefore, the Segment business line represented approximately 7% of Twilio's total Q4 2023 revenue.

----------Question 2----------
Decreasing. The transcript shows Q4 2023 revenue growth was 5% year-over-year, while for the full year 2023 revenue growth was 9% year-over-year, indicating a slowing growth rate. Additionally, the Q1 2024 guidance projects even lower growth of 2-3% year-over-year, confirming the declining trend.

----------Question 3----------
Let me help calculate the acquisition revenue for 2023.

From the transcript, we can see:
- Total revenue for 2023: $4,154 million
- Organic revenue for 2023: $4,146 million

Therefore, acquisition revenue would be:
Total Revenue - Organic Revenue = $4,154M - $4,146M = $8 million

So the acquisition revenue for the year ended December 31, 2023 was $8 million.

This can be verified by the fact that the difference between total revenue growth (9%) and organic revenue growth (10%) also suggests a small contribution from acquisitions.
```

Looks good! With these techniques at your side, you are ready to start applying models to chart and graph heavy content like slide decks.
