#include <vector>

using namespace std;
// @leet start

void perm(const vector<int> &nums, vector<bool> &visited, vector<int> &his,
          vector<vector<int>> &res) {
  if (his.size() == nums.size()) {
    res.push_back(his);
    return;
  }
  for (int i = 0; i < nums.size(); ++i) {
    if (visited[i]) {
      continue;
    }
    visited[i] = true;
    his.push_back(nums[i]);
    perm(nums, visited, his, res);
    his.pop_back();
    visited[i] = false;
  }
}

class Solution {

public:
  vector<vector<int>> permute(vector<int> &nums) {
    vector<bool> visited(nums.size(), false);
    vector<vector<int>> res;
    vector<int> his;

    perm(nums, visited, his, res);
    return res;
  }
};
// @leet end
