def preorderTraversal(self, root):
    if not root:
        return []
    stack = []
    stack.append(root.val)
    stack += self.preorderTraversal(root.left)
    stack += self.preorderTraversal(root.right)
    return stack

def preorderTraversal2(root):
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            result.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return result
