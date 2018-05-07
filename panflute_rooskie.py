#!/usr/bin/env python
from panflute import *
from google.cloud import translate


def translate_ru(elem, doc):
    if type(elem)==Para:
        english = stringify(elem)
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


def main(doc=None):
    return run_filter(translate_ru, doc=doc)


if __name__ == "__main__":
    main()
