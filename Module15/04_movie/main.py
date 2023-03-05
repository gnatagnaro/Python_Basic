def get_input_parameters():
    films = []
    count = int(input('Сколько фильмов хотите добавить? '))

    for film in range(count):
        name = input('Введите название фильма: ')
        films.append(name)

    return films

def display_result(favorite_films, errors):
    """
    Выводим список ошибок и список любимых фильмов

    :param favorite_films: список любимых фильмов, например: ["Леон", "Мементо"]
    :type favorite_films: List[str]
    :param errors: список ненайденных фильмов, например: ["Безумный Макс", "Царь горы"]
    :type errors: List[str]
    """
    # TODO: в этой функции пишем весь необходимый код
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем
    print('Ваш список любимых фильмов:', favorite_films)
    print('Список ненайденных фильмов:', errors)


def add_favorite_film(new_favorite_films, available_films):
    my_films = []
    error_films = []

    for i in range(len(new_favorite_films)):
        if new_favorite_films[i] in available_films:
            my_films.append(new_favorite_films[i])
        else:
            print(f'Ошибка: фильма {new_favorite_films[i]} у нас нет :(')
            error_films.append(new_favorite_films[i])
    return my_films, error_films


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    available_films = [
        "Крепкий орешек", "Назад в будущее", "Таксист",
        "Леон", "Богемская рапсодия", "Город грехов",
        "Мементо", "Отступники", "Деревня"
    ]
    new_favorite_films = get_input_parameters()  # получаем параметры
    favorite_films, errors = add_favorite_film(new_favorite_films, available_films)  #добавлем фильмы в список "любимых"
    display_result(favorite_films, errors)  # выводим результат
