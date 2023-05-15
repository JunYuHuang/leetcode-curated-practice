# O(9^2) T and O(9^2) S hashset solution (NeetCode's modded)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        SIDE, EMPTY_CELL = 9, "."
        rows, cols = {}, {}
        boxes = {} # represents each sub-box with key (r // 3, c // 3)

        for r in range(SIDE):
            for c in range(SIDE):
                cell = board[r][c]
                if board[r][c] == EMPTY_CELL: continue

                rows[r] = rows.get(r, set())
                cols[c] = cols.get(c, set())
                boxKey = (r // 3, c // 3)
                boxes[boxKey] = boxes.get(boxKey, set())

                if (cell in rows[r] or
                    cell in cols[c] or
                    cell in boxes[boxKey]):
                    return False

                rows[r].add(cell)
                cols[c].add(cell)
                boxes[boxKey].add(cell)
        return True
