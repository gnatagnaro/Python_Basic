# Задача 1. Сэндвич
#
# Есть функция, которая выводит начинку сэндвича. Сверху и снизу от начинки идут различные ингредиенты вроде салата, помидоров и других.
# Всё это в свою очередь содержится между двух половинок булочки.
# Реализуйте такую функцию и два соответствующих декоратора — ингредиенты и хлеб.
#
# Пример результата работы программы при вызове функции sandwich:
#
# </----------\>
# #помидоры#
# --ветчина--
# ~салат~
# <\______/>
#
#
#

def get_some_salad(func):
    def wrap_that_salad(*args, **kwargs):
        print("#помидоры#")
        func(*args, **kwargs)
        print("~салат~")

    return wrap_that_salad


def get_some_buns(func):
    def wrap_that_buns(*args, **kwargs):
        print("</----------\>")
        func(*args, **kwargs)
        print("<\______/>")

    return wrap_that_buns


@get_some_buns
@get_some_salad
def filling_burger(filler):
    print(filler)


filling_burger("ветчина")

# Задача 2. Плагины
#
# Один проект состоит из огромного количества разнообразных функций, часть из которых используется в других проектах в качестве плагинов,
# то есть они как бы «подключаются» и создают дополнительный функционал.
#
# Реализуйте специальный декоратор, который будет «регистрировать» нужные функции как плагины и заносить их в соответствующий словарь.
from typing import Dict, Callable


plugins: Dict = dict()


def go_to_plugins(func: Callable) -> Callable:
    plugins[func.__name__] = func
    return func


@go_to_plugins
def hello() -> None:
    print('Hello!')


print(plugins)


# Задача 1. Двойной вызов
#
# Реализуйте декоратор do_twice, который дважды вызывает декорируемую функцию. Не забывайте про документацию и аннотации типов.
#
#
#
# Пример декорируемой функции:
#
# def greeting(name):
#
#     print('Привет, {name}!'.format(name=name))
#
#
#
# Основной код:
#
# greeting('Tom')
#
#
#
# Результат:
#
# Привет, Tom!
#
# Привет, Tom!
#
#
#

from typing import Callable, Any, List


def do_twice(func: Callable) -> Callable:
    """декоратор do_twice, который дважды вызывает декорируемую функцию"""

    def wrapped_func(*args, **kwargs) -> Any:
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapped_func


@do_twice
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))


greeting("!")


# Задача 2. Таймер 2
#
# Для замера времени передачи различных данных на множество сайтов вы написали специальную функцию, которая сделала всю работу за вас,
# что позволило большую часть времени смотреть видео с котиками в интернете. Однако, увидев свой код, вы как программист с опытом поняли,
# что этот код можно написать намного красивее и удобнее.
#
# Реализуйте декоратор, который замеряет время работы задекорированной функции и выводит ответ на экран.
# Для проверки примените декоратор к какой-нибудь «тяжеловесной» функции и вызовите её в основной программе.
import time


def time_track(func: Callable) -> Callable:
    def surrogate(*args, **kwargs) -> Any:
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result

    return surrogate


@time_track
def hard_func() -> List:
    return [x ** 2 ** x for x in range(22)]


hard_func()


# Задача 1. Функции
#
# Дана функция func_1, которая принимает число и возвращает результат его сложения с числом 10:
#
#
#
# def func_1(x):
#
#     return x + 10
#
#
#
# Реализуйте функцию высшего порядка func_2, которая будет возвращать перемножение двух результатов переданной функции.
#
# Пример основного кода:
#
# print(func_2(func_1, 9))
#
#
#
# Результат: 361.
#
#
#

def func_1(x):
    return x + 10


def func_2(func, number):
    return func(number) * func(number)


print(func_2(func_1, 9))

# Задача 2. Таймер
#
# Вы работаете в отделе тестирования, и вам поручили с помощью различных функций замерить
# скорость передачи данных на нескольких десятках сайтов. Конечно же, вручную «щёлкать» сайты и замерять время вам было лень,
# поэтому возникла идея написать «автотест», который всё сделает сам.
#
# С помощью понятия функции высшего порядка реализуйте функцию-таймер,
# которая замеряет время работы переданной функции func и выдаёт ответ на экран.
#
# Проверьте работу таймера на какой-нибудь «тяжеловесной» функции.

# import time
#
#
# def timer(func):
#     start = time.time()
#     func()
#     end = time.time()
#     return end - start
#
#
# def hard_func():
#     return [x ** 2 ** x for x in range(22)]
#
#
# print(timer(hard_func))
