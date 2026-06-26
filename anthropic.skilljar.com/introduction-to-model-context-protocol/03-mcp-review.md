<!-- https://anthropic.skilljar.com/introduction-to-model-context-protocol/296691 -->
<!-- jwplayer-srt: https://cdn.jwplayer.com/tracks/bxkuJl5N.srt -->

# MCP review

We are all done with our project, but before we move on, I want
to do a quick recap on the three server primitives
that we learned about. So tools, resources, and prompts.
In particular, I want to highlight something interesting about each of
these. Namely, what part of an app is really
responsible for running each? In other words, in
a typical application, who is really running each
of these things and who benefits from them? Well,
we would say that tools are model controlled. This
means that Claude alone is really responsible for
deciding when to run a given tool. Resources
are app controlled. In other words, some code
running inside of your app is going to decide that
it needs some data provided by a resource. It will
be your app's code that decides to execute a resource
and use the return data in some way, maybe by
using that data in the UI or something like that. In
our case, we fetch a resource and then use
that data inside the UI to provide a list of autocomplete
options. We also fetch a resource
to augment a prompt. Both of those things were really application-related
code that was authored by you and I to
put together. And finally, prompts
are really user-controlled. So a user decides
when a prompt is going to run. A user might
start the invocation of a prompt by clicking on some UI
element, like a button or a menu option,
or they might make use of a slash command, which is what we
did. The reason I highlight what is controlling each
of these is to give you some idea of their purpose.
So if you ever need to add capabilities to
Claude, you're probably going to want to look at
implementing some tools inside of your MCP server or
consuming some server's tools through
your MCP client. If you ever
want to get some data into your app for the purposes of showing
content in UI or something similar, then you
probably want to use a resource. And if you ever
want to implement some kind of predefined workflow, you
probably want to look at prompts. Now
you can see examples of all these ideas inside
of the official Claude interface at
Claude.ai. So here's what it currently looks
like for me. You'll notice that underneath the
main chat input are some buttons right here. If
I click on one, and then click on one of these
examples, you'll see that I immediately dove
into a chat. So this was a user-controlled
action. I, as the user, decided to start
off this particular workflow, and I'm making use of a
prompt that was probably already written ahead of time
and probably has been optimized in some way. So
to implement that list of buttons right there, we would probably want
to put together a series of different prompts inside of a MCP
server. Likewise, if I go back and
maybe click on this little tab right here, the plus button,
you'll notice that I have a add from Google Drive button.
Now, I'm not going to click on it because it's going to show some of my internal
documents. But if I click on that button, I'm going to see some
documents that I can add into this chat as some context.
Knowing what documents to actually render in that list,
and then whenever I click on one, automatically injecting its
contents into the context of this chat, that is all
application-related code. So it is solely
the application that needs to know the list of documents
to render here. And that's, again, specifically
UI-related elements. So to implement
that listing of documents from Google Drive, I
would probably look at implementing a resource inside
of an MCP server. And then, finally, if I
enter in a message to this chat of something like,
what is squared three use JavaScript to calculate the value
and send it off, I'm clearly expecting Claude
to somehow execute some JavaScript code, which would
likely be done through the use of a tool. In
this case, the decision to use a tool was 100% model
controlled. It is the model that decided to use some
JavaScript tool execution. To implement something
like this inside of an MCP server, we'd likely
want to, you guessed it, provide a tool.
So in total, that's our three different server
primitives. And each one is really intended to
be used by a different portion of your overall application.
So we got tools which are generally going to serve your model,
resources, which are generally going to serve your app,
and prompts which are going to serve your users. And
once again, these are high level guidelines. And the only reason
I mentioned them is to just give you a sense of when
you should use each of these primitives, depending upon what
you are trying to put together.
