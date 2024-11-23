from typing import Optional
from header.list import ListNode

# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        fast, slow = head, head
        while True:
            slow = slow.next
            if fast and fast.next:
                fast = fast.next.next
            else:
                return None
            if fast == slow:
                break
        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return fast

    def _detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = set()
        while head:
            ident = id(head)
            if ident in nodes:
                return head
            nodes.add(ident)
            head = head.next
        return None


# @leet end

