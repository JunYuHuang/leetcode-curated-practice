# My O(N) T and O(N) S recursive with memo (top-down DP) solution
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1, 1, 2]
        def recurse(n):
            if n == 1 or n == 2: return n
            if n < len(memo): return memo[n]
            memo.append(recurse(n - 1) + recurse(n - 2))
            return memo[n]
        return recurse(n)