# russian-rainbow-mind-machine

This repository translates 
[rainbow mind machine](https://git.charlesreid1.com/b-rainbow-mind-machine)
documentation into Russian
by applying the magic of 
Google Cloud Translate API
with a pandoc filter.

[How this repo is organized](Organization.md)

## Part 1: Google Cloud Translate API Setup

The Google Cloud Translate API is what makes this all possible.

It is easier to translate documentation into Russian 
than it is to figure out how to parse Markdown programmatically
with panflute and pandocs.

[Part 1: Setup](Setup.md)

## Part 2: Pandoc

We want to parse and translate Markdown written
in English, and turn it into Markdown written in 
Russian. We use pandoc to parse the Markdown file
and identify the bits that can be translated,
pass them to the Google Cloud Translate API,
and convert the translated text back into
Markdown.

[Part 2A: Pandoc Parser: Markdown to JSON](PandocA.md)

[Part 2B: Pandoc Parser: JSON to JSON](PandocB.md)

## Part 3: Panflute

Panflute is a Python library for writing Pandoc filters.
It is picky and tricky.

[Part 3A: Panflute Filter: Translate](PanfluteA.md)

[Part 3B: Panflute Filter: Dealing with Links and Headers](PanfluteB.md)

## Part 4: Pandoc

The panflute filter will process JSON and return more JSON,
so we have one last step, which is converting the final
JSON document into Markdown.

[Part 4: Pandoc Parser: JSON to Markdown](PandocC.md)

## Part 5: Testing

You do want to write tests for all of this stuff, don't you?

[Part 5: Testing](Testing.md)

## Part 6: Useful Links

[Part 6: Useful Links](Links.md)
