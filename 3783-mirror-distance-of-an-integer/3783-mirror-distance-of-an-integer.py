class Solution:
    def mirror(self, num):
        ans = 0
        while num:
            ans = ans * 10 + num % 10
            num //= 10
        return ans

    def mirrorDistance(self, n: int) -> int:
        return abs(n - self.mirror(n))