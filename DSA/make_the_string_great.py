"""
Given a string s of lower and upper case English letters.
A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
* 0 <= i <= s.length - 2
* s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them.
You can keep doing this until the string becomes good.
Return the string after making it good.
Notice that an empty string is also good.
"""

def makeGood(s: str) -> str:
    i = 0
        
    small = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    capital = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    st = []
        
    for c in s:
        if not st:
            st.append(c)
        else:
            if (c.upper()==st[-1].upper()) and ((c in small and st[-1] in capital) or (c in capital and st[-1] in small)):
                st.pop()
            else:
                st.append(c)
        
    return "".join(st)



s = "leEeetcode"
print(makeGood(s))
