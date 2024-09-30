# O(4^L * M * N) T and O(4^L * M * N) S recursive backtracking solution (NeetCode's modded)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        WORD_LEN = len(word)
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        if WORD_LEN > ROWS * COLS:
            return False

        def dfs(r, c, i, used):
            if i >= WORD_LEN:
                return True
            if ((r < 0 or r >= ROWS) or
                (c < 0 or c >= COLS) or
                board[r][c] != word[i] or
                (r, c) in used):
                return False
            used.add((r, c))
            for dr, dc in directions:
                nei_r = dr + r
                nei_c = dc + c
                if dfs(nei_r, nei_c, i + 1, used):
                    return True
            used.remove((r, c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != word[0]:
                    continue
                if dfs(r, c, 0, set()):
                    return True
        return False