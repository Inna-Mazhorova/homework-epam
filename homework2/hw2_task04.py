import pickle
from typing import Callable

# Write a function that accepts another function as an argument. Then it
# should return such a function, so the every call to initial one
# should be cached.


# def func(a, b):
#   return (a ** b) ** 2
# cache_func = cache(func)
# some = 100, 200
# val_1 = cache_func(*some)
# val_2 = cache_func(*some)
# assert val_1 is val_2


def cache(func: Callable) -> Callable:
    cachedict = {}

    def cachefunc(*args):
        hash = pickle.dumps(args)
        if hash not in cachedict:
            print("Writing to cache")
            cachedict[hash] = func(*args)
        return cachedict[hash]

    return cachefunc


@cache
def func_square(a, b):
    return (a ** b) ** 2
