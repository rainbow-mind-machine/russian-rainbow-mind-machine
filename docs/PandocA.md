## Pandoc Parser: Markdown-to-JSON Parser

We use pandoc to convert structured Markdown into JSON.
This is done using the `-f` flag to specify the input format
and the `-t` flag to specify the target format:

```text
pandoc -t json -f gfm my_markdown_file.md
```

Here, we use `gfm` (Github-flavored markdown).

We can also read documents from stdin using the `-s` flag:

```text
cat my_markdown_file.md | pandoc -t json -f gfm -s 
```

The resulting JSON is ready to be parsed using a pandoc filter.

Note that if you wish to visualize the structure of the JSON
before processing it further, you can pipe it to `python -m json.tool`,
which nicely formats the JSON for printing and visualizing:

```text
cat my_markdown_file.md | pandoc -t json -f gfm -s | python -m json.tool 
```

