"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
return the maximum number of points that lie on the same straight line.
"""

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        max_p = 0
        for i in range(len(points)):
            slope = {}
            for j in range(i+1, len(points)):
                if points[j][1]-points[i][1] == 0 and points[j][0]-points[i][0] == 0:
                    if 0 in slope:
                        slope[0] += 1
                    else:
                        slope[0] = 2
                    if 'inf' in slope:
                        slope['inf'] += 1
                    else:
                        slope['inf'] = 2
                    if slope[0] > max_p:
                        max_p = slope[0]
                    if slope['inf'] > max_p:
                        max_p = slope['inf']
                elif points[j][0]-points[i][0] == 0:
                    if 'inf' in slope:
                        slope['inf'] += 1
                    else:
                        slope['inf'] = 2
                    if slope['inf'] > max_p:
                        max_p = slope['inf']
                else:
                    s = (points[j][1]-points[i][1]) / (points[j][0]-points[i][0])
                    if s in slope:
                        slope[s] += 1
                    else:
                        slope[s] = 2
                    if slope[s] > max_p:
                            max_p = slope[s]
        return max_p
