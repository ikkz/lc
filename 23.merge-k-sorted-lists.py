from typing import List, Optional
# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, id(head), head))
        head = ListNode(0)
        node = head
        while heap:
            _, _, node.next = heapq.heappop(heap)
            node = node.next
            if node.next:
                heapq.heappush(heap, (node.next.val, id(node.next), node.next))
            node.next = None
        return head.next


# @leet end
