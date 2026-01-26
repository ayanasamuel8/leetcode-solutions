class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        absolute_minimum = inf
        arr.sort()
        n = len(arr) - 1
        for i in range(n):
            absolute_minimum = min(absolute_minimum, arr[i + 1] - arr[i])
        ans = []
        for i in range(n):
            if arr[i + 1] - arr[i] == absolute_minimum:
                ans.append([arr[i], arr[i + 1]])
        return ans