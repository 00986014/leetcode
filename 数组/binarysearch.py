def binarysearch(L, target):
    l, r = 0, len(L)-1
    while l<=r:
        mid = l + (r-l)/2
        if L[mid] == target:
            return mid
        elif target > L[mid]:
            l = mid+1
        else:
            r = mid-1
    return -1

if __name__ == '__main__':
    import time
    L = range(1000000)
    t0 = time.clock()
    for i in L:
        assert i == binarysearch(L, i)
    t1 = time.clock()
    print t0, t1, t1-t0
