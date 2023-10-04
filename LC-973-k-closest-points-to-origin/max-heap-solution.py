# O((N - K) * LogN) T and O(N) S max heap solution
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        maxHeap = []
        for i in range(len(points)):
            dist = -1 * (points[i][0] ** 2 + points[i][1] ** 2)
            maxHeap.append([dist, i])
        heapq.heapify(maxHeap)
        while len(maxHeap) > k:
            heapq.heappop(maxHeap)
        for e in maxHeap:
            res.append(points[e[1]])
        return res
