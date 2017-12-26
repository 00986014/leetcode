def deleteNode(self, root, key):
    """
    :type root: TreeNode
    :type node: TreeNode
    :rtype: TreeNode
    """
    if root:
        # a loop to find a node with a given key
        p   = None
        cur = root
        while cur and cur.val != key:
            p = cur
            if cur.val < key :
                # if key to be removed is larger than current's key
                # then key to be removed is in right subtree
                cur = cur.right
            else:
                # if key to be removed in smaller than current's key
                # then key to be removed is in left subtree
                cur = cur.left
        
        # at this point p points to a parent of a node to be removed!
        # cur is node to be removed!
        if cur is None:
            # key is absent in the tree, nothing to do!
            return root
        
        if p is None:
            # root is being removed!
            left = root.left # left child
            root = root.right # right child always inherits the role of root
            root = self.insert(root,left) # insert left in new root 
        else:
            # detach both left and right children
            left  = cur.left
            right = cur.right
            cur.left = cur.right =  None
            # insert left into right
            right = self.insert(right,left) 
            # right child inherits father's role
            if p.left is cur:
                p.left = right 
            else:
                p.right = right

        return root
    
    # a util function to inser a given "node" in to a tree rooted at root
    # a node must not already exist in tree!
def insert(self, root, node):
    if root is None:
        # if tree is empty, return node being insert
        return node
    elif node is None:
        # if node being inserted is None, return root
        return root
    else:
        # find proper node's position in tree
        p   = None
        cur = root
        while cur:
            p = cur
            if node.val <= cur.val:
                cur = cur.left
            else:
                cur = cur.right
        
        # p is going to be father of node!
        # find if its suited as left or right child
        if node.val <= p.val:
            p.left = node
        else:
            p.right = node
        return root # modified tree returned
