## Pandoc Parser: JSON-to-Markdown Parser

To return everything back into Markdown, the last step of the pipeline
is to add another call to pandoc, but with the formats reversed, so that
it will turn JSON back into Markdown:

```text
cat shepherd.md | pandoc -t json -f gfm -s | ./panflute_rooskie.py  | pandoc -f json -t gfm -s > shepherd_ru.md
```



