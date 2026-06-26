<!-- https://anthropic.skilljar.com/introduction-to-model-context-protocol/296690 -->
<!-- jwplayer-srt: https://cdn.jwplayer.com/tracks/6VSbEk4Z.srt -->

# MCP clients

The next portion of model context protocol that we're going to investigate
is the client. The purpose of the client is
to provide a means of communication between your server
and an MCP server. This client is going to
be your access point to all the tools implemented by that server.
Now MCP is transport agnostic. This
is a fancy term that just says that the client and the
server can communicate over a variety of different
protocols. A very common way to run an MCP
server right now is on the same physical machine as
the MCP client. And if these two things are running
on the same machine, then they can communicate over standard
input output. And that's what we are going to be setting up
later on inside this section. There are,
however, other ways we can connect the MCP client
with the MCP server. So they can also connect
over HTTP or Web Sockets or
any of a number of other varieties or techniques.
Once a connection has been formed between the client and the
server, they communicate by exchanging messages.
The exact messages that are allowed are all defined inside
of the MCP spec. Some of the message types
that you and I are going to be focusing are the list
tools request and the list tools result.
As you guessed, list tools request is sent from the client
to the server and asks the server to list out all the different tools
that it provides. The server would then respond with
a list tools result message, which contains
a list of all the different tools that it can provide.
Two other common message types that you and I are going to see are
the call tool request and call tool result.
The first will ask the server to run a tool with some
particular arguments, and the second will contain the result
of the tool run. Now, at this point
in time, we've got this idea of a server and
a client. But I suspect it's probably
not really clear how all this stuff really works together. So
here's what we're going to do in the remainder of this video. We
are going to walk through an example call between
a lot of different things. So it's going to be kind of an involved
process. But we're going to imagine the communication that goes on between
a user or a server that we're putting together.
An MCP client, the MCP server, GitHub
as some provider that we're trying to access some data from, and
Claude. So let's get to it. Again, Stephen Grider, first
thing we would expect to happen is a user to submit some kind of query
or question to our server, like what repositories do
I have? At this point, it would be up to our server
to make a request off to Claude. But in that
request, we want to list out all the different tools that Claude has
access to. So before our server can make the request
off to Claude, it's first going to go through a little side detour
through the MCP client and the server. So here's what
happens. The server is going to realize that it
needs to see a list of tools to send off
to Claude, along with the user's query. So it's going to
ask the MCP client to get a list of tools. The
MCP client, in turn, is going to send a list
tools request off to the server, and the server
will respond with a list tools result.
Now that our MCP client has a list of the tools,
it will give that list of tools back to the server. And
now our server has everything it needs to make an initial
request off to Claude. It has both the original
message from the user and a list of tools to include.
So our server can make a request off to Claude with that query
and the set of tools. Claude is going to take a look
at the tools and realize, you know what, in order to answer
the user's original question right here, I really want
to call a tool. So Claude would respond
with some tool use message part. At
this point, our server is going to realize that Claude wants
to run a tool. But our server is no longer
really in charge of executing any tools. Instead,
our tools are going to be executed by the MCP server.
So in order to run the tool that Claude is asking
for, our server is going to ask the MCP client
to run a tool with some particular arguments that were
provided by Claude. The MCP client, however,
doesn't actually run the tool. It's going to send a call
tool request off to the MCP server. The
MCP server will receive that request and make
a follow request off to GitHub. So
this is where we would actually be getting a list of repositories
that belong to this particular user. GitHub
would respond with that list of repositories. Then
the MCP server would wrap up that data
inside of a call tool result and send
that back to the MCP client. Then the MCP
client in turn would hand the result off to our server.
Now our server has the list of repositories
and it can make a follow up request to Claude with
the tool result part inside of a user
message. So this tool result would include the list
of repositories that Claude was asking for.
And now Claude has all the information it needs to formulate
a final response. So it'll write out some text
of something like your repositories are, and then send that back
to our server, and our server would send it on back to our
user. All right, so this flow,
yes, it is rather complicated. The reason I want
to show you this is that we are going to see all these different
pieces as you and I start to implement our own
custom MCP client and MCP
server a little bit later on.
