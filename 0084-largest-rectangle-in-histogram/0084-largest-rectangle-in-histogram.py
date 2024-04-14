class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []
        heights.append(0)
        for idx, height in enumerate(heights):
            start = idx
            while start and stack[-1][1] > height:
                i, h = stack.pop()
                largest = max(largest, (idx-i)*h)
                start = i
            stack.append((start, height))

        return largest