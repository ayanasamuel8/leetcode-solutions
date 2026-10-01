class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []
        for i in s:
            if i not in paranthesis.keys():
                if not stack or paranthesis[stack[-1]] != i:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return not stack