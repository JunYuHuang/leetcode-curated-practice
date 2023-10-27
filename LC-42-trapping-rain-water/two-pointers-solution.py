# O(N) T and O(1) S two-pointer solution (NeetCode's modded)
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0
        res = 0
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        while l < r:
            if maxL < maxR:
                l += 1
                res += max(0, maxL - height[l])
                maxL = max(maxL, height[l])
            else:
                r -= 1
                res += max(0, maxR - height[r])
                maxR = max(maxR, height[r])
        return res
