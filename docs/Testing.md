## Testing

To test the pandoc filter to make sure it is working, you can 
create some Markdown in a file or from the command line, and feed it
through pandoc and into the filter:

```
$ echo "This is a [paragraph](https://example.com) of markdown text." | pandoc -t json -f gfm -s | ./ruskie.py
```





