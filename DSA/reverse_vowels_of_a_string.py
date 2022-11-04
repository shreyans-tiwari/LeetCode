s = "leetcode"
vowels = ['a','e','i','o','u','A','E','I','O','U']
p1 = 0
p2 = len(s)-1
temp = []
temp[:0] = s

while p1 < p2:
    while p1 < p2 and temp[p1] not in vowels:
        p1 += 1
    while p1 < p2 and temp[p2] not in vowels:
        p2 -= 1
    if p1 < p2:
        temp[p1], temp[p2] = temp[p2], temp[p1]
    p1 += 1
    p2 -= 1
    
print("".join(temp))
