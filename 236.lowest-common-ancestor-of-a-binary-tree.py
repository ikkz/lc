# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pathp = None
        pathq = None
        path = [root]
        def traverse(node):
            nonlocal pathq, pathp, path
            if not node:
                return
            if node == p:
                pathp = path.copy()
            if node == q:
                pathq = path.copy()
            if node.left:
                path.append(node.left)
                traverse(node.left)
                path.pop()
            if node.right:
                path.append(node.right)
                traverse(node.right)
                path.pop()
        traverse(root)
        path.pop()
        ml = min(len(pathq), len(pathp))
        for i in range(ml):
            if pathq[i] != pathp[i]:
                return pathq[i - 1]
        return pathp[ml - 1]
# @leet end
