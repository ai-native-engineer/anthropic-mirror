<!-- source: https://platform.claude.com/cookbook/misc-read-web-pages-with-haiku -->

# Summarizing Web Page Content with Claude 3 Haiku

In this recipe, we'll learn how to fetch the content of a web page given its URL and then use Anthropic's Claude API to generate a summary of the page's content.

Let's start by installing the Anthropic library.

## Setup

First, let's install the necessary libraries and setup our Anthropic client with our API key.

python

```
# Install the necessary libraries
%pip install anthropic
```

python

```
# Import the required libraries
from anthropic import Anthropic

# Set up the Claude API client
client = Anthropic()
MODEL_NAME = "claude-haiku-4-5"
```

## Step 1: Fetching the Web Page Content

First, we need to fetch the content of the web page using the provided URL. We'll use the requests library for this purpose.

python

```
import requests

url = "https://en.wikipedia.org/wiki/96th_Academy_Awards"
response = requests.get(url, timeout=30)

if response.status_code == 200:
    page_content = response.text
else:
    print(f"Failed to fetch the web page. Status code: {response.status_code}")
    exit(1)
```

## Step 2: Preparing the Input for Claude

Next, we'll prepare the input for the Claude API. We'll create a message that includes the page content and a prompt asking Claude to summarize it.

python

```
prompt = (
    f"<content>{page_content}</content>Please produce a concise summary of the web page content."
)

messages = [{"role": "user", "content": prompt}]
```

## Step 3: Generating the Summary

Now, we'll call the Haiku to generate a summary of the web page content.

python

```
response = client.messages.create(model="claude-haiku-4-5", max_tokens=1024, messages=messages)

summary = response.content[0].text
print(summary)
```

```
The 96th Academy Awards ceremony took place on March 10, 2024 at the Dolby Theatre in Los Angeles. The ceremony, hosted by Jimmy Kimmel, presented Academy Awards (Oscars) in 23 categories honoring films released in 2023.

The big winner of the night was the film "Oppenheimer," which won a leading 7 awards including Best Picture, Best Director for Christopher Nolan, and several technical awards. Other major winners were "Poor Things" with 4 awards and "The Zone of Interest" with 2 awards. Several notable records and milestones were set, including Steven Spielberg receiving his 13th Best Picture nomination, and Billie Eilish and Finneas O'Connell becoming the youngest two-time Oscar winners.

The ceremony featured musical performances, tributes to past winners, and a touching "In Memoriam" segment. However, it also faced some criticism, such as the distracting and hard-to-follow "In Memoriam" presentation and political controversy around a director's comments about the Israel-Gaza conflict.
```
