def lowestCommonAncestor(root, p, q):
    if not root:
        return None

    if p.val<root.val and q.val<root.val:
        return lowestCommonAncestor(root.left, p, q)
    if p.val>root.val and q.val>root.val:
        return lowestCommonAncestor(root.right, p, q)

    return root

def lowestCommonAncestor(self, root, p, q):
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root
