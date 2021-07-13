# I decided to write a code that generates data filtering object from a list of keyword parameters:


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):
        return [item for item in data if all(i(item) for i in self.functions)]


# example of usage:
positive_even = Filter(
    [lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)]
)


def make_filter(**keywords):
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():

        def keyword_filter_func(fvalue):
            return fvalue[key] == value

        filter_funcs.append(keyword_filter_func)
    return Filter(filter_funcs)


# There are multiple bugs in this code. Find them all and write tests for faulty cases.
