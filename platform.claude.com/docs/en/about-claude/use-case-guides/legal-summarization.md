<!-- source: https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization -->

# Legal summarization
This guide walks through how to leverage Claude's advanced natural language processing capabilities to efficiently summarize legal documents, extracting key information and expediting legal research. With Claude, you can streamline the review of contracts, litigation prep, and regulatory work, saving time and ensuring accuracy in your legal processes.
> Visit the [summarization cookbook](https://platform.claude.com/cookbook/capabilities-summarization-guide) to see an example legal summarization implementation using Claude.
Before building with Claude
### 
Decide whether to use Claude for legal summarization
Here are some key indicators that you should employ an LLM like Claude to summarize legal documents:
### You want to review a high volume of documents efficiently and affordably
### You require automated extraction of key metadata
### You want to generate clear, concise, and standardized summaries
### You need precise citations for your summaries
### You want to streamline and expedite your legal research process
### 
Determine the details you want the summarization to extract
There is no single correct summary for any given document. Without clear direction, it can be difficult for Claude to determine which details to include. To achieve optimal results, identify the specific information you want to include in the summary.
For instance, when summarizing a sublease agreement, you might wish to extract the following key points:

details_to_extract = [
    "Parties involved (sublessor, sublessee, and original lessor)",
    "Property details (address, description, and permitted use)",
    "Term and rent (start date, end date, monthly rent, and security deposit)",
    "Responsibilities (utilities, maintenance, and repairs)",
    "Consent and notices (landlord's consent, and notice requirements)",
    "Special provisions (furniture, parking, and subletting restrictions)",
]

### 
Establish success criteria
Evaluating the quality of summaries is a notoriously challenging task. Unlike many other natural language processing tasks, evaluation of summaries often lacks clear-cut, objective metrics. The process can be highly subjective, with different readers valuing different aspects of a summary. Here are criteria you may wish to consider when assessing how well Claude performs legal summarization.
### Factual correctness
### Legal precision
### Conciseness
### Consistency
### Readability
### Bias and fairness
See the guide on [establishing success criteria](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) for more information.
* * *
How to summarize legal documents using Claude
### 
Select the right Claude model
Model accuracy is extremely important when summarizing legal documents. Claude Opus 4.8 is an excellent choice for use cases such as this where high accuracy is required. If the size and quantity of your documents is large such that costs start to become a concern, you can also try using a smaller model like Claude Haiku 4.5.
To help estimate these costs, the following is a comparison of the cost to summarize 1,000 sublease agreements using both Opus and Haiku:
  * **Content size**
    * Number of agreements: 1,000
    * Characters per agreement: 300,000
    * Total characters: 300M
  * **Estimated tokens**
    * Input tokens: 86M (assuming 1 token per 3.5 characters)
    * Output tokens per summary: 350
    * Total output tokens: 350,000
  * **Claude Opus 4.8 estimated cost**
    * Input token cost: 86 MTok * $5.00/MTok = $430.00 USD
    * Output token cost: 0.35 MTok * $25.00/MTok = $8.75 USD
    * Total cost: $430.00 + $8.75 = $438.75 USD
  * **Claude Haiku 4.5 estimated cost**
    * Input token cost: 86 MTok * $1.00/MTok = $86.00 USD
    * Output token cost: 0.35 MTok * $5.00/MTok = $1.75 USD
    * Total cost: $86.00 + $1.75 = $87.75 USD


Actual costs may differ from these estimates. These estimates are based on the example highlighted in the section on [prompting](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization#build-a-strong-prompt).
### 
Transform documents into a format that Claude can process
Before you begin summarizing documents, you need to prepare your data. This involves extracting text from PDFs, cleaning the text, and ensuring it's ready to be processed by Claude.
Here is a demonstration of this process on a sample pdf:

from io import BytesIO
import re

import pypdf
import requests

def get_llm_text(pdf_file):
    reader = pypdf.PdfReader(pdf_file)
    text = "\n".join([page.extract_text() for page in reader.pages])

    # Remove page numbers
    text = re.sub(r"\n\s*\d+\s*\n", "\n", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    return text

# Create the full URL from the GitHub repository
url = "https://raw.githubusercontent.com/anthropics/anthropic-cookbook/main/skills/summarization/data/Sample Sublease Agreement.pdf"
url = url.replace(" ", "%20")

# Download the PDF file into memory
response = requests.get(url)

# Load the PDF from memory
pdf_file = BytesIO(response.content)

document_text = get_llm_text(pdf_file)
print(document_text[:50000])

In this example, you first download a pdf of a sample sublease agreement used in the [summarization cookbook](https://platform.claude.com/cookbook/capabilities-summarization-guide). This agreement was sourced from a publicly available sublease agreement from the [sec.gov website](https://www.sec.gov/Archives/edgar/data/1045425/000119312507044370/dex1032.htm).
The example uses the pypdf library to extract the contents of the pdf and convert it to text. The text data is then cleaned by removing page numbers and extra whitespace.
### 
Build a strong prompt
Claude can adapt to various summarization styles. You can change the details of the prompt to guide Claude to be more or less verbose, include more or less technical terminology, or provide a higher or lower level summary of the context at hand.
Here’s an example of how to create a prompt that ensures the generated summaries follow a consistent structure when analyzing sublease agreements:
Python

# Initialize the Anthropic client
client = anthropic.Anthropic()

def summarize_document(
    text, details_to_extract, model="claude-opus-4-8", max_tokens=1000
):
    # Format the details to extract to be placed within the prompt's context
    details_to_extract_str = "\n".join(details_to_extract)

    # Prompt the model to summarize the sublease agreement
    prompt = f"""Summarize the following sublease agreement. Focus on these key aspects:

    {details_to_extract_str}

    Provide the summary in bullet points nested within the XML header for each section. For example:

    <parties involved>
    - Sublessor: [Name]
    // Add more details as needed
    </parties involved>

    If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.

    Sublease agreement text:
    {text}
    """

    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system="You are a legal analyst specializing in real estate law, known for highly accurate and detailed summaries of sublease agreements.",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )

    return response.content[0].text

sublease_summary = summarize_document(document_text, details_to_extract)
print(sublease_summary)

This code implements a `summarize_document` function that uses Claude to summarize the contents of a sublease agreement. The function accepts a text string and a list of details to extract as inputs. In this example, the code calls the function with the `document_text` and `details_to_extract` variables that were defined in the previous code snippets.
Within the function, a prompt is generated for Claude, including the document to be summarized, the details to extract, and specific instructions for summarizing the document. The prompt instructs Claude to respond with a summary of each detail to extract nested within XML headers.
Because the code outputs each section of the summary within tags, each section can easily be parsed out as a post-processing step. This approach enables structured summaries that can be adapted for your use case, so that each summary follows the same pattern.
### 
Evaluate your prompt
Prompting often requires testing and optimization for it to be production ready. To determine the readiness of your solution, evaluate the quality of your summaries using a systematic process combining quantitative and qualitative methods. Creating a [strong empirical evaluation](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests#building-evals-and-test-cases) based on your defined success criteria allows you to optimize your prompts. Here are some metrics you may wish to include within your empirical evaluation:
### ROUGE scores
### BLEU scores
### Contextual embedding similarity
### LLM-based grading
### Human evaluation
### 
Deploy your prompt
Here are some additional considerations to keep in mind as you deploy your solution to production.
  1. **Ensure no liability:** Understand the legal implications of errors in the summaries, which could lead to legal liability for your organization or clients. Provide disclaimers or legal notices clarifying that the summaries are generated by AI and should be reviewed by legal professionals.
  2. **Handle diverse document types:** This guide discusses how to extract text from PDFs. In the real-world, documents may come in a variety of formats (PDFs, Word documents, text files, etc.). Ensure your data extraction pipeline can convert all of the file formats you expect to receive.
  3. **Parallelize API calls to Claude:** Long documents with a large number of tokens may require up to a minute for Claude to generate a summary. For large document collections, you may want to send API calls to Claude in parallel so that the summaries can be completed in a reasonable timeframe. Refer to Anthropic’s [rate limits](https://platform.claude.com/docs/en/api/rate-limits#rate-limits) to determine the maximum amount of API calls that can be performed in parallel.

* * *
Improve performance
In complex scenarios, it may be helpful to consider additional strategies to improve performance beyond standard [prompt engineering techniques](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview). Here are some advanced strategies:
### 
Perform meta-summarization to summarize long documents
Legal summarization often involves handling long documents or many related documents at once, such that you surpass Claude’s context window. You can use a chunking method known as meta-summarization in order to handle this use case. This technique involves breaking down documents into smaller, manageable chunks and then processing each chunk separately. You can then combine the summaries of each chunk to create a meta-summary of the entire document.
Here's an example of how to perform meta-summarization:
Python

# Initialize the Anthropic client
client = anthropic.Anthropic()

def chunk_text(text, chunk_size=20000):
    return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]

def summarize_long_document(
    text, details_to_extract, model="claude-opus-4-8", max_tokens=1000
):
    # Format the details to extract to be placed within the prompt's context
    details_to_extract_str = "\n".join(details_to_extract)

    # Iterate over chunks and summarize each one
    chunk_summaries = [
        summarize_document(
            chunk, details_to_extract, model=model, max_tokens=max_tokens
        )
        for chunk in chunk_text(text)
    ]

    final_summary_prompt = f"""

    You are looking at the chunked summaries of multiple documents that are all related.
    Combine the following summaries of the document from different truthful sources into a coherent overall summary:

    <chunked_summaries>
    {"".join(chunk_summaries)}
    </chunked_summaries>

    Focus on these key aspects:
    {details_to_extract_str}

    Provide the summary in bullet points nested within the XML header for each section. For example:

    <parties involved>
    - Sublessor: [Name]
    // Add more details as needed
    </parties involved>

    If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.
    """

    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system="You are a legal expert that summarizes notes on one document.",
        messages=[
            {"role": "user", "content": final_summary_prompt},
        ],
    )

    return response.content[0].text

long_summary = summarize_long_document(document_text, details_to_extract)
print(long_summary)

The `summarize_long_document` function builds upon the earlier `summarize_document` function by splitting the document into smaller chunks and summarizing each chunk individually.
The code achieves this by applying the `summarize_document` function to each chunk of 20,000 characters within the original document. The individual summaries are then combined, and a final summary is created from these chunk summaries.
Note that the `summarize_long_document` function isn't strictly necessary for the example pdf, as the entire document fits within Claude's context window. However, it becomes essential for documents exceeding Claude's context window or when summarizing multiple related documents together. Regardless, this meta-summarization technique often captures additional important details in the final summary that were missed in the earlier single-summary approach.
### 
Use summary indexed documents to explore a large collection of documents
Searching a collection of documents with an LLM usually involves retrieval-augmented generation (RAG). However, in scenarios involving large documents or when precise information retrieval is crucial, a basic RAG approach may be insufficient. Summary indexed documents is an advanced RAG approach that provides a more efficient way of ranking documents for retrieval, using less context than traditional RAG methods. In this approach, you first use Claude to generate a concise summary for each document in your corpus, and then use Claude to rank the relevance of each summary to the query being asked. For further details on this approach, including a code-based example, check out the summary indexed documents section in the [summarization cookbook](https://platform.claude.com/cookbook/capabilities-summarization-guide).
### 
Fine-tune Claude to learn from your dataset
Another advanced technique to improve Claude's ability to generate summaries is fine-tuning. Fine-tuning involves training Claude on a custom dataset that specifically aligns with your legal summarization needs, ensuring that Claude adapts to your use case. Here’s an overview on how to perform fine-tuning:
  1. **Identify errors:** Start by collecting instances where Claude’s summaries fall short - this could include missing critical legal details, misunderstanding context, or using inappropriate legal terminology.
  2. **Curate a dataset:** Once you've identified these issues, compile a dataset of these problematic examples. This dataset should include the original legal documents alongside your corrected summaries, ensuring that Claude learns the desired behavior.
  3. **Perform fine-tuning:** Fine-tuning involves retraining the model on your curated dataset to adjust its weights and parameters. This retraining helps Claude better understand the specific requirements of your legal domain, improving its ability to summarize documents according to your standards.
  4. **Iterative improvement:** Fine-tuning is not a one-time process. As Claude continues to generate summaries, you can iteratively add new examples where it has underperformed, further refining its capabilities. Over time, this continuous feedback loop will result in a model that is highly specialized for your legal summarization tasks.


Fine-tuning is currently only available via Amazon Bedrock. Additional details are available in the [AWS launch blog](https://aws.amazon.com/blogs/machine-learning/fine-tune-anthropics-claude-3-haiku-in-amazon-bedrock-to-boost-model-accuracy-and-quality/).
[  Summarization cookbook  View a fully implemented code-based example of how to use Claude to summarize contracts. ](https://platform.claude.com/cookbook/capabilities-summarization-guide)[  Citations cookbook  Explore the Citations cookbook recipe for guidance on how to ensure accuracy and explainability of information. ](https://platform.claude.com/cookbook/misc-using-citations)
  * [Before building with Claude](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization#before-building-with-claude)
  * [Decide whether to use Claude for legal summarization](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization#decide-whether-to-use-claude-for-legal-summarization)
  * [Determine the details you want the summarization to extract](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization#determine-the-details-you-want-the-summarization-to-extract)
  * [Establish success criteria](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization#establish-success-criteria)
  * [How to summarize legal documents using Claude](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization#how-to-summarize-legal-documents-using-claude)
  * [Select the right Claude model](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization#select-the-right-claude-model)
  * [Transform documents into a format that Claude can process](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization#transform-documents-into-a-format-that-claude-can-process)
  * [Build a strong prompt](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization#build-a-strong-prompt)
  * [Evaluate your prompt](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization#evaluate-your-prompt)
  * [Deploy your prompt](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization#deploy-your-prompt)
  * [Improve performance](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization#improve-performance)
  * [Perform meta-summarization to summarize long documents](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization#perform-meta-summarization-to-summarize-long-documents)
  * [Use summary indexed documents to explore a large collection of documents](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization#use-summary-indexed-documents-to-explore-a-large-collection-of-documents)
  * [Fine-tune Claude to learn from your dataset](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization#fine-tune-claude-to-learn-from-your-dataset)

Best practices/Use cases
# Legal summarization
This guide walks through how to leverage Claude's advanced natural language processing capabilities to efficiently summarize legal documents, extracting key information and expediting legal research. With Claude, you can streamline the review of contracts, litigation prep, and regulatory work, saving time and ensuring accuracy in your legal processes.
> Visit the [summarization cookbook](https://platform.claude.com/cookbook/capabilities-summarization-guide) to see an example legal summarization implementation using Claude.
Before building with Claude
### 
Decide whether to use Claude for legal summarization
Here are some key indicators that you should employ an LLM like Claude to summarize legal documents:
### You want to review a high volume of documents efficiently and affordably
### You require automated extraction of key metadata
### You want to generate clear, concise, and standardized summaries
### You need precise citations for your summaries
### You want to streamline and expedite your legal research process
### 
Determine the details you want the summarization to extract
There is no single correct summary for any given document. Without clear direction, it can be difficult for Claude to determine which details to include. To achieve optimal results, identify the specific information you want to include in the summary.
For instance, when summarizing a sublease agreement, you might wish to extract the following key points:

details_to_extract = [
    "Parties involved (sublessor, sublessee, and original lessor)",
    "Property details (address, description, and permitted use)",
    "Term and rent (start date, end date, monthly rent, and security deposit)",
    "Responsibilities (utilities, maintenance, and repairs)",
    "Consent and notices (landlord's consent, and notice requirements)",
    "Special provisions (furniture, parking, and subletting restrictions)",
]

### 
Establish success criteria
Evaluating the quality of summaries is a notoriously challenging task. Unlike many other natural language processing tasks, evaluation of summaries often lacks clear-cut, objective metrics. The process can be highly subjective, with different readers valuing different aspects of a summary. Here are criteria you may wish to consider when assessing how well Claude performs legal summarization.
### Factual correctness
### Legal precision
### Conciseness
### Consistency
### Readability
### Bias and fairness
See the guide on [establishing success criteria](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) for more information.
* * *
How to summarize legal documents using Claude
### 
Select the right Claude model
Model accuracy is extremely important when summarizing legal documents. Claude Opus 4.8 is an excellent choice for use cases such as this where high accuracy is required. If the size and quantity of your documents is large such that costs start to become a concern, you can also try using a smaller model like Claude Haiku 4.5.
To help estimate these costs, the following is a comparison of the cost to summarize 1,000 sublease agreements using both Opus and Haiku:
  * **Content size**
    * Number of agreements: 1,000
    * Characters per agreement: 300,000
    * Total characters: 300M
  * **Estimated tokens**
    * Input tokens: 86M (assuming 1 token per 3.5 characters)
    * Output tokens per summary: 350
    * Total output tokens: 350,000
  * **Claude Opus 4.8 estimated cost**
    * Input token cost: 86 MTok * $5.00/MTok = $430.00 USD
    * Output token cost: 0.35 MTok * $25.00/MTok = $8.75 USD
    * Total cost: $430.00 + $8.75 = $438.75 USD
  * **Claude Haiku 4.5 estimated cost**
    * Input token cost: 86 MTok * $1.00/MTok = $86.00 USD
    * Output token cost: 0.35 MTok * $5.00/MTok = $1.75 USD
    * Total cost: $86.00 + $1.75 = $87.75 USD


Actual costs may differ from these estimates. These estimates are based on the example highlighted in the section on [prompting](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization#build-a-strong-prompt).
### 
Transform documents into a format that Claude can process
Before you begin summarizing documents, you need to prepare your data. This involves extracting text from PDFs, cleaning the text, and ensuring it's ready to be processed by Claude.
Here is a demonstration of this process on a sample pdf:

from io import BytesIO
import re

import pypdf
import requests

def get_llm_text(pdf_file):
    reader = pypdf.PdfReader(pdf_file)
    text = "\n".join([page.extract_text() for page in reader.pages])

    # Remove page numbers
    text = re.sub(r"\n\s*\d+\s*\n", "\n", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    return text

# Create the full URL from the GitHub repository
url = "https://raw.githubusercontent.com/anthropics/anthropic-cookbook/main/skills/summarization/data/Sample Sublease Agreement.pdf"
url = url.replace(" ", "%20")

# Download the PDF file into memory
response = requests.get(url)

# Load the PDF from memory
pdf_file = BytesIO(response.content)

document_text = get_llm_text(pdf_file)
print(document_text[:50000])

In this example, you first download a pdf of a sample sublease agreement used in the [summarization cookbook](https://platform.claude.com/cookbook/capabilities-summarization-guide). This agreement was sourced from a publicly available sublease agreement from the [sec.gov website](https://www.sec.gov/Archives/edgar/data/1045425/000119312507044370/dex1032.htm).
The example uses the pypdf library to extract the contents of the pdf and convert it to text. The text data is then cleaned by removing page numbers and extra whitespace.
### 
Build a strong prompt
Claude can adapt to various summarization styles. You can change the details of the prompt to guide Claude to be more or less verbose, include more or less technical terminology, or provide a higher or lower level summary of the context at hand.
Here’s an example of how to create a prompt that ensures the generated summaries follow a consistent structure when analyzing sublease agreements:
Python

# Initialize the Anthropic client
client = anthropic.Anthropic()

def summarize_document(
    text, details_to_extract, model="claude-opus-4-8", max_tokens=1000
):
    # Format the details to extract to be placed within the prompt's context
    details_to_extract_str = "\n".join(details_to_extract)

    # Prompt the model to summarize the sublease agreement
    prompt = f"""Summarize the following sublease agreement. Focus on these key aspects:

    {details_to_extract_str}

    Provide the summary in bullet points nested within the XML header for each section. For example:

    <parties involved>
    - Sublessor: [Name]
    // Add more details as needed
    </parties involved>

    If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.

    Sublease agreement text:
    {text}
    """

    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system="You are a legal analyst specializing in real estate law, known for highly accurate and detailed summaries of sublease agreements.",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )

    return response.content[0].text

sublease_summary = summarize_document(document_text, details_to_extract)
print(sublease_summary)

This code implements a `summarize_document` function that uses Claude to summarize the contents of a sublease agreement. The function accepts a text string and a list of details to extract as inputs. In this example, the code calls the function with the `document_text` and `details_to_extract` variables that were defined in the previous code snippets.
Within the function, a prompt is generated for Claude, including the document to be summarized, the details to extract, and specific instructions for summarizing the document. The prompt instructs Claude to respond with a summary of each detail to extract nested within XML headers.
Because the code outputs each section of the summary within tags, each section can easily be parsed out as a post-processing step. This approach enables structured summaries that can be adapted for your use case, so that each summary follows the same pattern.
### 
Evaluate your prompt
Prompting often requires testing and optimization for it to be production ready. To determine the readiness of your solution, evaluate the quality of your summaries using a systematic process combining quantitative and qualitative methods. Creating a [strong empirical evaluation](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests#building-evals-and-test-cases) based on your defined success criteria allows you to optimize your prompts. Here are some metrics you may wish to include within your empirical evaluation:
### ROUGE scores
### BLEU scores
### Contextual embedding similarity
### LLM-based grading
### Human evaluation
### 
Deploy your prompt
Here are some additional considerations to keep in mind as you deploy your solution to production.
  1. **Ensure no liability:** Understand the legal implications of errors in the summaries, which could lead to legal liability for your organization or clients. Provide disclaimers or legal notices clarifying that the summaries are generated by AI and should be reviewed by legal professionals.
  2. **Handle diverse document types:** This guide discusses how to extract text from PDFs. In the real-world, documents may come in a variety of formats (PDFs, Word documents, text files, etc.). Ensure your data extraction pipeline can convert all of the file formats you expect to receive.
  3. **Parallelize API calls to Claude:** Long documents with a large number of tokens may require up to a minute for Claude to generate a summary. For large document collections, you may want to send API calls to Claude in parallel so that the summaries can be completed in a reasonable timeframe. Refer to Anthropic’s [rate limits](https://platform.claude.com/docs/en/api/rate-limits#rate-limits) to determine the maximum amount of API calls that can be performed in parallel.

* * *
Improve performance
In complex scenarios, it may be helpful to consider additional strategies to improve performance beyond standard [prompt engineering techniques](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview). Here are some advanced strategies:
### 
Perform meta-summarization to summarize long documents
Legal summarization often involves handling long documents or many related documents at once, such that you surpass Claude’s context window. You can use a chunking method known as meta-summarization in order to handle this use case. This technique involves breaking down documents into smaller, manageable chunks and then processing each chunk separately. You can then combine the summaries of each chunk to create a meta-summary of the entire document.
Here's an example of how to perform meta-summarization:
Python

# Initialize the Anthropic client
client = anthropic.Anthropic()

def chunk_text(text, chunk_size=20000):
    return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]

def summarize_long_document(
    text, details_to_extract, model="claude-opus-4-8", max_tokens=1000
):
    # Format the details to extract to be placed within the prompt's context
    details_to_extract_str = "\n".join(details_to_extract)

    # Iterate over chunks and summarize each one
    chunk_summaries = [
        summarize_document(
            chunk, details_to_extract, model=model, max_tokens=max_tokens
        )
        for chunk in chunk_text(text)
    ]

    final_summary_prompt = f"""

    You are looking at the chunked summaries of multiple documents that are all related.
    Combine the following summaries of the document from different truthful sources into a coherent overall summary:

    <chunked_summaries>
    {"".join(chunk_summaries)}
    </chunked_summaries>

    Focus on these key aspects:
    {details_to_extract_str}

    Provide the summary in bullet points nested within the XML header for each section. For example:

    <parties involved>
    - Sublessor: [Name]
    // Add more details as needed
    </parties involved>

    If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.
    """

    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system="You are a legal expert that summarizes notes on one document.",
        messages=[
            {"role": "user", "content": final_summary_prompt},
        ],
    )

    return response.content[0].text

long_summary = summarize_long_document(document_text, details_to_extract)
print(long_summary)

The `summarize_long_document` function builds upon the earlier `summarize_document` function by splitting the document into smaller chunks and summarizing each chunk individually.
The code achieves this by applying the `summarize_document` function to each chunk of 20,000 characters within the original document. The individual summaries are then combined, and a final summary is created from these chunk summaries.
Note that the `summarize_long_document` function isn't strictly necessary for the example pdf, as the entire document fits within Claude's context window. However, it becomes essential for documents exceeding Claude's context window or when summarizing multiple related documents together. Regardless, this meta-summarization technique often captures additional important details in the final summary that were missed in the earlier single-summary approach.
### 
Use summary indexed documents to explore a large collection of documents
Searching a collection of documents with an LLM usually involves retrieval-augmented generation (RAG). However, in scenarios involving large documents or when precise information retrieval is crucial, a basic RAG approach may be insufficient. Summary indexed documents is an advanced RAG approach that provides a more efficient way of ranking documents for retrieval, using less context than traditional RAG methods. In this approach, you first use Claude to generate a concise summary for each document in your corpus, and then use Claude to rank the relevance of each summary to the query being asked. For further details on this approach, including a code-based example, check out the summary indexed documents section in the [summarization cookbook](https://platform.claude.com/cookbook/capabilities-summarization-guide).
### 
Fine-tune Claude to learn from your dataset
Another advanced technique to improve Claude's ability to generate summaries is fine-tuning. Fine-tuning involves training Claude on a custom dataset that specifically aligns with your legal summarization needs, ensuring that Claude adapts to your use case. Here’s an overview on how to perform fine-tuning:
  1. **Identify errors:** Start by collecting instances where Claude’s summaries fall short - this could include missing critical legal details, misunderstanding context, or using inappropriate legal terminology.
  2. **Curate a dataset:** Once you've identified these issues, compile a dataset of these problematic examples. This dataset should include the original legal documents alongside your corrected summaries, ensuring that Claude learns the desired behavior.
  3. **Perform fine-tuning:** Fine-tuning involves retraining the model on your curated dataset to adjust its weights and parameters. This retraining helps Claude better understand the specific requirements of your legal domain, improving its ability to summarize documents according to your standards.
  4. **Iterative improvement:** Fine-tuning is not a one-time process. As Claude continues to generate summaries, you can iteratively add new examples where it has underperformed, further refining its capabilities. Over time, this continuous feedback loop will result in a model that is highly specialized for your legal summarization tasks.


Fine-tuning is currently only available via Amazon Bedrock. Additional details are available in the [AWS launch blog](https://aws.amazon.com/blogs/machine-learning/fine-tune-anthropics-claude-3-haiku-in-amazon-bedrock-to-boost-model-accuracy-and-quality/).
[  Summarization cookbook  View a fully implemented code-based example of how to use Claude to summarize contracts. ](https://platform.claude.com/cookbook/capabilities-summarization-guide)[  Citations cookbook  Explore the Citations cookbook recipe for guidance on how to ensure accuracy and explainability of information. ](https://platform.claude.com/cookbook/misc-using-citations)
