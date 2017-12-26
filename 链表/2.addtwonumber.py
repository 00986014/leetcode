class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def createLinkedList(nums, n):
    if n==0:
        return None
    head = ListNode(nums[0])
    cur = head
    for i in nums[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return head

def printLinkedList(head):
    cur = head
    while cur != None:
        print cur.val
        print '->'
        cur = cur.next
    print 'None'

def addTwoNumbers(head):
    root = n = ListNode(0)
    carry = 0

    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next

nums = [1,2,3,4,5]
n = len(nums)

head = createLinkedList(nums, n)
newhead = oddEvenList(head)
printLinkedList(newhead)
