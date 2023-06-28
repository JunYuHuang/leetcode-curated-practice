# O(Log(M * N)) T and O(1) S binary search solution
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        top = 0
        bot = len(matrix) - 1
        midRow = 0
        while top <= bot:
            midRow = top + (bot - top) // 2
            if target < matrix[midRow][0]:
                bot = midRow - 1
            elif target > matrix[midRow][-1]:
                top = midRow + 1
            else:
                break
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            midCol = left + (right - left) // 2
            if target == matrix[midRow][midCol]:
                return True
            elif target < matrix[midRow][midCol]:
                right = midCol - 1
            else:
                left = midCol + 1
        return False
