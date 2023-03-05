def get_input_parameters():
    """
    Получаем неотсортированный список чисел

    :return: неотсортированный список чисел, например: [1, 4, -3, 0, 10]
    :rtype: List[int]
    """
    n = int(input('Введите количество чисел в списке: '))
    num_list = []

    for i in range(n):
        num = int(input('Введите число: '))
        num_list.append(num)

    print('Изначальный список:', num_list)
    return num_list


def display_result(sorted_list):
    """
    Выводим отсортированный список

    :param sorted_list: отсортированный список, например: [-3, 0, 1, 4, 10]
    :type sorted_list: List[int]
    """
    print('Отсортированный список:', original_list)


def sort_list(original_list):
    """
    Сортируем список

    :param original_list: Исходный список: [1, 4, -3, 0, 10]
    :type original_list: List[int]

    :return: отсортированный, например: [-3, 0, 1, 4, 10]
    :rtype: List[int]
    """
    for minim in range(len(original_list)):
        for curr in range(minim, len(original_list)):
            if original_list[curr] < original_list[minim]:
                original_list[curr], original_list[minim] = original_list[minim], original_list[curr]
    return original_list


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    original_list = get_input_parameters()  # получаем параметры
    sorted_list = sort_list(original_list)  # сортируем список.
    display_result(sorted_list)  # выводим результат
