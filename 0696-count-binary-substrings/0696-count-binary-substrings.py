class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cnt = 0
        n = len(s)
        past = [0, '-1']
        curr = [0, '-1']
        for i in range(n):
            if s[i] != curr[1]:
                cnt += min(curr[0], past[0])
                past = curr
                curr = [1, s[i]]
            else:
                curr[0] += 1
        cnt += min(curr[0], past[0])
        return cnt