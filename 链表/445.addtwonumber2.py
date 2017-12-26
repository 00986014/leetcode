def addTwoNumbers(self, l1, l2):
    x1 = x2 = 0
    while l1:
        x1 = 10*x1 + l1.val
        l1 = l1.next
    while l2:
        x2 = 10*x2 + l2.val
        l2 = l2.next
    x = str(x1+x2)
    root = n = ListNode(0)
    for i in x:
        n.next = ListNode(int(i))
        n = n.next
    return root.next
