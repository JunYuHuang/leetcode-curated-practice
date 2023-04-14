# O(N * 2^N) T and O(N * 2^N) S recursive backtracking solution (NeetCode's expl.)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, N = [], len(nums)
        def backtrack(curr, i):
            if i == N:
                res.append(curr[:])
                return
            curr.append(nums[i])
            backtrack(curr, i + 1)
            curr.pop()
            backtrack(curr, i + 1)
        backtrack([], 0)
        return res