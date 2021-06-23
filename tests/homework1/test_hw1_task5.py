from homework1.task05.hw1_task05 import find_maximal_subarray_sum


def test_find_maximal_subarray_sum():
    assert find_maximal_subarray_sum(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3) == 18


test_find_maximal_subarray_sum()
