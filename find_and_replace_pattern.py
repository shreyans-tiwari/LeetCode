"""
Given a list of strings words and a string pattern, return a list of words[i] that match pattern.
You may return the answer in any order.
A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the
pattern with p(x), we get the desired word.
Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter,
and no two letters map to the same letter.
"""

words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"

res = []
map_p_t = {}

for i, p in enumerate(pattern):
    if p in map_p_t:
        map_p_t[p].append(i)
    else:
        map_p_t[p] = [i]

map_p = {}
for k in map_p_t:
    map_p[tuple(map_p_t[k])] = k

for w in words:
    map_w = {}
    f = 1

    if len(w) != len(pattern):
        continue

    for i, c in enumerate(w):
        if c in map_w:
            map_w[c].append(i)
        else:
            map_w[c] = [i]

    for k in map_w:
        if tuple(map_w[k]) not in map_p:
            f = 0
            break

    if f:
        res.append(w)

print(res)