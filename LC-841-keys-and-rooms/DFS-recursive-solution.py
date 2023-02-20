# My O(N + M) time and O(N?) space DFS recursive solution
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()
        def dfs(room):
            if room in visit: return
            visit.add(room)
            for key in rooms[room]: dfs(key)
        dfs(0)
        return len(visit) == len(rooms)