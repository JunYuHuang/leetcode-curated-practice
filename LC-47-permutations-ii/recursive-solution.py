# O(N * N!) T and O(N * N!) S recursive backtracking solution (NeetCode's modded)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, N = [], len(nums)
        nToCount = { n : 0 for n in nums }
        for n in nums: nToCount[n] += 1
        
        def backtrack(perm):
            if len(perm) == N:
                res.append(perm[:])
                return
            for n in nToCount:
                if nToCount[n] == 0: continue
                perm.append(n)
                nToCount[n] -= 1
                backtrack(perm)
                perm.pop()
                nToCount[n] += 1
        
        backtrack([])
        return res
                    