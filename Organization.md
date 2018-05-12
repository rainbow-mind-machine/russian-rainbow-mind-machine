# How this repo is organized

Here is a rundown of the directory structure
of Russian rainbow mind machine:

```
russian-rainbow-mind-machine/
        rmm/                [submodule]
        site/               [output for static site files, ignored]
        filters/            [pandoc filters, where the translation happens]
        docs/               [Russian markdown documentation]
        mkdocs-material/    [mkdocs documentation theme]
        tests/              [test pieces]
```

Files are as follows:

```
russian-rainbow-mind-machine/
        Makefile            [runs rmm documentation through translation filter]
        mkdocs.yml          [mkdocs documentation config file]
        requirements.txt    [helps pip install required software]
```


