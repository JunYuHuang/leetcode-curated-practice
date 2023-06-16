# O(N) T and O(1) S sliding window (NeetCode's modded.)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0

        res = 0
        N = len(prices)
        l = 0
        r = 1
        while r < N:
            if prices[l] > prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                if profit > res: res = profit
            r += 1
        return res
