<!-- source: https://platform.claude.com/cookbook/multimodal-using-sub-agents -->

#  Using Haiku as a sub-agent

In this recipe, we'll demonstrate how to analyze Apple's 2023 financial earnings reports using Claude 3 Haiku sub-agent models to extract relevant information from earnings release PDFs. We'll then use Claude 3 Opus to generate a response to our question and create a graph using matplotlib to accompany its response.

##  Step 1: Set up the environment

First, let's install the required libraries and set up the Claude API client.



%pip install anthropic IPython PyMuPDF matplotlib



# Import the required libraries

import base64

import io

import os

from concurrent.futures import ThreadPoolExecutor

import fitz

import requests

from anthropic import Anthropic

from PIL import Image

# Set up the Claude API client

client = Anthropic()

MODEL\_NAME = "claude-haiku-4-5"

##  Step 2: Gather our documents and ask a question

For this example, we will be using all Apple's financial statements from the 2023 financial year and asking about the net sales over the year.



# List of Apple's earnings release PDF URLs

pdf\_urls = [

"https://www.apple.com/newsroom/pdfs/fy2023-q4/FY23\_Q4\_Consolidated\_Financial\_Statements.pdf",

"https://www.apple.com/newsroom/pdfs/fy2023-q3/FY23\_Q3\_Consolidated\_Financial\_Statements.pdf",

"https://www.apple.com/newsroom/pdfs/FY23\_Q2\_Consolidated\_Financial\_Statements.pdf",

"https://www.apple.com/newsroom/pdfs/FY23\_Q1\_Consolidated\_Financial\_Statements.pdf",

]

# User's question

QUESTION = "How did Apple's net sales change quarter to quarter in the 2023 financial year and what were the key contributors to the changes?"

##  Step 3: Download and convert PDFs to images

Next, we'll define functions to download the earnings release PDFs and convert them to base64-encoded PNG images. We have to do this because these PDFs are full of tables that are hard to parse with traditional PDF parsers. It's easier if we just convert them to images and pass the images to Haiku.

The `download_pdf` function downloads a PDF file from a given URL and saves it to the specified folder. The `pdf_to_base64_pngs` function converts a PDF to a list of base64-encoded PNG images.



# Function to download a PDF file from a URL and save it to a specified folder

def download\_pdf(url, folder):

response = requests.get(url, timeout=60)

if response.status\_code == 200:

file\_name = os.path.join(folder, url.split("/")[-1])

with open(file\_name, "wb") as file:

file.write(response.content)

return file\_name

else:

print(f"Failed to download PDF from {url}")

return None

# Define the function to convert a PDF to a list of base64-encoded PNG images

def pdf\_to\_base64\_pngs(pdf\_path, quality=75, max\_size=(1024, 1024)):

# Open the PDF file

doc = fitz.open(pdf\_path)

base64\_encoded\_pngs = []

# Iterate through each page of the PDF

for page\_num in range(doc.page\_count):

# Load the page

page = doc.load\_page(page\_num)

# Render the page as a PNG image

pix = page.get\_pixmap(matrix=fitz.Matrix(300 / 72, 300 / 72))

# Convert the pixmap to a PIL Image

image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

# Resize the image if it exceeds the maximum size

if image.size[0] > max\_size[0] or image.size[1] > max\_size[1]:

image.thumbnail(max\_size, Image.Resampling.LANCZOS)

# Convert the PIL Image to base64-encoded PNG

image\_data = io.BytesIO()

image.save(image\_data, format="PNG", optimize=True, quality=quality)

image\_data.seek(0)

base64\_encoded = base64.b64encode(image\_data.getvalue()).decode("utf-8")

base64\_encoded\_pngs.append(base64\_encoded)

# Close the PDF document

doc.close()

return base64\_encoded\_pngs

# Folder to save the downloaded PDFs

folder = "../images/using\_sub\_agents"

# Create the directory if it doesn't exist

os.makedirs(folder)

# Download the PDFs concurrently

with ThreadPoolExecutor() as executor:

pdf\_paths = list(executor.map(download\_pdf, pdf\_urls, [folder] \* len(pdf\_urls)))

# Remove any None values (failed downloads) from pdf\_paths

pdf\_paths = [path for path in pdf\_paths if path is not None]

We use ThreadPoolExecutor to download the PDFs concurrently and store the file paths in pdf\_paths.

##  Step 4: Generate a specific prompt for Haiku using Opus

Let's use Opus as an orchestrator and have it write a specific prompt for each Haiku sub-agent based on the user provided question.



