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


def test_cache_remembers_4_times():
    times_called = 0

    @hw3_task01.cache(times=4)
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
