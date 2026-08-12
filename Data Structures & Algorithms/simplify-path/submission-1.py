class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        splittedPath = path.split("/")

        for char in splittedPath:
            if char:
                if char == '.' or (not stack and char == '..'):
                    continue

                elif char == '..':
                    stack.pop()

                else:
                    stack.append(char)

        return "/" + "/".join(stack)
