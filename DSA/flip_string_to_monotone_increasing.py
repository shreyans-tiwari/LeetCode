"""
A binary string is monotone increasing if it consists of some number of 0's (possibly none),
followed by some number of 1's (also possibly none).
You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.
Return the minimum number of flips to make s monotone increasing.
"""

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        Count no. of 1's to flip on LHS + no. of 0's to flip on RHS for each index i and return minimum no. of flips.
        """
        n_0 = 0
        n_1 = 1

        for c in s:
            if c == '0':
                n_0 += 1
            else:
                n_1 += 1
        
        n_1_left = 0
        n_0_right = n_0
        res = len(s)
        
        for c in s:
            if c == '0':
                n_0_right -= 1
            if n_0_right + n_1_left < res:
                res = n_0_right + n_1_left
            if c == '1':
                n_1_left += 1
        
        return res
            
