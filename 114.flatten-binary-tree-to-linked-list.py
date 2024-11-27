# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def concat(node):
            first, last = node, node
            if node.left or node.right:
                for n in [node.left, node.right]:
                    if not n:
                        continue
                    f, l = concat(n)
                    last.right = f
                    last = l
            first.left = None
            return first, last
        if root:
            return concat(root)[0]
        return root
# @leet end
