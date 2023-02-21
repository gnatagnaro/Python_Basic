def move(n, x, y):
    if n == 1:
        print("Перенести диск 1 со стержня", x, "на стержень", y)
    else:
        temp = 6 - x - y  # Вспомогательный колышек
        move(n - 1, x, temp)
        print("Перенести диск", n, "со стержня", x, "на стержень", y)
        move(n - 1, temp, y)


move(2, 1, 3)
