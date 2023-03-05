def get_input_parameters():
    """
    Получаем список весов контейнеров и вес нового контейнера
    Незабываем проверит данные: все числа целые и не превышают 200.

    :return: список весов контейнеров и вес нового контейнера,
             например: [[165, 163, 160, 160, 157, 157, 155, 154], 162]
    :rtype: List[List[int], int]
    """
    list_cont = []
    all_list = []

    n = int(input('Количество контейнеров: '))

    for i in range(n):
        cont = int(input('Введите вес контейнера: '))
        while cont > 200:
            print('Введенный вес контейнера должен быть меньше 200! ')
            cont = int(input('Введите вес контейнера: '))
        list_cont.append(cont)

    new_cont = int(input('Введите вес нового контейнера: '))
    all_list.append(list_cont)
    all_list.append(new_cont)
    return all_list


def display_result(serial_number_new_container):
    """
    Выводим порядковый номер нового контейнера.

    :param serial_number_new_container: порядковый номер нового контейнера, например: 3
    :type serial_number_new_container: int
    """

    print(f'Номер, который получит новый контейнер: {serial_number_new_container}')


def search_serial_number_new_container(list_container_weights, new_container_weight):
    """
    Ищем куда вставим новый контейнер.

    :param list_container_weights: список весов контейнеров, например: [165, 163, 160, 160, 157, 157, 155, 154]
    :type list_container_weights: List[int]
    :param new_container_weight: вес нового контейнера, например: 166
    :type new_container_weight: int

    :return: порядковый номер нового контейнера, например: 3
    :rtype: int
    """
    list_container_weights.append(new_container_weight)
    list_container_weights.sort(reverse=True)

    for j in range(len(list_container_weights)):
        if list_container_weights[j] < new_container_weight:
            param = j
            break

    return param


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    input_data = get_input_parameters()  # получаем параметры
    list_container_weights = input_data[0]
    new_container_weight = input_data[1]
    # Ищем куда вставим новый контейнер.
    serial_number_new_container = search_serial_number_new_container(list_container_weights, new_container_weight)
    display_result(serial_number_new_container)  # выводим результат
