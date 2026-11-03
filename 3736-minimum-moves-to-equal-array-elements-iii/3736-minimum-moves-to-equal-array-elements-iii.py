class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_element = max(nums)
        return max_element * len(nums) - sum(nums)