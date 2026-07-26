class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return nums[0] * nums[1] * nums[2]
        nums.sort()
        cand1 = reduce(lambda x, y: x *y, nums[-3:])
        cand2 = nums[-1] * nums[0] * nums[1]
        cand3 = 0 if 0 in nums else cand1
        return max(cand1, cand2, cand3)