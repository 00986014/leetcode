def removeNthFromEnd(head, n):
    dummyHead = ListNode(0)
    dummyHead.next = head

    p = q = dummyHead
    
    for i in range(n+1):
        q = q.next

    while q:
        p = p.next
        q = q.next

    p.next = p.next.next

    return dummyHead.next
