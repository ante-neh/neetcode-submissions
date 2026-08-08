class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                prevIndex = stack.pop()
                result[prevIndex] = index - prevIndex

            stack.append(index)

        return result
