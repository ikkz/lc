// @leet start

#include <climits>
#include <cmath>

class Solution {
public:
  int mySqrt(int x) {
    int low = 0, high = x / 2;
    while (low <= high) {
      long long mid = (low + high) / 2;
      long long res = mid * mid;
      if (res <= x && (mid + 1) * (mid + 1) > x) {
        return mid;
      } else if (res > x) {
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }
    return low;
  }
};
// @leet end
