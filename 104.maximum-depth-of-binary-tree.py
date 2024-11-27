# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(node, d):
            nonlocal res
            if not node:
                return
            if node.left:
                traverse(node.left, d + 1)
            
            res = max(res, d)

            if node.right:
                traverse(node.right, d + 1)
        if root:
            traverse(root, 1)
        return res


# @leet end
