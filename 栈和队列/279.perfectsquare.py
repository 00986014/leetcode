#coding:utf8
#转化为最短路径问题，将相差为1个完全平方数的两个点连一条边
def numSquares(n):
    #q中存放数据对，分别为n和走到n的步数
    q = [[n, 0]]
    A = set()
    A.add(n)
    while q:
        num = q[0][0]
        step = q[0][1]
        q.remove(q[0])

        i = 1
        while True:
            a = num-i*i
            if a<0:
                break
            if a == 0:
                return step+1
            if a not in A:
                q.append([a, step+1])
                A.add(num-i*i)
            i += 1
