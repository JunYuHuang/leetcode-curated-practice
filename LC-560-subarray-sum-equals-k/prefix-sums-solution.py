# O(N) T and O(N) S prefix sums solution (NeetCode's modded)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumToCount = { 0 : 1 }
        NUMS_LEN = len(nums)
        res = 0
        currSum = 0

        for i in range(NUMS_LEN):
            currSum += nums[i]
            targetSum = currSum - k
            if targetSum in sumToCount:
                res += sumToCount[targetSum]
            sumToCount[currSum] = sumToCount.get(currSum, 0)
            sumToCount[currSum] += 1
        return res
