def groupAnagrams(strs):
    words = {}

    for s in strs:
        k = str(sorted(s))
        if k in words:
            words[k].append(s)
        else:
            words[k] = [s]
        
    return words.values()


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
