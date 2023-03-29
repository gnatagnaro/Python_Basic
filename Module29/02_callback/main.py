import functools
from typing import Any, Callable, Optional

app = dict()


def callback(_func: Optional[Callable] = None, *, var: str = None) -> Callable:
    """Функция обратного вызова, вызывается при срабатывании события."""
    def deco(func: Callable) -> Callable:
        app[var] = func

        @functools.wraps(func)
        def wrapped(*args, **kwargs) -> Any:
            return func(*args, **kwargs)
        return wrapped
    if _func is None:
        return deco
    return deco(_func)


@callback(var='//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

print(app)
