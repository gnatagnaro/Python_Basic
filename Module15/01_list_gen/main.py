def get_input_parameters():
    num = int(input('Введите число: '))

    return num


def display_result(odd_numbers):
    x = f'Список из нечётных чисел от одного до {odd_numbers[-1]}: {odd_numbers}'

    print(x)


def get_odd_numbers(number):
    list_num = []

    for i in range(1, number + 1):
        if i % 2 != 0:
            list_num.append(i)

    return list_num


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    number = get_input_parameters()  # получаем параметры
    odd_numbers = get_odd_numbers(number)  # получаем нечётные числа
    display_result(odd_numbers)  # выводим результат
