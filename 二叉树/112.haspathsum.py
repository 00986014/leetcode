def hasPathSum(self, root, result):
    if not root:
        return False
    if not root.left and not root.right and root.val == result:
        return True
    return self.hasPathSum(root.left, result-root.val) or\
           self.hasPathSum(root.right, result-root.val)
