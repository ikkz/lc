from typing import Optional
from header.list import ListNode

# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head.next
        while slow and fast and slow != fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                return False
            fast = fast.next
        return slow and fast


# @leet end

