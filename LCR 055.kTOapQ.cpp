#include "header/tree.h"
#include <stack>

using namespace std;

// @leet start
class BSTIterator {
  stack<TreeNode *> st;

public:
  BSTIterator(TreeNode *root) {
    if (root) {
      forward_left(root);
    }
  }

  void forward_left(TreeNode *node) {
    while (node) {
      st.push(node);
      node = node->left;
    }
  }

  void forward() {
    if (st.empty()) {
      return;
    }
    auto node = st.top();
    if (node->right) {
      forward_left(node->right);
    } else {
      st.pop();
      while (!st.empty() && node == st.top()->right) {
        node = st.top();
        st.pop();
      }
    }
  }

  int next() {
    auto val = st.top()->val;
    forward();
    return val;
  }

  bool hasNext() { return !st.empty(); }
};
