from typing import Callable, Any
import functools


def how_are_you(func: Callable) -> Callable:
    """
    Декоратор, который при вызове декорируемой функции задает вопрос и требует ответа.
    :param func:
    :return:
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        return func(*args, **kwargs)
    return wrapped_func


@how_are_you
def test() -> None:
    """Функция для теста."""
    print('<Тут что-то происходит...>')


test()
