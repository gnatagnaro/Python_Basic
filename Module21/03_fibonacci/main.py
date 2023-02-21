def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


numb = int(input('Введите позицию числа в ряде Фибоначчи: '))
print('Число:', fib(numb))
