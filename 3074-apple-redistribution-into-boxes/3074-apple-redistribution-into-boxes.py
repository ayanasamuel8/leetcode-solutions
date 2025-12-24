class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity.sort(reverse=True)
        curr = 0
        for i in range(len(capacity)):
            curr += capacity[i]
            if curr >= total_apples:
                return i + 1