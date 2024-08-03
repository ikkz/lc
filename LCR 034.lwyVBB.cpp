#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
// @leet start
class Solution {
public:
  bool isAlienSorted(vector<string> &words, string order) {
    unordered_map<char, int> mp;
    for (int i = 0; i < order.size(); i++) {
      mp.insert({order[i], 'a' + i});
    }
    for (auto &str : words) {
      for (char &c : str) {
        c = mp[c];
      }
    }
    for (int i = 0; i < words.size() - 1; i++) {
      if (words[i] > words[i + 1]) {
        return false;
      }
    }
    return true;
  }
};
// @leet end
