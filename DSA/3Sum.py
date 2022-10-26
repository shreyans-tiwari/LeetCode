"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""

nums = [-1, 0, 1, 2, -1, -4]
res = []
nums.sort()     # Sorting the nums list

for i, a in enumerate(nums):
    if i > 0 and a == nums[i - 1]:      # Eliminating duplicate values
        continue
    l, r = i + 1, len(nums) - 1
    while l < r:        # Using two sum approach
        threeSum = a + nums[l] + nums[r]
        if threeSum > 0:        # Reducing right pointer if sum exceeds 0
            r -= 1
        elif threeSum < 0:      # Incrementing left pointer if sum is less than 0
            l += 1
        else:
            res.append([a, nums[l], nums[r]])   # Putting the correct triplet in result list
            l += 1
            while nums[l] == nums[l - 1] and l < r:     # Eliminating duplicate values
                l += 1

print(res)
