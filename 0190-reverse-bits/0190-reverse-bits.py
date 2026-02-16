class Solution:
    def reverseBits(self, n: int) -> int:
        bit = bin(n)[2:]
        return int(bit[::-1] + '0'*(32 - len(bit)),2)