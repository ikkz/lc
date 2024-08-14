#include <string>
#include <vector>

using namespace std;
// @leet start
using DpArray = vector<vector<bool>>;

class Solution {
  DpArray dp;
  vector<vector<string>> res;
  string s;

public:
  vector<vector<string>> partition(string s) {
    this->s = s;
    dp = DpArray(s.size(), vector<bool>(s.size(), false));
    res = {};
    // i <= j
    // i == j: dp[i][j] = true
    // si = sj: dp[i][j] = dp[i + 1][j - 1]
    for (int i = 0; i < s.size(); ++i) {
      dp[i][i] = true;
    }
    for (int i = s.size() - 1; i >= 0; --i) {
      for (int j = i + 1; j < s.size(); ++j) {
        if (s[i] == s[j]) {
          dp[i][j] = i + 1 >= j - 1 ? true : dp[i + 1][j - 1];
        }
      }
    }
    vector<string> p;
    t(0, p);
    return res;
  }

  void t(int start, vector<string> &p) {
    if (start == dp.size()) {
      res.push_back(p);
      return;
    }
    for (int j = start; j < dp.size(); ++j) {
      if (dp[start][j]) {
        p.push_back(s.substr(start, j - start + 1));
        t(j + 1, p);
        p.pop_back();
      }
    }
  }
};
// @leet end
