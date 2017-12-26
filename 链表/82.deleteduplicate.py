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


def deleteDuplicates(head):
    dummy = pre = ListNode(0)
    dummy.next = head
    while head and head.next:
        if head.val == head.next.val:
            while head and head.next and head.val == head.next.val:
                head = head.next
            head = head.next
            pre.next = head
        else:
            pre = pre.next
            head = head.next
    return dummy.next

nums = [1,1,1]
n = len(nums)

head = createLinkedList(nums, n)
newhead = deleteDuplicates(head)
printLinkedList(newhead)


