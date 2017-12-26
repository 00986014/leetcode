def mergeTwoLists(self, l1, l2):
    h = l = ListNode(0)
    
    while l1 or l2:
        if l1 and l2:
            if l1.val<=l2.val:
                l.next = l1
                l1 = l1.next
                l = l.next
            else:
                l.next = l2
                l2 = l2.next
                l = l.next
        elif l1:
            l.next = l1
            break
        elif l2:
            l.next = l2
            break
    return h.next
