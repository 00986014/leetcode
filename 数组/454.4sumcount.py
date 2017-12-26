def fourSumCount(A, B, C, D):
    d = {}
    for i in xrange(len(C)):
        for j in xrange(len(D)):
            if (C[i]+D[j]) not in d:
                d[C[i]+D[j]] = 1
            else:
                d[C[i]+D[j]] += 1

    result = 0
    for i in xrange(len(A)):
        for j in xrange(len(B)):
            if (-A[i]-B[j]) in d:
                result += d[-A[i]-B[j]]
                
    return result
