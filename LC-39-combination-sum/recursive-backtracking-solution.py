# O(N * 2^N) T and O(N * 2^N) S recursive backtracking solution (NeetCode's modded)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        CANDIDATES_LEN = len(candidates)
        res = []

        def dfs(i, curSub, curSum):
            if i >= CANDIDATES_LEN or curSum < 0:
                return
            if curSum == 0:
                res.append(curSub[:])
                return

            # include `candidates[i]`
            curSub.append(candidates[i])
            dfs(i, curSub, curSum - candidates[i])

            # exclude `candidates[i]`
            curSub.pop()
            dfs(i + 1, curSub, curSum)

        dfs(0, [], target)
        return res