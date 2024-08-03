#include <queue>

// @leet start
class MovingAverage {
private:
  int size;
  int sum = 0;
  std::queue<int> q;

public:
  /** Initialize your data structure here. */
  MovingAverage(int size) : size(size) {}

  double next(int val) {
    q.push(val);
    sum += val;
    if (q.size() > size) {
      sum -= q.front();
      q.pop();
    }
    return static_cast<double>(sum) / q.size();
  }
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */
// @leet end
