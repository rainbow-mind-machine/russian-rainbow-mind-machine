## Dealing with Links

One of the pain points of translating a document is figuring out 
what to do with hyperlinks. Here's how we deal with it:

We have a `prepare()` method in our panflute filter that is run 
before the document filter is applied, and a `finalize()` method
that is run after the document filter is applied.

The prepare method initializes an empty list to hold links.
As we parse each section of the document, we look for 
links, and when we find a link, we add the link to a list.

When the text is translated, links are stripped out and 
the original link text becomes plain text again.
Rather than try and determine which words in the 
translation map to the original link text,
we simply aggregate the links at the bottom of the 
document. Each link includes a translation of the 
original link text that is a link to the original link.

## Panflute Filter

Let's cover a bit more of the panflute magic that makes 
all of that happen.

This relies on two additional methods for the filter:
`prepare()` and `finalize()`.

The prepare method just creates an empty list that will
be used to store all of the link elements in the document:

```
def prepare(doc):
    doc.linklist = []
```

We call the `elem.walk()` method on each element of the 
document, so we have a chance to see each element and 
determine if it is a link. If it is, we keep it simple
and just save the entire element:

```
def strip_links(elem,doc):
    """
    Each link will be stripped in the translation process.
    Save them for the end.
    """
    if isinstance(elem,Link):
        doc.linklist.append(elem)

```

