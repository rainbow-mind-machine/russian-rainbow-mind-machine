## Panflute Filter: Translate

To translate Markdown text to Russian, we want to look for 
Para (paragraph) components, and extract the text from 
each paragraph as a string.

```text
cat shepherd.md | pandoc -t json -f gfm -s | filters/ruskie.py
```


The `ruskie.py` filter does the translating.
Here is the basic structure of that document.
Here we use the Google Cloud API from Python directly,
rather than fussing with assembling our own payloads
and using the `requests` library.

**`filters/ruskie.py`:**

```python
from panflute import *
from google.cloud import translate


def translate_document(elem, doc):
    ...


def main(doc=None):
    return run_filter(translate_document, doc=doc)


if __name__ == "__main__":
    main()
```

When we run this, it passes each document element through
`translate_document()`. 

Two things we wnat to do up front:

* Extract links (these are problematic for translation, 
    we deal with them by removing the link from the inline text
    and including a list at the bottom of the document of 
    the (translated) original link text, plus the link itself.

* Search for paragraphs of text, or headings, and replace text
    with a Russian translation.

To do the first, we define a function called `strip_links()`, 
which will strip out all the links and add them to the bottom 
of the document (more on this in a minute).

We pass this function to `elem.walk()` to apply it to every
element underneath the current element. This means we can 
write the `strip_links()` function in a similar way to the 
`translate_document()` function: look for specific types of
elements, and modify them accordingly.

```python
def translate_document(elem, doc):

    # Walk it and look for links first
    elem.walk(strip_links)

    ...
```

Another thing we want to do is translate paragraph text from
Russian to English. We use stringify to turn a list of Str 
and Space objects into a regular string:

```python
def translate_document(elem, doc):

    # Walk it and look for links first
    elem.walk(strip_links)

    if type(elem)==Para:
        english = stringify(doc)
        russian = english_to_russian(english)
        ...
```

The `english_to_russian()` function (more on this shortly) will use
the Google Cloud Translate API to translate English to Russian.
This requires an API key with Google Cloud (see [Setup](Setup.md)).

Once the translate function returns text, it will be Russian, 
so Unicode. Translate this text back into a format that is 
Pandoc-friendly, meaning wrap strings in Str() and Space objects.
To do this easily with a string in panflute, use `convert_text()`:

```
        english = stringify(elem)
        rooskie = english_to_russian(english)
        new_elems = convert_text(rooskie,input_format='markdown')
        return new_elems
```

To get Google Cloud Translate API working properly, 
you must export an environment variable `$GOOGLE_APPLICATION_CREDENTIALS`
that points to a JSON file with your API keys
EACH TIME YOU RUN THE SCRIPT!!!

```
############################################
############################################
##############                ##############
##############   NOTE         ##############
##############                ##############
##
## This step is required for the translate
## API calls to work. Don't leave this out.
##
############################################
############################################

export GOOGLE_APPLICATION_CREDENTIALS=/path/to/project-key-00000.json
```

