def findAnagrams(self, s, p):
    from collections import Counter
    length = len(p)
    l = []
    Cp = Counter(p)
    Cs = Counter(s[:length])
    if Cs == Cp:
        l.append(0)
    for i in xrange(1, len(s)-length+1):
        Cs[s[i-1]] -= 1
        if Cs[s[i-1]] == 0:
            del Cs[s[i-1]]
        Cs[s[i+length-1]] += 1
        if Cs == Cp:
            l.append(i)
    return l
