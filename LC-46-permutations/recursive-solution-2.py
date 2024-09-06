# O(N * !N) T and O(N * !N) S recursive backtracking solution
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)

        def dfs(perm, used):
            if len(perm) == N:
                res.append(perm[:])
                return
            for n in nums:
                if n in used:
                    continue
                perm.append(n)
                used.add(n)
                dfs(perm, used)
                perm.pop()
                used.remove(n)

        dfs([], set())
        return res