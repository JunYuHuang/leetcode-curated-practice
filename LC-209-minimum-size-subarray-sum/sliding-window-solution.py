# O(N) T and O(1) S sliding window solution
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        INF = float("INF")
        res = INF
        l = 0
        r = 0
        currSum = nums[0]
        numsLen = len(nums)
        while l <= r and r < numsLen:
            windowSize = r - l + 1
            if currSum >= target:
                if windowSize < res:
                    res = windowSize
                currSum -= nums[l]
                l += 1
            else:
                r += 1
                if r < numsLen:
                    currSum += nums[r]
        return 0 if res == INF else res
