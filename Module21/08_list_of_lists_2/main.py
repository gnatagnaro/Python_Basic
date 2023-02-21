# видоизменил функцию нахождения суммы, и все работает по той же логике, но уже со списком
# подскажите, пожалуйста, как еще можно было реализовать эту и предыдущую задачи?
# возможно, кто-то предлагал более логичные/быстрые/короткие варианты?

def sum(*args):
    if not any(type(arg) == list for arg in args):
        result = list()
        for arg in args:
            result.append(arg)
        return result
    unpacked = []
    for arg in args:
        if type(arg) != list:
            unpacked.append(arg)
        else:
            unpacked.extend(arg)
    return sum(*unpacked)


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

# print(sum(nice_list))
