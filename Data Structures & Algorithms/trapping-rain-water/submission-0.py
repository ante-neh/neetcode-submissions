class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax,rightMax = [0] * len(height), [0] * len(height)
        curMax = 0
        for i in range(len(height)):
            leftMax[i] = curMax
            curMax = max(curMax, height[i])

        curMax = 0

        for i in range(len(height) - 1, -1, -1):
            rightMax[i] = curMax
            curMax = max(curMax, height[i])

        
        maxArea = 0

        for i in range(len(height)):
            minHeight = min(leftMax[i], rightMax[i])
            if minHeight - height[i] > 0:
                maxArea += minHeight - height[i]

        return maxArea
