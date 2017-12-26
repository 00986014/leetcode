def isSymmetric(self, root):
    def isSym(L,R):
        if L and R and L.val == R.val: 
            return isSym(L.left, R.right) and isSym(L.right, R.left)
        return L == R
    return isSym(root, root)
