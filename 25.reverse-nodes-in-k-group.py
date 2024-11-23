from typing import Optional
from header.list import ListNode

# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(head, k):
    """
    head 指向每一组的第一个节点
    returns 反转后的组内最后一个节点
    """
    # 检查这一组是否有 k 个节点
    node = head
    count = k
    while count and node.next:
        node = node.next
        count -= 1
    if count:
        return None

    last_before_rev = node
    next_group_first = node.next

    prev = head.next
    cur = head.next.next
    prev.next = next_group_first
    ret = prev
    while cur != next_group_first:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    head.next = last_before_rev
    return ret

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        while node:
            node = reverse(node, k)
        return dummy.next
        
# @leet end
