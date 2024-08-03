#include <climits>
#include <vector>
using namespace std;
// @leet start
class Solution {
public:
  int minPathSum(vector<vector<int>> &grid) {
    vector<vector<int>> dp = grid;
    int m = grid.size(), n = grid[0].size();
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (i == 0 && j == 0) {
          continue;
        }
        int v = dp[i][j];
        int mv = INT_MAX;
        if (i - 1 >= 0) {
          mv = min(mv, v + dp[i - 1][j]);
        }
        if (j - 1 >= 0) {
          mv = min(mv, v + dp[i][j - 1]);
        }
        dp[i][j] = mv;
      }
    }
    return dp[m - 1][n - 1];
  }
};
// @leet end
