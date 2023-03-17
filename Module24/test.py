# class Potato:
#     states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}
#
#     def __init__(self, index):
#         self.index = index
#         self.state = 0
#
#     def grow(self):
#         if self.state < 3:
#             self.state += 1
#         self.print_state()
#
#     def is_ripe(self):
#         if self.state == 3:
#             return True
#         return False
#
#     def print_state(self):
#         print(f'Картошка {self.index} сейчас {self.states[self.state]}')
#
#
# class Garden:
#
#     def __init__(self, count):
#         self.potatoes = [Potato(index) for index in range(1, count + 1)]
#
#     def grow_all(self):
#         print('Картошка прорастает')
#         for potato in self.potatoes:
#             potato.grow()
#
#     def are_all_ripe(self):
#         # if not all([potato.is_ripe() for potato in self.potatoes]):
#         #     print('Картошка еще не созрела')
#         # else:
#         #     print('Вся картошка созрела. Можно собирать')
#
#         for potato in self.potatoes:
#             if not potato.is_ripe():
#                 print('Картошка еще не созрела')
#                 break
#         else:
#             print('Вся картошка созрела. Можно собирать')
#
#
# my_garden = Garden(5)
# my_garden.are_all_ripe()
# for _ in range(3):
#     my_garden.grow_all()
#     my_garden.are_all_ripe()
# class Point:
#
#     count_points = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.count_points += 1
#
#     def print_info(self):
#         print('Count:', self.count_points, '\nx and y:', self.x, self.y)
#
#
# f = Point(1, 2)
# f1 = Point(2, 3)
# f1.print_info()

# from random import randint
#
#
# class Toyota:
#
#     def __init__(self, color, price, max_speed, current_speed):
#         self.color = color
#         self.price = price
#         self.max_speed = max_speed
#         self.current_speed = current_speed
#
#     def check_info(self):
#         print(self.color, self.price, self.max_speed, self.current_speed)
#
#     def change_speed(self, new_speed):
#         self.current_speed = new_speed
#
#
# car = Toyota('red', 1e6, 200, randint(1, 200))
# car.check_info()
# car.change_speed(100)
# car.check_info()


# # Задача 1. Машина 2
# #
# # Модернизируйте класс Toyota из прошлого видео. Атрибуты остаются такими же:
# #
# # цвет машины (например, красный),
# # цена (один миллион),
# # максимальная скорость (200),
# # текущая скорость (ноль).
# #
# #
# # Добавьте два метода класса:
# #
# # Отображение информации об объекте класса.
# # Метод, который позволяет устанавливать текущую скорость машины.
# # Проверьте работу этих методов.
# #
# #
# #
#
# class Toyota:
#     color = 'red'
#     price = 1e6
#     max_speed = 200
#     current_speed = 0
#
#     def check_info(self):
#         print(self.color, self.price, self.max_speed, self.current_speed)
#
#     def change_speed(self, new_speed):
#         self.current_speed = new_speed
#
#
# car = Toyota()
# car.check_info()
# car.change_speed(100)
# car.check_info()
# print(Toyota.current_speed)  # обратите внимание, что скорость внутри Класса осталась той же, её изменения не коснулись
#
#
# # Задача 2. Семья
# #
# # Реализуйте класс «Семья», который состоит из атрибутов «Имя»,
# # Деньги» и «Наличие дома» и объекты которого могут выполнять следующие действия:
# #
# # Отобразить информацию о себе.
# # Заработать денег (подаётся число, которое прибавляется к текущему значению денег).
# # Купить дом (подаётся стоимость дома и необязательный аргумент «Скидка»).
# # Вывести соответствующее сообщение об успешной/неуспешной покупке дома.
# # Создайте как минимум один экземпляр класса и проверьте работу методов.
# #
# #
# #
# # Пример работы программы (вывод информации, покупка дома, заработок, очередная покупка):
# #
# #
# #
# # Family name: Common family
# #
# # Family funds: 100000
# #
# # Having a house: False
# #
# #
# #
# # Try to buy a house
# #
# # Not enough money!
# #
# #
# #
# # Earned 800000 money! Current value: 900000
# #
# # Try to buy a house again
# #
# # House purchased! Current money: 0.0
# #
# #
# #
# # Family name: Common family
# #
# # Family funds: 0.0
# #
# # Having a house: True
# class Family:
#     name = ""
#     money = 0
#     house = False
#
#     def print_info(self):
#         print("Family name: " + self.name, "Family funds: " + str(self.money), "Having a house: " + str(self.house), sep='\n')
#
#     def get_money(self, count):
#         self.money += count
#         print(f"Earned {count} money! Current value: {self.money}")
#
#     def buy_a_house(self, price, discount=0):
#         house_price = (price - price * (discount / 100))
#         if self.money >= house_price:
#             self.money -= house_price
#             print(f"House purchased! Current money: {self.money}")
#             self.house = True
#         else:
#             print("Not enough money!")
#
#
# human = Family()
# human.name = "Common family"
# human.money = 100000
#
# human.print_info()
# house_price = 900000
# human.buy_a_house(house_price)
# human.get_money(house_price - human.money)
# human.buy_a_house(house_price)
# human.print_info()

