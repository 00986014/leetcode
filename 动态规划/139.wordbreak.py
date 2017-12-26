def wordBreak(s, wordDict):
    n = len(s)
    l = [False]*(n+1)
    l[0] = True

    for i in xrange(1, n+1):
        for w in wordDict:
            if s[i-len(w):i]==w and l[i-len(w)]:
                l[i] = True
    return l[-1]
