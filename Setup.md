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





