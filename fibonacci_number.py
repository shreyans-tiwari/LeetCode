"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number
is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""

"""
# Recursion Solution
def fib(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1

    return fib(n-1)+fib(n-2)
"""
"""
# Iterative Solution
def fib(n: int) -> int:
    if n < 2:
        return n
    if n == 2:
        return 1

    x = 1
    y = 1

    for i in range(2, n):
        t = x + y
        x = y
        y = t

    return y
"""


def fib(n: int) -> int:
    # Dynamic Programming Solution
    dp = [0, 1]

    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])

    return dp[n]


print(fib(4))
