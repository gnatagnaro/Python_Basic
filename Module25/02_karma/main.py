from random import randint


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day():
    karma_points = randint(1, 7)
    chance = randint(1, 10)
    if chance == 1:
        rand_error = randint(1, 5)
        if rand_error == 1:
            raise KillError('ошибка уничтожения')
        elif rand_error == 2:
            raise DrunkError('пьяная ошибка')
        elif rand_error == 3:
            raise CarCrashError('ошибка при автомобильной аварии')
        elif rand_error == 4:
            raise GluttonyError('ошибка обжорства')
        else:
            raise DepressionError('ошибка депрессии')
    return karma_points


with open('karma.log', 'w', encoding='utf-8') as file:
    summ = 0
    while True:
        try:
            summ += one_day()
            if summ == 500:
                break
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as exc:
            file.write(exc + '' + type(exc))


class DivisionError(Exception):
    pass


with open("numbers.txt", "r", encoding="utf8") as file:
    for line in file:
        try:
            clear_line = line.rstrip()
            first, second = clear_line.split()
            if int(first) < int(second):
                raise DivisionError("нельзя делить большее на меньшее")
        except (ValueError, DivisionError) as exc:
            print(exc, type(exc), first, second)
