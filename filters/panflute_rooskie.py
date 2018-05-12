#!/usr/bin/env python
import panflute as pan
from google.cloud import translate

"""
OLD
Use ruskie.py
"""

def fake_translate_ru(elem, doc):
    if type(elem)==pan.Para:

        # Walk it and look for links first
        links = elem.walk(fake_extract_links)

        english = pan.stringify(elem)
        translate_client = translate.Client()
        #rooskie = translate_client.translate(
        #        english,
        #        target_language = 'ru')
        #rooskie = rooskie['translatedText']
        rooskie = "woeiureu rpoqiwuep roiquwproiuqwpe oirupqow eir"
        return_para = []
        for r in rooskie.split(" "):
            return_para.append(pan.Str(r))
            return_para.append(pan.Space)

        return pan.Para(*return_para)


def fake_extract_links(elem,doc):
    """Extract links."""
    if isinstance(elem, pan.Link):

        english = elem.args
        translate_client = translate.Client()
        rooskie = translate_client.translate(
                english,
                target_language = 'ru')
        rooskie = rooskie['translatedText']

        return elem


########################################


def translate_ru(elem, doc):
    """
    Translate text into Russian
    """
    if type(elem)==pan.Para:

        # Walk it and look for links first
        links = elem.walk(extract_links)

        english = pan.stringify(elem)
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


def extract_links(elem,doc):
    """Extract links."""
    if isinstance(elem, pan.Link):

        english = elem.args
        translate_client = translate.Client()
        rooskie = translate_client.translate(
                english,
                target_language = 'ru')
        rooskie = rooskie['translatedText']

        return elem


def main(doc=None):
    return pan.run_filter(fake_translate_ru, doc=doc)


if __name__ == "__main__":
    main()
