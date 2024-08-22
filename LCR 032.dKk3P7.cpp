#include <array>
#include <cstddef>
#include <string>
using namespace std;

// @leet start
using CharsMap = array<size_t, 26>;

CharsMap chars_map(const string &s) {
  CharsMap cm;
  for (char c : s) {
    cm[c - 'a']++;
  }
  return cm;
}

class Solution {
public:
  bool isAnagram(string s, string t) {
    return s == t ? false : (chars_map(s) == chars_map(t));
  }
};
// @leet end
