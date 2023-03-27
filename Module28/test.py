# Задача 1. Транспорт 2
#
# Используя код задачи про автомобили, лодки и амфибии, дополните абстрактный класс геттерами и сеттерами для соответствующих атрибутов.
# Используйте встроенные декораторы. Вот входные данные той задачи:
#
# У нас есть парк транспорта. У каждого транспорта есть цвет и скорость,
# и каждый умеет двигаться и подавать сигнал. В парке транспорта стоят:
#
# Автомобили. Они могут ездить только по земле.
# Лодки. Ездят только по воде.
# Амфибии. Могут перемещаться и по земле, и по воде.
from abc import ABC, abstractmethod


class MusicMixin:

    def play_music(self):
        print("""
        I see trees of green
        Red roses too
        I see them bloom
        For me and for you
        And I think to myself
        What a wonderful world
        """)


class Transport(ABC):

    def __init__(self, color, speed):
        self._color = color
        self._speed = speed

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @abstractmethod
    def ride_on_earth(self):
        pass

    @abstractmethod
    def ride_on_water(self):
        pass

    def signal(self):
        print("Сигнал")


class Car(Transport):

    def ride_on_earth(self):
        print("Едем по земле")


class Boat(Transport):

    def ride_on_water(self):
        print("Ходим по воде")


class Amphibian(Car, Boat, MusicMixin):
    pass


amph_transport = Amphibian('blue', 123)
amph_transport.ride_on_earth()
amph_transport.ride_on_water()
amph_transport.play_music()
print(amph_transport.color)
amph_transport.color = 'white'
print(amph_transport.color)


# Задача 1. Работа с файлом
#
# Реализуйте класс File — контекстный менеджер для работы с файлами.
# Он должен принимать на вход имя файла и режим чтения/записи и открывать сам файл. В начале работы менеджер возвращает файловый объект,
# а в конце — закрывает файл.
#
#
#
# Пример основного кода:
#
# with File(‘example.txt’, ‘w’) as file:
#
#     file.write(‘Всем привет!’)
#
#
#


class File:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding='utf8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True


with File("example.txt", "w") as file:
    file.write("Всем привет!")


# Задача 2. Пример
#
# На одном собеседовании вам дали такой основной код:
#
#
#
# my_obj = Example()
#
# with my_obj as obj:
#
#     print('Код внутри первого вызова контекст менеджера')
#
#     with my_obj as obj2:
#
#         raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')
#
#
#
#     print('Я обязательно выведусь...')
#
#
#
# Также вместе с этим кодом выдали результат его выполнения:
#
#
#
# Вызов __init__
#
# Вызов __enter__
#
# Код внутри первого вызова контекст менеджера
#
# Вызов __enter__
#
# Вызов __exit__
#
# Тип ошибки: <class 'Exception'>
#
# Значение ошибки: Выброс исключения во вложенном (втором) вызове контекст-менеджера
#
# "След" ошибки: <traceback object at 0x00000234E54CE4C0>
#
# Вызов __exit__
#
# Тип ошибки: <class 'Exception'>
#
# Значение ошибки: Выброс исключения во вложенном (втором) вызове контекст-менеджера
#
# "След" ошибки: <traceback object at 0x00000234E54CE4C0>
#
# . . . . (тут сама ошибка красным цветом) . . . .
#
#
#
# Исходя их этих входных данных, реализуйте класс «Контекст-менеджер», который будет выдавать такой же результат.
#
# После этого поправьте класс так, чтобы сработала последняя строчка основного кода. Сам основной код редактировать нельзя.
#
#
#
# Результат с последней строчкой:
#
# Вызов __init__
#
# Вызов __enter__
#
# Код внутри первого вызова контекст-менеджера
#
# Вызов __enter__
#
# Вызов __exit__
#
# Тип ошибки: <class 'Exception'>
#
# Значение ошибки: Выброс исключения во вложенном (втором) вызове контекст-менеджера
#
# "След" ошибки: <traceback object at 0x00000258ACA4F5C0>
#
# Я обязательно выведусь...
#
# Вызов __exit__

class Example:

    def __init__(self):
        print("Вызов __init__")

    def __enter__(self):
        print("Вызов __enter__")
        return True

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Вызов __exit__")
        if exc_type:
            print(f'Тип ошибки: {exc_type}\nЗначение ошибки: {exc_val}\n"След" ошибки: {exc_tb}')
        return True  # первый вариант без этой строки, второй с этой строкой


my_obj = Example()

with my_obj as obj:
    print('Код внутри первого вызова контекст менеджера')

    with my_obj as obj2:
        raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')

    print('Я обязательно выведусь...')



