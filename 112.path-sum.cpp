#include "header/tree.h"

// @leet start
class Solution {
public:
  bool hasPathSum(TreeNode *root, int targetSum, bool entry = true) {
    if (entry && !root) {
      return false;
    }
    if (!root->left && !root->right) {
      return targetSum == root->val;
    }
    return (root->left &&
            hasPathSum(root->left, targetSum - root->val, false)) ||
           (root->right &&
            hasPathSum(root->right, targetSum - root->val, false));
  }
};
// @leet end
