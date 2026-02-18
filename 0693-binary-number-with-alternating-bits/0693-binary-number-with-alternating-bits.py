class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bit = bin(n)[2:]
        return '00' not in bit and '11' not in bit