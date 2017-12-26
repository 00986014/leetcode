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
        

def reverseList(head):
    if not head:
        return None
    pre = None
    cur = head
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next

    return pre


nums = [1,2,3,4,5]
n = len(nums)

head = createLinkedList(nums, n)
printLinkedList(head)
newhead = reverseList(head)
printLinkedList(newhead)
