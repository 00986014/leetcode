def levelOrder(root):
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

    return result
