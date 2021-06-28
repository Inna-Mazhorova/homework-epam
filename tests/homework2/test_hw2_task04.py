from homework2.hw2_task04 import decorate, func


def test_cache():
    cache_func = decorate(func)
    some = 100, 200
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2
