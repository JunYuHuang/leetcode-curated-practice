# O(N! * N) T and O(N^2)? S backtracking solution (NeetCode's modded)
class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        # posDiag = (r + c), negDiag = (r - c)
        col, posDiag, negDiag = set(), set(), set()
        
        def backtrack(r):
            if r == n: 
                nonlocal res
                res += 1
                return
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                backtrack(r + 1)
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
            
        backtrack(0)
        return res