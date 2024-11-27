from typing import List, Optional
from header.tree import TreeNode


# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(pl, pr, il, ir):
            if pl > pr or il > ir:
                return None
            parent = preorder[pl]
            pos = inorder.index(parent, il, ir + 1)
            return TreeNode(
                parent,
                build(pl + 1, pl + pos - il, il, pos - 1),
                build(pl + pos - il + 1, pr, pos + 1, ir)
            )
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

# @leet end

