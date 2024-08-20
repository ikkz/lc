#include <algorithm>
#include <vector>
using namespace std;

// @leet start
class Solution {
  int target;
  vector<int> candidates;
  vector<vector<int>> res;

public:
  vector<vector<int>> combinationSum(vector<int> &candidates, int target) {
    sort(candidates.begin(), candidates.end());
    this->candidates = candidates;
    this->target = target;
    this->res = {};
    vector<int> nums;
    nums.reserve(150);
    t(0, 0, nums);
    return res;
  }

  void t(int i, int sum, vector<int> nums) {
    if (sum == target) {
      res.push_back(nums);
      return;
    }
    if (sum > target || i >= candidates.size() || nums.size() >= 150) {
      return;
    }
    int num = candidates[i];
    int k = 0;
    while (sum <= target) {
      t(i + 1, sum, nums);
      nums.push_back(num);
      sum += num;
      k++;
    }
    while (k--) {
      nums.pop_back();
    }
  }
};
// @leet end
