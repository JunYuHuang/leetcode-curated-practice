# O(N * 2^N) T and O(N) S recursive backtracking solution (NeetCode's modded)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, N = [], len(s)
        
        def backtrack(curr, l):
            if l >= N:
                res.append(curr[:])
                return
            for r in range(l, N):
                if not self.isPali(s[l:r + 1]): continue
                curr.append(s[l:r + 1])
                backtrack(curr, r + 1)
                curr.pop()
                
        backtrack([], 0)
        return res
        
    def isPali(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]: return False
            l, r = l + 1, r - 1
        return True