#!/usr/bin/env python
from panflute import *
import sys

def prepare(doc):
    doc.linklist = []

def translate_ru(elem, doc):
    if type(elem)==Para:

        # Walk it and look for links first
        elem.walk(strip_links)

        english = stringify(elem)

        #translate_client = translate.Client()
        #rooskie = translate_client.translate(
        #        english,
        #        target_language = 'ru')
        #rooskie = rooskie['translatedText']

        rooskie = "woeiureu <<<1>>> rpoqiwuep roiquwproiuqwpe oirupqow eir"

        new_elems = convert_text(rooskie,input_format='markdown')
        div = Div(*new_elems)
        return div


def strip_links(elem,doc):
    """
    Each link will be stripped in the translation process,
    but we insert symbols <<<1>>> where each link should go
    so they survive the translation process.
    """
    if isinstance(elem,Link):
        i = len(doc.linklist)+1
        doc.linklist.append(elem.url)
        snowflake = '<<<%d>>>'%(i)
        link_content = elem.content
        link_content += [Space,Str(snowflake)]

def finalize(doc):
    """
    Find instances of <<<1>>> and replace them
    with the corresponding links.
    """
    for i,url in enumerate(doc.linklist):
        snowflake = '<<<%d>>>'%(i+1)
        replacetext = '[%d]'%(i+1)
        a = Link(Str(replacetext),url=url)
        doc = doc.replace_keyword(snowflake,a)


def main(doc=None):
    return run_filter(translate_ru, prepare, finalize, doc=doc)


if __name__=="__main__":
    main()

