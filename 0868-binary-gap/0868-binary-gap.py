class Solution:
    def binaryGap(self, n: int) -> int:
        bit = bin(n)[2:]
        if bit.count('1') < 2:
            return 0
        found = 0
        dis = 0
        start = bit.index('1')
        n = len(bit)
        for i in range(start, n):
            if bit[i] == '0':
                dis += 1
            else:
                found = max(dis + 1, found)
                dis = 0
        return found