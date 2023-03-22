# My O(N) T and O(N) S recursive with memo (DP top-down) solution
class Solution:
    def fib(self, n: int) -> int:
        memo = [0, 1]
        def helper(n):
            if n <= 1: return n
            if n < len(memo): return memo[n]
            memo.append(helper(n - 1) + helper(n - 2))
            return memo[n]
        return helper(n)