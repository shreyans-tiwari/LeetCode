"""
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros.
For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.
Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers
needed so that they sum up to n.
"""

n = "27346209830709182346"

dict_digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
max_dgt = 0
for d in n:
    if dict_digit[d] > max_dgt:
        max_dgt = dict_digit[d]
    if max_dgt == 9:
        break
print(max_dgt)

# Leet Code 1 line solution:
# return int(max(n))
# Somehow it is faster than my implementation.
