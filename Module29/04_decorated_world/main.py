import functools
from typing import Callable, Any


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    """Декоратор для декораторов: декорирует другой декоратор."""
    @functools.wraps(decorator)
    def decorated_deco(*args, **kwargs) -> Callable:
        def deco_wrapper(func: Callable) -> Callable:
            return decorator(func, *args, **kwargs)
        return deco_wrapper
    return decorated_deco


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:
    """Декоратор, обрабатывающий обычную функцию."""
    @functools.wraps(func)
    def wrapped(*func_args, **func_kwargs) -> Callable:
        print(f'Переданные арги и кварги в декоратор: {dec_args}, {dec_kwargs}')
        res = func(*func_args, **func_kwargs)
        return res
    return wrapped


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет,", text, num)


decorated_function("Юзер", 101)
