"""

'Каждый дочерний класс должен иметь конструктор с одним параметром,
передающий свой параметр конструктору базового класса'.

Не вижу смысла это делать, так как в дочерних классах не добавляются новые параметры,
а значит, что при создании объекта дочернего класса вызывается конструктор родителя

"""


class Property:
    def __init__(self, worth):
        self.set_worth(worth)  # стоит ли делать так? защищаю данные от случайного изменения

    def get_worth(self):
        return self.__worth

    def set_worth(self, worth):
        self.__worth = worth

    def calculation(self):
        pass

    def __str__(self):
        return f'{__class__.__name__}, {self.__worth}'


class Apartment(Property):
    # def __init__(self, worth):
    #     super().__init__(worth)

    def calculation(self):
        return self.get_worth() / 1000


class Car(Property):
    # def __init__(self, worth):
    #     super().__init__(worth)

    def calculation(self):
        return self.get_worth() / 200


class CountryHouse(Property):
    # def __init__(self, worth):
    #     super().__init__(worth)

    def calculation(self):
        return self.get_worth() / 500


def main():
    money = int(input('Введите количество денег: '))
    apartment = Apartment(int(input('Введите стоимость квартиры: '))).calculation()
    car = Car(int(input('Введите стоимость машины: '))).calculation()
    country_house = CountryHouse(int(input('Введите стоимость дома: '))).calculation()
    print(f'Налог на квартиру: {apartment:,.1f} руб.; '
          f'на машину: {car:,.1f} руб.; '
          f'на дом: {country_house:,.1f} руб.\n ')

    if apartment + car + country_house > money:
        print(f'Не хватает: {abs(money - (apartment + car + country_house)):,.1f} руб.')
    else:
        print(f'Осталось: {money - (apartment + car + country_house):,.1f} руб.')


main()
