from typing import Optional
from header.tree import TreeNode


# @leet start
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        sum = 0
        path = [0]

        def traverseNode(node: TreeNode):
            nonlocal sum
            ps = node.val + path[-1]
            for k in path:
                if ps - k == targetSum:
                    sum += 1
            path.append(ps)
            if node.left:
                traverseNode(node.left)
            if node.right:
                traverseNode(node.right)
            path.pop()

        if root:
            traverseNode(root)
        return sum

    def _pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        sum = 0

        def findPath(node: TreeNode, target: int):
            nonlocal sum
            if node.val == target:
                sum += 1
            if node.left:
                findPath(node.left, target - node.val)
            if node.right:
                findPath(node.right, target - node.val)

        def traverseNode(node: TreeNode):
            findPath(node, targetSum)
            if node.left:
                traverseNode(node.left)
            if node.right:
                traverseNode(node.right)

        if root:
            traverseNode(root)
        return sum


# @leet end

