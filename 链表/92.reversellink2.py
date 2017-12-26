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


def reverseBetween(head, m, n):
    if m == n:
        return head

    dummyNode = ListNode(0)
    dummyNode.next = head
    pre = dummyNode

    for i in range(m - 1):
        pre = pre.next
    
    # reverse the [m, n] nodes
    reverse = None
    cur = pre.next
    for i in range(n - m + 1):
        next = cur.next
        cur.next = reverse
        reverse = cur
        cur = next

    pre.next.next = cur
    pre.next = reverse

    return dummyNode.next

nums = [1,2,3,4,5]
n = len(nums)

head = createLinkedList(nums, n)
newhead = reverseBetween(head, 2, 4)
printLinkedList(newhead)


