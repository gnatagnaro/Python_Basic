print('Задача 6. Спецшифр')

# Два сотрудника спецслужб переписываются необычным шифром.
# Каждую букву они шифруют в виде строки,
# внутри которой есть длинная последовательность букв “s”, 
# а длина самой длинной - это и есть номер буквы алфавита, которую хотят отправить.
# 
# Напишите программу,
# которая получает на вход строку,
# подсчитывает в ней самую длинную последовательность подряд идущих букв “s” и выводит ответ на экран.
# 
# Пример:
# Введите строку: ssbbbsssbc
# Самая длинная последовательность: 3

s = input('Введите строку: ')
count = 0
maxim = 0

for i in range(len(s)):
    if s[i] == 's':
        count += 1
        if s[len(s)-1] == 's':
            if count > maxim:
                maxim = count
    else:
        if count > maxim:
            maxim = count
        count = 0
        
print(f'Самая длинная последовательность: {maxim}')