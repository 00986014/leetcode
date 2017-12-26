def lengthOfLongestSubstring(s):
    A = set()
    l, r = 0, -1
    result = 0
    while l<len(s):
        if r+1<len(s) and s[r+1] not in A:
            r += 1
            A.add(s[r])
        else:
            A.remove(s[l])
            l += 1

        result = max(result, r-l+1)

    return result
