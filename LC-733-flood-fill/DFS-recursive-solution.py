# My O(MN) time and O(MN) space DFS recursive solution
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color: return image
        ROWS, COLS = len(image), len(image[0])
        visit = set()
        startColor = image[sr][sc]
        
        def dfs(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                (r, c) in visit or image[r][c] != startColor):
                return
            image[r][c] = color
            visit.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        dfs(sr, sc)
        return image