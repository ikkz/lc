from typing import Optional
from head.list import ListNode

# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def swap(node):
    """
    Swap node.next and node.next.next
    """
    if not node or not node.next or not node.next.next:
        return None
    next = node.next.next.next
    first = node.next
    node.next = node.next.next
    node.next.next = first
    node.next.next.next = next
    return first


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        node = dummy
        node.next = head
        while node:
            node = swap(node)
        return dummy.next

        
        
# @leet end
