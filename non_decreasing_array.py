"""
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one
element.
We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
"""
nums = [1, 2, 4, 5, 3]
res = True
cnt_violations = 0

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        if cnt_violations == 1:
            res = False
        cnt_violations += 1
        if i >= 2 and nums[i-2] > nums[i]:
            nums[i] = nums[i-1]

print(res)
