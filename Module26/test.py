# Задача 1. Бесконечный генератор
#
# По аналогии с бесконечным итератором из практики предыдущего урока, реализуйте свой счётчик-генератор,
# который также в цикле будет бесконечно выдавать значения.
#
# Дополнительно: преобразуйте (или напишите с нуля) итератор простых чисел в функцию-генератор.
#
#
#

def counter():
    n = 0
    while True:
        n += 1
        yield n


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


for i in get_prime_numbers(50):
    print(i, end='\t')
print()

# Задача 2. Очень большой файл
#
# Вам на обработку пришёл огромнейший файл с данными. Настолько огромный, что при его открытии компьютер просто зависает,
# так как данные не помещаются в оперативной памяти вашего суперкомпьютера (не очень-то и «супер»).
#
# В файле numbers.txt есть N чисел, разделённых пробелами и литералом пропуска строки. Напишите программу,
# которая подсчитает общую сумму чисел в файле. Для считывания файла реализуйте специальный генератор.

def numbers_from_text(text):
    return [int(number) for number in text.rstrip().split()]


def file_parser(path_to_file):
    with open(path_to_file) as file:
        for line in file:
            clear_line_sum = sum(numbers_from_text(line))
            # https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-map/
            yield clear_line_sum


all_sum = 0
for number in file_parser("numbers.txt"):
    all_sum += number

print("Вариант №1", all_sum)


# Ещё один вариант решения с функцией map()
def file_parser(path_to_file):
    with open(path_to_file) as file:
        for line in file:
            clear_line_sum = sum(map(int, line.rstrip().split()))
            # https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-map/
            yield clear_line_sum


all_sum = 0
for number in file_parser("numbers.txt"):
    all_sum += number

print("Вариант №2", all_sum)


def numbers_generator(filename):
    with open(filename, 'r') as f:
        for line in f:
            for number in line.split():
                yield int(number)


filename = 'numbers.txt'
total_sum = 0

for number in numbers_generator(filename):
    total_sum += number

print(f'Total sum: {total_sum}')

# # Задача 1. Бесконечный итератор
# #
# # Реализуйте итератор-счётчик, который не принимает никаких атрибутов и имеет только один статический атрибут — счётчик.
# # Итератор увеличивает счётчик и возвращает предыдущее значение. У вас должен получиться бесконечный итератор.
# #
# # То есть при вызове такого кода в основной программе
# #
# # my_iter = СountIterator()
# #
# # for i_elem in my_iter:
# #
# #     print(i_elem)
# #
# # значения будут выдаваться бесконечно.
# #
# #
# #
# import random
#
#
# class CountIterator:
#     count = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         CountIterator.count += 1
#         return CountIterator.count
#
#
# my_iter = CountIterator()
#
#
# # for i_elem in my_iter:
# #     print(i_elem)
#
#
# # Задача 2. Случайная сумма
# #
# # Алексею по работе необходимо обрабатывать огромные массивы данных из миллионов элементов.
# # Каждый новый элемент — это сумма случайного вещественного числа от 0 до 1 и предыдущего элемента (первый элемент —
# # просто случайное вещественное число от 0 до 1). Алексею нельзя хранить в памяти весь этот список, а со значениями работать как-то надо.
# #
# # Помогите Алексею, реализуйте такой класс-итератор и проверьте его работу.
# # Также сделайте, чтобы при каждом новом вызове итератора в цикле значения считались заново.
# #
# # Пример работы программы:
# #
# # Кол-во элементов: 5
# #
# # Элементы итератора:
# #
# # 0.74
# #
# # 1.13
# #
# # 1.95
# #
# # 2.2
# #
# # 2.55
# #
# # Новое кол-во элементов: 6
# #
# # Элементы итератора:
# #
# # 0.79
# #
# # 1.58
# #
# # 2.55
# #
# # 2.81
# #
# # 3.06
# #
# # 3.34
# #
# #
# #
#
# class SumsOfLastTwo:
#
#     def __init__(self, count):
#         self.last = 0
#         self.end = count
#         self.start = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start += 1
#         if self.start > self.end:
#             raise StopIteration
#         self.last += random.random()
#         return self.last
#
#
# counter = SumsOfLastTwo(5)
# for i in counter:
#     print(i)
#
#
# # Задача 3. Простые числа
# #
# # Реализуйте класс-итератор Primes, который принимает максимальное число N и выдаёт все простые числа от 1 до N.
# #
# # Основной код:
# #
# # prime_nums = Primes(50)
# #
# # for i_elem in prime_nums:
# #
# #     print(i_elem, end=' ')
# #
# # Ожидаемый результат кода:
# #
# # 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
#
# class Primes:
#
#     def __init__(self, n):
#         self.n = n
#         self.i = 1
#         self.prime_number = []
#
#     def __iter__(self):
#         self.i = 1
#         return self
#
#     def __next__(self):
#         while self.i <= self.n:
#             self.i += 1
#             for prime in self.prime_number:
#                 if self.i % prime == 0:
#                     break
#             else:
#                 self.prime_number.append(self.i)
#                 return self.i
#         raise StopIteration
#
#
# prime_nums = Primes(50)
#
# for i_elem in prime_nums:
#     print(i_elem, end=' ')


# class Primes:
#     def __init__(self, n):
#         self.n = n
#         self.primes = [2]
#         self.current = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current >= len(self.primes):
#             candidate = self.primes[-1] + 1
#             while True:
#                 if candidate > self.n:
#                     raise StopIteration
#                 is_prime = True
#                 for prime in self.primes[1:]:
#                     if prime*prime > candidate:
#                         break
#                     if candidate % prime == 0:
#                         is_prime = False
#                         break
#                 if is_prime:
#                     break
#                 candidate += 1
#             self.primes.append(candidate)
#         self.current += 1
#         return self.primes[self.current - 1]
#
#
# prime_nums = Primes(50)
#
# for i_elem in prime_nums:
#     print(i_elem, end=' ')
#
# # class СountIterator:
# #     count = 0
# #
# #     def __iter__(self):
# #         return self
# #
# #     def __next__(self):
# #         СountIterator.count += 1
# #         print(f'{СountIterator.count} -- {self.count}')
# #         return СountIterator.count - 1
# #
# #
# # my_iter = СountIterator()
# # for i_elem in my_iter:
# #     print(i_elem)
#
#
# # import random
# # #
# # #
# # # def for_like_while(n):
# # #     x = iter(n)
# # #     while True:
# # #         try:
# # #             print(next(x))
# # #         except StopIteration:
# # #             print('конец')
# # #             break
# # #
# # # t = [1, 2, 3, 100, 6523]
# # # for_like_while(t)
# #
# #
# # # Задача 1. Свой for (ну почти)
# # #
# # # Дан любой итерируемый объект, например список из N чисел. Реализуйте функцию,
# # # которая эмулирует работу цикла for с помощью цикла while и проходит во всем элементам итерируемого объекта.
# # # Не забудьте про исключение «конца итерации».
# # import random
# #
# # n = int(input("Введите количество чисел: "))
# # numbers = [random.randint(-100, 100) for _ in range(n)]
# #
# # buffer_iter = iter(numbers)
# # # buffer_iter = numbers.__iter__()
# #
# # while True:
# #     try:
# #         # buffer_iter.__next__()
# #         print(next(buffer_iter))
# #     except StopIteration:
# #         print("Конец!")
# #         break
