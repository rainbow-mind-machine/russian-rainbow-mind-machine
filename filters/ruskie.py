#!/usr/bin/env python
from panflute import *
import sys
from google.cloud import translate
from google.api_core.exceptions import Forbidden


def english_to_russian(english):
    """
    Use Google Cloud Translate API to translate English to Russian
    """
    try:
        translate_client = translate.Client()
        ru = translate_client.translate(
                english,
                target_language='ru')
        ru = ru['translatedText']
        return ru

    except Forbidden as e:
        sys.stderr.write(str(e))
        sys.stderr.write("Error calling Google Cloud Translate API\n")
        sys.stderr.write("Continuing...\n")
        pass


def prepare(doc):
    doc.linklist = []


def translate_document(elem, doc):
    """
    Extract text from select elements and translate them
    """
    if type(elem)==Para:

        # Walk it and look for links first
        elem.walk(strip_links)

        english = stringify(elem)

        rooskie = english_to_russian(english)
        new_elems = convert_text(rooskie,input_format='markdown')
        return new_elems

    elif type(elem)==Header:
        english = stringify(elem)
        rooskie = english_to_russian(english)
        h = Header(Str(rooskie))
        return h


def strip_links(elem,doc):
    """
    Each link will be stripped in the translation process.
    Save them for the end.
    """
    if isinstance(elem,Link):
        doc.linklist.append(elem)


def finalize(doc):
    """
    Create an unordered list at the end of the document
    containing all of the links.
    """
    en = "Links"
    ru = english_to_russian(en)
    h = Header(Str(ru), level=1)

    doc.content.insert(len(doc.content),h)

    for link in doc.linklist:
        en = stringify(link)
        ru = english_to_russian(en)
        link2 = Link(Str(ru), url=link.url)
        doc.content.insert(len(doc.content),Para(link2))


def main(doc=None):
    return run_filter(translate_document, prepare, finalize, doc=doc)


if __name__=="__main__":
    main()

