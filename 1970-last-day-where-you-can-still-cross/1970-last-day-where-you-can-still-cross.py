class Solution:
    def pathExist(self, cells, row, col):
        matrix = [[0] * col for _ in range(row)]
        for r, c in cells:
            r -= 1
            c -= 1
            matrix[r][c] = 1
        start = deque()
        visited = [[False] * col for _ in range(row)]
        for i in range(col):
            if matrix[0][i] == 0:
                start.append((0, i))
                visited[0][i] == True
                if 0 == row - 1:
                    return True
        drxn = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def in_bound(ni, nj):
            return 0 <= ni < row and 0 <= nj < col
        while start:
            i, j = start.popleft()
            if i == row - 1:
                return True
            for dx , dy in drxn:
                ni, nj = i + dx, j + dy
                if in_bound(ni, nj) and not visited[ni][nj] and matrix[ni][nj] == 0:
                    visited[ni][nj] = True
                    start.append((ni, nj))
        return False
                


    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left, right = 0, row * col
        best = 0
        while left <= right:
            mid = left + (right - left) // 2
            if self.pathExist(cells[:mid], row, col):
                best = mid
                left = mid + 1
            else:
                right = mid - 1
        return best