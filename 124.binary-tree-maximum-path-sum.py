# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        cache = dict()
        def maxSum(node):
            if node in cache:
                return cache[node]
            nonlocal res
            val = node.val
            cand = [node.val]
            if node.left:
                lsum = maxSum(node.left)
                val = max(val, node.val + lsum)
                cand.append(node.val + lsum)
            if node.right:
                rsum = maxSum(node.right)
                val = max(val, node.val + rsum)
                cand.append(node.val + rsum)
            if node.right and node.left:
                cand.append(node.val + lsum + rsum)
            res = max(max(cand), res)
            cache[node] = val
            return val
        maxSum(root)
        return res
# @leet end
