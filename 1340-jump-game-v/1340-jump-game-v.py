class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        can_reach = {}
        n = len(arr)
        def dp(i):
            nonlocal n
            if i >= n or i < 0:
                return 0
            if i in can_reach:
                return can_reach[i]
            p = 0
            for j in range(1, d + 1):
                diffp = i + j
                if diffp >= n:
                    break
                if arr[i] <= arr[diffp]:
                    break
                p = max(p, dp(diffp) + 1)
            ne = 0
            for j in range(1, d + 1):
                diffn = i - j
                if diffn < 0:
                    break
                if arr[i] <= arr[diffn]:
                    break
                ne = max(ne, dp(diffn) + 1)
            can_reach[i] = max(ne, p)
            return can_reach[i]
        ans = 0
        for i in range(n):
            ans = max(ans, dp(i))
        return ans + 1