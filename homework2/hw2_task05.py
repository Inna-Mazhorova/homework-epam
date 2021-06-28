import string
from typing import Any, List

# Some of the functions have a bit cumbersome behavior when we deal with
# positional and keyword arguments.
# Write a function that accept any iterable of unique values and then
# it behaves as range function:
# import string
# assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
# assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
# assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']


dict_ascii = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
}


def custom_range(his_ascii: str, fakestop: str, *args: List[Any]) -> List[str]:
    if len(args) > 2:
        raise Exception("funcion expects 2, 3 or 4 arguments only")
    elif len(args) == 2:
        start = fakestop
        step = args[1]
        stop = args[0]
    elif len(args) == 1:
        start = fakestop
        step = 1
        stop = args[0]
    else:
        start = "a"
        step = 1
        stop = fakestop
    stop_num = dict_ascii[stop]
    start_num = dict_ascii[start]
    counter = start_num
    result = []
    if step >= 0:
        while counter < stop_num:
            result.append(string.ascii_lowercase[counter])
            counter += step
        return result
    else:
        while counter > stop_num:
            result.append(string.ascii_lowercase[counter])
            counter += step
        return result
