# O(N) T and O(1) S greedy solution (NeetCode's modded)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curSum = 0

        # track max element in `nums` in case
        # all elements in `nums` are negative
        hasPositive = False
        maxEl = nums[0]

        for n in nums:
            if n > maxEl:
                maxEl = n
            if n > 0:
                hasPositive = True
            if curSum < 0:
                curSum = 0

            curSum += n
            if curSum > res:
                res = curSum

        return res if hasPositive else maxEl
