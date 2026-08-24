<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/parallelizing-claude-code -->

Lesson 61 of 65 · Claude with Amazon BedrockParallelizing Claude Code

Running multiple instances of Claude Code in parallel is one of the biggest productivity gains you can achieve. Since Claude is lightweight, you can easily spin up several copies, assign each a different task, and have them work simultaneously. This effectively gives you a team of virtual software engineers working on your project.

## The Challenge: File Conflicts

The main problem with parallel instances is that they might try to modify the same files at the same time. This can lead to conflicting or invalid code since each instance isn't aware of what the others are doing.

![](https://academy.claude.com/assets/media/23c2b65a689b211558ee5f064078042d0535c0d10f4b80bd5f094dfb2c879b7e.png)

The solution is to give each Claude instance its own separate workspace. Each instance works with its own copy of your project, makes changes in isolation, and then merges those changes back into your main project.

![](https://academy.claude.com/assets/media/3a6bb5b1df65e93091dcc1a1787b12d88c05df95497c7e0b46f802eeaeb89095.png)

## Git Worktrees

Git worktrees are perfect for this workflow. If your project is already managed by Git, you can use worktrees immediately. They're like an extension of Git's branching functionality that lets you create complete copies of your project in separate directories on your machine.

![](https://academy.claude.com/assets/media/950a050ee2b081d9db4b04d04b487afb506d797d846bf494df58912a8c0a2807.png)

Each worktree corresponds to a separate branch. You can have one folder for feature A and another for feature B, each containing a complete copy of your codebase. Then you run separate Claude Code instances in each worktree, working in total isolation.

![](https://academy.claude.com/assets/media/536e6bef11940caea62b1d41d10070eb1e2a220811cb0ff388da1af20b4d2c79.png)

Once each Claude instance finishes its feature, you commit the work and merge it back into your main branch, just like merging any normal Git branch.

![](https://academy.claude.com/assets/media/ad6aa49fddf47e8f7a267db97aaa4913d12c95fea4812cfcabc0514fa5acce73.png)

## Automating Worktree Creation

This might sound complicated to manage, but you can delegate the entire workflow to Claude Code itself. You can write a prompt that asks Claude to:

1. Create a new git worktree in a specific folder
2. Symlink dependencies that aren't tracked by Git
3. Launch a new VS Code instance in that directory

![](https://academy.claude.com/assets/media/8b857191538aca7ffc5a0a7ba8b5b63ae23497444cdadbf0ede58756341b4218.png)

## Custom Commands

Rather than copying and pasting long prompts every time, you can create custom slash commands in Claude Code. Add a `.md` file to `.claude/commands` to create a custom command.

![](https://academy.claude.com/assets/media/518237ab1b5c747edc756586e07903d4e20e5a84fc967528561f724331affa48.png)

The custom command can reference `$ARGUMENTS`, which gets replaced with whatever arguments you pass to your command. For example:

* `/project:create_worktree feature_a` creates a worktree named "feature\_a"
* `/project:create_worktree develop` creates a worktree named "develop"

## Parallel Development in Action

Here's how the complete workflow looks in practice. You can create multiple worktrees for different features:

![](https://academy.claude.com/assets/media/fa078fbbc5d07ffea2fdbd7703d792523ff28b6b9f66ad2be679b215e5854d77.png)

Each Claude instance works on its assigned task:

* Update document tests
* Add logging
* Add note-taking tools
* Add a subtract tool

![](https://academy.claude.com/assets/media/7100def75d32908917a6793170501668a72d5131b39e71549ccfb6b06c97e079.png)

## Merging Changes

When the features are complete, you can automate the merge process too. Create another custom command that tells Claude to:

1. Change into the worktree directory
2. Examine the latest commit
3. Change back to the root directory
4. Merge the worktree branch
5. Handle any merge conflicts automatically

![](https://academy.claude.com/assets/media/0cfd5f360ce83f3a7a29a93486a909ab400fcc51b73a9f3701fc7f9ad7cf3959.png)

Claude can even resolve merge conflicts automatically based on its understanding of the changes made in each branch.

## Results

This approach scales to as many parallel instances as you can manage. Instead of working on features sequentially, you can have multiple Claude instances developing different parts of your project simultaneously. It's like having your own team of developers, each working in their own isolated environment before bringing their work together.

The productivity gains are substantial - you're essentially multiplying your development capacity by the number of parallel instances you run.
