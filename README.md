# russian rainbow mind machine

This repository translates 
[rainbow mind machine](https://git.charlesreid1.com/b-rainbow-mind-machine)
documentation into Russian
by applying the magic of 
Google Cloud Translate API
with a pandoc filter.

For documentation about the translation process,
see the translate-yer-docs repository:

* documentation: [https://pages.charlesreid1.com/translate-yer-docs/](https://pages.charlesreid1.com/translate-yer-docs/)
* repo: [https://git.charlesreid1.com/charlesreid1/translate-yer-docs](https://git.charlesreid1.com/charlesreid1/translate-yer-docs)

For the Russian rainbow mind machine documentation:

* HTML: [https://pages.charlesreid1.com/russian-rainbow-mind-machine/](https://pages.charlesreid1.com/russian-rainbow-mind-machine/)
* Markdown: [ruskie_docs/index.md](ruskie_docs/index.md)

This repository contains the following files:
* `rmm` is rainbow mind machine (git submodule)
* `filters` contains the panflute filter used to translate docs to Russian
* `ruskie_docs` contains the translated documentation
* `mkdocs-material` and `mkdocs.yml` are used to make the documentation with `mkdocs`
* `translate` iterates over each English markdown document in `rmm` and calls pandoc to translate it
* `test_google_translate_credentials` translates "Hello world" to make sure your API calls are authenticated OK

