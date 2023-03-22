# My O(N) T and O(N) S iterative with memo (DP bot-up) solution
class Solution:
    def fib(self, n: int) -> int:
        memo = [0, 1]
        for i in range(2, n + 1):
            memo.append(memo[i - 1] + memo[i - 2])
        return memo[n]