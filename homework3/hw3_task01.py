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
            hash = pickle.dumps(args)
            if hash not in memo:
                memo[hash] = func(*args)
                # print("Writing to cache")
                return memo[hash]
            nonlocal times_called
            times_called += 1
            if times_called >= times:
                del memo[hash]
                times_called = 0
                # print("Deliting from cache, Число вызовов", times_called)
                memo[hash] = func(*args)
                return memo[hash]
            else:
                # print("From cache, Число вызовов", times_called)
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
