class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n, q = len(nums), len(queries)
        mod = int(1e9 + 7)
        for l, r, k, v in queries:
            i = l
            while i <= r:
                nums[i] = (nums[i] * v) % mod
                i += k
        return reduce(lambda a, b: a ^ b, nums)