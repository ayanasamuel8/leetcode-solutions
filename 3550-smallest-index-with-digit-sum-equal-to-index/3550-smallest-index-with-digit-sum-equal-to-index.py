class Solution:
    def sumOfDigits(self, num):
        total = 0

        while num:
            total += num % 10
            num //= 10
        
        return total

    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            if self.sumOfDigits(nums[i]) == i:
                return i
                
        return -1