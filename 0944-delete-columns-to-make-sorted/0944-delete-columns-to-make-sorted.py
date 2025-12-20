class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        n = len(strs[0])
        for i in range(n):
            s = []
            for str_ in strs:
                s.append(str_[i])
            cnt += int(s != sorted(s))
        return cnt