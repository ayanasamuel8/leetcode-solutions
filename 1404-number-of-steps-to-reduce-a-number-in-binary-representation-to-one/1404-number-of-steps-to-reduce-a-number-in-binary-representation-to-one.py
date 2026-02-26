class Solution:
    def add(self, s):
        ans = []
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                ans.append('1')
                break
            ans.append('0')
        ans.reverse()
        if i == 0:
            return '1' + ''.join(ans)
        return s[:i] + ''.join(ans)
    def numSteps(self, s: str) -> int:
        cnt = 0
        while len(s) > 1:
            if s[-1] == '1':
                s = self.add(s)
            else:
                s = s[:-1]
            cnt += 1
        return cnt