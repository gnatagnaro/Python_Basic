def get_input_parameters():

    n = int(input('Количество видеокарт: '))
    video_list = []

    for i in range(n):
        x = int(input(f'{i + 1} Видеокарта: '))
        video_list.append(x)

    return video_list


def display_result(old_video_cards, new_video_cards):

    print(f'Старый список видеокарт: {old_video_cards}')
    print(f'Новый список видеокарт: {new_video_cards}')


def select_video_cards(video_cards):
    new_list = []

    maxim = -1
    for j in range(len(video_cards)):
        if video_cards[j] > maxim:
            maxim = video_cards[j]

    for i in range(len(video_cards)):
        if video_cards[i] != maxim:
            new_list.append(video_cards[i])

    return new_list


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    video_cards = get_input_parameters()  # получаем параметры
    result_video_cards = select_video_cards(video_cards)  # удаляет наибольшие элементы.
    display_result(video_cards, result_video_cards)  # выводим результат
