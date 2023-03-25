from typing import Callable, Any
import time
import functools


def wait_deco(func: Callable) -> Callable:
    """Декоратор, ожидающий несколько секунд перед выполнением декорируемой функции."""
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        start = time.time()
        time.sleep(5)
        end = time.time()
        print(f'программа ждет 5 секунд: {end - start}')
        return func(*args, **kwargs)
    return wrapped_func


@wait_deco
def my_func() -> None:
    """Функция для теста."""
    print('smthing')


my_func()
