# How this repo is organized

Here is a rundown of the directory structure
of Russian rainbow mind machine:

## Documentation directories

The purpose of this library is to provide Russian documentation for rmm.
The documentation is located here:

```
russian-rainbow-mind-machine/
        rmm/                [submodule - rainbow mind machine]
        rmm/docs            [English rainbow mind machine documentation (markdown)]
        ruskie_docs/        [Russian rainbow mind machine documentation (markdown)]
        mkdocs-material/    [submodule - mkdocs documentation theme]
        mkdocs.yml          [mkdocs documentation config file]
```

Mkdocs is used to generate documentation. The mkdocs-material theme
is used to turn it into a web page.

## Translation materials

The translation is carried out by converting documents 
from English markdown to Russian markdown via a pandoc
pipeline. The pandoc pipeline is a filter applied to
each portion of the document.

The translation materials are located here:

```
russian-rainbow-mind-machine/
        filters/            [pandoc filters, where the translation happens]
        tests/              [test pieces]
        translate           [python script to do the translation]
        requirements.txt    [helps pip install required software]
```

