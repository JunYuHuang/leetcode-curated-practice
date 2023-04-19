# O(N ^ T) T and O(N ^ T) S recursive backtracking solution (NeetCode's modded)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, N = [], len(candidates)
        
        def backtrack(curr, currSum, i):
            if i >= N or currSum < 0: return
            if currSum == 0:
                res.append(curr[:])
                return
            curr.append(candidates[i])
            backtrack(curr, currSum - candidates[i], i)
            curr.pop()
            backtrack(curr, currSum, i + 1)
            
        backtrack([], target, 0)
        return res