#include <vector>
using namespace std;

// @leet start
class Solution {
public:
  int takeAttendance(vector<int> &records) {
    if (records.front() != 0) {
      return 0;
    }
    for (int i = 0; i < records.size() - 1; ++i) {
      if (records[i] + 1 != records[i + 1]) {
        return i + 1;
      }
    }
    return records.size();
  }
};
// @leet end
