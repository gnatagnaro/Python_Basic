import random

list_team1 = [round(random.triangular(5, 10), 2) for i in range(21)]
list_team2 = [round(random.uniform(5, 10), 2) for j in range(21)]
winners_list = [list_team1[x] if list_team1[x] > list_team2[x] else list_team2[x] for x in range(21)]

print(f'Первая команда: {list_team1}')
print(f'Вторая команда: {list_team2}')
print(f'Победители тура: {winners_list}')
