def slicer(my_tuple, rand_el):
    new_tuple = tuple()
    x = [my_tuple[:i+1] for i, j in enumerate(my_tuple) if j == rand_el]
    if my_tuple.count(rand_el) >= 2:
        new_tuple = x[1][1:]
    elif my_tuple.count(rand_el) == 1:
        x = [my_tuple[i:] for i, j in enumerate(my_tuple) if j == rand_el]
        new_tuple = x[0]

    return new_tuple


# print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
# Ответ в консоли: (2, 3, 4, 5, 6, 7, 8, 2)

# еще один вариант:
# def slicer(t, n):
#     if n not in t:
#         return ()
#     if t.count(n) == 1:
#         return t[t.index(n):]
#     return t[t.index(n):t.index(n, t.index(n) + 1) + 1]
#
#
# print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))

