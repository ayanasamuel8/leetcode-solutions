class Solution:
    def intersect(self, a, b, c, d, e, f, g, h):
        left   = max(a, e)
        right  = min(c, g)
        bottom = max(b, f)
        top    = min(d, h)
        if left < right and bottom < top:
            return min(right - left, top - bottom) ** 2
        return 0

    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        ans = 0
        for i in range(n):
            a, b = bottomLeft[i]
            c, d = topRight[i]
            for j in range(i+1, n):
                e,f = bottomLeft[j]
                g, h = topRight[j]
                ans = max(ans, self.intersect(a, b, c, d, e, f, g, h))
        return ans