def get_input_parameters():
    """
    Получаем сдвиг и начальны список

    :return: например: [3, [1, 4, -3, 0, 10]]
    :rtype: List[int, List[int]]
    """
    all_list = []
    cur_list = []

    n = int(input('Введите кол-во элементов списка: '))
    for i in range(n):
        x = int(input('Введите элемент списка: '))
        cur_list.append(x)

    _shift = int(input('Введите сдвиг: '))
    all_list.append(_shift)
    all_list.append(cur_list)
    print('Изначальный список:', cur_list)

    return all_list


def display_result(shifted_list):
    """
    Выводим получившиеся список

    :param shifted_list: сдвинутый список, например: [5, 1, 2, 3, 4]
    :type shifted_list: List[int]
    """
    print('Сдвинутый список:', shifted_list)


def shift_list(shift, original_list):
    """
    Сдвигаем список на определённое количество элементов в право

    :param shift: сдвиг: 3
    :type shift: int
    :param original_list: Исходный список: [1, 4, -3, 0, 10]
    :type original_list: List[int]

    :return: сдвинутый список, например: [5, 1, 2, 3, 4]
    :rtype: List[int]
    """
    #original_list = original_list[-shift:] + original_list[:-shift]
    # print(original_list)

    new_ls = [0] * len(original_list)
    j = 0
    for i in range(len(original_list)):
        if i + shift >= len(original_list):

            new_ls[j] = original_list[i]
            j += 1
        else:
            new_ls[i + shift] = original_list[i]

    return new_ls


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    input_data = get_input_parameters()  # получаем параметры
    shift = input_data[0]
    original_list = input_data[1]
    shifted_list = shift_list(shift, original_list)  # сдвигаем список.
    display_result(shifted_list)  # выводим результат
