# O((N - K) * LogN) T and O(N) S solution
from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distsAndPoints = [
            [-1 * self.euclidDistance(p), p] for p in points
        ]
        heapq.heapify(distsAndPoints)
        while len(distsAndPoints) > k:
            heapq.heappop(distsAndPoints)
        res = []
        for dist, point in distsAndPoints:
            res.append(point)
        return res

    def euclidDistance(self, point):
        return sqrt(point[0] ** 2 + point[1] ** 2)
