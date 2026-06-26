<!-- https://anthropic.skilljar.com/claude-code-in-action/301614 -->

**Time to get Claude Code set up locally!**

You can find full setup instructions here: <https://code.claude.com/docs/en/quickstart>

In short, you'll need to do the following:

1. `Install Claude Code` 1. MacOS, Linux, WSL: `curl -fsSL https://claude.ai/install.sh | bash` 2. Windows PowerShell: `irm https://claude.ai/install.ps1 | iex` 3. Windows Command Prompt (cmd.exe): `curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd` 4. `MacOS (Homebrew): brew install --cask claude-code` 2. After installation, run `claude` at your terminal. The first time you run this command you will be prompted to pick a color theme for the terminal and authenticate with your claude.ai credentials

If you get an error that `claude` isn't found after installing, or you hit a network or permissions error, see [Troubleshoot installation issues](https://code.claude.com/docs/en/troubleshoot-install) in the docs.

Using Claude Code through Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry? See [third-party provider setup](https://code.claude.com/docs/en/third-party-integrations) for additional setup instructions.
