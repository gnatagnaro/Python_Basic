violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

count_minutes = 0
n = int(input('Сколько песен выбрать? '))

for i in range(n):
    name = input(f'Введите название {i + 1}-й песни: ').lower()
    for j in violator_songs:
        if j[0].lower() == name:
           count_minutes += j[1]


print(f'Общее время звучания песен: {round(count_minutes, 2)} минуты')
