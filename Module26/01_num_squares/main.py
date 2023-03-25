from collections.abc import Iterable
from typing import Iterator


n = int(input('Введите число N: '))

print('\nКласс-итератор: ')


class Squares:
    def __init__(self, count: int) -> None:
        self.count = count
        self.start = 1

    def __iter__(self) -> Iterator[int]:  # какую аннотацию здесь нужно написать?
        return self

    def __next__(self) -> int:
        if self.count >= self.start:
            res = self.start ** 2
            self.start += 1
            return res
        else:
            raise StopIteration('Ошибка итерации')


sequence = Squares(n)
print('Последовательность:', end=' ')
for elem in sequence:
    print(elem, end=' ')


print('\n\nФункция-генератор: ')


def squares_generator(var: int) -> Iterable[int]:
    cur = 1
    while var >= cur:
        yield cur ** 2
        cur += 1


print('Последовательность:', end=' ')
for elem in squares_generator(n):
    print(elem, end=' ')

print('\n\nГенераторное выражение: ')

squares = (elem ** 2 for elem in range(1, n + 1))

print('Последовательность:', end=' ')
for i in squares:
    print(i, end=' ')
