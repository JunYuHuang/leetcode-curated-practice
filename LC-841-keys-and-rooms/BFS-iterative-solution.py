# My O(N + M) time and O(N) space BFS iterative solution
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit, roomQ = set(), deque([0])
        while roomQ:
            room = roomQ.popleft()
            visit.add(room)
            for key in rooms[room]:
                if key in visit: continue
                roomQ.append(key)
        return len(visit) == len(rooms)