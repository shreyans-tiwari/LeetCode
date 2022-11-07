"""
You are given a positive integer num consisting only of digits 6 and 9.
Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
"""

num = 9996
n = num
l = []
n_digit = ans = 0

while n > 0:
    l.insert(0, (n % 10))
    n = n // 10
    n_digit += 1

for i, v in enumerate(l):
    if v == 6:
        l[i] = 9
        break
        
for i in l:
    ans += i*(10**(n_digit-1))
    n_digit -= 1
        
print(ans)
