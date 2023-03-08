result = 0
with open('calc.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        try:
            result += eval(line)
        except Exception:
            if input(f'Обнаружена ошибка: {line.strip()}    Хотите исправить? ').lower() == 'да':
                line = input('Введите исправленную строку: ')
                result += eval(line)
print(f'Сумма результатов: {result}')

# второй вариант полностью рабочий и соответствует примерам в условии задачи, НО:

# хотел реализовать через ветвление, но выглядит не очень красиво, поэтому
# забросил эту идею, потому что минус данной программы в том, что
# при таком вводе она работает нормально: 10 + 3, а при таком уже нет: 10+3.
# это происходит из-за того, что основная идея в методе сплит, который во втором
# случае проверяет массив, состоящий всего из 1 элемента x = ['10+3']
# def eval(line):
#     try:
#         x = line.split()
#         if (x[0] and x[2]).isdigit():
#             if x[1] == '+':
#                 return (int(x[0]) + int(x[2]))
#             elif x[1] == '-':
#                 return (int(x[0]) - int(x[2]))
#             elif x[1] == '*':
#                 return (int(x[0]) * int(x[2]))
#             elif x[1] == '/':
#                 return (int(x[0]) / int(x[2]))
#             elif x[1] == '//':
#                 return (int(x[0]) // int(x[2]))
#             elif x[1] == '%':
#                 return (int(x[0]) % int(x[2]))
#             elif x[1] == '**':
#                 return (int(x[0]) ** int(x[2]))
#             else:
#                 raise Exception
#     except Exception:
#         if input(f'Обнаружена ошибка: {i_line.strip()}    Хотите исправить? ').lower() == 'да':
#             line = input('Введите исправленную строку: ')
#             return eval(line)
#         return 0
#
#
# with open('calc.txt', 'r', encoding='utf-8') as f:
#     summ = 0
#     for i_line in f:
#         summ += eval(i_line)
# print(f'Сумма результатов: {summ}')
