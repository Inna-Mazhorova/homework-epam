import time
from typing import Generator, List

"""
This task is optional.
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.
Definition of done:
 - function is created
 - function is properly formatted
 - function has tests
"""

"""
def fizz_buzz(n: int):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        else:
            yield str(i)

print(list(fizz_buzz(20)))
"""


def inf_seq():
    num = 0
    while True:
        yield num
        num += 1


fizz_buzz_generator = (
    (lambda x: {1: x, 6: "Fizz", 10: "Buzz", 0: "FizzBuzz"}[x ** 4 % 15])(n + 1)
    for n in inf_seq()
)

k = 20
array = [next(fizz_buzz_generator) for i in range(k)]
print(array)
