# Сначала вводится число N — количество друзей, затем вводится число K — количество долговых расписок,
# после этого следует K троек чисел: номер друга, взявшего в долг, номер друга, давшего деньги, и сумма.
# Гарантируется, что ни один друг не брал в долг сам у себя.
n = int(input('Кол-во друзей: '))
k = int(input('Долговых расписок: '))
friends_balance = [0] * n

for i in range(k):
    print(f'\n{i + 1}-я расписка')
    to = int(input('Кому: '))
    _from = int(input('От кого: '))
    how_much = int(input('Сколько: '))
    friends_balance[to - 1] += how_much
    friends_balance[_from - 1] -= how_much

print('\nБаланс друзей: ')
for i in range(len(friends_balance)):
    print(f'{i + 1}: {friends_balance[i]}')

# в примерах на сайте ошибка, так как по условию задачи: "Положительное число означает,
# что друг должен получить деньги от других, отрицательное — должен отдать деньги."

# Кол-во друзей: 3
# Долговых расписок: 1
#
# 1-я расписка
# Кому: 3
# От кого: 1
# Сколько: 100
#
# Баланс друзей:
# 1 : 100
# 2 : 0
# 3 : -100

# в балансе у 1: 100, а у 2: -100, хотя 1 отдавал деньги 3, и должно быть наоборот: у 1: -100, а у 2: 100