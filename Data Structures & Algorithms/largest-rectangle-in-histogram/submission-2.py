class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # start pos, height
        n = len(heights)
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                idx, height = stack.pop()
                maxArea = max(maxArea, height*(i-idx))
                start = idx
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h*(n-i))

        return maxArea
            

        

        