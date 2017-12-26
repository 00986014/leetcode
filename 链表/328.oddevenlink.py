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

def oddEvenList(head):
    h1 = l1 = ListNode(0)
    h2 = l2 = ListNode(0)

    i = 1
    while head:
        if i%2 == 1:
            l1.next = head
            l1 = l1.next
        else:
            l2.next = head
            l2 = l2.next
        i += 1
        head = head.next

    l2.next = None
    l1.next = h2.next
    return h1.next

nums = [1,2,3,4,5]
n = len(nums)

head = createLinkedList(nums, n)
newhead = oddEvenList(head)
printLinkedList(newhead)
