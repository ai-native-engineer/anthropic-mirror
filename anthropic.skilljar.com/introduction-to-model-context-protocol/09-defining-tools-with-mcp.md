<!-- https://anthropic.skilljar.com/introduction-to-model-context-protocol/296697 -->
<!-- jwplayer-srt: https://cdn.jwplayer.com/tracks/rq8e4RQ6.srt -->

# Defining tools with MCP

Let's start to make an MCP server for our
CLI chatbot. As you saw, the
CLI itself already works, and we can already chat with
Claude, but there's no additional functionality around the MCP
server tied to it just yet. So we're going to work on adding
in this MCP server that is going to have two tools
in it for right now. It's going to have one tool to read a document
and one tool to update the contents of a document.
The implementation of the server is going to be placed into the MCP
server.py file inside of the root project
directory. Inside of here, I've already gone through a little
bit of work to set up a basic MCP server. And
then I defined a collection of documents that are going to exist
only in memory. And then finally, I put together some
different to-do items. So these are different tasks that you
and I are going to complete inside of this file. For
right now, as I just mentioned, we're going to be working only on these first
two items, writing out two tools. Now
we have authored tools in the past, and we saw that,
oh, there's a lot of syntax there. There's those big JSON
schemas. But I got good news for you here. In
this project, we're making use of the official MCP
Python SDK. So that's what this MCP
packages we're making use inside of here. This
MCP package is going to create our MCP server
for us with just one line of code, like what you see right
there. This SDK also makes
it really easy to define tools. To define
a tool, all we have to do is write out what you see on the right-hand
side over here. This will make a tool named add
integers with this description and
two arguments that are going to be required to be passed into
it. Once we write out a tool definition like
this, behind the scenes, Anthropic is going to generate
a tool JSON schema for us, which
we can take and pass off to Claude. So
right away, as you can see, it starts to get a lot easier to do
some basic things like defined tools. Now, as I
mentioned, our first task is going to be to implement these two
different tools. So let's go back over to our MCP
server.py file right away, and we're going to start to implement
the first tool of reading a document. So
the only goal here is to take in the name of some document
and return the contents of it. All of our
documents are already placed inside of this docs dictionary.
The keys are the IDs or essentially names
of a document, and the value is a document's contents. So
our tool is really simple. We're going to take in one
of these strings, look up the appropriate value
inside this docs dictionary, and then return it. That's all
we need to do. So to implement this,
I'm going to find the first to do and right underneath it, I'm
going to define a new tool by writing out at
mcp.tool. I'm going
to give this tool a name of read_contents
and a description of read the contents of
a document and return it as a string. And
remember, in a perfect world, we put in a really fleshed
out description right here to make sure it's super clear to Claude,
exactly when to use this tool. But right now, just
as usual, to save a little bit of time and keep you from
having to type out a bunch of text here, I'm just going to leave in a very
simple description. then I will define my
actual tool function. So this is the function to run
whenever we decide to run this tool. I
will call it read_document. It's
going to take in a argument of doc_id that
is going to be a string. I'm
going to set that to a field with a description
of ID of the document to
read. And then we need to make sure that we import
this field class at the top. So I'm going to
go up to the top and add an import
from pydantic import field.
then back down here inside of the function
body, I'm going to put in my actual implementation. So
the first thing I'm going to do is just make sure I handle the case in
which Claude asks for a document that doesn't actually exist.
So I'll say if doc_id not
in docs. So in other words, if the provided
document ID is not found as a key inside of this dictionary,
then I'm going to raise a ValueError with
a f-string of "doc with id {doc_id} not found."
ID not found. And
then if we get past that check, I'll go ahead and return the actual
document. So I'll return docs[doc_id].
And that's it, that's all it takes to define a tool. So
we've specified the name of the tool, its description,
the argument that is expected, its type,
and a description for that argument as well. All
these different decorators and field types and whatnot
are all going to be taken together by this Python MCP
SDK, and it's going to generate a JSON
schema for us. Now that we've implemented
this first tool, I'm going to remove the to-do right there.
And then we will implement our other tool, the one to
edit a document. So we're going to repeat
the exact same process. I'll say MCP
dot tool. I'll give it a name of edit_document
with a description of edit a document
by replacing a string in the document's
contents or semi-content with a new string.
Then for the implementation, I'll call this function edit_doc.
Or so we'll be consistent, call edit_document. And
then we're going to take in a couple of different arguments here. First
is going to be a document ID and then a old
string to find and then a new string to replace
the old string with. So let's write this all
out. We're going to have a doc_id. That
will be a string with a description
of ID of the
document. that will
be edited. old_
string will be a string with
a description of the text to replace
must match exactly including
white space. And
then our new_string. the
new text to insert in place of
the old text. So our document editing here is
just a very simple find and replace. That's it. Once
again, inside of here, I'm going to make sure that Claude
is asking for a document that actually exists. So if doc_id
not in docs, raise
ValueError with a f-string
of "doc with id {doc_id} not
found." And then if we do find the correct
document, here's how we will do our edit. We'll say docs
[doc_id] = docs[doc_id].replace(old_string, new_string)
replace old_string with new_string.
And that's it. All
right. So just like that, we have put together two tool implementations
really, really quickly. I can't repeat it enough, defining
tools with this MCP Python SDK is
a lot easier than writing out the schema definition manually.
Now that we've got both tools put together, I'm going to delete the
Tudu right there. Okay, so this
is a good start. We have put together our MCP
server and we've implemented two tools inside of it.
