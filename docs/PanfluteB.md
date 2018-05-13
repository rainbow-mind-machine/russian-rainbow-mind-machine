## Dealing with Links

One of the pain points of translating a document is figuring out 
what to do with hyperlinks. Here's how we deal with it:

We have a `prepare()` method in our panflute filter that is run 
before the document filter is applied, and a `finalize()` method
that is run after the document filter is applied.

The prepare method initializes an empty list to hold links.
As we parse each section of the document, we look for 
links, and when we find a link, we add it to the 
link list. We then insert a marker, `<<<1>>>`, that
marks where that link should go.

Once the text has been translated, the `<<<1>>>` symbols
remain intact and are replaced with `[1]`, hyperlinking 
to the original link.

