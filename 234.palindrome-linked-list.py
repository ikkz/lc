from typing import Optional
from header.list import ListNode


# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        node = head
        for _ in range(length // 2 - 1):
            node = node.next
        next = node.next
        while next:
            new_next = next.next
            next.next = node
            node = next
            next = new_next

        for _ in range(length // 2):
            if head.val != node.val:
                return False
            head = head.next
            node = node.next

        return True


# @leet end

