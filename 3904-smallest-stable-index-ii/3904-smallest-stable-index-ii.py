class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        monostack = []
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if not monostack or nums[monostack[-1]] > nums[i]:
                monostack.append(i)
        maxi = -1
        for i in range(n):
            while monostack and monostack[-1] < i:
                monostack.pop()
            maxi = max(maxi, nums[i])
            if maxi - nums[monostack[-1]] <= k:
                return i
        return -1
