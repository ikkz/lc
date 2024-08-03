#include <tuple>
#include <vector>
using namespace std;

// @leet start
class Solution {
public:
  int rob(vector<int> &nums) {
    if (nums.size() == 1) {
      return nums.front();
    }
    int y, n;
    vector<pair<int, int>> dp(nums.size(), {0, 0});
    dp[1] = {nums[1], 0};
    for (int i = 2; i < nums.size(); i++) {
      dp[i] = {nums[i] + dp[i - 1].second,
               max(dp[i - 1].first, dp[i - 1].second)};
    }
    tie(y, n) = dp.back();
    int m = max(y, n);

    fill(dp.begin(), dp.end(), pair{0, 0});
    dp[1] = {nums[0], nums[0]};
    for (int i = 2; i < nums.size(); i++) {
      dp[i] = {nums[i] + dp[i - 1].second,
               max(dp[i - 1].first, dp[i - 1].second)};
    }
    tie(y, n) = dp.back();
    return max(m, n);
  }
};
// @leet end
