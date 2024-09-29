#include "header/node.h"
using ListNode = Node;

// @leet start

class Solution {
public:
  ListNode *mergeTwoLists(ListNode *list1, ListNode *list2) {
    if (list1 && list2) {
      auto node = list1->val < list2->val ? list1 : list2;
      node->next = mergeTwoLists(node->next, list1 == node ? list2 : list1);
      return node;
    }
    return list1 ? list1 : list2;
  }
};
// @leet end
