import re
import requests
import json

if __name__ == '__main__':
    # Задача 1. Звёздные войны
    #
    # Повторите пример парсинга, разобранный в видео: перейдите на сайт с API, посвящённый вселенной Star Wars.
    #
    # После этого сгенерируйте реквест-ссылку на данные о человеке под номером 3 (people/3/).
    #
    # Затем напишите программу, которая парсит данные об этом человеке,
    # изменяет его имя на ваше собственное и сохраняет результат в виде JSON-файла.
    #
    #
    #
    # Дополнительно: обратите внимание на значение ключа homeworld — там также хранится ссылка.
    # В том же коде спарсите эту ссылку и посмотрите, что там.
    #
    #
    #
    # Примечание: API тоже пишут люди, а значит, время от времени его могут как-то менять и усовершенствовать,
    # поэтому будьте внимательны: может быть, ссылка уже хранится в другом ключе.
    #
    #
    #

    result = requests.get("https://swapi.dev/api/people/3/")
    if result.status_code == 200:
        json_dict = json.loads(result.text)
        json_dict['name'] = input("Введите имя: ")
        with open("swap.json", "w") as file:
            json_text = json.dump(json_dict, file, indent=4)

        # Доп:
        result_homeworld = requests.get(json_dict['homeworld'])
        print(result_homeworld.text)

    # Задача 2. Документация API
    #
    # Обычно к открытым API прилагается подробная документация,
    # где описывается логика формирования ссылок и какие данные по ним можно получать (или отправлять!).
    #
    #
    #
    # Изучите документацию того же сайта по «Звёздным войнам».
    #
    #
    #
    # Поэкспериментируйте с получением данных о кораблях, планетах, фильмах и так далее.
    # А ещё попробуйте библиотеку swapi (о ней также в документации)
    # и с её помощью выведите начало сюжета из фильма «Новая надежда» (A New Hope).


    # print(swapi.get_film(1))
    # Сейчас библиотека не работает, получить начало сюжета можно напрямую

    result = requests.get("https://swapi.dev/api/films/1/")

    json_dict = json.loads(result.text)

    print(json_dict["opening_crawl"])

    # json.load(), json.loads() - десериализация файлов json, чтобы работать с ними, как с dict, load - для правильного чтения файлов json
    # json.dump(), json.dumps() - сериализация файлов json, преобразуют dict (словарь) в формат json, dump - для записи json-файлов

    my_req = requests.get('https://swapi.dev/api/people/1/')  # парсинг
    data = json.loads(my_req.text)  # десериализация json
    data['name'] = '123'
    print(data)

    with open('test.json', 'w') as f:
        json.dump(data, f, indent=4)  # сериализация json

    with open('test.json', 'r') as f:
        json.load(f)

    req = requests.get('https://swapi.dev/api/people/2/')
    data = json.loads(req.text)
    with open('test.json', 'w') as f:
        json.dump(data, f, indent=4)

    req = requests.get("https://swapi.dev/api/planets/1/")
    dt = json.loads(req.text)
    print(dt)

    req = requests.get('https://swapi.dev/api/films/')
    print(req.text)
    # Задача 1. Согласные
    #
    # Дан следующий текст:
    #
    #
    #
    # Even if they are djinns, I will get djinns that can outdjinn them.
    #
    #
    #
    # Используя регулярные выражения, напишите программу, которая выводит два списка:
    #
    # Первый содержит все слова, которые начинаются на гласную букву латинского алфавита
    # (в этот раз слово может состоять и из одной буквы, например I).
    # Второй содержит слова, которые начинаются на любой символ, кроме гласных букв латинского алфавита.
    # Для получения второго списка за основу используйте шаблон, которым вы получили первый список.
    #
    # Ещё небольшая подсказка: посмотрите, чем отличается символ * от символа +. Также, когда будете получать второй список,
    # обратите внимание, на какой символ начинаются слова.
    #
    #
    #
    # Ожидаемый результат:
    #
    # Слова на гласную: ['Even', 'if', 'are', 'I', 'outdjinn']
    #
    # Слова на любой символ, кроме гласной: ['they', 'djinns', 'will', 'get', 'djinns', 'that', 'can', 'them']
    #
    #

    text = "Even if they are djinns, I will get djinns that can outdjinn them."
    result_1 = re.findall(r"\b[aAeEiIoOuUyY]\w*", text)
    print("Слова на гласную:", result_1)
    result_2 = re.findall(r"\b[^aAeEiIoOuUyY\W]\w*", text)
    print("Слова на любой символ, кроме гласной:", result_2)
    #
    # Задача 2. Даты
    #
    # Из одного дата-центра пришёл текстовый пакет данных, который содержит информацию о кодовом названии оборудования,
    # его серийном номере и дате начала эксплуатации. Вот небольшой кусочек из этого пакета в виде строки:
    #
    #
    #
    # Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009
    #
    #
    #
    # Используя регулярные выражения, напишите программу, получающую список всех дат, которые встречаются в строке.
    #
    #
    #
    # Для этого необходимо использовать \d.
    #
    #
    #
    # Ожидаемый результат:
    #
    # ['12-05-2007', '11-11-2011', '12-01-2009']

    text = "Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009"

    result = re.findall(r"\d{2}-\d{2}-\d{4}", text)

    print(result)

    text = 'Even if they are djinns, I will get djinns that can outdjinn them.'
    pattern = re.compile(r'\b[aeiouyAEIOUY]\w*')
    print(pattern.findall(text))
    pattern = re.compile(r'\b[^aeiouyAEIOUY ]\w+')
    print(pattern.findall(text))

    text = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
    pattern = re.compile(r'\d{0,2}-\d{0,2}-\d{0,4}')
    print(pattern.findall(text))

    # Задача 1. Скороговорка
    #
    # Дан текст вот такой английской скороговорки:
    #
    #
    #
    # How much wood would a woodchuck chuck if a woodchuck could chuck wood?
    #
    #
    #
    # С помощью модуля re реализуйте программу, которая выполняет следующие действия по порядку:
    #
    # Определить, начинается ли текст с шаблона wo.
    # Найти первое упоминание шаблона wo в тексте.
    # Определить содержимое найденной по шаблону подстроки из пункта 2.
    # Найти позицию, с которого начинается первое упоминание шаблона wo.
    # Найти позицию, на которой заканчивается первое упоминание шаблона wo.
    # Получить список из каждого упоминания шаблона wo в тексте.
    # Заменить в тексте все совпадения по шаблону wo на слово «ЗАМЕНА».
    # По каждому действию вывести соответствующий результат. Не используйте методы строк. Не забывайте использовать приписку r в шаблонах.
    #
    #
    #
    # Ожидаемый результат работы программы:
    #
    #
    #
    # Поиск шаблона в начале строки: None
    #
    # Поиск первого найденного совпадения по шаблону: <re.Match object; span=(9, 11), match='wo'>
    #
    # Содержимое найденной подстроки: wo
    #
    # Начальная позиция: 9
    #
    # Конечная позиция: 11
    #
    # Список всех упоминаний шаблона: ['wo', 'wo', 'wo', 'wo', 'wo']
    #
    # Текст после замены: How much ЗАМЕНАod ЗАМЕНАuld a ЗАМЕНАodchuck chuck if a ЗАМЕНАodchuck could chuck ЗАМЕНАod?
    #
    #
    #

    text = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"

    words = text.split()

    result = re.search("wo", words[0])
    print("Поиск шаблона в начале строки: ", result)

    result = re.search("wo", text)
    print("Поиск первого найденного совпадения по шаблону: ", result)

    result = re.search("wo", text)
    print("Содержимое найденной подстроки: ", result.group(0))

    print("Начальная позиция:", result.start())
    print("Конечная позиция:", result.end())

    result = re.findall("wo", text)
    print("Список всех упоминаний шаблона:", result)

    result = re.sub("wo", "ЗАМЕНА", text)
    print("Текст после замены:", result)

    # Задача 2. Экранирование спецсимволов
    #
    # В видео при написании шаблона мы брали только обычные строки, без всяких специальных знаков.
    # Часть из этих спецсимволов является неотъемлемой частью регулярных выражений (о чём мы поговорим уже в следующем видео),
    # они даже выделяются своими цветами при написании паттернов. Например:
    #
    #
    #
    #
    #
    # Поэтому если мы хотим найти в тексте спецсимвол, а не использовать его как часть паттерна,
    # то нужно его дополнительно экранировать — добавить обратный слеш перед этим знаком.
    # Например, если нам нужно будет найти шаблон wd+?. в виде полноценного текста, то это будет выглядеть так:
    #
    #
    #
    #
    #
    # А теперь сама задача. Дан немного изменённый текст скороговорки:
    #
    #
    #
    # How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?,
    #
    #
    #
    # Напишите программу, которая выводит список из всех упоминаний подстроки \wwood+?,
    #
    #
    #
    # Ожидаемый результат:
    #
    #
    #
    # Список всех упоминаний шаблона: ['\\wwood+?,', '\\wwood+?,']
    text = "How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?,"

    result = re.findall(r"\\wwood\+\?,", text)
    print("Список всех упоминаний шаблона:", result)
    print('*' * 100)
    text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
    pattern = re.compile(r'wo')
    print(f"Поиск шаблона в начале строки: {pattern.match(text)}")
    print(f"Поиск первого найденного совпадения по шаблону: {pattern.search(text)}")
    print(f"Определить содержимое найденной по шаблону подстроки: {pattern.search(text).group(0)}")
    print(f"Найти позицию, с которого начинается первое упоминание шаблона wo: {pattern.search(text).start()}")
    print(f"Найти позицию, на которой заканчивается первое упоминание шаблона wo: {pattern.search(text).end()}")
    print(f"Получить список из каждого упоминания шаблона wo в тексте: {pattern.findall(text)}")
    print(f"Заменить в тексте все совпадения по шаблону wo на слово «ЗАМЕНА»: {pattern.sub('ЗАМЕНА', text)}")
    print('*' * 100)
    text = 'How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?,'
    pattern = re.compile(r'\\wwood\+\?,')
    print(pattern)
    print(pattern.findall(text))
    print('*' * 100)
