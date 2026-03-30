class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        left = [s1[i] for i in range(len(s1)) if i % 2]
        right = [s1[i] for i in range(len(s1)) if not i % 2]
        odd = [s2[i] for i in range(len(s2)) if i % 2]
        even = [s2[i] for i in range(len(s2)) if not i % 2]
        return sorted(left) == sorted(odd) and sorted(right) == sorted(even)