# O(N) T and O(1) S two pointers solution (NeetCode's modded)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        NUMS_LEN = len(nums)

        for r in range(1, NUMS_LEN):
            if nums[r - 1] == nums[r]:
                continue
            nums[l] = nums[r]
            l += 1

        return l
