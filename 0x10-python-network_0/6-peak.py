#!/usr/bin/python3
'''a module containing the function (find_peak)'''


def find_peak(nums):
    """finds a peak in a list of unsorted integers."""
    if nums is None or len(nums) == 0:
        return None
    if len(nums) < 3:
        return max(nums)

    mid_idx = len(nums) // 2
    mid = nums[mid_idx]
    if mid > nums[mid_idx - 1] and mid > nums[mid_idx + 1]:
        return mid
    if mid < nums[mid_idx - 1]:
        return find_peak(nums[:mid_idx])
    return find_peak(nums[mid_idx + 1:])
