#include <string>
#include <vector>
using namespace std;

// @leet start
class Solution {
public:
  int n;
  vector<string> res;

  vector<string> generateParenthesis(int n) {
    res = {};
    this->n = n;
    string s;
    t(0, 0, s);
    return res;
  }

  void t(int r, int l, string &s) {
    if (r == n && l == n) {
      res.push_back(s);
      return;
    }
    if (r < n) {
      s.push_back('(');
      t(r + 1, l, s);
      s.pop_back();
    }
    if (l < r) {
      s.push_back(')');
      t(r, l + 1, s);
      s.pop_back();
    }
  }
};
// @leet end
