# O(N^2 * N!) T and O(N^2 * N!) S iterative backtracking solution (NeetCode's modded)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    perm_copy = perm[:]
                    perm_copy.insert(i, n)
                    new_perms.append(perm_copy)
            perms = new_perms
        return perms