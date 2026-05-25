class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] != '0':
            return False
        stack = deque()
        stack.appendleft(n - 1)
        for i in range(n - 2, -1, -1):
            if s[i] == '0':
                while stack and (stack[-1] > i + maxJump):
                    stack.pop()
                if not stack:
                    return False
                elif i + minJump > stack[-1]:
                    if i == 0:
                        return False
                    continue
                else:
                    stack.appendleft(i)
        return True