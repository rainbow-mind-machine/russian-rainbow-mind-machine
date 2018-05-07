# russian-rainbow-mind-machine

This repository translates 
[rainbow mind machine](https://git.charlesreid1.com/b-rainbow-mind-machine)
documentation into Russian
by applying the magic of 
Google Cloud Translate API
with a pandoc filter.

[Part 1: Setup](#setup)

[Part 2: Translate](#translate)

# Setup

Rundown of necessary setup steps:

* Create Google Cloud account
* Enable Googe Cloud Translate API
* Set up gcloud command line tool
* Test gcloud command line tool


## Create Google Cloud Account

Creating a Google Cloud account requires a credit card.

Obtaining a credit card is generally straightforward,
and simply involves burrowing your way into the corporate
bureaucracy by getting a job in an IT department. 

Academic institutions provide an optimal environment
for obtaining a credit card to carry out sanctioned
bot flock activities.

## Enable API

Enable the Google Cloud Translate API [here](https://cloud.google.com/translate/docs/quickstart).

## Set Up Command Line Tool

The Google Cloud SDK provides a command line tool
that has utilities for interacting with the APIs.

The prior step will give you a JSON key file. 
Associate this with the command line tool using 
the `auth activate-service-account` verb:

```text
gcloud auth activate-service-account --key-file=[PATH]
```


## Test Command Line Tool

The API endpoint we will use is:

```text
https://translation.googleapis.com/language/translate/v2
```

To call this endpoint, we have to include 
a payload containing our API key, which we
obtained earlier when we enabled the API.
The `gcloud` tool provides a way to insert
credentials easily:

The command 

```text
curl -s -X POST -H "Content-Type: application/json" \
    -H "Authorization: Bearer "$(gcloud auth print-access-token) \
    --data "{
        'q':'Rainbow mind machine is extendable to keep bots from becoming boring. There are only two components to extend. These two components have a simple and clear order of function calls. Rainbow mind machine uses sensible defaults.',
        'source': 'en',
        'target': 'ru',
        'format': 'text'
    }" "https://translation.googleapis.com/language/translate/v2"
```

should yield the result:

```text
{
  "data": {
    "translations": [
      {
        "translatedText": "Радужная машина разума расширяема, чтобы боты не становились скучными. Расширяются только два компонента. Эти два компонента имеют простой и понятный порядок вызовов функций. Машина Rainbow mind использует разумные значения по умолчанию."
      }
    ]
  }
}
```

So far, so good.




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



### Links

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

