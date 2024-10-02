from typing import Optional, List
from header.tree import TreeNode


# @leet start
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traverse(node, level):
            if not node:
                return
            if node.right:
                traverse(node.right, level + 1)
            if level >= len(res):
                res.extend([None] * (1 + level - len(res)))
            if res[level] is None:
                res[level] = node.val
            if node.left:
                traverse(node.left, level + 1)

        traverse(root, 0)
        return res


# @leet end
