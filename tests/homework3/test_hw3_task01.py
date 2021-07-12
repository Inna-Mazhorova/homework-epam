from homework3 import hw3_task01


def test_cache_remembers_3_times():
    times_called = 0

    @hw3_task01.cache(times=3)
    def f():
        nonlocal times_called
        times_called += 1
        return times_called

    assert f() == 1
    assert times_called == 1
    assert f() == 1
    assert times_called == 1
    assert f() == 1
    assert times_called == 1
    assert f() == 2
    assert times_called == 2


def test_cache_remembers_zero_times():
    times_called = 0

    @hw3_task01.cache(times=0)
    def f():
        nonlocal times_called
        times_called += 1
        return times_called

    assert f() == 1
    assert times_called == 1
    assert f() == 2
    assert times_called == 2
    assert f() == 3
    assert times_called == 3


def test_cache_remembers_zero_times():
    @hw3_task01.cache(times=2)
    def foo(*args):
        return args[0]

    val1 = foo(1)
    val2 = foo(1)
    val4 = foo(2)
    val3 = foo(1)
    assert val1 is val2
    assert val4 is not val2
