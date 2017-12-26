def kthSmallest(self, root, k):
    count = []
    self.helper(root, count)
    return count[k-1]
    
def helper(self, node, count):
    if not node:
        return
    
    self.helper(node.left, count)
    count.append(node.val)
    self.helper(node.right, count)
