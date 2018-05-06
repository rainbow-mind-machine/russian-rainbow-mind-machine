# russian-rainbow-mind-machine

This repository translates 
[rainbow mind machine](https://git.charlesreid1.com/b-rainbow-mind-machine)
documentation into Russian
using the Google Cloud Translate API.

## The Steps

Rundown of necessary steps:

* Create Google Cloud account
* Enable Googe Cloud Translate API
* Set up command line tool
* Test command line tool
* Parse and translate Markdown: English to Russian


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

```
gcloud auth activate-service-account --key-file=[PATH]
```


## Test Command Line Tool

The API endpoint we will use is:

```
https://translation.googleapis.com/language/translate/v2
```

To call this endpoint, we have to include 
a payload containing our API key, which we
obtained earlier when we enabled the API.
The `gcloud` tool provides a way to insert
credentials easily:

The command 

```
$ curl -s -X POST -H "Content-Type: application/json" \
    -H "Authorization: Bearer "$(gcloud auth print-access-token) \
    --data "{
        'q':'Rainbow mind machine is extendable to keep bots from becoming boring. There are only two components to extend. These two components have a simple and clear order of function calls. Rainbow mind machine uses sensible defaults.',
        'source': 'en',
        'target': 'ru',
        'format': 'text'
    }" "https://translation.googleapis.com/language/translate/v2"
```

should yield the result:

```
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

## Parse and Translate Markdown: English to Russian

To do this, we use pandoc to extract information
from the Markdown document as JSON, extract the text
to be translated, pass it into API calls, and re-assemble
the result into Markdown.

To convert `sheep.md` to `sheep.json`,

```
cat sheep.md | pandoc -t json -s | python -m json.tool > sheep.json
```

In general, the text that needs to be translted is in a dictionary 
contains a key-value pair `{"t" : "Plain"}` (and another nested
dictionary that contains each word in the sentence.

This gives us a way to proceed with extracting only the 
text that needs to be modified,nd maintaining proper 
formatting.


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



