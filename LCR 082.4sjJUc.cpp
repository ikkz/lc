#include <algorithm>
#include <utility>
#include <vector>
using namespace std;
// @leet start
class Solution {
  vector<pair<int, int>> candidates;
  int target;
  vector<vector<int>> res;

public:
  vector<vector<int>> combinationSum2(vector<int> &candidates, int target) {
    sort(candidates.begin(), candidates.end());
    this->target = target;
    this->candidates.clear();
    this->res.clear();
    for (int n : candidates) {
      if (this->candidates.empty()) {
        this->candidates.push_back({n, 1});
      } else if (this->candidates.back().first == n) {
        this->candidates.back().second++;
      } else {
        this->candidates.push_back({n, 1});
      }
    }
    vector<int> nums;
    t(0, nums, 0);
    return res;
  }

  void t(int i, vector<int> &nums, int sum) {
    if (sum == target) {
      res.push_back(nums);
      return;
    }
    if (i == candidates.size() || sum > target) {
      return;
    }
    t(i + 1, nums, sum);
    auto c = candidates[i];
    int k = c.second;
    while (k--) {
      nums.push_back(c.first);
      sum += c.first;
      t(i + 1, nums, sum);
    }
    k = c.second;
    while (k--) {
      nums.pop_back();
    }
  }
};
// @leet end
