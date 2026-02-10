class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        max_len = 0
        for i in range(len(nums)):
            odd = defaultdict(int)
            even = defaultdict(int)
            for j in range(i, len(nums)):
                if nums[j] % 2:
                    odd[nums[j]] += 1
                else:
                    even[nums[j]] += 1
                if len(odd) == len(even):
                    max_len = max(max_len, j - i + 1)
        return max_len