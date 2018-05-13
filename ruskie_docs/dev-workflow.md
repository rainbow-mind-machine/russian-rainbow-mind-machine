# Рабочий процесс Dev

# Рабочий процесс документации

Чтобы получить копию документации локально:

# Ленький путь

Оформить копию ветки gh-pages.

# Строительная документация

Чтобы создавать документацию локально, вам понадобятся mkdocs:

    pip install mkdocs

Чтобы сделать документацию, выполните команду mkdocs build из основного
репозитория, чтобы создать сайт в источнике каталога /:

    mkdocs build

Чтобы запустить веб-сервер, используйте легкий HTTP-сервер python:

    cd source/
    python -m http.server 8000

или используйте mkdocs:

    mkdocs serve

# Рабочий процесс исправления ошибок

Рабочий процесс для исправления ошибок и дополнений.

# Рабочий процесс филиала

Рабочий процесс филиала:

  - development takes place on various feature branches
  - the `master` branch contains the latest (unstable) code
  - use tags to release particular versions

# Теги рабочий процесс

Теги рабочий процесс:

  - When you've tested that everything is good to go:
  - Increment version number in `setup.py`
  - Update changelog
  - Create tag for release

Создать команду тега:

    git tag -a vX.Y -m 'rainbow mind machine X.Y'

# Рабочий процесс Pypy

Рабочий процесс Pypi:

  - One-time: set up your .pypirc

  - Make the package bundle

  - Upload the package bundle to Pypi

  - Test the package with virtualenv

  - 
# Рабочий процесс Dockerhub

# связи
