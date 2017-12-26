def frequencySort(s):
    from collections import Counter
    d = Counter(s)
    l = sorted(d.values())
    s = ''
    for i in l[::-1]:
        for k in d:
            if d[k] == i:
                s += k*i
                d[k] = 0
    return s
        
