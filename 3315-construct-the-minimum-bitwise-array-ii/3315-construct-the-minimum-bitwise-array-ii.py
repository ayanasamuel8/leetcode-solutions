class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)

        def find(x):
            cx = x
            if x % 2 == 0:
                return -1
            i = 0
            while x:
                if x & 1 == 0:
                    break
                i += 1
                x >>= 1
            cx = cx & ~(1 << (i - 1))
            return cx

        for i in range(n):
            ans.append(find(nums[i]))
        return ans