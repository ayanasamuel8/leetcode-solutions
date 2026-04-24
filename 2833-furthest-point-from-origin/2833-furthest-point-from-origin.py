class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cnt = 0
        val = {"L": -1, "R": 1}
        total = 0
        for i in moves:
            if i == '_':
                cnt += 1
            else:
                total += val[i]
        return abs(total) + cnt