class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = int(1e9 + 7)
        start = 0
        for i in range(1, n + 1):
            shift = len(bin(i)[2:])
            start <<= shift
            start += i
            start %= mod
        return start