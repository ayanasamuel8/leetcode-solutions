class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)

        def find(x):
            if x % 2 == 0:
                return -1
            i = 0
            while x:
                if x & (1 << i) == 0:
                    break
                i += 1
            x = x & ~(1 << (i - 1))
            return x

        for i in range(n):
            ans.append(find(nums[i]))
        return ans