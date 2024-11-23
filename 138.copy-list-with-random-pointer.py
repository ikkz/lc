# @leet start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        node_map = dict()

        def copyNode(node):
            if not node:
                return None
            if id(node) not in node_map:
                copy = Node(node.val)
                node_map[id(node)] = copy
                if node.next:
                    copy.next = copyNode(node.next)
                if node.random:
                    copy.random = copyNode(node.random)
                return copy
            return node_map[id(node)]

        return copyNode(head)


