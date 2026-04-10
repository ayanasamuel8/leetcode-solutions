class Solution:
    def calc(self, nums):
        if len(nums) < 3:
            return inf
        return abs(nums[0] - nums[1]) + abs(nums[1] - nums[2]) + abs(nums[2] - nums[0])
    def minimumDistance(self, nums: List[int]) -> int:
        mp = defaultdict(deque)
        ans = inf
        for idx, num in enumerate(nums):
            mp[num].append(idx)
            if len(mp[num]) > 3:
                mp[num].popleft()
            ans = min(ans, self.calc(mp[num]))
        return ans if ans < inf else -1