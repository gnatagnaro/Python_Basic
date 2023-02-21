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
