#include <climits>
#include <iostream>
#include <limits>
#include <string>
#include <vector>
using namespace std;

// @leet start

class Solution {
public:
  int minCut(string s) {
    auto dp = vector<vector<bool>>(s.size(), vector<bool>(s.size(), false));
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
    vector<int> min_count(s.size(), 0);
    for (int i = 0; i < s.size(); ++i) {
      min_count[i] = i;
    }
    for (int j = 0; j < s.size(); ++j) {
      if (dp[0][j]) {
        min_count[j] = 0;
      } else {
        for (int i = 1; i <= j; i++) {
          if (dp[i][j]) {
            min_count[j] = min(min_count[i - 1] + 1, min_count[j]);
          }
        }
      }
    }
    return min_count.back();
  }
};
// @leet end
