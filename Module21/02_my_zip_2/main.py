# подскажите, пожалуйста, как еще можно было реализовать данную функцию?
def my_zip(*args):
    length = min(len(element) for element in args)
    tpl_list = [tuple(struct[i] for struct in map(list, args)) for i in range(length)]
    return tpl_list


a = [{"x": 4}, "b", "z", "d"]
b = (10, {20}, [30], "z")
print(my_zip(a, b))

a = [1, 2, 3, 4, 5]
b = {1: "s", 2: "q", 3: 4}
x = (1, 2, 3, 4, 5)
print(my_zip(a, b, x))


# def shortest_sequence_range(*args):  # функция определения длинны кратчайшей последовательности
#     return range(len(sorted(args, key=len)[0]))  # сортируем переданные аргументы по длине и берём длину самой короткой
#
#
# def my_zip(first, second):
#     # делаем цикл равный длине самой короткой последовательности и берём каждый i-й из каждой последовательности
#     ans = ((first[i], second[i]) for i in shortest_sequence_range(first, second))
#     return ans
