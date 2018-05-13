# Использование радужной машины разума с докером

Чтобы использовать машину радужного разума из контейнера докера, вы
можете сами создать контейнер, используя файл Docker в этом
репозитории; вы можете использовать изображение контейнера из
dockerhub; или вы можете использовать файл docker compose и файл
docker-compose.yml в этом каталоге.

# Строительство автономного докерного контейнера

Вы можете использовать скрипт make\_rmm\_container.sh для создания
базового контейнера машины с радужным сознанием (называемого
rmm\_base):

# Тяжелая докерная тара

Вы также можете вытащить контейнер из докер-хаба:

    docker pull charlesreid1/rainbowmindmachine

Радужная машина ума на докер-хабе

# Docker Compose

Например, бот, использующий машину радужного разума в контейнере докера,
см.

  - [b-apollo](https://git.charlesreid1.com/bots/b-apollo)
  - [b-ginsberg](https://git.charlesreid1.com/bots/b-ginsberg)
  - [b-milton](https://git.charlesreid1.com/bots/b-milton)

Основные шаги заключаются в следующем:

  - Create a Twitter application
  - Create a rainbow mind machine bot application
  - Run the container pod interactively once with `docker-compose run
    <name-of-service>`
  - Run the container pod in detached mode with `docker-compose up -d`

# Проблемы с разработчиками

# Управление размером изображения Docker

Официальные изображения Pockon Docker огромны: абсолютное наименьшее
изображение составляет 200 МБ, а полный контейнер python 3 с
использованием debian занимает около 1 ГБ.

Чтобы уменьшить размер этих изображений, вы можете использовать
несколько стратегий.

  - Используйте альпийский вариант для «реальной сделки» - он разработан
    как минимальный, но требует объединения любых «дополнений» в
    контейнер

  - Используйте изображение, предназначенное для небольших
    
      - [jfloff/alpine-python](https://github.com/jfloff/alpine-python)

  - Поддерживать логическое разделение
    
      - one container per flock
      - one pod per server

# связи

[Радужная машина ума на докер-хабе]()
