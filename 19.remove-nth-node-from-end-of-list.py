from typing import Optional
from header.list import ListNode


# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = ListNode(next=head)
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head.next


# @leet end