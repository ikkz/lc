from typing import List

# @leet start
from bisect import bisect_left


def binary_search(arr, target: int):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        class Proxy:
            def __getitem__(self, idx: int):
                return matrix[idx // col][idx % col]

            def __len__(self):
                return row * col

        p = Proxy()
        # return (res := bisect_left(p, target)) != len(p) and p[res] == target
        return binary_search(p, target)


# @leet end

