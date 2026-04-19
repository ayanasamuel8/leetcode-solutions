class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        mono = []
        for i in range(m -1, -1, -1):
            if not mono or nums2[mono[-1]] < nums2[i]:
                mono.append(i)
        ans = 0
        for i in range(n):
            while mono and nums2[mono[-1]] >= nums1[i]:
                ans = max(ans, mono.pop() - i)
            if mono and mono[-1] == i:
                mono.pop()
        return ans