# O(N * 2^N) T and O(N * 2^N) S recursive backtracking solution (NeetCode's expl.)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        res = []

        def dfs(i, subset):
            if i >= N:
                res.append(subset[:])
                return
            # include `nums[i]`
            subset.append(nums[i])
            dfs(i + 1, subset)

            # exclude `nums[i]`
            subset.pop()
            while i + 1 < N and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, subset)

        dfs(0, [])

        return res