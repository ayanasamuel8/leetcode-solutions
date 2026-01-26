class Solution:
    def minimumAbsDifference(self, nums: List[int]) -> List[List[int]]:
        absolute_minimum = inf
        nums.sort()
        n = len(nums) - 1
        for i in range(n):
            diff = nums[i + 1] - nums[i]
            if diff < absolute_minimum:
                ans = []
                absolute_minimum = diff
            if diff == absolute_minimum:
                ans.append([nums[i], nums[i + 1]])
        return ans