class Solution:
    def is_prime(self, set_bits):
        if set_bits == 1: return False
        if set_bits < 3: return True

        for i in range(2, math.isqrt(set_bits) + 1):
            if set_bits % i == 0:
                return False
        return True
    def countPrimeSetBits(self, left: int, right: int) -> int:
        cnt = 0
        for i in range(left, right + 1):
            set_bits = bin(i)[2:].count('1')
            if self.is_prime(set_bits):
                print(i, bin(i)[2:])
                cnt += 1
        return cnt