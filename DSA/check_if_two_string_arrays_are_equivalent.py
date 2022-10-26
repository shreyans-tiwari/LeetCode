"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
"""

word1 = ["ab", "c"]
word2 = ["a", "bc"]

s1 = "".join(word1)
s2 = "".join(word2)

if s1 == s2:
    print(True)
else:
    print(False)