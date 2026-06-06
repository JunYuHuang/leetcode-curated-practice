# NeetCode's 2-pointer (quicksort select) O(n) T + O(1) S solution
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        numsLen = len(nums)
        k = 0

        for i in range(numsLen):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
