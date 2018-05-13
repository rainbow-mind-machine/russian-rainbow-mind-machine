
## Pandoc Filter: JSON-to-JSON Filter

To translate Markdown from English to Russian,
we use pandoc to parse the Markdown file and 
extract the text that needs to be translated.

Specifically, we write a JSON-to-JSON pandoc filter
using [panflute](http://scorreia.com/software/panflute/index.html),
a Python library for writing pandoc filters.

The syntax is as follows:

```text
cat my_markdown_file.md | pandoc -t json -f gfm -s | ./my_panflute_filter.py 
```

The convention for panflute filters is that each document component
is passed to the panflute filter, and remains unmodified if the filter
returns nothing. (This saves the filter some extra work.)

In other words, the filter should decide when to take action and 
modify a document component.



