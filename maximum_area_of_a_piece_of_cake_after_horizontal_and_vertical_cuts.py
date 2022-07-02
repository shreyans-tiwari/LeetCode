"""
You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:
* horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
* verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the
arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 10^9 + 7.
"""

h = 5
w = 4
horizontalCuts = [3, 1]
verticalCuts = [1]

horizontalCuts.append(0)
horizontalCuts.append(h)
verticalCuts.append(0)
verticalCuts.append(w)

horizontalCuts.sort()
verticalCuts.sort()
max_h = 0
max_v = 0

for i in range(len(horizontalCuts) - 1):
    max_h = max(max_h, (horizontalCuts[i + 1] - horizontalCuts[i]))
for i in range(len(verticalCuts) - 1):
    max_v = max(max_v, verticalCuts[i + 1] - verticalCuts[i])

print((max_v * max_h) % (10 ** 9 + 7))
