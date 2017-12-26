def groupAnagrams(self, strs):
    d = {}
    l = []
    index = 0
    from collections import Counter
    for s in strs:
        t = tuple(sorted([x for x in s]))
        if t in d:
            l[d[t]].append(s)
        else:
            d[t] = index
            l.append([s])
            index += 1
    return l
