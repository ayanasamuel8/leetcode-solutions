class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False
        code = set()
        for i in range(1 << k):
            code.add(i)
        
        num = 0
        for i in range(k - 1):
            num <<= 1
            num |= int(s[i])
        
        base = 0
        for i in range(k):
            base |= 1
            base <<= 1
        base >>= 1
        
        for i in range(k -1, n):
            num <<= 1
            num |= int(s[i])
            num &= base
            code.discard(num)
        return len(code) == 0
