"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace
and initial word order.
"""


def reverseWords(s: str) -> str:
    output = s.split()
    for i, o in enumerate(output):
        output[i] = o[::-1]
    return " ".join(output)


print(reverseWords("Let's take LeetCode contest"))
print(reverseWords("God Ding"))