class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        ascii1 = [0]
        ascii2 = [0]
        n, m = len(s1), len(s2)

        for i in range(n - 1, -1, -1):
            ascii1.append(ascii1[-1] + ord(s1[i]))
        for i in range(m - 1, -1, -1):
            ascii2.append(ascii2[-1] + ord(s2[i]))
        ascii1.reverse()
        ascii2.reverse()

        @cache
        def dp(i, j):
            if i >= n or j >= m:
                return ascii1[i] + ascii2[j]
            
            if s1[i] == s2[j]:
                return dp(i + 1, j + 1)
            else:
                return min(dp(i + 1, j) + ord(s1[i]), dp(i, j + 1) + ord(s2[j]))
        return dp(0, 0)
