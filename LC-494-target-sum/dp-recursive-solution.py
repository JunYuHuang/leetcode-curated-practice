# O(NT) time and O(NT) space DP recursive solution where T = sum(nums) (NeetCode's modified)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {} # (pos, current total sum) -> # of ways to reach target
        
        def dfs(i, curr):
            if i == len(nums):
                return 1 if curr == target else 0
            if (i, curr) in memo:
                return memo[(i, curr)]
            add = dfs(i + 1, curr + nums[i])
            minus = dfs(i + 1, curr - nums[i])
            memo[(i, curr)] = add + minus
            return memo[(i, curr)]
        return dfs(0, 0)