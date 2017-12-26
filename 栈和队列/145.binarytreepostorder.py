def postorderTraversal(self, root):
    if not root:
        return []
    stack = []
    stack += self.postorderTraversal(root.left)
    stack += self.postorderTraversal(root.right)
    stack.append(root.val)
    return stack

def postorderTraversal2(root):
    if not root:
        return []
    visited = set([root])
    stack = [root]
    res = []
    while stack:
        node = stack[-1]
        if not (node.right and not node.right in visited or\
                node.left and not node.left in visited):
            stack.pop()
            res.append(node.val)
        if node.right and not node.right in visited:
            visited.add(node.right)
            stack.append(node.right)
        if node.left and not node.left in visited:
            visited.add(node.left)
            stack.append(node.left)
    return res
