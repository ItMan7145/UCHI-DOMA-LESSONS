import functools
import time
from typing import Callable, Any


def timer(func: Callable, *args, **kwargs) -> Any:
    """Декоратор"""

    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        start_t = time.time()
        result = func(*args, **kwargs)
        print(*args, **kwargs)
        end_t = time.time()
        run_t = round(end_t - start_t, 4)
        print(f'Функция работала {run_t} секунд')
        return result

    return wrapper_func


def login(func: callable, *args, **kwargs):
    def wrapper_func(*args, **kwargs):
        print(f'Вызываемая функция: {func.__name__}. \n Позициованные аргументы: {args}.'
              f' \n Именованные аргументы: {kwargs} \n')

        result = func(*args, **kwargs)
        return result

    return wrapper_func


@login()
@timer
def squares_sum() -> int:
    num = 100
    result = 0
    for n in range(1, num + 1):
        result += sum([n ** 2 for x in range(1000)])
    return result


@timer
@login()
def cube_sum(a):
    result = 0
    for n in range(1, a + 1):
        result += sum([n ** 3 for x in range(1000)])
    return result


# result1 = timer(squares_sum)
# print(result1)
#
# result2 = timer(cube_sum, 100)
# print(result2)

print(squares_sum())
print(cube_sum(150))
