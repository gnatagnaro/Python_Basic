import functools
from time import time
from datetime import datetime
from typing import Any, Callable


def logged(func: Callable, cls, date_format: str) -> Callable:
    """Декоратор, логирующий время запуска и завершения методов класса."""
    @functools.wraps(func)
    def wrapped(*args, **kwargs) -> Any:
        start = time()
        print(f"- Запуск '{cls.__name__}.{func.__name__}'. Дата и время запуска:", datetime.now().strftime(date_format))
        func(*args, **kwargs)
        print(f"- Завершение '{cls.__name__}.{func.__name__}', время работы = {time() - start:0.3f}s")
        return
    return wrapped


def log_methods(date_format: str) -> Callable:
    """Декоратор, принимающий формат даты и проверяющий методы класса."""
    def deco(cls):
        for i_method in dir(cls):
            if i_method.startswith('__'):
                continue
            a = getattr(cls, i_method)
            if hasattr(a, '__call__'):
                decorated_a = logged(a, cls, date_format)
                setattr(cls, i_method, decorated_a)
        return cls
    return deco


@log_methods("%b %d %Y — %H:%M:%S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


@log_methods("%b %d %Y — %H:%M:%S")
class B(A):
    def test_sum_1(self) -> None:
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self) -> int:
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()

# - Запускается 'B.test_sum_1'. Дата и время запуска: Apr 23 2021 - 21:50:37
# - Запускается 'A.test_sum_1'. Дата и время запуска: Apr 23 2021 - 21:50:37
# Тут метод test_sum_1
# - Завершение 'A.test_sum_1', время работы = 0.187s
# Тут метод test_sum_1 у наследника
# - Завершение 'B.test_sum_1', время работы = 0.187s
# - Запускается 'B.test_sum_2'. Дата и время запуска: Apr 23 2021 - 21:50:37
# Тут метод test_sum_2 у наследника
# - Завершение 'B.test_sum_2', время работы = 0.370s
