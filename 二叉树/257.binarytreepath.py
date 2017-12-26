def binaryTreePaths(root):
    result = []

    if not root:
        return []

    if not root.left and not root.right:
        result.append(str(root.val))
        return result

    left = binaryTreePaths(root.left)
    for i in left:
        result.append(str(root.val)+'->'+i)
    right = binaryTreePaths(root.right)
    for i in right:
        result.append(str(root.val)+'->'+i)

    return result
