# Задача 1. Однострочный код
#
# Пользователь вводит неопределённое количество чисел. Напишите код, который запрашивает эти числа и сортирует их по возрастанию.
# Реализуйте решение в одну строку.
#
#
#
# Пример работы консоли:
#
# Введите числа: 5 8 4 1 0 3
#
# [0, 1, 3, 4, 5, 8]
#
#
#

numbers = input("Введите числа: ")
print(sorted(list(map(int, numbers.split()))))

# Задача 2. Однострочный код 2
#
# Пользователь вводит строку, состоящую из любых символов. Напишите код, который выводит на экран список этих символов,
# исключая цифры и буквы в верхнем регистре.
#
#
#
# Пример работы консоли:
#
# Введите строку: qWe456rtY
#
# ['q', 'e', 'r', 't']
#
#
#

text = input("Введите строку: ")

print(list(filter(lambda x: not (x.isupper() or x.isdigit()), text)))

# Задача 3. Функция reduce
#
# Помимо map и filter, есть ещё одна функция — reduce. Она применяет указанную функцию к элементам последовательности,
# сводя её к единственному значению. Однако используют reduce довольно редко. Начиная с третьей версии Python,
# эту функцию даже вынесли из встроенных функций в модуль functools.
#
#
#
# Пример кода с reduce:

from functools import reduce
from typing import List


def my_add(a: int, b: int) -> int:
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


numbers: List[int] = [0, 1, 2, 3, 4]
print(reduce(my_add, numbers))
#
#
#
# Результат:
#
# 0 + 1 = 1
#
# 1 + 2 = 3
#
# 3 + 3 = 6
#
# 6 + 4 = 10
#
# 10
#
#
#
# Используя функцию reduce, реализуйте код, который считает, сколько раз слово was встречается в списке:
#
#
#
sentences = ["Nory was a Catholic", "because her mother was a Catholic",
             "and Nory’s mother was a Catholic", "because her father was a Catholic",
             "and her father was a Catholic", "because his mother was a Catholic", "or had been"]


def check_was(a, b):
    if isinstance(a, str):  # обработаем первый элемент отдельно
        a = int(a.count('was'))
    print(a, '************', b)
    result = a + int(b.count('was'))
    return result  # т.к. мы возвращаем int - то дальше 'a' всегда будет int-ом, а в 'b' будет новая строка


print(reduce(check_was, sentences))


# Задача 1. Минимум и максимум
#
# Мы знаем, что для нахождения минимального и максимального значений в наборе данных можно использовать две встроенные функции:
# min() и max(). И у них тоже можно использовать именованный аргумент key.
#
#
#
# Скажем, дан вот такой список, в котором хранятся результаты соревнований в виде словарей:
#
#
#
# grades: Dict[str, Union[str, int]] = [{'name': 'Kenneth', 'score': 3}, {'name': 'Bebe', 'score': 41},
# {'name': 'Joyce', 'score': 24}, {'name': 'Richard', 'score': 37}, {'name': 'Marian', 'score': 44}, {'name': 'Jana', 'score': 45},
#
# {'name': 'Sarah', 'score': 90}, {'name': 'Eddie', 'score': 2}, {'name': 'Mary', 'score': 63},
#
# {'name': 'Ronald', 'score': 15}, {'name': 'David', 'score': 44}, {'name': 'Richard', 'score': 78},
#
# {'name': 'Warren', 'score': 7}, {'name': 'Alyssa', 'score': 13}, {'name': 'Lloyd', 'score': 52},
#
# {'name': 'Vanessa', 'score': 6}, {'name': 'Karen', 'score': 40}, {'name': 'James', 'score': 54},
#
# {'name': 'Annie', 'score': 87}, {'name': 'Glenn', 'score': 9}, {'name': 'Bruce', 'score': 68},
#
# {'name': 'Ramona', 'score': 64}, {'name': 'Jeannie', 'score': 22}, {'name': 'Aaron', 'score': 3},
#
# {'name': 'Ronnie', 'score': 47}, {'name': 'William', 'score': 94}, {'name': 'Sandra', 'score': 40},
#
# ]
#
#
#
# Напишите код, который выводит на экран минимальное и максимальное количество очков из этого списка.
# Используйте только встроенные функции и лямбда-функции, то есть реализуйте решение «в две строки».
#
#
#

