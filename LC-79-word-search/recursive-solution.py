# O(M * N * 4^K) T and O(M * N * 4^K) S recursive backtracking solution (NeetCode's modded)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS, N = len(board), len(board[0]), len(word)
        if N > ROWS * COLS: return False
        
        visit = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def backtrack(i, r, c):
            if i == N: return True 
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                board[r][c] != word[i] or (r, c) in visit):
                return False
            visit.add((r, c))
            for dr, dc in directions:
                neiR, neiC = dr + r, dc + c
                if backtrack(i + 1, neiR, neiC): return True
            visit.remove((r, c))
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != word[0]: continue
                if backtrack(0, r, c): return True
        return False