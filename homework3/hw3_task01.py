import functools

# In previous homework task 4, you wrote a cache function that remembers other function output value.
# Modify it to be a parametrized decorator, so that the following code:
# Would give out cached value up to times number only. Example:


def cache(times=3):
    def wrapper_count_times(func):
        memo = {}

        @functools.wraps(func)
        def count_times(*args, **kwargs):
            count_times.num_times += 1

            if count_times.num_times == 1:
                memo[args] = func(*args)
                # print("Writing to cache")
                return memo[args]
            elif (count_times.num_times >= 2) and (count_times.num_times <= times):
                # print("From cache")
                try:
                    return memo[args]
                except:
                    memo[args] = func(*args)
                    # print("Writing to cache")
                    return memo[args]
            else:
                result = func(*args, **kwargs)
                return result
            return func(*args, **kwargs)

        count_times.num_times = 0
        return count_times

    return wrapper_count_times


@cache(times=3)
def our_function():
    func_output = input("? ")
    return func_output


@cache(times=3)
def quadro_func(a):
    return a ** 2
