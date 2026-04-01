class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(directions)
        ind = [i for i in range(n)]
        zipped = list(zip(directions, positions, healths, ind))
        zipped.sort(key=lambda x:x[1])
        stack = []
        for drxn, pos, health, idx in zipped:
            if drxn == 'L':
                while stack and stack[-1][0] == 'R' and stack[-1][1] < health:
                    stack.pop()
                    health -= 1
                if stack and stack[-1][0] == 'R' and stack[-1][1] == health:
                    stack.pop()
                    continue
                elif stack and stack[-1][0] == 'R' and stack[-1][1] > health:
                    stack[-1][1] -= 1
                    continue
            stack.append([drxn, health, idx])
        return [j for i, j,z in sorted(stack, key=lambda x:x[2])]