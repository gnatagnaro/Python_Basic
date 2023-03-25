from typing import Callable, Any
from datetime import datetime
import functools


def logging(func: Callable) -> Callable:
    """
    Декоратор, логирующий работу кода.
    :param func:
    :return: wrapped_logging
    """
    @functools.wraps(func)
    def wrapped_logging(*args, **kwargs) -> Callable:
        with open('functions_errors.log', 'a', encoding='utf-8') as file:
            try:
                print(f'\nВызывается функция {func.__name__};\n'
                      f'Документация: {func.__doc__};\n'
                      f'Позиционные аргументы: {args};\n'
                      f'Именованные аргументы: {kwargs}.\n')
                return func(*args, **kwargs)
            except Exception as exc:
                file.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} '
                           f'Ошибка в функции {func.__name__}: {type(exc)}\n')
    return wrapped_logging


@logging
def my_func() -> None:
    """Функция для теста"""
    print('smthing')
    print(int('smthing'))  # для теста логирования ошибок


@logging
def divide(x: Any, y: Any) -> int:
    """Функция выполняет деление чисел"""
    return x/y


@logging
def multiply(x: Any, y: Any) -> Any:
    """Функция выполняет умножение чисел"""
    return x*y


print(divide(10, 0))
print(multiply(2, 'test'))
my_func()
