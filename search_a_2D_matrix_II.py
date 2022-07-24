"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
"""

matrix = [[1, 4, 7, 11, 15],
          [2, 5, 8, 12, 19],
          [3, 6, 9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]]
target = 5
res = False

"""
# Naive approach
r, c = len(matrix), len(matrix[0])
for i in range(r):
    l = 0
    u = c - 1
    while l <= u:
        mid = (l + u) // 2
        if matrix[i][mid] == target:
            res = True
            break
        elif matrix[i][mid] < target:
            l = mid + 1
        else:
            u = mid - 1
    if res:
        break

print(res)
"""

# Proper Solution with O(m+n) complexity
i = 0
j = len(matrix[0]) - 1

while i < len(matrix) and j >= 0:
    cur = matrix[i][j]
    if target == cur:
        res = True
        break
    if target > cur:
        i += 1
    if target < cur:
        j -= 1

print(res)
