from random import randint


class Human:

    def __init__(self, name, degree_satiety=50, house=None):
        self.name = name
        self.degree_satiety = degree_satiety
        self.house = house

    def eat(self):
        self.degree_satiety += 10
        self.house.refrigerator_food -= 10
        return f'{self.name} поел: {self.degree_satiety}, ' \
               f'но еды стало меньше: {self.house.refrigerator_food}'

    def work(self):
        self.degree_satiety -= 10
        self.house.bedside_table_money += 10
        return f'{self.name} заработал денег: {self.house.bedside_table_money}, ' \
               f'но состояние сытости уменьшилось: {self.degree_satiety}'

    def play(self):
        self.degree_satiety -= 10
        return f'{self.name} поиграл, но состояние сытости уменьшилось: {self.degree_satiety}'

    def go_store_for_food(self):
        self.house.refrigerator_food += 10
        self.house.bedside_table_money -= 10
        return f'{self.name} сходил в магазин: {self.house.refrigerator_food}, ' \
               f'но деньги уменьшились: {self.house.bedside_table_money}'


class House:
    def __init__(self, refrigerator_food=50, bedside_table_money=0):
        self.refrigerator_food = refrigerator_food
        self.bedside_table_money = bedside_table_money


def day(person):
    cube = randint(1, 6)
    if person.degree_satiety < 0:
        print(f'{person.name} умер :(')
        return 1
    elif person.degree_satiety < 20 and home.refrigerator_food >= 10:
        output = person.eat()
    elif person.house.refrigerator_food < 10:
        output = person.go_store_for_food()
    elif person.house.bedside_table_money < 50:
        output = person.work()
    elif cube == 1:
        output = person.work()
    elif cube == 2:
        output = person.eat()
    else:
        output = person.play()
    print(output)
    return 0


home = House()
person1 = Human('Том', 50, home)
person2 = Human('Фред', 50, home)
i = 0
for i in range(1, 366):
    if day(person1) or day(person2):
        print('bad')
        break
if i == 365:
    print(f'{person1.name} и {person2.name} смогли прожить вместе целый год!')
