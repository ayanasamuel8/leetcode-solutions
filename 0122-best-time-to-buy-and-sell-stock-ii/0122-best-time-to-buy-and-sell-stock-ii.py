class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dp(i, buy):
            if i == n:
                return 0
            if buy:
                return max(-prices[i] + dp(i + 1, False), dp(i + 1, True))
            else:
                return max(prices[i] + dp(i + 1, True), dp(i + 1, False))
        return dp(0, True)