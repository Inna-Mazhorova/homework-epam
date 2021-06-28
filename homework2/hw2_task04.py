from typing import Callable

"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""


def func(a, b):
    return (a ** b) ** 2


def decorate(func: Callable) -> Callable:
    cache = {}

    def cache_func(*some):
        if some in cache:
            return cache[some]
        else:
            cache[some] = func(*some)
            return cache[some]

    return cache_func
