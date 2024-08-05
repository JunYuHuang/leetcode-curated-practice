# O(N * 2^N) T and O(N * 2^N) S recursive backtracking solution (NeetCode's modded)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        NUMS_LEN = len(nums)

        def dfs(i, subset = []):
            if i >= NUMS_LEN:
                res.append(subset[:])
                return
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()
            dfs(i + 1, subset)

        dfs(0)

        return res