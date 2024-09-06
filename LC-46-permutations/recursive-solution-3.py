# O(N^2 * N!) T and O(N^2 * N!) S recursive backtracking solution (NeetCode's modded)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        perms = self.permute(nums[1:])
        res = []
        for perm in perms:
            for i in range(len(perm) + 1):
                perm_copy = perm[:]
                perm_copy.insert(i, nums[0])
                res.append(perm_copy)
        return res