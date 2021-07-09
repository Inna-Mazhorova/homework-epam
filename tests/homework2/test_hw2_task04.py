from homework2 import hw2_task04


def test_cache():
    val1 = hw2_task04.func_square(100, 200)
    val2 = hw2_task04.func_square(100, 200)
    val3 = hw2_task04.func_square(4, 2)
    val4 = hw2_task04.func_square(100, 200)
    assert val1 == val2
    assert not val2 == val3
    assert val1 == val4
