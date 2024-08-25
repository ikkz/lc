#include <vector>
using namespace std;

// @leet start
class Solution {
  vector<vector<int>> *matrix;
  int m, n;
  vector<vector<int>> lens;

public:
  int longestIncreasingPath(vector<vector<int>> &matrix) {
    this->matrix = &matrix;
    m = matrix.size();
    n = matrix.front().size();
    lens = vector(m, vector(n, 0));
    int ml = 1;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        walk(i, j);
        ml = max(ml, lens[i][j]);
      }
    }
    return ml;
  }

  int walk(int i, int j) {
    if (lens[i][j] != 0) {
      return lens[i][j];
    }
    int c = (*matrix)[i][j];
    auto next = [this, c, i, j](int ni, int nj) {
      if (ni < 0 || ni >= m || nj < 0 || nj >= n) {
        return false;
      }
      if ((*matrix)[ni][nj] > c) {
        lens[i][j] = max(lens[i][j], walk(ni, nj) + 1);
        return true;
      }
      return false;
    };
    bool b1 = next(i + 1, j);
    bool b2 = next(i - 1, j);
    bool b3 = next(i, j - 1);
    bool b4 = next(i, j + 1);
    if (!(b1 || b2 || b3 || b4)) {
      lens[i][j] = 1;
    }
    return lens[i][j];
  }
};
// @leet end
