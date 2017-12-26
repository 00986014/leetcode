def minWindow(s, t):
    from collections import Counter
    Ct = Counter(t)
    Cs = Counter('')
    for k in Ct:
        Cs[k] -= Ct[k]

    def function(d):
        for v in d.values():
            if v<0:
                return 0
        return 1

    result = s+' '
    l, r = 0, -1
    while l<len(s):
        if r+1<len(s) and not function(Cs):
            r += 1
            Cs[s[r]] += 1
                    
        else:
            Cs[s[l]] -= 1
            l += 1

        if function(Cs) and len(result)>r-l+1:
            result = s[l:r+1]
        
    if len(result) == len(s) + 1:
        return ''
    return result
            
        
    
