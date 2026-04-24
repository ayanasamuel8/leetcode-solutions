class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        L = R = 0
        val = {'L': -1, 'R': 1}
        for i in moves:
            if i == "_":
                L -= 1
                R += 1
            else:
                L += val[i]
                R += val[i]
        return max(abs(L), abs(R))