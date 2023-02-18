# My O(MN) time and O(MN) space BFS iterative solution
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color: return image
        ROWS, COLS = len(image), len(image[0])
        visit, q = set(), deque([(sr, sc)])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        startColor = image[sr][sc]
        while q:
            r, c = q.popleft()
            image[r][c] = color
            visit.add((r, c))
            for dr, dc in directions:
                neiR, neiC = dr + r, dc + c
                if (neiR < 0 or neiR >= ROWS or neiC < 0 or neiC >= COLS or
                    (neiR, neiC) in visit or image[neiR][neiC] != startColor):
                    continue
                q.append((neiR, neiC))
        return image