## Useful Links

* Markdown to structured JSON using pandoc: 
    * [Text.Pandoc.JSON](https://hackage.haskell.org/package/pandoc-types-1.17.4.2/docs/Text-Pandoc-JSON.html)

* How to write Pandoc filters using Python: 
    * [pandocfilters](https://pypi.org/project/pandocfilters/)

* Example reading from stdin:
    * `pandoc -t json -s | ./caps.py | pandoc -f json`

* Link to examples:
    * [pandocfilters examples](https://github.com/jgm/pandocfilters/tree/master/examples)
    * [caps.py](https://github.com/jgm/pandocfilters/blob/master/examples/caps.py)

* requests library Python:
    * [requests quickstart](http://docs.python-requests.org/en/latest/user/quickstart/)
    * `>>> r = requests.put('http://httpbin.org/put', data = {'key':'value'})`

* pandocfilters
    * [pandocfilters](https://github.com/jgm/pandocfilters)
    * also see [but i don't want to learn haskell](http://pandoc.org/filters.html#but-i-dont-want-to-learn-haskell) on pandoc.org.

