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


def custom_range(symbols_list: str, fakestop: str, *args: List[Any]) -> List[str]:
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
    stop_num = symbols_list.find(stop)
    start_num = symbols_list.find(start)
    counter = start_num
    result = []
    if step >= 0:
        while counter < stop_num:
            result.append(symbols_list[counter])
            counter += step
        return result
    else:
        while counter > stop_num:
            result.append(symbols_list[counter])
            counter += step
        return result
