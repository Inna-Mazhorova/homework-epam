from homework5 import hw5_task02


def test_wraps_works_properly():
    assert (
        hw5_task02.custom_sum.__doc__
        == "This function can sum any objects which have __add___"
    )
    assert hw5_task02.custom_sum.__name__ == "custom_sum"
