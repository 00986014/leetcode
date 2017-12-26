def isValidBST(self, root):
    min_range = float("-inf")
    max_range = float("inf")
    return self.isBST(min_range, max_range, root)

def isBST(self, min_range, max_range, current):
    if current == None:
        return True
    if current.val <= min_range or current.val >= max_range:
        return False
    return self.isBST(min_range, current.val, current.left) and\
           self.isBST(current.val, max_range, current.right) 
