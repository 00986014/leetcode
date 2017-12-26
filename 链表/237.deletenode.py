def deleteNode(node):
    if not node:
        return
    if not node.next:
        del node
        node = None
        return
    node.val = node.next.val
    node.next = node.next.next
