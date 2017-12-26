def rightSideView(self, root):
    result = []
    if not root:
        return result

    q = []
    q.append((root, 0))
    while q:
        node = q[0][0]
        level = q[0][1]
        q.remove(q[0])

        if level == len(result):
            result.append([])

        result[level].append(node.val)
        if node.left:
            q.append((node.left, level+1))
        if node.right:
            q.append((node.right, level+1))
    
    res = []
    for i in result:
        res.append(i[-1])
    
    return res

def rightSideView2(self, root):
    if not root:
        return []
    right = self.rightSideView(root.right)
    left = self.rightSideView(root.left)
    return [root.val] + right + left[len(right):]

def rightSideView3(self, root):
    def collect(node, depth):
        if node:
            if depth == len(view):
                view.append(node.val)
            collect(node.right, depth+1)
            collect(node.left, depth+1)
    view = []
    collect(root, 0)
    return view

