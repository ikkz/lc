# @leet start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def bt(i, current, acc):
            if i == len(candidates):
                if current == target:
                    res.append(acc.copy())
                return
            count = 0
            bt(i + 1, current, acc)
            while current + candidates[i] <= target:
                count += 1
                current += candidates[i]
                acc.append(candidates[i])
                bt(i + 1, current, acc)
            while count:
                count -= 1
                current -= candidates[i]
                acc.pop()

        bt(0, 0, [])
        return res


# @leet end

