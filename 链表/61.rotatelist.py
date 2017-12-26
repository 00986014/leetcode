def rotateRight(self, head, k):
    if k == 0 or not head:
        return head
    dummyHead = ListNode(0)
    dummyHead.next = head        
    p = q = dummyHead
    
    length = 0
    while q.next:
        q = q.next
        length += 1
    q = dummyHead
    k = k%length
    if k == 0:
        return head
    
    for i in range(k):
        q = q.next

    while q.next:
        p = p.next
        q = q.next
        
    dummyHead.next = p.next
    q.next = head
    p.next = None
    
    return dummyHead.next
