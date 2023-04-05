# O(K * N^K) T and O(K * N^K) S DFS backtracking solution (NeetCode's)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(startPos, comb):
            if len(comb) == k:
                res.append(comb[:])
                return
            for i in range(startPos, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()
        backtrack(1, [])
        return res