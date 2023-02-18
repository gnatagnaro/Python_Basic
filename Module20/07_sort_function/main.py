def tpl_sort(*my_tuple):
    if not int() in my_tuple:
        return tuple(my_tuple)
    return tuple(sorted(my_tuple))


# print(tpl_sort(6, 3, -1, 8, 4, 10, -5, 'ff', [1, 2, 3]))
# Ответ в консоли: (-5, -1, 3, 4, 6, 8, 10)
