# O(9^M) T and O(81) S DFS backtracking solution (msdn's modded)
class Solution:
    def __init__(self):
        self.rows = defaultdict(set)
        self.cols = defaultdict(set)
        self.squares = defaultdict(set)
        self.candidates = [str(i) for i in range(1, 10)]
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def initialScan():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".": continue
                    self.rows[r].add(board[r][c])
                    self.cols[c].add(board[r][c])
                    self.squares[(r // 3, c // 3)].add(board[r][c])
        def canPlace(r, c, val):
            return not (val in self.rows[r] or val in self.cols[c] or
                       val in self.squares[(r // 3, c // 3)])
        def placeNum(r, c, val):
            board[r][c] = val
            self.rows[r].add(val)
            self.cols[c].add(val)
            self.squares[(r // 3, c // 3)].add(val)
        def removeNum(r, c, val):
            board[r][c] = "."
            self.rows[r].remove(val)
            self.cols[c].remove(val)
            self.squares[(r // 3, c // 3)].remove(val)
        def getNextCell(r, c): 
            return [r, c + 1] if c < 8 else [r + 1, 0]
        def backtrack(r, c):
            if r == 9: return True
            if board[r][c] != ".":
                nR, nC = getNextCell(r, c)
                return backtrack(nR, nC)
            for val in self.candidates:
                if canPlace(r, c, val):
                    placeNum(r, c, val)
                    nR, nC = getNextCell(r, c)
                    if backtrack(nR, nC): return True
                    removeNum(r, c, val)
            return False
        initialScan()
        backtrack(0, 0)