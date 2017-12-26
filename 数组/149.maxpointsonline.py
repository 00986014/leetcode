def maxPoints(self, points):
    if len(points) == 1:
        return 1
    result = 0
    for p in points:
        d = {}
        g = 0
        dup = 0
        for q in points:
            if q.x != p.x or q.y != p.y:
                if q.x != p.x:
                    g = 10.0*float(q.y-p.y)/(q.x-p.x)
                else:
                    g = float('inf')         
                d[g] = d.get(g, 0) + 1
            else:
                dup += 1
        if len(d) == 0:
            result = len(points)
        for k in d:
            result = max(result, d[k]+dup)
    return result
