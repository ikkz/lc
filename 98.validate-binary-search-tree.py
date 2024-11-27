# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        res = True
        def traverse(node):
            nonlocal prev, res
            if not res:
                return
            if not node:
                return
            traverse(node.left)
            if prev is None:
                prev = node.val
            elif node.val <= prev:
                res = False
                return
            prev = node.val
            traverse(node.right)
        traverse(root)
        return res
# @leet end
