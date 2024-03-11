# O(N) T and O(1) S prefix sums optimized solution (NeetCode's modded)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        numsLen = len(nums)
        for i in range(numsLen):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1
