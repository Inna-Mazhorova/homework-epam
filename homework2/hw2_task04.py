import os
import pickle

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


def cached(cachefile):
    # A function that creates a decorator which will use "cachefile" for caching the results of the decorated function
    def decorator(func):
        def wrapped(*args, **kwargs):
            # if cache exists -> load it and return its content
            if os.path.exists(cachefile):
                with open(cachefile, "rb") as cachehandle:
                    print("using cached result from '%s'" % cachefile)
                    return pickle.load(cachehandle)
            result = func(*args, **kwargs)
            # write to cache file
            with open(cachefile, "wb") as cachehandle:
                print("saving result to cache '%s'" % cachefile)
                pickle.dump(result, cachehandle)
            return result

        return wrapped

    return decorator


@cached("function_square.pickle")
def function_square(a, b):
    return (a ** b) ** 2
