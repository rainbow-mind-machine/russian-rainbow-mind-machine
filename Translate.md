# Translate

We want to parse and translate Markdown written
in English, and turn it into Markdown written in 
Russian. We use pandoc to parse the Markdown file
and identify the bits that can be translated,
pass them to the Google Cloud Translate API,
and convert the translated text back into
Markdown.

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


## Pandoc Filter: Translate

To translate Markdown text to Russian, we want to look for 
Para (paragraph) components, and extract the text from 
each paragraph as a string.

```text
cat shepherd.md | pandoc -t json -f gfm -s | ./panflute_rooskie.py 
```


The `panflute_rooskie.py` filter does the translating.
Here is the basic structure of that document.
Here we use the Google Cloud API from Python directly,
rather than fussing with assembling our own payloads
and using the `requests` library.

**`panflute_rooskie.py`:**

```python
from panflute import *
from google.cloud import translate


def translate_ru(elem, doc):
    ...


def main(doc=None):
    return run_filter(translate_ru, doc=doc)


if __name__ == "__main__":
    main()
```

When we run this, it passes each document element through
`translate_ru()`. We want this method to search for 
paragraphs, extract the string, and pass them to the 
Translate API:

```python
def translate_ru(elem, doc):
    if type(elem)==Para:
        english = stringify(doc)
        translate_client = translate.Client()
        rooskie = translate_client.translate(
                english,
                target_language = 'ru')
        
        ...
```

Note that this method is much easier, but requires
exporting an environment variable `$GOOGLE_APPLICATION_CREDENTIALS`
that points to a JSON file with your API keys
(see [Setup](#setup) section above):

```
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/project-key-00000.json
```

The translation API will return unicode text. This needs to be 
converted into a format that pandoc can understand. Each word 
must be wrapped using a `Str()` string object, with a `Space` 
object between each word.

To do this, use some basic Python functionality: the `split()`
method and the `append()` method, with a splat `*` operator for
good measure:

```python
def translate_ru(elem, doc):
    if type(elem)==Para:
        english = stringify(doc)
        translate_client = translate.Client()
        rooskie = translate_client.translate(
                english,
                target_language = 'ru')
        rooskie = rooskie['translatedText']
        return_para = []
        for r in rooskie.split(" "):
            return_para.append(Str(r))
            return_para.append(Space)
        return Para(*return_para)
```


## Pandoc Parser: JSON-to-Markdown Parser

To return everything back into Markdown, the last step of the pipeline
is to add another call to pandoc, but with the formats reversed, so that
it will turn JSON back into Markdown:

```text
cat shepherd.md | pandoc -t json -f gfm -s | ./panflute_rooskie.py  | pandoc -f json -t gfm -s > shepherd_ru.md
```


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

See `ruskie.py`.


## Testing

To test the pandoc filter to make sure it is working, you can 
create some Markdown in a file or from the command line, and feed it
through pandoc and into the filter:

```
$ echo "This is a [paragraph](https://example.com) of markdown text." | pandoc -t json -f gfm -s | ./ruskie.py
```


## Useful Links

* Markdown to structured JSON using pandoc: 
    * [Text.Pandoc.JSON](https://hackage.haskell.org/package/pandoc-types-1.17.4.2/docs/Text-Pandoc-JSON.html)

* How to write Pandoc filters using Python: 
    * [pandocfilters](https://pypi.org/project/pandocfilters/)

* Example reading from stdin:
    * `pandoc -t json -s | ./caps.py | pandoc -f json`

* Link to examples:
    * [pandocfilters examples](https://github.com/jgm/pandocfilters/tree/master/examples)
    * [caps.py](https://github.com/jgm/pandocfilters/blob/master/examples/caps.py)

* requests library Python:
    * [requests quickstart](http://docs.python-requests.org/en/latest/user/quickstart/)
    * `>>> r = requests.put('http://httpbin.org/put', data = {'key':'value'})`

* pandocfilters
    * [pandocfilters](https://github.com/jgm/pandocfilters)
    * also see [but i don't want to learn haskell](http://pandoc.org/filters.html#but-i-dont-want-to-learn-haskell) on pandoc.org.


