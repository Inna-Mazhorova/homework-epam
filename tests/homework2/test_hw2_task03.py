from homework2.hw2_task03 import combinations_list


def test_combinations_list():
    assert combinations_list([1, 2], [3, 4]) == [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
    ]
