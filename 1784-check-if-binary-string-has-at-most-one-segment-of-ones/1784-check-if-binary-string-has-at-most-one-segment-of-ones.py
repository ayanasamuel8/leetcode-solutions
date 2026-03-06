class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        lastOne = -1
        n = len(s)
        for i in range(n):
            if s[i] == '1':
                if lastOne != -1 and i - lastOne > 1:
                    return False
                lastOne = i
        return True