<!-- https://anthropic.skilljar.com/introduction-to-model-context-protocol/296699 -->
<!-- jwplayer-srt: https://cdn.jwplayer.com/tracks/tGeGbDbu.srt -->

# Defining resources

In this video, we're going to move on to the next major feature inside
of MCP servers, which is Resources. To
help you understand resources, we're going to be implementing another
feature inside of our project. Here's what we're going to add in.
I want to allow a user to mention a document
by putting in an @ symbol and then the name of a document.
Whenever they do so, I want to automatically fetch the
contents of that document and insert it into the prompt
that we send off to Claude. So in total, there's kind
of two aspects to this feature. Whenever user types
out the @ symbol inside the message, we're going to automatically
show a list of all the different documents that they can mention
inside of a little autocomplete window. Then whenever
user submits a message with a mention inside of
it, we're going to automatically get the contents of that document
and insert it into the prompt that we send off to Claude.
So for example, if a user says something like what's
in the @report.pdf file, I
would want to assemble a prompt like this and send it to Claude.
So we're going to have the query inside there from the user, and
then we're also going to tell Claude that the user might have referenced
some document, and here is the contents of the document.
So the approach here or the idea here is that we will
not have to rely upon Claude to go and make
use of some tool to figure out what is inside of the
report.pdf file. Instead, the user can just
preemptively mention the file, and we're going to automatically
insert some context ahead of time. Now, one thing I
want to clarify here is that we're kind of talking about two
separate features. The first feature is that whenever
a user types in the @ symbol, we really need
the MCVP server to give us a list of all the
different documents that the user can possibly mention.
And then the second aspect here is that whenever a
user submits a message that contains a mention, then
we need the MCP server to give us the contents of a single
document. To get this information out of our MCP server,
we are going to be making use of resources. Resources
allow our MCP server to expose some amount
of data to the client. We usually define one resource
for each distinct read operation. So in
our example, we need to get a list of documents and
read the contents of a single document. So we would
probably end up making two separate resources. One
resource would be responsible for returning just a list
of document names so we can put them inside the autocomplete,
and then we would probably make another resource that will expose
the contents of a single document based upon its
document ID. When we define these
resources, they are going to be accessed through our MCP
client. So the entire flow that we're going to eventually
put together here, whenever user types in something
like what's in the @ and then presumably
they're going to put in something right there, as soon as they type in that @
character, we need to display a list of document
names to put in the auto complete. So our
code is going to reach out to the MCP client,
which in turn is going to send a read resource
request off to the MCP server.
Inside of that read resource request, we're going to include
something called the URI. That is essentially
the address of the resource we want to read.
This URI gets defined whenever we put together
our resource initially. So the URI is that
right there. When we send
off this read resource request, the MCP
server is going to look at the exact URI that we put inside
of here, and then run the function we
put together right there. Take the result and
send it back to us inside of a read resource
result message. We can then take the data
inside there and display it inside of our autocomplete or do
whatever else we need to do with it. There are two different
types of resources, direct and templated. You'll
also sometimes see direct resources referred to as static
resources. A direct resource just has
a static URI, so it's always going to be the exact
same thing, such as docs, colon slash slash documents.
A templated resource will have one or more parameters
inside of its URI. So for example, we might have documents
slash, and then kind of a wildcard right here. So
we can put in any document ID we want to. And
whenever we ask for this resource, that document
ID right there inside the URI will be automatically parsed
by the Python MCP SDK and
provided as a keyword argument to our function.
The keyword argument will have the exact same name of whatever
string you put in right there. So Doc ID right there will
be Doc ID right there. As
you can probably guess, we'll make use of templated resources anytime
that we want to allow a little bit more selection or variety
or customization in what someone is asking for
out of our MCP server. Implementing resources
is pretty straightforward. So let's go back over to our editor and we're
going to add in some resources to our server right away.
All right, so back over inside my editor, I will find the MCP
server.py file. I'm then going to scroll down a
little bit and I'm going to find some comments for writing
a resource to return all document IDs and
writing a resource to return the contents of a particular
document. Now for this first one right here, I
put in the comment Document IDs. Remember
for us, our document IDs are essentially the
name of the document. So for us, we're really just returning
these IDs. They're going to serve the purpose of the name. That
means we can put them directly into that autocomplete element.
All right, so to make our resource, I'm going to delete
that to do. and then I'll add in an MCP.resource.
The first argument is going to be the URI for accessing
this thing. Again, it's kind of equivalent to a route handler.
So I will use docs, colon slash
slash documents, and I'm also going
to add in a MIME type of application
slash JSON. A resource can
return any type of data, so it can be plain text,
it can be JSON, it can be binary data, anything.
It's up to us to kind of give our client a hint
as to what kind of data we are returning. To do
so, we're going to define this MIME type. A MIME
type of application slash JSON is a hint to
our client, who's eventually going to ask for this resource
right here, that we're going to be sending back a string that
contains some structured JSON data. And
so it would be up to our client to de-serialize
that data, or essentially turn it into some usable data
structure. Underneath that decorator, I'll
write out my function of list_docs, and
I'm going to return a list of strings. And
then inside there, I will return list_docs
keys. So just take all the keys out of that dictionary and
turn it into a list, and I'm going to return it. Now,
you'll notice that we are not returning distinct JSON here.
In other words, we're not actually returning a string. The MCP
Python SDK is going to automatically take whatever we return
and turn it into a string for us. All
right, let's take care of our second resource. So I'm going
to delete that comment and then replace it with MCP
resource, docs, colon
slash slash documents. And then this time I
want a templated resource because I'm putting in this
wildcard right here. And
then my mind type this time around, just for a little
bit of variety, I'm going to be returning plain
text because it's going to be just the contents of the document.
And I'm not going to wrap it up in any kind of structure. Now,
just so you know, in a real application, something
like read a document, I would probably return
an entire document record. So some kind of
dictionary that contains maybe the ID, the
content, the author name, the author ID, and
stuff like that. But just for the sake of an example, I'm
going to return just the text at the document to show
you how we would normally return plain text. So
in this scenario, my MIME type would be text slash plane,
and then I will make fetch_doc.
I'm going to take doc_id, which is going to be a string,
and I'm going to return a string. Once again, whatever
word you put right there, it's going to show up as a
keyword argument inside of your function. If we
added in some additional parameters inside of here, such
as maybe doc_type or something like that, it would
just show up as an additional keyword argument
like so. Then
inside of here, I'm going to first make sure that the ID that this person
is asking for actually exists. So if doc_id
not in docs, I'm
going to raise a ValueError with
an f-string that says doc with ID not
found. And then if we get past that check, I'll
return docs[doc_id]. And
that's it. Now let's try testing this stuff out inside
of our MCP Inspector once again. So
remember at our terminal, we can run the command UVicorn,
mcptest.mcpserver:app --reload.
That's going to start up a web server at port 6277
or C_VI 6274 as the default. So I'm going
to make sure I open that up inside my browser. Here
we go. I'll click connect. I'll then find
resources. And then I should be able to list
out all the different resources that are available. Now when
I list out resources, this is going to be specifically static
or direct resources. So I'll see only docs
slash documents. And then I can separately list
out all my different resource templates. And so I'll see
that I have one resource template of fetch_doc.
I can first try to run the slash documents
right here. We'll see what we get back. So this
is the actual message, the exact structure that
gets returned from our MCP server. You'll
notice that it has a text property and inside there is all
the data that we are returning serialized as JSON
string. So again, it would be up to us inside
of our CLI application to take this text right here and
deserialize it from this JSON string into
a usable list of strings. Then
we can also test out fetch_doc. So I'll click on that.
I have to enter a doc ID. So I'm going to put in.
I want to read the report.pdf
file. And I'll read
the resource. And now I should see the contents
of that particular document. And you'll notice this
is around. Once again, I get a text slash plain. So that's
a hint to me that this is plain text. And I should
not attempt to deserialize it from JSON in
any way.
