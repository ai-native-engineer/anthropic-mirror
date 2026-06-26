<!-- source: https://platform.claude.com/docs/en/get-started -->

# Get started with Claude
Make your first API call to Claude and build a simple web search assistant.
Prerequisites
  * An Anthropic [Console account](https://platform.claude.com/)
  * An [API key](https://platform.claude.com/settings/keys)

Call the API
cURL
cURL
CLI
CLI
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby
  1. 1
Set your API key
Export your API key as an environment variable. The SDK reads `ANTHROPIC_API_KEY` automatically.

export ANTHROPIC_API_KEY="your-api-key-here"

  2. 2
Create a project and install the SDK

mkdir claude-quickstart && cd claude-quickstart
python3 -m venv .venv && source .venv/bin/activate
pip install anthropic

  3. 3
Create your code
Create a file called `quickstart.py`:
Python

import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1000,
    messages=[
            "role": "user",
            "content": "What should I search for to find the latest developments in renewable energy?",
    ],
)
print(message.content)

  4. 4
Run your code

python quickstart.py

Output

[TextBlock(citations=None, text='Here are some effective search strategies to find the latest developments in renewable energy:\n\n## General Search Terms\n- "Renewable energy news 2025"\n- ...', type='text')]

Next steps
You made your first API call. Next, learn the Messages API patterns you'll use in every Claude integration.
[ Working with the Messages API Learn multi-turn conversations, system prompts, stop reasons, and other core patterns. ](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)
Once you're comfortable with the basics, explore further:
[ Models overview Compare Claude models by capability and cost. ](https://platform.claude.com/docs/en/about-claude/models/overview)[ Features overview Browse all Claude capabilities: tools, context management, structured outputs, and more. ](https://platform.claude.com/docs/en/build-with-claude/overview)[  Client SDKs Reference documentation for Python, TypeScript, C#, and other client libraries. ](https://platform.claude.com/docs/en/cli-sdks-libraries/overview)
  * [Prerequisites](https://platform.claude.com/docs/en/get-started#prerequisites)
  * [Call the API](https://platform.claude.com/docs/en/get-started#call-the-api)
  * [Next steps](https://platform.claude.com/docs/en/get-started#next-steps)

Messages/First steps
# Get started with Claude
Make your first API call to Claude and build a simple web search assistant.
Prerequisites
  * An Anthropic [Console account](https://platform.claude.com/)
  * An [API key](https://platform.claude.com/settings/keys)

Call the API
cURL
cURL
CLI
CLI
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby
  1. 1
Set your API key
Export your API key as an environment variable. The SDK reads `ANTHROPIC_API_KEY` automatically.

export ANTHROPIC_API_KEY="your-api-key-here"

  2. 2
Create a project and install the SDK

mkdir claude-quickstart && cd claude-quickstart
python3 -m venv .venv && source .venv/bin/activate
pip install anthropic

  3. 3
Create your code
Create a file called `quickstart.py`:
Python

import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1000,
    messages=[
            "role": "user",
            "content": "What should I search for to find the latest developments in renewable energy?",
    ],
)
print(message.content)

  4. 4
Run your code

python quickstart.py

Output

[TextBlock(citations=None, text='Here are some effective search strategies to find the latest developments in renewable energy:\n\n## General Search Terms\n- "Renewable energy news 2025"\n- ...', type='text')]

Next steps
You made your first API call. Next, learn the Messages API patterns you'll use in every Claude integration.
[ Working with the Messages API Learn multi-turn conversations, system prompts, stop reasons, and other core patterns. ](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)
Once you're comfortable with the basics, explore further:
[ Models overview Compare Claude models by capability and cost. ](https://platform.claude.com/docs/en/about-claude/models/overview)[ Features overview Browse all Claude capabilities: tools, context management, structured outputs, and more. ](https://platform.claude.com/docs/en/build-with-claude/overview)[  Client SDKs Reference documentation for Python, TypeScript, C#, and other client libraries. ](https://platform.claude.com/docs/en/cli-sdks-libraries/overview)
