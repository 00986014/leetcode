# coding:utf8
# 01背包问题
# w为物品的重量数组，v为价值数组，c为背包容量
def knapsack01(w, v, c):
    if not w:
        return 0
    n = len(w)
    l = [-1]*(c+1)

    for j in range(c+1):
        if j>=w[0]:
            l[j] = v[0]
        else:
            l[j] = 0

    for i in range(n):
        for j in range(C, w[i]-1, -1):
            l[j]=max(l[j],v[i]+l[j-w[i]])

    return l[c]

    
    
    
