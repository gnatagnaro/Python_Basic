from random import randint


class Warrior:

    index = 0

    def __init__(self):
        self.health = 100
        Warrior.index += 1
        self.id = Warrior.index

    def hit(self, x):
        if x.health > 0:
            x.health -= 20


warriors = [Warrior(), Warrior()]


def fight():
    q = int(input('Введите: 1 - атаковать, 2 - для закрытия программы: '))
    if q == 1:
        i = randint(0, 1)
        attacker, victim = warriors[i], warriors[i - 1]
        attacker.hit(victim)
        print(f'Атаковал юнит №{attacker.id}. У противника осталось {victim.health}\n')
        if victim.health == 0:
            print(f'Победил юнит №{attacker.id}!\n')
        else:
            fight()
    elif q == 2:
        print('Вы вышли из программы.\n')
    else:
        print('Вы ввели не ту команду!\n')
        fight()


fight()
