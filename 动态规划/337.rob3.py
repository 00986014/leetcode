def rob(self, root):
    rob_root, not_rob_root = self.max_rob(root)
    return max(rob_root, not_rob_root)

def max_rob(self, root):
    if not root:
        return 0, 0
    rob_l, not_rob_l = self.max_rob(root.left)
    rob_r, not_rob_r = self.max_rob(root.right)
    return root.val + not_rob_l + not_rob_r,\
           max(rob_l, not_rob_l) + max(rob_r, not_rob_r)