# import random
#
#
# class Toyota:
#     color = 'red'
#     price = 1e6
#     max_speed = 200
#     current_speed = 0
#
#     # def __int__(self, color='red', price=1e6, max_speed=200, current_speed=0):
#     #     self.color = color
#     #     self.price = price
#     #     self.max_speed = max_speed
#     #     self.current_speed = current_speed
#
#     def print_info(self):
#         print(self.color, self.price, self.max_speed, self.current_speed)
#
#     def set_cur_speed(self, x):
#         self.current_speed = x
#
#
# first_car = Toyota()
# first_car.print_info()
# first_car.set_cur_speed(random.randint(0, 200))
# first_car.print_info()
# first_car.current_speed = 100
#

# Задача 1. Машина
#
# Напишите класс Toyota, состоящий из четырёх статических атрибутов:
#
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Создайте три экземпляра класса и каждому из них поменяйте значение текущей скорости на случайное число от нуля до 200.
#
#
#
# import random
#
#
# class Toyota:
#     color = 'red'
#     price = 1e6
#     max_speed = 200
#     current_speed = 0
#
#
# first_car = Toyota()
# first_car.current_speed = random.randint(0, 200)
# second_car = Toyota()
# second_car.current_speed = random.randint(0, 200)
# third_car = Toyota()
# third_car.current_speed = random.randint(0, 200)
#
# print(first_car.current_speed, second_car.current_speed, third_car.current_speed)
#

# Задача 2. Однотипные объекты
#
# В офис заказали небольшую партию из четырёх мониторов и трёх наушников. У монитора есть четыре характеристики:
# название производителя, матрица, разрешение и частота обновления экрана. Все четыре монитора отличаются только частотой.
#
# У наушников три характеристики: название производителя, чувствительность и наличие микрофона. Отличие только в наличии микрофона.
#
#
#
# Для внесения в базу программист начал писать такой код:
#
#
#
# monitor_name_1 = 'Samsung'
#
# monitor_matrix_1 = 'VA'
#
# monitor_res_1 = 'WQHD'
#
# monitor_freq_1 = 60
#
# monitor_name_2 = 'Samsung'
#
# monitor_matrix_2 = 'VA'
#
# monitor_res_2 = 'WQHD'
#
# monitor_freq_2 = 144
#
# monitor_name_3 = 'Samsung'
#
# monitor_matrix_3 = 'VA'
#
# monitor_res_3 = 'WQHD'
#
# monitor_freq_3 = 70
#
# monitor_name_4 = 'Samsung'
#
# monitor_matrix_4 = 'VA'
#
# monitor_res_4 = 'WQHD'
#
# monitor_freq_4 = 60
#
#
#
# headphones_name_1 = 'Sony'
#
# headphones_sensitivity_1 = 108
#
# headphones_micro_1 = False
#
# headphones_name_2 = 'Sony'
#
# headphones_sensitivity_2 = 108
#
# headphones_micro_2 = True
#
# headphones_name_3 = 'Sony'
#
# headphones_sensitivity_3 = 108
#
# headphones_micro_3 = True
#
#
#
# Поправьте программиста: перепишите код, используя классы и экземпляры классов.

# class Monitor:
#     name = "Samsung"
#     matrix = "VA"
#     resolution = "WQHD"
#     frequency = 0
#
#
# class Headphones:
#     name = "Sony"
#     sensitivity = 108
#     micro = True
#
#
# monitors = [Monitor() for _ in range(4)]
# headphones = [Headphones() for _ in range(3)]
#
# for index, number in enumerate([60, 144, 70, 60]):
#     monitors[index].frequency = number
#
# headphones[0].micro = False
