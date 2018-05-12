# Pandoc filters

This directory contains Python scripts to apply filters to pandoc documents.

## Translation

Pandoc turns English Markdown documents into JSON.

These filters extract plain text from JSON, and use the Google Cloud Translate API
to translate the text from English to Russian.

The filters also extract links before the translation is carried out 
and re-insert them at a similar location when the translation is done.

Pandoc then turns the JSON back into Russian Markdown.

## Authentication

To perform this task, you need to authenticate with Google Cloud.
Your authentication key should be set up with `gcloud` (see [../Setup.md](../Setup.md))
and should not need to be stored in this repository.


