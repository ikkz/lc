# @leet start
from collections import deque, defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses
        edges = defaultdict(set)
        for a, b in prerequisites:
            indeg[a] += 1
            edges[b].add(a)
        q = deque()
        for i, k in enumerate(indeg):
            if not k:
                q.append(i)
        count = numCourses
        while q:
            node = q.popleft()
            count -= 1
            for next in edges[node]:
                indeg[next]-=1
                if indeg[next] == 0:
                    q.append(next)
        return not count
                

# @leet end
