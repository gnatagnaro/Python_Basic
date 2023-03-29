import functools
from typing import Callable, Any, Optional


def check_permission(_func: Optional[Callable] = None, *, var: str = None) -> Callable:
    def deco(func: Callable) -> Callable:
        """Декоратор, проверяющий, есть ли у пользователя доступ к вызываемой функции,
        и если нет, то выдаёт исключение PermissionError."""
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Any:
            if var in user_permissions:
                return func(*args, **kwargs)
            else:
                raise PermissionError(f'У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
        return wrapped_func
    if _func is None:
        return deco
    return deco(_func)


user_permissions = ['admin']


@check_permission(var='admin')
def delete_site() -> None:
    print('Удаляем сайт')


@check_permission(var='user_1')
def add_comment() -> None:
    print('Добавляем комментарий')


delete_site()
add_comment()
