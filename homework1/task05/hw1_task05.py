from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    nums.sort(reverse=True)
    chosen_nums = []
    for i in range(k):
        chosen_nums.append(nums[i])
    return sum(chosen_nums)
