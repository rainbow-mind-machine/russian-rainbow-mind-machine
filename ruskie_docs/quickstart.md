# Быстрый старт

Давайте рассмотрим быстрый пример, чтобы проиллюстрировать, как это
работает.

Помните, у нас есть только 3 объекта, которые нам нужно понять:

  - The Keymaker (makes/manages keys and authenticates with Twitter)
  - The Shepherd (one shepherd = one bot flock, runs the flock)
  - The Sheep (one sheep = one bot, defines bot behavior)

# Keymaker: шаг аутентификации

Первым шагом в машине радужного разума является запуск Keymaker, чтобы
дать разрешение на использование твита от имени каждого из наших
бот-пользователей. Это генерирует ключи, которые приложение
радужной системы разума должно присутствовать в чириканье как
стая бота.

Keymaker принимает набор элементов и создает один ключ для каждого
элемента.

Набор элементов может представлять собой список Python с целыми числами
или папку с текстовыми файлами или набор URL-адресов или просто старые
ярлыки строк.

Ключи - это то, что позволяет нашему приложению чирикать, используя
ботовую учетную запись.

Мы вызываем make\_a\_key () для каждого элемента для создания каждого
ключа.

Keymaker требует, чтобы мы указали параметр имени, чтобы назвать бота и
параметр json, чтобы указать местоположение ключа.

Также обратите внимание: для этого требуется, чтобы ваш секретный и
потребительский токен вашего приложения Twitter был установлен в
apikeys.py.

В приведенном ниже примере «элементы» представляют собой строки,
содержащие имя бота. Это использует учетные данные в apikeys.py
и выводит ключевые файлы в keys / key1.json и keys / key2.json.

``` python
import rainbowmindmachine as rmm
import subprocess

subprocess.call(['mkdir','-p','keys/'])

k = rmm.Keymaker()

# Create some keys
k.make_key({
    'name':'Twitter Bot 1',     # This is the bot label
    'json':'keys/key1.json'     # This is the key file
})
k.make_key({
    'name':'Twitter Bot 2',
    'json':'keys/key2.json'
})
```

Когда этот скрипт запущен, Keymaker проведет ряд интерактивных шагов для
создания ключей от каждого элемента.

# Запуск Bot Flock

Как только это будет сделано, сделайте Пастуха для бот-паства и укажите
его клавишам, созданным в каталоге keys / keymaker:

``` python
import rainbowmindmachine as rmm

# make the Shepherd
sh = rmm.Shepherd("keys/")

# Change everybody's Twitter page color
sh.perform_action('change color','#CFC')

# Everybody tweet in parallel
sh.perform_pool_action('tweet')
```

Теперь вы можете запустить это на экране или в фоновом режиме, и он
будет последовательно менять цвет страницы каждой страницы бота, а
затем будет прокручивать один поток на одну овцу.

# Настройка овец

Мы не указали, какую овцу мы хотим, чтобы Пастух создал, поэтому Пастух
использует класс Овца по умолчанию.

Чтобы изменить поведение вашего бота, вы можете использовать встроенные
типы овцы (PhotoADaySheep, PoemSheep, QueneauSheep и т. Д.) Или вы
можете расширить класс Sheep для определения пользовательского
поведения.

Например, чтобы определить новое поведение populate\_queue ():

``` python
import rmm 

class CustomSheep(rmm.Sheep):
    def populate_queue(self,items):
        ...
```

Затем измените Пастуха, чтобы использовать этот новый класс овцы:

``` python
# make the Shepherd
sh = rmm.Shepherd("keys/", sheep_class=CustomSheep)

# Change everybody's Twitter page color
sh.perform_action('change color','#CFC')

# Everybody tweet in parallel
sh.perform_pool_action('tweet')
```

# Другие примеры

# Пример: Ginsberg Bot Flock

Бот-стайка Гинсберга - простой пример стаи, на которой работает
несколько PoemSheep, причем каждая овчарка загружает
стихотворение из текстового файла и чирикает стихотворение по
одной строке за раз.

См. Example\_flocks / ginsberg\_botflock и b-ginsberg на
git.charlesreid1.com.

# Пример: Apollo Space Junk Bot Flock

Apollo Space Junk Bot Flock использует генерацию queneau для создания
фальшивой радиопередачи космической миссии Apollo. Эта бот-стая
запускает несколько QueneauSheep.

См. Example\_flocks / apollo\_botflock и b-apollo на
git.charlesreid1.com.

# Пример: Mathematics Tripos Bot

Бот Math Tripos - это, в основном, стая с одним ботём фото в день. Он
демонстрирует, как создать ботовую стаю с одним ботом.

У бота Math Tripos есть каталог, полный 366 вопросов из Математического
Триполи Кембриджского университета, в формате LaTeX. Каждое уравнение
LaTeX преобразуется в png. Каждый бот задает новый вопрос.

Смотрите b-tripos на git.charlesreid1.com.

# связи

[example\_flocks /
ginsberg\_botflock](/example_flocks/ginsberg_botflock/)

[b-ginsberg на
git.charlesreid1.com](https://git.charlesreid1.com/bots/b-ginsberg)

[example\_flocks / apollo\_botflock](/example_flocks/apollo_botflock/)

[b-apollo на
git.charlesreid1.com](https://git.charlesreid1.com/bots/b-apollo)

[b-tripos на
git.charlesreid1.com](https://git.charlesreid1.com/bots/b-tripos)
