## Panflute Filter: Translate

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