# Задача 1. Транспорт
#
# У нас есть парк транспорта. У каждого транспорта есть цвет и скорость, и каждый умеет двигаться и подавать сигнал.
# В парке транспорта стоят:
#
# Автомобили. Они могут ездить только по земле.
# Лодки. Ездят только по воде.
# Амфибии. Могут перемещаться и по земле, и по воде.
# Напишите код, который реализует соответствующие классы и методы. Класс «Транспорт» должен быть абстрактным и содержать абстрактные методы.
#
# Также добавьте класс-примесь, в котором реализован функционал проигрывания музыки. «Замешайте» этот класс в «Амфибию»
#
#
#
from abc import ABC, abstractmethod


class MusicMixin:

    def play_music(self):
        print("""
        I see trees of green
        Red roses too
        I see them bloom
        For me and for you
        And I think to myself
        What a wonderful world
        """)


class Transport(ABC):

    @abstractmethod
    def ride_on_earth(self):
        pass

    @abstractmethod
    def ride_on_water(self):
        pass


class Car(Transport):

    def ride_on_earth(self):
        print("Едем по земле")


class Boat(Transport):

    def ride_on_water(self):
        print("Ходим по воде")


class Amphibian(Car, Boat, MusicMixin):
    pass


amph_transport = Amphibian()
amph_transport.ride_on_earth()
amph_transport.ride_on_water()
amph_transport.play_music()


# Задача 2. Фигуры
#
# При моделировании компьютерных объектов используются два типа фигур: прямоугольники и квадраты. Каждая из них имеет координаты XY,
# длину и ширину. Также каждая фигура может менять координаты (двигаться) и менять размер.
#
# Реализуйте такие классы. Учтите, что с точки зрения интерфейса прямоугольник и квадрат — это разные фигуры и работают они по-разному.
# В частности, по разному работает метод изменения размера фигуры, так как у квадрата все стороны равны.

# Вариант с примесью - когда один метод работает одинаково для двух классов
class Figure:

    def __init__(self, pos_x, pos_y, length, width):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length
        self.width = width

    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


class ResizeAbleMixin:
    def resize(self, length, width):
        self.length = length
        self.width = width


class Rectangle(Figure, ResizeAbleMixin):
    pass


class Square(Figure, ResizeAbleMixin):

    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size, size)


# Второй вариант с абстрактным классом и переопределением метода изменения размеров

class Figure(ABC):

    def __init__(self, pos_x, pos_y, length, width):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length
        self.width = width

    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def resize(self, width, length):
        pass


class Rectangle(Figure):

    def resize(self, width, length):
        self.width = width
        self.length = length


class Square(Figure):

    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size, size)

    def resize(self, width, length):
        if width == length:
            self.width = width
            self.length = length
        else:
            print("У квадрата стороны равны!")


# Задача 1. Снова роботы
#
# На военную базу привезли очередную партию роботов. И в этот раз не абы каких, а летающих: разведывательного дрона и военного робота.
#
# Разведывательный дрон просто летает в поиске противника.
# При команде operate он выводит сообщение «Веду разведку с воздуха» и передвигается немного вперёд.
#
# У летающего военного робота есть оружие,
# и при команде operate он выводит сообщение о защите военного объекта с воздуха с помощью этого оружия.
#
# Напишите программу, которая реализует все необходимые классы роботов.
# Сущности «Робот» и «Может летать» должны быть вынесены в отдельные классы.
# Обычный робот имеет модель и может вывести сообщение «Я — Робот». Объект, который умеет летать,
# дополнительно имеет атрибуты «Высота» и «Скорость», а также может взлетать, летать и приземляться.

class Robot:

    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model

    def __str__(self):
        res = super().__str__()
        return res + ' {} model {}'.format(self.__class__.__name__, self.model)

    def operate(self):
        print('Я - Робот!')


class CanFly:

    def __init__(self, *args, **kwargs):
        self.altitude = 0  # метров
        self.velocity = 0  # км/ч

    def take_off(self):
        self.altitude = 100
        self.velocity = 300

    def fly(self):
        self.altitude = 5000

    def land_on(self):
        self.altitude = 0
        self.velocity = 0

    def operate(self):
        super().operate()
        print('летим')

    def __str__(self):
        res = super().__str__()
        return res + ' {} высота {} скорость {}'.format(
            self.__class__.__name__, self.altitude, self.velocity,
        )


class ScoutDrone(CanFly, Robot):

    def __init__(self, model):
        super().__init__(model=model)

    def operate(self):
        super().operate()
        print('Робот ведет разведку с воздуха')


class WarDrone(CanFly, Robot):

    def __init__(self, model, gun):
        super().__init__(model=model)
        self.gun = gun

    def operate(self):
        super().operate()
        print(f'Робот защищает объект при помощи {self.gun}')


print()
ScoutDrone('a1').operate()
print()
WarDrone('r2-d2', 'intellect').operate()


class X: pass
class A(X): pass
class B(X): pass
class C(X): pass
class D(X): pass
class E(A, B): pass
class F(B, C): pass
class G(B, C, D): pass
class H(C, D): pass
class J(E, G): pass
class K(F, G, H): pass
class Z(J, K): pass
# порядок разрешения метода init ZJEAKFGBHCDX
