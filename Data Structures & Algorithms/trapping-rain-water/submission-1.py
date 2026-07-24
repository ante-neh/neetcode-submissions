class Solution:
    def trap(self, height: List[int]) -> int:
        maxArea = 0
        leftMax, rightMax = height[0], height[-1]
        left, right = 0, len(height) - 1

        while left < right:
            if height[left] < height[right]:
                left += 1
                leftMax = max(leftMax, height[left])
                maxArea += leftMax - height[left]

            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                maxArea += rightMax - height[right]

        return maxArea