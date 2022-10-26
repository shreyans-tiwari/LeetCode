"""
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
In one move, you can increment or decrement an element of the array by 1.
Test cases are designed so that the answer will fit in a 32-bit integer.
"""

nums = [1, 10, 2, 9]
nums.sort()
res = 0

if len(nums) % 2 == 1:
    mid = len(nums) // 2
    for i, num in enumerate(nums):
        if i < mid:
            res += nums[mid] - num
        else:
            res += num - nums[mid]
else:
    mid1 = (len(nums) // 2) - 1
    mid2 = len(nums) // 2
    t1 = t2 = 0
    for i, num in enumerate(nums):
        if i < mid1:
            t1 += nums[mid1] - num
        else:
            t1 += num - nums[mid1]
        if i < mid2:
            t2 += nums[mid2] - num
        else:
            t2 += num - nums[mid2]
    res = min(t1, t2)

print(res)