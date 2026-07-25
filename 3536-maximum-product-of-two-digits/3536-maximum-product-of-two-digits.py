class Solution:
    def maxProduct(self, n: int) -> int:
        singles = []
        while n:
            singles.append(n % 10)
            n//=10
        return reduce(lambda x,y: x * y, sorted(singles, reverse=True)[:2])