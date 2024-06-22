# O(N) T and O(1) S greedy / BFS solution (NeetCode's modded)
class Solution:
    def jump(self, nums: List[int]) -> int:
        LAST_POS = len(nums) - 1
        l = 0
        r = 0
        res = 0

        while r < LAST_POS:
            farthest = 0

            for i in range(l, r + 1):
                if i + nums[i] > farthest:
                    farthest = i + nums[i]

            l = r + 1
            r = farthest
            res += 1

        return res