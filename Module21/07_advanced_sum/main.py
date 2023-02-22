def sum(*args):
    if not any(type(arg) == list for arg in args):
        result = 0
        for arg in args:
            result += arg
        return result
    unpacked = []
    for arg in args:
        if type(arg) != list:
            unpacked.append(arg)
        else:
            unpacked.extend(arg)
    return sum(*unpacked)


# print(sum([[1, 2, [3]], [1], 3]))
# print(sum(1, 2, 3, 4, 5))
#
# def my_sum(*args):
#     total_sum = 0
#     for i_elem in args:
#         if isinstance(i_elem, int):
#             total_sum += i_elem
#         elif isinstance(i_elem, (list, tuple)):
#             for x in i_elem:
#                 total_sum += my_sum(x)
#             # Вложенный цикл можно заменить на одну строку кода
#             # total_sum += my_sum(*i_elem)
#
#     return total_sum
