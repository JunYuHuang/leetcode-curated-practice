# O(N) T and O(1) S greedy solution (NeetCode's modded)
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalSum = 0
        curMaxSum = 0
        maxSum = nums[0]
        curMinSum = 0
        minSum = nums[0]

        for n in nums:
            curMaxSum = max(curMaxSum + n, n)
            maxSum = max(maxSum, curMaxSum)
            curMinSum = min(curMinSum + n, n)
            minSum = min(minSum, curMinSum)
            totalSum += n

        if maxSum < 0:
            return maxSum

        return max(maxSum, totalSum - minSum)
