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
            if summ >= 500:
                break
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as exc:
            file.write(str(exc) + ' ' + str(type(exc)) + '\n')
