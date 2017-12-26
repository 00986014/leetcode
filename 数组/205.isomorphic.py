def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    d = {}
    for i in xrange(len(s)):
        if t[i] in d.values() and s[i] not in d:
            return False
        if s[i] not in d and t[i] not in d.values():
            d[s[i]] = t[i]
        else:
            if d[s[i]] != t[i]:
                return False
    return True
