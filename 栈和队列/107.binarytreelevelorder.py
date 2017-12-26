def levelOrderBottom(root):
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

    return result[::-1]



def levelOrderBottom2(self, root):
    res = []
    self.dfs(root, 0, res)
    return res

def dfs(self, root, level, res):
    if root:
        if len(res) < level + 1:
            res.insert(0, [])
        res[-(level+1)].append(root.val)
        self.dfs(root.left, level+1, res)
        self.dfs(root.right, level+1, res)

