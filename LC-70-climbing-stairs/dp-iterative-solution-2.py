# My O(N) T and O(1) S iterative with memo (bot-up DP) solution
class Solution:
    def climbStairs(self, n: int) -> int:
        nMinusTwo, nMinusOne, res = 1, 2, -1
        for i in range(3, n + 1):
            res = nMinusTwo + nMinusOne
            temp = nMinusOne
            nMinusOne = res
            nMinusTwo = temp
        return n if (n == 1 or n == 2) else res