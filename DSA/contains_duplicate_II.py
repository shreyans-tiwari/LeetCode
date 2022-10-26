"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such
that nums[i] == nums[j] and abs(i - j) <= k.
"""


def containsNearbyDuplicate(nums, k):
    freq = {}
    for i, n in enumerate(nums):
        if n in freq:
            if abs(i - freq[n]) <= k:
                return True
            else:
                freq[n] = i
        else:
            freq[n] = i

    return False


nums = [1, 2, 3, 1]
k = 3
print(containsNearbyDuplicate(nums, k))
