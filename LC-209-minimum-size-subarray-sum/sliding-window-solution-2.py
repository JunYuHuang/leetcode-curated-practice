# O(N) T and O(1) S sliding window solution (NeetCode's modded)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        currSum = 0
        INF = float("INF")
        res = INF
        numsLen = len(nums)
        for r in range(numsLen):
            currSum += nums[r]
            while currSum >= target:
                if r - l + 1 < res:
                    res = r - l + 1
                currSum -= nums[l]
                l += 1
        return 0 if res == INF else res
