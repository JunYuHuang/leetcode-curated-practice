# O(1) T `sumRegion()` prefix sums solution (NeetCode's modded)
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.sumMat = [[0] * (COLS + 1) for r in range(ROWS + 1)]
        for r in range(1, ROWS + 1):
            for c in range(1, COLS + 1):
                downLeft = self.sumMat[r][c - 1]
                upRight = self.sumMat[r - 1][c]
                upLeft = self.sumMat[r - 1][c - 1]
                downRight = matrix[r - 1][c - 1]
                self.sumMat[r][c] = downRight + downLeft + upRight - upLeft

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        upLeft = self.sumMat[row1 - 1][col1 - 1]
        upRight = self.sumMat[row1 - 1][col2]
        downLeft = self.sumMat[row2][col1 - 1]
        downRight = self.sumMat[row2][col2]
        return downRight - downLeft - upRight + upLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
