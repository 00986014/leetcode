def inorderTraversal(self, root):
    if not root:
        return []
    stack = []
    stack += self.inorderTraversal(root.left)
    stack.append(root.val)
    stack += self.inorderTraversal(root.right)
    return stack

def inorderTraversal2(root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right
