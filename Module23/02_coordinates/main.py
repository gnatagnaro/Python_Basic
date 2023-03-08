import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


try:
    with open('coordinates.txt', 'r', encoding='utf-8') as file, \
            open('result.txt', 'w', encoding='utf-8') as file_2:
        for line in file:
            try:
                nums_list = line.split()
                res1 = f(int(nums_list[0]), int(nums_list[1]))
                res2 = f2(int(nums_list[0]), int(nums_list[1]))
                number = random.randint(0, 100)
                my_list = sorted([str(res1), str(res2), str(number)])
                file_2.write(' '.join(my_list) + '\n')
            except Exception as ex:
                print(type(ex), ex)
except Exception as e:
    print(type(e), e)
