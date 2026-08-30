class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        smidx = nums.index(min(nums)) + 1
        lgidx = nums.index(max(nums)) + 1
        n = len(nums) + 1
        return min(max(smidx, lgidx), n - min(smidx, lgidx), min(smidx, lgidx) + n - max(smidx, lgidx))