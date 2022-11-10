"""
You are given a string s consisting of lowercase English letters.
A duplicate removal consists of choosing two adjacent and equal letters and removing them.
We repeatedly make duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made.
"""

def removeDuplicates(s: str) -> str:
    ans = []

    for c in s:
        if not ans:
            ans.append(c)
        else:
            if ans[-1] == c:
                ans.pop()
            else:
                ans.append(c)
        
    return "".join(ans)


s = "azxxzy"
print(removeDuplicates(s))
