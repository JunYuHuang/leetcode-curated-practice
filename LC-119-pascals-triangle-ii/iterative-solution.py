# My O(N^2) T and O(rowIndex?) S solution
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for r in range(1, rowIndex + 1):
            temp = [1] * (len(res) + 1)
            for c in range(1, len(temp) - 1):
                temp[c] = res[c - 1] + res[c]
            res = temp
        return res