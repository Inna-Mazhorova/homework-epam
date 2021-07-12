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

            if times_called == 1:
                memo[hash] = func(*args)
                print("Writing to cache")
                return memo[hash]
            elif 2 <= times_called <= times:
                print("From cache")
                try:
                    return memo[hash]
                except:
                    memo[hash] = func(*args)
                    print("Writing to cache")
                    times_called -= 1
                    return memo[hash]
            else:
                result = func(*args)
                times_called = 0
                return result

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
