#include <climits>
#include <vector>

using namespace std;
// @leet start
class Solution {
public:
  int coinChange(vector<int> &coins, int amount) {
    vector<int> dp(amount + 1, INT_MAX);
    dp[0] = 0;
    for (int i = 1; i <= amount; i++) {
      int mc = INT_MAX;
      for (auto coin : coins) {
        for (int c = 1; i - c * coin >= 0; c++) {
          if (auto pc = dp[i - c * coin]; pc != INT_MAX) {
            mc = min(mc, pc + c);
            break;
          }
        };
      }
      dp[i] = mc;
    }
    return dp[amount] == INT_MAX ? -1 : dp[amount];
  }
};
// @leet end
