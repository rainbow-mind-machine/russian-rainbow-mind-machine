#!/usr/bin/env python3
from pandocfilters import toJSONFilter, stringify, Emph, Para
from google.cloud import translate

def translate_ru(key, value, format, meta):
    if(key=='Para'):

        english = stringify(value)

        translate_client = translate.Client()
        rooskie = translate_client.translate(
                english,
                target_language = 'ru')

        rooskie = rooskie['translatedText']
        return Para([rooskie])

if __name__ == "__main__":
    toJSONFilter(translate_ru)

