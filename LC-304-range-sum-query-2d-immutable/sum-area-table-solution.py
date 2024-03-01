# O(1) T `sumRegion()` summed area table solution (Wikipedia modded)
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.sumMat = [[0] * COLS for r in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                left = self.sumMat[r][c - 1] if c else 0
                up = self.sumMat[r - 1][c] if r else 0
                upLeft = self.sumMat[r - 1][c - 1] if r and c else 0
                areaSum = matrix[r][c] + left + up - upLeft
                self.sumMat[r][c] = areaSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        upLeft = self.sumMat[row1 - 1][col1 - 1] if row1 and col1 else 0
        upRight = self.sumMat[row1 - 1][col2] if row1 else 0
        downLeft = self.sumMat[row2][col1 - 1] if col1 else 0
        downRight = self.sumMat[row2][col2]
        return upLeft - upRight - downLeft + downRight

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
