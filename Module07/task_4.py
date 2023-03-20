print('Задача 4. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было. 
# 
# Напишите программу, 
# которая получает список оценок - N чисел - и выводит на экран сообщение о том, 
# кого сегодня больше: отличников, хорошистов или троечников.

# Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.

n = int(input('Введите количество человек в классе: '))
count_three = 0
count_four = 0
count_five = 0
ans = 'Сегодня в классе никого нет'

for i in range(n):
    print('Оценка №', i + 1)
    mark = int(input('Введите оценку по информатике (3, 4 или 5): '))
    if mark == 3:
        count_three += 1
    elif mark == 4:
        count_four += 1
    elif mark == 5:
        count_five += 1
    else:
        # Запрещаем пользователю вводить любое другое число, кроме 3, 4 или 5: 
        while True:
            print('Не то число!')
            mark = int(input('Введите оценку по информатике (3, 4 или 5): '))
            if mark == 3:
                count_three += 1
                break
            elif mark == 4:
                count_four += 1
                break
            elif mark == 5:
                count_five += 1
                break
                
maxim = 0
if count_three > maxim:
    maxim = count_three
    ans = 'Сегодня больше троечников'
if count_four > maxim:
    maxim = count_four
    ans = 'Сегодня больше хорошистов'
if count_five > maxim:
    maxim = count_five
    ans = 'Сегодня больше отличников'
    
# Попытка усложнить задание, рассмотрев те случаи, когда количество учеников равно:
if count_three == count_four == count_five and count_three > 0 and count_four > 0 and count_five > 0:
    ans = 'Количество троечников, хорошистов и отличников равно'
else:
    if count_three == count_four and count_three > 0 and count_four > 0 and count_four >= maxim:
        ans = 'Количество троечников и хорошистов равно'
    elif count_three == count_five and count_three > 0 and count_five > 0 and count_five >= maxim:
        ans = 'Количество троечников и отличников равно'
    elif count_four == count_five and count_four > 0 and count_five > 0 and count_five >= maxim:
        ans = 'Количество хорошистов и отличников равно'
        
print(ans)