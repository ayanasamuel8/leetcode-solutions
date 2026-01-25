class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        min_ = nums[-1] - nums[-k]
        for i in range(n - k):
            min_ = min(min_, nums[i + k - 1] - nums[i])
        return min_