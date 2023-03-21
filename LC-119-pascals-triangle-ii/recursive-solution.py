# O(N^2) T and O(N^2) S solution (chetan_6780's modded)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        res = [1]
        prevRow = self.getRow(rowIndex - 1)
        for c in range(1, rowIndex):
            res.append(prevRow[c - 1] + prevRow[c])
        res.append(1)
        return res