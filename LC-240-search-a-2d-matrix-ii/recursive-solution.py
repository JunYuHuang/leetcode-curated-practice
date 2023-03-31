# O(M + N) T and O(1) S iterative D&C solution (DBabichev's modded)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        r, c = 0, COLS - 1 # start at top-right cell
        while r < ROWS and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else: 
                return True
        return False