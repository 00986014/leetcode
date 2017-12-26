def lowestCommonAncestor(self, root, p, q):
    if not root:
        return None
    if p==root or q==root:
        return root
    
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    elif not (left and right):
        return left or right
