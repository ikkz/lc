// @leet start
#include <set>
#include <vector>

using namespace std;
class Solution {
public:
  int longestConsecutive(vector<int> &nums) {
    if (nums.size() == 0) {
      return 0;
    }
    set<int> s;
    for (auto n : nums) {
      s.insert(n);
    }
    bool b = false;
    int prev = 0, ml = 1, cl = 1;
    for (auto n : s) {
      if (b) {
        if (n == prev + 1) {
          cl++;
          ml = max(ml, cl);
        } else {
          cl = 1;
        }
        prev = n;
      } else {
        b = true;
        prev = n;
      }
    }
    return ml;
  }
};
// @leet end
