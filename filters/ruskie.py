#!/usr/bin/env python
from panflute import *
import sys
from google.cloud import translate
from google.api_core.exceptions import Forbidden

def prepare(doc):
    doc.linklist = []

def translate_ru(elem, doc):
    if type(elem)==Para:

        # Walk it and look for links first
        elem.walk(strip_links)

        english = stringify(elem)

        sys.stderr.write("About to call Google Cloud Translate API\n")
        sys.stderr.write("String length: %d\n"%(len(english)))
        try:
            translate_client = translate.Client()
            rooskie = translate_client.translate(
                    english,
                    target_language = 'ru')
            rooskie = rooskie['translatedText']

            new_elems = convert_text(rooskie,input_format='markdown')
            return new_elems

        except Forbidden as e:
            sys.stderr.write(e)
            sys.stderr.write("Error calling Google Cloud Translate API\n")
            sys.stderr.write("Continuing...\n")
            pass



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
    list_items = []
    for link in doc.linklist:
        list_items.append(ListItem(Para(link)))
    bullet_list = BulletList(*list_items)
    # doc.content is a sequence of Element objects
    # under the hood, that's just a ListContainer
    # and the ListContainer is, under the hood, just a list
    doc.content.insert(-1,bullet_list)


def main(doc=None):
    return run_filter(translate_ru, prepare, finalize, doc=doc)


if __name__=="__main__":
    main()

