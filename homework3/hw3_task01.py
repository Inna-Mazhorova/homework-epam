import functools
import pickle

# In previous homework task 4, you wrote a cache function that remembers other function output value.
# Modify it to be a parametrized decorator, so that the following code:
# Would give out cached value up to times number only. Example:


def cache(times=3):
    def wrapper_count_times(func):
        memo = {}
        times_called = 0

        @functools.wraps(func)
        def count_times(*args, **kwargs):
            nonlocal times_called
            times_called += 1
            hash = pickle.dumps(args)

            if times == 0:
                result = func(*args)
                return result
            elif hash not in memo:
                print("Writing to cache", times_called)
                memo[hash] = func(*args)
                return memo[hash]
            elif times_called == (times + 1):
                print("Deleting from cache", times_called)
                result = func(*args)
                del memo[hash]
                times_called = 1
                return result
            else:
                print("Число вызовов", times_called)
                return memo[hash]

        return count_times

    return wrapper_count_times


@cache(times=3)
def our_function():
    func_output = input("? ")
    return func_output


@cache(times=3)
def func_quadro(x):
    func_output = x * x
    return func_output
