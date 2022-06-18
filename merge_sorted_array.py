nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

i, j = m, 0
while i < m+n:
    nums1[i] = nums2[j]
    j += 1
    i += 1
nums1.sort()
print(nums1)
