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
