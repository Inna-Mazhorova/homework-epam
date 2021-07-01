import functools

# In previous homework task 4, you wrote a cache function that remembers other function output value.
# Modify it to be a parametrized decorator, so that the following code:
# Would give out cached value up to times number only. Example:


def cache(times):
    def count_times(func):
        memo = []

        @functools.wraps(func)
        def wrapper_count_times(*args, **kwargs):
            wrapper_count_times.num_times += 1

            if wrapper_count_times.num_times == 1:
                result = func(*args, **kwargs)
                memo.append(result)
                return result
            elif (wrapper_count_times.num_times >= 2) and (
                wrapper_count_times.num_times <= times
            ):
                return memo[0]
            else:
                result = func(*args, **kwargs)
                return result
            return func(*args, **kwargs)

        wrapper_count_times.num_times = 0
        return wrapper_count_times

    return count_times


@cache(times=3)
def our_function():
    func_output = input("? ")
    return func_output
