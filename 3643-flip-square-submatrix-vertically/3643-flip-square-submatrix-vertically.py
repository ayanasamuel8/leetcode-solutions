class Solution:
    def reverse(self, grid, k, y):
        ans = []
        for i in range(len(grid) - 1, -1, -1):
            ans.append(grid[i][y:y + k])
        return ans

    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        rev = self.reverse(grid[x:x+k], k, y)
        n, m = len(grid), len(grid[0])
        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i < x or i >= x + k or j < y or j >= y + k:
                    ans[i][j] = grid[i][j]
        for i in range(k):
            for j in range(k):
                ans[i+x][j + y] = rev[i][j]
        return ans