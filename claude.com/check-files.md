<!-- source: https://claude.com/check-files -->

# Check if a file was made with Claude

## Check a file

Drag and drop or click to add a file.

Supported formats: JPG, PNG, GIF, WEBP, TIFF, HEIC, AVIF, SVG, DNG, JXL, MP4, MOV, AVI, WAV, MP3, M4A, FLAC · up to 100 MB

This tool runs in your browser. Your file never leaves your device. By using this tool, you agree to Anthropic’s [Usage Policy (opens in new tab)](https://www.anthropic.com/legal/aup) and acknowledge our [Privacy Policy (opens in new tab)](https://www.anthropic.com/legal/privacy).

## What the tool does

The tool checks a file for a Content Credential from Claude. If it finds one, that tells you Claude may have made or processed the file. It doesn't tell you who authored the underlying content, and it carries no identifying information about the user.

The tool does not check text. Claude marks text with a watermark in the writing itself. Find details on text detection [here (opens in new tab)](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content).

## How it works

When Claude produces a supported file type (such as a .png, .jpg, or .svg), it attaches a Content Credential in the form of a small, cryptographically signed note in the file’s metadata, saying that the file may have been made or processed with Claude.

This is an open industry standard called C2PA—the same used by camera manufacturers and in photo-editing software to record where an image came from. Any C2PA-aware tool can read it.

If we find one that points to Claude, we'll tell you here.

## How can I tell if Claude wrote a piece of text?

Text is checked through a Detection API, which is currently in private preview for eligible organizations as required under EU law.

Read more about file and text detection [here (opens in new tab)](https://support.claude.com/en/articles/16266773).

## What happens to the file you upload

* Your file stays on your device.
* The checker only reads the attached credential, not the file itself.
* Your file is never stored or used for any other purpose.
