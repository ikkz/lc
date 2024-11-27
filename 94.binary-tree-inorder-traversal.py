from typing import Optional

# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []
        stack = [[root, 0]]
        while stack:
            node, step = stack[-1]
            match step:
                case 0:
                    stack[-1][-1] = 1
                    if node.left:
                        stack.append([node.left, 0])
                case 1:
                    stack[-1][-1] = 2
                    res.append(node.val)
                case 2:
                    stack[-1][-1] = 3
                    if node.right:
                        stack.append([node.right, 0])
                case 3:
                    stack.pop()
        return res


    def _inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traverse(node):
            if not node:
                return
            if node.left:
                traverse(node.left)

            res.append(node.val)

            if node.right:
                traverse(node.right)
        traverse(root)
        return res


        
# @leet end
