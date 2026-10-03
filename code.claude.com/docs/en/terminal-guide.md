<!-- source: https://code.claude.com/docs/en/terminal-guide -->

# Terminal guide for new users

> A step-by-step guide to installing Claude Code for first-time terminal users on macOS, Linux, and Windows.

You can use Claude Code even if you've never used a terminal before. This guide walks you through opening a terminal, installing Claude Code, and your first interactions.

* [macOS and Linux](#macos-and-linux)
* [Windows](#windows)

<Note>
  Don't want to use the terminal? The Claude Code desktop app lets you skip the terminal entirely. Download it for [macOS](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect?utm_source=claude_code\&utm_medium=docs) or [Windows](https://claude.com/download?utm_source=claude_code\&utm_medium=docs), then see the [Desktop quickstart](https://code.claude.com/docs/en/desktop-quickstart) to get started. On Linux, install the app with apt by following the [Linux install instructions](https://code.claude.com/docs/en/desktop-linux).
</Note>

## macOS and Linux

Follow these steps to install and start Claude Code from a macOS or Linux terminal. Claude Code requires macOS 13.0 or later. See the [system requirements](https://code.claude.com/docs/en/setup#system-requirements) for supported Linux distributions.

<Steps>
  <Step title="Open a terminal">
    **macOS**: Press `Cmd + Space` to open Spotlight Search, type `Terminal`, and press `Enter`.

    **Linux**: Open your terminal app. On most distributions, press `Ctrl + Alt + T` or search for "Terminal" in your application menu.

    A window will appear with a blinking cursor. This is your terminal, where you type commands.
  </Step>

  <Step title="Install Claude Code">
    Copy this line, paste it into your terminal (`Cmd + V` on macOS, `Ctrl + Shift + V` on Linux), and press `Enter`:

    ```bash theme={null}
    curl -fsSL https://claude.ai/install.sh | bash
    ```

    This downloads and runs the Claude Code installer from claude.ai. You'll see text scrolling as it works. When it's done, you'll see "Claude Code successfully installed!" If you see an error instead, check the [troubleshooting section](#macos-and-linux-troubleshooting) below.
  </Step>

  <Step title="Start Claude Code">
    Type `claude` and press `Enter`:

    ```bash theme={null}
    claude
    ```

    If you see `command not found: claude`, the install directory isn't on your PATH yet. Follow the ['command not found: claude'](#macos-and-linux-troubleshooting) fix below, then open a new terminal window and try again.

    You'll be prompted to [log in](https://code.claude.com/docs/en/authentication) with your Claude account. Follow the on-screen instructions. A browser window will open for you to sign in.
  </Step>

  <Step title="Start using Claude Code">
    Once logged in, you can start asking Claude questions about your code or anything else. Claude Code runs entirely in text. You type messages and press `Enter` to send them. A few things to know:

    * You can't click on things in the terminal. Use the arrow keys to move around.
    * Press `Esc` to interrupt Claude if it's running.
    * Type `exit` or press `Ctrl + D` twice on an empty prompt to leave Claude Code.
    * Type `/help` to see available commands.
  </Step>
</Steps>

***

## Windows

Follow these steps to optionally install Git for Windows, set up PowerShell, and start Claude Code on Windows. Claude Code requires Windows 10 version 1809 or later. See the [system requirements](https://code.claude.com/docs/en/setup#system-requirements) for full details.

<Steps>
  <Step title="Install Git for Windows (optional)">
    Git for Windows provides Git Bash, which enables the Bash tool. Without it, Claude Code uses PowerShell instead. You won't need to learn Git yourself.

    If you don't already have it:

    1. Go to [git-scm.com/downloads/win](https://git-scm.com/downloads/win) and download the installer
    2. Run the installer. Click Next on each screen to accept the defaults. The installer has many screens, but you don't need to change anything.
    3. If it asks you to choose an editor, keep the default and click Next.
    4. When you see "Adjusting your PATH environment," keep the recommended option selected.

    <Note>
      Already have Git? You can skip this step. If you're not sure, install it anyway. Reinstalling won't cause problems.
    </Note>
  </Step>

  <Step title="Open PowerShell">
    PowerShell is Windows' built-in terminal for typing commands. It comes pre-installed on every Windows computer.

    Press `Win + X` and select **Windows PowerShell** (or **Terminal**) from the menu. A window with a blinking cursor will appear. This is where you'll type commands.

    <Note>
      Windows has two command-line programs: PowerShell and CMD. They look similar but use different commands. Make sure you're in PowerShell for the next step.

      How to tell which one you're in:

      * **PowerShell**: shows `PS C:\Users\YourName>` at the start of each line
      * **CMD**: shows `C:\Users\YourName>` without the `PS`
    </Note>
  </Step>

  <Step title="Install Claude Code">
    Copy this line, paste it into PowerShell with `Ctrl + V` or right-click, and press `Enter`:

    ```powershell theme={null}
    irm https://claude.ai/install.ps1 | iex
    ```

    This downloads and runs the Claude Code installer. `irm` fetches the file and `iex` runs it. You'll see text scrolling as it works. When it's done, you'll see "Claude Code successfully installed!" If you see an error instead, check the [troubleshooting section](#windows-troubleshooting) below.

    <Note>
      If you're in CMD instead of PowerShell, use this command:

      ```batch theme={null}
      curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
      ```
    </Note>
  </Step>

  <Step title="Start Claude Code">
    Run `claude`. If PowerShell says `'claude' is not recognized`, the install directory isn't on your PATH yet. Follow the ['claude is not recognized'](#windows-troubleshooting) fix below, then open a new PowerShell window and try again.

    ```powershell theme={null}
    claude
    ```

    You'll be prompted to [log in](https://code.claude.com/docs/en/authentication) with your Claude account. Follow the on-screen instructions. A browser window will open for you to sign in.
  </Step>

  <Step title="Start using Claude Code">
    Once logged in, you can start asking Claude questions about your code or anything else. Claude Code runs entirely in text. You type messages and press `Enter` to send them. A few things to know:

    * You can't click on things in the terminal. Use the arrow keys to move around.
    * Press `Esc` to interrupt Claude if it's running.
    * Type `exit` or press `Ctrl + D` twice on an empty prompt to leave Claude Code.
    * Type `/help` to see available commands.
  </Step>
</Steps>

***

## What's next?

Once you see the Claude Code welcome screen, you're ready to go. You don't need to know how to code. Describe what you want in plain English, and Claude writes the code for you.

### Build something

Claude can create projects from a description:

```text wrap theme={null}
make me a simple webpage that says hello world
```

If Claude asks for your permission before creating or changing files, press `Enter` to choose **Yes** and approve. Once Claude creates the files, double-click the HTML file to open it in your browser.

### Work with files on your computer

Claude can read and organize files you already have:

```text wrap theme={null}
look at the screenshots on my Desktop and rename them based on what's in each image
```

### Ask questions

Claude can explain things, help you learn, or plan out a project:

```text wrap theme={null}
I want to build a personal budget tracker. What would I need?
```

If you don't have a project yet, that's fine. Claude can help you start a new one.

### Other ways to use Claude Code

You don't have to use the terminal. Claude Code is also available in:

* [VS Code](https://code.claude.com/docs/en/vs-code) and [JetBrains IDEs](https://code.claude.com/docs/en/jetbrains) as editor extensions
* The [desktop app](https://code.claude.com/docs/en/desktop-quickstart), with no terminal required
* The [web](https://code.claude.com/docs/en/claude-code-on-the-web) at claude.ai/code for cloud sessions
* [GitHub Actions](https://code.claude.com/docs/en/github-actions) and [GitLab CI/CD](https://code.claude.com/docs/en/gitlab-ci-cd) for automation

### Learn more

* [Quickstart](https://code.claude.com/docs/en/quickstart): a guided walkthrough of your first project with Claude Code
* [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works): understand how Claude reads your files, runs commands, and makes edits
* [Best practices](https://code.claude.com/docs/en/best-practices): get better results with effective prompting and project setup
* [Common workflows](https://code.claude.com/docs/en/common-workflows): step-by-step guides for debugging, testing, refactoring, and more
* [Terminal configuration](https://code.claude.com/docs/en/terminal-config): customize your terminal for the best Claude Code experience

***

## Troubleshooting

### macOS and Linux troubleshooting

If you run into problems installing on macOS or Linux, check these common issues:

<Accordion title="'command not found: claude'">
  If you see `command not found: claude` after installing, the folder where the installer put `claude` isn't in your PATH. The installer prints the exact fix under `Setup notes` at the end of the install, so run that command, or use the one for your shell below.

  For Zsh, the macOS default shell:

  ```bash theme={null}
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
  source ~/.zshrc
  ```

  For Bash on Linux:

  ```bash theme={null}
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
  source ~/.bashrc
  ```

  For Bash on macOS, follow the macOS Bash step in [fix your PATH](https://code.claude.com/docs/en/troubleshoot-install#verify-your-path) instead.

  Then open a new terminal and try `claude` again. If it still isn't found, check that the file `~/.local/bin/claude` exists. If it doesn't, the install didn't finish. For more details, see [fix your PATH](https://code.claude.com/docs/en/troubleshoot-install#verify-your-path).
</Accordion>

<Accordion title="Error with HTML code or 'syntax error near unexpected token'">
  If you see `bash: line 1: syntax error near unexpected token '<'` or HTML code like `<!DOCTYPE html>` in your terminal, the install URL returned a web page instead of the installer script.

  If the page says "App unavailable in region," Claude Code is not available in your country. See [supported countries](https://www.anthropic.com/supported-countries).

  Otherwise, try running the command again. If it keeps happening, install with [Homebrew](https://brew.sh) instead:

  ```bash theme={null}
  brew install --cask claude-code
  ```

  When it finishes, open a new terminal window, type `claude --version`, and press Enter: the command prints a version number such as `2.1.211 (Claude Code)` when the install worked.
</Accordion>

<Accordion title="'dyld' error or 'built for Mac OS X 13.0'">
  If you see `dyld: cannot load`, `dyld: Symbol not found`, or `built for Mac OS X 13.0`, your macOS version is likely older than Claude Code supports.

  Open the Apple menu and select About This Mac to check your version. If it's older than 13.0, update macOS through Software Update. See the [macOS troubleshooting guide](https://code.claude.com/docs/en/troubleshoot-install#dyld-cannot-load-on-macos) for more details.
</Accordion>

For other errors, see the full [installation troubleshooting guide](https://code.claude.com/docs/en/troubleshoot-install).

### Windows troubleshooting

If you run into problems installing on Windows, check these common issues:

<Accordion title="'irm is not recognized'">
  You're in CMD, not PowerShell. Close this window and open PowerShell instead (`Win + X` then select Windows PowerShell).

  Alternatively, use the CMD install command:

  ```batch theme={null}
  curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
  ```
</Accordion>

<Accordion title="SSL/TLS error or 'Could not create SSL/TLS secure channel'">
  This usually happens on older Windows 10 systems. Run this line first, then retry the install:

  ```powershell theme={null}
  [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
  irm https://claude.ai/install.ps1 | iex
  ```
</Accordion>

<Accordion title="'Claude Code on Windows requires either Git for Windows (for bash) or PowerShell'">
  Neither PowerShell nor Git Bash was found. Claude Code needs at least one shell.

  1. Ensure `powershell.exe` is on your `PATH`. Its default location is `C:\Windows\System32\WindowsPowerShell\v1.0\`. Alternatively, install [PowerShell 7](https://aka.ms/powershell), which provides `pwsh`.
  2. If you'd rather use Git Bash, install [Git for Windows](https://git-scm.com/downloads/win) per the [first step in the Windows section](#windows).
  3. If Git is installed but Claude Code can't find it, tell it where to look:
     ```powershell theme={null}
     $env:CLAUDE_CODE_GIT_BASH_PATH="C:\Program Files\Git\bin\bash.exe"
     ```
     Then run `claude` again. If your Git is installed somewhere else, find the path by running:
     ```powershell theme={null}
     Get-Command git | Select-Object Source
     ```
     Look for the `Git\bin` folder in that path and use it instead.

  To make this permanent so you don't have to set it every time, see [configure Git Bash path](https://code.claude.com/docs/en/troubleshoot-install#claude-code-on-windows-requires-either-git-for-windows-for-bash-or-powershell).
</Accordion>

<Accordion title="'claude is not recognized'">
  This error means the install directory isn't in your PATH. Run these commands in PowerShell to add it:

  ```powershell theme={null}
  $currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User')
  [Environment]::SetEnvironmentVariable('PATH', "$currentPath;$env:USERPROFILE\.local\bin", 'User')
  ```

  Close PowerShell, open a new window, and try `claude` again. You should see the Claude Code welcome screen. See [verify your PATH](https://code.claude.com/docs/en/troubleshoot-install#verify-your-path) for more details.
</Accordion>

<Accordion title="'Claude Code does not support 32-bit Windows'">
  On a 64-bit machine, this error means you opened `Windows PowerShell (x86)` instead of `Windows PowerShell`. The x86 entry runs as a 32-bit process. Close it, open the Start menu entry without `(x86)` in its name, and run the install command again. If you're not sure your machine is 64-bit, or the error persists, see [the full explanation](https://code.claude.com/docs/en/troubleshoot-install#claude-code-does-not-support-32-bit-windows).
</Accordion>

For other errors, see the full [installation troubleshooting guide](https://code.claude.com/docs/en/troubleshoot-install).
