# Ключ-манипулятор

клавишник

Вы определенно можете доверять этому ключевому клиенту. кредит

Keymaker - это объект, который используется для аутентификации с помощью
Twitter и генерирования ключей OAuth, которые приложение должно делать
от имени пользователя.

# Трехсторонний OAuth-процесс

Keymaker выполняет одноразовый шаг авторизации, который необходимо
выполнить один раз для каждой учетной записи Sheep = Twitter bot =
Twitter.

Keymaker получит набор «предметов» (подробнее об этом в один момент), с
одним элементом = один Овечка = один бот = одна учетная запись Twitter
и т. Д. Keymaker выполняет итерацию через каждый элемент и выполняет
трехногий процесс OAuth ,

Вот краткое описание процесса:

  - The three legs are: the user (the bot account), the
    credential-checker (Twitter), and the consumer (your
    rainbowmindmachine app - specifically, the Keymaker)
  - The Keymaker will initiate the process by requesting an OAuth URL
    from Twitter (this is how a Twitter app asks a user for permission
    to access their account)
  - Twitter will return an OAuth URL to the Keymaker, which will pass it
    to the user
  - The user will open the URL in their browser, and sign in using a bot
    account
  - Twitter will verify the credentials of the user, and create a
    temporary PIN number that is shown to the user
  - The user will copy and paste that PIN number into the Keymaker,
    which passes the PIN to Twitter
  - Twitter verifies the PIN matches the one given to the user, and
    grants the application the access it requested.

Почему песня и танец? Трехсторонний процесс аутентификации предназначен
для того, чтобы приложения могли проверять личность пользователя (т. Е.
Да, этот пользователь фактически предоставил разрешение для приложения
контролировать свою учетную запись) без необходимости обработки
конфиденциальных данных, таких как хэшированный пароль
пользователя. Это также помогает Twitterу контролировать
процесс.

# пример

Давайте посмотрим на пример. Чтобы создать Apollo Space Junk Bot Flock,
мы использовали бы три элемента, соответствующие трем ботам APOLLO
Space Junk (@ apollo11junk, @ apollo12junk, @ apollo13junk). Поскольку
это боты генерации диалога Queneau, три элемента - три файла JSON,
заполненные данными, которые используются ботами для создания
диалога.

# Подклассы Keymaker

машина радужного разума предназначена для расширения, поэтому важно, как
мы создаем производные классы из класса Keymaker.

У нас есть два примера: FileKeymaker и TxtKeymaker. Эти два Keymakers
позволяют Keymaker использовать файлы определенного типа (например,
текстовые файлы или файлы изображений) в качестве «элементов», которые
использует Keymaker для создания ботов Sheep.

# Учетные записи Keymaker

# Ввод ключа: ключи API

Keymaker требует ввода двух частей информации:

  - Consumer token API key
  - Consumer token secret API key

Эти жетоны используются для аутентификации (вашего приложения) с помощью
Twitter и позволяют им подтвердить, что вы являетесь владельцем своего
приложения Twitter. Они не связаны с бот-аккаунтом. Ключи
API-интерфейса потребительского токена и пользовательского
токена должны быть доступны из настроек главной учетной записи
бота.

(Вы создали основную учетную запись бота, не так ли?\!?)

Существует три способа передачи ключей API в Keymaker: через JSON-файл,
через словарь или через переменные среды.

# Использование файла JSON

Чтобы указать ключи API в файле JSON:

apikeys.json:

``` text
{
    "consumer_token" : "AAAAAAA",
    "consumer_secret_token" : "BBBBBBBB"
}
```

Затем создайте Keymaker и настройте ключи API следующим образом:

make\_shepherd\_with\_json.py:

``` python
import rainbowmindmachine as rmm

keymaker = rmm.Keymaker()
keymaker.set_apikeys_file('apikeys.json')
```

# Использование словаря Python

Чтобы указать ключи API, используя словарь python

make\_shepherd\_with\_dict.py:

``` python
import rainbowmindmachine as rmm

keymaker = rmm.Keymaker()
keymaker.set_apikeys_dict({
    "consumer_token" : "AAAAAAAAAAAA",
    "consumer_token_secret" : "BBBBBBBBBBBBB"
})
```

# Использование переменных среды

Этот последний метод полезен, если вы хотите настроить интеграционные
тесты и использовать фактические ключи API, но вы не хотите их жестко
закодировать в файле или подвергать их риску утечки. Большинство
тестовых служб, таких как Travis, предоставляют механизмы для
получения учетных данных и секретов в тестовых контейнерах.

Чтобы использовать этот метод, установите две переменные среды:

``` text
$ export CONSUMER_TOKEN="AAAAAAAA"
$ export CONSUMER_TOKEN_SECRET="BBBBBBBBBBB"
```

Теперь сделайте Keymaker следующим образом:

``` python
import rainbowmindmachine as rmm

keymaker = rmm.Keymaker()
keymaker.set_apikeys_env()
```

# Выход Keymaker: клавиши OAuth

После того, как Keymaker и пользователь пройдут трехсторонний процесс
аутентификации, Twitter предоставит приложению пару токенов OAuth
(токен и секретный токен), которые приложение может использовать для
управления учетной записью пользователя на указанном уровне разрешений
(это будет длиться бесконечно или пока пользователь не аннулирует доступ
в своих настройках Twitter).

Новые токены OAuth можно легко переделать с использованием тех же
трехступенчатых процессов аутентификации, если ключи OAuth
потеряны или пользователь отозвал доступ и должен повторно
предоставить его.

Keymaker выводит эти токены OAuth вместе с другой информацией, которая
будет полезна для объекта Sheep, в словарь Python и выводит ее в файл
JSON, который будет передан Овцам, как только Пастух создаст каждого
Овца.

Файлы JSON - это «бот-ключи», в смысле «ключи к машине» или «ключи к
королевству». Они хранятся в каталоге ключей бота, который можно
настроить (см. Ниже).

# Процесс создания ключа: сделайте ключ

После того, как ваш ключ настроен с помощью ключей API, вы можете
сделать токены OAuth (клавиши бота) с помощью метода
Keymaker.make\_a\_key ().

(Производные классы Keymaker обычно переопределяют или заменяют этот
метод, например, с помощью метода make\_keys ().)

Если мы хотим проверить Keymaker и создать ключи для одного бота, мы
можем указать имя бота и имя файла JSON, чтобы сбрасывать его (и
управлять именем каталога ключей ботов):

    import rainbowmindmachine as rmm
    
    keymaker = rmm.Keymaker()
    keymaker.make_a_key( name = 'My Bot',
                         json = 'mybot.json',
                         keys_out_dir = 'bot_keys')

# связи

[кредит](credits.md)

[Apollo Space Junk Bot Flock](https://pages.charlesreid1.com/b-apollo)

[@ apollo11junk](https://twitter.com/apollo11junk)

[@ apollo12junk](https://twitter.com/apollo12junk)

[@ apollo13junk](https://twitter.com/apollo13junk)

[мастер бота](installing.md)

[Пасти](shepherd.md)
