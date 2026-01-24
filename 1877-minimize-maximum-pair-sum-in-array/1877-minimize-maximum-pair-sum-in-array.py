class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        max_ = 0
        while left < right:
            max_ = max(max_, nums[left] + nums[right])
            right -= 1
            left += 1
        return max_