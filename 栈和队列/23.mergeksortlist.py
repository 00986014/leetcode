#coding:utf8
#这里传入的参数lists是所有list的头结点
def mergeKLists(self, lists):
    dummy = ListNode(None)
    curr = dummy
    q = PriorityQueue()
    for node in lists:
        if node: q.put((node.val,node))
    while q.qsize()>0:
        curr.next = q.get()[1]
        curr=curr.next
        if curr.next: q.put((curr.next.val, curr.next))
    return dummy.next
