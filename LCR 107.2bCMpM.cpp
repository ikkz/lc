#include <queue>
#include <tuple>
#include <utility>
#include <vector>

using namespace std;

// @leet start
class Solution {
public:
  vector<vector<int>> updateMatrix(vector<vector<int>> &mat) {
    auto res = mat;
    auto q = queue<pair<int, int>>();
    int m = mat.size(), n = mat.front().size();
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (mat[i][j] == 0) {
          q.push({i, j});
        } else {
          res[i][j] = -1;
        }
      }
    }
    int r, c;
    auto walk = [&res, &q, m, n](int i, int j, int next) {
      if (i >= 0 && i < m && j >= 0 && j < n && res[i][j] == -1) {
        res[i][j] = next;
        q.push({i, j});
      }
    };
    while (!q.empty()) {
      tie(r, c) = q.front();
      q.pop();
      int next = res[r][c] + 1;
      walk(r - 1, c, next);
      walk(r + 1, c, next);
      walk(r, c - 1, next);
      walk(r, c + 1, next);
    }
    return res;
  }
};
// @leet end
