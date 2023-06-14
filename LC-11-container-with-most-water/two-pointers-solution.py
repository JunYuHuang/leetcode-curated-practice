# O(N) T and O(1) S two pointers solution (NeetCode's modded)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            if area > res:
                res = area
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res
