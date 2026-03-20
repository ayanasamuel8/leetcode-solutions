class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        if k == 1:
            return [[0] * (m - k + 1) for _ in range(n - k + 1)]
        def mindiff(arr):
            new = sorted(set(arr))
            if len(new) == 1:
                return 0
            min_ = inf
            for i in range(1, len(new)):
                min_ = min(min_, abs(new[i] - new[i - 1]))
            return min_
        ans = []
        for i in range(n - k + 1):
            temp = deque()
            tempans = []
            for j in range(m):
                for sub in range(k):
                    temp.append(grid[i + sub][j])
                if len(temp) == k * k:
                    tempans.append(mindiff(temp))
                    for s in range(k):
                        temp.popleft()
            ans.append(tempans)
        return ans
