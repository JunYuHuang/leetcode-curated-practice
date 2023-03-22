# My O(N) T and O(1) S iterative with memo (DP bot-up) solution
class Solution:
    def fib(self, n: int) -> int:
        nMinusTwo, nMinusOne = 0, 1
        res = -1
        for i in range(2, n + 1):
            res = nMinusOne + nMinusTwo
            temp = nMinusOne
            nMinusOne = res
            nMinusTwo = temp
        return n if n <= 1 else res