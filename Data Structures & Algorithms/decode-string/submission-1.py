class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currNum = 0
        currString = ""

        for char in s:
            if char.isdigit():
                currNum = currNum * 10 + int(char)
            
            elif char == '[':
                stack.append((currString, currNum))
                currString = ""
                currNum = 0

            elif char == ']':
                prevString, num = stack.pop()
                currString = prevString + (currString * num)

            else:
                currString += char

        return currString
        