def generate\_haiku\_prompt(question):

messages = [

{

"role": "user",

"content": [

{

"type": "text",

"text": f"Based on the following question, please generate a specific prompt for an LLM sub-agent to extract relevant information from an earning's report PDF. Each sub-agent only has access to a single quarter's earnings report. Output only the prompt and nothing else.\n\nQuestion: {question}",

}

],

}

]

response = client.messages.create(model="claude-opus-4-1", max\_tokens=2048, messages=messages)

return response.content[0].text

haiku\_prompt = generate\_haiku\_prompt(QUESTION)

print(haiku\_prompt)



```
Extract the following information from the Apple earnings report PDF for the quarter:
1. Apple's net sales for the quarter
2. Quarter-over-quarter change in net sales
3. Key product categories, services, or regions that contributed significantly to the change in net sales
4. Any explanations provided for the changes in net sales

Organize the extracted information in a clear, concise format focusing on the key data points and insights related to the change in net sales for the quarter.
```

##  Step 5: Extract information from PDFs

Now, let's define our question and extract information from the PDFs using sub-agent Haiku models. We format the information from each model into a neatly defined set of XML tags.



def extract\_info(pdf\_path, haiku\_prompt):

base64\_encoded\_pngs = pdf\_to\_base64\_pngs(pdf\_path)

messages = [

{

"role": "user",

"content": [

\*[

{

"type": "image",

"source": {

"type": "base64",

"media\_type": "image/png",

"data": base64\_encoded\_png,

},

}

for base64\_encoded\_png in base64\_encoded\_pngs

],

{"type": "text", "text": haiku\_prompt},

],

}

]

response = client.messages.create(model="claude-haiku-4-5", max\_tokens=2048, messages=messages)

return response.content[0].text, pdf\_path

def process\_pdf(pdf\_path):

return extract\_info(pdf\_path, haiku\_prompt)

# Process the PDFs concurrently with Haiku sub-agent models

with ThreadPoolExecutor() as executor:

extracted\_info\_list = list(executor.map(process\_pdf, pdf\_paths))

extracted\_info = ""

# Display the extracted information from each model call

for info in extracted\_info\_list:

extracted\_info += (

'<info quarter="' + info[1].split("/")[-1].split("\_")[1] + '">' + info[0] + "</info>\n"

)

print(extracted\_info)



```
<info quarter="Q4">According to the condensed consolidated statements of operations, Apple's net sales changed as follows in the 2023 financial year:

Quarter Ended September 30, 2023:
- Total net sales were $89,498 million, up from $90,146 million in the prior year quarter.
- Product sales were $67,184 million and services sales were $22,314 million.

Key contributors to the changes:
- Product sales decreased from $70,958 million in the prior year quarter.
- Services sales increased from $19,188 million in the prior year quarter.

Overall, Apple's total net sales decreased slightly compared to the same quarter in the prior year, driven by a decline in product sales which was partially offset by growth in services sales.</info>
<info quarter="Q3">Based on the financial statements provided, Apple's net sales changed as follows between the quarters in the 2023 financial year:

- Net sales increased from $81,797 million in the three months ended July 1, 2023 to $82,959 million in the three months ended June 25, 2022. This represents a quarter-over-quarter increase of around $1,162 million.

The key contributors to this increase appear to be:

- Products sales increased from $60,584 million to $63,355 million, an increase of around $2,771 million.
- Services sales increased from $21,213 million to $19,604 million, an increase of around $1,609 million.

So the growth in both product sales and services sales contributed to the overall increase in Apple's net sales between these two quarters in the 2023 fiscal year.</info>
<info quarter="Q2">According to the financial statements, Apple's net sales changed significantly between the quarters in the 2023 financial year:

- For the three months ended April 1, 2023, net sales were $94,836 million.
- For the six months ended March 26, 2022, net sales were $97,278 million.

This shows that net sales decreased by around $2,442 million from the prior six-month period to the most recent three-month period.

The key contributors to this change in net sales appear to be:

1. Products sales decreased from $107,560 million in the prior six-month period to $73,929 million in the recent three-month period.
2. Services sales increased from $41,673 million in the prior six-month period to $20,907 million in the recent three-month period.

So the decrease in product sales was the primary driver behind the overall decline in net sales from the prior period to the most recent quarter.</info>
<info quarter="Q1">According to the condensed consolidated statements of operations, Apple's net sales increased from $117,154 million in the three months ended December 31, 2022 to $123,945 million in the three months ended December 25, 2021. This represents a quarter-over-quarter increase in net sales.

The key contributors to this change were:

1. Increase in product sales revenue from $96,388 million to $104,429 million.
2. Increase in services revenue from $20,766 million to $19,516 million.

So the overall increase in net sales was driven primarily by higher product sales, with services revenue also showing a smaller increase quarter-over-quarter.</info>
```

