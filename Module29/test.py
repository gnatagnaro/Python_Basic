# Задача 1. Createtime
#
# Реализуйте декоратор класса, который выдаёт дату и время создания, а также список всех методов объекта класса каждый раз,
# когда объект класса создаётся в основном коде.
#
#
#
import datetime


def decorator(cls):
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)

        print("Время создания -", datetime.datetime.now())
        print("Методы:", end=" ")
        for i_method in dir(cls):
            if i_method.startswith('__'):
                continue
            print(i_method, end=' ')
        print()
        return instance

    return wrapper


@decorator
class Example:

    def hello(self):
        print("hello")

    def hello_2(self):
        print("hello")


Example()
Example()


# Задача 2. Декорацию знаешь?
#
# На новой работе вы познакомились с middle-разработчиком на Python, который согласился научить вас всему, что умеет сам.
# Но перед этим он решил точечно проверить ваши знания. Он показал код, где один и тот же
# декоратор логирования использовался для каждого метода класса отдельно:
#
#
#
# Зная, что классы тоже можно декорировать, вы сразу поняли, как можно упростить код.
#
# Реализуйте декоратор logging, который должен декорировать класс и логировать каждый метод в нём.
# Логирование реализуйте на своё усмотрение:
#
# это может быть, например, вывод названия метода, его аргов, кваргов и документации на экран;
# либо вывод всей этой информации в отдельный файл вместе с датой и временем.


def logged(func):
    def wrapped(*args, **kwargs):
        print("Запуск функции произошёл в:", datetime.datetime.now())
        return func(*args, **kwargs)

    return wrapped


def decorator(cls):
    for i_method in dir(cls):
        if i_method.startswith('__'):
            continue
        a = getattr(cls, i_method)
        if hasattr(a, '__call__'):
            decorated_a = logged(a)
            setattr(cls, i_method, decorated_a)
    return cls


@decorator
class A:

    def test_sum_1(self) -> int:
        print('Тут метод test_sum_1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


A().test_sum_1()


import datetime
import functools
import time


def create_time(cls):
    @functools.wraps(cls)
    def wrapped(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print(datetime.datetime.utcnow())
        return instance
    return wrapped


def timer(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return end - start
    return wrapped


def for_all_methods(decorator):
    @functools.wraps(decorator)
    def decorate(cls):
        for i_name in dir(cls):
            if not i_name.startswith('__'):
                cur_method = getattr(cls, i_name)
                decorated_method = decorator(cur_method)
                setattr(cls, i_name, decorated_method)
        return cls
    return decorate


@create_time
@for_all_methods(timer)
class MyClass:
    def __init__(self, x):
        self.x = x

    @classmethod
    def first(cls):
        print('1st')

    @classmethod
    def second(cls):
        print('second')

    def sq_sum(self):
        return self.x


f1 = MyClass(132)
print(f1.sq_sum())
f2 = MyClass(132)
f3 = MyClass(132)
# Задача 1. Повторение кода
#
# В одной из практик вы уже писали декоратор do_twice, который повторяет вызов декорируемой функции два раза.
# В этот раз реализуйте декоратор repeat, который повторяет задекорированную функцию уже n раз.
#
#
#


def do_nice(n):
    def wrap_fun(func):
        """декоратор do_twice, который дважды вызывает декорируемую функцию"""
        def wrapped_func(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
            return

        return wrapped_func

    return wrap_fun


@do_nice(5)
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))


greeting("hello")

# Задача 2. Замедление кода 2
#
# Продолжаем работать с нашим старым кодом. Ранее мы уже писали декоратор,
# который перед выполнением декорируемой функции ждёт несколько секунд.
#
# Модернизируйте этот декоратор так, чтобы количество секунд можно было передавать в качестве аргумента.
# По умолчанию декоратор ждёт одну секунду. Помимо этого сделайте так, чтобы декоратор можно было использовать
# как с аргументами, так и без них.

from time import sleep


def slow_it_now(_func=None, *, n=1):
    def slowdown_ns(func):
        def wrapper(*args, **kwargs):
            sleep(n)
            result = func(*args, **kwargs)
            return result

        return wrapper

    if _func is None:
        return slowdown_ns
    else:
        return slowdown_ns(_func)


@slow_it_now
def test() -> None:
    """
    Проверка декоратора и вывод прстого сообщения

    :return:
    """
    print('<Тут что-то происходит...>')


test()



from typing import Callable, Any, Optional
import time
import functools


def deco(_func: Optional[Callable] = None, *, n: int = 1):
    def wait_deco(func: Callable) -> Callable:
        """Декоратор, ожидающий несколько секунд перед выполнением декорируемой функции."""
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Any:
            start = time.time()
            time.sleep(n)
            end = time.time()
            print(f'программа ждет {n} секунд: {end - start}')
            return func(*args, **kwargs)
        return wrapped_func
    if _func is None:
        return wait_deco
    else:
        print(211221211221212121)
        return wait_deco(_func)


@deco(n=5)
def my_func() -> None:
    """Функция для теста."""
    print('smthing')


my_func()


from typing import Callable, Any


def deco(n):
    def repeat(func):
        @functools.wraps(func)
        def wrapped_repeat(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
            return
        return wrapped_repeat
    return repeat


@deco(5)
def my_func(name):
    print(f'hello, {name}')


my_func(213)


def do_twice(func: Callable) -> Callable:
    """Декоратор do_twice, который дважды вызывает декорируемую функцию"""
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        return func(*args, **kwargs)

    return wrapped_func


@do_twice
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))


greeting("!")


# Задача 1. Таймер
#
# Реализуйте функцию (не класс) timer в качестве контекст-менеджера:
# функция должна работать с оператором with и замерять время работы вложенного кода.
#
#
#

from contextlib import contextmanager
import time


@contextmanager
def timer():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(end - start)


# Задача 2. Директории
#
# Реализуйте функцию in_dir, которая принимает в качестве аргумента путь и временно меняет текущую рабочую директорию на новую.
# Функция должна быть контекст-менеджером. Также реализуйте обработку ошибок (например, если такого пути не существует).
# Вне зависимости от результата выполнения контекст-менеджера нужно возвращаться в изначальную рабочую директорию.
#
#
#
# Пример основного кода:
#
# with in_dir('C:\\'):
#
#     print(os.listdir())
#
# Результат:
#
# <тут все папки из вашего диска C>
import os


@contextmanager
def in_dir(path):
    print('start')
    cur_path = os.getcwd()
    os.chdir(path)
    try:
        yield
    except Exception as exc:
        print(exc)
    finally:
        os.chdir(cur_path)
    print('exit')


with in_dir('C:\\Skillbox\\'):
    print(os.listdir())

