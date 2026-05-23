class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        return sum(1 for _ in range(n) if nums[_]>nums[(_+1)%n])<2