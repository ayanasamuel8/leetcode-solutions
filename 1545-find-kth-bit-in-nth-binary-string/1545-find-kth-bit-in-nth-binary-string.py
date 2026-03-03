class Solution:
    def revinvert(self, s):
        ans = []
        for i in s:
            ans.append(str(1 - int(i)))
        return list(reversed(ans))
    def findKthBit(self, n: int, k: int) -> str:
        ans = ['0']
        for i in range(1, n):
            ans.extend(['1'] + self.revinvert(ans))
        return ans[k-1]