#coding:utf8
def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0

    # python中的排序函数高级用法
    intervals.sort(key=lambda x: x.end)

    result, pre = 1, 0    
    for i in xrange(1, len(intervals)):
        if intervals[i].start>=intervals[pre].end:
            result += 1
            pre = i

    return len(intervals)-result
