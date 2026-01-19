class Solution:
    def check(self, pref, size):
        n, m = len(pref), len(pref[0])
        min_ = inf
        for i in range(n - size):
            for j in range(m - size):
                sum_ = pref[i + size][j + size] - pref[i + size][j] - pref[i][j + size] + pref[i][j]
                min_ = min(min_, sum_)
        return min_

    def prefixSum(self, mat):
        n, m = len(mat), len(mat[0])
        pref = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                pref[i + 1][j + 1] = mat[i][j] + pref[i][j + 1] + pref[i + 1][j] - pref[i][j]
        return pref

    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n, m = len(mat), len(mat[0])
        prefix = self.prefixSum(mat)
        left, right = 0, min(n, m)
        while left <= right:
            mid = left + (right - left) // 2
            if self.check(prefix, mid) <= threshold:
                best = mid
                left = mid + 1
            else:
                right = mid - 1
        return best
