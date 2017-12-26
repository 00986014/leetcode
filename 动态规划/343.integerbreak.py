# coding:utf8
def integerBreak(n):
    l = []
    for i in xrange(n+1):
        l.append(-1)
    return breakInteger(n)

def breakInteger(n):
    if n==1:
        return 1

    if l[n] != -1:
        return l[n]
    result = -1
    # 分割成i和n-i两块，将n-i继续分割
    for i in range(1, n+1):
        result = max(result, i*(n-i), i*breakInteger(n-i))

    l[n] = result
    return result


def integerBreak(n):
    l = []
    for i in xrange(n+1):
        l.append(-1)
    l[1]=1
    for i in xrange(2, n+1):
        for j in xrange(1, i):
            l[i] = max(l[i], j*(i-j), j*l[i-j])
    return l[n]
