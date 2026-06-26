<!-- source: https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart -->

# CLI quickstart
Install the ant command-line tool, authenticate, and send your first request to the Claude API.
The `ant` CLI provides access to the Claude API from your terminal. Every API resource is exposed as a subcommand, with output formatting, response filtering, and YAML or JSON file input.
The ant CLI in action.
Compared to `curl`, `ant` builds request bodies from typed flags or piped YAML instead of hand-written JSON, and inlines file contents into string fields with an `@path` reference. It extracts response fields with a built-in `--transform` query, so you don't need a separate tool like `jq`, and it paginates list endpoints automatically.
For endpoint-specific parameters and response schemas, see the [API reference](https://platform.claude.com/docs/en/api/cli/messages/create). This page gets you to a working command. For everything else the CLI does, see [Using the CLI](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/using) and [CLI scripting and automation](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/scripting).
Installation
Homebrew (macOS)
Homebrew (macOS)
curl (Linux/WSL)
curl (Linux/WSL)
Go
Go

brew install anthropics/tap/ant

Check the installation:

ant --version

Authentication
`ant auth login` opens a browser-based OAuth flow against the Claude Console and stores the resulting credentials locally, so you can call the API without creating or managing an API key.
CLI

ant auth login

For other ways to authenticate (API key environment variable, headless hosts, multiple workspaces, named profiles, and Workload Identity Federation), see [CLI authentication options](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/authentication).
Send your first request
With the binary installed and authenticated, call the [Messages API](https://platform.claude.com/docs/en/api/cli/messages/create):

ant messages create \
  --model claude-opus-4-8 \
  --max-tokens 1024 \
  --message '{role: user, content: "Hello, Claude"}'

Output

  "model": "claude-opus-4-8",
  "id": "msg_01YMmR5XodC5nTqMxLZMKaq6",
  "type": "message",
  "role": "assistant",
  "content": [
      "type": "text",
      "text": "Hello! How are you doing today? Is there something I can help you with?"
  ],
  "stop_reason": "end_turn",
  "usage": { "input_tokens": 27, "output_tokens": 20 /*, ... */ }

The response is the full API object, pretty-printed because stdout is a terminal.
Shell completion
The CLI ships completion scripts for bash, zsh, fish, and PowerShell. Generate and install one for your shell:
zsh
zsh
bash
bash
fish
fish
PowerShell
PowerShell

ant @completion zsh > "${fpath[1]}/_ant"
# Restart your shell or run: autoload -U compinit && compinit

Next steps
[  CLI authentication options API keys, headless hosts, multiple workspaces, and named profiles ](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/authentication)[ Using the CLI Command structure, output formats, GJSON transforms, and request bodies ](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/using)[  CLI scripting and automation Version-control API resources, scripting patterns, and use from Claude Code ](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/scripting)
  * [Installation](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart#installation)
  * [Authentication](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart#authentication)
  * [Send your first request](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart#send-your-first-request)
  * [Shell completion](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart#shell-completion)
  * [Next steps](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart#next-steps)

CLI, SDKs, and libraries/ant CLI
# CLI quickstart
Install the ant command-line tool, authenticate, and send your first request to the Claude API.
The `ant` CLI provides access to the Claude API from your terminal. Every API resource is exposed as a subcommand, with output formatting, response filtering, and YAML or JSON file input.
The ant CLI in action.
Compared to `curl`, `ant` builds request bodies from typed flags or piped YAML instead of hand-written JSON, and inlines file contents into string fields with an `@path` reference. It extracts response fields with a built-in `--transform` query, so you don't need a separate tool like `jq`, and it paginates list endpoints automatically.
For endpoint-specific parameters and response schemas, see the [API reference](https://platform.claude.com/docs/en/api/cli/messages/create). This page gets you to a working command. For everything else the CLI does, see [Using the CLI](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/using) and [CLI scripting and automation](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/scripting).
Installation
Homebrew (macOS)
Homebrew (macOS)
curl (Linux/WSL)
curl (Linux/WSL)
Go
Go

brew install anthropics/tap/ant

Check the installation:

ant --version

Authentication
`ant auth login` opens a browser-based OAuth flow against the Claude Console and stores the resulting credentials locally, so you can call the API without creating or managing an API key.
CLI

ant auth login

For other ways to authenticate (API key environment variable, headless hosts, multiple workspaces, named profiles, and Workload Identity Federation), see [CLI authentication options](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/authentication).
Send your first request
With the binary installed and authenticated, call the [Messages API](https://platform.claude.com/docs/en/api/cli/messages/create):

ant messages create \
  --model claude-opus-4-8 \
  --max-tokens 1024 \
  --message '{role: user, content: "Hello, Claude"}'

Output

  "model": "claude-opus-4-8",
  "id": "msg_01YMmR5XodC5nTqMxLZMKaq6",
  "type": "message",
  "role": "assistant",
  "content": [
      "type": "text",
      "text": "Hello! How are you doing today? Is there something I can help you with?"
  ],
  "stop_reason": "end_turn",
  "usage": { "input_tokens": 27, "output_tokens": 20 /*, ... */ }

The response is the full API object, pretty-printed because stdout is a terminal.
Shell completion
The CLI ships completion scripts for bash, zsh, fish, and PowerShell. Generate and install one for your shell:
zsh
zsh
bash
bash
fish
fish
PowerShell
PowerShell

ant @completion zsh > "${fpath[1]}/_ant"
# Restart your shell or run: autoload -U compinit && compinit

Next steps
[  CLI authentication options API keys, headless hosts, multiple workspaces, and named profiles ](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/authentication)[ Using the CLI Command structure, output formats, GJSON transforms, and request bodies ](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/using)[  CLI scripting and automation Version-control API resources, scripting patterns, and use from Claude Code ](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/scripting)
