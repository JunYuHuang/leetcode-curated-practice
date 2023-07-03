# O(LogN) T and O(1) S binary search solution (@camoenv3572's comment on NeetCode's video modded)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                # search in right and lower half of nums
                l = m + 1
            elif nums[m] < nums[r]:
                # search in left and lower half of nums including nums[m]
                r = m
            else: # nums[m] == nums[l]
                return nums[l]
