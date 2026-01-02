class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return max([(v, i) for i, v in Counter(nums).items()])[1]