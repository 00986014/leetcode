def removeElements(head, val):
    dummyhead = ListNode(0)
    dummyhead.next = head
    cur = dummyhead
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        cur = cur.next
    return dummyhead.next
