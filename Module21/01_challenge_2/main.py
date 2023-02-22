def func(num):
    if num <= 0:
        return num
    func(num - 1)
    print(num)


numb = int(input('Введите число: '))
func(numb)