We extract information from the PDFs concurrently using sub-agent models and combine the extracted information. We then prepare the messages for the powerful model, including the question and the extracted information, and ask it to generate a response and matplotlib code.

##  Step 6: Pass the information to Opus to generate a response

Now that we have fetched the information from each PDF using the sub-agents, let's call Opus to actually answer the question and write code to create a graph to accompany the answer.



# Prepare the messages for the powerful model

messages = [

{

"role": "user",

"content": [

{

"type": "text",

"text": f"Based on the following extracted information from Apple's earnings releases, please provide a response to the question: {QUESTION}\n\nAlso, please generate Python code using the matplotlib library to accompany your response. Enclose the code within <code> tags.\n\nExtracted Information:\n{extracted\_info}",

}

],

}

]

# Generate the matplotlib code using the powerful model

response = client.messages.create(model="claude-opus-4-1", max\_tokens=4096, messages=messages)

generated\_response = response.content[0].text

print("Generated Response:")

print(generated\_response)



```
Generated Response:
Based on the extracted information from Apple's earnings releases, Apple's net sales changed as follows in the 2023 financial year:

In Q1, net sales increased from $117,154 million in the previous quarter to $123,945 million, driven by increases in both product sales and services revenue.

In Q2, net sales decreased by around $2,442 million compared to the prior six-month period, primarily due to a decrease in product sales, which was partially offset by an increase in services sales.

In Q3, net sales increased by approximately $1,162 million compared to the previous quarter, with growth in both product sales and services sales contributing to the overall increase.

In Q4, total net sales decreased slightly compared to the same quarter in the prior year, driven by a decline in product sales, which was partially offset by growth in services sales.

Here's a Python code snippet using the matplotlib library to visualize the quarterly net sales data:

<code>
import matplotlib.pyplot as plt

quarters = ['Q1', 'Q2', 'Q3', 'Q4']
net_sales = [123945, 94836, 82959, 89498]

plt.figure(figsize=(8, 6))
plt.bar(quarters, net_sales, color='skyblue', width=0.6)
plt.xlabel('Quarter')
plt.ylabel('Net Sales (in millions)')
plt.title('Apple Net Sales by Quarter - FY 2023')
plt.xticks(quarters)
plt.yticks([0, 20000, 40000, 60000, 80000, 100000, 120000])
plt.grid(True, linestyle='--', alpha=0.5)

for i, v in enumerate(net_sales):
    plt.text(i, v + 1000, f'${v:,.0f}', ha='center', fontsize=10)

plt.show()
</code>

This code creates a bar chart showing Apple's net sales for each quarter in the 2023 financial year. The x-axis represents the quarters, and the y-axis represents the net sales in millions of dollars. The chart also includes data labels showing the exact net sales values for each quarter.
```

##  Step 7: Extract response and execute Matplotlib code

Finally, let's extract the matplotlib code from the generated response and execute it to visualize the revenue growth trend.

We define the `extract_code_and_response` function to extract the matplotlib code and non-code response from the generated response. We print the non-code response and execute the matplotlib code if it is found.

Note that it is not good practice to use `exec` on model-written code outside of a sandbox but for the purposes of this demo we are doing it :)



# Extract the matplotlib code from the response

# Function to extract the code and non-code parts from the response

def extract\_code\_and\_response(response):

start\_tag = "<code>"

end\_tag = "</code>"

start\_index = response.find(start\_tag)

end\_index = response.find(end\_tag)

if start\_index != -1 and end\_index != -1:

code = response[start\_index + len(start\_tag) : end\_index].strip()

non\_code\_response = response[:start\_index].strip()

return code, non\_code\_response

else:

return None, response.strip()

matplotlib\_code, non\_code\_response = extract\_code\_and\_response(generated\_response)

print(non\_code\_response)

if matplotlib\_code:

# Execute the extracted matplotlib code

# Note: exec is used here for demonstration purposes to run model-generated visualization code.

# In production, use a sandboxed environment for executing untrusted code.

exec(matplotlib\_code) # noqa: S102

else:

print("No matplotlib code found in the response.")
