from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    counter = 0
    max_sum = nums[0]
    while k > 1:
        while counter + k <= len(nums):
            sum_iteration = sum(nums[counter : counter + k])
            if sum_iteration > max_sum:
                max_sum = sum_iteration
            counter += 1
        k -= 1
    return max_sum
