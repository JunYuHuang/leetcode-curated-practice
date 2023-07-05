# O(LogN) T and O(1) S binary search solution (NeetCode's modded)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]:
                # nums[m] is in left sorted half
                if nums[l] <= target <= nums[m]:
                    r = m - 1 # search this half
                else:
                    l = m + 1 # search other right half
            else: # nums[l] > nums[m]
                # nums[m] is in right sorted half
                if nums[m] <= target <= nums[r]:
                    l = m + 1 # search this half
                else:
                    r = m - 1 # search other left half
        return -1
