def findContentChildren(g, s):
    s.sort(reverse=True)
    g.sort(reverse=True)

    si, gi = 0, 0
    result = 0

    while gi<len(g) and si<len(s):
        if s[si]>=g[gi]:
            result += 1
            si += 1
            gi += 1
        else:
            gi += 1

    return result
        
