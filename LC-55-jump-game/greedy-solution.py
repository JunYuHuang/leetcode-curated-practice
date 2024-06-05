# O(N) T and O(1) S greedy solution (NeetCode's modded)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        NUMS_LEN = len(nums)
        goalPos = NUMS_LEN - 1

        for i in range(NUMS_LEN - 2, -1, -1):
            if i + nums[i] >= goalPos:
                goalPos = i

        return goalPos == 0
