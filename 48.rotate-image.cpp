#include <utility>
#include <vector>
using namespace std;

// @leet start
#define V(p) matrix[p.first][p.second]

using Point = pair<int, int>;

class Solution {
public:
  void rotate(vector<vector<int>> &matrix) {
    int n = matrix.size(), r = n / 2, c = n / 2 + n % 2;
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        Point lt = {i, j}, rt = {j, n - i - 1}, rb = {n - i - 1, n - j - 1},
              lb = {n - j - 1, i};
        auto lbv = V(lb);
        V(lb) = V(rb);
        V(rb) = V(rt);
        V(rt) = V(lt);
        V(lt) = lbv;
      }
    }
  }
};
// @leet end

/*
输入

[[5,1,9,11]
[2,4,8,10]
[13,3,6,7]
[15,14,12,16]]
输出
[[15,13,14,5]
[7,6,3,1]
[12,8,4,2]
[16,9,10,11]]
预期结果
[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 * */
