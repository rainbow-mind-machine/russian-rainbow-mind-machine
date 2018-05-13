
## Pandoc Filter: JSON-to-JSON Filter

To translate Markdown from English to Russian,
we use pandoc to parse the Markdown file and 
extract the text that needs to be translated.

Specifically, we write a JSON-to-JSON pandoc filter
using [panflute](http://scorreia.com/software/panflute/index.html),
a Python library for writing pandoc filters.

The syntax is as follows:

```text
cat my_markdown_file.md | pandoc -t json -f gfm -s | filters/my_filter.py
```

The convention for panflute filters is that the JSON document
is passed into the panflute filter one component at a time.
If the filter does not return anything, the document element
will be used as-is in the final document. If a new document
element is returned, it is used in place of the old 
document element.



