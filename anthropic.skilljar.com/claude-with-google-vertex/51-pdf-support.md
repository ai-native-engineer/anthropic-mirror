<!-- https://anthropic.skilljar.com/claude-with-google-vertex/289198 -->

# PDF support

<!-- jwplayer-srt: https://cdn.jwplayer.com/tracks/09sjqvSY.srt -->

## 자막 (영상 전사)

Besides images, Claude can also read content directly out of a PDF file. I'm going to show you how you do that in this video. Attached to this video, you will find a document called earth.pdf. If you open it up, you'll see that it's just a couple of pages out of the Wikipedia article on Earth. So make sure you download this PDF file and place it inside the same directory as your notebook. To read a PDF file, we use almost the exact same code that we use for reading an image and feeding the image into Claude. So I'm going to find where we are currently opening up an image right here, and I'm going to change it to earth.pdf. I'm going to rename this variable from image bytes to how about file bytes, because no longer are we reading an image. I'm going to make sure I update the variable down here as well. I'm going to change the type right here from image to document, and then the media type will go from image slash png to application slash pdf. And then finally, the question that we're asking of Claude about this document, rather than feeding in our big prompt that we have in the previous cell, I'm going to ask Claude to summarize the document in one sentence. And let's see what we get out of Claude. So I'm going to run this. And there's the summary. It looks like it successfully read the contents of that PDF file. Now, Claude has the ability to not only read text out of a PDF, it can also read images or charts, tables, and so on. So you should really think of Claude as being like a one stop shop for extracting just about any kind of information out of a PDF document.
