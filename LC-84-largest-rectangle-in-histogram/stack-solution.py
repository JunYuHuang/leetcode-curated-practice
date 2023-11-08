# O(N) T and O(N) S monotonic increasing stack (NeetCode's modded)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []  # of el (i, heights[i])
        heightsLen = len(heights)
        for i in range(heightsLen):
            pos = i
            while stack and stack[-1][1] > heights[i]:
                lastI, lastHeight = stack.pop()
                area = (i - lastI) * lastHeight
                if area > res:
                    res = area
                pos = lastI
            stack.append([pos, heights[i]])
        while stack:
            i, height = stack.pop()
            area = (heightsLen - i) * height
            if area > res:
                res = area
        return res
