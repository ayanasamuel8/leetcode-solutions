class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odds, evens = [], []
        for num in nums1:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
        odds.sort()
        evens.sort()
        if odds and evens:
            if evens[0] > odds[0]:
                return True
            return False
        return True