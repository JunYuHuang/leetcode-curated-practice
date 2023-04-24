# O(2^N)? T and O(2^N)? S recursive backtrack solution 
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, N = [], len(candidates)
        candidates.sort()
        
        def backtrack(comb, i, currSum):
            if currSum == target:
                res.append(comb[:])
                return
            if i >= N or currSum > target: return
            comb.append(candidates[i])
            backtrack(comb, i + 1, currSum + candidates[i])
            comb.pop()
            while i + 1 < N and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(comb, i + 1, currSum)
            
        backtrack([], 0, 0)
        return res