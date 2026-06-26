<!-- https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296287 -->
<!-- jwplayer-srt: https://cdn.jwplayer.com/tracks/vqeJrkXx.srt -->

# The StreamableHTTP transport

Time to discuss the Streamable HTTP
transport. This transport allows us to send messages
between a client and a server over an HTTP connection.
The nice thing about this transport is that it really enables remotely
hosted MCP servers. So whereas with the
standard IO transport, we always had to run the client
and the server on the same machine. With the Streamable HTTP
transport, we can remotely host our server. So
our remote server might be hosted at MCPServer.com
or something like that. This really opens the door to a much
wider range of possibilities around MCP servers,
because you can make a public server that anyone can
connect to. However, as I've hinted
at over the last couple of videos, there are some settings
that you might need to apply to this transport that
will limit the functionality of your MCP server,
specifically limit the types of messages that
you can send from the server back over to the client.
So that is the big issue that I want
you to be aware of. There are some settings that are going to restrict
the functionality of the server when you are using this
particular transport. So if you are ever developing
an application on your local machine and everything
is working just fine with the standard IO transport and
then you deploy and you start to use the HTTP transport
and things aren't working quite so well, this is the video you want
to come back to to understand what is going on.
To get started, I would like to give you a quick demonstration of
an app that I showed you previously inside of this course. You
might recall this Wikipedia research assistant. It
makes use of a next JS application that is connected
to an MCP server that implements a research
tool. This server is using the Streamable
HTTP transport, so I will be able to use
this application to show you a couple scenarios where the
Streamable HTTP transport doesn't quite
work as expected. First, I'm going to
send off a request here, just going to ask for
a report on archaeology, just to remind you what this application
looks like. So usually, when I send in a query
like this, I'm going to see a call tool request
here, and I get a nice progress bar, I get status
updates, and eventually, if I wait just
a little bit, I will get a full
response. Now over here inside the source code for
the MCP server, you'll notice that there are two settings that
I have commented out. Stateless HTTP and
JSON response. By default, these settings
are set to false, but there are going to be some scenarios
where you very much have to enable them or set them to true,
and it will go into more details on what those scenarios are a little bit
later on. Changing these settings to true is going
to impact the functionality of your MCP server,
and in some cases, it might even break how your client
works. So let me show you an example of this right away. I
want to change stateless HTTP to be true.
I'm going to save the file. Then I'm going to reload
the page and run the exact same query again.
And now you're not going to see a big difference
here, but there is something you'll notice right away. You'll
notice that now I don't get a progress bar anymore.
So no progress bar whatsoever above the log
statements. In addition, if I let this just sit here for a
while, and I'm going to speed the video up, We
will see that eventually the request fails entirely without
generating any text. Now I'm going to refresh
the page, I'm going to turn on JSON response
to be true, save the file, and then run
the exact same query again. Now we'll see that with
both these settings set to true, we get some even more surprising
results. Now I don't see any progress bar, I don't get
any log statements, and take my word for it if we let this
just sit here, the request is going to fail again.
So right away, we can see at these two settings, although seemingly
innocuous, have a big impact on our MCP
server. So the rest of this video is all about helping you understand
what these settings are talking about, why we might set them
to true, and exactly what's going on here.
First, I want to give you a very quick reminder of a diagram I
showed you in the last video. And I made a big deal about how
the standard IO transport had the ability to
initiate a request from the client to the server and then get a
response back. And likewise, the server
at any point in time could initiate a request
off to the client and get a response back.
So keep in mind for just a moment, as I give you a quick
review on HTTP communication.
So this is going back to some of the basics around HTTP,
and this is all HTTP communication, not
just MCP related stuff. So
as a reminder, if we have a client and a server, at
any point in time, a client can very easily make a request
off to the server. For example, on the right-hand side, the
client can make a post-request off to the server and
expect to get back some kind of response. No
issue with this setup whatsoever. So
translating this over to the MCP world, that means that if we
want to make an initial request from the client to the server, no
problem is going to work. And if we want to get a response
from the server backward the client, no problem whatsoever is
going to work just fine. However, if we consider
the reverse scenario, if the server wants
to initiate a request down to the client, that's
not quite so easy with HTTP requests.
At a very basic level, the server doesn't know the
address of the client, and the client might not even be publicly
accessible. So it's very challenging in traditional
HTTP for the server to initiate a
request down to the client. And that means that in
our MCP world, it's really hard for the server
to send that initial request down, and it also means
that it's kind of hard to imagine how you'd ever expect
to get a response from the client back to the server.
So if we consider this diagram that we looked at a moment ago,
where I had told you that there are some requests that
are being issued from the server down to the client, that
means that in this HTTP world, there
are some message types that are just plain
tough to implement with normal HTTP
requests. Specifically, sampling request,
listing routes, progress notifications, and logging notifications,
along with some other message types that I'm just not showing on this diagram,
are tougher to implement in an HTTP world.
And sure enough, that's kind of what you saw back over here
with this demo. As soon as I started to flip some of these
properties from false to true, well, you saw some
different parts of the application start to break and just not work
as expected. And what exactly broke?
Well, that's right. The progress notification broke, the
logging broke, and sampling, or essentially the
create message request broke as well. Sampling was being
used to author the fund research report.
Now I do have some good news. Even though making requests
from a server down to a client is challenging
in a pure HTTP world, the Streamable
HTTP transport does have a clever solution.
But there are some caveats that you need to be aware of. Let's
take a look at how the transport actually works and exactly what
those caveats are in just a moment.
