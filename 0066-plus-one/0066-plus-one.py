class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = deque()
        n = len(digits)
        q = 1
        for i in range(n - 1, -1, -1):
            curr = digits[i] + q
            q = curr // 10
            ans.appendleft(curr % 10)
        if q > 0:
            ans.appendleft(q)
        return list(ans)
            