# NeetCode's quicksort / 2-pointer O(n) T and O(1) S modded solution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        numsLen = len(nums)

        for r in range(numsLen):
            if nums[r] != 0:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1