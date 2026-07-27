class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_ = -inf
        for i in range(n):
            for j in range(i + 1, n):
                max_ = max(max_, (nums[i] - 1) * (nums[j] - 1))
        return max_