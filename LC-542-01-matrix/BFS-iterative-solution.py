# O(MN) time and O(MN) space BFS iterative solution (hiepit's modified)
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        q = deque()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0: q.append((r, c))
                else: mat[r][c] = -1 # mark non-zero cells as unvisited / unprocessed
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                neiR, neiC = dr + r, dc + c
                if (neiR < 0 or neiR >= ROWS or 
                    neiC < 0 or neiC >= COLS or
                    mat[neiR][neiC]  != -1): 
                    continue
                mat[neiR][neiC] = mat[r][c] + 1
                q.append((neiR, neiC))
        return mat