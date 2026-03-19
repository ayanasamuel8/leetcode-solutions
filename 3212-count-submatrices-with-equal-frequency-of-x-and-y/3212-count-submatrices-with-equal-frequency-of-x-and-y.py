class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        available = [[False] * (m + 1) for _ in range(n + 1)]
        prefix = [[0] * (m + 1) for _ in range(n + 1)]
        val = {'X': 1, 'Y': -1, '.': 0}
        for i in range(n):
            for j in range(m):
                if grid[i][j] != '.' or (i > 0 and available[i - 1][j]) or (j > 0 and available[i][j - 1]):
                    available[i][j] = True
                prefix[i + 1][j + 1] = prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j] + val[grid[i][j]]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if prefix[i + 1][j + 1] == 0 and available[i][j]:
                    cnt += 1
        return cnt