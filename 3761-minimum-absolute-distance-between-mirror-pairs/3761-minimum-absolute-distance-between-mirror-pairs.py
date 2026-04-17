class Solution:
    def mirror(self, num):
        newnum = 0
        while num:
            newnum *= 10
            newnum += num % 10
            num //= 10
        return newnum

    def minMirrorPairDistance(self, nums: List[int]) -> int:
        idx = defaultdict(list)
        n = len(nums)
        ans = inf
        for i in range(n):
            idx[nums[i]].append(i)
        for i in range(n):
            revnum = self.mirror(nums[i])
            if len(idx[revnum]) > 0:
                right = bisect_right(idx[revnum], i)
                if right < len(idx[revnum]):
                    ans = min(ans, abs(idx[revnum][right] - i))
        return ans if ans != inf else -1