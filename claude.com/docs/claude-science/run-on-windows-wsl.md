<!-- source: https://claude.com/docs/claude-science/run-on-windows-wsl -->

Claude Science doesn’t ship a native Windows build yet, but the Linux binary runs well under Windows Subsystem for Linux (WSL 2). Setup takes about five minutes.

##  Enable WSL

In PowerShell, run as Administrator:

```
wsl --install -d Ubuntu-24.04
```

Reboot if Windows prompts you to, then open **Ubuntu 24.04** from the Start Menu and create your Linux user when asked.

Use Ubuntu 24.04 or newer. Claude Science’s sandbox requires bubblewrap 0.8.0 or later, and Ubuntu 22.04 ships an older version. WSL 2 is also required (WSL 1 can’t run the sandbox); `wsl --install` sets up WSL 2 by default. If you have an older WSL setup, check with `wsl -l -v` and upgrade with `wsl --set-version Ubuntu-24.04 2`.

##  Install dependencies

Inside the Ubuntu terminal:

```
sudo apt update && sudo apt install -y curl bubblewrap socat
```

##  Install Claude Science

Run the installer inside Ubuntu. It downloads the current release, verifies its checksum, and installs the `claude-science` command:

```
curl -fsSL https://claude.ai/install-claude-science.sh | bash
```

Then confirm the command is on your PATH:

```
. ~/.profile
claude-science --version
```

Install from inside Ubuntu rather than downloading the binary with a Windows browser and copying it across. The installer verifies the download and keeps you on the stable release channel.

##  Run it

```
claude-science serve --port 8765 --no-browser
```

First launch prints progress to the terminal and ends with a local URL. Copy that URL into any Windows browser: WSL 2 forwards `localhost` automatically, so the link works from Windows as-is. The URL contains a one-time sign-in token; to print a fresh one later, run:

```
claude-science url
```

Then sign in with your Claude account and complete the setup wizard as described in [Get started](/docs/claude-science/get-started).

##  Keep it running

The app runs inside the WSL virtual machine, so it stops when WSL shuts down. Closing your last Ubuntu terminal shuts the VM down after a short idle period, and `wsl --shutdown` stops it immediately.
To start Claude Science again from PowerShell without opening an Ubuntu terminal:

```
wsl -d Ubuntu-24.04 -- ~/.local/bin/claude-science serve --port 8765 --no-browser
```

Leave that PowerShell window open; it keeps the VM alive. To run it in the background of an existing Ubuntu session instead:

```
claude-science serve --port 8765 --no-browser --detached
```

##  Troubleshooting

| Symptom | What it means |
| --- | --- |
| `command not found: claude-science` | `~/.local/bin` isn’t on your PATH yet. Run `. ~/.profile` or open a new terminal. |
| An error mentioning `bwrap too old` | Your Ubuntu version ships an older bubblewrap. Use Ubuntu 24.04 or newer. |
| `daemon already running on port 8765` | Claude Science is already running. Run `claude-science url` and open the printed link; there’s no need to start it again. |
| `port 8765 is already in use` | A different program holds that port. Pick another with `--port 8080`. |
| The browser can’t reach `localhost:8765` | Confirm the daemon is still running in WSL. If you use a custom `.wslconfig` network mode, try the WSL address (run `hostname -I` inside Ubuntu) instead of `localhost`. |

[Get started](/docs/claude-science/get-started)[Core concepts](/docs/claude-science/core-concepts)
