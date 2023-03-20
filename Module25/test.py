# # Задача 1. Юниты
# #
# # Есть базовый класс «Юнит», который определяется количеством здоровья (хитпоинты).
# # У Юнита есть действие «получить урон» (базовый класс получает 0 урона).
# #
# # Также есть два дочерних класса:
# #
# # Солдат: получает урон, равный переданному значению.
# # Обычный гражданин: получает урон, равный двукратному переданному значению.
# # Реализуйте родительский и дочерние классы и их методы, используя принцип полиморфизма (а также инкапсуляции и наследования, конечно же).
# #
# #
# #
#
# class Unit:
#
#     def __init__(self, hp):
#         self.__hp = hp
#
#     def set_hp(self, amount):
#         self.__hp = amount
#
#     def get_hp(self):
#         return self.__hp
#
#     def get_damage(self, amount):
#         self.set_hp(self.get_hp() - 0)  # -0 написан для наглядности, в теории  мы могли бы этого и не писать
#
#
# class Soldier(Unit):
#
#     def get_damage(self, amount):
#         self.set_hp(self.get_hp() - amount)
#
#
# class Citizen(Unit):
#     def get_damage(self, amount):
#         self.set_hp(self.get_hp() - amount * 2)
#
#
# # Задача 2. Полёт
# #
# # Иногда для реализации дочерних классов используется так называемый класс-роль,
# # где также описываются общие атрибуты и методы, но в программе инициализируются объекты только дочерних классов,
# # а базовый класс-роль не трогается. К примеру, что общего у бабочки и ракеты? Они обе могут летать и приземляться.
# #
# #
# #
# # Реализуйте класс «Может летать».
# #
# # Атрибуты:
# #
# # Высота = 0.
# # Скорость = 0.
# # Методы:
# #
# # Взлететь (в теле прописать pass).
# # Лететь (в теле прописать pass).
# # Приземлиться (установить высоту и скорость в значение 0).
# # Вывести высоту и скорость на экран.
# #
# #
# # Затем реализуйте два дочерних класса:
# #
# # «Бабочка», который может:
# #
# # Взлететь (высота = 1).
# # Лететь (скорость = 0.5).
#
# # «Ракета», которая может:
# #
# # Взлететь (высота = 500, скорость = 1000).
# # Приземлиться (высота = 0, взрыв).
# # Взорваться (тут уже что угодно).
#
#
# class CanFly:
#
#     def __init__(self):
#         self.altitude = 0  # метров
#         self.velocity = 0  # км/ч
#
#     def take_off(self):
#         pass
#
#     def fly(self):
#         pass
#
#     def land_on(self):
#         self.altitude = 0
#         self.velocity = 0
#
#     def __str__(self):
#         return '{} высота {} скорость {}'.format(
#             self.__class__.__name__, self.altitude, self.velocity,
#         )
#
#
# class Butterfly(CanFly):
#
#     def take_off(self):
#         self.altitude = 1
#
#     def fly(self):
#         self.velocity = 0.1
#
#
# class Aircraft(CanFly):
#
#     def take_off(self):
#         self.velocity = 300
#         self.altitude = 1000
#
#     def fly(self):
#         self.velocity = 800
#
#
# class Missile(CanFly):
#
#     def take_off(self):
#         self.velocity = 1000
#         self.altitude = 10000
#
#     def land_on(self):
#         self.altitude = 0
#         self.destroy_enemy_base()
#
#     def destroy_enemy_base(self):
#         print('Ракета показала себя великолепно. Только упала не на ту планету (C) Вернер фон Браун')
#
#
# # class CanFly:
# #     def __init__(self, h, s):
# #         self.set_h(h)
# #         self.set_s(s)
# #
# #     def takeoff(self):
# #         pass
# #
# #     def fly(self):
# #         pass
# #
# #     def land(self):
# #         self.__h = 0
# #         self.__s = 0
# #
# #     def set_h(self, h):
# #         self.__h = h
# #
# #     def set_s(self, s):
# #         self.__s = s
# #
# #     def __str__(self):
# #         return f'Высота: {self.__h}, скорость: {self.__s}'
# #
# #
# # class Butterfly(CanFly):
# #     def takeoff(self):
# #         self.set_h(1)
# #
# #     def fly(self):
# #         self.set_s(0.5)
# #
# #
# # class Rocket(CanFly):
# #     def takeoff(self):
# #         self.set_h(500)
# #         self.set_s(1000)
# #
# #     def land(self):
# #         self.set_h(0)
# #         self.explosion()
# #
# #     def explosion(self):
# #         print('6AX')
#
# # class Unit:
# #     def __init__(self, hp):
# #         self.set_hp(hp)
# #
# #     def set_hp(self, hp):
# #         self.__hp = hp
# #
# #     def get_hp(self):
# #         return self.__hp
# #
# #     def get_damage(self, damage):
# #         self.set_hp(self.get_hp() - 0)
# #
# #
# # class Soldier(Unit):
# #     def get_damage(self, damage):
# #         self.set_hp(self.get_hp() - damage)
# #
# #
# # class Citizen(Unit):
# #     def get_damage(self, damage):
# #         self.set_hp(self.get_hp() - 2 * damage)
# # # Задача 1. Корабли
# # #
# # # Даны два класса кораблей — грузовой и военный. У каждого из этих кораблей есть своя модель,
# # # и каждый может сделать два действия: сообщить свою модель и идти по воде.
# # #
# # # Грузовой корабль имеет такой атрибут, как заполненность, изначально он равен нулю.
# # # У него есть ещё два действия: погрузить и выгрузить груз с корабля.
# # #
# # # У военного же корабля нет никаких грузов, есть только оружие, которое передаётся вместе с моделью.
# # # Также, вместо погрузки и выгрузки, у него есть другое действие — атаковать.
# # #
# # # Реализуйте классы грузового и военного кораблей.
# # # Для этого выделите общие атрибуты и методы в отдельный класс «Корабль» и используйте наследование.
# # # Не забудьте про функцию super в дочерних классах.
# # #
# # #
# # #
# #
# # class Ship:
# #
# #     def __init__(self, model="корабль"):
# #         self.model = model
# #
# #     def __str__(self):
# #         return self.model
# #
# #     def sail(self):
# #         print(f"{self.model} идёт по воде!")
# #
# #
# # class WarShip(Ship):
# #
# #     def __init__(self, weapon, model="военный корабль"):
# #         super().__init__(model)
# #         self.weapon = weapon
# #
# #     def attack(self):
# #         print(f"{self} делает пиу-пиу!")
# #
# #
# # class CargoShip(Ship):
# #
# #     def __init__(self, model="грузовой корабль"):
# #         super().__init__(model)
# #         self.fullness = 0
# #
# #     def loading(self, value):
# #         self.fullness += value
# #
# #     def unloading(self, value):
# #         self.fullness -= value
# #
# #
# # # Задача 2. Роботы
# # #
# # # На военную базу завезли несколько интересных моделей роботов, которые похожи между собой, но имеют немного разные функции.
# # # У каждого робота есть номер модели и действие operate, которое означает, что делает робот. Особенности роботов следующие:
# # #
# # # У робота-пылесоса есть мешок для мусора, изначально он пустой (0). При команде operate робот сообщает,
# # # что он пылесосит пол, и выводит текущую заполняемость мешка.
# # # У военного робота есть оружие, и при команде operate он выводит сообщение о защите военного объекта с помощью этого оружия.
# # # Ещё есть робот — подводная лодка, который также является военным. У этого робота есть значение глубины,
# # # и при команде operate он делает то же, что и военный робот, плюс сообщает, что охрана ведётся под водой.
# # #
# # # Напишите программу, которая реализует все необходимые классы роботов.
# # #
# # #
# # #
# #
# # class Robot:
# #
# #     def __init__(self, model):
# #         self.model = model
# #
# #     def __str__(self):
# #         return '{} model {}'.format(self.__class__.__name__, self.model)
# #
# #     def operate(self):
# #         print('Робот ездит по кругу')
# #
# #
# # class WarRobot(Robot):
# #
# #     def __init__(self, gun, model):
# #         super().__init__(model)
# #         self.gun = gun
# #
# #     def operate(self):
# #         print(f'Робот охраняет военный обьект при помощи {self.gun}')
# #
# #
# # class VacuumCleaningRobot(Robot):
# #
# #     def __init__(self, model):
# #         super().__init__(model)
# #         self.garbage_bag = 0
# #
# #     def operate(self):
# #         print('Робот пылесосит пол')
# #
# #
# # class SubmarineRobot(WarRobot):
# #
# #     def __init__(self, gun, model, depth):
# #         super().__init__(gun, model)
# #         self.depth = depth
# #
# #     def operate(self):
# #         super().operate()
# #         print('Охрана ведется под водой на глубине', self.depth)
# #
# #
# # # Задача 3. Кастомные исключения
# # #
# # # Исключения в Python также являются классами, и все они берут свои истоки от самого главного класса — Exception.
# # # И для создания своего собственного класса ошибки достаточно написать его дочерний класс. Например:
# # #
# # #
# # #
# # # class MyOwnException(Exception):
# # #
# # #     pass
# # #
# # #
# # #
# # # raise MyOwnException('Это моя ошибка!')
# # #
# # #
# # #
# # # Причём содержимое объекта исключения чаще всего так и оставляют (просто pass), чтобы не сломать автоматические обработчики исключений.
# # #
# # # Напишите программу, которая считывает из файла numbers.txt пары чисел, делит первое число на второе и выводит ответ на экран.
# # # Если первое число меньше второго, то программа выдаёт исключение DivisionError (нельзя делить большее на меньшее).
# # #
# # # Дополнительно, с помощью try except, можно обработать исключение на своё усмотрение.
# #
# # class DivisionError(Exception):
# #     pass
# #
# #
# # with open("numbers.txt", "r", encoding="utf8") as file:
# #     for line in file:
# #         try:
# #             clear_line = line.rstrip()
# #             first, second = clear_line.split()
# #             if int(first) < int(second):
# #                 raise DivisionError("нельзя делить большее на меньшее")
# #         except (ValueError, DivisionError) as exc:
# #             print(exc, type(exc), first, second)
# #
# #
#
#
# # class Robot:
# #     def __init__(self, model):
# #         self.__model = model
# #
# #     def operate(self):
# #         pass
# #
# #
# # class Roomba(Robot):
# #     def __init__(self, model):
# #         super().__init__(model)
# #         self.__garbage_bag = 0
# #
# #     def operate(self):
# #         self.__garbage_bag += 1
# #         print(f'Пылешошу пол! Заполняемость мешка: {self.__garbage_bag}')
# #
# #
# # class WarRobot(Robot):
# #     def __init__(self, model, weapon):
# #         super().__init__(model)
# #         self.__weapon = weapon
# #
# #     def operate(self):
# #         print(f'Защищаю военный объект при помощи: {self.__weapon}!')
# #
# #
# # class Submarine(Robot):
# #     def __init__(self, model, deep):
# #         super().__init__(model)
# #         self.__deep = deep
# #
# #     def operate(self):
# #         print(f'Защищаю военный объект. Охрана ведется под водой на глубине: {self.__deep}')
#
#
# # class Ship:
# #     def __init__(self, model):
# #         self.__model = model
# #
# #     def get_model(self):
# #         return self.__model
# #
# #     def sail(self):
# #         return f'Корабль модели {self.__model} плывет по воде'
# #
# #
# # class CargoShip(Ship):
# #     def __init__(self, model):
# #         super().__init__(model)
# #         self.__fullness = 0
# #
# #     def load(self):
# #         self.__fullness += 1
# #         print(f'Корабль {self.get_model()} загружается: {self.__fullness}')
# #
# #     def unload(self):
# #         if self.__fullness > 0:
# #             self.__fullness -= 1
# #             print(f'Корабль {self.get_model()} разгружается: {self.__fullness}')
# #
# #
# # class WarShip(Ship):
# #     def __init__(self, model, weapon):
# #         super().__init__(model)
# #         self.__weapon = weapon
# #
# #     def attack(self):
# #         return f'Корабль {self.get_model()} атакует оружием {self.__weapon}'
# #
# #
# # x = CargoShip('ssd')
# # x.load()
# # x.unload()
#
# # # Задача 1. Координаты точки
# # #
# # # В одной из практик предыдущего модуля была задача на реализацию класса «Точка».
# # # Модернизируйте класс по следующему условию: объект «Точка» на плоскости имеет координаты x и y;
# # # при создании новой точки могут передаваться пользовательские значения координат, по умолчанию x = 0, y = 0.
# # #
# # #
# # #
# # # Реализуйте класс, который будет представлять эту точку, и напишите следующие методы:
# # #
# # # Предоставление информации о точке (используйте магический метод str).
# # # Геттер и сеттер для x.
# # # Геттер и сеттер для y.
# # # Для сеттеров реализуйте проверку на корректность входных данных: координаты должны быть числом.
# # #
# # #
# # #
# #
# # class Point:
# #     count = 0
# #
# #     def __init__(self, x=0, y=0):
# #         self.__x = x
# #         self.__y = y
# #         Point.count += 1
# #
# #     def __str__(self):
# #         return f"({self.__x}, {self.__y})"
# #
# #     def get_x(self):
# #         return self.__x
# #
# #     def get_y(self):
# #         return self.__y
# #
# #     def check_value(self, value):
# #         if isinstance(value, str) and value.isdigit():
# #             value = float(value)
# #         if isinstance(value, (int, float)):
# #             return value
# #         return None
# #
# #     def set_x(self, value):
# #         checker_value = self.check_value(value)
# #         if checker_value:
# #             self.__x = checker_value
# #
# #     def set_y(self, value):
# #         checker_value = self.check_value(value)
# #         if checker_value:
# #             self.__y = checker_value
# #
# #
# # # Задача 2. Человек
# # #
# # # Реализуйте класс «Человек», который инициализируется именем (имя должно состоять только из букв)
# # # и возрастом (должен быть в диапазоне от 0 до 100), а внутри класса считается общее количество инициализированных объектов.
# # # Реализуйте сокрытие данных для всех атрибутов (как статических, так и динамических),
# # # а для изменения и получения данных объекта напишите специальные геттеры и сеттеры.
# # #
# # # При тестировании класса измените приватный атрибут (например, возраст) двумя способами:
# # # сеттером и «крайне не рекомендуемым», который был показан в видео.
# #
# # class Human:
# #     count = 0
# #
# #     def __init__(self, name, age):
# #         self.__name = ''
# #         self.__age = 0
# #         self.set_age(age)
# #         self.set_name(name)
# #
# #         Human.count += 1
# #
# #     def set_age(self, value):
# #         if isinstance(value, (int, float)) and 0 <= value <= 100:
# #             self.__age = value
# #         else:
# #             raise ValueError("Ошибка в возрасте")
# #
# #     def set_name(self, value):
# #         if isinstance(value, str) and value.isalpha():
# #             self.__name = value
# #         else:
# #             raise ValueError("Ошибка в имени")
# #
# #     def get_name(self):
# #         return self.__name
# #
# #     def get_age(self):
# #         return self.__age
# #
# #
# # human = Human('helo', 100)  # значения передадутся в сеттер
# # human._Human__age = 99  # «крайне не рекомендуемый» метод
