class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        n = len(s)
        left = 0
        ans = 0
        for right in range(n):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            ans = max(ans, right - left + 1)
        return ans