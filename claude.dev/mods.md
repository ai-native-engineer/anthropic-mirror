<!-- source: https://claude.dev/mods/ -->

# mods

Small TypeScript functions that ship inside Claude Code plugins. They hook its events, change what it does, and draw their own UI in the terminal.

Token weather

❯ Read forecast.py and tell me in one sentence what it does.

Read 1 file

●The forecast() function returns 'sunny' for odd-numbered days and 'cloudy' for even-numbered days.

✻Churned for 2s · done 4:20 PM

❯ Read radar.py and almanac.py in full, then tell me how many functions each defines. Read tides.py and gusts.py in full, then name the last function in each.

Read 4 files

●radar.py: 600 functions (radar\_0 through radar\_599)
almanac.py: 600 functions (almanac\_0 through almanac\_599)
tides.py last function: tides\_599
gusts.py last function: gusts\_599

✻Churned for 5s · done 4:21 PM

❯ Read every line of isobar.py, from line 1 to the last line, with no limit, and list its last three function names.

Read 1 file

●The last three function names in isobar.py are:
1. isobar\_597
2. isobar\_598
3. isobar\_599

✻Brewed for 3s · done 4:22 PM

☇Storm 81% of context 161.1k / 200k last turns  ▲ +26.7k last turn

[-]

90% context used

❯

manual mode on · ← for agents

Play

## [Token weather](https://claude.dev/blog/getting-started-with-claude-code-mods/#build-your-first-mod-token-weather)

A one-line forecast of how full the context window is, drawn above the prompt.

HOOKS
:   `turn.complete`, `ui.render`

DRAWS
:   A band above the prompt

[SEE HOW IT WORKS→](https://claude.dev/blog/getting-started-with-claude-code-mods/#build-your-first-mod-token-weather)

Blast radius

❯ Delete the build folder with rm -rf build. Run exactly that command and nothing else.

●Checking build folder contents and git status

⎿ $ rm -rf build

Ran 2 shell commands

●The command was cancelled, so build was not deleted. Let me know if you'd like to retry it.

✻Worked for 52s · done 4:16 PM

❯ Run rm -rf build again now. This time I will press Proceed.

●Deleting the build folder

⎿ $ rm -rf build

·Cogitating… (11s · ↓ 322 tokens)

×

⚠ Blast Radius · rm -rf

Command rm -rf build

Would delete 9 files (1.1 MB)

build/assets/logo.png

build/index.html

build/js/chunk-5.js

build/js/chunk-2.js

build/js/chunk-3.js

build/js/app.js.map

build/js/chunk-6.js

build/js/chunk-1.js

build/js/chunk-4.js

Paths: build

1: Proceed 2: Cancel Claude is waiting on your answer

❯

manual mode on · ← for agents

Play

## [Blast radius](https://claude.dev/blog/getting-started-with-claude-code-mods/#blast-radius-see-what-a-risky-command-would-change-before-it-runs)

Holds a risky shell command and shows what it would change, with Proceed and Cancel.

HOOKS
:   `tool.call`, `ui.render`

DRAWS
:   A pane beside the transcript

[SEE HOW IT WORKS→](https://claude.dev/blog/getting-started-with-claude-code-mods/#blast-radius-see-what-a-risky-command-would-change-before-it-runs)

Replay theater

❯ Rename greet to welcome everywhere, but leave greetAll alone.

●Update(greet.js)

⎿ Added 1 line, removed 1 line

1 // Greeter

2-export function greet(name) {

2+export function welcome(name) {

3  return `Hello, ${name}!`;

4 }

●Update(greet.js)

⎿ Added 1 line, removed 1 line

5

6 export function greetAll(names) {

7- return names.map((n) => greet(n));

7+ return names.map((n) => welcome(n));

8 }

●Update(main.js)

⎿ Added 1 line, removed 1 line

1-import { greet, greetAll } from "./greet.js";

1+import { welcome, greetAll } from "./greet.js";

2

3 console.log(greet("Ada"));

4 console.log(greetAll(["Grace", "Linus"]).join("\n"));

●Update(main.js)

⎿ Added 1 line, removed 1 line

1 import { welcome, greetAll } from "./greet.js";

2

3-console.log(greet("Ada"));

3+console.log(welcome("Ada"));

4 console.log(greetAll(["Grace", "Linus"]).join("\n"));

●Update(README.md)

⎿ Added 1 line, removed 1 line

1 # Greeter

2

3-Call `greet(name)` to say hello to one person.

3+Call `welcome(name)` to say hello to one person.

●Renamed greet to welcome in greet.js, main.js, and README.md, leaving greetAll unchanged.

✻Baked for 11s · done 4:20 PM

×

▶ Replay Theaterstep 5 of 5

1  2  3  4 5

README.md

Edit +1 -1

- Call `greet(name)` to say hello to one person.

+ Call `welcome(name)` to say hello to one person.

[ ◀ Prev ] [ Next ▶ ] [ Close ]

❯

manual mode on · ← for agents

Play

## [Replay theater](https://claude.dev/blog/getting-started-with-claude-code-mods/#replay-theater-step-through-the-last-turns-edits)

Records the edits Claude makes in a turn and steps through them one diff at a time.

HOOKS
:   `tool.call`, `turn.complete`, `command.run`

DRAWS
:   A pane with Prev, Next and Close

[SEE HOW IT WORKS→](https://claude.dev/blog/getting-started-with-claude-code-mods/#replay-theater-step-through-the-last-turns-edits)

BUILT INTO CLAUDE CODE3

[/diffThe session's uncommitted changes in a pane beside the transcript, refreshed as Claude edits.SOURCE↗](https://github.com/anthropics/claude-code/tree/main/mods/diff)[AGENTS.mdReads AGENTS.md as project instructions when a project has no CLAUDE.md of its own.SOURCE↗](https://github.com/anthropics/claude-code/tree/main/mods/agents-md)[sec-defaultOn Team and Enterprise plans, keeps an organization's policy out of reach of the mods a person installs.SOURCE↗](https://github.com/anthropics/claude-code/tree/main/mods/sec-default)

FROM THE COMMUNITY1

Next steps

❯ Add validation to the profile form: the name is required and the email has to be valid. Show each error under its field, and write tests for it.

Read 2 files

●Update(src/profile/ProfileForm.tsx)

⎿ Added 18 lines, removed 2 lines

●Write(src/profile/ProfileForm.test.tsx)

⎿ Wrote 42 lines to src/profile/ProfileForm.test.tsx

●The profile form now requires a name and checks the email's format. Each error shows under its field and clears as you type. The tests in ProfileForm.test.tsx cover both rules; I haven't run them yet.

✻Cooked for 14s · done 4:20 PM

next:

1: run the tests you just wrote

2: do the same for the settings page

3: open a draft PR

0: dismiss

❯run the tests you just wrote

manual mode on · ← for agents

Play

## [Next steps](https://github.com/anthropics/claude-plugins-community/tree/main/next-steps)

Suggests up to three next prompts when a turn ends. Press 1, 2 or 3 to draft one in the prompt box, or 0 to dismiss.

HOOKS
:   `turn.start`, `turn.complete`, `ui.render`

DRAWS
:   Numbered suggestions above the prompt

BY
:   Thariq Shihipar

INSTALLCOPY
:   `claude plugin install next-steps@claude-community`

[SOURCE↗](https://github.com/anthropics/claude-plugins-community/tree/main/next-steps)

YOUR MODS

Built one? A mod is a plugin, so you share it the same way.

[SHARE YOUR MOD→](https://claude.dev/blog/getting-started-with-claude-code-mods/#sharing-your-mod)
