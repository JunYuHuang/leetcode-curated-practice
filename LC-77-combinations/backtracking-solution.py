# O(k * n^k) T and O(k * n^k) S recursive backtracking solution (NeetCode's modded)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i = 1, comb = []):
            if len(comb) == k:
                res.append(comb[:])
                return
            for j in range(i, n + 1):
                comb.append(j)
                dfs(j + 1, comb)
                comb.pop()

        dfs()
        return res