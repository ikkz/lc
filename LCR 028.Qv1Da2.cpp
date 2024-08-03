#define NODE_CHILD

#include "header/node.h"

// @leet start

class Solution {
public:
  Node *flatten(Node *head) {
    if (head) {
      _flatten(head);
    }
    return head;
  }

  Node *_flatten(Node *head) {
    auto node = head;
    while (true) {
      auto next = node->next;
      if (node->child) {
        auto last = _flatten(node->child);
        node->next = node->child;
        node->child->prev = node;
        node->child = nullptr;
        last->next = next;
        if (next) {
          next->prev = last;
        } else {
          return last;
        }
      }
      if (!next) {
        return node;
      }
      node = next;
    }
    return nullptr;
  }
};
// @leet end
