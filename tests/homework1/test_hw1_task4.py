from homework1.task04.hw1_task04 import check_sum_of_four


def test_check_sum_of_four():
    one = [2, 2, -1]
    two = [3, 5, -2]
    three = [4, 5, 0]
    four = [-1, 3, 6]
    assert check_sum_of_four(one, two, three, four) == 2
