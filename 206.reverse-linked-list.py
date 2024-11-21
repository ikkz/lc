from typing import Optional
from header.list import ListNode


# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, node: Optional[ListNode], prev=None) -> Optional[ListNode]:
        if not node:
            return node
        next = node.next
        node.next = prev
        return self.reverseList(next, node) if next else node

    def _reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev, node = head, head.next
        head.next = None
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev


# @leet end

