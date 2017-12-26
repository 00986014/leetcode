def numberOfBoomerangs(points):
    for i in points:
        d = {}
        for j in points:
            dis = (i[0]-j[0])**2 + (i[1]-j[1])**2
            if dis != 0:
                d[dis] = d.get(dis, 0) + 1
        for k in d:
            result += d[k]*(d[k]-1)
    return result
                
