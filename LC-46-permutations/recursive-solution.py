# O(N * N!) T and O(N * N!) S recursive backtracking solution
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)

        def dfs(perm, cur_nums):
            if len(perm) >= N:
                res.append(perm[:])
                return
            for i in range(len(cur_nums)):
                perm.append(cur_nums[i])
                new_nums = cur_nums[:i] + cur_nums[i + 1:]
                dfs(perm, new_nums)
                perm.pop()

        dfs([], nums)
        return res