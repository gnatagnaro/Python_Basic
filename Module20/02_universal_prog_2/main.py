def is_prime(num):
    if num > 1:
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                return False
        return True


def crypto(data):
    result = []
    if isinstance(data, dict):
        data = data.values()
    for index, value in enumerate(data):
        if is_prime(index):
            result.append(value)
    return result

#
# print(crypto('О Дивный Новый мир!'))
# print(crypto([100, 200, 300, 'буква', 0, 2, 'а']))
# print(crypto({0: 'е', 1: 'о', 2: 'ч', 3: 'ы', 4: 'в', 5: 'н', 6: 'д', 7: 'а', 8: 'ш', 9: 'ц'}))
# print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
