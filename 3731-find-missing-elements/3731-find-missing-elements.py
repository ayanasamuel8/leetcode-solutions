class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        st = set(nums)
        for i in range(min(nums), max(nums) + 1):
            if i not in st: ans.append(i)
        return ans