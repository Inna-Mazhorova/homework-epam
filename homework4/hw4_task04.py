from typing import List

"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
"""


def fizzbuzz(number: int) -> List[str]:
    """
    Return true if List is fizzbuzz
    >>> fizzbuzz(20) == [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz', 16, 17, 'fizz', 19, 'buzz']
    True

    Return false if List is not fizzbuzz
    >>> fizzbuzz(20) == [1, 2, 'fizz', 4, 5, 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz', 16, 17, 'fizz', 19, 'buzz']
    False

    """

    result = []
    for i in range(1, number + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            result.append("fizzbuzz")
        elif i % 3 == 0:
            result.append("fizz")
        elif i % 5 == 0:
            result.append("buzz")
        else:
            result.append(i)
    return result
