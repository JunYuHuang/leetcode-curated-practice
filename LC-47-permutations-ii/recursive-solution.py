# O(N * !N) T and O(N * !N) S recursive backtracking (NeetCode's modded)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        def dfs(perm):
            if len(perm) >= N:
                res.append(perm[:])
                return
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    dfs(perm)
                    perm.pop()
                    count[n] += 1

        dfs([])
        return res