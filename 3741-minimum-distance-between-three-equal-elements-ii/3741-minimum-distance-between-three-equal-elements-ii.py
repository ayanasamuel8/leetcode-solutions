class CustomQue:
    def __init__(self):
        self.mpque = defaultdict(deque)
    def add(self, key, num):
        self.mpque[key].append(num)
        val = inf
        if len(self.mpque[key]) >= 3:
            val = self.calc(self.mpque[key])
            self.mpque[key].popleft()
        return val
    
    def calc(self, nums):
        return abs(nums[0] - nums[1]) + abs(nums[1] - nums[2]) + abs(nums[2] - nums[0])


class Solution:
    
    def minimumDistance(self, nums: List[int]) -> int:
        cque = CustomQue()
        ans = inf
        for idx, num in enumerate(nums):
            ans = min(ans, cque.add(num, idx))
        return ans if ans < inf else -1