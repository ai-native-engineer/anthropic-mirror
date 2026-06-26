<!-- https://anthropic.skilljar.com/claude-platform-101/486260 -->
<!-- youtube: hftmYd97LBw -->

# MCP

We have tools, skills, connectors. So,
why does MCP exist? It looks like a
second API on top of the API. Well, fair
question.
Now, let's say my agent needs to pull
tasks from Asana, check a Google
Calendar, or search Slack all in one go.
With custom tools, I have to write three
integrations here. But then, I have to
also maintain those integrations every
time an API changes for every single
service, which happens often.
Congratulations, you're now maintaining
a pile of third-party API wrappers.
Well, MCP shifts that maintenance to the
service provider. So, Asana publishes an
MCP server, Slack publishes one, Google
publishes one. Each server exposes its
own tools with descriptions, schemas,
and authentication through a standard
protocol. You change nothing.
These three features do different jobs.
Tools connect Claude to your internal
systems, your database, your project
tracker, your proprietary APIs. You own
the code, so you also own the
maintenance.
Skills teach Claude a procedure, your
report template, your review checklist.
Skills are instructions, not necessarily
integrations.
And MCP connects Claude to third-party
services where the service provider
maintains the integration. You don't
write the Asana wrapper, Asana did.
And so, the short version of all this is
that tools is for your stuff, skills for
your processes, and MCP for everyone
else's stuff.
The cleanest way to feel MCP is to point
Claude at any MCP server and let it
discover what's there. For my example,
I'm going to use the Linear MCP server.
I've put all that in my .env file.
And it's going to connect and see the
tools that is available.
As you can see, the MCP servers key
declares the connection. We have a type,
we have a URL,
a name to refer it to by,
and then optionally an off token.
And tools with the type MCP tool set
configures which tools Claude can use
from that server. The default is all of
them, but if you are trying to scope it
down, definitely put it here.
Now notice that we never wrote a single
tool schema. Claude introspects the
server,
gets the list of tools and their schemas
back, and picks the right one for the
prompt. And as of this video, this is
currently in beta. Note the beta header.
So, let's run it.
If your MCP URL points at, say, Linear's
MCP endpoint, Claude lists Linear's
tools and then calls one. Same for
basically any compliant server. We
didn't define a single tool. We didn't
write a Linear client. Linear is
maintaining that.
MCP servers often expose many, many
tools, and you don't always want Claude
using all of them. That might be you
don't want it to do some write
permissions, or you just don't want to
store all of that in context.
So, let's disable everything by default
and then enable specific tools that we
want. Now Claude can search Slack and
list channels, but can't post or delete.
Useful when you trust a service to read
things, but don't want Claude writing on
your behalf by accident.
MCP [music] exists so you don't have to
maintain integrations someone else has
already built. Tools for your data,
skills for your process,
MCP for third-party services. Go to
modelcontextprotocol.io
for the list of available servers and to
learn more about this protocol.
