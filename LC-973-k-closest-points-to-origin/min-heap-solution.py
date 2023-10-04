# O(KLogN) T and O(N) S min heap solution
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i in range(len(points)):
            dist = points[i][0] ** 2 + points[i][1] ** 2
            minHeap.append([dist, i])
        heapq.heapify(minHeap)
        res = []
        for _ in range(k):
            dist, i = heapq.heappop(minHeap)
            res.append(points[i])
        return res
