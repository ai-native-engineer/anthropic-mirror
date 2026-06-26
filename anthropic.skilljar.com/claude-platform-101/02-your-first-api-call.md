<!-- https://anthropic.skilljar.com/claude-platform-101/486251 -->
<!-- youtube: j0ftK_R5DTs -->

# Your first API call

Saying hi to Claude might warm your
heart, but it's not really useful.
[music]
So, let's send it a real document and
get structured insight back in just
under 20 lines of code.
First, let's grab an API key from
platform.claude.com.
You'll have to purchase some credits
beforehand.
Take the API key and store it in a
.env.local file so that it stays out of
your version control.
Next, we install the SDK.
npm install @anthropic.ai/sdk
Now, every API call goes through the
messages.create function.
You specify three things:
a model,
a max tokens limit,
and a list of messages, which are
objects that contain either user or
assistant roles, structured similarly to
how you would have a conversation with
Claude elsewhere.
Let's give Claude something a little bit
more interesting than hello.
I want to point it at some buggy code
and ask for a review.
So, here's the whole thing. One file,
about 20 lines of code.
So, two things to notice here. First,
the system is where I shape the persona.
I want a terse senior reviewer, not a
chatty one, so I just say that. And
second, the message.content is an array
of blocks, not a string. So, for a basic
text reply, there's usually just one
block of type text. But, Claude can
return multiple blocks: text, tool
calls, thinking. So, we always loop and
check the type. So, let's run it.
And Claude spots that add is subtracting
and tells you in one paragraph. That's
it. That's the whole API call. And so,
in a real product, the same
messages.create shape is the engine
behind something like a summarize
endpoint. Pull a meeting transcript out
of the database, hand it to Claude with
a system prompt that says extract
insights and risks and save the result
back on the row, return it to the UI.
Same call, but wrapped in a route
handler.
Your first API call is a messages.create
function with a model
token limit
and messages.
Add a system prompt to shape Claude's
behavior.
And from here, everything builds on this
pattern.
