# не очень понятно условие задания.. реализовал, как понял

def calculating_math_func(data, dict):
    if data in factorials:  # если факториал в словаре - result = его значению
        result = factorials[data]
    else:
        result = 1
        for index in range(1, data + 1):
            result *= index
        factorials[data] = result  # иначе находим факториал и добавляем его значение в словарь
    result /= data ** 3
    result = result ** 10
    return result


factorials = {}  # словарь всех найденных факториалов
#
# print(calculating_math_func(3, factorials))
# print(factorials)
# print(calculating_math_func(3, factorials))
# print(factorials)
# print(calculating_math_func(3, factorials))
# print(factorials)
