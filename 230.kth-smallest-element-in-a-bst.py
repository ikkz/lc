# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = None

        def traverse(node):
            nonlocal count, res, k
            if res is not None:
                return
            if not node:
                return
            traverse(node.left)
            count += 1
            if count == k:
                res = node.val
            traverse(node.right)

        traverse(root)
        return res


# @leet end

