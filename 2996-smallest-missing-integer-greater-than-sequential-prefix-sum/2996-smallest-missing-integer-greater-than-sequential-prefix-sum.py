class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        longest = 1
        longSum = nums[0]
        currSum = nums[0]
        left = 0
        n = len(nums)
        for right in range(1, n):
            if nums[right] == nums[right - 1] + 1:
                currSum += nums[right]
            else:
                currSum = nums[right]
                break
                left = right
            if longest < right - left + 1:
                longest = right - left + 1
                longSum = currSum
        start = longSum
        st = set(nums)
        for i in range(start, start + n + 1):
            if i not in st:
                return i