class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        longSum = nums[0]
        left = 0
        n = len(nums)
        for right in range(1, n):
            if nums[right] != nums[right - 1] + 1:
                break
            longSum += nums[right]
    
        start = longSum
        st = set(nums)
        for i in range(start, start + n + 1):
            if i not in st:
                return i