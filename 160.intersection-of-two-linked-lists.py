from typing import Optional
from header.list import ListNode
# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def list_len(node: ListNode) -> int:
    l = 0
    while node:
        l += 1
        node = node.next
    return l


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        len_a, len_b = list_len(headA), list_len(headB)
        long, short = (headA, headB) if len_a > len_b else (headB, headA)
        diff = abs(len_a - len_b)
        while diff and long:
            long = long.next
            diff -= 1
        while long and short and long != short:
            long = long.next
            short = short.next
        return long


# @leet end

