# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        x = [root]
        res = []
        while x:
            y = []
            for n in x:
                if n.left:
                    y.append(n.left)
                if n.right:
                    y.append(n.right)
            res.append(list(map(lambda n: n.val, x)))
            x = y
        return res

        
# @leet end
