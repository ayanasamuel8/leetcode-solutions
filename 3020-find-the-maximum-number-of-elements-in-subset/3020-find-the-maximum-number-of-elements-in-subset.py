class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        mp = Counter(nums)
        seen = set()
        def count(base):
            seen.add(base)
            if mp[base] < 2:
                return 1
            mp[base] -= 2
            if mp[base ** 2] < 1:
                return 1
            return count(base ** 2) + 2
        nums = sorted(set(nums))
        max_el = 1
        for i in nums:
            if i not in seen:
                max_el = max(max_el, count(i))
        return max_el