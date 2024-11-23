from header.list import ListNode
from typing import Optional


# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2
        head = ListNode(0)
        node = head
        add = 0
        while l1 or l2 or add:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + add
            add = s // 10
            next = ListNode(s % 10)
            node.next = next
            node = next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next


# @leet end

