class Solution:
    def isGood(self, nums: List[int]) -> bool:
        perm = [i for i in range(1, len(nums) - 1)]
        perm.extend([len(nums)- 1, len(nums)-1])
        nums.sort()
        return nums == perm