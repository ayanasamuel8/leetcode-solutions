class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        chars = set('abc')
        char_count = defaultdict(int)
        def is_valid():
            return set(char_count) == chars
        left = 0
        count = 0
        for right in range(len(s)):
            char_count[s[right]] += 1
            first = left
            while is_valid():
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            if first != left and not is_valid():
                left -= 1
                char_count[s[left]] += 1
            if is_valid():
                count += (left + 1)
        return count