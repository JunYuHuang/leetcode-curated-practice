# O(N * 2^N) T and O(N * 2^N) S recursive backtracking solution (NeetCode's expl.)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        N = len(candidates)
        res = []

        def dfs(i, comb, curSum):
            if curSum == 0:
                res.append(comb[:])
                return
            if i >= N or curSum < 0:
                return

            # include `candidates[i]`
            comb.append(candidates[i])
            dfs(i + 1, comb, curSum - candidates[i])
            comb.pop()

            # exclude `candidates[i]` and its dupes
            while i + 1 < N and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, comb, curSum)

        dfs(0, [], target)

        return res