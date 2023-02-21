# как иначе можно реализовать данную программу?

def search_element(data, tag, depth=None):
    result = None
    if depth is None or depth >= 1:
        if tag in data:
            return data[tag]
    else:
        return None
    for key, value in data.items():
        if isinstance(value, dict):
            if depth is not None:
                result = search_element(value, tag, depth - 1)
                if result:
                    break
            else:
                result = search_element(value, tag)
    return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

search_key = input("Введите искомый ключ: ")
req = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if req == 'y':
    max_depth = int(input('Введите максимальную глубину: '))
    value = search_element(site, search_key, max_depth)
else:
    value = search_element(site, search_key)
print("Значение:", value)
