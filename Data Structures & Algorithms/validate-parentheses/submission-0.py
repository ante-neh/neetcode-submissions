class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = { ')':'(','}':'{',']': '[' }
        stack = []

        for c in s:
            if stack and bracketMap.get(c, None) and stack[-1] == bracketMap[c]:
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0