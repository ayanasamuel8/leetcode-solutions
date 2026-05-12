class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        srt = sorted(tasks, key=lambda x: x[1] - x[0], reverse=True)
        tot = 0
        left = 0
        for i, j in srt:
            if left < j:
                tot += j - left
                left = j
            left -= i
        return tot