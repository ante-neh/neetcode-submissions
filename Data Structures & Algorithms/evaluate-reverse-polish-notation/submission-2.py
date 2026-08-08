class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num1 + num2)

            elif token == "-":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2 - num1)

            elif token == "*":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num1 * num2)

            elif token == "/":
                num1, num2 = stack.pop(), stack.pop()
                result = num2 // num1 if (num2 / num1) > 0 else math.ceil(num2 / num1)
                stack.append(result)

            else:
                stack.append(int(token))

        return stack[-1]