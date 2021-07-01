from homework3 import hw3_task01


def test_cache_remembers():
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
