class Solution:
    def judgeCircle(self, moves: str) -> bool:
        drxn = {'U': [-1, 0], 'D': [1, 0], 'R': [0, 1], 'L': [0, -1]}
        start = [0, 0]
        for move in moves:
            start[0] += drxn[move][0]
            start[1] += drxn[move][1]
        return start == [0,0]