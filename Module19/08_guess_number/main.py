numbers = int(input('Введите максимальное число: '))
all_nums = set(range(1, numbers + 1))

while True:
    guess = input('Нужное число есть среди вот этих чисел: ').title()
    if guess == 'Помогите!':
        break
    guess = {int(x) for x in guess.split()}
    answer = input('Ответ Артёма: ').title()
    # print(all_nums)
    if answer == 'Да':
        all_nums &= guess
        # all_nums.intersection_update(guess)
        # print(all_nums)
    else:
        all_nums -= guess
        # print(all_nums)
        # all_nums.difference_update(guess)

print(*all_nums)
