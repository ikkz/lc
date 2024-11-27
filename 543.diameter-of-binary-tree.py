# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def depth(node):
            nonlocal res
            if not node:
                return 0
            left, right = depth(node.left), depth(node.right)
            res = max(res, left + right)
            return max(left, right) + 1
        depth(root)
        return res

# @leet end
