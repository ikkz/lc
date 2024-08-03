#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

// @leet start
class Solution {
public:
  vector<int> findOrder(int numCourses, vector<vector<int>> &prerequisites) {
    unordered_map<int, unordered_set<int>> paths;
    vector<int> indegree(numCourses, 0);
    vector<bool> visited(numCourses, false);
    vector<int> seq;

    for (auto &path : prerequisites) {
      indegree[path.front()]++;
      if (auto it = paths.find(path.back()); it != paths.end()) {
        it->second.insert(path.front());
      } else {
        auto st = unordered_set<int>();
        st.insert(path.front());
        paths.insert({path.back(), st});
      }
    }
    while (true) {
      bool changed = false;
      for (int i = 0; i < numCourses; i++) {
        if (visited[i] || indegree[i] > 0) {
          continue;
        }
        visited[i] = true;
        seq.push_back(i);
        changed = true;

        auto nexts = paths.find(i);
        if (nexts != paths.end()) {
          for (auto n : nexts->second) {
            indegree[n]--;
          }
        }
      }
      if (!changed) {
        break;
      }
    }
    for (auto v : visited) {
      if (!v) {
        return {};
      }
    }
    return seq;
  }
};
// @leet end
