import functools
import pickle

# In previous homework task 4, you wrote a cache function that remembers other function output value.
# Modify it to be a parametrized decorator, so that the following code:
# Would give out cached value up to times number only. Example:


def cache(times=3):
    def wrapper_count_times(func):
        memo = {}

        @functools.wraps(func)
        def count_times(*args, **kwargs):
            count_times.num_times += 1
            hash = pickle.dumps(args)

            if count_times.num_times == 1:
                memo[hash] = func(*args)
                print("Writing to cache")
                return memo[hash]
            elif 2 <= count_times.num_times <= times:
                print("From cache")
                try:
                    return memo[hash]
                except:
                    memo[hash] = func(*args)
                    print("Writing to cache")
                    return memo[hash]
            else:
                result = func(*args)
                return result
            return func(*args)

        count_times.num_times = 0
        return count_times

    return wrapper_count_times


@cache(times=3)
def our_function():
    func_output = input("? ")
    return func_output
