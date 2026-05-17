class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        seen = set()

        @cache
        def dp(i):
            
            if i < 0 or i >= n:
                return False
            if arr[i] == 0:
                return True
            if i in seen:
                return False
            seen.add(i)
            left = dp(i - arr[i])
            right = dp(i + arr[i])
            if left or right:
                return True

            return False
        return dp(start)