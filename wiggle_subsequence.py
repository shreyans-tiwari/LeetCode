"""
A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive
and negative. The first difference (if one exists) may be either positive or negative.
A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining
elements in their original order.

Given an integer array nums, return the length of the longest wiggle subsequence of nums.
"""
nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
dp = []
res = 0

for i in range(1, len(nums)):
    if nums[i - 1] - nums[i] != 0:
        dp.append(nums[i - 1] - nums[i])

if not dp:
    res =1
else:
    cur = 2
    for i in range(1, len(dp)):
        if (dp[i - 1] < 0 and dp[i] > 0) or (dp[i - 1] > 0 and dp[i] < 0):
            cur += 1

print(cur)
