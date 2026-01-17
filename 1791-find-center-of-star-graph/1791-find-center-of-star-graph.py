class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        indegree = defaultdict(int)
        for u, v in edges:
            indegree[v] += 1
            indegree[u] += 1
        for u in range(1, n + 2):
            if indegree[u] == n:
                return u
        return -1