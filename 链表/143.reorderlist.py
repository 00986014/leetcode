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

def reorderList(head):
    head1, head2 = splitList(head)
    head2 = reverseList(head2)
    head = mergeList(head1, head2)
    return head

def splitList(head):
    dummyHead = ListNode(0)
    dummyHead.next = head
    p = q = dummyHead
    while p and p.next:
        p = p.next
        p = p.next
        q = q.next
    newhead = q.next
    q.next = None
    return dummyHead.next, newhead

def reverseList(head):
    pre = None
    cur = head
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre

def mergeList(head1, head2):
    dummyHead = ListNode(0)
    p = dummyHead
    i = 1
    while head1 or head2:
        if i%2 == 1:
            p.next = head1
            head1 = head1.next
            p = p.next
            i += 1
        else:
            p.next = head2
            head2 = head2.next
            p = p.next
            i += 1
    return dummyHead.next

nums = [1,2,3,4]
n = len(nums)

head = createLinkedList(nums, n)
newhead = reorderList(head)
printLinkedList(newhead)
