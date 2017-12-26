def swapPairs(head):
    dummyHead = ListNode(0)
    dummyHead.next = head

    p = dummyHead
    while p.next and p.next.next:
        n1 = p.next
        n2 = p.next.next
        next = n2.next

        n2.next = n1
        n1.next = next
        p.next = n2

        p = n1

    return dummyHead.next
