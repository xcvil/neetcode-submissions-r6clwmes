class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        n = len(heights)

        for i ,height in enumerate(heights):
            start = i

            while stack and height <= stack[-1][1]: # =?
                pre_i, pre_height = stack.pop()
                maxArea = max(maxArea, (i-pre_i)*pre_height)
                start = pre_i
            stack.append((start, height))

        for i, height in stack:
            maxArea = max(maxArea, (n-i)*height)

        return maxArea