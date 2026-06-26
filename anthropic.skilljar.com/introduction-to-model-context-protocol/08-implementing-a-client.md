<!-- https://anthropic.skilljar.com/introduction-to-model-context-protocol/296696 -->
<!-- jwplayer-srt: https://cdn.jwplayer.com/tracks/szOeZDgZ.srt -->

# Implementing a client

Now that our server is in a good place, we're going to shift gears
a little bit and start working on our MCP client.
The client can be found inside the MCP client.py
file inside the root project directory. Now before we do
anything inside this file, I just want to give you a very quick reminder
here. Remember what I told you about earlier. Usually
in a typical project, we are either making use of a client
or we are implementing a server. It's just in this
one particular project that we are working on that we are doing both. Again,
just so you can see both sides of the puzzle. Now
the MCP client itself inside of this
file is consisting of a single class. You'll notice
there is a lot of code inside of here and it doesn't look quite as
pretty as some of the code we just wrote out inside of the server.
So let me tell you exactly what's going on inside this file and exactly
why it is so large. Okay, so
inside this file, we are making the MCP
client class. This class is going to wrap
up something called a client session. The client session
is the actual connection to our MCP server.
This client session is a part of the MCP
Python SDK. So again, this session
is what gives us this connection to the outside server.
The session itself requires a little bit of resource cleanup.
In other words, whenever we close down our program or decide
that we don't need the server anymore, we have to go through a little bit of
a cleanup process. And I have already written out
a lot of that cleanup code inside of the MCP
client class. So that's really why this class
exists at all, just to make that cleanup a little
bit easier. You can see some of that cleanup code inside
of the Connect function and down a little bit lower.
at the cleanup, async enter, and async
exit functions as well. So it's very common
practice to not just make use of this
client session directly, instead very common to
wrap it up inside of a larger class that's going to manage some of
this different resource stuff for you. The
next thing I want to clarify is why this client exists
at all. So in other words, what is the client really doing
for us here? Well, remember, this full that
we looked at a little bit ago. So we had our code right
here. And at certain points in time, we needed, say,
a list of tools to send off to Claude. And then later
on after that, we also needed to run a tool
that was requested by Claude. In order
to reach out to our MCP server and get this list
of tools or to run a tool, that's where we
are making use of the MCP client. So we can imagine
that this client is exposing some functionality that
belongs to the server to the rest of our codebase. So
inside of our codebase, inside this project, specifically inside
of the core directory, there is a lot of code already
inside there that I put together that is making use of
this class. So there is some other code that's going to
call Some of the different functions you see inside of here,
like list tools, call tool, list prompts, get prompt, and so
on. For right now, in this video, we're going to focus on implementing
two functions, list tools and call tool.
So as you just saw in the diagram, we looked at a moment ago, these
two functions are going to be used in different parts of our code base
to get a list of tools to provide off to Claude, and
then eventually call a tool whenever Claude requests to call
a tool. Implementing these two functions is going to
be really simple and straightforward. So let me show you how we're going
to do it. We'll first begin with list tools. I'm
going to remove the two do inside there and replace
it with result is awaitself.session.
I'm going to call that like a function list underscore
tools. And then I will return result
dot tools. And that's it. So
this is going to get access to our session, which is our
actual connection to the MCP server. It's going to
call a built-in function to get a definition or a list
of all the different tools that are implemented by that server. I'm
going to get back result and then just return the tools and
that's it. Then we can implement call
tool right here in a very similar fashion. So this will
be return a
waitself.session, call
tool, tool name, and tool input.
Once again, getting access to the session, that is our
connection to the server, and I'm going to attempt to call
a very specific tool, the name the tool we passed in,
along with the input parameters or input arguments to it, that
were provided by Claude. Now, at this point
in time, I would like to test out these two functions really quickly.
To do so, we're going to go down to the bottom of this file, where
I put together a very small testing harness for us. So
down here, you'll notice I put together this
testing block, so we can run this MCP
client.py file directly. And if we do so, we're
going to form a connection to our MCP server, and
then we can just run some commands against it and just see what we get
back. Notice that in your version of the code,
there's a comment in there about changing the command and args
right here in case you are not making use of Uvicorn. So
if you're not using Uvicorn, make sure you take a look at that comment.
Inside of this with block, I'm going
to add in a little bit of testing code. So I'll
say result is await underscore
client list tools. And
then I'm going to just print out the result that we get
back. So this should start
up a copy of our MCP server, then
attempt to get a list of all the different tools that are defined
by it, and then just print out the result. To
test this out, I will flip back over to my terminal and
do a uvicorn run, MCP underscore
client.py. And as usual, if you
are not making use of uvicorn, you'll just do a Python
MCP client.py. Okay, so I'll run
that, and there is our list of tool
definitions. So I can see inside of here that I have the read.contents
tool, which we put together a little bit ago, and our edit
document tool as well. Each one has a description
and an input schema as well.
So this is our tool definition, which will eventually
be passed off to Claude. Now before we move on, there's
one other thing I want to test. Remember, we
just implemented the function that's going to allow us to
list out some tools and pass them off to Claude and
the function that's going to allow us to call a tool that is implemented
by the MCP server and then pass the result off to Claude
as well. I have already implemented the code that is
going to call list tools and call tool
for us somewhere else inside this project. So now
that we have added in this functionality, now that we have defined
these tools and the ability to call a particular tool, we
can now run our CLI again and attempt
to get Claude to make use of these tools. In other
words, we can ask Claude to inspect the contents
of some particular document and even edit a document.
So let me show you how we do that. Inside of my
MCP server, I just want to give you a reminder that there is
a document with a ID of report.pdf,
and it has some texture of something like a 20 meter
condenser tower. I'm going to go back over
to my terminal, and I'm going to run
my project with a uvicorn run main.py.
And then I'm going to ask Claude what is the contents
of the report.pdf document.
And make sure you put in exactly report.pdf
here. And when we run this, we're
sending off along with the request our list of tools.
Claude is going to decide to use the read document tool.
And it's going to get the contents of the document. And then we will see
that yes, Claude was able to get the contents of
that document. We are told that the report is something
about a 20 meter condenser tower. All
right, so at this point, we have added in some functionality around
our client. Remember, the client is what allows
us to access some functionality that is implemented inside
of the MCP server. At this point in time, we have
been able to list out some tools that are created
by the server and execute a tool that has been implemented
by the server.