grades = [
    {'name': 'Kenneth', 'score': 3}, {'name': 'Bebe', 'score': 41}, {'name': 'Joyce', 'score': 24},
    {'name': 'Richard', 'score': 37}, {'name': 'Marian', 'score': 44}, {'name': 'Jana', 'score': 45},
    {'name': 'Sarah', 'score': 90}, {'name': 'Eddie', 'score': 2}, {'name': 'Mary', 'score': 63},
    {'name': 'Ronald', 'score': 15}, {'name': 'David', 'score': 44}, {'name': 'Richard', 'score': 78},
    {'name': 'Warren', 'score': 7}, {'name': 'Alyssa', 'score': 13}, {'name': 'Lloyd', 'score': 52},
    {'name': 'Vanessa', 'score': 6}, {'name': 'Karen', 'score': 40}, {'name': 'James', 'score': 54},
    {'name': 'Annie', 'score': 87}, {'name': 'Glenn', 'score': 9}, {'name': 'Bruce', 'score': 68},
    {'name': 'Ramona', 'score': 64}, {'name': 'Jeannie', 'score': 22}, {'name': 'Aaron', 'score': 3},
    {'name': 'Ronnie', 'score': 47}, {'name': 'William', 'score': 94}, {'name': 'Sandra', 'score': 40},
]
# Решение через key
print(max(grades, key=lambda x: x["score"]))
print(min(grades, key=lambda x: x["score"]))
# Вывод исключительно очков:
print(max(grades, key=lambda x: x["score"])['score'])
print(min(grades, key=lambda x: x["score"])['score'])

# Решение через map, который будет изучен в следующем модуле
print(list(map(lambda x: x['score'], grades)))  # для наглядности
print(max(map(lambda x: x['score'], grades)))
print(min(map(lambda x: x['score'], grades)))
print(grades)

# Задача 2. Сортировка
#
# Таблица базы данных состоит из строк, в которых хранится информация о каждом человеке: его имя, возраст и остальные данные.
# Вас попросили реализовать для этой базы сортировку по возрасту (по убыванию и по возрастанию).
#
# Реализуйте класс Person с соответствующей инициализацией, а также сеттерами и геттерами.
# Затем создайте список из хотя бы трёх людей и отсортируйте их. Для сортировки используйте лямбда-функцию.

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @name.setter
    def name(self, word):
        self._name = word

    def __repr__(self):
        return f"({self.name}, {self.age})"


first = Person("Max", 29)
second = Person("Christine", 21)
third = Person("Anthony", 35)
humans = [first, second, third]
print(humans)
humans.sort(key=lambda x: x.age)
print(humans)
humans.sort(key=lambda x: x.age, reverse=True)
print(humans)
humans.sort(key=lambda x: x.age)
print(humans)
humans.sort(key=lambda x: -x.age)
print(humans)

my_list = [Person('Name', 10), Person('Name', 1), Person('Name', 3)]
print(my_list)
my_list_sorted = sorted(my_list, key=lambda x: x.age)
print(my_list_sorted)

# Задача 1. Счётчик 2
#
# Как-то мы уже создавали декоратор counter, который считает и выводит количество вызовов декорируемой функции.
# Для этого мы использовали интересную особенность классов. В этот раз реализуйте тот же декоратор,
# но уже с использованием знаний о локальных и глобальных переменных.
#
# Реализуйте декоратор двумя способами:
#
# используя глобальную переменную count;
# используя локальную переменную count внутри декоратора.
#
#
# Дополнительно: найдите команду (в интернете или даже сами), которая перечисляет все функции и методы,
# находящиеся во встроенном пространстве имён в Python.
#
#
#
# Результат выполнения команды:
#
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__'  ну и так далее.

global_count = {}
count = 0


def decorator_counter(func):
    def wrapped_func(*args, **kwargs):
        global count
        count += 1
        wrapped_func.count += 1
        global_count[func.__name__] = global_count.get(func.__name__, 0) + 1
        return func(*args, **kwargs)

    wrapped_func.count = 0
    return wrapped_func


@decorator_counter
def hello():
    print('hello')


@decorator_counter
def hello_2():
    print('hello')


print(global_count, hello.count, hello_2.count)
hello()
print(global_count, hello.count, hello_2.count)
hello_2()
print(global_count, hello.count)
print(count)
print('*' * 100)
print(dir('.'))
print('*' * 100)
print(locals())
print('*' * 100)
print(globals())
