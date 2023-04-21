# O(N * 2^N) T and O(N * 2^N) S recursive backtracking solution (NeetCode's expl.)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, N = [], len(nums)
        
        def backtrack(curr, i):
            if i >= N:
                res.append(curr[:])
                return
            curr.append(nums[i])
            backtrack(curr, i + 1)
            curr.pop()
            i += 1
            while i < N and nums[i - 1] == nums[i]:
                i += 1
            backtrack(curr, i)
            
        backtrack([], 0)
        return res