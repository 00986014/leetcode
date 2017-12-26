#coding:utf8
def pathSum(root, sum):
    if not root:
        return 0

    result = findPath(root, sum)
    result += pathSum(root.left, sum)
    result += pathSum(root.right, sum)
    return result

#在以root为根节点的二叉树中寻找包含root的和为sum的路径
def findPath(root, sum):
    if not root:
        return 0

    result = 0
    if root.val == sum:
        result += 1

    result += findPath(root.left, sum-root.val)
    result += findPath(root.right, sum-root.val)

    return result
    
